# ~john

John McGowan's portfolio. "The future is unknown."

## What's on the page

**The water.** The landing page is a full-screen canvas drawing a live ASCII fluid
field: domain-warped travelling waves for the ambient swell, plus ripple rings from pointer
moves (scaled by velocity), clicks and hovers, and a soft wake under the cursor. As you
scroll, the canvas shrinks into a strip pinned to the top (`stripH` is 17.3% of the viewport
height, clamped to 113–167px) and the sections scroll underneath it on white.

**The bout.** Inside the water, two judoka fight on a yellow tatami with a blue border. Each is about 34
ellipsoid, box and cylinder primitives on a joint rig, raycast into the character grid. The
throws are harai goshi, uchi mata, seoi nage, tai otoshi and tomoe nage; a tie is a blocked
turn-in or a faked foot sweep. Poses run on
cubic Hermite splines at each technique's real key times with limb lag, and the thrown
fighter flies one Bézier arc. Every exchange randomises its pace, arc height, landing spot
and impact. The middle of the screen is the mean (marked `^ mean` under the mat): the
bout and its mat walk off it as Zob wins or loses and come back when he does. Near the
middle the walk is drawn true; farther out it's squeezed toward a margin and the camera
pans the rest, so the mat's seams slide past and the fighters never leave the screen. In
the scrolled strip the walk stays in the gap between the bar's pills.
The camera also breathes: it pulls back as Zob's total wanders from the mean (gently from
the first step, harder once the bout would leave the frame, never below 40% of the landing
scale) and eases back in as it reverts. Every landing hits, at every speed: two rings
through the water from the spot, a fountain of spray, and the mat jolts.

**Zob.** The bout is driven by Zob, who has $1,000 and bets Banker at a baccarat table.
It's real punto banco: 8 decks, burn card, cut card and the standard third-card rules.
Banker pays `0.446247 / 0.458597` (≈0.97307 to 1), which makes the game exactly even. In
4M simulated hands the mean was −0.0002 bets a hand (z = −0.39).

- Banker is blue and always stands on the right; Player is red and always on the left. The
  winner throws the loser out past his own side (blue throws red right, red throws blue
  left), then they walk back to their marks, red passing behind and blue in front.
- The bout moves with Zob's money in bet units: +PAY to the right on a Banker win, −1 to
  the left on a Player win. That makes Dist. a random walk around a flat Est. of 0.
- When Dist. crosses 0 after 5,000 hands, they bow, "MEAN REVERTED" shows, and the run
  restarts.
- At 1× the bout sets the pace: the next hand is dealt after the exchange plus a
  0.45–1.75s grip-fighting beat. At 10× and up it's time-based (`HAND = 4.4`s ÷ speed).
  Past 1× the throws are capped (they run 2.6× faster, about one every two seconds) so the
  frame cost doesn't grow with speed: every hand is still counted, each throw acts out the
  latest one, and the mat slides to catch up. The Zob card says so.

Zob's card shows him as a green-on-black terminal: Banker, Player, Hands, Balance, Dist.,
Expected, Bet and Last, with speed (1/10/100/1k×) and bet ($1/5/25/100) toggles.
`[ chart ]` opens a chart of Dist. against Expected and a log of recent hands.

**Landing.** Name and role, the line, one sentence on what I do, and two buttons
(Résumé, Copy email). Only the buttons take the pointer, so the wheel still scrolls.

**Sections.** A floating bar (name on the left; Experience, Projects, About and Contact,
plus a Résumé button on wide screens) sits over the strip and marks the section in the
middle of the screen. A skip link comes first. Under the strip:

- **Experience**: Meristead Wealth as a case study (what was built and what it bought, for
  three pieces of work, and a diagram of the Orion → Salesforce sync), then Mobius and the
  Cornell game as rows.
- **Projects**: five cards, each with copy, a picture, four facts and its stack.
  - Ninth Circle: a sketch of its feed , with generated covers and a draggable star rating.
  - Quill: a real screenshot (`img/quill.webp`, taken with the app's own script hook),
    marked work in progress; its button opens an email asking for access to the private repo.
  - wrestlELO: a scoreboard running Elo's expected-score formula on two sliders. Links to `wrestlelo/`.
  - Zob: his terminal.
  - The small-data study: a line chart of the real results (crosshair tooltip, a table
    under "See the numbers"), redrawn at its real width so it reads on a phone.
  - "Also built" is a list. Rows with nothing public to link aren't links. Sharp's row
    opens the widget below.
- **About**: prose beside a fact sheet (education, coursework, SIE, awards, toolbox).
- **Now**: four cards with an "Updated" stamp.
- **Contact**: the email, Copy email, Résumé and GitHub, then a colophon.

**Sharp.** The Mandarin widget, rebuilt as a draggable window over the page: type Chinese
(or tap a sample) for pinyin and an English meaning, with the original's pixel armies
fighting in the title bar. Pinyin comes from `pinyin-pro` (pinned, with an integrity hash,
loaded the first time Sharp opens). Meanings come from MyMemory's free API, which gets
whatever is typed. Its top answer is sometimes junk, so the widget ranks its matches by
quality and shows two runners-up. Escape closes it and focus goes back to the button.

**Print.** Printing drops the canvas, the bar and the widgets and spells out links.

## Rendering

Painting each run of same-coloured characters with its own `fillText` cost about 23k calls
a frame and held the field near 30fps. Now the glyphs go down as one string per row in flat
ink on a mask canvas, and the colour comes from a `cols × rows` tint image stretched over it
with `source-in`. The colour is continuous instead of banded, and it's about ten times
faster.

`prefers-reduced-motion` renders a still frame that redraws on interaction instead of
animating.

## Scrolling

The document never scrolls; `#scroller` does. Safari 26 draws whatever the root scroller
has under its translucent toolbar, so this keeps content from showing through it. The
canvas is `pointer-events:none`, so wheel and swipe reach the scroller and ripples listen on
the window. The landing line is `position:fixed` above the canvas and moved by the script
with the scroll.

## Palette

Light, high-key, chlorinated. No pink, ever.

| token | hex | role |
| --- | --- | --- |
| Pool | `#EEFAF0` | the ground |
| Paper | `#FDFDFB` | raised surfaces, scrims |
| Ultramarine | `#0E2A8C` | ink |
| Tangerine | `#FF5A1F` | primary accent, the tilde |
| Chrome | `#FFC93C` | highlights |
| Aqua | `#12C6C0` | links |
| Lime | `#7BDD2E` | live states |
| Slate | `#5A6A87` | the only neutral, blue-biased |

Type: Instrument Serif (headlines), Hanken Grotesk (body), DM Mono (labels, data and the
ASCII field itself). Page text is near-black `#0B0B10` on white, with `#F4F5F3` cards.

## Poke the water

Two round buttons ride the bottom-left corner of the water: the full screen on landing,
the strip once scrolled. ❚❚ pauses everything that moves (the loop, the game, the diagram's
packets) and remembers the choice. The ≈ button shows its label on hover. Open it for:

- **characters**: type any ramp. The first character is the empty trough and the last is
  the crest.
- **palette**: pool, riso or chlorine.
- **feedback**: calm, wet or choppy (scales every ripple and the cursor wake).

Chlorine and calm are the defaults. It also shows the grid size and fps.

## Editing

Everything is in `index.html`. Grep these headers in the script:

- `THE BOUT`: the rig, materials, primitives (`judoka()`) and `pose()`.
- `the throws`: the `TECH` table, `begin()` and `boutMove()`.
- `the mat`: `matSetup` and `matRow`.
- `the strip`: `layout()` and the `AX`/`AY` anchors.
- `THE TABLE`: the shoe, `hand()`, `gameTick()` and `fresh()`.
- `Zob in Projects`: the terminal, log and chart.

Copy lives in the `<section class="station">` blocks, and the landing words in
`<header class="hero">`. The Ninth Circle sketch's covers and rater are in the second
`<script>`, after the engine. Each station's `data-accent` is the
RGB the water eases toward in that section. Colours are custom properties at the top of
`<style>`, and the water palettes are the `PAL` array.

Facts on the page come from the résumé and the projects' own READMEs and result files.
Keep them in step when either changes. Update the Now cards and their "Updated" stamp as
things change.
