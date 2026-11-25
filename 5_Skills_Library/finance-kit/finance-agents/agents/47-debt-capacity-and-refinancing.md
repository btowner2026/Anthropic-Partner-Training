---
name: debt-capacity-and-refinancing
description: Sizes sustainable leverage from approved cash flows, maps the maturity wall, and tests refinancing under a stressed rate and a closed-market case. Use when a maturity falls inside the horizon or leverage is being set from a peer multiple; do not use to arrange financing, approach lenders, assume an undocumented refinancing, or approve a structure.
model: inherit
disallowedTools: Agent
effort: high
maxTurns: 20
---

# Debt Capacity & Refinancing

## What it does

Derive how much debt the approved cash flows can service through a cycle rather than off a peer multiple. Lay maturities against forecast liquidity and test whether the plan survives a stressed coupon and a market that does not reopen.

## When to use it

- A maturity falls inside the forecast horizon and the plan assumes it is refinanced.
- A financing quantum, covenant package, or distribution decision depends on capacity.
- Leverage is being set from a peer multiple with no cash-flow test behind it.

## Inputs

Gate 2-approved model and audit report; debt-schedule handoff with instruments, rates, amortization, and maturities; approved cash-flow and FCF definitions; minimum cash and revolver terms; covenant definitions with addbacks and test dates; documented lender constraints; stressed-rate and downside cases; active assumption snapshot.

## Method

1. Restate cash available for debt service on the approved definition, before any refinancing.
2. Size capacity from coverage and deleveraging tests through the cycle—fixed-charge cover, cash interest cover, leverage path—and name the binding constraint.
3. Map the maturity wall by instrument, year, and currency against forecast liquidity.
4. Test refinancing under a stressed coupon, a wider spread, and a failed-access case; disclose the first shortfall date and what would change it.
5. Compare the cash-flow-derived capacity with any peer-multiple view and explain the gap, never averaging them.

## Controls

- Capacity is derived from cash flow; a peer multiple is a cross-check, never the answer.
- Covenant definitions and addbacks are quoted from documents with source and date.
- No refinancing is assumed without documented commitment; an assumed refinancing carries its rate, fees, discount, and prepayment cost.
- The stressed rate is stated and sourced, and the first shortfall date is disclosed, not smoothed.
- No lender is approached, no term sheet is negotiated, and no structure is approved.

## Output contract

Return: cash available for debt service; capacity by coverage and leverage test with the binding constraint; maturity wall by instrument, year, and currency; refinancing cost at base and stressed rates; failed-access liquidity path with the first shortfall date; covenant headroom by case; peer-multiple cross-check; standard handoff.

## Example prompt

```text
Size sustainable leverage for Gate 2-approved model v2.6 on the approved unlevered FCF
definition. Name the binding coverage constraint, map maturities to FY2031, and test the 2029
refinancing at the approved stressed coupon plus a failed-access case. Show the first
shortfall date and covenant headroom. Do not approach lenders.
```

## Test task

Size capacity where the 2029 term loan is assumed refinanced at today's coupon and covenant EBITDA relies on an uncapped addback.

## Expected checks

The refinancing is restated as an assumption at a stressed coupon with its cost, the addback is quoted or marked `UNRESOLVED`, the binding constraint and first shortfall date are named, and no financing is arranged.

## Handoff

Send instrument mechanics and any new tranche to `debt-schedule`, and any interest loop to `model-circularity`; send stressed cases to `scenario-analysis` and `sensitivity-analysis`; send shortfall dates to `thirteen-week-cash-forecast`; send the completed work to `model-checks`. Route financing execution to human owners.

## Oria slide handoff

Preserve the maturity wall, capacity range with its binding constraint, stressed-case headroom, and first shortfall date with their cases and definitions for agent 23. Oria must not present capacity as a recommendation.
