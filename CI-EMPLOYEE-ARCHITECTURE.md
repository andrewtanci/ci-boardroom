# CI Boardroom — Modular Employee Architecture

**Version:** 0.1  
**Date:** 16 Sep 2026  
**Status:** Architecture specification for controlled implementation and testing

## 1. Core Concept

Treat each CI specialist as a modular **Employee Folder**.

An Employee Folder is not merely a persona or attitude prompt. It is a bounded capability package containing the specialist's role, domain methods, skills, checks, tools, context, challenge responsibilities, escalation boundaries and tests.

This allows a human administrator to:

- hire = add/enable an Employee Folder;
- remove = disable/remove an Employee Folder;
- upgrade = add or replace Skills inside that Employee Folder;
- retrain = update methods/checks/context;
- reassign = change routing/scope;
- audit = inspect exactly what capability package was active;
- test = assess the Employee Folder independently before deployment.

The metaphor is for usability. The underlying architecture remains explicit and machine-readable enough to support testing and orchestration.

## 2. Proposed Main Structure

```text
CI-BOARDROOM/
├── GOVERNANCE/
│   ├── BOARDROOM.md
│   ├── EXECUTION-HARD-GATES.md
│   ├── OUTCOME-TESTS.md
│   └── LOAD-MANIFEST.md
│
├── EMPLOYEES/
│   ├── CEO-INTEGRATOR/
│   ├── EVIDENCE-RESEARCH/
│   ├── FINANCE/
│   ├── COMMERCIAL-MARKET/
│   ├── OPERATIONS/
│   ├── TECHNICAL/
│   ├── CUSTOMER-PEOPLE/
│   └── RISK-LEGAL/
│
├── SHARED-WORKSPACE/
│   ├── DECISION-LEDGER.md
│   ├── EVIDENCE-REGISTER.md
│   ├── CHALLENGE-REGISTER.md
│   └── DECISION-STATE.md
│
├── SKILL-LIBRARY/
│   └── reusable skills that may be installed into Employee Folders
│
└── TESTS/
    ├── EMPLOYEE-TESTS/
    ├── INTEGRATION-TESTS/
    └── REGRESSION-TESTS/
```

Do not migrate existing canonical files blindly. This is the target architecture; migration occurs only after compatibility and benchmark tests.

## 3. Standard Employee Folder

Every Employee Folder should follow a common contract:

```text
EMPLOYEES/FINANCE/
├── EMPLOYEE.md
├── ROLE.md
├── METHODS.md
├── CHECKS.md
├── CHALLENGE.md
├── BOUNDARIES.md
├── CONTEXT/
├── SKILLS/
└── TESTS/
```

### EMPLOYEE.md
Machine/human-readable manifest:

- employee ID;
- display name;
- purpose;
- version;
- enabled/disabled status;
- capabilities;
- required inputs;
- allowed outputs;
- dependencies;
- installed Skills;
- escalation targets;
- last validated test version.

### ROLE.md
Defines what the specialist owns and explicitly does **not** own.

### METHODS.md
Contains actual practitioner methods, calculations, frameworks, evidence standards and domain workflow. This is the specialist's substantive expertise.

### CHECKS.md
Mandatory pre-output checks and common failure modes.

### CHALLENGE.md
Defines what this specialist must challenge in other specialists' work and what evidence can reverse its own position.

### BOUNDARIES.md
Defines authority, safety, professional-review and escalation limits.

### CONTEXT/
Domain references, organisation-specific context and approved knowledge packages. Context must be versioned/provenanced where material.

### SKILLS/
Plug-in capabilities installed for this Employee. Skills should be narrow, testable and removable where possible.

### TESTS/
Employee-specific competence, regression and failure tests.

## 4. Skills Are Not Employees

Keep the distinction clean:

- **Employee** = role/capability container.
- **Skill** = a specific reusable capability.
- **Context** = information the Employee may use.
- **Tool** = mechanism the Employee may invoke.
- **Governance** = rules all Employees must obey.

Example:

A Finance Employee might contain Skills for:

- unit economics;
- cash-flow/runway analysis;
- valuation;
- scenario analysis;
- financing-term analysis.

Upgrading valuation should not require rewriting the whole Finance Employee.

A Skill may potentially be shared by multiple Employees if its contract and tests support that use.

## 5. Hire / Remove / Upgrade Operations

### Hire

Add an Employee Folder, validate its manifest/dependencies, run Employee tests, run integration tests, then enable routing.

### Remove

Disable routing first. Verify no mandatory dependency becomes orphaned. Run integration tests. Then remove/archive if desired.

**Do not assume deleting a folder is always safe.** A specialist may be required by another Employee, workflow, test or regulatory control.

### Upgrade

Change a Skill/method/context package, increment its version, run its tests, then rerun affected Employee/integration/regression tests.

### Rollback

Retain sufficient version history to restore the last validated package when an upgrade degrades performance.

## 6. CEO / Chief Integrator

The CEO/Integrator is an orchestrator, not an all-knowing super-expert.

Responsibilities:

1. identify the human's real objective and constraints;
2. determine consequence level;
3. select only relevant Employees;
4. ensure Reality Contact before accepting the plan;
5. give specialists the appropriate evidence/state;
6. expose material disagreements rather than forcing consensus;
7. request additional evidence where a specialist identifies a reversible uncertainty;
8. integrate specialist outputs;
9. produce the strongest evidence-grounded answer;
10. preserve named human decision authority.

The CEO should not silently overwrite a specialist's evidence-based objection merely to create a clean consensus.

## 7. Shared Workspace Instead of Endless Agent Conversation

Employees should communicate through structured shared state wherever possible.

### Decision Ledger

Minimum fields:

| Field | Purpose |
|---|---|
| Issue | decision component under review |
| Claim | current proposition |
| Evidence | supporting/contradicting evidence |
| Source status | verified / inferred / unresolved |
| Employee position | specialist assessment |
| Challenge | objection from another Employee |
| Reversal condition | evidence that would change position |
| Status | open / verify / resolved / stop-escalate |
| Owner | Employee responsible for next analytical action |

### Evidence Register

Stores evidence references, provenance, date/version/jurisdiction where relevant, verification status and which claims depend on them.

### Challenge Register

Preserves substantive disagreements and whether they were resolved by evidence, calculation, human judgment or remain unresolved.

### Decision State

Contains the current objective, constraints, options, locked human preferences, unresolved questions, authority level and final human decision-owner.

The shared workspace is the coordination substrate. Free-form agent dialogue is secondary and should not become the only record of reasoning state.

## 8. Dynamic Staffing

Do not load every Employee for every question.

The CEO selects the smallest council that covers material consequences.

Examples:

- simple nutrition comparison: relevant health/nutrition specialist + evidence/research; no corporate finance specialist;
- acquisition: finance + commercial + operations + risk/legal + evidence;
- software architecture: technical + operations + security/risk + commercial if economics matter;
- assessment design: adult-learning/assessment + evidence + compliance/quality where applicable.

This controls cost, latency, context pollution and theatrical over-deliberation.

## 9. Reality Contact for Every Employee

Before an Employee's contribution is accepted, ask:

> What would we need to observe to know this specialist's conclusion is working or true, and can we actually observe it?

Each Employee must distinguish:

- evidence it actually inspected;
- evidence reasonably retrievable;
- assumptions;
- unknowns;
- outcome signals that could later validate/refute its conclusion.

## 10. Human-Facing Management Model

The folder architecture should eventually make CI understandable without exposing implementation complexity.

A user could conceptually see:

**My Boardroom**

- CEO / Chief Integrator — Active
- Finance — Active
- Market — Active
- Operations — Active
- Risk & Legal — Active
- Employee / People — Inactive

Possible management actions:

- Add Employee
- Disable Employee
- Upgrade Skills
- Inspect Skills
- Run Assessment
- View Last Validation
- View Challenges

The UI metaphor must not falsely imply that an Employee is a human, licensed professional or independently accountable person. It is an AI capability package.

## 11. Assessment Before Deployment

Every Employee should be independently assessable.

Assessment layers:

1. **Skill test** — can installed Skill perform its bounded task?
2. **Employee test** — can the Employee perform its domain role?
3. **Challenge test** — will it identify material errors in another Employee's work?
4. **Integration test** — does adding/removing it improve rather than degrade Boardroom performance?
5. **Regression test** — do previously corrected failures remain corrected?
6. **Reality test** — can claimed outputs/outcomes actually be observed and verified?

An Employee should not be marked validated merely because its files exist.

## 12. Migration Rule

Current CI Boardroom remains canonical until the modular architecture proves equivalent or better performance.

Migration sequence:

1. freeze current Boardroom baseline;
2. build CEO + three high-value Employee Folders first;
3. extract existing methods without losing governance;
4. implement shared Decision/Evidence/Challenge state;
5. run identical benchmark cases against current monolithic Boardroom and modular Boardroom;
6. compare accuracy, material-fact capture, unsupported claims, latency/cost and human usability;
7. fix regressions;
8. only then migrate additional specialist roles;
9. promote modular architecture to canonical runtime only after defined acceptance criteria pass.

**Cleaner architecture is a hypothesis until measured.**

## 13. Initial Build Recommendation

Start with four Employees:

1. **CEO / Chief Integrator** — routing, integration, challenge resolution and human-authority preservation.
2. **Evidence / Research** — retrieval, source integrity, verification and Reality Contact.
3. **Finance / Commercial Reality** — economics, quantitative consequences and business viability.
4. **Operations / Technical Reality** — feasibility, execution constraints, implementation and failure modes.

Risk/legal/customer/people/domain-specific Employees follow based on benchmark coverage and actual use.

This minimum architecture is large enough to test modularity but small enough to diagnose failures.

---

## Governing Principle

> **Employee Folders make capability modular. Skills make expertise upgradeable. Shared state makes challenge inspectable. Tests make capability claims falsifiable. The named human remains the decision-owner.**
