# brand-motion-intro — how to use

*[Leia em português](README.pt.md)*

A Claude Code skill that turns a one-line message, your design system and a music track into a 10–20 s motion video (MP4) with every transition on the beat. This page is for **people using the skill**; [`SKILL.md`](SKILL.md) is what Claude reads.

## 1. Requirements

| You need | Check |
|---|---|
| [Claude Code](https://claude.com/claude-code) (CLI, desktop app or IDE extension) | `claude --version` |
| Node.js 20+ | `node -v` |
| Python 3.9+ (no extra packages) | `python3 --version` |
| Google Chrome (used headless to record frames) | macOS default path, or set `CHROME=/path/to/chrome` |
| ffmpeg | installed by step 2, or your own on `PATH` |

## 2. Install

**a. Make the skill available to Claude Code.** Copy (or link) the skill folder into your personal skills folder:

```bash
mkdir -p ~/.claude/skills
```

```bash
cp -R skills/brand-motion-intro ~/.claude/skills/
```

To use it in a single project only, copy it to `<project>/.claude/skills/` instead. To keep it in sync with this repo, use a symlink: `ln -s "$PWD/skills/brand-motion-intro" ~/.claude/skills/brand-motion-intro`.

**b. Install the render scripts' dependencies** (puppeteer-core + ffmpeg-static):

```bash
cd ~/.claude/skills/brand-motion-intro/scripts && npm install
```

If npm blocked install scripts and `node_modules/ffmpeg-static/ffmpeg` doesn't exist, download the binary once:

```bash
cd ~/.claude/skills/brand-motion-intro/scripts/node_modules/ffmpeg-static && node install.js
```

**c. Restart Claude Code** (or open a new session) so it picks up the skill.

## 3. Prepare your material

1. **Your message as one sentence with commas** — each comma becomes a transition. Example: `Hi, I'm IY., Isabela Yukari, Design Engineer`.
2. **A reference** (link, screenshots or a description) of the motion style you like.
3. **Your brand**: a repo with your site/design system, a Figma file, or at least hex colors, fonts and the logo.
4. **Format and length**: 16:9 (feed, YouTube, portfolio) or 9:16 (Stories/Reels); 12–20 s.
5. **A music file you have a license for** (MP3/WAV), saved on your computer.

## 4. Use it

Open Claude Code in any folder (ideally the repo with your design system) and ask in plain language — the skill triggers on requests like "make a motion video like this reference". You can also call it by name: `/brand-motion-intro`.

Example request:

> Make a 20s 16:9 motion video in the style of this reference: <link>. Text: "Hi, I'm IY., Isabela Yukari, Design Engineer" — each comma is a transition. Use the design system in ~/Portfolio. Mood: futuristic glassmorphism, but sweet. Music: ~/Downloads/track.mp3.

What happens next:

1. **Brief** — Claude asks only what's missing (format, mood, music, light or dark).
2. **Strategy** — it proposes the narrative arc and a hero object that closes the loop in your logo. Approve or redirect it.
3. **Stills** — you get a contact sheet with 9–12 key frames. This is the cheapest moment to change direction.
4. **Adjustments** — ask in text: "lighter palette", "slower words", "make the ball become the dot of the logo at the end".
5. **Music sync** — Claude finds the tempo, the drop and sections with vocals, splices the track on the beat and pins each transition to a hit.
6. **Render** — 60 fps MP4 (≈ 3 frames/s, so a 20 s video takes ~7 min), then an automatic scan for glitched frames.
7. **Delivery** — the MP4 in a folder you choose (e.g. `~/Movies`), plus what was and wasn't checked.

Useful follow-ups: "also make a 9:16 Stories version", "render in 4K" (`SCALE=2`), "export a version with sound effects only so I can add music on Instagram".

## 5. Run the scripts yourself (optional)

From `scripts/`:

```bash
node render.cjs ../templates/scene.html stills 1 2 3 4
```

```bash
python3 analyze_beats.py ~/Downloads/track.mp3 --from 50 --to 100
```

```bash
python3 splice_audio.py ~/Downloads/track.mp3 audio.wav 64.28:79.78 133.80:end --dur 20
```

```bash
WARP=1 DUR=20 node render.cjs ../templates/scene.html video silent.mp4
```

```bash
python3 scan_flicker.py silent.mp4
```

Then mux: `ffmpeg -i silent.mp4 -i audio.wav -map 0:v -map 1:a -c:v copy -c:a aac -shortest final.mp4`.

## 6. Tips and troubleshooting

| Situation | What to do |
|---|---|
| The reference is an Instagram post | Send screenshots or describe it — Claude usually can't play it without a login. |
| You can't download the music | Ask for a version with sound effects only and add the track in Instagram's music library. |
| The video feels too fast | Ask for at least 1.5 s per phrase; the time warp stretches scenes without re-animating. |
| A one-frame blink in the video | Ask Claude to run `scan_flicker.py` and fix the flagged frames before delivery. |
| Vocals over the text | Ask for an instrumental section; listen to confirm. |
| `Chrome not found` | Set `CHROME` to your Chrome path. |
| `ffmpeg: not found` | Run step 2b, or install ffmpeg and make sure it's on `PATH`. |

**Music rights:** publishing requires a license that covers the platform. The skill never downloads tracks from stock libraries for you.
