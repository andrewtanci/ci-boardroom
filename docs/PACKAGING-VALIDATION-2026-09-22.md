# Packaging correction — 22 September 2026

Scope approved: align distribution and installation with the existing canonical runtime. Do not redesign the council or claim the prompt rules are technically enforced.

Baseline: `f9efad0370e4a2f5956fddbae409d902dbd5474a`.

Observed failures before implementation: stale packaged Multi-Factor rider; absent execution gates; no complete paste export; failed downloads modifying the old installation; the documented installer missing a required file. Four test methods ran and reported five failures (including subtests).

Correction: generate package references, checksum list and complete paste export from the load manifest; stage and verify downloads before replacing the installation; retain the previous directory; correct onboarding and test-loading instructions. Existing canonical runtime bodies remain unchanged.

Verification: `python3 scripts/sync_package.py --check`; `python3 -m unittest discover -s tests -v`; `bash -n scripts/install_skill.sh`; `git diff --check`.

Nine deterministic tests cover canonical/reference equality, complete ordered paste content, failed downloads, successful full installation, checksum mismatch, failed replacement restoration, drift detection/regeneration, exact checksum coverage, and rejection of incomplete/duplicate/malformed load manifests. Network retrieval and the injected failed move are controlled test doubles; the actual documented shell block and filesystem operations run in temporary directories. No user installation is modified by these tests.

Fresh review found an incomplete-checksum-list acceptance defect in the first patch. A truncated list allowed an altered unlisted rider through verification. Regression cases reproduced this before correction. The installer now rejects omitted, duplicate, unexpected and path-bearing checksum entries before checking hashes. The generator requires the exact four-file runtime sequence, and the test harness preserves the installer exit status independently of the parent-shell sentinel. Checksums establish consistency against the downloaded manifest, not authenticity against a compromised publisher.

Reviewer probes additionally exercised paths with spaces, refused symlink destinations, caught TERM during replacement and recoverable previous user files. Native macOS/Bash 3.2, real network authenticity, power-loss durability and model behaviour were not exercised; Linux Bash 5.2 was available.

Decision: this evidence supports the package correction, not a model-quality release claim. Retrieval quality, recalculation, synthesis, goal protection, practical expertise and feedback recurrence still require observed model runs. No new model benchmark or independent performance panel was run.

Rulings: preserve the existing public-repository Skill distribution rather than installing a personal ChatGPT Skill; do not alter canonical decision rules during a packaging fix; retain recoverable installer backup/staging directories rather than deleting user files; use the existing checkout on a new branch, preserving the previous release branch. Costs: installed client copies still need updating, behavioural gaps may remain, and retained directories use disk space.

Review focus: macOS Bash 3.2 compatibility; spaces in destination paths; interrupted replacement; symlink targets; stale or mixed downloads; generator changes omitting a required source. An uncatchable termination/power loss can require manual recovery from the retained previous directory.
