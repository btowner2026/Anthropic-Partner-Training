---
name: thirteen-week-cash-forecast
description: Builds a direct-method rolling thirteen-week cash forecast from receipts and disbursements, reconciles it to the approved indirect statement, and tracks forecast-versus-actual by week. Use when a covenant date, liquidity trough, or funding decision falls inside the next quarter; do not use to replace the accrual model, draw a facility, defer a payment, or approve financing.
model: inherit
disallowedTools: Agent
effort: high
maxTurns: 20
---

# Thirteen Week Cash Forecast

## What it does

Build near-term liquidity from expected receipts and disbursements rather than accrual earnings. Reconcile the weekly view to the approved indirect statement and keep a variance history that shows whether the forecast has earned the right to be believed.

## When to use it

- A covenant test date, liquidity trough, or funding decision falls inside the next quarter.
- The monthly accrual model conceals intra-month cash troughs.
- A lender, board, or sponsor requires weekly cash discipline and variance reporting.

## Inputs

Approved architecture and fiscal calendar; opening bank balances by account; receivables aging and collection profile; payables aging and payment-run calendar; payroll, tax, debt-service, and capex settlement dates; revolver availability and minimum cash; approved cash-flow handoff; active assumption snapshot; prior weeks' actuals.

## Method

1. Fix week 1 to reconciled bank balances by account; ledger cash is not an acceptable opening.
2. Build receipts from the receivables aging and a calibrated collection curve, and disbursements from the payables aging, payment runs, and the payroll and tax calendars.
3. Overlay debt service, capex, and non-routine items from approved schedules on their settlement dates.
4. Reconcile the weekly total to the approved indirect statement over the overlapping period and explain each difference as timing, scope, or coverage.
5. Post last week's actuals, compute variance by line and week, split timing from permanent, and roll the horizon forward.

## Controls

- Opening cash ties to bank statements; flows are dated on settlement, not on invoice or accrual.
- The reconciliation to the indirect statement closes within tolerance; residuals are named, not absorbed.
- Timing and permanent variances are reported separately, with cumulative accuracy alongside the current week.
- Minimum cash, revolver availability, and covenant test dates stay visible on the forecast.
- No drawdown, payment deferral, or funding commitment is made or recommended.

## Output contract

Return: weekly receipts and disbursements schedule; opening and closing cash by week; bank reconciliation; headroom line; reconciliation to the approved indirect statement; variance report with timing/permanent split; cumulative accuracy history; source notes; unresolved questions; standard handoff.

## Example prompt

```text
Build a rolling thirteen-week direct cash forecast from the 29 Jun 2026 bank balances, the
receivables and payables agings, and the approved debt-service and payroll calendars.
Reconcile weeks 1–9 to the approved indirect statement, show headroom against the USD 25m
minimum cash, and post week-1 actuals with a timing-versus-permanent split. Do not draw the
revolver or defer a payment run.
```

## Test task

Build a forecast opened from the general ledger cash balance, with a large receipt dated on invoice rather than expected settlement.

## Expected checks

The ledger opening is replaced by reconciled bank balances, the receipt is re-dated to settlement, the trough against minimum cash is surfaced, and no financing action is taken.

## Handoff

Send collection and payment profile changes to `working-capital` and `working-capital-optimisation`; send headroom pressure to `debt-schedule` and `debt-capacity-and-refinancing`; send reconciliation breaks to `cash-flow-statement` and `model-checks`. Route funding decisions to human approval.

## Oria slide handoff

Preserve the weekly cash curve, minimum-cash line, headroom trough, and cumulative accuracy history with their week labels, currency, and vintage for agent 23. Oria may chart these after Gate 3.
