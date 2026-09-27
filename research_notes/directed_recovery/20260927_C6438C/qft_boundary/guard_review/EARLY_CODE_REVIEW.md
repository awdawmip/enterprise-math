# Boundary-entry guard: early shared-context review

Status: `SHARED_CONTEXT_STATIC_REVIEW / NOT_FORMAL_ADMISSION`. This review read the complete new `boundary_execution/boundary_uniform.py` at SHA-256 `875133020ba713af755d19b121f416938193835c3e2c9b7e6ab228c19b814c83`, the initial `check_boundary_precheck.py`, frozen Uniform `755d398a19881508112c9e360c94bf10133681af8d3cbdbb103accdecc306e28`, WordCertificateBank `c3e8156b5c7573778cd1e781f23e82394c83842a9f4655b59c9659035dc62ce3`, and the inherited adaptive transaction/Gram call paths. It performed no scientific execution and inspected no new result that had not yet been produced. The present file preserves the initial findings; subsequent corrections and executed evidence belong in a separate final review.

## Two actionable initial findings

1. The precheck constructs a program with the exact-six codec, so its phase objects are frozen `RestrictedNativeWord` dataclasses. The initial `word` and `column` mutations directly assign to these objects before the guarded invocation. They therefore raise `FrozenInstanceError` before the intended public rejection check. A temporary replacement phase object with one changed field, followed by restoration of the original dictionary entry, can exercise the intended boundary without modifying the frozen class.

2. The initial evidence-capture sites retain mutable lists from inherited evidence. In particular, `target_state_after_rejections=target.evidence()` precedes another `target.advance`, and `failed_attempt=interrupted.evidence()` precedes a successful retry. Inherited `certificates`, `interruption_events` and `observer_operations` are live lists, while cursor/report fields are snapshots. Later serialization can thus combine an old cursor/count with newer list contents. The complete captured object must be detached at such capture points, or the new public evidence method must explicitly return a detached result. The new guard diagnostics alone already use `deepcopy`; that does not detach the rest of the inherited payload.

Both findings were sent immediately to the root and implementation owner. Neither finding changes the frozen Uniform scientific recurrence. No source was edited by this reviewer.

## Core call-path assessment

The eight explicit public entry points are `gamma`, `mass`, `probabilities`, `advance`, `prepare_next`, `cursor`, `evidence`, and `report`. Their common context manager performs one complete certificate-bank binding check at an outermost call, then retains `AdaptiveFeedbackGram._check` inside recursive computation. The latter still checks the complete admitted program snapshot, committed-bit ledger and pending-history consistency. The override deliberately bypasses only Uniform's repeated full bank check; no gate action, defect rule, probability expression or charge decision is replaced.

The context manager encloses the outer full check and wrapped method in `try/finally`. Ordinary errors, rejected preconditions and `BaseException` subclasses unwind guard depth and clear the owner at an outer exit. Recursive public invocations retain the same owner and do not repeat the expensive bank check. Constructor admission still pays the frozen parent's one check. The certificate-bank class and its immutable identity are additionally checked at outer boundaries.

The inherited classmethod restoration constructs this subclass, pays either cold admission or checked in-process reuse, replays committed public operations, and strictly compares the complete new cursor. Policy/schema/source/guard fields intentionally distinguish this stage from old Uniform cursors. Failure evidence is requested after a failed public operation has unwound. Restoration does not recover a random tape or previous query cache, and the selected-bit retry guarantee comes from the existing ordinary-exception transaction.

## Boundaries and accounting

- Guard-depth cleanup for `BaseException` is not a guarantee of full ledger rollback after arbitrary `KeyboardInterrupt` or `SystemExit`. The inherited adaptive `advance` transaction catches `Exception`. Its documented query-budget interruptions are covered; stronger process interruption atomicity is not added by this wrapper.
- Trusted synchronous objects and no external mutation during an outer call are necessary assumptions. The owner check is a misuse diagnostic, not a thread lock or a proof that every simultaneous race is rejected before arithmetic. Arbitrary Python monkeypatching and private-field tampering are outside scope.
- `outer_entries` includes rejected outer invocations. `bank_check_attempts` counts calls that actually reach `WordCertificateBank.check`; snapshot or type failures can occur before that increment. `bank_check_successes` counts only successful checks. Nested exception events may describe the same propagated exception at several depths and are not independent scientific attempts.
- `report` and `evidence` are themselves guarded public work. Calling them changes host guard counters. Their added diagnostic block is captured after that method's context exits; an internally nested report can correctly show an active parent depth. Top-level diagnostics should show depth zero.
- The optimization still compares the adaptive program snapshot/ledger internally and performs full metadata checks once per outer entry. Reduced repeated serialization is a host-cost improvement to test; it does not reduce a mathematical Gram-query bound, prove a faster sampler asymptotically, or eliminate full native-word certificate setup.

Subject to the two evidence/checker fixes above and these stated boundaries, this static review found no additional scientific call-path defect in the initial wrapper. Actual finite-prefix equivalence, interruption recovery, complete-law equality and measured costs remain execution claims to be checked against the produced raw evidence.

Global-Knowledge-Sync: main@a462f7a7 / GLOBAL_KNOWLEDGE_V1
