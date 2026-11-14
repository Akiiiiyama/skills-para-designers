// Tokens (W3C DTCG) → dist/tokens.json, dist/index.js and dist/tokens.css. No dependencies.
// Source of truth: tokens/. Never edit dist/ by hand.
import { readFile, writeFile, mkdir } from 'node:fs/promises';

const here = (p) => new URL(`../${p}`, import.meta.url);
const read = async (p) => JSON.parse(await readFile(here(p), 'utf8'));

const pkg = await read('package.json');
const prefix = pkg.dsPrefix || 'ds';
const [primitives, typography, light, dark] = await Promise.all([
  read('tokens/primitives.json'), read('tokens/typography.json'), read('tokens/theme/light.json'), read('tokens/theme/dark.json'),
]);

// Flatten the tree into { name: 'color/neutral/0', type, value }. A group's $type applies to its children.
function flatten(node, path = [], type) {
  const out = [];
  const groupType = node.$type ?? type;
  for (const [key, child] of Object.entries(node)) {
    if (key.startsWith('$') || typeof child !== 'object' || child === null) continue;
    if ('$value' in child) out.push({ name: [...path, key].join('/'), type: child.$type ?? groupType, value: child.$value });
    else out.push(...flatten(child, [...path, key], groupType));
  }
  return out;
}

const REF = /^\{([^}]+)\}$/;
const toName = (ref) => ref.replace(/\./g, '/');

// Replace every {reference} with its final value; keep the first reference in `ref` so CSS can point to var(--…).
function resolveAll(list, lookup) {
  const resolve = (value, seen = []) => {
    if (typeof value === 'string' && REF.test(value)) {
      const name = toName(value.match(REF)[1]);
      if (seen.includes(name)) throw new Error(`Circular reference: ${[...seen, name].join(' → ')}`);
      const target = lookup.get(name);
      if (!target) throw new Error(`Reference not found: ${value}`);
      return resolve(target.value, [...seen, name]);
    }
    if (Array.isArray(value)) return value;
    if (value && typeof value === 'object') return Object.fromEntries(Object.entries(value).map(([k, v]) => [k, resolve(v, seen)]));
    return value;
  };
  return list.map((t) => {
    const ref = typeof t.value === 'string' && REF.test(t.value) ? toName(t.value.match(REF)[1]) : undefined;
    return { ...t, value: resolve(t.value), ...(ref && { ref }) };
  });
}

const base = [...flatten(primitives), ...flatten(typography)];
const baseLookup = new Map(base.map((t) => [t.name, t]));
const resolvedBase = resolveAll(base, baseLookup);
const themes = {};
for (const [mode, source] of Object.entries({ light, dark })) {
  const list = flatten(source);
  themes[mode] = resolveAll(list, new Map([...baseLookup, ...list.map((t) => [t.name, t])]));
}
const names = (l) => l.map((t) => t.name).sort().join();
if (names(themes.light) !== names(themes.dark)) throw new Error('Light and dark themes must have exactly the same token names.');

const prims = resolvedBase.filter((t) => t.type !== 'typography');
const types = resolvedBase.filter((t) => t.type === 'typography');

// ---- CSS
const cssName = (name) => `--${name.replace(/\//g, '-')}`;
const family = (v) => v.map((f) => (/\s/.test(f) ? `'${f}'` : f)).join(', ');
const cssValue = (t) => t.type === 'cubicBezier' ? `cubic-bezier(${t.value.join(', ')})` : t.type === 'fontFamily' ? family(t.value) : String(t.value);
const themeDecl = (list, indent = '  ') => list.map((t) => `${indent}${cssName(t.name)}: ${t.ref ? `var(${cssName(t.ref)})` : cssValue(t)};`).join('\n');

const css = `/* Generated from tokens/ by scripts/build.mjs. Do not edit by hand. */

/* Raw values */
:root {
${prims.map((t) => `  ${cssName(t.name)}: ${cssValue(t)};`).join('\n')}
}

/* Theme: light by default, or any block with data-theme="light" */
:root, [data-theme="light"] {
${themeDecl(themes.light)}
  color-scheme: light;
}

/* Theme: dark from the operating system… */
@media (prefers-color-scheme: dark) {
  :root:not([data-theme="light"]) {
${themeDecl(themes.dark, '    ')}
    color-scheme: dark;
  }
}

/* …or chosen on the page */
[data-theme="dark"] {
${themeDecl(themes.dark)}
  color-scheme: dark;
}

/* Type: one class per style */
${types.map((t) => {
  const v = t.value, upper = t.name.endsWith('label') ? '\n  text-transform: uppercase;' : '';
  return `.${prefix}-type-${t.name.split('/').at(-1)} {\n  font-family: ${family(v.fontFamily)};\n  font-size: ${v.fontSize};\n  font-weight: ${v.fontWeight};\n  line-height: ${v.lineHeight};\n  letter-spacing: ${v.letterSpacing};${upper}\n}`;
}).join('\n\n')}

body { background: var(--color-bg); color: var(--color-text-primary); font-family: var(--font-family-sans); }
`;

// ---- JS: tokens.color.accent['600'] → '#1F5FD6'
function nest(list) {
  const root = {};
  for (const t of list) {
    const parts = t.name.split('/');
    let node = root;
    parts.slice(0, -1).forEach((p) => (node = node[p] ??= {}));
    node[parts.at(-1)] = t.value;
  }
  return root;
}

await mkdir(here('dist'), { recursive: true });
await writeFile(here('dist/tokens.json'), JSON.stringify({ primitives: prims, typography: types, themes }, null, 2) + '\n');
await writeFile(here('dist/index.js'), `// Generated. Do not edit.\nexport const tokens = ${JSON.stringify(nest(resolvedBase), null, 2)};\nexport const themes = ${JSON.stringify({ light: nest(themes.light), dark: nest(themes.dark) }, null, 2)};\n`);
await writeFile(here('dist/tokens.css'), css);
console.log(`${pkg.name}: ${prims.length} primitives, ${types.length} type styles, ${themes.light.length} theme tokens × 2 modes → dist/`);
