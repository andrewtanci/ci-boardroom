# CI Boardroom — External Evidence Engine

**Version:** 0.2  
**Date:** 16 Sep 2026  
**Purpose:** turn paid operational work and contemporaneous records into independent decision evidence, then use low-friction blinded judging and a failure taxonomy to harden CI.

---

## 1. Strategic Role

CI must distinguish three assets:

1. **Rules** — public and copyable.
2. **Evidence** — independently grounded proof that the rules improve decisions.
3. **Learning system** — accumulated real failure modes, controls, tests and recurrence data.

The durable asset is not a static prompt. It is the evidence-and-learning loop.

**Primary correction in v0.2:** do not make volunteer crowdsourcing the default evidence-acquisition strategy. Harvest evidence first from paid work, authorised operational records and existing professional networks where access, incentives and provenance already exist.

---

## 2. Evidence Acquisition Hierarchy

Use the highest-quality, lowest-friction evidence source available.

### Tier 1 — Paid operational work

Every paid pilot or engagement is a potential evidence-generation event. Examples include assessment marking, content generation, moderation, QA, compliance review and decision-support work.

Capture naturally occurring:

- AI errors;
- human corrections;
- disagreements between markers/reviewers;
- missed evidence;
- material late discoveries;
- appeal/moderation reversals;
- audit/non-compliance findings;
- situations where a human override changed the result.

Do not manufacture failures for the sake of the benchmark.

### Tier 2 — Contemporaneous written records

Prefer dated records created before the outcome where permission exists. Examples may include assessment appeals, moderation records, audit findings, QA records, non-compliance reports, decision papers, version histories, review comments and correspondence.

These can be stronger than retrospective memory because they preserve what was actually known and believed at the time.

### Tier 3 — Structured retrospective from known practitioners

Use when records are incomplete. Keep it short and separate ex-ante reconstruction from outcome discussion.

### Tier 4 — External volunteer contribution

Useful later for diversity and adversarial expansion, but not the default dependency for the first proof cycle.

---

## 3. Five-Field Capture — Voice First

The founder/operator capture workflow must fit real behaviour. Default input is a short voice note, not a form.

Capture only:

1. **Decision + date**
2. **What was chosen / produced**
3. **What went wrong or nearly went wrong**
4. **The fact that would have changed/flipped the decision**
5. **Was that fact knowable or retrievable at the time?**

CI performs downstream reconstruction, evidence classification, taxonomy mapping, control design and regression-case generation.

Do not require the contributor to learn CI terminology.

---

## 4. Hindsight Guard — Two-Phase Reconstruction

Outcome knowledge contaminates memory. Therefore reconstruct the ex-ante state before discussing the outcome whenever possible.

### Phase A — Before outcome disclosure

Ask:

- What was the objective?
- What options were available?
- What did you know then?
- What documents/data existed then?
- What did the team believe then?
- What uncertainty was recognised then?
- What would a competent practitioner normally have checked then?

Freeze this reconstruction.

### Phase B — Outcome and failure

Only after Phase A:

- What happened?
- What went wrong or nearly went wrong?
- What fact changed the understanding?
- Was it available/retrievable before the decision?
- What part of the outcome was execution or luck rather than decision quality?

Where good contemporaneous records exist, prefer them over reconstructed memory.

Every fact must be classified:

- available ex ante;
- reasonably retrievable ex ante;
- genuinely unavailable ex ante;
- known only after outcome.

Never allow post-outcome facts into the system's original evidence packet.

---

## 5. Case Reconstruction and Provenance

CI converts source material into a benchmark packet containing:

- case ID/domain;
- decision date;
- objective;
- options;
- supplied evidence;
- retrievable evidence, if applicable;
- hidden material constraints;
- plausible wrong path;
- predetermined critical-fact key;
- reversal condition;
- strongest objection;
- uncertainty a correct answer must preserve;
- known outcome, if historical;
- confounders;
- prohibited hindsight information;
- source permissions/use restrictions.

### Independence levels

- **E0 — CI synthetic:** entirely authored by CI. Regression only.
- **E1 — CI-derived:** inspired by external material but not externally validated.
- **E2 — SME-validated:** reconstructed by CI and validated by originating/domain SME.
- **E3 — Independent/contemporaneous evidence:** material evidence/key comes from non-CI operational records or external practitioner work.
- **E4 — Historical-real:** real decision with contemporaneous ex-ante evidence and known later outcome.

**Important:** paid work does not automatically make a case E3/E4. Provenance depends on the underlying evidence and validation, not whether CI was paid. A pilot-generated case may be E2, E3 or E4 depending on what records actually exist.

External proof should rely primarily on E2–E4.

---

## 6. External Judge Protocol — Pairwise First

Do not expose external judges to the internal 12-point rubric. Keep that for internal diagnostics and hard-key analysis.

Default external evaluation is deliberately short.

### Judge sees

- case context needed to judge;
- two outputs in a common blind wrapper: **Output A** and **Output B**;
- randomised left/right ordering.

### Required judge questions

**Q1 — Forced choice**

> Which output would better support the named human decision-owner: A or B?

If genuinely indistinguishable, a predeclared tie option may be allowed; do not add it ad hoc after seeing results.

**Q2 — Decisive reason**

> What one thing most influenced your choice?

**Q3 — Critical-fact binary**

> Did this output catch the material fact/constraint that could have changed the decision? Y/N

Apply Q3 to each output where a predetermined critical fact exists.

**Q4 — Dangerous blind spot, optional but strongly useful**

> What is the most dangerous blind spot or unsupported assumption the human would still need to catch?

Target judge burden: approximately 2–5 minutes per pair, measured rather than assumed.

### Why pairwise

Pairwise comparison reduces calibration burden and judge fatigue. It does not eliminate bias. Randomisation, multiple judges, domain qualification and appropriate statistical treatment remain necessary.

---

## 7. Internal Scoring Remains Rich

CI may still apply the full internal hard-metric rubric to each run for diagnosis:

- critical facts;
- decision-changing detail;
- retrieval;
- source/version/jurisdiction;
- arithmetic/logic;
- whole-option recalculation;
- strongest objection;
- unsupported claims;
- calibration;
- authority preservation;
- executable recommendation;
- pre-action decision improvement.

External pairwise preference is **not** a replacement for objective hard-key scoring. The two answer different questions.

---

## 8. Judge Incentives and Credibility

Do not assume qualified practitioners will donate hours.

Preferred mechanisms:

1. **Paid judging** — transparent compensation for defined evaluation work.
2. **Value exchange** — e.g. a bounded CI decision review/advisory session in exchange for defined contribution, with conflicts disclosed.
3. **Existing paid/advisory duties** — only where judging responsibilities are explicitly agreed.

Record compensation/value exchange as part of the methodology. Payment does not invalidate judging, but undisclosed incentives undermine credibility.

Judge controls:

- 2–3 external practitioners per domain where feasible;
- relevant domain experience documented;
- conflicts/prior CI relationship disclosed;
- output order randomised;
- judges score independently before discussion;
- disagreements retained as data;
- LLM judge secondary only;
- judging time and completion/abandonment measured.

---

## 9. Agentic System Failure Taxonomy

Every material miss is classified by **failure mechanism**, not anecdote.

### F1 — Evidence Acquisition Failure
Premature surrender; failure to retrieve; stale/wrong-version source; failure to inspect supplied evidence.

### F2 — Material Detail Failure
Missing exact variant, clause, portion, constraint or contextual detail capable of changing the decision.

### F3 — State Update / Recalculation Failure
Late information acknowledged but complete option not rebuilt; stale recommendation survives changed facts.

### F4 — Objective / Constraint Failure
Wrong objective, hidden goal substitution, runway error, failure to protect locked human goal.

### F5 — Reasoning / Causal Failure
Mechanism treated as outcome; arithmetic error; correlation/causation error; second-order effects ignored.

### F6 — Consensus / Social Reasoning Failure
Majority pressure; persuasive wrong agent; user-preference agreement replacing evidence; correlated-agent error.

### F7 — Behaviour / Execution Reality Failure
Sanitised assumptions instead of observed behaviour; recommendation impossible in actual operating conditions.

### F8 — Authority / Governance Failure
AI silently takes consequential authority; decision-owner absent; override not meaningful; evidence trail inadequate.

### F9 — Calibration / Uncertainty Failure
False certainty; material ambiguity hidden; confidence inconsistent with evidence quality.

### F10 — Communication / Decision-Use Failure
Correct analysis buried in generic prose; consequences not translated; action/stop gate unclear.

### F11 — Specification / Runtime Failure
Rule exists in documentation but is not executed; required gate fails to fire.

### F12 — Learning-System Failure
Known failure recurs; post-hoc excuse replaces pre-action rule; incident not converted into regression test/control.

Taxonomy remains provisional. External failures may create, split or merge nodes.

---

## 10. Failure-to-Control Matrix

For every material failure record:

| Field | Requirement |
|---|---|
| Failure ID | unique identifier |
| Case/run | source case and run |
| Taxonomy node | F1–F12 or proposed new node |
| Observable failure | what actually happened |
| Decision consequence | why it mattered |
| Knowable ex ante? | yes/no/partial |
| Root mechanism | not merely symptom |
| Existing control | rule/gate/test that should have prevented it |
| Control status | absent / inadequate / not executed |
| New control | smallest generalisable intervention |
| Regression case | test that reproduces the failure |
| Recurrence result | whether later runs repeat it |
| Provenance | founder/client/SME/judge/record/public incident/etc. |

A correction is not institutional learning until it has a control and recurrence test.

---

## 11. Paid-Pilot Evidence Loop

Default near-term operating loop:

**Paid work → naturally occurring discrepancy/failure → contemporaneous records + five-field voice capture → ex-ante reconstruction → permission/validation → blind comparison → practitioner pairwise judgment → failure taxonomy → control → regression test → rerun → recurrence measurement.**

This makes evidence collection a byproduct of useful client work rather than a separate volunteer-recruitment programme.

Potential early sources in training/assessment environments include, where authorised:

- assessment-marking disagreements;
- moderation decisions;
- assessment appeals;
- QA findings;
- audit/clarification records;
- content-generation errors;
- evidence/mapping omissions;
- assessor/trainer overrides;
- compliance corrections.

Do not assume any specific SSG/client record can be reused externally. Permission, confidentiality and purpose limitation govern use.

---

## 12. Privacy, Confidentiality and Rights Gate

Paid access is **not** permission to train, benchmark, publish or expose client material to third-party models.

Before reuse:

- establish contractual/explicit permission and intended use;
- minimise identifying and unnecessary information;
- separate confidential source records from benchmark-safe reconstruction;
- preserve legal privilege/confidentiality where applicable;
- record internal-only / anonymised-external / public-use status;
- consider personal-data obligations and client policies;
- never send protected evidence to a competitor/model environment not authorised for that data.

For pilots, evidence-use permission should be designed into engagement documentation rather than requested only after an interesting failure occurs.

---

## 13. Revised First Proof Sequence

Do not begin by recruiting five strangers.

### Phase 1 — Existing paid pilots

Use the first two suitable pilot engagements to test the capture pipeline. Harvest only naturally occurring, authorised evidence.

### Phase 2 — Existing WSQ/professional network records

Seek permission for historical records that preserve ex-ante evidence: moderation, appeals, QA, audit/clarification and similar decision records. Target at least five usable cases before broad contributor recruitment.

### Phase 3 — External diversity only where needed

After analysing domain/failure coverage, recruit external contributors specifically to fill blind spots rather than as a generic crowdsourcing campaign.

### Phase 4 — Automate proven friction

Only after repeated manual use should CI build portals or elaborate tooling. The founder's default capture remains voice-first unless evidence shows another interface works better.

---

## 14. Success Criteria

The evidence engine succeeds if it produces:

- real non-founder failures from paid/authorised work;
- contemporaneous ex-ante evidence where possible;
- low-friction operator capture;
- credible pairwise practitioner judging;
- reproducible internal hard scoring;
- novel failure modes not generated by Andrew/CI;
- measurable conversion of failures into controls;
- declining recurrence of previously knowable failures;
- acceptable evaluation cost and latency;
- evidence that transfers across users, domains and models.

The goal is not to accumulate impressive benchmark material. The goal is to make CI progressively harder to fool in ways that matter to human decisions.
