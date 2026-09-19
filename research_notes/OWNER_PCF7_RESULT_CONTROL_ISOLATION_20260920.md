# Exact PCF7 Result control-authority isolation

Classification: `NO_NEW_MATHEMATICS / CONTROL_PLANE_MAINTENANCE`.
Base: `fdd604f4686649f1374aa2b9568f05867d6f5bee`.

An ordinary UR review transaction passed its own candidate checks and rolled
back during the global post-check because another frozen Result and review
failed strict integrity checks. The affected objects are
`RR-F97259D79B7E7EF3F69F` and `DR-027ED0C06D7B6A76E0FF`.

The Result has four exact raw errors: unknown execution record, invalid
method_harvest, invalid independence_status and invalid source_exposure_status.
Its declared execution payload already exists at the flat path
`research_execution_records/ER-E90FEF513B0AEE96C73E.json`, with the exact bytes
bound by the frozen manifest. The canonical iterator intentionally reads only
task subdirectories, so this historical payload is not a canonical execution
identity. The review's current report differs from both declared artifact
digests; its Result-record binding itself still matches.

## Narrow containment

The existing Result-authority isolation gains one constrained evidence basis:
`BOUND_FROZEN_RESULT_FLAT_EXECUTION_RECORD`. It accepts only the fixed flat
execution path for the stated ID, matching schema/identity/Result relation
fields, and exactly one frozen-manifest entry containing both original byte
digests. The canonical execution map must still lack that ID. The payload is
not copied, indexed, aliased, authorized or assigned a new claim.

The complete raw strict error set remains distinct from diagnostics evaluated
against the historical payload. Both sets, the Result/publication and all ten
dependency files are pinned. A changed dependency, missing manifest entry,
added canonical alias or changed error set invalidates this containment.

One Result-authority row withholds this exact Result and its derived review.
One existing invalid-review audit row contains the separate artifact-digest
fault. The existing cause-composition layer combines these causes. No new
review, Result, task, execution identity or mathematical decision is created.
All ten original dependency files remain byte-identical. The original
`ACCEPTED` declaration is retained as history, not repaired or reinterpreted.
The held task state remains nonterminal and requires control recovery; no
Working Truth, Foundation, successor or promotion permission is granted.

## Verification

- The five new regression tests cover non-indexing/nonterminal state, rejection
  of a new canonical alias, missing/duplicate/two-digest manifest defects,
  fixed-path/identity restrictions and distinct complete error sets.
- Forty related Result/review/guard tests and forty-three follow-up cause,
  exact-source-set and candidate-transaction tests passed.
- The complete current result/review integrity audit passed after containment.
- A separate bounded technical check by EM-DVR-57CCCE found no new issue and
  independently confirmed all ten original dependency byte pairs. Its receipt
  is retained at
  `research_artifacts/PCF7_RESULT_CONTROL_ISOLATION_20260920/technical_review.json`.
  This was a technical control check, not a mathematical review.
- No PCF7 mathematical checker, proof or computation was rerun for this change.

An initial test command named two nonexistent test modules; that invocation
reported import errors. The actual applicable modules above were then located
and executed successfully. No passing result is claimed for the bad command.

## Recovery boundary

The original PCF7 owner/authorized reviewer must resolve its own execution
record layout, metadata and report binding through the ordinary current-source
protocol. This containment does not provide that mathematical or execution
authority. Unrelated valid writers can proceed after consuming the actual
published control change and refreshing their own Result write bindings.
