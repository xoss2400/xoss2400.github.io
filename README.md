# Small Software

A personal portfolio site. One HTML file, one canvas, zero frameworks, no images.

The background is **Ripplekit**: an ASCII fluid field rendered on a 2D canvas.
Ambient interference waves keep the surface moving, pointer movement and clicks
drop expanding ripple rings, and draws are run-length batched per row so a
~7,000-character grid redraws ~30x/second without cooking a fan.

Inspired by [asciify's fluid background](https://asciify.org/docs/backgrounds/fluid).

## Play with it

The console in the bottom-right is live:

- **characters** — type any ramp. First character is the empty trough, last is the bright crest.
- **palette** — hi-vis / ultraviolet / toxic
- **tempo** — chill / normal / espresso

Click anywhere to drop a ripple. `prefers-reduced-motion` renders a still frame instead.

## Editing

Everything is in `index.html`:

- Copy, projects and interests live in the markup. Interest size is `style="--s:1..5"` — bigger means it rents more brain space.
- Colors are CSS custom properties at the top of `<style>`; canvas palettes are the `PALETTES` array in the script.
- Swap the placeholder `hi@example.com` and the `#` links in "Say hi" for real ones.
