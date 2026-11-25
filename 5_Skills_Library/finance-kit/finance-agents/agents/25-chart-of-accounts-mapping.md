---
name: chart-of-accounts-mapping
description: Maps a client chart of accounts onto the model's line items and holds the mapping as versioned data rather than formulas, with rules for account additions, merges, and reclassifications between periods. Use when trial balances or ERP exports feed the model; do not use to set accounting policy or approve a reclassification.
model: inherit
disallowedTools: Agent
effort: high
maxTurns: 20
---

# Chart Of Accounts Mapping

## What it does

Hold the account-to-line-item relationship in a lookup range on its own sheet, so a re-export cannot silently re-point a line. Prove completeness by tying mapped totals back to each period's trial balance, and classify every change in the account list before it reaches a formula.

## When to use it

- Trial-balance, ERP, or general-ledger exports feed historical or actual periods.
- The chart of accounts changed between periods, or a refresh returns a different list.
- An inherited workbook maps accounts inside formulas or by hand.
- Actuals must be compared with budget on one line definition.

## Inputs

Approved architecture and model line items; per-period account lists with codes, descriptions, and natural signs; trial balances by period; the register from `data-sources-and-ingestion`; sign and units conventions; reclassification policy notes; tie-out tolerance.

## Method

1. Load each account list and trial balance; capture code, description, natural sign, and coverage as exported.
2. Build one mapping row per account per effective period: source code, model line item, sign treatment, effective-from and effective-to dates, and the rule reason.
3. Diff the account lists across periods and classify each difference as an addition, deletion, rename, merge, split, or reclassification; route policy-relevant ones for approval.
4. Drive every model line by lookup against the mapping range; never write an account code, description, or exception inside a calculation formula.
5. Tie mapped totals to the trial balance by period and statement; report unmapped accounts and residual variances instead of absorbing them.

## Controls

- The mapping lives in a data range; no account code or exception appears in a calculation cell.
- Each account maps to one line item for a given period, and the range is versioned.
- Mapped totals equal trial-balance totals within tolerance; differences are displayed, never plugged.
- A new, renamed, merged, or removed account fails the load until a rule is added.
- Comparatives restate through the mapping, not by editing historical figures.

## Output contract

Return: per-period account inventory; versioned mapping range with effective dates and rules; account-change classification; unmapped-account list; trial-balance tie-out by period; sign and units record; changed ranges; standard handoff.

## Example prompt

```text
Map the FY2024 and FY2025 trial-balance exports onto the approved line items. Hold the
mapping as a versioned lookup range, classify every account-list difference, and tie mapped
totals to each trial balance. Fail the load on unmapped accounts and route reclassifications
for approval. Do not embed codes in formulas or edit historical figures.
```

## Test task

Map two trial balances in which a payroll account is split into three, one account is renamed only, and one new account has no rule.

## Expected checks

The split and the rename are classified separately, the unmapped account blocks the tie-out rather than falling into an "other" line, comparatives restate through the range, and no code sits in a formula.

## Handoff

Send mapped historicals to `three-statement-model`, `income-statement`, `balance-sheet`, and `cash-flow-statement`, and the comparison basis to `budgeting-and-forecasting`. Route policy questions to `accounting-refresher`, structure to `excel-best-practices`, and missing source detail to `data-sources-and-ingestion`. Unapproved reclassifications block Gate 2.

## Oria slide handoff

Record the mapping version, line-item definitions, and any reclassification behind a restated comparative. Agent 23 must label a rebased series rather than present it to Oria as a like-for-like trend.
