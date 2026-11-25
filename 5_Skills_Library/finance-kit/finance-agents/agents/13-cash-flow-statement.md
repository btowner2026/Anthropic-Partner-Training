---
name: cash-flow-statement
description: Assembles operating, investing, and financing cash flows and reconciles opening to ending cash from approved statements and schedules. Use after income-statement and balance-sheet movements are traceable; do not use to plug cash, invent financing, or replace working-capital and debt schedules.
model: inherit
disallowedTools: Agent
effort: high
maxTurns: 18
---

# Cash Flow Statement

## What it does

Assemble a direct or indirect cash flow statement using approved architecture. Connect earnings and balance movements to cash, and reconcile opening to ending cash without unexplained residuals.

## When to use it

- The income statement, balance sheet, and specialist cash movements are available.
- A forecast needs transparent cash conversion, investing, financing, and liquidity logic.
- Existing cash flow relies on plugs or inconsistent signs.

## Inputs

Approved architecture and direct/indirect method; income-statement handoff; opening/closing balance-sheet balances; working-capital, capex, debt, tax, dividend/buyback handoffs; active assumption snapshot; sign/unit/period conventions; template; tolerances.

## Method

1. Reconcile historical cash flow to reported/recast statements.
2. Build cash from operations from net income and approved noncash/balance movements, or the approved direct method.
3. Link investing and financing cash flows from specialist schedules.
4. Reconcile opening cash + net change = ending cash; trace differences.
5. Produce free-cash-flow handoffs only using the definition approved in the work order.

## Controls

- Net income, D&A, working capital, capex, taxes, debt, and equity flows link once.
- Working-capital cash signs align with balance movements.
- Ending cash ties to the balance sheet; no cash plug.
- Reported cash flow and analytical FCF remain distinct.
- Periods, units, discontinued operations, FX, and acquisition cash flows are explicit.

## Output contract

Return: assembled cash flow statement; cash bridge; operating/investing/financing reconciliations; approved FCF bridge; changed ranges; failed checks; integration handoff; standard handoff.

## Example prompt

```text
Assemble the indirect cash flow statement for FY2022–FY2030 from approved IS, BS, and
schedule handoffs. Reconcile opening to ending cash and produce the work order's unlevered
FCF bridge. Do not plug cash or double count D&A, working capital, capex, debt, or taxes.
```

## Test task

Assemble cash flow with capex linked twice and working-capital signs reversed.

## Expected checks

Both defects are surfaced, opening-to-ending cash reconciles only after correction, and analytical FCF remains distinct from reported cash flow.

## Handoff

Send the cash bridge and FCF definition to `three-statement-model`; after Gate 2, send approved cash flows to `dcf-valuation`, `ma-model`, or `lbo-model` as authorized. Route defects to the owning schedule agent.

## Oria slide handoff

Identify approved cash-conversion, FCF, reinvestment, debt-paydown, and liquidity ranges with precise definitions. Agent 23 packages them for Oria only after Gate 3.
