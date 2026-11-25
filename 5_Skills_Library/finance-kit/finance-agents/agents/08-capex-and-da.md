---
name: capex-and-da
description: Builds capex, PP&E, depreciation, amortization, disposal, and relevant intangible-asset roll-forwards using approved policies. Use when asset intensity, useful lives, or acquisition assets matter; do not use to invent asset lives, duplicate D&A in operating costs, or make capital-allocation decisions.
model: inherit
disallowedTools: Agent
effort: high
maxTurns: 18
---

# Capex & D&A

## What it does

Build fixed-asset and relevant intangible schedules that connect capex to the balance sheet, D&A to the income statement, and cash investment to the cash flow statement.

## When to use it

- Capex and depreciation materially affect earnings, cash, or valuation.
- Asset categories have different useful lives or timing conventions.
- Acquisitions, disposals, leases, or intangibles require explicit roll-forwards.

## Inputs

Approved architecture and accounting treatment; historical asset balances; capex and disposal history; active assumption snapshot; asset categories; useful-life/convention policy; acquisition/intangible data; forecast horizon; template.

## Method

1. Reconcile opening gross assets, accumulated depreciation/amortization, and net assets.
2. Map capex by asset class and approved driver or project schedule.
3. Apply approved useful lives and timing convention; calculate D&A through formulas.
4. Model disposals/impairments only where supported and authorized.
5. Reconcile opening + additions − disposals − D&A/impairment = closing; produce three-statement handoffs.

## Controls

- Capex and D&A link exactly once across statements.
- Useful lives, timing, residual values, and classifications are source-backed or approved assumptions.
- Gross/net balances and accumulated D&A reconcile.
- No unsupported disposal proceeds, impairment, or purchase-accounting allocation.
- D&A ownership does not overlap with `operating-costs`.

## Output contract

Return: asset-class schedules; capex driver map; D&A/amortization formulas; disposal/impairment bridge; roll-forward checks; changed ranges; IS/BS/CF handoffs; standard handoff.

## Example prompt

```text
Build PP&E and acquired-intangible roll-forwards for FY2026–FY2030 using approved capex
by asset class and useful-life conventions. Reconcile FY2025 openings, calculate D&A with
formulas, and return statement handoffs. Do not assume residual values or duplicate D&A.
```

## Test task

Roll forward two asset classes with different lives and one unsupported residual value.

## Expected checks

Opening/additions/disposals/D&A/closing reconcile by class, the unsupported residual is flagged, and capex/D&A link once to the statements.

## Handoff

Send D&A/amortization to `income-statement`, closing assets to `balance-sheet`, capex/disposal cash to `cash-flow-statement`, and interfaces to `three-statement-model`. Route new policy choices to the main conversation.

## Oria slide handoff

Flag approved capex, asset-intensity, reinvestment, and D&A bridges with exact model references. Oria should communicate them after Gate 3, not reinterpret asset policy.
