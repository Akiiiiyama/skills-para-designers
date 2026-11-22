#!/usr/bin/env python3
"""Find one-frame glitches (flashes, missing layers) in a rendered video.

    python3 scan_flicker.py video.mp4 [--fps 60]

A frame is flagged when it differs a lot from both neighbours while the neighbours look alike —
the signature of a capture glitch, not of real motion. Exits 1 if anything is found.
Run it on every render before delivering; look at the flagged frames before re-rendering.
"""
import argparse, os, shutil, subprocess, sys

W, H = 96, 54


def ffmpeg():
    if os.environ.get('FFMPEG'):
        return os.environ['FFMPEG']
    local = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'node_modules', 'ffmpeg-static', 'ffmpeg')
    return local if os.path.exists(local) else (shutil.which('ffmpeg') or 'ffmpeg')


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('video'); ap.add_argument('--fps', type=float, default=60)
    args = ap.parse_args()
    raw = subprocess.run([ffmpeg(), '-v', 'error', '-i', args.video, '-vf', f'scale={W}:{H},format=gray',
                          '-f', 'rawvideo', '-'], check=True, capture_output=True).stdout
    n = W * H
    fr = [raw[i:i + n] for i in range(0, len(raw) - n + 1, n)]
    diff = lambda a, b: sum(abs(a[i] - b[i]) for i in range(n)) / n
    bad = []
    for k in range(1, len(fr) - 1):
        dab, dbc = diff(fr[k - 1], fr[k]), diff(fr[k], fr[k + 1])
        if dab > 2 and dbc > 2 and diff(fr[k - 1], fr[k + 1]) < dab * 0.4:
            bad.append(k)
    for k in bad:
        print(f'glitch at {k / args.fps:.3f}s (frame {k})')
    print(f'{len(fr)} frames, {len(bad)} glitch(es)')
    return 1 if bad else 0


if __name__ == '__main__':
    sys.exit(main())
