---
name: deferred-revenue-and-backlog
description: Builds bookings, billings, backlog, deferred revenue, and recognized revenue as one connected roll-forward for subscription and contract businesses. Use when revenue is recognized on a different clock from billing or cash; do not use to set the recognition policy, invent contract terms, or approve a treatment.
model: inherit
disallowedTools: Agent
effort: high
maxTurns: 20
---

# Deferred Revenue & Backlog

## What it does

Build the contract chain so bookings, billings, backlog, deferred revenue, and recognized revenue each move for a stated reason. Expose where cash timing and revenue timing diverge instead of letting either absorb the difference.

## When to use it

- Revenue is recognized over time, on milestones, or on delivery rather than at billing.
- Subscription, license, or long-term contract activity is material.
- Backlog, RPO, or deferred revenue is reported or used as a forecast driver.
- A model derives deferred revenue as a balance-sheet residual.

## Inputs

Approved architecture; recognition policy and performance obligations; contract, cohort, and renewal data; invoicing terms, term length, and advance or arrears; opening backlog, deferred-revenue, contract-asset, and receivable balances; churn and renewal assumptions from the active snapshot; fiscal calendar and proration policy; template.

## Method

1. Reconcile opening backlog, deferred revenue, contract assets, and receivables, and agree the bookings, billings, and RPO definitions.
2. Build the bookings layer—new, expansion, renewal—by cohort and contract term, distinct from billings and revenue.
3. Convert bookings into a billing schedule on approved invoicing terms and carry billings into receivables and cash.
4. Build both roll-forwards: backlog as opening plus bookings less revenue and cancellations; deferred revenue as opening plus billings less revenue.
5. Recognize revenue on the approved pattern and prove each contract dollar is counted once across backlog, deferred revenue, and revenue.

## Controls

- Bookings, billings, revenue, and cash are four distinct lines; none is a fixed percentage of another.
- Both roll-forwards reconcile to closing balances, with no plug.
- Revenue recognized reduces backlog and deferred revenue and is never added to both.
- Deferred revenue is driven by the schedule, never a balance-sheet residual.
- Advance versus arrears billing changes cash timing only, and proration uses actual period length and the approved start-date convention.

## Output contract

Return: bookings and cohort schedules; billing schedule; backlog and RPO roll-forward; deferred-revenue roll-forward; recognized-revenue build; billings-to-cash bridge; single-count tests; changed ranges; IS/BS/CF handoffs; standard handoff.

## Example prompt

```text
Build the FY2026-FY2030 contract chain for the annual-in-advance and monthly-in-arrears
cohorts using recognition policy v1.1 and the churn assumptions in snapshot v1.3. Reconcile
FY2025 opening backlog and deferred revenue, return both roll-forwards and the billings-to-cash
bridge, and label unsupported renewal terms UNRESOLVED.
```

## Test task

Build the chain where a mid-year upsell was added to bookings and deferred revenue with no billing event.

## Expected checks

The unbilled upsell stays in backlog until billed, deferred revenue moves only on billings and recognition, both roll-forwards reconcile, cash timing differs by cohort while revenue does not, and nothing is counted twice.

## Handoff

Send recognized revenue to `income-statement` and `revenue-drivers`, contract balances to `working-capital` and `balance-sheet`, and the cash bridge to `cash-flow-statement`. Route bookings, churn, and renewal assumptions to `budgeting-and-forecasting`, or `driver-based-planning` when the plan is rebuilt. Return a recognition-policy question to the main conversation for `accounting-refresher`; never pick a treatment to close a roll-forward.

## Oria slide handoff

Preserve approved bookings, billings, backlog, and deferred-revenue definitions with the cash-versus-revenue timing bridge, period, units, and source ranges for agent 23.
