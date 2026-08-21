# R022 Fourth-Pass Deepening — Structured Exact Fast Paths and Certificate Reuse Depth

**Researcher-ID:** `EM-R022-HC7B4A`  
**Task:** `RS-R022-HASHCLASH-BRC-TOOL-MINING`  
**Taskbook base:** `89fb6c99fa2a00e42f58c1fc11ea016b7421f3be`  
**Owner PR:** `#497`  
**Status:** `FOURTH_PASS / RESEARCH ADDENDUM / NOT CANONICAL`

## Executive result

The third pass showed that unrestricted exact Residual Join Basis (RJB) minimization already contains Set Cover.

The fourth pass asks the constructive follow-up: **what source-shaped structure makes exact BRC normalization cheap again?**

Two useful regimes survive.

1. **Laminar residual-support dictionaries** admit a closed-form unweighted exact basis: one representative of every inclusion-maximal nonempty residual signature. Exhaustive enumeration checked all **831** nonempty laminar set families on a four-element universe with no counterexample.
2. **Cumulative dependency footprints** induce a nested certificate-validity refinement tree. For two contexts, the deepest equal footprint defines an exact **Certificate Reuse Depth (CRD)**: cached prefix certificates no deeper than CRD remain reusable; deeper certificates must be invalidated.

The second mechanism is directly source-shaped by HashClash's `bequal` plus masked prefix reuse. The first is a general RJB fast path and should not be attributed to HashClash unless a concrete residual-support family is proved laminar.

A required kill test shows that if dependency footprints are not cumulative/refining, the validity partitions can cross and no prefix/refinement-tree cache theorem follows.

Recommended fourth-pass classification:

`BRC_STRUCTURED_FAST_PATHS_FOUND / LAMINAR_RJB_EXACT / CERTIFICATE_REUSE_DEPTH_CLASSIFIED / NONCUMULATIVE_FOOTPRINT_KILL / NOT_CANONICAL`.

## 1. Two different geometries

The RJB hardness result is worst-case. Exact BRC can still be cheap under structure.

R022 now separates:

### Residual-output overlap geometry

Objects are `phi(b) subseteq U x Y`. This controls collective dominance and RJB minimization. Arbitrary overlap yields Set-Cover hardness.

### Certificate-validity geometry

Objects are sets of branch/context instances on which a cached certificate remains valid. This controls reuse/invalidation. Prefix/cumulative footprints can make these regions nested even when residual-output supports are not.

The two geometries need not have the same structure.

## 2. Laminar RJB theorem

Let `F` be a finite family of nonempty residual-support signatures, viewed as subsets of the finite atom universe `U x Y`.

Assume `F` is laminar: for every `A,B in F`, either `A subseteq B`, `B subseteq A`, or `A intersect B = empty`.

Let target `z = union F`, and let `M` be the inclusion-maximal distinct signatures in `F`.

### Laminar Maximum-Signature Basis Theorem

`M` is a minimum-cardinality exact existing-token RJB for `z`.

Moreover every minimum-cardinality basis contains one token with each maximal signature, so the minimum is unique up to duplicate tokens carrying identical maximal signatures.

### Proof

Distinct maximal laminar sets are disjoint. Their union is `z`, so choosing one representative of each maximal signature gives an exact basis of size `|M|`.

Any exact cover of `z` must cover every maximal component. Any selected set intersecting a maximal component is, by laminarity, either inside it or contains it. Strict containment of the maximal component is impossible by maximality. Covering the entire maximal component with a single selected token therefore requires an equal maximal signature; otherwise at least two proper subsets are needed. Thus every cover has cardinality at least `|M|`.

## 3. Exhaustive finite verification

Artifact: `experiments/r022_structured_certificate_fastpaths.py`.

The oracle enumerates every nonempty subfamily of the nonempty subsets of a four-element universe and filters to laminar families.

Observed:

- laminar families tested: **831**;
- counterexamples to `minimum cover size = number of inclusion-maximal sets`: **0**.

This is bounded executable evidence, not the proof.

Focused fourth-pass tests: **4/4 PASS**.

## 4. Immediate regimes

- **Chain:** totally nested residual signatures give exact existing-token RJB width 1; keep a maximum signature.
- **Laminar forest:** width equals the number of inclusion-maximal components.
- **Disjoint family:** every nonempty signature is maximal; no support redundancy exists.
- **Arbitrary overlap:** general RJB returns to Set-Cover-hard optimization.

So the structural spectrum is:

`chain -> maximal compression`

`laminar forest -> one token per maximal component`

`disjoint -> no compression`

`arbitrary overlap -> hard covering problem`.

## 5. Normalizer fast path

Recommended `residual_join_normalizer` dispatch:

1. remove bottom signatures;
2. hash-cons equal signatures;
3. pairwise dominance;
4. detect laminarity of the remaining explicit signatures;
5. if laminar, return inclusion-maximal signatures as a proved minimum unweighted basis;
6. otherwise enter bounded collective/RJB optimization;
7. if exact optimization exceeds budget, use `REPLAY_EXACT` or explicitly `HEURISTIC`.

Weighted token costs are not covered by the simple maximal-signature theorem; they require a separate optimization, naturally dynamic-programming-shaped on the laminar containment forest. R022 does not claim or implement a weighted theorem in this pass.

## 6. Cumulative dependency footprints

Let `delta_b(x,kappa)` be the complete dependency footprint needed to justify a certificate through depth `b`.

Call the footprint family cumulative when there exists a projection `rho_b` such that

`delta_b = rho_b o delta_{b+1}`.

Equivalently, equality at depth `b+1` implies equality at depth `b`.

### Refinement theorem

Under cumulative footprints, the equality partition induced by `delta_{b+1}` refines the equality partition induced by `delta_b`.

Therefore certificate validity classes across increasing depth form a nested refinement hierarchy. A deeper class belongs to exactly one shallower parent class.

This is the formal structure required for a prefix/trie certificate cache.

## 7. Certificate Reuse Depth (CRD)

For old and new contexts `kappa,lambda`, define `CRD(kappa,lambda)` as the largest depth for which cumulative dependency footprints remain equal.

In literal prefix models this is common-prefix length.

### Reuse theorem schema

Assume a certificate at depth `d` depends only on `delta_d`.

If `d <= CRD(kappa,lambda)`, the cached certificate remains valid after replacing `kappa` by `lambda`.

If `d > CRD(kappa,lambda)`, validity is not justified by the old footprint and the certificate must be recomputed or separately re-proved.

### Synthetic witness

Old context: `0 1 1 0 1 0`.

New context: `0 1 1 1 1 0`.

CRD = **3**.

Certificates at depths 1 and 3 are reusable; certificates at depths 4 and 5 are invalidated.

## 8. Relation to HashClash

HashClash `md5_connect` uses previous/new upper-path equality depth `bequal`, cached failure depth `isgood[i]`, masked `dFt/dFtp1/dFtp2/dFtp3` prefixes, and `lastdFp1/2/3` dependency participation.

R022's CRD abstraction extracts the reusable pattern:

`compute deepest still-equal sufficient dependency footprint -> reuse certificates only inside that validity depth -> invalidate the rest`.

This is stronger than merely saying "memoize failed branches".

R022 does **not** prove that every actual HashClash dependency mask across all connector states is one globally laminar family. The source supports a prefix-sensitive reuse pattern; the general refinement-tree theorem requires the stated cumulative-footprint condition.

## 9. Nonnested-footprint kill

Cumulativity is necessary.

Synthetic contexts: `00, 01, 10, 11`.

Suppose depth-1 footprint reads bit 0, but depth-2 footprint discards bit 0 and reads only bit 1.

Depth-1 classes are `{00,01}` and `{10,11}`.

Depth-2 classes are `{00,10}` and `{01,11}`.

The partitions cross, so depth 2 does not refine depth 1.

Therefore there is no valid refinement tree and no common-prefix-style certificate reuse theorem.

This kills any attempt to derive CRD solely from an integer depth label without proving cumulative dependency factorization.

## 10. Positive/negative certificate asymmetry

RJC algebra unifies positive and negative rewrites semantically, but their common computational structures can differ.

### Positive residual basis

Signatures overlap in outcome/future atom space. General collective optimization is Set-Cover hard. Laminar output supports give an exact fast path.

### Negative prefix cones

Validity classes live in branch/context instance space. Under cumulative footprints they form partition refinements/trie nodes. Empty-parent certificates subsume descendants.

Therefore negative certificate caching can be cheap even when positive branch-basis compression is globally hard.

**RCC/RJC optimization and CS-NCC cache management share semantic algebra but need not use the same data structure or optimizer.**

## 11. New resource quantities

R021/R014 should consider:

- `residual_overlap_class = chain | laminar | disjoint | general`;
- `laminar_maximal_count`;
- `certificate_reuse_depth`;
- `certificate_refinement_depth`;
- `certificate_invalidated_count`;
- `certificate_reused_count`;
- cost of testing/refining dependency footprints;
- cost of residual-signature overlap detection.

## 12. Tool architecture update

The candidate `residual_join_normalizer` gets a strategy ladder:

`bottom/equality -> pairwise dominance -> laminar exact fast path -> bounded collective exact solver -> replay-exact -> heuristic`.

A separate candidate `scoped_certificate_cache` should manage certificate scope, cumulative dependency footprints, CRD computation, validity reuse, selective invalidation, and provenance.

The tools should remain separate because residual-output overlap and certificate-validity refinement are different geometries.

## 13. Prior-art/rooting boundary

Nothing here is claimed as a new generic set-family or cache theorem. Roots include laminar set families, containment forests, tries/prefix trees, memoization/cache invalidation, partition refinement, and dynamic programming on tree-structured decompositions.

The Enterprise Math residue is placing those structures behind an explicit residual-support/certificate semantic contract, selecting them as exact BRC fast paths, integrating them with `EXACT / REPLAY_EXACT / HEURISTIC`, and tying CRD to selective on-demand invalidation rather than global re-refinement.

## 14. Direct R021 feedback

Add two structural fast paths after the third-pass RJC/RJB layer.

### Laminar RJB fast path

If the admissible support-signature family under the target is laminar, choose one representative per inclusion-maximal nonempty signature. This is an exact minimum-cardinality existing-token basis; skip general RJB/Set-Cover search.

### Certificate Reuse Depth

If dependency footprints are cumulative, cache validity classes as a refinement tree, define `CRD(old_context,new_context)`, reuse certificates at depth `d <= CRD`, and invalidate deeper certificates only.

Do not enable either fast path without its structural precondition.

## 15. Fourth-pass classification

`BRC_STRUCTURED_FAST_PATHS_FOUND / LAMINAR_RJB_EXACT / CERTIFICATE_REUSE_DEPTH_CLASSIFIED / NONCUMULATIVE_FOOTPRINT_KILL / R021_FEEDBACK_READY / NOT_CANONICAL`

Cumulative picture after four passes:

1. source mechanisms are not a new generic search algorithm;
2. BRC has an exact support-semantic certificate algebra;
3. optimal general branch-basis compression is hard;
4. source-shaped structural subclasses recover cheap exact normalization and selective certificate reuse.
