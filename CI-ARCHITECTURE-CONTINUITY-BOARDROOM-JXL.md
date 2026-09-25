# CI Architecture Map — Continuity × Boardroom × JXL

**Version:** 0.1

## One-System View

```text
                         HUMAN DECISION-OWNER
                                  │
                                  ▼
                    CONTINUITY INTELLIGENCE
                 relevant state across time
                                  │
                    context routing / update
                    ┌─────────────┴─────────────┐
                    ▼                           ▼
             CI BOARDROOM                    JXL / 觉行录
          decision intelligence          reflection/cultivation
                    │                           │
                    ▼                           │
        CEO / Chief Integrator                  │
                    │                           │
       ┌────────────┼────────────┐              │
       ▼            ▼            ▼              │
    Evidence     Employees      Tools            │
       │            │            │              │
       └────── Shared Decision State ───────────┘
                    │
                    ▼
          recommendation / challenge
                    │
                    ▼
            HUMAN FINAL AUTHORITY
                    │
                    ▼
                 OUTCOME
                    │
                    └─────> Continuity update
```

## Responsibilities

### Continuity Intelligence
Preserves relevant goals, current state, behaviour, preferences, strengths, blind spots, communication needs, decision history and outcomes.

### Boardroom
Dynamically assembles the necessary expertise, retrieves current external evidence, challenges assumptions, calculates consequences, proposes the strongest supportable action and preserves human authority.

### JXL
Uses relevant continuity when the requested purpose is reflection/cultivation rather than decision optimisation. Understanding is not agreement; reflection is not authority transfer.

## Runtime Sequence

1. Parse current human request.
2. Retrieve relevant continuity.
3. Identify objective and current phase.
4. Route to Boardroom, JXL or both according to purpose.
5. Boardroom selects required Employees dynamically.
6. Evidence/Research establishes current external reality.
7. Employees perform discipline-specific work and challenge.
8. CEO integrates without hiding material dissent.
9. Communication layer expresses the result in the form most likely to be understood accurately by this decision-owner.
10. Human chooses.
11. Capture decision/outcome where appropriate.
12. Update Continuity and regression controls.

## Critical Distinction

**Personalisation is not persuasion.**

CI may tailor explanation, examples, sequencing and firmness to improve comprehension and execution of the human's own declared objective. It must not exploit vulnerabilities, conceal alternatives, manufacture urgency or override human authority.

## Coaching Example

The same food choice can receive different guidance depending on:
- current measured state;
- distance to declared target;
- deadline;
- prior planned exceptions;
- today's intake/activity;
- repeated behaviour;
- whether the person needs flexibility or a firm boundary to protect their own chosen goal.

The evidence and arithmetic remain the same. The communication and recommended alternative may be personalised.

## Business Example

A CEO may receive:
- concise runway impact rather than long prose;
- an explicit execution bottleneck because history shows implementation slippage;
- a direct stop gate when another commitment makes the plan infeasible.

The Boardroom does not change evidence to suit the CEO. It changes the **delivery and execution design** so the evidence is more usable.

## Pull-Out Principle

Continuity must remain a separable architectural layer. It can be:
- inspected independently;
- upgraded independently;
- routed into different CI products;
- withheld from irrelevant Employees;
- tested independently from Boardroom reasoning.

This prevents the user model from becoming buried inside a monolithic prompt.
