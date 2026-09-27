# Segmented SO view: bounded source review

Status: **STATIC_SHARED_CONTEXT_REVIEW / NOT_FORMAL_ADMISSION**.
The design, complete current adapter source and relevant frozen constructor/guard/cursor chain were read. No candidate module was imported, no metadata experiment or native calculation was run, and no implementation file was changed. This is a source-specific readiness opinion; it does not assert that the planned checker or performance comparison has passed.

**No blocking implementation defect was found.** The adapter is ready for its declared bounded checks. Its exact-equivalence claim needs the fixed-admitted-bank qualification below, which is consistent with the design's stronger identity requirement.

Reviewed source: `segmented_so_view.py`, SHA-256 `90c773c74a81ed239e32fcc12fa8d238032d6fbcfef3f4d6eb2056856666ed99`. The design read for this review had SHA-256 `c7b25bb6f17d76143a1fe9e5980c8e2560a3498e97de899e22255f2e4f6cf2d2`. These source hashes were supplied by the implementation author after source-only hashing. The checker is still being completed and is not included in this readiness opinion.

## Representation and admission

The candidate still invokes the frozen `_program_view`, retaining complete native-word fields, forward/inverse columns, sparse caches, codec and phase metadata. The fast comparison uses three separate immutable byte strings. It does not substitute Python numeric equality or a hash for complete-byte equality, so the old JSON distinctions between integers, booleans and floats are preserved.

The expected token is derived only after the inherited constructor has invoked the exact `SOTraceBank.check`. Its source is the admitted bank's immutable `_view_bytes`, decoded once and required to reproduce the same canonical wrapper bytes. Neither a caller-supplied token nor a current unchecked program view can authorize it. The bank's actual records and scalar norm bounds remain unchanged.

Under the pinned encoder semantics, equality of all three segments implies equality of the frozen complete wrapper. On a mismatch the adapter invokes the exact class method `SOTraceBank.check` and accepts only its successful return. The token is never updated after a compatibility acceptance. This handles the design's noncanonical integer-key normalization case without progressively changing the trusted baseline. Raw-view or JSON-encoding errors reject; there is no permissive exception fallback.

The equivalence is the **program-view acceptance relation with the originally admitted bank fixed, after that bank passes the token's canonical-wrapper gate**. In particular, `_derive_token` checks `metadata_bytes(decoded) == bank._view_bytes`. Without this gate, decoding and reencoding `native_fields` could normalize a noncanonical frozen wrapper; segment equality would then identify the normalized wrapper rather than prove equality to the original admitted bytes. The gate prevents such a fast-path acceptance. Ordinary actual native rows contain tuple/list/primitive values, and admitted phase/codec metadata is already normalized; those expected inputs satisfy the gate. This static argument is not a claim that every possible legacy wrapper satisfies it.

The new constructor therefore has a stricter admitted-wrapper domain. The adapter also requires `word_certificates is original_bank`, whereas the frozen SO boundary checked exact type and binding hash and could accept a different legitimate bank instance with the same binding. Thus neither all-bank construction nor the entire mutable-object API is claimed equivalent. Both restrictions are intentional token binding, not reasons to weaken the check. The reviewed design's section 4 did not yet explicitly state the new canonical gate in its construction recipe and equivalence domain; root and the implementation author were notified to clarify it before final publication. This is a documentation qualification, not a blocking code defect.

## Construction, guards and exceptions

The inspected constructor chain is `SegmentedBoundarySOTrace -> BoundaryCheckedSOTrace -> SOTraceUniformFeedbackGram -> AdaptiveFeedbackGram -> GramSampler`. The boundary sets its depth/owner/statistics before entering that chain. The constructors do not dynamically enter one of the eight guarded public methods before the new token and view counters exist. The SO constructor performs its bank check directly. The new adapter derives its token only after that admission finishes and its own source identity is set.

Six methods inherit their existing single public-entry wrapper: gamma, mass, probabilities, advance, prepare_next and report. The cursor and evidence overrides each have one new wrapper and explicitly invoke the undecorated SO policy implementation, avoiding a duplicate outer wrapper. Calls back through `self.cursor`, `self.report`, `self.mass` and recursive `self.gamma` retain the existing nested topology. Every outer entry uses the new complete view check; internal `_check` calls continue to perform the frozen Adaptive phase snapshot and committed-ledger checks.

The frozen owner/depth context manager is reused, including its `finally` path and exception diagnostics. Token or bank rejection occurs before the method body can propagate native state. This preserves the existing synchronous trusted-object scope. It does not promise thread-safe concurrent mutation, protection against hostile private-field or method replacement, or full transaction rollback for every `BaseException`. The inherited advance transaction catches `Exception`; guard-depth unwinding alone must not be described as a new KeyboardInterrupt ledger guarantee.

## Cursor, evidence and counters

The cursor has a new schema/profile, actual adapter source identity, frozen parent and boundary source fields, and the token digest. The inherited strict classmethod restore constructs `cls`, admits or checks the actual bank, derives a fresh token, replays the committed bits and pending decision, and compares the entire new cursor with strict JSON bytes. It does not import an external token as authority. Old-profile cursors deliberately differ. Replay failure evidence remains the inherited behavior; constructor failures occur before its replay exception wrapper and have no new partial-evidence guarantee.

The new view statistics distinguish segmented attempts/fast accepts from compatibility checks/accepts/rejections and token/bank identity rejections. `bank_check_attempts` and the policy binding-check count are now **logical complete binding checks**, not literal invocations of the frozen bank method. Diagnostics explicitly say this and separately report constructor-plus-compatibility invocations. The constructor's one direct frozen check is correctly separate from a cold bank's full scientific admission work. Token derivation adds host work and retained bytes without removing that admission.

`raw_view_construction_failures` counts exceptions from `_program_view` only; later segment-encoding errors still reject through the outer guard but are not covered by that narrower counter. This matches the field's current source boundary and should not be called a count of every serialization failure.

The adapter's view statistics and segment sizes are detached in diagnostics. Other inherited evidence still contains live lists or receipt references; a checker that saves a snapshot and then continues execution must detach the complete evidence, as in the earlier stages. The source does not silently add a stronger evidence-immutability guarantee.

## Bounded checks still required

The declared checker should exercise an ordinary fast accept, a compatibility accept with unchanged E, a compatibility rejection, strict bool/int and float/int changes, and exact bank/token identity controls. A metadata helper check must not be described as actual admission of a fabricated bank. The new constructor and pending/terminal restoration need actual integration coverage, with same-bit budget interruption recovery and complete matrix/observer comparison to the frozen SO boundary. Unexpected failure receipts should remain separate from complete results.

No speed claim follows from this source review. Normal entries still traverse and encode the complete native fields and phase/codec metadata; the token adds persistent representation storage. The slow branch repeats work. Any timing comparison must separately account for cold admission/token construction, cache state, all native counters, evidence capture and background serialization.

Global-Knowledge-Sync: main@b98c6e4 / GLOBAL_KNOWLEDGE_V1
