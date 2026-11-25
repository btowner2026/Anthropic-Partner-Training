---
name: working-capital-optimisation
description: Quantifies the cash released by moving DSO, DPO, and DIO, prices each lever against its commercial cost, and separates structural improvement from period-end pull-forward that reverses. Use when cash conversion is a live agenda item or a reported gain needs a durability test; do not use to rebuild working-capital mechanics, contact counterparties, or approve a lever.
model: inherit
disallowedTools: Agent
effort: high
maxTurns: 20
---

# Working Capital Optimisation

## What it does

Size the cash locked in the operating cycle, convert each day of DSO, DIO, and DPO into cash on the approved denominators, and test whether a lever survives its commercial cost and the following period.

## When to use it

- Cash conversion is a live management, board, or sponsor agenda item.
- A reported working-capital gain needs a durability test before it is banked.
- A funding gap might be closed from the balance sheet before it is closed with debt.

## Inputs

Approved working-capital schedules and roll-forwards; receivables and payables aging by counterparty; inventory by category with obsolescence data; contractual terms alongside actual payment behavior; revenue and cost handoffs; factoring or supply-chain finance terms and fees; daily balances around period end; active assumption snapshot; day-count policy.

## Method

1. Calibrate DSO, DIO, and DPO on the approved denominators and period lengths, using average rather than closing balances.
2. Convert one day of each metric into cash and build the release bridge for the stated target set.
3. Price every lever against its commercial cost—early-settlement discount, stock-out risk, price increase, facility fee—and report the net effect, never the gross release.
4. Test durability: compare period-end with intra-period average balances, isolate deferred payment runs, pulled-forward collections, and channel loading, and mark any release that reverses.
5. Rank surviving levers by net cash, cost, reversal risk, and owner, and list the assumption changes each requires for approval.

## Controls

- Days use the correct denominator and period length; averages and closing balances are not mixed.
- Gross cash release is never quoted without its commercial cost.
- One-off period-end movement is reported separately and labeled as reversing.
- Factoring and supply-chain finance carry their fee and classification; neither is shown as free cash.
- No counterparty is contacted and no lever is approved; accepted changes flow through `working-capital` drivers, not direct edits to balances.

## Output contract

Return: days calibration; cash-per-day sensitivity; ranked lever list with gross cash, commercial cost, and net effect; durability and reversal test; financing-arrangement disclosure; required assumption changes; standard handoff.

## Example prompt

```text
Calibrate FY2026 DSO, DIO, and DPO from the approved working-capital schedules, quantify the
cash in one day of each, and assess a proposed 8-day DPO extension funded by the supplier
finance facility. Price the price increase and facility fee, test whether last period's DPO
gain was structural, and rank levers by net cash. Do not contact suppliers.
```

## Test task

Assess a DPO extension where the prior period's gain came from deferring the final payment run by four days, with the facility fee undisclosed.

## Expected checks

The deferred run is identified as pull-forward and excluded from structural improvement, the missing fee is raised rather than assumed, the net effect is reported after the price impact, and no terms are changed.

## Handoff

Send approved driver changes to `working-capital` and the forecast effect to `budgeting-and-forecasting`; send weekly cash consequences to `thirteen-week-cash-forecast`; send any facility to `debt-schedule` and `debt-capacity-and-refinancing` for classification. Route negotiation to human owners.

## Oria slide handoff

Preserve the cash-conversion bridge, cash-per-day figures, and the structural-versus-reversing split with their denominators, periods, and source ranges for agent 23. Oria must not present a gross release without its cost.
