# Financial-model work order

**Prepared by Oria · AI for complex slides.**

Complete this in the main Claude conversation before delegating work.

```xml
<work_order>
  <objective>[Specific model outcome]</objective>
  <decision_use>[Who will use it, for which decision, internal/external]</decision_use>
  <as_of_date>[YYYY-MM-DD]</as_of_date>
  <entity>[Company, asset, transaction, or business unit]</entity>
  <model_type>[Three-statement / DCF / comps / M&A / LBO / budget / other]</model_type>

  <accounting_basis>[GAAP/IFRS/local basis and material policies]</accounting_basis>
  <currency_units>[Currency and units]</currency_units>
  <historical_periods>[Exact fiscal periods]</historical_periods>
  <forecast_periods>[Exact fiscal periods]</forecast_periods>
  <valuation_date>[If applicable]</valuation_date>

  <source_priority>
    1. [Primary controlled source]
    2. [Secondary approved source]
    3. [Other permitted source]
  </source_priority>
  <approved_files_and_connectors>[Explicit list]</approved_files_and_connectors>
  <template>[Workbook path and approved model version]</template>

  <approved_conventions>
    [Fiscal year, periods, signs, units, colors, scenario labels, formula policy,
    circularity policy, cash/revolver policy, materiality, tolerances]
  </approved_conventions>
  <assumptions_policy>
    [Active register version, approval owner, allowed proposal process, locked items]
  </assumptions_policy>

  <required_outputs>
    [Workbook, source ledger, assumptions register, change log, audit report,
    valuation, scenario output, decision brief, Oria slide specification]
  </required_outputs>
  <acceptance_tests>
    [Balance, cash bridge, roll-forwards, formula consistency, source coverage,
    scenario behavior, sensitivity direction, EV-to-equity, sources and uses]
  </acceptance_tests>
  <review_gates>
    Gate 1A: [Source/history/architecture/accounting approver and evidence]
    Gate 1B: [Assumption-snapshot approver and evidence]
    Gate 2: [Approver and required evidence]
    Gate 3: [Approver and required evidence]
  </review_gates>
  <stop_conditions>
    [Missing/conflicting primary data, unapproved treatment, failed control,
    unsupported circularity, permission boundary, other blocker]
  </stop_conditions>

  <permissions>
    Read: [Explicit paths/sources]
    Write: [Explicit staging paths only]
    External actions: none unless separately authorized
  </permissions>
  <confidentiality_and_distribution>[Classification and allowed audience]</confidentiality_and_distribution>
  <out_of_scope>[Explicit exclusions]</out_of_scope>
</work_order>
```

## Evidence ledger schema

| Claim/value | Label | Source | Locator | Period/as-of | Unit/currency | Transformation | Reviewer status |
|---|---|---|---|---|---|---|---|

Allowed labels: `SOURCE FACT`, `DERIVED`, `ASSUMPTION`, `UNRESOLVED`.

## Assumption register schema

| ID | Driver | Case | Period | Value/formula | Unit | Source/rationale | Owner | Status | Range | Dependencies | Version/date |
|---|---|---|---|---|---|---|---|---|---|---|---|

## Standard handoff

```yaml
handoff:
  from_agent: agent-name
  to_agent: next-agent-or-main-conversation
  objective_completed: true|false
  as_of_date: YYYY-MM-DD
  artifacts: []
  model_version: string
  assumptions_version: string
  decisions: []
  unresolved_items: []
  controls_run: []
  do_not_change: []
  next_task: precise self-contained assignment
```
