# CI Boardroom — External Evidence Engine

**Version:** 0.1  
**Date:** 16 Sep 2026  
**Purpose:** operationalise independent case creation, blinded practitioner judging, and failure-taxonomy learning without slowing the engineering loop.

---

## 1. Strategic Role

CI must distinguish three assets:

1. **Rules** — public and copyable.
2. **Evidence** — independently generated proof that the rules improve decisions.
3. **Learning system** — accumulated real failure modes, controls, tests and recurrence data.

The durable asset is not a static prompt. It is the evidence-and-learning loop.

This file operationalises the external dependency identified by the benchmark: non-CI case authors and credible external judges.

---

## 2. War Story Extraction Protocol

Do not ask domain practitioners to "write an AI benchmark case." Ask them to reconstruct a real decision failure or near miss.

### Interview opening

> Tell me about a real decision where the people involved had substantial information but still made, or nearly made, the wrong choice. What looked obvious at the time? What small fact, hidden constraint, behavioural reality or second-order effect changed the decision? When did the team discover it?

### Required probes

Ask only enough to reconstruct the decision:

- What was the actual objective?
- What options were genuinely available at the time?
- What evidence existed **before** the decision?
- What evidence was unavailable until later?
- What did the group initially believe?
- What was the strongest plausible wrong answer?
- What material fact or constraint was overlooked?
- Could a diligent decision-maker have found it ex ante?
- What would a competent practitioner have checked?
- What would have changed the decision?
- What happened afterward?
- Which parts of the outcome were execution/luck rather than decision quality?

### Anti-hindsight rule

Never turn post-outcome information into evidence the system supposedly had before the decision. Every fact must be classified:

- available ex ante;
- reasonably retrievable ex ante;
- genuinely unavailable ex ante;
- known only after outcome.

### Internal translation

CI converts the interview into a benchmark packet containing:

- case ID/domain;
- objective;
- options;
- supplied evidence;
- retrievable evidence, if applicable;
- hidden material constraints;
- plausible wrong path;
- predetermined critical-fact key;
- reversal condition;
- strongest objection;
- uncertainty that a correct answer must preserve;
- known outcome, if historical;
- confounders;
- prohibited hindsight information.

### SME validation

Do not ask the SME to review the whole CI framework. Return a short validation sheet containing only:

1. reconstructed decision objective;
2. critical facts;
3. hidden traps;
4. predetermined answer/reversal key where objective truth permits one;
5. what remains legitimately judgment-dependent.

SME confirms or corrects this before the case is frozen.

A case is not "external" merely because an external person inspired it. The external practitioner must validate the factual packet and hidden traps before preregistration.

---

## 3. External Case Independence Levels

Record provenance for every case.

- **E0 — CI synthetic:** entirely authored by CI. Regression only.
- **E1 — CI-derived:** inspired by a real external anecdote but not externally validated.
- **E2 — SME-validated:** reconstructed by CI and validated by the originating/domain SME.
- **E3 — Independent-authored:** evidence packet/key materially authored outside CI.
- **E4 — Historical-real:** reconstructed from a real decision with contemporaneous evidence and known later outcome.

External superiority claims should rely primarily on E2–E4 cases. E0/E1 remain valuable for engineering but cannot carry independent-proof claims.

---

## 4. Judge Interface — Minimum Friction, Maximum Integrity

Judges should not read internal council transcripts unless the benchmark question specifically concerns deliberation trace quality.

Default interface shows:

### Panel A — Case context

Only the information necessary to judge the output, including the locked objective and relevant evidence/key.

### Panel B — Blind system output

Rendered in a common wrapper as **System A/B/C**. Remove provider/model/product names, timestamps, UI branding and avoidable formatting fingerprints.

Do **not** rewrite substantive content merely to make systems look alike. Normalisation must not change meaning.

### Panel C — Hard-key checklist

Binary or objective fields first, for example:

- material constraint identified? Y/N
- critical fact correct? Y/N
- required recalculation performed? Y/N
- unsupported material claim present? Y/N
- uncertainty preserved? Y/N
- human authority boundary preserved where applicable? Y/N

### Panel D — Practitioner judgment

Use short anchored scales only for dimensions that genuinely require expert judgment, such as:

- decision usability;
- practitioner realism;
- quality of trade-off analysis;
- second-order effect recognition;
- proportionality of uncertainty.

### Panel E — Red flag

> What is the most dangerous blind spot, unsupported assumption or omission in this output that a competent human decision-owner would need to catch?

### Panel F — Confidence

Judge records confidence in their assessment and whether the case falls within their actual expertise.

---

## 5. Judge Integrity Controls

- 2–3 external practitioners per domain where feasible.
- Conflicts and prior relationship to CI disclosed.
- Output order randomised per judge.
- Hard metrics scored before subjective impressions.
- Judge identity hidden from systems and other judges during scoring.
- No discussion among judges before independent scoring is submitted.
- Disagreement retained as data; do not force consensus.
- Adjudication only for predetermined hard-key disputes or protocol errors.
- LLM judge may be used as a secondary diagnostic, never the sole proof source.
- Capture judging time and abandonment rate: a protocol too burdensome to sustain is operationally weak.

---

## 6. Agentic System Failure Taxonomy

Every material miss should be classified by **failure mechanism**, not anecdote.

Initial top-level taxonomy:

### F1 — Evidence Acquisition Failure
Examples: premature surrender; failure to retrieve; stale/wrong-version source; failure to inspect supplied evidence.

### F2 — Material Detail Failure
Examples: missing exact variant, clause, portion, constraint or contextual detail capable of changing the decision.

### F3 — State Update / Recalculation Failure
Examples: late information is acknowledged but complete option is not rebuilt; stale recommendation survives changed facts.

### F4 — Objective / Constraint Failure
Examples: wrong objective, hidden goal substitution, calendar/runway error, failure to protect a locked human goal.

### F5 — Reasoning / Causal Failure
Examples: mechanism treated as outcome; arithmetic error; correlation/causation error; second-order effects ignored.

### F6 — Consensus / Social Reasoning Failure
Examples: majority pressure; persuasive wrong agent; user-preference agreement replacing evidence; correlated-agent error.

### F7 — Behaviour / Execution Reality Failure
Examples: sanitised assumptions instead of observed behaviour; recommendation impossible in real operating conditions.

### F8 — Authority / Governance Failure
Examples: AI silently takes consequential authority; decision-owner absent; override not meaningful; evidence trail inadequate.

### F9 — Calibration / Uncertainty Failure
Examples: false certainty; material ambiguity hidden; confidence inconsistent with evidence quality.

### F10 — Communication / Decision-Use Failure
Examples: correct analysis buried in generic prose; consequences not translated; action/stop gate unclear.

### F11 — Specification / Runtime Failure
Examples: rule exists in documentation but is not executed; required gate fails to fire.

### F12 — Learning-System Failure
Examples: known failure recurs; post-hoc excuse replaces pre-action rule; incident not converted into regression test/control.

This taxonomy is provisional. New external failures may create, split or merge nodes. Do not force novel failures into existing categories merely for neatness.

---

## 7. Failure-to-Control Matrix

For every material failure, record:

| Field | Requirement |
|---|---|
| Failure ID | unique identifier |
| Case/run | source case and run |
| Taxonomy node | F1–F12 or new proposed node |
| Observable failure | what actually happened |
| Decision consequence | why it mattered |
| Knowable ex ante? | yes/no/partial |
| Root mechanism | not merely symptom |
| Existing control | rule/gate/test that should have prevented it |
| Control status | absent / inadequate / not executed |
| New control | smallest generalisable intervention |
| Regression case | test that would reproduce the failure |
| Recurrence result | whether subsequent runs repeat it |
| External provenance | Andrew/client/SME/judge/public incident/etc. |

A correction is not considered institutional learning until it has a control and a recurrence test.

---

## 8. Compounding Evidence Loop

The operating loop is:

**Real decision/war story → ex-ante evidence reconstruction → independent validation → blind system run → practitioner judging → failure taxonomy → control → regression test → rerun → recurrence measurement → longitudinal outcome evidence.**

The valuable dataset is therefore not simply "cases." It is linked data connecting:

- decision context;
- evidence available at decision time;
- traps/failure modes;
- system behaviour;
- practitioner judgment;
- human intervention;
- control introduced;
- recurrence/non-recurrence;
- eventual outcome and confounders.

That dataset can become harder to reproduce as it accumulates, but it is **not automatically a moat**. Defensibility depends on access rights, data quality, diversity, continued inflow, privacy/legal permissions, integration into product controls, and demonstrated predictive/operational value.

---

## 9. Privacy, Confidentiality and Rights Gate

Real executive war stories may contain confidential, privileged, personal, health, employment, legal or commercially sensitive information.

Before ingestion:

- establish permission and intended use;
- minimise unnecessary identifying information;
- separate confidential source material from benchmark-safe reconstruction;
- do not publish client cases merely because they were useful internally;
- preserve legal privilege/confidentiality where applicable through qualified review;
- record whether the case may be used internally, externally in anonymised form, or publicly;
- never expose protected source evidence to a competing system if the benchmark environment is not authorised for it.

Independent evidence is valuable only if collected lawfully and ethically.

---

## 10. Minimum Viable External Proof Sprint

Before building a heavy portal, prove the workflow manually.

**Sprint 1:**

1. Recruit 5 external case contributors across at least 3 domains.
2. Conduct structured war-story interviews.
3. Produce at least 5 E2+ cases.
4. Recruit 2–3 qualified judges for each represented domain.
5. Run CI, same-model baseline and at least one native competitor where access permits.
6. Blind outputs using a simple controlled form/workflow.
7. Capture hard scores, practitioner scores, red flags, time and cost.
8. Populate the failure taxonomy/control matrix.
9. Publish results according to the preregistration commitment, including losses.
10. Only then decide which portal features deserve engineering.

### Build-vs-learn gate

Do **not** spend the next sprint building a polished SME portal before validating that SMEs will provide usable war stories and judges will complete the scoring protocol.

Manual workflow first; automate demonstrated bottlenecks second.

---

## 11. Success Criteria for the Intake Engine

The intake/evaluation system succeeds if it produces:

- genuinely external cases rather than CI-authored variants;
- low enough SME effort to sustain contribution;
- credible blinded judging;
- reproducible hard scoring;
- novel failure modes not generated by Andrew/CI;
- measurable conversion of failures into controls;
- declining recurrence of previously knowable failures;
- acceptable evaluation cost and latency;
- evidence that transfers across users, domains and models.

The goal is not to accumulate impressive-looking benchmark material. The goal is to make CI progressively harder to fool in ways that matter to human decisions.
