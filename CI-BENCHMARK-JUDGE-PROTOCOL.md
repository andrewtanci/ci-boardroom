# CI Boardroom — External Judge Protocol

**Version:** 0.1  
**Date:** 16 Sep 2026

## Purpose

Prevent CI from marking its own exam.

The benchmark uses objective keys first and blinded external human judgment second. LLM judging is supplementary only.

---

## 1. Judge Composition

For each domain-sensitive case, use **2–3 external practitioners** with enough experience to recognise material omissions, unrealistic execution and false certainty.

Examples:

- acquisition/finance: corporate finance, investment, M&A or experienced CFO practitioner;
- contracts: qualified lawyer or senior commercial/contracts practitioner, with legal-finality boundaries respected;
- technology: practitioner experienced in the relevant workload/stack;
- marketing/growth: practitioner accountable for downstream economics, not only top-funnel metrics;
- governance/human authority: AI governance, risk, audit, assurance or accountable operational leadership.

One person may judge several cases only where their expertise genuinely covers them.

---

## 2. Independence and Conflict Declaration

Before judging, each judge declares:

- financial interest in CI;
- employment/consulting relationship with CI;
- involvement in writing CI's benchmark cases or rules;
- material relationship with a comparator;
- prior access to unblinded outputs;
- other conflict that could affect scoring.

A conflicted judge may provide commentary but should not be the decisive blinded rater unless the conflict is unavoidable and disclosed.

The founder and CI authors may challenge a score after judging, but they do not substitute their own preference for the blind score.

---

## 3. Blinding

Before human judging:

1. strip product/model names from outputs;
2. remove branding, attribution footers and obvious framework-specific labels where removal does not alter substantive content;
3. assign random output IDs independently per case;
4. randomise display order;
5. do not tell judges which systems are expected to perform best.

If an output's wording makes its identity obvious, record blinding leakage rather than pretending the judge remained blind.

---

## 4. Scoring Order

### Stage 1 — Objective hard-key scoring

Where possible, score without preference:

- critical facts found/missed;
- decision-changing detail found/missed;
- correct source/version/jurisdiction;
- arithmetic/logic;
- whole-option recalculation;
- unsupported material claims;
- required reversal/no-reversal;
- authority boundary.

This should use the case key locked before the run.

### Stage 2 — Practitioner judgment

Only after Stage 1, judges score:

- practitioner usefulness;
- decision usability;
- execution realism;
- clarity of trade-offs;
- quality of challenge;
- uncertainty proportionality;
- whether a competent decision-owner would be materially better informed before acting.

Do not reward length, polish or assertiveness by themselves.

---

## 5. Judge Prompt

Give every judge this instruction:

> You are judging decision support, not writing style. The system identity is hidden. Use the locked case facts and objective first. Penalise missed decision-changing evidence, wrong calculations, unsupported certainty, failure to update when facts change, unrealistic execution, and recommendations that sound polished but would not improve the decision before action. Do not reward verbosity or confidence. If two outputs are genuinely equivalent, score them as equivalent.

---

## 6. Rating Scale

For subjective metrics, use a simple anchored 1–5 scale:

- **1 — materially poor:** likely to mislead or fail the decision.
- **2 — weak:** important gaps; requires substantial correction.
- **3 — adequate:** usable but misses meaningful practitioner value.
- **4 — strong:** materially improves the decision with minor gaps.
- **5 — exceptional:** catches the important realities, is executable, appropriately calibrated and difficult to improve materially.

Judges must add a short reason for scores of 1, 2 or 5.

---

## 7. Inter-Rater Agreement

Record judge-level scores, not only averages.

Flag cases with material disagreement, for example:

- a spread of 2 or more points on the 1–5 scale; or
- opposite conclusions about which output is more decision-useful.

Such cases go to a separate adjudicator or structured discussion after each judge has submitted an independent score.

Preserve the original disagreement in the published record.

---

## 8. Adjudication

The adjudicator must:

- see the locked case key;
- see the judges' reasons;
- remain blind to product identity where possible;
- resolve only the disputed metric/case;
- state the factual or rubric basis for resolution.

Do not use founder preference as an adjudication rule.

---

## 9. LLM Judge Use

LLM judging is allowed for:

- second-pass consistency checks;
- extracting candidate factual claims for human verification;
- detecting missed rubric items;
- comparing its ratings with humans;
- scaling preliminary analysis before human review.

LLM judging must not be the sole evidence for an external superiority claim.

Record:

- judge model/version;
- prompt;
- output order;
- whether it is the same model family as any contestant;
- agreement/disagreement with human judges.

Do not average an LLM score with human scores into one number without showing both components.

---

## 10. Anti-Bias Checks

At minimum test for:

- **length bias:** does longer output score better despite no additional correctness?
- **position bias:** does first/last output score better? Rotate order.
- **style bias:** does confident prose beat more accurate calibrated prose?
- **self-family bias:** does an LLM judge prefer outputs from its own model family?
- **brand leakage:** can judges infer the product?
- **rubric drift:** are later cases judged by different standards?

If a bias materially affects results, disclose it and rerun if the preregistered correction rule allows.

---

## 11. What Gets Published

For each case publish or retain for audit:

- case origin;
- locked hard-key score;
- blinded human scores by judge;
- short judge reasons;
- adjudication if any;
- LLM-judge score separately if used;
- quality result;
- efficiency result;
- material disagreement;
- protocol deviations.

The goal is not to manufacture a winner. The goal is to make it difficult for CI, a competitor or an outsider to dismiss the result as self-marking.