# Versioning Standing Rule

For every published CI Boardroom package update:

1. update the version in both plugin manifests;
2. add a dated entry to `CHANGELOG.md`;
3. rebuild `skills/ci-boardroom/SKILL.md` from the current public `BOARDROOM.md`;
4. verify the Skill contains the current Boardroom gates and preserves human authority;
5. validate JSON manifests, Markdown links and the published behavioural test files;
6. do not present a test definition as a passed model evaluation.
7. verify every relative file referenced by `skills/ci-boardroom/SKILL.md` is bundled inside that Skill folder and fetched by the documented installer.

`BOARDROOM.md` remains the canonical readable operating specification. Installed and pasted copies do not auto-update.
