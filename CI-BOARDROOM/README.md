# CI Boardroom — Modular Runtime Prototype

**Status:** Prototype. The current canonical Boardroom remains the production baseline until this modular architecture passes benchmark and regression gates.

## Purpose

This directory is the first implementation of the Employee Folder architecture defined in `CI-EMPLOYEE-ARCHITECTURE.md`.

Each Employee is a bounded AI capability package. Employees may be enabled, disabled, upgraded and tested independently, subject to dependency and integration checks.

## Initial Team

1. `EMPLOYEES/CEO-INTEGRATOR/` — routes work, integrates disagreement, preserves human authority.
2. `EMPLOYEES/EVIDENCE-RESEARCH/` — retrieves and verifies evidence; enforces Reality Contact.
3. `EMPLOYEES/FINANCE-COMMERCIAL/` — tests economics, commercial assumptions and quantitative consequences.
4. `EMPLOYEES/OPERATIONS-TECHNICAL/` — tests feasibility, execution constraints and technical reality.

## Shared State

All Employees coordinate through `SHARED-WORKSPACE/DECISION-LEDGER.md` rather than relying on unstructured agent conversation.

## Prototype Rule

Do not claim the modular architecture is superior merely because it is cleaner. It must beat or match the current Boardroom on locked cases without unacceptable cost/latency regression before promotion.
