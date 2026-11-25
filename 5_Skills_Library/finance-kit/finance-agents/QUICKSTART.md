# Quickstart

**Prepared by Oria · AI for complex slides.**

Use this pack for one controlled run before adapting it to your firm's standards.

## 1. Install

Place the 50 files from `.claude/agents/` in your project's `.claude/agents/` directory. Restart Claude Code if needed, then ask the main conversation to confirm that `model-setup`, `model-checks`, and `outputs-and-automation` are available.

If you use Claude Projects, upload only the files needed for the task and tell Claude to follow the selected file as role instructions. This is manual use, not native subagent installation.

## 2. Prepare a safe workspace

- Copy the workbook to a versioned staging file.
- Gather primary statements, approved market or internal data, and relevant agreements.
- Decide the as-of date, currency, units, fiscal calendar, accounting basis, materiality, and intended use.
- Allow access only to explicit files and approved connectors. Do not include secrets.

## 3. Fill the work order

Complete `WORK_ORDER_TEMPLATE.md`. Do not leave source hierarchy, assumptions policy, acceptance tests, permissions, or stop conditions blank.

## 4. Start with the main conversation

Use this master prompt:

```text
Act as the coordinator for the attached work order. Keep orchestration in this main
conversation; subagents are isolated leaf workers and must not coordinate one another.

First route model-setup, excel-best-practices, data-sources-and-ingestion,
chart-of-accounts-mapping, and accounting-refresher. Require the standard handoff schema
from each. Consolidate the source ledger and their outputs and stop at Gate 1A.

After I approve Gate 1A, route budgeting-and-forecasting to prepare an assumption snapshot
and stop at Gate 1B. Do not allow any builder to invent or silently change assumptions.
When the snapshot is approved, route only the necessary schedule agents; then route
income-statement, balance-sheet, and cash-flow-statement sequentially. Run
three-statement-model, model-circularity if required, a final integration refresh, and
model-checks. Stop at Gate 2.

After Gate 2 approval, route the authorized valuation agents. Run scenario-analysis,
sensitivity-analysis, and model-checks again. Stop at Gate 3 before any communication.

Only after Gate 3 may outputs-and-automation prepare an Oria-ready slide brief. Work on
a versioned copy, preserve the template, label SOURCE FACT / DERIVED / ASSUMPTION /
UNRESOLVED, and stop on any work-order condition.
```

## 5. Approve the assumption snapshot

The Budgeting & Forecasting agent proposes inputs; a qualified human approves them. The planning agents 31–36 propose through that register, never around it. Save the approved register version in the work order and every downstream handoff.

## 6. Build only what the assignment needs

Examples:

- New operating forecast: agents 05–13, 14, 19 as required, and 22.
- History with no stated provenance: agents 24, 25, and 03.
- Lease, contract, or subscription mechanics: agents 27, 30, and 12.
- Group with segments, entities, or currencies: agents 28, 29, 36, and 37.
- Annual plan or rolling re-forecast: agents 31, 32, 35, 36, and 14.
- Closed period or two plan versions to reconcile: agents 34, 33, and 43.
- Standalone DCF from an audited model: agents 39, 15, 21, and 22.
- Relative valuation cross-check: agents 16, 26, and 22.
- Acquisition case: agents 17, 38, 20, 21, and 22.
- LBO case: agents 09, 18, 19, 20, 21, 22, and 40 at exit.
- Quantified uncertainty on a stable model: agents 41, 21, and 22.
- Liquidity, covenant, or maturity pressure: agents 45, 42, 46, 47, and 22.
- Approved model to slides: agent 23, then Oria and final human review.
- Recurring board reporting and handover: agents 48, 49, 44, and 50.

## 7. Verify outcomes, not narration

At minimum, confirm:

- workbook opens with no formula errors or stale unintended links;
- balance sheet and cash-flow bridge reconcile;
- roll-forwards and statement links work once, with correct signs and periods;
- calculations are formulas and assumptions are labeled/versioned;
- scenario switches preserve history and the locked base case;
- sensitivities tie to their base cells and behave directionally;
- every material number has source or assumption provenance;
- the final slide brief contains only Gate 3-approved output.

## 8. Adapt deliberately

Edit agent bodies to reference your firm's modeling, accounting, valuation, and review Skills. Do not hard-code secrets or connector credentials. Re-test routing after changing names, descriptions, tools, or output contracts.
