# Changelog

All notable changes to the CI Boardroom package are recorded here.

## [1.1.1] — 22 September 2026

- Correct distribution drift: generate Skill references and the complete paste bundle from the canonical load manifest.
- Include the current 28-section Multi-Factor rider and previously omitted Execution Hard Gates.
- Align install, quick-start and behavioural-test loading instructions.
- Stage and checksum downloads before replacement; preserve previous installations and isolate shell failures. Builds on the installer failure reported in draft PR #6 without merging that stale three-file patch.
- Add deterministic distribution and failure-recovery tests. These are packaging tests, not model behavioural passes or comparative superiority evidence.
- Require exact checksum coverage and the complete four-file runtime manifest; reject omissions, duplicate entries and unexpected paths before installation or generation.
- Preserve existing canonical decision rules. No new council architecture, automatic memory, client installation or technical enforcement of prompt rules is claimed.

## [1.1.0] — 15 August 2026

- published the reusable CI Boardroom Skill and Claude/Codex plugin manifests
- synchronized the Skill with the current public `BOARDROOM.md`
- included the Accuracy Before Agreement gate and six Accuracy Level 1 behavioural tests
- included the Multi-Factor Reality & Outcome and Marginal Gains, Timing & Habit gates
- published the twelve-test outcome regression benchmark
- preserved universal-paste use alongside installable Skill routes
- bundled both referenced rider files inside the installable Skill folder and updated installation to fetch the complete self-contained package

The behavioural tests are evaluation cases, not proof of universal model performance. Each model and setup still requires validation.

## [1.0.0] — Draft prepared 31 July 2026

- prepared the first installer and manifest draft
- kept the draft isolated until the Boardroom content gaps were repaired and approved
