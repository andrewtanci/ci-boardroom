# Install CI Boardroom

**Delegate the work. Do not delegate the authority.**

CI Boardroom remains usable by copy and paste, and is now also packaged as a reusable, self-contained Skill. The installable folder contains `SKILL.md` and both referenced rider files.

## 1. Codex Skill — complete self-contained package

Run this in Terminal:

```bash
install_dir="$HOME/.codex/skills/ci-boardroom"
base_url="https://raw.githubusercontent.com/andrewtanci/ci-boardroom/main/skills/ci-boardroom"

mkdir -p "$install_dir"

for file in \
  SKILL.md \
  CI-MULTI-FACTOR-REALITY-OUTCOME-RIDER.md \
  CI-MARGINAL-GAINS-TIMING-HABIT-LEVERAGE-RIDER.md
do
  curl -fsSL "$base_url/$file" -o "$install_dir/$file" || exit 1
done

test -s "$install_dir/SKILL.md" && \
test -s "$install_dir/CI-MULTI-FACTOR-REALITY-OUTCOME-RIDER.md" && \
test -s "$install_dir/CI-MARGINAL-GAINS-TIMING-HABIT-LEVERAGE-RIDER.md"
```

Inspect the three downloaded files, then start a new Codex session. Ask naturally, or say: `Use CI Boardroom on this.`

## 2. Claude Code plugin

In Claude Code:

```text
/plugin marketplace add andrewtanci/ci-boardroom
/plugin install ci-boardroom@ci-boardroom
/reload-plugins
```

Then ask naturally or invoke the CI Boardroom skill.

## 3. Claude.ai custom Skill

Download all three files into one folder named `ci-boardroom`:

- [SKILL.md](skills/ci-boardroom/SKILL.md)
- [Multi-Factor Reality & Outcome Rider](skills/ci-boardroom/CI-MULTI-FACTOR-REALITY-OUTCOME-RIDER.md)
- [Marginal Gains, Timing & Habit Leverage Rider](skills/ci-boardroom/CI-MARGINAL-GAINS-TIMING-HABIT-LEVERAGE-RIDER.md)

Compress the complete `ci-boardroom` folder as a ZIP, then upload the ZIP through Claude.ai's Skills interface if your account supports custom Skills.

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
- Re-run the complete Codex installation block above to replace all three local package files with the current public version.
- Before relying on a new model or setup, run the published Accuracy and Outcome behavioural tests.
- Test files are regression benchmarks, not guarantees of universal performance.
