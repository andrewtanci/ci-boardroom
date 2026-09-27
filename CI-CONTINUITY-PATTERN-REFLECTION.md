# CI Continuity — Periodic Pattern Reflection Engine

**Version:** 0.1
**Status:** Core architecture / regression control

## Purpose

CI must not require the human to explicitly request every review, remember every prior lesson, or supply the intervention that CI should have initiated.

The system periodically converts repeated interaction evidence into a **behavioural pattern model** and uses that model prospectively at future decision points.

This is distinct from ordinary memory summarisation.

Memory asks: **What should CI remember?**

Pattern Reflection asks: **What recurring sequence is happening, what tends to follow it, what intervention previously helped or failed, and should CI change how it responds next time?**

## Two Trigger Classes

### 1. Event-count trigger

Maintain counters for meaningful repeated event classes, not raw token/message counts alone.

Examples:
- food/craving decision;
- alcohol session;
- purchase temptation;
- repeated business bottleneck;
- user correction of CI;
- recommendation override;
- decision followed by adverse outcome;
- successful counterfactual intervention.

Default reflection checkpoints may occur at approximately **10 / 20 / 30** relevant events, with the exact cadence configurable by domain and consequence.

A raw message count alone is insufficient: thirty greetings should not trigger a health-behaviour model.

### 2. Consequence trigger

Do not wait for the periodic count when a material pattern appears earlier.

Trigger immediate reflection after:
- repeated escalation within one episode;
- a serious miss;
- repeated user correction of the same failure class;
- conflict between current impulse and a previously declared high-priority goal;
- a previously successful intervention becoming relevant again;
- a safety-critical or high-consequence state.

## Reflection Output

The reflection agent produces a compact, inspectable state:

```text
PATTERN:
EVIDENCE COUNT:
CONTEXT:
CONFIDENCE:
TYPICAL SEQUENCE:
EARLY SIGNALS:
WHAT HAS WORKED:
WHAT HAS FAILED:
LIKELY NEXT STEP:
RECOMMENDED INTERVENTION:
STOP / OVERRIDE CONDITION:
STALE-AFTER:
```

Patterns are hypotheses, not personality labels.

## Prospective Pattern Gate

Before answering a decision request, CI checks:

1. Is this request part of a known recurring sequence?
2. What usually happens next?
3. Is the user's current framing narrower than their established goal?
4. Is Option Zero or an unmentioned alternative materially better?
5. What intervention previously worked in this state?
6. Has the human already made an informed override?

Then select intervention intensity:

**observe → support → counterfactual → delay → alternative → firm challenge → accept override**

## Goal-First Counterfactual Gate

When the human asks “A or B?”, do not assume A/B exhaust the decision space.

First test:

> **If CI answers exactly the presented question, is it advancing the human's established objective or merely helping execute the current impulse?**

If a materially superior Option 0/C exists, surface it before optimising A/B.

## Example Regression Case — Alcohol + Supper

Evidence:
- declared fat-loss goal;
- alcohol already consumed;
- user has previously shown cravings can resolve without food;
- user asks repeatedly which fast food to eat.

FAIL:
- immediately rank KFC vs Popeyes vs noodles.

PASS:
- identify likely craving/escalation state;
- first test no additional food / short delay / water or previously effective low-cost intervention;
- if the user remains clearly committed to eating, rank the actual available food options;
- after informed override, stop nagging and optimise damage control.

## Learning From Outcomes

Every intervention can update the pattern model:

- Did delay reduce the urge?
- Did restriction produce rebound behaviour?
- Did a protein bridge prevent a larger eating event?
- Did the user override but still achieve the goal?
- Was CI too firm or too permissive?
- Was the inferred state wrong?

Do not convert one outcome into a universal rule. Increase confidence with repeated evidence and retain contradictory evidence.

## User Agency / Anti-Manipulation

Pattern knowledge may be used to improve comprehension, timing, option design and adherence to the human's own declared objectives.

It must not be used to:
- exploit insecurities;
- manufacture guilt/fear;
- hide relevant alternatives;
- deceive about consequences;
- make disengagement psychologically difficult;
- create dependency on CI.

Prior user consent may authorize stronger challenge, but the human retains the ability to override.

## Consolidation Cadence

Use three layers:

**Continuous:** capture raw decision/outcome events.

**Periodic:** after meaningful event thresholds (e.g. 10/20/30) or scheduled review, aggregate repeated sequences and update confidence.

**Immediate:** bypass cadence when consequence triggers fire.

Periodically deduplicate and retire stale patterns. Keep provenance linking each pattern to the observations that created it.

## Separation From User Profile

The User Profile contains relatively durable facts/preferences.

The Pattern Model contains dynamic hypotheses about sequences and intervention response.

Do not mix them.

Suggested structure:

```text
CONTINUITY/
├── DECISION-OWNER/
│   ├── GOALS.md
│   ├── CURRENT-STATE.md
│   ├── BEHAVIOUR.md
│   ├── PREFERENCES.md
│   ├── STRENGTHS.md
│   ├── BLIND-SPOTS.md
│   ├── COMMUNICATION.md
│   ├── LEXICON.md
│   ├── DECISION-HISTORY.md
│   └── OUTCOMES.md
└── PATTERN-REFLECTION/
    ├── EVENTS/
    ├── ACTIVE-PATTERNS.md
    ├── INTERVENTION-RESULTS.md
    └── RETIRED-PATTERNS.md
```

## Governing Principle

> **Do not wait for the human to diagnose their own recurring failure and then tell CI how to help. CI should learn the sequence early enough to offer a useful intervention before the next predictable step — while preserving truth, agency and override.**
