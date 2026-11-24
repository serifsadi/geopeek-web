// Screenshot pipeline.
// Put captures in src/assets/shots/{light,dark}/<name>.(png|webp|jpg).
// A missing light capture falls back to the dark one (and vice versa) and is
// reported as a placeholder at build time. See PLACEHOLDERS.md.
import type { ImageMetadata } from 'astro';
import { getImage } from 'astro:assets';

const files = import.meta.glob<{ default: ImageMetadata }>(
  '/src/assets/shots/*/*.{png,webp,jpg,jpeg}',
  { eager: true },
);

function find(theme: 'light' | 'dark', name: string): ImageMetadata | undefined {
  for (const ext of ['png', 'webp', 'jpg', 'jpeg']) {
    const m = files[`/src/assets/shots/${theme}/${name}.${ext}`];
    if (m) return m.default;
  }
  return undefined;
}

const warned = new Set<string>();

export function shot(name: string) {
  const dark = find('dark', name);
  const light = find('light', name);
  const d = dark ?? light;
  const l = light ?? dark;
  if (!d || !l) throw new Error(`Missing screenshot: ${name}`);
  if ((!light || !dark) && !warned.has(name)) {
    warned.add(name);
    console.warn(`[shots] ${name}: only ${light ? 'light' : 'dark'} capture found, used for both themes (placeholder)`);
  }
  return { light: l, dark: d, placeholder: !light || !dark };
}

export async function srcset(img: ImageMetadata, widths: number[]) {
  const ws = widths.filter((w) => w < img.width);
  ws.push(img.width);
  const r = await getImage({ src: img, widths: ws, format: 'webp', quality: 82 });
  return { src: r.src, srcset: r.srcSet.attribute, width: img.width, height: img.height };
}
