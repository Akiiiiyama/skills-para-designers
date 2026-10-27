#!/usr/bin/env python3
"""Build the video soundtrack from pieces of one track, joined on the beat.

    python3 splice_audio.py track.mp3 out.wav 64.28:79.78 75.80:78.30 133.80:end --dur 20 --fade 0.4

Each segment is source_start:source_end in seconds ("end" = end of the track). Segments are
placed back to back; each join gets an 8 ms equal-power crossfade centered on the cut, so the
total length and the beat grid stay exact. Cut only on beats (from analyze_beats.py), and never
inside one of the track's own pauses — that reads as a gap. The output is padded or trimmed to
--dur and gets a short fade at the very end (--fade).
"""
import argparse, array, os, shutil, subprocess, wave

SR = 44100
XF = int(0.008 * SR)


def ffmpeg():
    if os.environ.get('FFMPEG'):
        return os.environ['FFMPEG']
    local = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'node_modules', 'ffmpeg-static', 'ffmpeg')
    return local if os.path.exists(local) else (shutil.which('ffmpeg') or 'ffmpeg')


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('track'); ap.add_argument('out'); ap.add_argument('segments', nargs='+')
    ap.add_argument('--dur', type=float, required=True)
    ap.add_argument('--fade', type=float, default=0.4)
    args = ap.parse_args()

    raw = subprocess.run([ffmpeg(), '-v', 'error', '-i', args.track, '-ac', '2', '-ar', str(SR), '-f', 's16le', '-'],
                         check=True, capture_output=True).stdout
    a = array.array('h'); a.frombytes(raw)
    total = len(a) / 2 / SR
    half = XF / 2 / SR

    pieces = []
    for k, s in enumerate(args.segments):
        t0, t1 = s.split(':')
        t0 = float(t0); t1 = total if t1 == 'end' else float(t1)
        # widen every inner edge by half a crossfade so the cut lands exactly on the beat
        lo = t0 - (half if k > 0 else 0)
        hi = t1 + (half if k < len(args.segments) - 1 else 0)
        pieces.append(a[int(round(lo * SR)) * 2:int(round(hi * SR)) * 2])

    x = pieces[0]
    for y in pieces[1:]:
        out = x[:-XF * 2]
        for i in range(XF):
            g = i / XF
            for c in range(2):
                v = x[len(x) - XF * 2 + i * 2 + c] * (1 - g) ** 0.5 + y[i * 2 + c] * g ** 0.5
                out.append(int(max(-32768, min(32767, v))))
        out.extend(y[XF * 2:])
        x = out

    n = int(args.dur * SR)
    x = x[:n * 2]
    while len(x) < n * 2:
        x.append(0)
    f0 = int((args.dur - args.fade) * SR)
    for i in range(max(0, f0), n):
        g = (n - i) / (args.fade * SR)
        x[i * 2] = int(x[i * 2] * g); x[i * 2 + 1] = int(x[i * 2 + 1] * g)

    with wave.open(args.out, 'wb') as w:
        w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR); w.writeframes(x.tobytes())
    print(f'{args.out}: {args.dur}s from {len(args.segments)} segment(s)')


if __name__ == '__main__':
    main()
