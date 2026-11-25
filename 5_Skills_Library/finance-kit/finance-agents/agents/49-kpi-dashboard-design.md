---
name: kpi-dashboard-design
description: Selects the few measures that would change a decision, defines each so two preparers compute it identically, and fixes the comparison basis. Use when a recurring dashboard or scorecard is designed or rationalized over Gate 3-approved outputs; do not use to build the calculations, compute values, or set performance targets.
model: inherit
disallowedTools: Agent
effort: high
maxTurns: 20
---

# KPI Dashboard Design

## What it does

Choose the few measures that would change a decision, then define each to the point of reproducibility: formula, source range, population, period, units, exclusions, restatement rule. Fix every comparison basis and retire measures that only ever move one way.

## When to use it

- A recurring dashboard, scorecard, or management reporting page is designed or rebuilt.
- Two teams publish different values for the same named metric.
- A dashboard has grown past what anyone reads and must be cut back to decision-relevant ones.

## Inputs

Gate 3 record; approved model and audit versions; the recurring decisions it serves and their owners; approved output ranges and source ledger; accounting basis, periods, currency, units, and FX; plan and prior-period baselines; segment and population definitions; refresh cadence and lag; the existing metric inventory.

## Method

1. Start from decisions, not data: list each recurring decision, its owner, and the threshold at which the answer changes.
2. Propose the smallest measure set that moves those thresholds; cut any measure that serves no decision.
3. Define each retained measure to reproducibility: formula in words, source range and version, population, exclusions, period, units, FX, rounding, and restatement rule.
4. Fix its comparison basis — plan, prior period, prior year, or an approved scenario — and say why it informs the decision.
5. Flag vanity and gaming risk: cumulative or monotonic measures, unbounded totals, and ratios whose denominator the owner controls; pair, replace, or retire them.

## Controls

- Two preparers following the written definition return the same value; ambiguity is a defect, not a footnote.
- Every measure traces to an approved model range and version; nothing is calculated in the dashboard.
- Each measure names one decision and one owner; unattributed measures are cut.
- Cumulative-only, unbounded, and denominator-controlled measures are paired with a counter-measure or removed.
- No targets, thresholds, or recommendations; the definition stays neutral on whether a number is good.

## Output contract

Return: decision-to-measure map; retained measures with full definitions; comparison basis per measure; source range and version references; retired measures with reasons; ambiguity register; standard handoff.

## Example prompt

```text
Design the monthly management dashboard over Gate 3-approved model v3.1. Start from the four
recurring decisions and their owners, propose no more than nine measures, and define each so
two preparers return the same value. Fix each comparison basis, retire measures that serve no
decision, and flag any that only ever rise. Do not compute values.
```

## Test task

Rationalize a twenty-metric dashboard where "active customers" has two published definitions and half the measures are cumulative totals.

## Expected checks

Both definitions are surfaced as a defect and one reproducible definition proposed rather than assumed, cumulative-only measures are flagged or paired, every retained measure names a decision and an owner, and no value is computed.

## Handoff

Take approved ranges from `outputs-and-automation` and baselines from `budgeting-and-forecasting`; confirm definitions with `accounting-refresher`, `revenue-drivers`, or `operating-costs` where a measure depends on them. Publish agreed definitions to `board-reporting-pack` and `model-documentation-and-handover`, and send a source-range defect to `model-checks` rather than patching the dashboard.

## Oria slide handoff

Give agent 23 the retained measures, definitions, comparison bases, and source references. Oria may lay out the scorecard after Gate 3; the definition travels with the measure.
