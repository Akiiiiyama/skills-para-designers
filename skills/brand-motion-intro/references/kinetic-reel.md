# Recipe: kinetic-type role reel ("Design Engineer" reel)

A second recipe for this skill, different from the hero-object intro in `SKILL.md`. It is a 14 s reel that says **who you are and how you work** through kinetic type, hard background cuts on the beat and small artifacts of your craft. Built from a real project: [`examples/de-reel/scene.html`](../examples/de-reel/scene.html) (9:16, 1080×1920) and [`examples/de-reel/scene-wide.html`](../examples/de-reel/scene-wide.html) (16:9, 1920×1080), both rendered at 2× to 2160×3840 and 3840×2160.

Use it when the person shares a fast "creative director" style reel (type that changes on every beat, flat color backgrounds, quick montage) and wants it to speak about a role, such as Design Engineer.

## 1. Brief

Ask, in one round:

| Ask | Example answer |
|---|---|
| Reference reel | A creative-direction reel with type on beats and a fast montage |
| Role to land on | Design Engineer |
| Roles to pass through, **in order** | Design Engineer → Product Designer |
| Name, as it should be typed | Isabela Yukari |
| One principle line, in two halves | "I design in **pixels**" / "and ship in **code**." |
| Skills for the wheel | Design Systems, Prototyping, Motion, Accessibility, Design Tokens, React… |
| Brand tokens | `#141414` ink, `#FFFFFF`, `#F2F2F2`, `#C8102E` accent, `#8A8A8A`; DM Sans + JetBrains Mono; `cubic-bezier(.16,1,.3,1)` |
| Formats | 9:16 for Reels first, then 16:9 for desktop/portfolio |
| Music | A licensed track; you will use only the part **before the vocals start** |

Don't copy the reference. Translate its **grammar** (beat cuts, light/bold type pairs, mono labels, a fast montage) into the person's craft: in the example, every scene shows design and code side by side.

## 2. Structure: seven scenes on the beat grid

There is no time warp in this recipe. Scene time **is** music time, and every scene starts on a beat. First find the tempo and the strong hits (`scripts/analyze_beats.py`), then write the beat grid at the top of the scene:

```js
const B = 0.46154, BEAT = (k) => 0.405 + k * B;      // 130 BPM, first beat at 0.405 s
const T = { hello: 0.75, name: 2.251, roles: 4.558, meta: 8.712, meta2: 9.635, wheel: 10.097, mont: 11.482, end: 12.404 };
```

The strong hits in this track were 2.251 · 5.02 · 8.712 · 12.404. Put the big changes (name, principle, final) on them.

| # | Scene | Starts | What happens | Design ↔ code idea |
|---|---|---|---|---|
| A | **Hello.** | 0 | Dark grid with crosshairs draws in; a red text caret types "Hello" and turns into the period | Figma-style selection box with `x y W H` above and `font: 700 170px "DM Sans";` below |
| B | **I'm + name** | 2.251 (hit) | Hard cut to white; "I'm" rises from a mask; the name is typed as a light/bold pair, then shrinks away | Typing = building |
| C | **Roles** | 4.558 | One role per block of beats, each on its own background: Design **Engineer** on red, then Product **Designer** on light gray | Mono label `ROLE 01 / 02` |
| D | **Principle** | 8.712 (hit) | "I design in **pixels**" with six design-tool icons orbiting; on the next beat "and ship in **code**." and each icon morphs into a code icon | The whole thesis in one beat |
| E | **Skills wheel** | 10.097 | "I ship •" and a 3D-ish list that turns one item per beat; the active item is red and bold | |
| F | **Craft montage** | 11.482 | Eight full-screen artifacts of the logo, one per ~0.115 s: tokens sheet, code editor, spacing redlines, dark toggle, button states, responsive frames, AA contrast badge, git commit | Proof of craft, too fast to read, slow enough to recognize |
| G | **Close** | 12.404 (hit) | Name in light/bold; the red dot lands as the period with a spring; mono tag `DESIGN ENGINEER — 2026` is typed; fade out 13.6–14 s | The dot that started as the caret ends as the period |

The **red dot** is the thread: caret in A and B, period in A and G. It is one element (`#dot`) positioned from measured text (a zero-size `vertical-align: baseline` span after the last letter), never from hard-coded numbers.

## 3. Build rules for this recipe

- **One `.scene` per section**, toggled with `visibility` from `render(t)`. Background and text color are set per scene in one place at the top of `render(t)`, as hard cuts on the beat.
- **Light/bold pairs**: `<span class="lt">Design </span><span class="bd">Engineer</span>` (300 vs 700). One family for display, mono only for labels and code.
- **Mask reveals**: `.mask { overflow:hidden; padding:0 0.08em 0.18em; margin:0 -0.08em -0.18em }` and slide the inner span with `translateY(110% → 0)`. The padding keeps descenders and tight tracking from being clipped.
- **Typing**: a pure function that slices the text by a character count from `prog(t, a, b)`; a blinking caret is `Math.floor(t / 0.265) % 2`.
- **Springs** for landings (`1 - e^(-8x)·cos(15x)`), `OUT` easing for entrances, hard cuts between scenes.
- **Labels**: `HELLO 00 / 05`, `ROLE 01 / 02`, `SKILLS 11` in mono at the top corners, hidden during the montage.
- **Instagram safe area (9:16)**: keep labels at `top: 300px` and main type between ~700 and ~1450 px; the app UI covers the top and bottom.

## 4. Music: the intro before the vocals

1. Analyse the track and list where the **voice** starts (`analyze_beats.py` flags `voice?` bars). In the example the vocals start at ~14.2 s, so the reel is 14 s long and uses 0:00–0:14.
2. Listen for single **spoken words** inside the intro. The example had one at ~10.4–11.3 s. Replace that stretch with an identical stretch from earlier in the intro, cut exactly on beats:

```bash
python3 scripts/splice_audio.py track.mp3 audio.wav 0:10.097 6.405:7.790 11.482:14 --dur 14 --fade 0.45
```

3. Never start the music later in the track to "skip" the vocals: people expect the song's real opening.

## 5. Review, then render

```bash
cd scripts
WIDTH=1080 HEIGHT=1920 node render.cjs ../examples/de-reel/scene.html stills 1.2 3.5 5.5 7.5 9.3 10.3 11.55 13.3
WIDTH=1080 HEIGHT=1920 SCALE=2 CRF=12 STABLE=1 DUR=14 node render.cjs ../examples/de-reel/scene.html video silent.mp4
python3 scan_flicker.py silent.mp4
ffmpeg -i silent.mp4 -i audio.wav -map 0:v -map 1:a -c:v copy -c:a aac -b:a 320k -shortest -movflags +faststart reel-4k.mp4
```

- Preview at 1× first (about 5 minutes for 840 frames); render 2× only after the person approves.
- `STABLE=1` re-captures a frame until two screenshots match. Use it for every final render.

## 6. Desktop version (16:9)

Re-compose; don't crop. In the example only positions changed (see `scene-wide.html`):

- page `1920×1080`, `.center` width 1920, grid columns/rows re-spaced;
- main type moved from ~860 px to ~460 px from the top; labels to `top: 64px` (no app UI to avoid);
- orbiting icons on a wide ellipse (`rx 620, ry 330`) around the centered line;
- each montage tile re-laid out around the vertical center.

```bash
WIDTH=1920 HEIGHT=1080 SCALE=2 CRF=12 STABLE=1 DUR=14 node render.cjs ../examples/de-reel/scene-wide.html video silent-wide.mp4
```

## 7. Iterating with the person

- **Change only what was asked.** In the example, a request for slower roles in a new order was first answered by also removing the skills wheel and half of the montage. The person had liked those, and the work was redone. If a change needs time taken from another scene, ask before cutting.
- Keep every delivered version (`-v2`, `-v3`) and the scene source **in a repository**, not in a temporary folder. Temporary folders are wiped, and the scene is the only editable source of the video.
- When asked about colors, recommend staying inside the brand: ink + white + one saturated accent (~10% of the screen), gray as support.

## Checklist

- [ ] Beat grid written at the top of the scene; every scene starts on a beat, big changes on strong hits
- [ ] Roles in the order the person gave
- [ ] One thread element (the red dot) from the first to the last scene
- [ ] Each scene shows design and code side by side
- [ ] Music: only the intro before vocals; spoken words replaced on beats
- [ ] 9:16 safe area respected; 16:9 re-composed, not cropped
- [ ] Contact sheet reviewed; `scan_flicker.py` reports 0 on the final render
- [ ] Scene sources committed to a repository
