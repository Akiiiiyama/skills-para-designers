#!/usr/bin/env python3
"""Find the real hits, tempo, sections and likely vocals of a music track.

    python3 analyze_beats.py track.mp3 [--from 55 --to 95] [--json out.json]

Prints:
  1. hits (onsets) with level and low-band level — strong hits are the kick/accents to sync cuts to;
  2. tempo candidates scored by how many strong hits land on the grid (not autocorrelation alone:
     autocorrelation locked onto 80 BPM for a 120 BPM track, a 2:3 relation);
  3. one line per bar (4 beats) with loudness, breakdown/drop marks and a vocal hint.

Needs ffmpeg (env FFMPEG, PATH, or scripts/node_modules/ffmpeg-static). No numpy.
"""
import argparse, json, math, os, shutil, subprocess, sys, array

SR = 11025
HOP = 110            # samples per envelope window (~10 ms)
STEP = HOP / SR      # seconds per window — use this, not 0.01, or times drift along the track


def ffmpeg():
    if os.environ.get('FFMPEG'):
        return os.environ['FFMPEG']
    local = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'node_modules', 'ffmpeg-static', 'ffmpeg')
    return local if os.path.exists(local) else (shutil.which('ffmpeg') or 'ffmpeg')


def decode(path):
    raw = subprocess.run([ffmpeg(), '-v', 'error', '-i', path, '-ac', '1', '-ar', str(SR), '-f', 's16le', '-'],
                         check=True, capture_output=True).stdout
    a = array.array('h'); a.frombytes(raw)
    return a


def db(x):
    return 10 * math.log10(x + 1e-12)


def features(a):
    """Per 10 ms window: total level, low band (<~150 Hz, kick) and voice band (300–3000 Hz)."""
    w = HOP
    c_low = 1 - math.exp(-2 * math.pi * 150 / SR)
    c_300 = 1 - math.exp(-2 * math.pi * 300 / SR)
    c_3k = 1 - math.exp(-2 * math.pi * 3000 / SR)
    lo = l3 = l3k = 0.0
    tot, low, mid = [], [], []
    for i in range(0, len(a) - w, w):
        s = sl = sm = 0.0
        for v in a[i:i + w]:
            v /= 32768
            lo += c_low * (v - lo); l3 += c_300 * (v - l3); l3k += c_3k * (v - l3k)
            m = l3k - l3
            s += v * v; sl += lo * lo; sm += m * m
        tot.append(s / w); low.append(sl / w); mid.append(sm / w)
    return tot, low, mid


def find_hits(tot, low):
    env = [db(x) for x in tot]
    hits = []
    for k in range(3, len(env)):
        if env[k] - min(env[k - 3:k]) > 12 and env[k] > -16:
            t = k * STEP
            if not hits or t - hits[-1]['t'] > 0.15:
                hits.append({'t': round(t, 2), 'db': round(env[k], 1), 'low': round(db(low[k]), 1)})
    if hits:
        lows = sorted(h['low'] for h in hits)
        cut = lows[int(len(lows) * 0.9)] - 5      # kicks/accents: within 5 dB of the loudest low hits
        for h in hits:
            h['strong'] = h['low'] >= cut
    return hits


def tempo(hits, lo_bpm=70, hi_bpm=170, tol=0.025, span=8.0, window=(0, 1e9)):
    """Score each beat length by the share of nearby strong-hit pairs (< span s apart) whose distance
    is a whole number of beats. Local pairs tolerate slow tempo drift over a long track."""
    strong = [h['t'] for h in hits if h.get('strong')]
    if len(strong) < 4:
        return []
    pairs = [strong[j] - strong[i] for i in range(len(strong)) for j in range(i + 1, len(strong))
             if strong[j] - strong[i] < span]
    if not pairs:
        return []
    inside = [h for h in hits if h.get('strong') and window[0] <= h['t'] <= window[1]] or [h for h in hits if h.get('strong')]
    anchor = max(inside, key=lambda h: h['low'])['t']
    cands = []
    p = 60 / hi_bpm
    while p <= 60 / lo_bpm:
        on = 0
        for dt in pairs:
            d = dt % p
            if min(d, p - d) < tol:
                on += 1
        cands.append((on / len(pairs), p))
        p += 0.0005
    cands.sort(reverse=True)
    out = []
    for frac, p in cands:
        if all(abs(p - q) > 0.01 for _, q in out):
            out.append((frac, p))
        if len(out) == 4:
            break
    return [{'bpm': round(60 / p, 1), 'beat': round(p, 4), 'fit': round(f, 2), 'anchor': anchor} for f, p in out]


def bars(tot, mid, beat, anchor, duration):
    """One row per bar (4 beats) aligned to the anchor hit."""
    bar = 4 * beat
    start = anchor - math.floor(anchor / bar) * bar
    rows = []
    t = start
    while t + bar <= duration:
        i, j = int(t / STEP), int((t + bar) / STEP)
        e = sum(tot[i:j]) / max(1, j - i); m = sum(mid[i:j]) / max(1, j - i)
        rows.append({'t': round(t, 2), 'db': round(db(e), 1), 'mid': round(db(m), 1), 'voice_ratio': round(db(m) - db(e), 1)})
        t += bar
    if rows:
        levels = sorted(r['db'] for r in rows); med = levels[len(levels) // 2]
        ratios = sorted(r['voice_ratio'] for r in rows); rmed = ratios[len(ratios) // 2]
        for k, r in enumerate(rows):
            r['breakdown'] = r['db'] < med - 6
            r['drop'] = k > 0 and rows[k - 1]['db'] < med - 6 and r['db'] >= med - 3
            # voice band (300–3000 Hz) unusually strong, or jumping more than the mix vs. the same spot one phrase (2 bars) earlier
            jump = k >= 2 and r['mid'] - rows[k - 2]['mid'] > 4 and (r['mid'] - rows[k - 2]['mid']) - (r['db'] - rows[k - 2]['db']) > 1.5
            r['voice?'] = r['db'] > -40 and (r['voice_ratio'] > rmed + 3 or jump)
    return rows


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('track')
    ap.add_argument('--from', dest='t0', type=float, default=0)
    ap.add_argument('--to', dest='t1', type=float, default=1e9)
    ap.add_argument('--json')
    args = ap.parse_args()

    a = decode(args.track)
    duration = len(a) / SR
    tot, low, mid = features(a)
    hits = find_hits(tot, low)

    print(f'duration {duration:.2f}s')
    print('\n== hits (★ = strong: sync cuts to these)')
    for h in hits:
        if args.t0 <= h['t'] <= args.t1:
            print(f"  {h['t']:8.2f}s  {h['db']:6.1f} dB  low {h['low']:6.1f} dB  {'★' if h.get('strong') else ''}")

    cands = tempo(hits, window=(args.t0, args.t1))
    print('\n== tempo candidates (fit = share of strong hits on the grid)')
    for c in cands:
        print(f"  {c['bpm']:6.1f} BPM  beat {c['beat']:.4f}s  fit {c['fit']:.2f}")
    if not cands:
        print('  not enough strong hits'); return
    best = cands[0]
    print(f"  → using {best['bpm']} BPM, anchored on the strongest hit at {best['anchor']}s."
          ' Check: strong hits should fall on whole or half beats of this grid.')

    rows = bars(tot, mid, best['beat'], best['anchor'], duration)
    print('\n== bars (4 beats). breakdown = much quieter than usual · DROP = beat comes back · voice? = heuristic, listen to confirm')
    for r in rows:
        if args.t0 - 4 * best['beat'] <= r['t'] <= args.t1:
            tags = ' '.join(x for x, on in (('breakdown', r['breakdown']), ('DROP', r['drop']), ('voice?', r['voice?'])) if on)
            bar = '#' * int(max(0, 40 + r['db']))
            print(f"  {r['t']:8.2f}s  {r['db']:6.1f} dB  {bar:<32} {tags}")

    if args.json:
        json.dump({'duration': duration, 'hits': hits, 'tempo': cands, 'bars': rows}, open(args.json, 'w'), indent=1)
        print(f'\njson → {args.json}')


if __name__ == '__main__':
    sys.exit(main())
