# X6 Unit129 — live signed-triad midpoint repair: translation-covariant native paths

**Observed/executed:** 2026-11-18. **Mother objective:** `PO-X6-SPATIAL-FOUNDATION-CONSISTENCY-20260905`. **Task:** `RS-X6-LEGACY-PLANE-RECONCILIATION`, publication `TP2-B4A441B23DA3159232C2`. **Research lane:** `chatgpt-research-onhour-enterprise-math-20260923`. **Author status:** `AUTHOR-CURRENT-SOURCE-PATCH-EXECUTED / EXACT-INTEGER / UNREVIEWED / NOT_ADMITTED`.

## Exact source defect and repaired current consumer

Unit126 proved a source-level typing restriction: the historical `midpoint_options(a,b)` returned `(ZERO,a+b)` for every two-step native signed pair, even though that expression is only correct when both endpoints are unit neighbors of the same selected zero anchor. Unit127 then directly executed the complete actual triadic module; Unit128 made its 13 mathematical assertions always-on in all CPython modes. Its current post-Unit128 source remained incorrect for translated legal inputs outside the 480 anchored caller pairs.

This unit performed the scoped **live current-source correction** of `experiments/x6_triadic_atomic_scatter_v1_20260906/check_triadic_atomic_scatter.py`:

- Previous active Git blob: `eb2036264f5b754988a5841ca1d83fab561aa49b`, checked and used as the CAS predecessor.
- New active Git commit: `573a2560680d780ffffe5c21cbb5653d042a6b84`; **Git blob** `cf5bc031b90b26d82216925d2768583db4e10f57`, immutable remote content verified.
- Changes are restricted to the `midpoint_options` helper. It retains the two always-on original BRC guards, computes the two actual signed primitive increments of `d=b-a`, and returns their intermediate Cell addresses `a+step`. When `ZERO` is one of the two midpoints, it is ordered first so the original signed-triad branch-bit semantics are preserved.
- Original signed native `signed_brc.py` remains at exact frozen Git blob `300a96e3dc24bf6fff73743037a0347a8bc83176`, corresponding to task scientific input pin `59538f585d037d09ef687b28715c4bc1a3f9fe03`. No P000 or frozen experiment was edited.

The current source edit is a genuine executable interface repair. It preserves Unit128's 13 always-on guard changes, the original 160 signed triad inputs and the original printed report.

## Exact mathematical claim

Let `a,b ∈ Z^6` be signed X6 Cell coordinates relative to an arbitrary *selected* anchor, let `d=b-a`, and assume native signed axis path length `L(d)=sum_i |d_i|=2` and minimal N-BRC multiplicity `B_min(d)=2`. Then necessarily there are **two distinct** named axes `i<j` and signs `s_i,s_j ∈ {-1,+1}` such that `d=s_i e_i+s_j e_j`. There are exactly two shortest primitive paths, with intermediate Cells

```text
M(a,b) = {a+s_i e_i, a+s_j e_j}.
```

**Proof.** Among integer vectors of L1 norm 2, the only support patterns are `2` on one axis (BRC=1) or one unit on each of two distinct axes (BRC=2). For the latter, any shortest two-step primitive path orders these two signed increments; the first increment reaches precisely one of the displayed intermediate Cells. This also proves for every translation `t∈Z^6`:

```text
M(a+t,b+t) = M(a,b)+t.
```

The originally returned `{ZERO,a+b}` fails this translation law as a general Cell function. Under the original actual triadic caller contract `a=s_i e_i`, `b=s_j e_j`, `i≠j`, its two values coincide with the actual pair and the original first-branch ZERO ordering is retained. This theorem concerns native *two-step paths*; a two-force primitive equilibrium is not inferred.

A translated counterexample preserved from Unit126: `a=(1,0,1,0,0,0)`, `b=(0,1,1,0,0,0)`; the correct midpoint set is `{(0,0,1,0,0,0),(1,1,1,0,0,0)}`. The repaired live function returns this set.

## Actual three-mode and original-module validation

Locally reconstructed the complete exact previous active source (6074 bytes, prepatch blob `eb203...`) and the complete frozen native BRC (2852 bytes, blob `300a96...`). Applied the replacement to the actual complete Python module, first computed the new `cf5bc...` blob, ran all checks, and then made a guarded GitHub current-source update. The actual remote file was read back byte-for-byte and matched that local new blob.

Three Python configurations were executed separately: normal, `-O`, `-OO`. For **each** mode:

| Check | Exact result |
|---|---:|
| Full corrected *original module* exit | 0 / PASS |
| Full module stdout SHA256 | `03f98b37a4dcf346cc3a7063206f84253a3b7c1a219f1892f7967cd55201c2a2` |
| Named two-axis legal signed pairs, full midpoint match | 43,740 / 43,740 |
| Translation covariance checks with nonzero six-vector shift | 43,740 / 43,740 |
| Original anchored `q_triad` real caller pair-order equivalence | 480 / 480 |
| Illegal native pair inputs rejected | 4 / 4 |
| Controlled wrong native BRC multiplicity (`return 0`) rejected | 1 / 1 |
| AST `Assert` nodes remaining | 0 |

The 43,740 pairs exhaust `a ∈ {-1,0,1}^6`, `i<j` chosen among six axes and both independent signed increments. The prior raw helper returned the mathematically correct set for only 120 of these pairs; 43,620 wrong off-domain cases are directly removed. All three modes' certificate JSON stdout SHA256 is `e91721567b48069c5a9723300bb2c9de9d34211c8e9cdaa95692d7abc2ed7811`, exactly equal. Error checks use ordinary `if/raise`, not optimized-away `assert`.

The published regression is [the complete source-executing checker](../research_checks/X6_UNIT129_TRANSLATION_COVARIANT_MIDPOINT_REGRESSION_20261118.py) and the [integer execution certificate](../research_checks/X6_UNIT129_TRANSLATION_COVARIANT_MIDPOINT_RESULTS_20261118.json). These are finite exhaustive checks for the declared finite domain; the universal correctness and translation law follow from the proof above. The published checker uses repository-relative paths (`parents[1]`) instead of the local isolated-directory root and was separately exercised in all three Python modes.

## Typed downstream reconciliation row and next problem

| Current consumer | Source location | Old issue | Current disposition | Evidence |
|---|---|---|---|---|
| Signed triadic atomic midpoint helper | `experiments/x6_triadic_atomic_scatter_v1_20260906/check_triadic_atomic_scatter.py`, `midpoint_options` and real callers | `{ZERO,a+b}` implicitly treated as general two-step native path; optimized validators were previously optional | **PRESERVE_PATH_BRC / LIVE_GENERAL_TRANSLATION_REPAIRED / ALWAYS_ON_NATIVE_CHECKS** | Unit126 exact scope theorem; Unit127 original full-module replay; Unit128 13-guard repair; this Unit129 source commit + 3-mode native execution and 43,740 pair coverage |

The unrelated LP011 historical wrong signed argmax and LP019 alleged positive natural N-BRC subtraction callsites remain `UNRESOLVED_PROVENANCE` until original exact source:line and actual operation can be pinned. The broader 28-LP source:line consumer closure remains open. Driver `REQUEST_REVISION` and independent R063/Helly original benchmark review via Issue #2416 remain independently assigned; this author-side source repair is not their review.

**Next exact action:** reconcile the original own-run `onhour-20261118-1707-x6-own-units126-127-native-progress-v1` and `onhour-20261118-1701-x6-own-exact-continuation-v1` receipts by unchanged target ID, preserve their actual Source effects, and extend the 28-LP source:line consumer ledger to the next current executable rather than duplicate finished triaxial proofs. Semantic PROGRESS for Unit128–129 follows only the current own winning native authorization and nonoverlapping checkpoint contract.
