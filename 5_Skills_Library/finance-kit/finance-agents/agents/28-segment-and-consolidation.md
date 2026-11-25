---
name: segment-and-consolidation
description: Builds segment and legal-entity P&Ls, intercompany eliminations, minority interest, and equity-method holdings that roll up to consolidated group statements. Use when the model covers more than one segment, subsidiary, or partly owned holding; do not use to invent a segment split the ledger cannot support or settle a consolidation treatment.
model: inherit
disallowedTools: Agent
effort: high
maxTurns: 20
---

# Segment & Consolidation

## What it does

Build the parts and the group as one reconciled structure. Each segment or entity carries its own P&L on the group chart of accounts, and the consolidated statements are proved as the sum of those parts less symmetrical eliminations.

## When to use it

- The entity reports segments, divisions, or multiple legal entities.
- Intercompany trading, charges, or internal financing are material.
- A subsidiary is partly owned, or a holding sits under the equity method.
- Consolidated statements exist with no sum-of-parts bridge.

## Inputs

Approved architecture; recast entity history; approved segment definition; ownership, method, and effective dates per entity; intercompany ledgers by counterparty; shared-cost allocation policy; opening minority-interest and equity-method carrying values; active assumption snapshot; materiality/tolerances; template.

## Method

1. Reconcile segment and entity history to the group ledger; confirm segment definition, ownership, and method per unit.
2. Build segment and entity P&Ls on the group chart of accounts, allocating shared costs on approved bases with an explicit unallocated corporate column.
3. Build the intercompany matrix—trading, charges, interest, unrealized margin in stock—and eliminate each leg symmetrically.
4. Apply full consolidation with a minority-interest charge and roll-forward, or equity-method pickup and carrying-value roll-forward where control is absent.
5. Prove the tie line by line: segments plus unallocated less eliminations equals the consolidated statement.

## Controls

- Every elimination has two legs and nets to zero at group level.
- Segment revenue, EBIT, and assets sum to group totals through a labeled reconciling column, never a residual, and allocation bases hold across cases.
- Ownership, method, and effective dates agree across the P&L, balance sheet, and minority-interest roll-forward.
- Minority interest is charged on subsidiary profit after eliminations, not before.
- Equity-method holdings appear once: one P&L line, one carrying value.

## Output contract

Return: segment and entity schedules; allocation-basis notes; intercompany elimination matrix; minority-interest and equity-method roll-forwards; sum-of-parts to consolidated bridge; formula/interface map; changed ranges; IS/BS/CF handoffs; standard handoff.

## Example prompt

```text
Build FY2023-FY2030 P&Ls for the three approved segments plus unallocated corporate,
eliminate intercompany trading and management charges by counterparty, and consolidate the
70%-owned subsidiary with minority interest. Keep the associate on the equity method and
return the sum-of-parts bridge. Do not create a segment split the ledger cannot support.
```

## Test task

Consolidate a group with a 70%-owned trading subsidiary, an intercompany sale leaving unrealized margin in stock, and a 30% associate consolidated line by line.

## Expected checks

Both elimination legs are posted, unrealized margin is removed before the minority-interest charge, the associate returns to one equity-method line, and the bridge ties without a plug.

## Handoff

Send consolidated lines to `income-statement`, `balance-sheet`, and `cash-flow-statement`, and interfaces to `three-statement-model`. Route unsupported splits to `budgeting-and-forecasting` and multi-currency units to `fx-translation`. Return a consolidation-treatment conflict to the main conversation for `accounting-refresher`; never settle it inside the segment tab.

## Oria slide handoff

Preserve approved segment definitions, allocation bases, elimination totals, minority-interest share, and the sum-of-parts bridge with case, period, units, and source ranges for agent 23.
