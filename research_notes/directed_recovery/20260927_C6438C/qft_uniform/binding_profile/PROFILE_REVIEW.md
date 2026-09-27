# Metadata profile and proposed guard placement

Status: bounded read-only shared-context review; no new scientific execution, timing run, source modification or formal independent admission. The optimization below is a next-version proposal, not part of the published sampler.

## What the profile establishes

The reviewed profile source is `profile_binding_metadata.py`, SHA-256 `32f9402b1d6611823218f2512033944597a1e239a7c50112caf2f96a731fb255`. Its recorded result is `BINDING_METADATA_PROFILE.json`, SHA-256 `a712ae4fbb888a0c4b880540af4c5f3fa175eab154ed78a8f23ab25e31eff8ac`. The input is the frozen uniform execution gzip `14456595a5ff8e7c3e67d78fe091b1aefec68be835a9674cefbd4dfba3b0b015`.

It reads the actual recorded phase/codec metadata pair, whose canonical encodings contain 235,524 and 235,745 bytes. In three trials of 200 repetitions, encoding and comparing both values took 2.742862, 2.787494 and 2.793887 seconds. Plain equality against a separately deep-copied structure took 0.133636, 0.170985 and 0.162285 seconds. The source performs only standard-library metadata loading, copying, serialization, equality and timing. It imports no scientific propagator and executes no native arithmetic.

This is relevant because `WordCertificateBank._program_view` serializes those two bindings on every bank check. The final uniform run records 12,139 successful checks on retained Uniform objects, with additional checks outside them. The microprofile thus identifies a repeatedly exercised host operation worth reducing.

It does **not** measure the entire `_program_view`, its gate/column comparisons, a sampler trajectory, or an isolated end-to-end experiment. Loading and deep-copy preparation are outside the timed loops. The serialization loop always precedes the equality loop; cache, scheduling, allocation and concurrency conditions are not controlled. Multiplying these timings by the full-run check count cannot attribute or predict the old/new checker elapsed-time difference. The full-run regression remains separately reported in `cost_review/COST_NOTE.md`.

Plain equality is a diagnostic comparator, **not a validated replacement** for strict serialization. The explicit counterexample `{'x':True} == {'x':1}` holds in Python while their canonical JSON bytes differ. This does not mean every such metadata type change alters a scientific amplitude; it means ordinary equality does not preserve exact schema/provenance identity. Serialized cursor/certificate verification must retain its strict type distinctions.

## Existing guard coverage and its limits

This review also read the frozen `phase_snapshot` in `carry_executor.py` (`f017b1fb1516e8faa97afd39d663e4eda6d21cad95f65bb2ccf5a79d7ff3b810`), `AdaptiveFeedbackGram._check` (`86263eb4a70fe53f8960aae2c1f0b8695dbca40a597b2711af90f20667ed3c45`), and the current uniform/bank sources listed in `cost_review/SOURCE_REVIEW.md`.

The inherited snapshot compares the program identity, arithmetic input/schedule fields, dimensions, codec, native gate identities, words, denominators, complete cached columns and sparse application caches. The ledger check additionally binds committed bits and the pending decision's prefix. These checks remain useful on recursive Gram queries and feedback applications.

However, this snapshot is a trusted in-process value tuple comparison. It does not include the serialized `phase_bindings`/`codec_binding` or every certificate-view statistic; Python numeric equality also does not itself give a strict external schema. It must not be described as independently preserving all certificate provenance/type requirements. The bank's complete view and serialized restore checks supply additional constraints.

Consequently, moving full checks only to `prepare_next`, `cursor` and `evidence` would leave directly callable `gamma` or `mass` paths outside those boundaries. Metadata could change between public calls without being rejected on such a query. That narrower placement is not a complete replacement contract.

## Sufficient next-version contract

A safe candidate is **one complete check at the outermost public call**, followed by the existing computational snapshot/ledger checks inside that call. Its proof requires all of the following:

1. Construction/admission still binds an actual `WordCertificateBank`, its complete word/codec view, immutable witness records, and source provenance. Cold construction/restore still pays for the required native replay; arbitrary serialized certificates are not trusted or downgraded to plain equality.
2. Every public entry that queries, changes or reports this object's state is covered: `gamma`, `mass`, `probabilities`, `advance`, `prepare_next`, `cursor`, `evidence`, and `report`. Restore must establish the same invariant before replay. Alternatively, some entries may become private only under an explicit narrower API. Underscore helpers remain private implementation boundaries.
3. On transition from reentrancy depth zero to one, perform the complete strict bank/type/provenance comparison and the inherited snapshot/ledger validation. Nested public calls and recursive `gamma` retain the inherited computational and ledger checks, but need not serialize the complete bank metadata again. Always release the depth guard in `finally`, including exceptions and budget exhaustion.
4. During one synchronous outer call, no external thread, callback or concurrent actor may mutate the program, bank, metadata or committed ledger. Ordinary trusted source code and immutable word/certificate contents are assumed, as in the existing admission contract. This is not a proof against Python monkeypatching or arbitrary hostile memory mutation. A guard shared across threads without an ownership/locking rule would not meet the premise.
5. Before a candidate certificate is applied, it is selected from the same immutable, admitted bank and remains bound to the actual omitted word/direction. Cursor binding obligations, charges and selected-word chronology are preserved. Strict serialized restore rejects mismatched bank/source/word/type claims. Budget rollback preserves the old pending decision and invalidates uncommitted cache entries exactly as before. A new implementation has new source identities; byte-identical cursors or automatic cross-version cursor acceptance are not asserted.

Under these premises, the removed nested checks would all compare the same unchanged bank view with the same admitted view. They would therefore succeed and have no scientific side effect. Induction over the nested call sequence gives the same selected words, signed Gram recurrence, observer values, cache updates, charges and commit/rollback behavior. Only metadata-work counters and timing change. Across distinct outer calls, the complete check runs again, so a persistent metadata or provenance mutation is still rejected before the next operation consumes or reports the object.

This argument does not justify weakening the serialized certificate/cursor schema, treating a non-immutable token as sufficient proof, skipping program admission, or removing the per-recursion computational/ledger guard. It also does not remove exact Gram-query complexity. The unimplemented candidate would need a bounded same-input regression with direct `gamma`/`mass` mutation controls, strict bool/int certificate controls, exception-depth reset, restore/rollback equivalence and separated cold/warm costs before claiming an actual improvement.
