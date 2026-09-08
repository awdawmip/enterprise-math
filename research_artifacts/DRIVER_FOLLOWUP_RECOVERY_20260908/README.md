# PFSSV Driver review and same-task revision recovery

The existing frozen PFSSV return is preserved. Driver review `DR-FDDA90E2280E08CA5A35` requests revision; the original broad hard-target closure is not accepted. The existing review was successfully continued through the canonical materializer at 2026-09-08T09:52:25.354611+00:00, creating generation 2 `TP2-2029B5CCC5EEC5F0132C` and packet `DFU-19973107B48580C086E7`. The actual command exited zero in 41.3588077 seconds. No new claim, session, research execution, or mathematical acceptance is asserted.

The review identifies three concrete defects: null support drops geometrically eligible zero-count positions, the labelled prime-rank coordinate is a surviving-row index, and full corrected cross-scale profiles are missing. The independent check covers two already exposed discovery cells at X=100000, reproducing 237 and 25 raw pairs. It is neither a fresh blind experiment nor a reconstruction of the full original study. The same-task revision preserves the original hard target, scales, widths, native progressive-plane interpretation and all eight output obligations.

## Actual transaction history

- The first review write was rolled back after a historical raw audit failure; the Result writer repair is already merged in PR #1407.
- The next review command persisted the single genuine DR, then exited nonzero because Windows CRLF preparation failed the LF taskbook parser. `review_attempt2_receipt.json` records that boundary; it is not a successful followup receipt.
- The first followup recovery passed preparation and produced candidate files, then exited nonzero because the old transaction used a global raw audit containing 39 historical packet faults and nine other pending review registrations. All three candidate files were removed. `recovery_attempt1_failed.json` preserves the actual failed command and raw-output hashes.
- After the candidate transaction fix, the second recovery reused the existing DR and completed. `recovery_attempt2_success.json` binds the successful command, raw stdout hash, complete returned packet and actual persisted paths. `persisted_bindings.json` records their exact bytes. Deterministic publication and packet IDs do not include timestamps, so this successful attempt reused the rolled-back candidate IDs with new timestamped bytes. An ID alone is not evidence of success.

## Control changes and validation

Taskbook preparation freezes the LF text already validated by the canonical preparer. The authority-map loop uses the existing bounded read snapshot, ending before writes. Each materialization fully validates its own candidate before and after packet persistence, checks raw review/packet identity uniqueness, runs the current CI isolation chain, and requires every file it created to retain the frozen bytes. Rollback refuses to remove externally modified files. The first-review facade relies on successful canonical materialization instead of subsequently failing on unrelated pending work.

Public and raw audits remain unchanged diagnostic interfaces. The 39 historical packet faults were not newly quarantined, and the nine pending registrations were not declared complete. This change does not claim a globally clean raw store.

The author ran 20 focused tests, including 14 fresh-process transactions using actual bootstrap, builders, validators and the current isolation chain. Root ran 52 composed tests in 37.787 seconds, all passing. Negative cases cover candidate-source mismatch, duplicates, taskbook/TP2/DFU byte drift, coordinated drift, missing Result, a second review, reopened parent Objective and exact-isolation drift. Earlier 38-test and newline receipts remain as historical stages; the final 52-test receipt is `candidate_composition_tests.json`. The independent reviewer checked the frozen source, prior newline implementation and actual logs without repeating materialization.

Publication and main-merge evidence are separate from these local transaction receipts. The next scientific frontier is the generation-2 taskbook. Use current canonical claim and runtime authorization before executing it.
