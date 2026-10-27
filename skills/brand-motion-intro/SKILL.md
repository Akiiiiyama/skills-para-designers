---
name: brand-motion-intro
description: Plans and produces a short personal-brand motion video (10–20 s intro for Instagram, LinkedIn or a portfolio) from a one-line message, the person's design system and a licensed music track — code-rendered to MP4 with every transition on the beat. Use when someone wants a "video like this reference", a motion intro, a brand reel or a portfolio teaser.
---

# Brand motion intro

A strategic workflow for a 10–20 s motion video that introduces a person or brand: kinetic type, one hero object that carries the story, the brand's own palette and easing, and cuts locked to the music. The scene is an HTML page rendered frame by frame (headless Chrome → ffmpeg), so every detail is editable by text and re-renders in minutes.

Built from a real project: [`examples/iy-intro/scene.html`](examples/iy-intro/scene.html) — "Hi, I'm IY., Isabela Yukari, Design Engineer", 20 s, 60 fps, synced to a 120 BPM track.

## When to use

- The person shares a reference reel ("I want a video in this style") or asks for a motion intro, brand reel, portfolio teaser or animated signature.
- They have (or can point to) a brand: logo, colors, type — ideally a design system in a repo or Figma.
- Not for long-form editing of filmed footage, or for videos that need a real person on camera.

## Steps

### 1. Brief (ask before building)

Get answers to these, in one round of questions. Everything else has a sensible default.

| Ask | Why | Default |
|---|---|---|
| **The message**, as one line with commas | Each comma becomes a transition. "Hi, I'm IY., Isabela Yukari, Design Engineer" = 3 phrases + brand close. | — (required) |
| **Reference** (link or description) | Extract pacing, transitions and mood — not to copy it. If the link is behind a login, ask for screenshots or a description. | — |
| **Brand source**: repo, Figma, site | Tokens, fonts, logo, easing curves. | Ask for hex colors + font |
| **Format and length** | 16:9 1920×1080 (feed/YouTube/portfolio) or 9:16 1080×1920 (Stories/Reels). | 16:9, 12–20 s |
| **Mood** in two words, e.g. "futuristic + sweet" | Drives palette use, motion weight and music. | — |
| **Music**: a track file they licensed | You sync cuts to it. You can't download from stock libraries for them. | Ask; offer a version with only sound effects so they can add music in the app |
| **Deliverable** | MP4 only, or MP4 + editable scene. | MP4 |

### 2. Strategy (write it down before any code)

1. **Narrative arc** — five beats: *hook* (something draws itself) → *identity* (name) → *symbol* (a metaphor for how they work) → *role* (what they do) → *brand close* (logo).
2. **One hero object that closes the loop.** Pick an element of the logo (a dot, a letter, a shape) and let it travel the whole video. In the example: the red dot of "IY." falls → grows into a glass sphere → becomes the iris of an eye → returns to the right as a sphere → shrinks back into the dot of the logo. Loops make a 15 s video feel designed, not assembled.
3. **The symbol** (middle of the video) — a visual metaphor the person relates to (an eye for "design vision"). If it touches identity or culture (e.g. an almond-shaped East Asian eye, katakana, ensō, hanko), draw it with care: elegant line work, no caricature, and only because the person asked for it or it is part of their identity.
4. **Commas = transitions.** List them and decide what carries each one (the hero morphs, a blink, a glass panel sweep, a text blur-out).
5. **Pace for reading.** Each phrase stays fully readable ≥ 1.5 s. People asked for "slower" in the example; 20 s for 3 phrases + close felt right.

### 3. Extract the brand

From the repo/Figma, copy into `:root` tokens: background, ink, accent, muted gray, line color; font families and weights; the easing curve (e.g. `cubic-bezier(.16,1,.3,1)`); logo construction (e.g. "IY" + red dot); existing motion (an intro animation in the site is gold — reuse its gestures). Screenshot the home page if it will appear in the video.

If the brand is light, keep the video light — a dark "futuristic" default fights a white portfolio.

### 4. Storyboard in scene time

Write a table: scene time (s) → what moves. Start with the original pacing (~12 s); you will stretch it to the music later with the time warp, so don't tune seconds yet.

### 5. Build the scene

Copy [`templates/scene.html`](templates/scene.html). Rules:

- `render(t)` is a **pure function** of time. No CSS transitions/animations, no `setTimeout`, no `Date.now()`. Same `t` → same frame.
- One DOM element per moving thing; set `transform`/`opacity`/`clip-path` from `t` with `prog()`, `OUT`/`INOUT`, `drop()`.
- Give every animated element the `.anim` class (`will-change: transform, opacity, filter`) so its layer exists from frame 0.
- Text reveals: wrap words in `.mask` and slide the inner span (`translateY(110% → 0)` or `translateX(60% → 0)`).
- The hero is one element for the whole video; morph it with position/size/opacity of its layers.
- Measure layout once in `layout()` after fonts load (e.g. where the logo dot sits) — never hard-code glyph positions.
- Expose `window.ready` (fonts + images loaded), `window.render`, and `window.renderV` (warped).

### 6. Review with contact sheets, then iterate

```bash
cd scripts && npm install          # puppeteer-core + ffmpeg-static (see Pitfalls if ffmpeg is missing)
node render.cjs ../path/scene.html stills 1.0 2.3 3.5 5.0 6.4 7.8 9.2 11.5
ffmpeg -pattern_type glob -i '../path/stills/t-*.png' -vf "scale=640:360,tile=3x3" -frames:v 1 sheet.png
```

Read the sheet image yourself and fix composition before showing anything. Show the person stills or a sheet for direction changes; full renders take minutes.

### 7. Music: find the real beat

```bash
python3 scripts/analyze_beats.py track.mp3 --from 50 --to 100
```

- Trust the **list of strong hits**, not only the tempo guess. Check that strong hits fall on whole/half beats of the chosen BPM. (Autocorrelation alone locked onto 80 BPM for a 120 BPM track and every cut landed off-beat.)
- Choose a window of the video's length that contains a **drop** (the beat comes back after a breakdown): put the first transition on it.
- Avoid bars flagged `voice?` — then **listen** to confirm. People notice vocals that fight the text.
- Prefer the track's **real ending** for the close; splice to it instead of fading mid-phrase.

```bash
python3 scripts/splice_audio.py track.mp3 audio.wav 64.28:79.78 75.80:78.30 133.80:end --dur 20 --fade 0.4
```

Cut only on beats and never inside one of the track's own pauses (a silence before a big hit) — a pause without its hit reads as a gap.

### 8. Time-warp the scene to the music

Edit `WARP` in the scene: pairs `[video time, scene time]`. Pin each transition (scene time) to a strong hit (video time) and the scene stretches between them. Pair a hit with the hero's landings (dot lands, eye blinks, logo forms).

### 9. Render, scan, mux

```bash
WARP=1 DUR=20 FPS=60 node scripts/render.cjs scene.html video silent.mp4     # SCALE=2 → 4K from a 1080p scene
python3 scripts/scan_flicker.py silent.mp4                                   # must report 0 glitches
ffmpeg -i silent.mp4 -i audio.wav -map 0:v -map 1:a -c:v copy -c:a aac -b:a 256k -ar 48000 -shortest final.mp4
```

Look at any flagged frame before re-rendering. Rendering is ~3 frames/s: run long renders in the background.

### 10. Deliver

- Save to a folder the person can open (e.g. `~/Movies/`), reveal it, and say what changed and what you did **not** verify (e.g. "not listened to in real time").
- Stories/Reels: render a 9:16 scene (1080×1920) — re-compose, don't crop the 16:9 one.
- Instagram: the account must hold the music license (or connect the stock library); for in-app music, deliver a version with sound effects only and a silent one.

## Checklist

- [ ] Message split by commas; each comma has a named transition
- [ ] One hero object that starts and ends the video (loop closed in the logo)
- [ ] Tokens, fonts and easing copied from the real design system
- [ ] Cultural/identity elements requested by the person and drawn without caricature
- [ ] Each phrase readable ≥ 1.5 s
- [ ] Tempo checked against the strong-hit list; transitions on strong hits
- [ ] No vocals in the chosen window (listened); ending is musical, no gap at splices
- [ ] Contact sheet reviewed before the full render
- [ ] `scan_flicker.py` reports 0 glitches on the final render
- [ ] Final MP4 checked (duration, 60 fps, audio stream) and revealed to the person

## Pitfalls (all hit in the example project)

- **`backdrop-filter` flickers in headless Chrome**: some frames render the glass layer blank. Fake glass with gradients + borders + shadows instead.
- **One-frame glitches (torn or half-drawn frame)**: Chrome creates a compositing layer the first time an element gets a blur, an opacity change, etc., and a capture during that frame comes out broken. Fix both ways: `will-change: transform, opacity, filter` on every animated element (the `.anim` class), and wait two `requestAnimationFrame`s after `render(t)` before each screenshot (`render.cjs` does this). Verified: the template glitched at 4.0 s without `will-change` and rendered clean twice with it.
- **Fonts**: `document.fonts.ready` doesn't fetch glyphs that aren't on the page yet. Call `document.fonts.load()` for every family/weight (and for CJK fonts like Noto Sans JP, with the exact characters).
- **Inline styles with two `display` declarations**: the last one wins — `display:none` earlier in the same `style` attribute does nothing. Hide things from `render(t)`.
- **Glyph-based positions**: measure the logo's dot from a hidden `.` span and calibrate once with a zoomed still; text metrics differ by font.
- **ffmpeg-static without the binary**: if npm blocked install scripts, run `node node_modules/ffmpeg-static/install.js` once.
- **Instagram/login walls**: reference posts often won't play without login; ask for screenshots instead of fighting it.
- **Dark vs. brand**: confirm light/dark with the person before building; it's the most expensive thing to change later.

## Examples

- [`examples/iy-intro/scene.html`](examples/iy-intro/scene.html) — full scene: blueprint guides, "Hi, I'm IY." with falling letters, dot → glass sphere with ensō, almond eye that looks around and blinks (the middle transition), "Design Engineer" with glass chips, sphere → logo dot. Vertical katakana per phrase. `WARP` pinned to a 120 BPM track: drop at 4.5 s, blink at 12.45 s, dot lands at 16.45 s.
- [`templates/scene.html`](templates/scene.html) — minimal starting point with the same structure (6 s, one phrase, hero → logo dot).
