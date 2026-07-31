# Segment C Status — Installers + Versioning

**Branch:** `feature/installers`  
**State:** review-ready; not merged; no release, GPT or plugin was published.

## Files added

- `.claude-plugin/marketplace.json`
- `.claude-plugin/plugin.json`
- `.codex-plugin/plugin.json`
- `skills/ci-boardroom/SKILL.md`
- `docs/installer-spec-verification.md`
- `INSTALL.md`
- `CHANGELOG.md`
- `release-drafts/v1.0.0.md`
- `VERSIONING.md`

## Files changed

- `BOARDROOM.md`: only the permitted version line was added at the top.
- `README.md`: one Install options section was added.
- `AGENTS.md`: unchanged. The connected repository policy rejected a full-file rewrite because the existing public-repository instructions contain broader product language that conflicts with the locked-three-products rule. The identical requested standing rule is preserved in `VERSIONING.md` for review; it can be moved into `AGENTS.md` only after the conflicting legacy text is separately resolved.

## Specification result

See `docs/installer-spec-verification.md`. Claude Code, Claude.ai, GPT Store and OpenAI's now-documented universal ChatGPT/Codex plugin route were checked against current official sources. Unstated limits are marked **unverifiable**.

## Release status

Release title and notes are prepared in `release-drafts/v1.0.0.md`. The GitHub connector available in this run does not expose a create-draft-release action, so no server-side draft release was created. Nothing was published.

## Andrew account actions

- create and test the ChatGPT GPT;
- complete the Builder Profile;
- provide or approve public support, privacy and terms URLs;
- approve the ZIP release asset;
- explicitly approve GitHub Release publication;
- separately approve OpenAI plugin submission and later publication.
