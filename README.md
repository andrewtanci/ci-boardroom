# Continuation Intelligence

**Let AI do the work. You stay in control.**

Continuation Intelligence brings CI Kernel continuity instructions and Boardroom decision-support instructions together in one package. Start directly. You do not need a separate Kernel installation or a sequence of book chapters.

**Continuity & Recovery candidate: 1.3.0-rc.1.** This branch prepares a reviewed-checkpoint workflow and recovery guides. It is not a published release. The stable `main` package remains 1.2.0 until review and approval.

## Try CI

1. **[Download the combined CI Skill ZIP](downloads/Continuation%20Intelligence%20-%20Download%20Skills.zip?raw=true)** — Kernel, Boardroom, required riders, setup and recovery guides in one package. Keep an untouched copy.
2. **[Set it up](START-HERE.md)** through your AI app's supported Skill import route. Check that the complete instructions and riders can be read. The technical Skill name is `ci-boardroom`.
3. **[Try the fictional workshop example](examples/continuity-recovery-example.md)**, then check its objective, constraints, owner and next step against the source card.

For a one-chat trial, use the [complete copy/paste text](downloads/Continuation%20Intelligence%20-%20Copy%20and%20Paste.txt?raw=true) from the same version. Use one loading route per task. App support and context limits vary; a partial load is incomplete.

This repository is the main home for CI downloads, demos, releases and stars. [SkillsNova's CI download page](https://skillsnova.sg/#bonus) provides public setup context and may continue to serve the stable package during candidate review. The [Kernel repository](https://github.com/andrewtanci/ci-perpetual-kernel) retains historical component sources; no separate install is needed.

The [download checksums](downloads/SHA256SUMS) verify exact files. See the [release candidate notes](docs/RELEASE-CANDIDATE-1.3.0-rc.1.md) for checks, limits and remaining approval steps.

## Continue in a new chat

When you want to move your work to a new chat, type **full migrate**. Wait for the answer, review the continuation block, then copy and paste it into the new chat. Keep your own saved copy and the original source files.

The command prepares a handover from the information the AI can access. Check important details and missing information before continuing. Follow the [save, load, verify and recovery steps](CONTINUITY-RECOVERY.md), using the [18-field checkpoint template](CHECKPOINT-TEMPLATE.md).

## What it helps with

Continuation Intelligence provides instructions for the AI to:

- examine evidence, challenge assumptions and expose uncertainty;
- compare the actual options against your objective and constraints;
- use task-specific analytical roles to identify objections and practical next steps;
- keep decisions, versions and approval boundaries explicit;
- prepare a continuation block for you to review, save and carry into a later conversation;
- keep you, or a named accountable human, in charge of consequential decisions and external actions.

The authority flags are Assist, Advise, Approve and Stop / Escalate. Expert roles are AI analytical perspectives unless a real qualified professional is involved.

## What to expect

Continuation Intelligence is a reusable instruction package. It can guide a model's approach, but it cannot guarantee compliance, accuracy or correct results.

It does not install automatic memory, background monitoring, a scheduler or account connections. Continuity depends on the material the AI can access and the checkpoints you review, save and provide again. Your AI app controls its tools, context capacity, permissions and Skill support.

Test a small task in your own setup and check the output against your sources. A checksum verifies file consistency, not model behaviour. Existing pasted copies do not auto-update.

## Repository and development references

The current reader downloads are in [downloads/](downloads/), generated from `CI-PUBLIC-KERNEL.md` and the canonical Boardroom source by `python3 scripts/build_reader_downloads.py`. This repository also preserves the Boardroom source, earlier component packaging, examples and diagnostic tests. The older Boardroom-only engineering files remain development references, not additional required installs. The main public ZIP also carries the setup guide, checkpoint template, recovery guide, fictional example and MIT licence.

For current customer setup, use [Start Here](START-HERE.md) or [SkillsNova](https://skillsnova.sg/#bonus). The older component files elsewhere in this repository are not necessarily byte-identical to the reader downloads.

- [Boardroom source](BOARDROOM.md)
- [Examples](EXAMPLES.md)
- [Accuracy behaviour tests](CI-ACCURACY-TESTS.md)
- [Outcome tests](CI-OUTCOME-TESTS.md)
- [Load and validation reference](CI-LOAD-MANIFEST.md)
- [Earlier installation reference](INSTALL.md)
- [Kernel component history](https://github.com/andrewtanci/ci-perpetual-kernel)
- [Paid boundary](PAID-BOUNDARY.md)

These diagnostic tests are not a guarantee of reliability or proof of superiority. If you report a failure case, remove private, personal, client, employee, confidential and commercially sensitive information.

## 中文说明

Continuation Intelligence 整合了 Kernel 连续性指令与 Boardroom 决策支持指令，无需分别安装，也无需先完成书中章节。

请先看[快速开始](START-HERE.md)，下载同一套 CI；也可从 [SkillsNova](https://skillsnova.sg/#bonus) 查看公开下载说明。技术 Skill 名称为 `ci-boardroom`。请确认 AI 能读取完整内容。需要转到新聊天时，输入 `full migrate`，等待生成结果，审核后复制到新聊天。重要检查点需要由你保存，并在需要时再次提供。最终决定权始终属于用户或指定的人类负责人。

## Continuation Intelligence book

The book provides the wider method and background. You can start using Continuation Intelligence directly.

- [Continuation Intelligence on Amazon](https://amazon.com/dp/B0H4CVNZPH)
- [Continuation Intelligence on Amazon](https://amazon.com/dp/B0H4CXR3HJ)

## Support the project

If Continuation Intelligence helps you, star this repository so more people can find it.

## Licence

The project is released under the [MIT License](LICENSE).

## Attribution

Boardroom Cards generated with the Boardroom method carry this footer:

“Generated with CI Boardroom · Continuation Intelligence.”
