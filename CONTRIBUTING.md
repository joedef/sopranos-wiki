# Contributing

Thanks for helping. This is a hobby wiki about a television series that ended in 2007 — the bar for participation is low, the bar for accuracy is high.

## The one hard rule

**Do not paste in copyrighted text.** No script pages, no transcribed scenes, no wholesale copying from another wiki or site. Quote briefly for commentary — a line of dialogue, a sentence from a review — and attribute it. Everything else must be in your own words.

This protects the project and keeps the CC BY-SA license honest.

## How to make a change

1. Fork the repo and create a branch.
2. Edit the Markdown in `docs/`. Every page has an ✏️ link at the top right of the live site that opens the right file on GitHub.
3. Run `mkdocs build --strict` if you can — it catches broken internal links, the most common breakage.
4. Open a pull request describing what you changed and, for facts, where the figure came from.

`main` is protected. Every change needs a passing build and an approving review before it merges — including a maintainer's own. Typo fixes don't need a local build; just open the PR.

## House style

**Voice.** Plain, specific, unhurried. Write like a well-read friend explaining something they love, not like an encyclopedia and not like a recap. Avoid superlatives that do no work ("iconic," "legendary," "masterpiece") — show why instead.

**Facts vs. readings.** State facts flatly. Frame interpretation as interpretation: *"Chase has said…"*, *"the most common reading is…"*, *"one way to take the cut to black is…"*. Where critics disagree, say so and name them. Never launder an opinion as a fact.

**The ending especially.** [Reading the Ending](docs/analysis/reading-the-ending.md) presents the major interpretations and does not declare a winner. That is deliberate and load-bearing. Do not "fix" it by asserting that Tony definitely died or definitely lived — including on other pages. Chase's own statements have shifted over eighteen years, and the page tracks them chronologically for exactly this reason.

**Episode citations.** Reference episodes as `"Title" (S3E11)`. Season and episode numbers use the HBO broadcast order.

**Numbers.** Give the figure, the unit, and the source. Viewership numbers in particular vary by whether you mean the premiere airing, the same-night repeat, or the weekly cume — say which.

**Dates.** Real-world dates get years (`June 10, 2007`). In-universe timing uses the show's own framing.

**Spoilers.** There are none. This is a reference work for a series that ended in 2007; pages assume you've seen it. Don't add spoiler warnings.

## Page conventions

**Infobox.** Character, person, and season pages open with a fact panel:

```html
<div class="infobox" markdown>
#### At a glance
Played by
:   James Gandolfini

First appearance
:   "The Sopranos" (S1E1)
</div>
```

**Epigraph.** Major pages may open with one quotation:

```html
<p class="epigraph">Those who want respect, give respect.
<cite>Tony Soprano</cite></p>
```

**Episode tables** go inside `<div class="episodes" markdown>` for the tighter type treatment.

**Charts** are plain HTML/CSS — no libraries, no external requests. Copy the pattern in [`docs/data/charts.md`](docs/data/charts.md) and set the width percentages yourself.

**Links.** Use relative Markdown links (`[Tony](../characters/tony-soprano.md)`). `--strict` fails the build on a broken one, which is the point.

## Sourcing

Add anything you lean on to [`docs/reference/sources.md`](docs/reference/sources.md). Preferred, roughly in order:

1. Primary — the episodes, the DVD/Blu-ray commentaries, contemporaneous interviews, *The Sopranos Sessions* interviews with Chase
2. Documented secondary — Alan Sepinwall and Matt Zoller Seitz, *Difficult Men* (Brett Martin), Peter Biskind, published critics
3. Reference aggregators — Wikipedia, the Emmy database, Nielsen reporting

Be careful with cast anecdotes. Twenty-five years of convention panels and podcasts have smoothed a lot of stories into shapes that suit the teller. Where accounts conflict, write it as disputed and name who says what.

## Scope

In scope: all 86 episodes, the characters, cast and crew, *The Many Saints of Newark*, the real organized-crime history the show draws on, and the cultural legacy.

Out of scope: unmarked speculation, fan fiction, real-crime coverage untethered from the show, and anything about living people that isn't documented and relevant.

## Code of conduct

Be decent. Argue about the ending as much as you like; do it without being unpleasant to a person.
