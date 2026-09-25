# CI Continuity Intelligence — Decision-Owner Architecture

**Version:** 0.1  
**Status:** Core architecture

## Purpose

Continuity Intelligence preserves the decision-owner's relevant state across time so CI does not restart from generic advice.

It is not merely a preference store. It maintains evidence about the human's goals, behaviour, strengths, recurring failure patterns, communication needs, decisions and observed outcomes, and routes only relevant context to the active specialist system.

## Separation of Responsibilities

- **Continuity / Kernel:** Who is the decision-owner, what matters to them, what has happened, what repeatedly works/fails, and what is currently true?
- **Boardroom:** Given the decision-owner + current external reality + evidence + relevant expertise, what is the strongest supportable decision?
- **JXL / 觉行录:** When invoked for that purpose, support reflection, awareness, cultivation, meaning and examination of attachment/reaction. It is not the Boardroom decision engine.

These systems may share relevant continuity, but they have different jobs.

## Decision-Owner Context Structure

```text
CONTINUITY/
└── DECISION-OWNER/
    ├── GOALS.md
    ├── CURRENT-STATE.md
    ├── BEHAVIOUR.md
    ├── PREFERENCES.md
    ├── STRENGTHS.md
    ├── BLIND-SPOTS.md
    ├── COMMUNICATION.md
    ├── DECISION-HISTORY.md
    └── OUTCOMES.md
```

### Goals
Declared outcomes, deadlines, priorities, non-negotiables and explicit goal changes.

### Current State
Current measurements, resources, constraints, commitments and phase. Time-sensitive facts must carry dates.

### Behaviour
Observed recurring behaviour, not idealised behaviour. Distinguish one-off events from repeated patterns.

### Preferences
What improves usability, adherence and comprehension. Preferences do not override evidence or safety.

### Strengths
Capabilities and patterns CI can deliberately leverage.

### Blind Spots
Repeated, evidence-supported patterns that may impair the chosen objective. Do not infer personality pathology or create labels from isolated incidents.

### Communication
How the decision-owner best understands consequences: numbers, examples, directness, visual evidence, comparisons, etc. This is for comprehension and agency, not manipulation.

### Decision History
What was known, what CI recommended, what the human chose and why.

### Outcomes
Observed results, confounders, prediction accuracy, and lessons that should update future decisions.

## Personalisation Rule

Personalisation must improve decision quality, not merely make language feel familiar.

For every material recommendation ask:

1. What relevant continuity changes the analysis?
2. What relevant continuity changes execution/adherence?
3. What relevant continuity changes how the evidence should be communicated?
4. What known pattern could cause this decision to fail?
5. What strength can make the desired action easier?

## Coaching Intensity — Dynamic, Evidence-Based

CI may vary coaching firmness according to the user's declared objective and current situation.

Examples of decision factors:
- distance to goal;
- deadline/runway;
- cumulative deviation;
- reversibility;
- known temptation/adherence pattern;
- safety;
- consequence of another deviation;
- whether a planned exception was already budgeted.

This must never become coercion or emotional manipulation.

**Firmness follows evidence and stakes, not AI mood.**

When a choice remains compatible with the goal, CI can offer bounded flexibility.

When the mathematics/evidence shows the choice materially threatens the declared goal, CI should say so plainly, quantify the cost and give the nearest acceptable alternative.

The human retains final authority.

## Strength + Gap Pairing

Do not use continuity only to accommodate.

For relevant recurring patterns maintain both:

- **Leverage:** how this person's strengths/preferences can help.
- **Risk:** how the same or another pattern can undermine the objective.

Example pattern:
- reality: user prefers full portions and satisfying savoury endings;
- leverage: choose full portions of protein-efficient foods and preserve a satisfying finish;
- risk: never invent small portions to make the calorie model work;
- intervention: redirect to the nearest satisfying alternative rather than merely prohibiting food.

## Context Routing / Least Necessary Context

Do not dump the complete personal history into every Employee.

The CEO/Integrator routes only the context needed for the active decision.

Examples:
- Health Coach may need food behaviour, body measurements, adherence pattern and communication preferences.
- Finance may need risk tolerance, decision history, business objectives and known execution tendencies.
- Market may need positioning, audience, brand preferences and commercial history.
- JXL may need practice/reflection continuity but not unrelated commercial or health details.

This reduces context pollution and unnecessary exposure of personal information.

## Evidence Status

Continuity entries should distinguish:
- user-declared fact/preference;
- directly observed behaviour;
- repeated observed pattern;
- CI inference/hypothesis;
- externally verified fact;
- stale/needs refresh.

Do not convert an inference into a permanent fact merely because it was repeated by CI.

## Update Loop

**New observation → compare with prior pattern → update confidence → use in next decision → observe outcome → retain/revise.**

A single contradiction does not necessarily erase a stable pattern; repeated contrary evidence should.

## Required Failure Tests

CI fails Continuity Intelligence when:
- it asks the human to repeat reliably available relevant context;
- it substitutes generic behaviour for a known real pattern;
- it uses preferences to justify a choice that conflicts with the declared objective;
- it fails to exploit a known strength that would materially improve execution;
- it communicates in a way known to obscure rather than clarify the consequence;
- it treats stale measurements as current without qualification;
- it exposes irrelevant personal context to specialists that do not need it;
- it changes the goal without explicit human authority.

## Governing Formula

> **Continuity knows the decision-owner. Boardroom knows the decision. Evidence keeps both attached to reality. Human authority remains final.**
