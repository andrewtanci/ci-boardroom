# CI Boardroom — Benchmark Pre-Registration

**Version:** 0.1  
**Date:** 16 Sep 2026  
**Status:** PRE-RUN TEMPLATE — must be completed and committed before the first scored external benchmark run.

---

## 1. Publication Commitment

> **Results will be published regardless of outcome, including results that show CI Boardroom underperforming a comparator.**

This commitment applies to all preregistered systems, cases and metrics unless a case is excluded under a rule written here before the runs begin.

A disappointing result is evidence. It must not disappear because it is commercially inconvenient.

---

## 2. Purpose

The benchmark tests two separate propositions:

### Claim A — Decision quality
Whether CI Boardroom improves detection of decision-changing facts, retrieval, recalculation, challenge, uncertainty handling and decision usability.

### Claim B — Human-authority assurance
Whether CI workflows create auditable evidence that a named human genuinely exercised judgment over consequential AI-supported work.

This benchmark primarily tests Claim A. Claim B requires separate workflow/pilot evidence and must not be declared proven by benchmark answers alone.

---

## 3. Frozen Benchmark Inputs

Before the first run, fill in and commit:

- benchmark version:
- commit SHA containing protocol:
- run start date:
- systems under test:
- exact model/provider/version for each system:
- inference/reasoning mode:
- tool/web access:
- memory/context settings:
- system or framework instructions where publishable:
- case IDs:
- case-origin classification (CI-authored / external practitioner / historical real):
- number of repetitions per case:
- judge roster or judge-selection procedure:
- objective scoring key:
- subjective scoring rubric:
- efficiency metrics:
- exclusions allowed before run:
- statistical/reporting method:

Do not add a new system, metric or exclusion after seeing results without declaring a new benchmark version.

---

## 4. External Case Requirement

The first externally meaningful pilot must include at least **five cases authored or materially controlled outside CI**.

CI-authored cases may run in parallel as diagnostics but must not be merged into the external superiority statistic.

External case authors lock before runs:

- prompt and evidence packet;
- critical facts;
- decision-changing facts;
- reversal conditions;
- known ambiguities;
- unacceptable unsupported claims;
- source/version/jurisdiction expectations;
- scoring key;
- exclusion conditions.

---

## 5. Judge Requirement

Primary subjective judging uses blinded external human practitioners. Target **2–3 judges per domain**.

The founder and CI designers do not serve as the sole or decisive blinded judges.

LLM judging may be used as a secondary analysis only and must be reported separately from human judging.

Judge conflicts and material prior relationships with CI or comparator products must be disclosed.

---

## 6. Model-Confound Control

Run and report separately where technically possible:

1. **Framework-isolation track:** same base model, different method/instructions.
2. **End-to-end product track:** each product in its native configuration.

Do not attribute an end-to-end product win to the framework alone when the underlying model/orchestration differs.

---

## 7. Architecture-Resilience Cases

Consensus-trap and persuasive-agent cases are classified as architecture-resilience tests.

Until CI has native or controlled multi-model diversity:

- report the structural limitation;
- do not pretend multiple role prompts equal independently trained models;
- keep framework-isolation and end-to-end product results separate;
- do not delete the cases merely because they expose a weakness.

---

## 8. Quality Metrics

Pre-register the hard metrics to be used, including where relevant:

- critical-fact recall;
- decision-changing-detail recall;
- retrieval completion;
- source/version/jurisdiction accuracy;
- calculation accuracy;
- whole-option recalculation;
- unsupported-claim rate;
- correct-reversal rate;
- false-reversal rate;
- authority preservation.

Subjective metrics may include practitioner usefulness, decision usability, execution realism, clarity of trade-offs and proportionality of uncertainty.

---

## 9. Efficiency Metrics

Record separately from quality:

- latency;
- API/model/tool cost;
- token/compute proxy;
- number of model calls;
- number of retrieval/tool calls;
- user clarification turns;
- human-review time;
- correction time after a material miss;
- retry/failure rate.

Do not hide a commercially impractical quality gain inside one blended score.

---

## 10. Run Integrity

For each run:

- preserve raw input;
- preserve raw output;
- preserve source/tool logs where available;
- record timestamp and configuration;
- randomise output labels before judges see them;
- do not manually improve a system output before judging;
- do not rerun only the system that lost unless the same rerun rule applies to all systems;
- record failed or aborted runs.

---

## 11. Exclusions

A run may be excluded only for a preregistered technical reason such as:

- system outage;
- tool failure that affected all comparable runs under the same condition;
- corrupted evidence packet;
- accidental disclosure of system identity to judges where blinding is required;
- case author confirms the answer key itself is defective.

Poor performance is not an exclusion criterion.

Post-hoc exclusions must be listed openly with the original result retained in the audit record.

---

## 12. Protocol Change Control

Once the first scored external run starts, this version is frozen.

If the protocol, cases, scoring key, judge rules or system configuration materially changes:

1. increment benchmark version;
2. describe why the change was made;
3. identify whether the change was prompted by observed results;
4. rerun affected systems/cases where a fair comparison requires it;
5. preserve the previous version and results.

---

## 13. Reporting Commitment

Publish:

- wins;
- losses;
- ties;
- judge disagreements;
- efficiency trade-offs;
- current architectural limitations;
- material protocol deviations;
- cases where the benchmark could not determine a winner.

Do not publish only a headline score without the case-origin mix, model/configuration information and quality/efficiency breakdown.

The benchmark exists to discover whether CI is better, where it is better, where it is worse, and what must change next.