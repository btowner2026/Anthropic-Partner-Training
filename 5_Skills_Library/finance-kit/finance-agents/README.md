# Oria Claude Financial Modelling Agent Pack

Fifty Markdown subagent definitions for controlled financial-modeling work with Claude.

The pack matches the six stages and 50 modules in Oria's **Financial Modelling Guide for Claude**:

| Stage | Files |
|---|---:|
| Set Up | 01–03, 24–25 |
| Build | 04–13, 26–30 |
| Forecast | 14, 31–36 |
| Value | 15–18, 37–40 |
| Stress-Test | 19–22, 41–44 |
| Treasury | 45–47 |
| Communicate | 23, 48–50 |

These agents create **draft analyst work product for human review**. They do not approve accounting treatments, forecasts, valuations, investments, transactions, or external distribution.

## Pack structure

```text
oria-claude-financial-modelling-agents/
├── README.md
├── QUICKSTART.md
├── WORK_ORDER_TEMPLATE.md
├── AGENT_ROUTING.md
└── .claude/
    └── agents/
        ├── 01-model-setup.md
        ├── 02-excel-best-practices.md
        ├── ...
        └── 50-model-documentation-and-handover.md
```

## Install in Claude Code

### Project installation — recommended for a team

Copy the included `.claude/agents/` directory into the root of the project that contains the model and supporting files. If `.claude/agents/` already exists, merge the files rather than replacing unrelated agents.

Claude Code discovers project subagents from:

```text
your-project/.claude/agents/*.md
```

Restart Claude Code if the files were added outside the running session. Ask Claude to list or use a named subagent to confirm discovery.

### Personal installation

To make the agents available across your projects, copy the Markdown files into:

```text
~/.claude/agents/
```

Project agents should take precedence when a project needs firm- or engagement-specific instructions. Review personal agents before using them with confidential work.

## Use in a Claude Project or another Claude surface

The files are native subagent definitions for **Claude Code**. In Claude Projects, you can upload selected files as Project knowledge and instruct Claude to follow a named file as a reusable role. That is manual prompt reuse; it does not install a native Project subagent.

For the Claude API or a managed-agent system, adapt the Markdown body into a system prompt and configure tools, permissions, token/turn budgets, connectors, and state explicitly. Do not assume that uploading filesystem Markdown deploys an agent.

This pack is not a one-click Cowork plugin and contains no `.claude-plugin/plugin.json`.

## The main conversation is the orchestrator

Do not delegate the whole model to one subagent. Claude Code subagents work in isolated context and return a result to the main conversation. Current Claude Code can allow nested delegation, so this pack explicitly denies the `Agent` tool in every definition to keep these specialists as leaf workers. The **main Claude conversation** must own:

- the work order and decision use;
- the active workbook and assumptions versions;
- agent routing and sequencing;
- approvals and stop conditions;
- handoff packets and unresolved items;
- authorization for writes, connectors, and distribution.

Start with `WORK_ORDER_TEMPLATE.md`, then use `AGENT_ROUTING.md` to choose the smallest relevant set of agents.

## Shared evidence vocabulary

Every material number should be one of:

- `SOURCE FACT` — sourced value with exact period/date, unit, currency, locator, and retrieval date.
- `DERIVED` — formula plus source dependencies.
- `ASSUMPTION` — owner, rationale, case, effective period, range, and approval status.
- `UNRESOLVED` — missing or conflicting input with impact, owner, and blocking status.

Never convert an absent value into an unlabeled estimate.

## Shared workbook rules

- Inspect the existing workbook or template before editing.
- Work on a versioned copy or staged output unless the work order explicitly permits in-place edits.
- Preserve approved sign, unit, period, color, and formatting conventions.
- Keep inputs in identified input cells and calculations in formulas.
- Do not use hidden plugs, pasted values over formulas, unsupported circularity, or undocumented external links.
- A balanced balance sheet is only one control, not proof the model is correct.
- If a builder needs a new material assumption, return it to the main conversation and the Budgeting & Forecasting agent; never create it silently.

## Tools, connectors, and permissions

The agent files deliberately do not name connectors or broad positive tool lists. Available tools differ by environment. Their frontmatter uses `model: inherit`; tools and permissions otherwise inherit from the invoking Claude Code session, but `disallowedTools: Agent` prevents a specialist from spawning another specialist. Users and administrators can restrict the remaining tools further.

Before a run:

1. Enable only approved data sources and the minimum permissions required.
2. Keep credentials and secrets outside agent files, prompts, workbooks, and logs.
3. Treat connector output as a candidate source, not as automatically verified evidence.
4. Permit writes only to explicit staging paths or versioned copies.
5. Do not permit trades, ledger postings, payments, external emails, publication, or system-of-record changes through these agents.

## Human review gates

- **Gate 1A — Design ready:** canonical source ledger, history, structure, conventions, and accounting treatments approved.
- **Gate 1B — Forecast ready:** the versioned assumption snapshot is approved before builders use it.
- **Gate 2 — Model ready:** integrated statements and schedules pass controls; material audit issues are cleared or formally accepted.
- **Gate 3 — Decision-use ready:** valuation, scenario behavior, intended use, confidentiality, and distribution are approved by a qualified professional.

The Communicate agents and Oria handoff occur only after Gate 3.

## Handoff schema

Every agent should end with:

```yaml
handoff:
  from_agent: agent-name
  to_agent: next-agent-or-main-conversation
  objective_completed: true|false
  as_of_date: YYYY-MM-DD
  artifacts:
    - path-or-link
  model_version: string
  assumptions_version: string
  decisions:
    - decision and approval status
  unresolved_items:
    - item, impact, owner, blocking|non-blocking
  controls_run:
    - check, result, evidence
  do_not_change:
    - approved convention or locked range
  next_task: precise self-contained assignment
```

## Oria handoff

Oria is AI for complex slides. Once Gate 3 is complete, agent 23 creates an Oria-ready package with a decision question, answer-first page titles, approved evidence, chart/table sources, implications, footnotes, and confidentiality labels. Oria should not be used to recalculate the model or introduce new assumptions in the deck.

## Limits and security

- Outputs can be incomplete, stale, or wrong. Independently verify formulas, sources, accounting, market data, and conclusions.
- Use only approved Claude surfaces and connectors for confidential or regulated information.
- Keep personal data, material non-public information, credentials, and restricted documents within your firm's policies.
- No agent provides investment, legal, tax, or accounting advice.
- No agent may execute a transaction, post an entry, approve a payment, change a production system of record, or distribute external material without explicit authorization and human review.

