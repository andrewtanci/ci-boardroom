# Install CI Boardroom — 30 seconds

**Delegate the work. Do not delegate the authority.**

## 1. Universal paste — works now

1. Open [BOARDROOM.md](BOARDROOM.md).
2. Copy the whole file.
3. Paste it into a new ChatGPT, Claude, Gemini, Kimi, Qwen or DeepSeek conversation.
4. Add your task. You remain the final decision-owner.

## 2. Claude Code plugin

In Claude Code:

```text
/plugin marketplace add andrewtanci/ci-boardroom
/plugin install ci-boardroom@ci-boardroom
/reload-plugins
```

Then ask naturally or invoke the namespaced CI Boardroom skill.

## 3. Claude.ai custom Skill

1. Download the `ci-boardroom-skill.zip` asset from the approved GitHub Release when it is published.
2. In Claude.ai, go to **Customize → Skills → + → Create skill → Upload a skill**.
3. Upload the ZIP and enable **CI Boardroom**.

Until the release asset exists, use the universal-paste method. No asset or release is live from this branch.

## 4. ChatGPT GPT

**Placeholder:** the public CI Boardroom GPT link does not exist yet.

Andrew must create and approve the GPT in his account. Exact steps are in [docs/installer-spec-verification.md](docs/installer-spec-verification.md).

## 5. ChatGPT/Codex plugin

The repository includes the current `.codex-plugin/plugin.json` skills-only package. Public listing requires OpenAI review and Andrew's later approval; it has not been submitted.

Interim transparent Codex fetch pattern:

```bash
mkdir -p "$HOME/.agents/skills/ci-boardroom"
curl -fsSL https://raw.githubusercontent.com/andrewtanci/ci-boardroom/main/skills/ci-boardroom/SKILL.md \
  -o "$HOME/.agents/skills/ci-boardroom/SKILL.md"
```

Inspect the downloaded file before use, then start a new Codex session.

## Get updates

Click **Watch → Custom → Releases** on GitHub.

Pasted copies do not auto-update; the latest file always lives here.
