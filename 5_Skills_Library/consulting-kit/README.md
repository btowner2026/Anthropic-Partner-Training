# Claude Consulting Skills

**11 Claude skills for the strategy work that happens before the deck exists.**

These follow the arc of a real engagement: turn a vague brief into one decision-shaped question, break it into a MECE tree, state hypotheses you could actually be wrong about, run the diagnostics that settle them, and land an answer that survives a hostile room. They are method, not templates — they make Claude reason the way a strategy team reasons, and they hold the same discipline whether the question is growth, cost or operations.

They were written by [Oria](https://www.oria.one/?utm_source=github&utm_medium=readme&utm_campaign=claude-consulting-skills) and published free. If the answer eventually has to become a partner-grade deck, that is what Oria does.

## The skills

### Frame the problem — get the question right before anyone runs a number

| Skill | What it does |
|:--|:--|
| [`problem-definition`](skills/problem-definition) | Turns a symptom or a solution-in-disguise into a one-page SCQA problem statement and a single decision-shaped key question, tested against five sharpness checks. |
| [`issue-tree-builder`](skills/issue-tree-builder) | Decomposes that key question into a MECE issue tree or hypothesis tree, names the decomposition logic, and ranks the branches so the critical path is obvious. |
| [`hypothesis-design`](skills/hypothesis-design) | Commits to a provisional answer, breaks it into disprovable hypotheses, and pairs each with its disproof condition and the one analysis that settles it. |

### Run the analysis — the diagnostics that settle the question

| Skill | What it does |
|:--|:--|
| [`competitor-analysis`](skills/competitor-analysis) | Reads industry structure with Porter's Five Forces, then profiles each rival on capability, cost and vulnerability so you know which threats are real. |
| [`cost-driver-analysis`](skills/cost-driver-analysis) | Splits a cost movement into volume, rate and mix effects, finds the sub-driver behind the dominant one, and maps each effect to the intervention that fits it. |
| [`zero-based-budget-builder`](skills/zero-based-budget-builder) | Rebuilds a cost centre from a zero base, classifying every line as minimum, target or enhancement, with a justification sentence ready for the CFO. |
| [`process-redesign`](skills/process-redesign) | Maps a value stream end to end with real timing and first-pass-yield data, diagnoses the handoffs, and designs a future state with the controls that make it stick. |

### Land the answer — synthesise it, choose it, defend it

| Skill | What it does |
|:--|:--|
| [`insight-synthesis`](skills/insight-synthesis) | Ladders each finding from observation to implication to action, clusters them into a handful of governing insights, and ranks those by decision impact. |
| [`where-to-play-how-to-win`](skills/where-to-play-how-to-win) | Builds the five-part strategy choice cascade with explicit exclusions, then stress-tests it for coherence and against the strongest competitor's implied cascade. |
| [`pyramid-storyline`](skills/pyramid-storyline) | Structures the argument answer-first — one governing thought, three to five MECE pillars, SCQA setup — and checks the vertical and horizontal logic. |
| [`objection-handling`](skills/objection-handling) | Pre-mortems the pushback, writes each objection in the challenger's sharpest form, scores it on likelihood and lethality, and drafts the answer and its follow-up. |

## Install

Each skill is a folder containing a `SKILL.md` with YAML frontmatter, following the [Agent Skills](https://code.claude.com/docs/en/skills) format.

**Claude Code** — clone into your skills directory:

```bash
git clone https://github.com/andreworia/claude-consulting-skills.git
cp -r claude-consulting-skills/skills/* ~/.claude/skills/
```

**Claude app (web, desktop, mobile)** — go to Settings → Capabilities → Skills and upload a skill folder, or zip one and upload it.

**A single skill** — copy just the folder you want. Each one is self-contained.

## Usage

Skills load themselves when the conversation matches their description. You can also name one directly:

```
Use the problem-definition skill. The client says "our margins are getting
crushed, we need to cut costs" and wants a plan in six weeks.
```

```
Use issue-tree-builder on that key question, then rank the branches.
```

A natural chain for a full engagement:

```
problem-definition  →  issue-tree-builder  →  hypothesis-design
                    →  competitor-analysis / cost-driver-analysis
                    →  insight-synthesis  →  pyramid-storyline
                    →  objection-handling
```

A cost or operations engagement swaps the middle: `cost-driver-analysis` to find where the money actually went, then `zero-based-budget-builder` to rebuild the spend or `process-redesign` to fix the flow that created it. The framing and the landing stay the same.

Then bring the storyline into PowerPoint with [Oria](https://www.oria.one/install?utm_source=github&utm_medium=readme&utm_campaign=claude-consulting-skills) to get native, editable shapes rather than an image of a slide.

## Why these exist

Oria builds the AI that renders complex, professional slides inside PowerPoint. Most of our users are consultants and strategy teams, and the hardest part of their job is never the drawing — it is getting to a defensible answer. So we wrote down the method: how a key question is sharpened until it is worth answering, why a hypothesis you cannot disprove is worthless, what separates a finding from an insight. None of that is proprietary, so it is published here for free.

More skill packs and prompt libraries: [oria.one/resources](https://www.oria.one/resources?utm_source=github&utm_medium=readme&utm_campaign=claude-consulting-skills).

## Related repositories

- [claude-powerpoint-skills](https://github.com/andreworia/claude-powerpoint-skills) — storyline, exhibit and deck-review skills
- [claude-excel-skills](https://github.com/andreworia/claude-excel-skills) — financial modelling and spreadsheet skills
- [claude-finance-skills](https://github.com/andreworia/claude-finance-skills) — investment banking, PE and valuation skills
- [claude-pptx-skills](https://github.com/andreworia/claude-pptx-skills) — corporate template and brand-compliance skills

## Contributing

Issues and pull requests are welcome. If a skill is wrong, or you have a sharper version, open a PR.

## License

[MIT](LICENSE) — use them commercially, modify them, redistribute them. Attribution appreciated, not required.

<br />

<p align="center">
  <a href="https://www.oria.one/?utm_source=github&utm_medium=readme&utm_campaign=claude-consulting-skills">
    <img src="https://raw.githubusercontent.com/andreworia/claude-consulting-skills/main/.github/assets/oria-logo.png" width="44" alt="Oria">
  </a>
</p>
<p align="center">
  <sub>Built by <a href="https://www.oria.one/?utm_source=github&utm_medium=readme&utm_campaign=claude-consulting-skills"><b>Oria</b></a> — AI for complex professional slides</sub>
</p>
