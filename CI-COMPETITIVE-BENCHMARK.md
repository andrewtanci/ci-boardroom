# CI Boardroom — Competitive Benchmark & Proof Protocol

**Version:** 0.1  
**Benchmark date:** 16 Sep 2026  
**Purpose:** test whether CI Boardroom actually improves decision quality versus serious alternatives. Do not claim superiority before evidence exists.

---

## 1. Claim Discipline

The hypothesis is:

> CI Boardroom can outperform ordinary single-model advice and generic multi-agent councils on real-world decision quality by combining evidence retrieval, decision-changing detail detection, whole-option recalculation, practitioner synthesis, behavioural reality, consequence translation, human authority and outcome learning.

This is **a hypothesis to test**, not a marketing fact.

A feature list cannot prove better decisions. A benchmark must test outputs and later outcomes.

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

Relevant research available by Sep 2026 shows:

- structured multi-agent methods can improve factual accuracy and reduce hallucinations;
- debate can also drift, converge prematurely or be manipulated by persuasive agents;
- majority pressure can suppress correction;
- longer debate can reduce task focus;
- role diversity and intrinsic reasoning strength matter more than simply adding agents;
- agreement does not necessarily mean correctness.

Sources:

- Socratic Elenchus-inspired multi-agent debate, Expert Systems with Applications, 2026: https://www.sciencedirect.com/science/article/pii/S0957417426011218
- "When collaboration fails", Scientific Reports, 2026: https://www.nature.com/articles/s41598-026-42705-7
- "Stay Focused: Problem Drift in Multi-Agent Debate", EACL 2026: https://aclanthology.org/2026.findings-eacl.268/
- "Can LLM Agents Really Debate?", 2025/26 study: https://arxiv.org/abs/2511.07784
- "Beyond Consensus", 2026: https://doi.org/10.48550/arXiv.2608.30373

**CI design consequence:** the product must optimise for better decisions, not for more debate. Specialist seats must add independent evidence or analysis. Red Team must attack consensus. Evidence must dominate persuasive confidence.

---

## 4. Provisional Structural Comparison

This table reflects **publicly documented capabilities**, not measured decision quality. "Not publicly evidenced" does not mean the competitor lacks the capability.

| Capability | CI Boardroom current specification | The AI Council | Resync War Room | Council AI / generic multi-model councils |
|---|---|---|---|---|
| Dynamic expert roles | Documented | Documented | Documented | Documented |
| Visible dissent / challenge | Documented | Documented | Documented | Documented |
| Multi-model diversity | Optional/external cross-examination; not yet native product proof | Not clearly required by public page | Explicitly documented | Explicitly documented |
| Source/evidence discipline | Explicit hierarchy + retrieval rules | Audit trail; public page less specific on source hierarchy | Document grounding + citations | Deep research / peer review |
| Human final authority | Core principle and authority flags | User sees Arbiter verdict; human role implied | Explicit named-human ratification | Generally user decides |
| Decision-changing detail gate | Explicit | Not publicly evidenced | Not publicly evidenced | Not publicly evidenced |
| Retrieval-before-user-handoff gate | Explicit hard gate | Not publicly evidenced | Not publicly evidenced | Not publicly evidenced |
| Whole-option recalculation after late changes | Explicit hard gate | Not publicly evidenced | Not publicly evidenced | Not publicly evidenced |
| Behavioural reality / known-user pattern | Explicit | Not publicly evidenced | Decision register/history | Persistent context varies |
| Goal/runway backward calculation | Explicit | Not publicly evidenced | Scenario analysis generally | Not publicly evidenced |
| Consequence translation into human-meaningful units | Explicit | Not publicly evidenced | Not publicly evidenced | Not publicly evidenced |
| Outcome calibration | Specification supports feedback loop but product proof incomplete | Explicitly documented | Explicitly documented | Varies |
| Audit / decision record | Boardroom Card + evidence concepts; product implementation incomplete | Explicitly documented | Explicitly documented | Often documented |
| Deliverable execution | Can produce work products in host environment | Writer explicitly documented | Board-ready memo documented | Varies |
| On-prem / enterprise data isolation | Not yet proven as CI product capability | Not established from public page reviewed | Explicitly documented | Varies |
| Ex-ante failure-to-rule learning | Explicit | Outcome calibration documented; exact protocol unclear | Outcome feedback documented | Not publicly evidenced |

### What this means now

CI has several **methodological differentiators on paper**, especially around real-world detail, retrieval, complete-option recalculation, consequence translation and authority. But serious competitors are ahead or at least more publicly productised in areas such as native multi-model diversity, audit trail, decision register, persistent outcome calibration and enterprise deployment.

Therefore **CI is not yet proven superior overall**.

---

## 5. What Would Count as Proof

CI can claim a benchmark advantage only after a controlled comparison.

### Track A — Closed-book deterministic cases
All systems receive the same supplied evidence. No web access is required. Ground truth is fixed in advance.

Measures:

- critical-fact extraction;
- arithmetic/logic correctness;
- decision-changing detail detection;
- correct whole-option recalculation after a late change;
- unsupported-claim rate;
- correct uncertainty;
- final recommendation alignment with predetermined objective/constraints.

### Track B — Open-web retrieval cases
All systems receive the same query and equivalent web/source access.

Measures:

- whether the system retrieves rather than unnecessarily asking the user;
- primary-source hit rate;
- source freshness;
- source/version matching;
- number of material facts missed;
- citation correctness;
- whether retrieved facts alter the recommendation when they should.

### Track C — Longitudinal real decisions
Use actual business/personal decisions where outcomes become observable.

Measures:

- prediction/calibration accuracy;
- decision reversals caused by previously missed facts;
- ex-ante risk detection;
- implementation success;
- time to decision;
- human override rate;
- post-decision regret/error category;
- whether the framework updates from misses.

Track C is the strongest evidence but takes time.

---

## 6. Fair Benchmark Rules

1. Same user prompt and same supplied evidence.
2. Equivalent source access for retrieval tests.
3. No product receives hidden facts unavailable to another.
4. Randomise and blind output labels before human scoring.
5. Define ground-truth critical facts and reversal conditions **before** running the systems.
6. Do not let CI write the judging rubric after seeing competitor outputs.
7. Use at least two independent human raters for subjective usability/practitioner-quality scores.
8. Separate factual correctness from style/preferences.
9. Record model/version/date because performance changes.
10. Repeat cases to test consistency, not just best-run performance.
11. Publish failures as well as wins.
12. Do not count council agreement as evidence of correctness.

---

## 7. Core Scorecard

### Hard metrics

- **Critical Fact Recall:** % of predetermined material facts captured.
- **Decision-Changing Detail Recall:** % of facts capable of reversing the call that were surfaced/retrieved.
- **Retrieval Completion:** % of reasonably retrievable material facts obtained before user handoff.
- **Source Match Accuracy:** % of cited facts matched to correct product/version/jurisdiction/date.
- **Calculation Accuracy:** % of material calculations correct.
- **Whole-Option Recalculation:** pass/fail after additions/substitutions.
- **Unsupported Claim Rate:** unsupported material claims per answer.
- **Correct-Reversal Rate:** when new evidence should reverse the recommendation, how often it does.
- **False-Reversal Rate:** how often the system changes recommendation when evidence did not justify it.
- **Authority Preservation:** pass/fail on named human authority for consequential action.

### Human-rated metrics

Score only after blinding outputs:

- practitioner usefulness;
- clarity of trade-offs;
- strength of challenge;
- decision usability;
- proportionality of uncertainty;
- absence of generic filler;
- execution realism.

### Longitudinal metrics

- calibration versus actual outcomes;
- avoidable miss rate;
- percentage of misses converted into pre-action rules;
- repeat-error rate;
- outcome improvement over baseline process.

---

## 8. Pass Threshold for a Superiority Claim

Do **not** use a single weighted score as the only proof.

A credible claim should require:

1. CI materially beats the baseline on at least three core hard metrics;
2. CI does not materially worsen unsupported claims or human-authority preservation;
3. the advantage repeats across multiple domains, not only food/health or Andrew-specific cases;
4. blinded human raters prefer CI on decision usability/practitioner quality;
5. real-outcome calibration is at least competitive once enough longitudinal cases exist;
6. results reproduce across more than one frontier model/version where possible.

Until then, wording should be:

> "CI Boardroom is designed to address failure modes that many council systems do not publicly document. We are benchmarking whether those design choices produce better real-world decisions."

Not:

> "CI Boardroom is proven better than every AI council."

---

## 9. Biggest Competitive Threats to CI

### Threat 1 — Native model diversity
A true multi-model council can expose correlated blind spots that one model wearing several role prompts may not. CI needs either native multi-model orchestration or a very low-friction cross-examination layer.

### Threat 2 — Productised outcome calibration
Several competitors already advertise decision registers and calibration. CI must turn its feedback-loop philosophy into persistent product behaviour, not just written rules.

### Threat 3 — Enterprise integration and privacy
Resync publicly offers on-prem infrastructure and document grounding. CI needs a credible enterprise data architecture before claiming board-level deployment advantage.

### Threat 4 — Framework bloat
CI's growing rigor can become latency, cost and complexity. Hard gates must activate only when material. A fast routine answer should remain fast.

### Threat 5 — Andrew-overfitting
Live testing with a demanding founder is valuable, but the method must generalise. Every personal lesson must be converted into a domain-independent failure class and then tested on unrelated users/domains.

### Threat 6 — Specification/execution gap
The KFC side-dish incident showed that writing a rule does not guarantee runtime compliance. CI needs executable gates, automated test cases and release checks.

---

## 10. Strongest Current CI Thesis

The most defensible differentiation is **not "we have more experts."**

It is:

> CI Boardroom is a human-authority-preserving decision system designed to catch the small, real-world facts and behavioural realities that change the decision; retrieve evidence before burdening the human; recalculate the complete option when reality changes; translate evidence into consequences; challenge consensus; and learn from observable outcomes.

That thesis is sufficiently distinct to test.

The next job is empirical proof.