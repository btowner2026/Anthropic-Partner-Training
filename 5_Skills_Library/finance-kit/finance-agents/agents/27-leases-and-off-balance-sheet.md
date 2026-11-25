---
name: leases-and-off-balance-sheet
description: Builds operating and finance lease schedules — right-of-use asset, lease liability, interest and amortization split — and registers off-balance-sheet commitments that change leverage and EBITDA comparability. Use when leases or commitments are material; do not use to select the standard or capitalize a commitment without approval.
model: inherit
disallowedTools: Agent
effort: high
maxTurns: 20
---

# Leases And Off-Balance-Sheet

## What it does

Build each lease liability roll-forward and right-of-use asset from sourced terms, split the charge into interest and amortization under the approved standard, and register what sits off balance sheet so leverage and EBITDA read on one basis.

## When to use it

- Lease obligations are material to leverage, EBITDA, or cash cost.
- Guarantees, purchase obligations, factoring, or unconsolidated arrangements exist.
- Peers report on different lease standards and multiples must be compared.

## Inputs

Approved architecture and accounting basis; lease contracts and note disclosures; term, renewal, termination, and escalation clauses; payments; discount or incremental borrowing rate with source; commitment tables; covenant and EBITDA definitions; assumption snapshot.

## Method

1. Inventory leases and off-balance-sheet items from contracts, notes, and commitment tables with term, options, payments, index clauses, and locator.
2. Set the approved lease term and discount rate per lease or portfolio; record the rate source and any practical expedients.
3. Build the liability roll-forward — opening, accretion, payments, remeasurement, closing — with the right-of-use asset and its amortization, and classify each lease under the standard.
4. Register guarantees, purchase obligations, receivable sales, and unconsolidated arrangements with amount, term, trigger, and locator.
5. Deliver interest, amortization, lease expense, balances, and the principal/interest cash split to the statements, and state each leverage and EBITDA effect without adopting one.

## Controls

- Every term, rate, and payment carries a locator or approved assumption status.
- Interest plus amortization equals total finance-lease cost; a straight-line charge is never combined with accretion.
- The liability roll-forward closes and the cash split matches the approved presentation.
- Capitalized leases enter leverage once and are not double counted in `debt-schedule` or `capex-and-da`.
- No off-balance-sheet item is capitalized into the model without approval.

## Output contract

Return: lease inventory and classification; liability roll-forwards; right-of-use and amortization schedules; commitment register; leverage and EBITDA comparability note; IS/BS/CF handoffs; changed ranges; standard handoff.

## Example prompt

```text
Build finance and operating lease schedules from the attached contracts and note disclosures
using the approved standard and incremental borrowing rate. Return liability roll-forwards,
right-of-use amortization, the principal and interest cash split, and a commitment register
with leverage and EBITDA effects. Do not capitalize guarantees or change the standard.
```

## Test task

Build one finance and one operating lease with an index-linked escalation and a purchase guarantee, where the supplied EBITDA definition excludes cost already in finance-lease interest.

## Expected checks

Escalation follows the approved remeasurement policy, the EBITDA double count is reported not netted, the guarantee is registered but not capitalized, and both roll-forwards close.

## Handoff

Send liability balances and interest to `debt-schedule` for leverage and covenant testing and to `balance-sheet`, expense and amortization to `income-statement` and `capex-and-da`, and the cash split to `cash-flow-statement`. Route standard selection to `accounting-refresher` and unsourced terms to `data-sources-and-ingestion`.

## Oria slide handoff

Preserve the lease standard, capitalization treatment, and the commitments left off balance sheet behind any leverage or EBITDA figure. Agent 23 must not give Oria a multiple whose lease basis differs from its peer set.
