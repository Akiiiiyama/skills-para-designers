// Renders an HTML scene frame by frame and encodes it with ffmpeg.
//
//   node render.cjs <scene.html> stills 1.0 2.5 4.0   → <scene dir>/stills/t-1.00.png …
//   node render.cjs <scene.html> video out.mp4        → silent H.264 MP4
//
// The scene must expose window.ready (a Promise) and window.render(t) — or window.renderV(t)
// when WARP=1 (time-warped to the music). render(t) must be a pure function of t.
//
// Env: DUR (s, default 12) · FPS (default 60) · WIDTH/HEIGHT (CSS px, default 1920×1080)
//      SCALE (device pixel ratio: 2 → 3840×2160 from a 1920×1080 scene) · WARP=1 · CRF (default 14)
//      CHROME (path to Chrome; default macOS location)
const puppeteer = require('puppeteer-core');
const { spawn } = require('child_process');
const fs = require('fs');
const path = require('path');

const [sceneArg, mode, ...rest] = process.argv.slice(2);
if (!sceneArg || !['stills', 'video'].includes(mode)) {
  console.error('usage: node render.cjs <scene.html> stills <t…> | video <out.mp4>');
  process.exit(1);
}
const scene = path.resolve(sceneArg);
const DUR = Number(process.env.DUR || 12);
const FPS = Number(process.env.FPS || 60);
const W = Number(process.env.WIDTH || 1920), H = Number(process.env.HEIGHT || 1080);
const SCALE = Number(process.env.SCALE || 1);
const FN = process.env.WARP ? 'renderV' : 'render';
const CHROME = process.env.CHROME || '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome';

function ffmpegPath() {
  if (process.env.FFMPEG) return process.env.FFMPEG;
  try { return require('ffmpeg-static'); } catch { return 'ffmpeg'; }
}

// Wait for two animation frames so the compositor has painted the state set by render(t).
// Without this, a frame is sometimes captured mid-paint (a one-frame flash in the video).
const settle = (page) => page.evaluate(() => new Promise((r) => requestAnimationFrame(() => requestAnimationFrame(r))));

(async () => {
  const browser = await puppeteer.launch({
    executablePath: CHROME,
    headless: 'new',
    args: ['--allow-file-access-from-files', '--force-color-profile=srgb'],
  });
  const page = await browser.newPage();
  await page.setViewport({ width: W, height: H, deviceScaleFactor: SCALE });
  await page.goto('file://' + scene, { waitUntil: 'networkidle0' });
  await page.evaluate(() => window.ready);

  if (mode === 'stills') {
    const dir = path.join(path.dirname(scene), 'stills');
    fs.mkdirSync(dir, { recursive: true });
    for (const t of rest.map(Number)) {
      await page.evaluate((fn, t) => window[fn](t), FN, t);
      await settle(page);
      await page.screenshot({ path: path.join(dir, `t-${t.toFixed(2)}.png`) });
    }
    console.log(`${rest.length} stills → ${dir}`);
  } else {
    const out = path.resolve(rest[0] || 'silent.mp4');
    const n = Math.round(DUR * FPS);
    const ff = spawn(ffmpegPath(), ['-y', '-v', 'error', '-f', 'image2pipe', '-framerate', String(FPS), '-i', '-',
      '-c:v', 'libx264', '-preset', 'slow', '-crf', String(process.env.CRF || 14),
      '-pix_fmt', 'yuv420p', '-movflags', '+faststart', out], { stdio: ['pipe', 'ignore', 'inherit'] });
    for (let i = 0; i < n; i++) {
      await page.evaluate((fn, t) => window[fn](t), FN, i / FPS);
      await settle(page);
      const buf = await page.screenshot({ type: 'png' });
      if (!ff.stdin.write(buf)) await new Promise((r) => ff.stdin.once('drain', r));
      if (i % FPS === 0) console.log(`frame ${i}/${n}`);
    }
    ff.stdin.end();
    await new Promise((r) => ff.on('close', r));
    console.log(`video → ${out} (${W * SCALE}×${H * SCALE}, ${FPS} fps, ${DUR}s)`);
  }
  await browser.close();
})();
