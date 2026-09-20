# Cross-conversation architecture rebuild checkpoint

Status: IN_PROGRESS / NONOPERATIONAL_DESIGN_AND_VALIDATION_CHECKPOINT.
User instruction: repair the research state machine after the old Drivers/researchers disappeared, take responsibility for MCP, and make tasks continuable from any new authorized conversation.
Classification: CONTROL_PLANE_MAINTENANCE; no new mathematical research, acceptance or promotion.

The current implementation base is main369fcbce4a644c6b7b199b1e8bb7ceaa9825d4ed, tree51e9be6017e5e8997db436d6460cf91cbf86f1dd. All7,478 files/140,422,552 bytes were verified against their Git blobs; the real commit/tree were materialized locally with a shallow boundary. The fresh Issue240 stream contains858 raw server envelopes. GK read snapshot0d088c584ca0e862f24aca7ada9e6ab0fb7a1265 was established by the shipped sync helper.

Implemented candidate direction:
- Existing immutable Task/publication remains durable; execution identities and sessions are replaceable.
- Upgrade the existing succession policy to authenticated typed CLAIM continuation with exact predecessor CAS and one current writer. Preserve old claim bytes; fence old writes.
- Distinct Driver DA succession and current-session write authority, preserving historical review validity and author/exposure semantics.
- Prospective payload-bound RR/DR write authorization; exact legacy cutover records retain all original audits.
- MCP-native real execution-session/identity/RA registration, independent DA activation, fixed artifact readback, Source checkpoint/return/review writers, lifecycle close and client-scoped capability keys.
- Separate control-main version from fixed branch evidence; a dirty worktree cannot be advertised as immutable source.
- New default sessions require only MCP, without private predecessor contact or an additional GitHub connector. No arbitrary shell, automatic mathematics or Foundation grant is introduced.

Actual validation milestones at this checkpoint:
- Candidate EM focused regressions:69 tests plus6 subtests passed, including existing architecture/FREE/identity guards.
- Pure current-main Result/review audit of the exact T6 legacy return intake passed;35 old branch files and28 frozen output pins verified. Original actual RR blob62e50de0541fcb25492cffd9354afa8d3a3cda52 retained; T6/global target remains OPEN and awaiting independent review.
- The real isolated native Research flow ran A-to-B takeover, checkpoint, fixed native freeze, fresh Driver review and native followup successfully. It used synthetic control fixtures, not GitHub writes or mathematical acceptance.
- Candidate whole inventory retains289 tasks with103 NEEDS_DISPATCH,53 AWAITING_REVIEW,25 BLOCKED,20 DORMANT and88 COMPLETE.
- Independent review found and drove fixes for caller-forged stale timestamps, session-key recovery via a shared public request ID, unbound legacy-session enrollment and mixed-commit artifact pins.
- MCP-specific coverage was56 passing tests before the final gateway additions; the complete expanded suite is still being verified.

Pending work remains material: final GOV/native writer gateway integration; actual API/session lifecycle and Source CAS reconciliation tests; finishing asynchronous inventory pagination; fresh-main/cutover reconciliation; complete current-code pin review; canonical publication and live MCP deployment/acceptance. The candidate is not deployed and this checkpoint does not announce completion.

Local recovery locations:
- D:/em/TEMP/continuation-rebuild-20260920/OWNER_STATE.json
- D:/em/research-continuation-base-369f-20260920
- D:/em/research-continuation-integration-20260920
- D:/em/continuation-core-20260920
- D:/em/mcp-successor-20260920
- D:/em/mcp-successor-em-patch-20260920

The old two-hour mathematical research window remains stopped. This is a separately authorized architecture repair with no new time budget. Resume the remaining implementation/validation, preserving frozen mathematics, P000, source firewalls, history and other worktrees.
