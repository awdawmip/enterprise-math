# Verification-order correction: bounded source review

Status: **SHARED_CONTEXT_AUTHOR_CROSS_CHECK / READ_ONLY / NOT_ADMITTED**.
No scientific checker was run for this review. The parent is separately
replaying the positive fixtures and K=0 boundary under the new source.
The two previously frozen documents in this directory remain unchanged.

## Exact change and source binding

The archived source at
`aggregation/prior_validation_run/paid_aggregator.py` has SHA256
`b6aec3c6dc4732e4be2bf19ca0bcc2d52a4e7630356c96abc7be8168b23a51fe`.
The current `aggregation/paid_aggregator.py` has SHA256
`ff7cf4c32d5cd86c68a2602c4991972004762343ecff4de72e735441b1a68768`.
A read-only complete-file diff shows exactly one change in
`PaidAggregator._verify_address`, at lines 72--73: the actual target
certificate verification now runs before the inherited modular-table
verification. Neither call, result attachment, nor mathematical
contraction was removed.

The dependent `leading_zero_aggregator.py` is unchanged at SHA256
`f6597bcd54c4e9525ef142e3a661a0f30a14bc184169cf8d053005a8149cb7cb`.
The original mathematical and static reviews remain bound to their
listed earlier source hashes. This addendum binds the verification-order
change to the new source rather than retroactively changing those records.

## Failed target-certificate path

Before the change, the actual inherited-table permutation replay ran
first and returned a receipt into a local variable. If the following
target verification rejected its certificate, the local inherited
receipt had not yet been attached to the returned verification object
or to the target exception. Thus this preliminary work could be omitted
from the rejected-target evidence.

Now the target verifier runs first. All preceding wrapper operations
are source/program/history checks, type/range checks, dictionary and
schedule binding, and selection of the inherited table. They perform
no native modular replay. If target verification raises, execution
never reaches `verify_lazy_permutation(inherited)`. Consequently the
specific unreported preliminary replay identified in the cost audit
is no longer performed.

The target verifier retains its existing behavior: malformed schema
or pre-execution canonical-content failures are rejected before its
mathematical work; failed actual recovery carries its own evidence;
and a completed replay which disagrees with supplied scientific content
raises `TargetAddressError` containing that replay. Reordering the
wrapper neither strips nor replaces those target-side receipts.

## Successful path and limits

When target verification succeeds, the same inherited-table replay
still runs and its receipt is immediately attached as
`inherited_permutation_replay`. Completed membership is still required
before the query count is incremented and the verification is returned.
Both MEMBER and NONMEMBER routes therefore retain their original
mathematical premises and outputs. Counted suffix matrices, signs,
residuals, period reduction and denominator scaling are unaffected.

Native process-cache call deltas and source bindings can change when
the calls are reordered. This review does not infer bit-identical
execution receipts from identical mathematical behavior; retaining
the old run and executing the new-source fixtures is appropriate.

This correction is specifically about a rejected target certificate
under the existing unchanged, valid admitted-program contract. It is
not a claim that every hypothetical exception after successful target
replay, including a separately corrupted inherited program object,
now has a universal exception-level receipt wrapper. No expansion to
hostile program mutation is needed for the present contract.

Conclusion: the two-line reordering fixes the identified failed-target
receipt omission without changing the proved aggregation formulas or
the successful verification obligations. No additional substantive
defect was found in this bounded diff review.
