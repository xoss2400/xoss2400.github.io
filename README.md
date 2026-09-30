# ~john

A personal site that doesn't scroll. It zooms.

Brand: **Tilde** — the mark is `~`, which means both "home directory" and "a wave."
One hand-written `index.html`, one canvas, no frameworks, no build step, no images.

## Two ideas hold it up

**Depth equals specificity.** Five levels, each a full viewport. Level 1 is the widest
statement (the wordmark); each zoom in is something more particular — what I built, what
I'm obsessed with, what I'm doing this month, how to reach me. Magnification is shown as
a real readout (`1.00×`, `1.90×`, `3.61×`, `6.86×`, `13.0×`).

Navigate by wheel, trackpad pinch, swipe, `↑`/`↓`, `+`/`−`, `Home`/`End`, or the depth
rail. Nothing scrolls; a station that overflows on a short screen keeps its own scroll
and only zooms once you hit its edge.

**Everything is water.** The background is a live ASCII fluid field — three domain-warped
travelling waves for the ambient churn, plus expanding ripple rings from every pointer
move (strength scaled by cursor velocity), every click, and every hover over an
interactive element. A smoothed "well" follows the cursor and visibly deforms the
surface. Changing depth fires a double shockwave from the centre, surges the amplitude,
stretches the wavelength, and lerps the crest colour to that section's accent.

Draws are run-length batched per row — one `fillText` per run of same-coloured characters
— so a ~100,000-cell grid (characters set to about a third the size, ten times the
count) holds ~30fps. `prefers-reduced-motion` renders a still frame
that redraws on interaction instead of animating.

## Palette

Light, high-key, chlorinated. No pink, ever.

| token | hex | role |
| --- | --- | --- |
| Pool | `#EAF7F4` | the ground |
| Paper | `#FDFDFB` | raised surfaces, scrims |
| Ultramarine | `#0E2A8C` | ink, and the crest of the water |
| Tangerine | `#FF5A1F` | primary accent, the tilde |
| Chrome | `#FFC93C` | highlights |
| Aqua | `#12C6C0` | mid-water, links |
| Lime | `#7BDD2E` | live states |
| Slate | `#5A6A87` | the only neutral, blue-biased |

Type: Archivo Black (display), Hanken Grotesk (body), DM Mono (labels, data, and the
ASCII field itself).

## Poke the water

The pill at bottom-left is collapsed by default. Open it for:

- **characters** — type any ramp; first character is the empty trough, last is the crest
- **palette** — pool / riso / chlorine
- **feedback** — calm / wet / choppy (scales every ripple and the cursor well)

Chlorine and calm are the defaults.

## Editing

All in `index.html`. Copy lives in the five `<section class="station">` blocks. Level 3 holds two
lists you'll want to keep adding to — `.shelf` for books (a `<cite>`, a `<small>` author
and a one-line take) and `.pins` for sites worth keeping (one `<li><a>` each). Each
station's `data-accent` is the RGB the water shifts to at that depth. Colours are custom properties
at the top of `<style>`; water palettes are the `PAL` array in the script.

Swap the placeholder `hi@example.com` and the four `#` links on level 5 before showing
anybody.
