# Legacy local CFD handoff snapshot

This directory preserves the complete 25-file local bundle created before GitHub write capability was available in that session. The original ZIP is stored losslessly as four ordered Base64 parts; `ARCHIVE_REASSEMBLY.json` gives the exact archive SHA256 and reconstruction rule. Statements inside the historical bundle such as `DRAFT_NOT_PUBLISHED`, missing write capability, or missing task registration describe that bundle's observation time, not current state.

Current task mapping is in `CURRENT_MAPPING.json`. Eight CFD tasks were already published before this recovery; the ninth prior-art task is published by the same transaction that adds this archive, with task id `RS-CFD-PRIOR-ART-AUDIT-20260910` and publication id `TP2-ABB0F0E69389742569BF`. The existing main-task claim and later trajectory checkpoint are preserved and not replayed.
