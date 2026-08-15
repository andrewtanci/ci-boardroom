# Install CI Boardroom

**Delegate the work. Do not delegate the authority.**

CI Boardroom remains usable by copy and paste, and is now also packaged as a reusable Skill.

## 1. Codex Skill — one command

Run this in Terminal:

```bash
mkdir -p "$HOME/.codex/skills/ci-boardroom" && \
curl -fsSL https://raw.githubusercontent.com/andrewtanci/ci-boardroom/main/skills/ci-boardroom/SKILL.md \
  -o "$HOME/.codex/skills/ci-boardroom/SKILL.md"
```

Inspect the downloaded file, then start a new Codex session. Ask naturally, or say: `Use CI Boardroom on this.`

## 2. Claude Code plugin

In Claude Code:

```text
/plugin marketplace add andrewtanci/ci-boardroom
/plugin install ci-boardroom@ci-boardroom
/reload-plugins
```

Then ask naturally or invoke the CI Boardroom skill.

## 3. Claude.ai custom Skill

Download [skills/ci-boardroom/SKILL.md](skills/ci-boardroom/SKILL.md), place it in a folder named `ci-boardroom`, compress that folder as a ZIP, then upload the ZIP through Claude.ai's Skills interface if your account supports custom Skills.

## 4. Universal paste — works across models

1. Open [BOARDROOM.md](BOARDROOM.md).
2. Copy the whole file.
3. Paste it into a new ChatGPT, Claude, Gemini, Kimi, Qwen or DeepSeek conversation.
4. Add your task. You remain the final decision-owner.

## 5. ChatGPT and public plugin listing

The source package and Codex manifest are public in this repository. A public ChatGPT plugin/GPT listing is a separate review and publishing step and is not claimed here.

## What a Skill is

A Skill is a reusable instruction package with discovery metadata. Its core is still readable Markdown: that transparency is intentional. Compatible clients load it automatically when relevant; the universal-paste route remains available for clients that do not install Skills.

## Updates and verification

- Pasted copies do not auto-update.
- Re-run the Codex command above to replace the local copy with the current public version.
- Before relying on a new model or setup, run the published Accuracy and Outcome behavioural tests.
- Test files are regression benchmarks, not guarantees of universal performance.
