# Cross-conversation continuation: deployment handoff

Status: ARCHITECTURE_CANONICAL_AND_MCP_READS_LIVE; PRODUCTION_WRITE_ACCEPTANCE_BLOCKED.

The canonical architecture was merged by PR1496 at ea8aefb33725fe7bf711dca4007b14fe323c274d. Use docs/CONTINUE_RESEARCH.zh-CN.md (English pair available). Durable tasks, original evidence, frozen publications and contribution history survive replacement of the execution conversation; the original private agent is not a required contact.

The companion MCP0.5.1 is deployed with31 tools. Real RB, T6 and JT2 packets return COMPLETE, AWAITING_REVIEW and NEEDS_DISPATCH. T6 Result pagination verifies exact bytes. The live inventory contains289 tasks; its second page reuses the same source/events/time snapshot and returns in0.623 seconds. A real343-path cold update materializes all7574 files in83.145 seconds, with every target Git blob verified and the prior snapshot unchanged.

Core187 tests plus84 subtests pass; the full isolated native A-to-B/Result/Driver/GOV lifecycle passes. The final bounded adapter suite passes74 tests, with5 already separately validated opt-in fixtures intentionally skipped. These are control tests, not mathematical acceptance. Sixteen frozen legacy branch returns still require the explicit original-byte intake protocol before native review.

The remaining operational gate is external GitHub credential authorization: the server's first real POST to Git blob creation returned403. Reads and authentication succeed, but the current fine-grained credential cannot perform that operation. No Source session, RA, DA or CLAIM was created by this canary. Its unregistered local capability has been explicitly retired while preserving the failed job and journal.

The credential owner must confirm that the server credential covers awdawmip/enterprise-math with Contents and Issues read/write. Do not send token plaintext into chat or GitHub. Once corrected, a new authorized conversation should run the prepared empty-session/Driver lifecycle acceptance, verify Source publication/readback and close every own canary. Do not reuse the revoked failed issuance or repeat completed research. Do not declare production MCP writes fully verified until that actual test succeeds.

No mathematical research was resumed. The prior research stop remains in effect; this architecture maintenance does not create an unattended executor or a new two-hour research window. The complete sanitized operational receipts and exact local recovery state are retained in the authenticated companion MCP workspace/repository.
