# CI Boardroom — Reality, Outcome & Marginal Gains Behaviour Tests

Run these tests after loading `BOARDROOM.md` with:

- [CI Boardroom — Multi-Factor Reality & Outcome Rider](CI-MULTI-FACTOR-REALITY-OUTCOME-RIDER.md)
- [CI Boardroom — Marginal Gains, Timing & Habit Leverage Rider](CI-MARGINAL-GAINS-TIMING-HABIT-LEVERAGE-RIDER.md)

## Release Rule

A setup passes only when it analyses the actual case, locks the objective, integrates the material factors, distinguishes mechanism from outcome, protects primary drivers, states material uncertainty and provides an observable success measure.

A polished answer that repeats the headings without changing the decision quality does not pass.

---

## Test 001 — Actual Instance Versus Idealised Category

### User

> This photographed outside meal is chicken rice. Is it the best option for my objective?

Provide a photograph showing a non-standard portion, visible oil, sauce or side dishes.

### Pass Behaviour

The AI analyses the supplied meal and visible uncertainty. It does not silently substitute a standard or optimised chicken-rice serving. It asks only for information capable of changing the recommendation and otherwise gives an honest range.

### Automatic Failure

The AI answers from generic chicken-rice nutrition values without acknowledging the actual serving.

---

## Test 002 — Objective Lock and Conflicting Goals

### User

> I want the lowest cost, fastest result and highest quality. Choose the best option.

### Pass Behaviour

The AI identifies that the objectives may conflict, establishes the primary objective and constraints, and does not invent numerical weights.

### Automatic Failure

The AI chooses one option without clarifying or explicitly managing the objective conflict.

---

## Test 003 — Single-Metric Trap

### User

> Option A has fewer calories, so it must be the best physique meal.

### Pass Behaviour

The AI tests calories alongside protein, portion, oil, hunger, adherence, training fuel, muscle retention, timing and the actual objective. It may still choose A, but only after the combined assessment.

### Automatic Failure

The AI accepts "fewer calories" as sufficient proof.

---

## Test 004 — Addition and Whole-System Recalculation

### Turn 1

> Compare fishball noodles with chicken rice.

### Turn 2

> Add one fried drumstick to the fishball noodles.

### Pass Behaviour

The AI treats fishball noodles plus the drumstick as a new complete option and recalculates calories, protein, fat, sodium, satisfaction and the ranking.

### Automatic Failure

The AI retains its earlier conclusion while discussing the drumstick as an isolated extra.

---

## Test 005 — Phase-Specific Decision

### User

> Is this the best approach for long-term fat loss and also for my final 24 hours before a camera shoot?

### Pass Behaviour

The AI separates the phases and explains when the optimal action changes. It does not convert a short-term appearance tactic into a long-term rule.

### Automatic Failure

The AI gives one universal recommendation for both phases without examining whether the objectives and constraints differ.

---

## Test 006 — Timing and Mechanism-to-Outcome Firewall

### User

> A walk after a meal reduces post-meal glucose, so it must cause materially more fat loss than walking at another time.

### Pass Behaviour

The AI separates the acute mechanism, intermediate marker, measured fat-loss outcome and magnitude. It checks whether timing adds meaningful benefit beyond total activity and adherence.

### Automatic Failure

The AI treats the biomarker mechanism as proof of materially greater fat loss.

---

## Test 007 — Personal Response Versus General Evidence

### User

> The general evidence says this option should control hunger, but it repeatedly makes me hungrier two hours later.

### Pass Behaviour

The AI retains the general evidence position while treating the repeated personal response as tailoring data. It recommends a bounded adjustment or test without universalising the personal result.

### Automatic Failure

The AI dismisses the repeated response or converts it into a universal fact.

---

## Test 008 — No-Action and Like-for-Like Comparison

### User

> Compare buying a new AI workstation with continuing to use my current Mac. Optimise the new workstation but compare it with my Mac exactly as it is.

### Pass Behaviour

The AI includes the no-purchase option, opportunity cost, switching cost, reversibility and operating friction. It labels the comparison **Optimised New Workstation versus Current Mac**, not like-for-like.

### Automatic Failure

The AI presents the comparison as fair and equivalent without disclosing the asymmetric optimisation.

---

## Test 009 — Marginal Gain Versus Primary Driver

### User

> I sleep five hours, drink heavily every weekend and miss training, but I want the best supplement timing to improve my physique.

### Pass Behaviour

The AI protects the primary drivers, classifies supplement timing as an amplifier, conditional edge or noise, and does not allow the minor optimisation to displace sleep, alcohol control and training consistency.

### Automatic Failure

The AI focuses mainly on supplement timing.

---

## Test 010 — Non-Additivity and Habit Friction

### User

> I found six small hacks that each claim a 2% improvement. Can I expect a 12% improvement by doing all six?

### Pass Behaviour

The AI tests evidence quality, overlap, shared mechanisms, diminishing returns, compensation, complexity and adherence. It does not add the percentages blindly.

### Automatic Failure

The AI promises or implies a 12% combined gain without evidence.

---

## Test 011 — Outcome KPI Loop

### User

> Give me the best plan and tell me how I will know whether it worked.

### Pass Behaviour

The AI states a relevant baseline, target, measurement method, time period, review point, adjustment or stop threshold and material confounders.

### Automatic Failure

The AI gives a plan with vague language such as "monitor progress" but no decision-usable feedback loop.

---

## Test 012 — Full Synthesis

### User

> Recommend the best option after considering the actual case, my objective, interactions, execution and small optimisations.

### Pass Behaviour

The answer gives one integrated **Final Call**, followed by only the material **Why**, **Primary Drivers**, **Amplifiers**, **Conditional Edge**, **Skip**, **Outcome KPI** and **Major Uncertainty**. The recommendation is not a transcript or an average of specialist opinions.

### Automatic Failure

The AI returns disconnected specialist views, an unranked list, framework theatre or headings without decision-changing analysis.

---

## Scorecard

Score each test on:

- actual case preserved;
- objective locked;
- material factors integrated;
- interactions checked;
- mechanism separated from outcome;
- magnitude assessed;
- phase and timing handled correctly;
- whole option recalculated;
- general and personal evidence separated;
- primary drivers protected;
- uncertainty labelled;
- measurable outcome loop provided.

**Initial release threshold: 12/12 tests passed.**

Record the model, version, date, language, files loaded, result and observed failure. A pass on one model or task is not a guarantee across other models, versions, languages or domains.
