# R022 Sixth-Pass Deepening — Reversible Recoalescence and Future-Language Refinement

**Researcher-ID:** `EM-R022-HC7B4A`  
**Task:** `RS-R022-HASHCLASH-BRC-TOOL-MINING`  
**Taskbook base:** `89fb6c99fa2a00e42f58c1fc11ea016b7421f3be`  
**Owner PR:** `#497`  
**Status:** `SIXTH_PASS / RESEARCH ADDENDUM / NOT CANONICAL`

## Executive result

Pass 5 separated exactness verification from basis optimality. Pass 6 asks when a support-exact recoalescence remains valid if the **future operation language changes**.

The key boundary is non-monotone/retractive future operations.

Even when the final observable remains only Boolean result support, a forgetful support merge can become inexact if the future is allowed to remove individual branch copies. Current support cannot distinguish one copy from two copies, but one future deletion can.

For `n >= 0` identical residual branch copies, Boolean observable `q(n)=1[n>0]`, and future language containing up to `h` anonymous `delete-one` operations, the unique coarsest pointwise future-exact token (up to relabeling) is

`tau_h(n) = min(n, h+1)`.

Thus the horizon-`h` future has exactly `h+2` semantic classes:

`0,1,...,h, >=h+1`.

When the horizon extends from `h` to `H>h`, every old nonsaturated class remains unchanged; only the old saturated class `n>=h+1` must split into `h+1, h+2, ..., H, >=H+1`.

If the old execution discarded the underlying count/checkpoint, this split cannot be reconstructed. That is an exact NO_RESURRECTION witness for future-language extension.

Recommended classification:

`BRC_REVERSIBILITY_BOUNDARY_FOUND / DELETE_OPERATION_DOES_NOT_DESCEND_THROUGH_SUPPORT / BOUNDED_DELETION_TOKEN_COARSEST / SATURATED_CLASS_ON_DEMAND_REFINEMENT / REPLAY_EXACT_NECESSITY_SHARPENED / NOT_CANONICAL`.

## 1. Aggregate descent criterion

Let `E` be a runtime encoding of fine branch configurations and `F` a future operation. `F` safely descends through `E` exactly when

`E(C)=E(D) => E(F(C))=E(F(D))`

for all relevant configurations.

For copy count use `q(n)=1[n>0]`.

### Add-one

`add(n)=n+1` descends through support-only state.

### Delete-one

`del(n)=max(n-1,0)` does not.

States `n=1` and `n=2` have the same current support, but after one deletion:

`q(del(1))=0`,
`q(del(2))=1`.

This is a minimal NO_RESURRECTION witness once deletion enters the future language.

## 2. Why idempotent recoalescence can fail under retraction

For static Boolean support, `x union x = x` makes duplicate contributions idempotent. But an operation that removes one underlying copy acts on the branch configuration before final union.

Therefore observable idempotence does not imply future compositional exactness. Every declared future operation must also descend through the chosen carrier.

So `x∨x=x` is not a license to forget multiplicity under arbitrary future languages.

## 3. Bounded deletion future signature

Let the residual language contain `id, del, del^2, ..., del^h` and observe Boolean support after each word.

For copy count `n`,

`Phi_h(n) = (1[n>0], 1[n>1], ..., 1[n>h])`.

Two counts have equal future signatures iff

`min(n,h+1) = min(m,h+1)`.

Define `tau_h(n)=min(n,h+1)`.

### Deletion-Horizon Coarsest Token Theorem

For Boolean support and at most `h` anonymous deletions, `tau_h` is the unique coarsest deterministic pointwise exact encoding up to relabeling.

### Proof

If `tau_h(n)=tau_h(m)`, either both counts are the same integer `<=h`, or both are `>=h+1`. Hence all predicates `n>k`, `m>k` agree for `0<=k<=h`.

Conversely, suppose `n<m` and the tokens differ. If `n<=h`, choose `k=n`: then `n>k` is false and `m>k` true. The only remaining case would put both above `h`, which would make both tokens `h+1`, contradiction.

## 4. Stage-aware exact deletion transition

At a stage with `r>=1` deletions remaining, store

`t=tau_r(n) in {0,...,r+1}`.

After one deletion, the residual horizon is `r-1`. The exact induced transition is

`t -> max(t-1,0)`.

If `t<=r`, the count is exactly `n=t`. If `t=r+1`, then `n>=r+1`; after deletion `n'>=r`, whose next saturated token is `r=t-1`.

Executable checks verified this transition for horizons through 8 and counts through 64.

## 5. Horizon growth gives local on-demand refinement

Suppose an execution compiled for horizon `h` is later queried under horizon `H>h`.

The old partition is

`{0},{1},...,{h},{n>=h+1}`.

The new partition is

`{0},{1},...,{H},{n>=H+1}`.

All old classes `0,...,h` remain intact. Only the saturated class refines:

`{n>=h+1}` -> `{h+1},{h+2},...,{H},{n>=H+1}`.

### Saturated-Class Refinement Law

Language extension requires refinement only inside the old saturated class.

For `h=2`, `H=5`, old top token `3` refines to `3,4,5,6`, where `6` denotes `n>=6`.

## 6. NO_RESURRECTION under future-language extension

At old horizon `h=2`, counts `n=3` and `n=4` both encode as `tau_2=3`; their old future signatures agree.

Extend to horizon 3:

`tau_3(3)=3`,
`tau_3(4)=4`.

After three deletions, count 3 has support 0 while count 4 still has support 1.

An execution that retained only the old saturated token and destroyed every count/checkpoint cannot produce the exact new split. It must have stronger metadata, replay from a checkpoint/fine source, or declare the stronger query unavailable/inexact.

This makes `REPLAY_EXACT` mathematically necessary when future-language extension may demand distinctions deliberately forgotten earlier.

## 7. Reversibility metadata ladder

### Support-only

Stores only whether at least one copy exists. Exact for horizon 0 and for operations that descend through the quotient.

### Bounded deletion token

Stores `tau_h(n)`. Exact for up to `h` anonymous deletions. Metadata depends on declared horizon rather than full fine count.

### Full count

Supports arbitrary anonymous deletion sequences, but not automatically named branch provenance.

### Provenance / incidence metadata

Needed when future operations identify which branch/history is removed or source identity becomes observable.

### Replay checkpoint

Allows live execution to use a smaller forgetful token while preserving the ability to reconstruct stronger metadata on demand.

Thus BRC reversibility is future-language-relative.

## 8. Refinement direction and certificate reuse

A certificate proved for a stronger future language can be restricted to a weaker one. The reverse is not generally valid.

For `H>=h`, `tau_H` determines `tau_h`, while `tau_h` does not determine `tau_H` on its saturated class.

So semantic reuse has a direction:

`strong future-complete token -> weaker query` is safe;

`weaker token -> stronger future` may require splitting/replay.

## 9. Relation to causal rewind

Pass 2 established that an actually exact RCC for a fixed future language cannot later need semantic rewind solely because of that merge.

Pass 6 sharpens the exception: rewind/refinement may become necessary when the operation language itself becomes stronger by adding retraction/deletion. The earlier merge was exact for the old language but insufficient for the new one.

The saturated-class law identifies exactly which old class needs refinement in the bounded deletion model.

Causal refinement depth should therefore be indexed not only by execution stage but also by future-language version/strength.

## 10. Relation to HashClash

HashClash connector duplicate elimination remains a valid local feasibility/support recoalescence because downstream connector computation does not ask to selectively retract one predecessor history after duplicate residual states are identified.

The outer chosen-prefix script may backtrack to earlier near-collision stages, but it does so by retaining/reconstructing stage artifacts and rerunning work rather than asking a merged connector token to reveal a predecessor permanently forgotten.

So the source architecture naturally separates local forgetful exact recoalescence from outer replay/checkpoint-based recovery.

## 11. Tool delta

### `safe_operation_language`

Test whether each declared future operation descends through the complete runtime encoding. Do not call an operation safe merely because it preserves the current observable.

### `deletion_horizon_token`

Compile bounded anonymous retraction to `tau_h(n)=min(n,h+1)`.

### `future_language_refine`

When horizon changes `h -> H`, refine only the saturated class, using retained metadata/checkpoint.

### `replay_contract`

Record which hidden distinction is needed to rebuild a stronger token if the future language later expands.

## 12. R021 feedback

R021 should add an explicit future-operation/reversibility axis.

1. RJC/idempotent support merge is exact only relative to a future language whose operations descend through the chosen carrier.
2. Anonymous branch removal is a kill test for support-only forgetfulness.
3. For bounded anonymous deletion horizon `h`, the coarsest exact token is `min(n,h+1)`.
4. Horizon extension refines only the prior saturated class.
5. `REPLAY_EXACT` should cover not only budget eviction but also deliberate information forgetting when later future-language strengthening may require it.
6. Track future-language version/horizon, reversibility class, saturated/refinable classes, replay source/checkpoint, and operation-descent proof status.

No correction is requested to R023. Pass 6 is an execution-language specialization of its no-resurrection/future-signature semantics.

## 13. Sixth-pass classification

`BRC_REVERSIBILITY_BOUNDARY_FOUND / DELETE_OPERATION_DOES_NOT_DESCEND_THROUGH_SUPPORT / BOUNDED_DELETION_TOKEN_COARSEST / SATURATED_CLASS_ON_DEMAND_REFINEMENT / REPLAY_EXACT_NECESSITY_SHARPENED / R021_FEEDBACK_READY / NOT_CANONICAL`.

Cumulative compiler picture:

`declared future language -> complete-enough runtime carrier -> proof-carrying exact normalization -> forget only distinctions no declared future can use -> retain replay capability if future-language strengthening is allowed`.
