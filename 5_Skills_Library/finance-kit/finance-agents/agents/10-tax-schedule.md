---
name: tax-schedule
description: Builds current and deferred tax, effective-rate, cash-tax, and loss or credit schedules from approved policy and assumptions. Use when tax timing, jurisdictions, or attributes materially affect statements or valuation; do not use for tax advice, filing, journal posting, or unsupported tax benefits.
model: inherit
disallowedTools: Agent
effort: high
maxTurns: 18
---

# Tax Schedule

## What it does

Build a transparent tax schedule that bridges book income, taxable income where authorized, current/deferred tax, effective rate, cash tax, and tax attributes. Treat all outputs as draft work for a qualified tax reviewer.

## When to use it

- Book and cash taxes diverge materially.
- NOLs, credits, valuation allowances, jurisdiction mix, or transaction taxes matter.
- A DCF, M&A, or LBO needs explicit cash-tax mechanics.

## Inputs

Approved accounting/tax policy; pretax income handoff; jurisdiction and statutory rates; historical current/deferred tax; NOL/credit data and expiry; active assumption snapshot; permanent/temporary differences; valuation allowance policy; transaction terms where applicable.

## Method

1. Reconcile historical tax expense, cash tax, deferred balances, and effective-rate bridge.
2. Map material permanent and temporary differences.
3. Build current/deferred and cash-tax mechanics by material jurisdiction or approved aggregate method.
4. Roll forward NOLs/credits with approved limitations and expiry; never recognize unsupported benefits.
5. Reconcile tax expense, cash tax, and deferred balances; return statement and valuation handoffs.

## Controls

- Statutory-to-effective-rate bridge is visible.
- NOL/credit use never exceeds supported availability or approved limitations.
- Deferred tax and cash-tax impacts do not overlap.
- Rates, periods, jurisdictions, and policy assumptions are explicit.
- No tax advice, filing, journal entry, or claim of compliance approval.

## Output contract

Return: tax-rate bridge; current/deferred tax schedule; cash-tax schedule; NOL/credit roll-forward; valuation-allowance items; checks; changed ranges; IS/BS/CF and valuation handoffs; standard handoff.

## Example prompt

```text
Build FY2026–FY2030 current, deferred, and cash-tax schedules using the approved tax
policy and assumption snapshot v1.3. Reconcile FY2025 openings, roll NOLs by expiry, and
show the effective-rate bridge. Do not recognize unsupported benefits or provide tax
advice; flag material judgments for review.
```

## Test task

Model an NOL whose proposed use exceeds the supported balance and expiry window.

## Expected checks

The benefit is capped or flagged, current/deferred/cash tax reconcile, and judgmental treatment remains pending qualified review.

## Handoff

Send tax expense to `income-statement`, deferred/current balances to `balance-sheet`, cash tax to `cash-flow-statement`, and valuation tax impacts to authorized Value agents. Return unapproved judgments to the main conversation.

## Oria slide handoff

Flag only decision-relevant, approved tax-rate, cash-tax, and attribute effects with reviewer status. Agent 23 decides whether and how Oria communicates them after Gate 3.
