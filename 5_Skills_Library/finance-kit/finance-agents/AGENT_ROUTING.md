# Agent routing and sequencing

**Prepared by Oria · AI for complex slides.**

The main Claude conversation routes these agents. Subagents are leaf workers: they receive a self-contained assignment, return the standard handoff, and do not coordinate one another.

## Roster

| # | Stage | Agent | Route when | Never use it to |
|---:|---|---|---|---|
| 01 | Set Up | `model-setup` | define architecture, interfaces, timeline, gates | build formulas before approval |
| 02 | Set Up | `excel-best-practices` | set or review workbook conventions | make forecast judgments |
| 03 | Set Up | `accounting-refresher` | create the canonical ledger and map accounting treatments | issue accounting approval |
| 04 | Build | `three-statement-model` | integrate approved schedules/statements | invent drivers or assumptions |
| 05 | Build | `revenue-drivers` | build driver-based revenue mechanics | use an unexplained top-line plug |
| 06 | Build | `operating-costs` | build cost and margin mechanics | choose arbitrary margin targets |
| 07 | Build | `working-capital` | build operating-balance roll-forwards | hide a cash or balance plug |
| 08 | Build | `capex-and-da` | build fixed-asset and D&A roll-forwards | invent asset lives or residuals |
| 09 | Build | `debt-schedule` | build debt, interest, liquidity, covenants | assume refinancing without approval |
| 10 | Build | `tax-schedule` | build tax and attribute schedules | provide tax advice or unsupported benefits |
| 11 | Build | `income-statement` | assemble the income statement from schedules | duplicate detailed schedule logic |
| 12 | Build | `balance-sheet` | assemble the balance sheet from roll-forwards | force balance with a plug |
| 13 | Build | `cash-flow-statement` | assemble and reconcile cash movements | treat cash as unexplained residual |
| 14 | Forecast | `budgeting-and-forecasting` | recast drivers and control forecast assumptions | edit formulas or approve its own assumptions |
| 15 | Value | `dcf-valuation` | build DCF from an audited model | issue an approved target price |
| 16 | Value | `comparable-companies` | build relative valuation from governed peers | mix periods or definitions silently |
| 17 | Value | `ma-model` | build an authorized acquisition case | recommend or execute a transaction |
| 18 | Value | `lbo-model` | build leveraged returns and debt paydown | invent financing or exit terms |
| 19 | Stress-Test | `model-circularity` | diagnose/implement approved circularity | conceal non-convergence |
| 20 | Stress-Test | `scenario-analysis` | build coherent driver-based cases | overwrite the locked base case |
| 21 | Stress-Test | `sensitivity-analysis` | build/test one- and two-way sensitivities | substitute grids for coherent scenarios |
| 22 | Stress-Test | `model-checks` | independently audit workbook end state | silently repair or professionally approve |
| 23 | Communicate | `outputs-and-automation` | package approved outputs and Oria brief | recalculate the model or distribute materials |
| 24 | Set Up | `data-sources-and-ingestion` | tie every historical figure to a sourced locator | estimate a missing figure or set accounting policy |
| 25 | Set Up | `chart-of-accounts-mapping` | map a client ledger onto model line items | set accounting policy or approve a reclassification |
| 26 | Build | `equity-schedule` | build basic and diluted share roll-forwards | value the company or state a target price |
| 27 | Build | `leases-and-off-balance-sheet` | build lease schedules and register commitments | select the standard or capitalize without approval |
| 28 | Build | `segment-and-consolidation` | build segment and entity roll-ups and eliminations | invent a split the ledger cannot support |
| 29 | Build | `fx-translation` | translate functional currencies and reconcile CTA | forecast rates or reclassify a functional currency |
| 30 | Build | `deferred-revenue-and-backlog` | connect bookings, billings, backlog, and revenue | set the recognition policy or invent contract terms |
| 31 | Forecast | `driver-based-planning` | rebuild a top-down target as a bottom-up driver plan | approve the target or edit builder formulas |
| 32 | Forecast | `rolling-forecast` | maintain a re-based live forward view | restate closed periods or approve its own cycle |
| 33 | Forecast | `budget-bridge` | reconcile two approved plan versions step by step | invent a balancing plug or re-forecast the drivers |
| 34 | Forecast | `variance-analysis` | explain actual against budget and prior year after close | re-forecast, restate actuals, or rate performance |
| 35 | Forecast | `headcount-and-compensation-plan` | build bottom-up personnel cost into operating costs | set salary bands or model individual pay |
| 36 | Forecast | `cost-allocation-and-transfer-pricing` | allocate shared cost on an approved basis | set statutory transfer prices or approve tax positions |
| 37 | Value | `sum-of-the-parts` | value a group segment by segment and bridge to equity | invent segment data or assume a holding discount |
| 38 | Value | `accretion-dilution` | test the EPS effect of an authorized transaction | build the full deal model or recommend a deal |
| 39 | Value | `cost-of-capital-build` | evidence a WACC and rank its sensitive inputs | solve a rate back from a wanted value |
| 40 | Value | `returns-and-value-creation-bridge` | attribute a return to growth, multiple, leverage, cash | re-underwrite a deal or issue investment advice |
| 41 | Stress-Test | `monte-carlo-simulation` | run defended distributional analysis on key drivers | replace causal scenarios or imply real-world probability |
| 42 | Stress-Test | `covenant-and-liquidity-stress` | locate the first breach period and tightest headroom | assume a waiver or refinancing, or advise on financing |
| 43 | Stress-Test | `back-testing-and-forecast-accuracy` | score prior vintages and correct persistent bias | restate history or re-run a vintage on today's information |
| 44 | Stress-Test | `model-audit-trail` | bind every material output to version, owner, and gate | edit calculations or grant professional sign-off |
| 45 | Stress-Test | `thirteen-week-cash-forecast` | build weekly direct-method liquidity and variance | replace the accrual model or approve financing |
| 46 | Stress-Test | `working-capital-optimisation` | price cash-conversion levers and test durability | rebuild working-capital mechanics or approve a lever |
| 47 | Stress-Test | `debt-capacity-and-refinancing` | size sustainable leverage and test the maturity wall | arrange financing or assume an undocumented refinancing |
| 48 | Communicate | `board-reporting-pack` | assemble the board finance section from approved output | recompute a figure or recommend a course of action |
| 49 | Communicate | `kpi-dashboard-design` | define the few measures that would change a decision | build the calculations or set performance targets |
| 50 | Communicate | `model-documentation-and-handover` | write the handover a successor can own the model from | fix defects found while documenting or certify it |

## Default sequence and gates

```text
01 → 02 → 24 → 25 → 03
  ↓
GATE 1A: approve canonical evidence ledger, history, architecture, conventions, accounting treatment
  ↓
14 prepares assumption register and driver proposals, with 31 / 32 / 35 where the plan needs them
  ↓
GATE 1B: approve assumption snapshot
  ↓
05 / 06 / 07 / 08 / 09 / 10 as required, plus 26 / 27 / 28 / 29 / 30 / 36 where material
  ↓
11 → 12 → 13 → 04 initial integration → 19 if required → 04 final refresh → 22
  ↓
GATE 2: approve integrated base model
  ↓
39 → 15 / 16 / 17 / 18 as authorized → 37 / 38 / 40 as authorized
  ↓
20 → approved changes through 14 → relevant builders → 11 → 12 → 13 → 04 → relevant Value agents
  ↓
21 → 41 if authorized → 42 → 45 / 46 / 47 where liquidity or leverage is live → 22 re-test
  ↓
33 / 34 / 43 whenever a plan version or reporting period closes
  ↓
GATE 3: approve valuation, stress behavior, intended use, distribution
  ↓
23 → Oria → final human review
  ↓
48 / 49 / 50 for recurring reporting, dashboards, and handover
```

## Parallelism rules

- The main conversation inventories approved sources; independent collection may run in parallel. Agents 24 and 25 establish provenance and the ledger mapping first, then agent 03 consolidates one canonical evidence ledger before historical mapping and Gate 1A.
- Agents 05–10 may run in parallel only after model architecture, interfaces, and assumptions are frozen. Agents 26–30 join them only where the line is material; an immaterial lease, segment, or currency exposure stays inside its parent schedule.
- Route statements sequentially: 11 Income Statement → 12 Balance Sheet → 13 Cash Flow Statement. Only independent preparatory checks within them may run in parallel.
- Valuation methods may run in parallel after Gate 2, but they must use one valuation date and the same approved model version. Agent 39 completes before any discounted method, and 15, 17, 18, 37, and 40 must share one approved cost-of-capital version.
- Scenario ideas may be explored in parallel; implementation routes through agent 14 and the responsible builders. Planning agents 31–36 propose through the register, never around it, and no planning output reaches a builder except inside an approved snapshot.
- Agent 22 must be independent of the builders and run at least twice: before valuation and after material valuation/scenario changes.
- Treasury agents 45–47 run on the approved model rather than beside it: 45 reconciles to the approved cash-flow statement, 46 and 47 consume its output, and none of the three may commit, defer, or arrange funding.
- Agent 43 requires dated forecast vintages and closed actuals; it never scores the live forecast it is run alongside.
- Agent 44 runs alongside the whole sequence rather than at one point in it. It must be current at every gate and is checked, not written, at Gate 3.
- Agent 23 must not begin from a draft model to save time. Agents 48–50 are subject to the same rule; 49 defines measures over approved outputs and 50 documents the model as approved, and neither computes.

## Routing failures to avoid

- Asking agent 04 to source, forecast, build, value, and audit the entire model.
- Letting parallel builders use different assumptions versions.
- Sending a missing input directly from a builder into an invented hardcode.
- Asking agent 20 to change output cells rather than causal drivers.
- Letting agent 31 or 32 push a driver change into a builder without a new approved snapshot.
- Letting a valuation builder be its only reviewer.
- Running agent 45 from ledger cash rather than reconciled bank balances.
- Reading an agent 41 percentile as the probability of a real-world event.
- Asking agent 48 or 49 to close a reporting gap with a number the model never produced.
- Creating Oria slides before Gate 3, causing model/deck drift.

## Oria route

Agent 23 prepares the package; Oria creates the complex slides; a human reviewer approves the final deck. The package must include approved model/audit versions, audience, decision question, slide limit, headline, evidence, chart/table source, implication, footnote, confidentiality label, and unresolved items.
