# CI Boardroom — Competitive Benchmark & Proof Protocol

**Version:** 0.2  
**Benchmark date:** 16 Sep 2026  
**Purpose:** test whether CI Boardroom actually improves decision quality versus serious alternatives. Do not claim superiority before evidence exists.

---

## 1. Claim Discipline

Two claims must be kept separate.

### Claim A — Decision-quality claim

> CI Boardroom can catch more decision-changing facts, retrieve more material evidence before user handoff, recalculate the whole option more reliably, challenge weak assumptions more effectively, and produce more usable decisions than ordinary single-model advice or generic council workflows.

This claim is benchmarkable now.

### Claim B — Human-authority assurance claim

> CI can produce auditable evidence that a named human genuinely exercised authority over consequential AI-supported work rather than merely rubber-stamping AI output.

This is not established by case-answer scoring alone. It requires real workflow/pilot evidence, decision records, human intervention evidence and the broader CI/AI TAP assurance route.

**Do not let Claim A consume the proof effort while Claim B is the more durable strategic position.**

Both claims remain hypotheses until tested. A feature list or written framework cannot prove either claim.

---

## 2. Current Market Reality

Publicly documented competitors already cover important parts of the problem.

### The AI Council — https://www.theaicouncil.io/
Public documentation shows multiple AI advisers, visible dissent, voting, an Arbiter, audit trail, custom agents/skills, a Writer that produces deliverables, and outcome calibration that records whether decisions worked.

### Resync War Room — https://resync.nz/resync-labs/war-room/
Public documentation shows independent drafts, anonymous critique, revision, voting, weighted voices/vetoes, document grounding with citations, named-human ratification, a decision register with outcomes, multi-model diversity, and deployment on the customer's own infrastructure.

### Council AI — https://www.topaicouncil.com/
Public documentation shows independent outputs from multiple models, anonymised peer review/scoring, a Chairman synthesis, confidence/disagreement reporting, deep-research mode and code-review mode.

### AI Council Cloud — https://aicouncil.cloud/
Public documentation shows multiple deliberation modes, persistent workspaces, evidence mode requiring citations, decision audit trails, chains/workflows, and bring-your-own-provider keys.

### Open-source evidence-governed councils
Examples such as https://github.com/MaciejZet/ai-council publicly document blind rounds, red team, evidence judge, chairman, decision memory, typed verdicts and outcome calibration.

**Implication:** "many experts debating" is not a moat. Voting, dissent, evidence mode, memory and calibration already exist elsewhere.

---

## 3. External Research Challenge to the Council Thesis

Multi-agent deliberation is promising but is not automatically more accurate.

Relevant research available by Sep 2026 shows that structured multi-agent methods can improve factual accuracy, but debate can also drift, converge prematurely, reward persuasive agents, or suppress correction under majority pressure. Agreement does not establish correctness.

Sources:

- Socratic Elenchus-inspired multi-agent debate, Expert Systems with Applications, 2026: https://www.sciencedirect.com/science/article/pii/S0957417426011218
- "When collaboration fails", Scientific Reports, 2026: https://www.nature.com/articles/s41598-026-42705-7
- "Stay Focused: Problem Drift in Multi-Agent Debate", EACL 2026: https://aclanthology.org/2026.findings-eacl.268/
- "Can LLM Agents Really Debate?", 2025/26: https://arxiv.org/abs/2511.07784
- "Beyond Consensus", 2026: https://doi.org/10.48550/arXiv.2608.30373

**CI design consequence:** optimise for better decisions, not more debate. Evidence must outrank confidence, role agreement and rhetorical force.

---

## 4. Specification Is Not Behaviour

A documented rule is not evidence that the runtime follows the rule.

The KFC side-dish failure is the canonical example: CI had already documented retrieval-before-handoff, yet the next answer still asked the human for retrievable information.

Therefore every claimed differentiator must be labelled separately as:

1. **Documented** — written in the specification.
2. **Observed** — demonstrated in a controlled case.
3. **Repeated** — reproduced across repeated runs/domains/models.
4. **Externally validated** — passed non-CI-authored cases under blind judging.
5. **Outcome validated** — supported by real-world decision/workflow evidence.

Never collapse these stages into one claim.

---

## 5. Case-Origin Firewall — No Home-Field Advantage

The benchmark must distinguish who wrote the exam.

### Pool I — CI-authored diagnostic/regression cases

These are useful for debugging, release checks and testing whether CI executes its own rules. They **cannot by themselves support a superiority claim** because the system helped define the failure modes and pass conditions.

The current `CI-BENCHMARK-CASES.md` suite belongs to this pool unless a case is explicitly replaced or independently authored.

### Pool E — External practitioner-authored cases

Cases must be authored or materially controlled by people who did not design the CI rule being tested. For the first external benchmark, obtain at least **five non-CI-authored cases** and expand thereafter.

For domain-sensitive cases, case authors should be credible practitioners in the relevant domain. The case author defines before any run:

- source packet;
- critical facts;
- decision-changing fact(s);
- reversal condition(s);
- known ambiguity;
- unacceptable unsupported claims;
- expected escalation/professional-review boundary where relevant.

### Pool H — Historical real decisions

Use real historical cases where the evidence packet and eventual outcome are already known. This reduces benchmark gaming but does not make outcome causation simple. Cases must be sanitised for confidentiality.

**External superiority claims require Pool E and/or Pool H. Pool I is never sufficient.**

---

## 6. Judge Design — No Self-Marking

A benchmark without a credible judge is not credible proof.

### Primary judges

Use **2–3 external human judges per domain**, blinded to system identity. Prefer practitioners with enough domain competence to recognise decision-changing omissions and unrealistic recommendations.

Judges must disclose material conflicts, commercial relationships or prior involvement with CI or a competitor.

The founder, CI authors and prompt designers may inspect results and challenge scoring, but **must not be the sole or decisive blinded judges**.

### Objective key before subjective scoring

Hard metrics are scored against the locked case key before any subjective preference score. When possible, automate deterministic checks for arithmetic, source/version match and critical-fact recall.

### LLM judge

An LLM judge may be used only as a **secondary analytic instrument**, not the sole authority. Its scores must be compared against human ratings because LLM judges can be affected by verbosity, style, ordering, self-preference and model-family bias.

If an LLM judge materially disagrees with human judges, report the disagreement rather than averaging it away.

### Inter-rater reliability

Record agreement between human judges. Material disagreement triggers adjudication by a separate domain practitioner or a pre-defined adjudication rule. Do not silently choose the rating more favourable to CI.

---

## 7. Model-Confound Control

Do not confuse framework quality with base-model capability.

Run two separate comparison tracks and report them separately.

### Track F — Framework-isolation track

Where technically possible, run:

- the same base model with a neutral/default prompt;
- the same base model with CI Boardroom instructions;
- the same base model with a comparator method/prompt where that method can be reproduced fairly.

This asks: **what does the method add when the underlying model is held constant?**

### Track P — End-to-end product track

Run each competitor in its normal native configuration, including its chosen models, orchestration, tools, memory and interface.

This asks: **which product produces the better real-world result as actually delivered?**

Track F supports causal attribution to method. Track P supports commercial comparison. Never use Track P alone to claim that the framework rather than the model caused the difference.

Record model, version, inference mode, date, tool access and material settings for every run.

---

## 8. Multi-Model / Consensus Architecture Control

A single model wearing several personas has correlated failure modes. Do not present role diversity as equivalent to true model diversity.

Consensus-trap and persuasive-agent tests remain important, but classify them as **architecture-resilience tests**.

Until CI has native or controlled multi-model orchestration:

- report these cases as a current architecture limitation;
- do not use failure on them to infer that the underlying CI decision rules are invalid;
- equally, do not exclude them from an overall end-to-end product comparison merely because CI is structurally disadvantaged.

For method-isolation analysis, run a separate same-model version that tests whether evidence-over-consensus rules improve behaviour within one base model. For product comparison, let native multi-model products use their real architecture and report CI's gap honestly.

---

## 9. Benchmark Tracks

### Track A — Closed-book deterministic cases

All systems receive the same supplied evidence. Ground truth is fixed in advance.

Measures include critical-fact extraction, arithmetic/logic correctness, decision-changing detail detection, whole-option recalculation, unsupported-claim rate, uncertainty and recommendation alignment with locked objectives/constraints.

### Track B — Open-web retrieval cases

All systems receive the same query and materially equivalent source access.

Measures include retrieval-before-handoff, primary-source hit rate, freshness, product/version/jurisdiction matching, citation correctness and whether retrieved facts appropriately change the recommendation.

### Track C — Longitudinal real decisions

Use actual decisions where outcomes later become observable.

This track has the highest ecological relevance but is **slow and noisy**, not near-term proof. Outcomes may be confounded by execution quality, luck, market movement, changing conditions and human overrides. Record those confounders explicitly.

Track C should support long-term calibration and assurance learning, not be used to delay near-term controlled benchmarking.

---

## 10. Fair Benchmark Rules

1. Same user prompt and supplied evidence within each controlled track.
2. Equivalent source/tool access where the track requires retrieval.
3. No system receives hidden case facts unavailable to another.
4. Randomise and blind output labels before human scoring.
5. Lock critical facts, reversal conditions and objective scoring key before runs.
6. Do not rewrite the rubric after seeing competitor outputs.
7. Use external domain judges for the external proof set.
8. Separate factual correctness from style/preferences.
9. Record model/version/date/configuration.
10. Repeat cases; do not cherry-pick the best run.
11. Publish failures as well as wins.
12. Do not count council agreement as evidence of correctness.
13. Do not mix CI-authored diagnostic cases with external proof cases in one superiority statistic.
14. Protocol changes after first execution create a new benchmark version; rerun affected comparisons.
15. Preserve raw outputs, source logs, judge scores and adjudications so the result can be audited.

---

## 11. Pre-Registration Commitment

Before the first scored external run, commit the protocol, case IDs, scoring rules, judge process, exclusions and systems under test to the repository.

The pre-registration must include this exact commitment:

> **Results will be published regardless of outcome, including results that show CI Boardroom underperforming a comparator.**

Do not quietly remove failed cases after runs. Any exclusion must be based on a pre-registered rule or transparently documented as a post-hoc deviation.

---

## 12. Quality Scoreboard

### Hard metrics

- **Critical Fact Recall** — predetermined material facts captured.
- **Decision-Changing Detail Recall** — facts capable of reversing the call surfaced/retrieved.
- **Retrieval Completion** — retrievable material facts obtained before unnecessary user handoff.
- **Source Match Accuracy** — fact matched to correct product/version/jurisdiction/date.
- **Calculation Accuracy** — material calculations correct.
- **Whole-Option Recalculation** — complete option updated after additions/substitutions.
- **Unsupported Claim Rate** — unsupported material claims per answer.
- **Correct-Reversal Rate** — recommendation changes when locked reversal evidence requires it.
- **False-Reversal Rate** — recommendation changes without sufficient evidence/objective change.
- **Authority Preservation** — human decision ownership preserved when consequential.

### Human-rated metrics

After blinding:

- practitioner usefulness;
- clarity of trade-offs;
- strength of challenge;
- decision usability;
- proportionality of uncertainty;
- absence of generic filler;
- execution realism.

---

## 13. Efficiency Scoreboard — Commercial Reality

Quality and efficiency must be reported separately. A system that is marginally better but 10× slower or 20× more expensive may lose commercially.

Record where measurable:

- wall-clock latency to usable answer;
- model/API/tool cost;
- input/output tokens or comparable compute proxy;
- number of model calls;
- number of retrieval/tool calls;
- number of user clarification turns;
- time to correct an identified error;
- total human-review time required;
- failure/retry rate.

Do not hide efficiency inside one weighted quality score. Report quality and efficiency side by side and identify Pareto-dominant results where one system is both better and cheaper/faster.

---

## 14. Longitudinal / Outcome Scoreboard

For real decisions, record:

- prediction/calibration versus outcome;
- avoidable miss rate;
- ex-ante risk detection;
- human override rate;
- implementation/execution confounders;
- repeat-error rate;
- percentage of misses converted into pre-action rules;
- whether those new rules prevent recurrence.

This track is strategically important but cannot be the sole proof for the first 12 months because outcome samples accumulate slowly and causality is noisy.

---

## 15. Pass Threshold for a Decision-Quality Advantage Claim

Do not use a single weighted score as the only proof.

A credible external Claim A should require:

1. a locked preregistered protocol;
2. external/non-CI-authored case coverage;
3. blinded external human judging;
4. CI materially beating baseline/comparators on multiple core hard metrics;
5. no material worsening in unsupported claims or human-authority preservation;
6. the advantage repeating across more than one domain;
7. results surviving same-base-model framework isolation where technically possible;
8. efficiency not being commercially disproportionate to the quality gain;
9. repeated runs rather than best-run selection;
10. publication of losses as well as wins.

Until then, use:

> "CI Boardroom is designed to address decision failure modes that many council systems do not publicly document. We are testing whether those design choices produce measurably better real-world decision support."

Do not use:

> "CI Boardroom is proven better than every AI council."

---

## 16. Claim B — Human Authority / Assurance Proof Route

Claim B is a different business proof problem.

Case benchmarks can test whether an answer names the human owner or flags authority drift, but that does not prove the human genuinely exercised authority in a live workflow.

The stronger proof route is through pilots that retain evidence such as:

- who received the AI output;
- what evidence was available to the human;
- what the human changed, challenged, approved, rejected or escalated;
- whether the human could realistically detect errors;
- whether decision criteria were known in advance;
- whether the AI's role stayed within the delegated boundary;
- the final accountable human action;
- the evidence trail supporting that action.

This is the route toward CI's assurance / AI TAP positioning. It is more durable than a public prompt rule because it depends on workflow, evidence, governance practice and accumulated proof rather than copyable wording.

---

## 17. Biggest Competitive Threats to CI

### Threat 1 — Native model diversity
True multi-model councils can expose correlated blind spots that one model wearing several roles may not. CI needs native multi-model orchestration or a low-friction equivalent.

### Threat 2 — Productised outcome calibration
Competitors already advertise decision registers and calibration. CI must turn its feedback-loop philosophy into persistent product behaviour.

### Threat 3 — Enterprise integration and privacy
Competitors already document enterprise/on-prem capabilities. CI needs a credible data architecture before claiming deployment advantage.

### Threat 4 — Framework bloat
Rigor can become latency, cost and complexity. Hard gates must activate only when material.

### Threat 5 — Andrew-overfitting
One demanding founder is a strong failure detector but not a representative population. External practitioner/client failures must feed the rule-learning pipeline.

### Threat 6 — Specification/execution gap
Written rules can fail at runtime. Release gates must test behaviour rather than presence of text.

### Threat 7 — Copyability of public rules
Decision rules in a public repository can be copied. Do not treat wording as a durable moat. Durable advantage must come from positioning, evidence, workflow integration, assurance architecture, accumulated outcome/failure data and speed of learning.

---

## 18. Strongest Current Strategic Thesis

The most defensible near-term proposition is not "we have more experts."

For Claim A:

> CI Boardroom is designed to catch the small, real-world facts and behavioural realities that change a decision, retrieve evidence before burdening the human, recalculate the complete option when reality changes, challenge unsupported consensus and translate evidence into actionable consequences.

For Claim B:

> CI's longer-term moat is auditable human authority: evidence that consequential AI-supported work remained genuinely under accountable human judgment rather than becoming automated authority by default.

The benchmark proves or disproves Claim A. Real assurance pilots and AI TAP evidence must prove or disprove Claim B.
