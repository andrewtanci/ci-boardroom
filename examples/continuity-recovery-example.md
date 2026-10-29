# Fictional workshop: save, load and recover

This example is fictional. All names and dates here are test fixtures, not real
people, plans, commitments or evidence of a successful assistant run.

## Source card

Maya is preparing a draft agenda for a beginner workshop called **Paper Lantern**.
The approved design limit is **90 minutes**, with **12 participants**. The venue
is **unknown**. The human decision-owner is **Maya**. AI may draft and revise the
agenda; sending invitations, booking a venue and approving spending remain
outside the authorized scope. Keep the participant count and duration fixed.

## Work prompt

> Use CI to draft a practical beginner workshop agenda for Paper Lantern. The
> total must fit 90 minutes for 12 participants. Maya owns final approval. The
> venue is unknown. Draft only; do not send, book or spend. Then prepare a full
> migrate checkpoint using only these facts. Mark proposed agenda details as
> proposals rather than approved decisions.

## Reviewed checkpoint fixture

This hand-authored fixture makes the expected fields explicit. It is not a model
transcript. Save just this block as `checkpoint.md` for the local recovery drill.

```text
CI CONTINUATION BLOCK
Checkpoint ID: fictional-paper-lantern-v1
Saved at: 2026-10-29 00:00 UTC (fictional fixture)
CI package version: 1.3.0-rc.1
Review status: hand-authored fictional test fixture; not a real approval

1. User identity needed for this work: Maya, fictional workshop owner.
2. Current primary objective: Draft a beginner workshop agenda for Paper Lantern.
3. Project or workstream: Paper Lantern workshop.
4. Recent session summary: Source card supplied; agenda remains a proposal.
5. Locked decisions with human approval status and scope: Fictional source card fixes 90 minutes and 12 participants; no external action authorized.
6. Locked terms and definitions: Paper Lantern is the workshop name.
7. Constraints and boundaries: 90 minutes; 12 participants; beginner audience; draft only.
8. Rejected or superseded directions and reasons: No superseded decisions supplied.
9. Current working state and exact artifact versions: Source card in examples/continuity-recovery-example.md; checkpoint.md v1; agenda not approved.
10. Open decisions: Agenda details and venue remain open.
11. Assumptions and uncertainties: Venue unknown; no budget supplied.
12. Evidence and source base with dates or file references: Fictional source card above, fixture dated 2026-10-29.
13. Human authority boundary and approvals still required: Maya owns final approval; AI may draft only; no sending, booking or spending.
14. Next exact step: Propose a 90-minute agenda for Maya to review.
15. Risks and watchouts: A 120-minute draft would conflict with the source card.
16. Lineage core of relevant older decisions: No earlier history supplied.
17. Most recent session update: Checkpoint fixture prepared; no invitations sent.
18. Continuity instruction for the next AI: Verify objective, version, duration, participants, owner, unknown venue and drafting-only scope; surface conflicts and wait for confirmation.
END CI CONTINUATION BLOCK
```

## Bad edit and expected recovery

In a separate test copy, change only field 7 from `90 minutes` to `120 minutes`.
That conflicts with the source card and field 5. Verify that the file's hash and
diff change. Preserve the bad copy, restore the known-good checkpoint using the
[recovery guide](../CONTINUITY-RECOVERY.md), then reload it and the unchanged source
card in a fresh chat. Check that the proposed agenda fits 90 minutes and retains
the 12-person limit, Maya's ownership, unknown venue and drafting-only scope.

For a real two-assistant trial, retain each setup's actual response and failures.
No assistant response or cross-client compatibility result is asserted here.
