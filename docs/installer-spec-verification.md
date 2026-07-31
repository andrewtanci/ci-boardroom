# Installer Spec Verification — 31 July 2026

Every specification below was checked against an official source on 31 July 2026. Anything the official source did not state is marked **unverifiable**.

| Surface | Verified current specification | Direct source | Status / implication |
|---|---|---|---|
| Claude Code plugin | A distributable marketplace uses `.claude-plugin/marketplace.json`; each plugin requires at least `name` and `source`. Plugin components live at the plugin root; only `plugin.json` belongs inside `.claude-plugin/`. Skills use `skills/<name>/SKILL.md`. Installation uses `/plugin marketplace add …`, then `/plugin install plugin@marketplace`, then `/reload-plugins`. | https://code.claude.com/docs/en/plugin-marketplaces · https://code.claude.com/docs/en/plugins · https://code.claude.com/docs/en/plugins-reference | **VERIFIED.** This branch includes both manifests and the skill. |
| Claude.ai consumer Skill | Create a skill folder with a `SKILL.md`/skill file containing required `name` and `description` metadata, ZIP the folder, then go to Customize → Skills → + → Create skill → Upload a skill. Custom uploads are private to the individual account unless organization sharing/provisioning is used. | https://support.claude.com/en/articles/12512198-how-to-create-custom-skills · https://support.claude.com/en/articles/12512180-use-skills-in-claude | **VERIFIED.** An exact numeric Skill ZIP size limit was not stated on the official Skill pages checked: **unverifiable**. |
| GPT Store | Public publishing depends on plan/workspace permissions. The builder profile may need a verified name/domain/social profile. Public Actions require a valid privacy-policy URL. Public GPTs are checked against policy/product requirements. | https://help.openai.com/en/articles/8798878-sharing-and-publishing-gpts · https://help.openai.com/en/articles/8554397-creating-and-editing-gpts | **VERIFIED.** A current official GPT instruction-character limit was not stated on the official GPT pages checked: **unverifiable**. Andrew must create and test the GPT in his account. |
| ChatGPT/Codex plugin | OpenAI now documents a universal plugin directory shared by supported ChatGPT and Codex surfaces. Every plugin has `.codex-plugin/plugin.json`; a skills-only plugin may point `skills` to `./skills/`. Public submission requires Apps Management write access, verified developer/business identity, listing/legal/support URLs, starter prompts, five positive and three negative test cases, and review before the publisher chooses to publish. | https://developers.openai.com/plugins/build/plugins · https://developers.openai.com/plugins/deploy/submission · https://developers.openai.com/codex/plugins | **VERIFIED.** This supersedes the earlier assumption that third-party submission was undocumented. No submission or publication was performed. |
| Codex interim local install | Codex discovers personal skills under `$HOME/.agents/skills`. The repository can supply a transparent one-file fetch until a public plugin is approved. | https://developers.openai.com/codex/skills · https://developers.openai.com/codex/plugins | **VERIFIED pattern.** Users must inspect the fetched file before enabling it. |

## Account-only GPT Store steps

1. Open ChatGPT → Explore GPTs → Create.
2. Set the name to **CI Boardroom**.
3. Paste the versioned Boardroom instructions into the GPT instructions.
4. Add realistic conversation starters and test in Preview.
5. Complete the Builder Profile using the intended verified identity/domain.
6. If any public Action is later added, add its valid privacy-policy URL.
7. Choose a category, review public listing details and policy requirements.
8. Keep it private or link-only for review first. Publish only after Andrew explicitly approves.

## OpenAI plugin submission items still needing Andrew

- Verified individual or business identity in the publishing organization.
- Apps Management write access.
- Public website, support, privacy-policy and terms URLs.
- Production-ready logo and category.
- Five positive and three negative reviewer test cases.
- Final country availability selection.
- Explicit approval to submit and, after approval, a separate explicit approval to publish.
