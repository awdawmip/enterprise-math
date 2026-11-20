# X6 Unit189 — Exact restoration of a frozen binary merge's weighted relation field, and limits of BRC path-history recovery

Date: 2026-11-20. Parent `PO-X6-SPATIAL-FOUNDATION-CONSISTENCY-20260905`, task `RS-X6-LEGACY-PLANE-RECONCILIATION`, publication `TP2-B4A441B23DA3159232C2`; ordinary research lane `chatgpt-research-onhour-enterprise-math-20260923`, not maintenance. **AUTHOR_PROVED / EXACT_INTEGER_BIGINT_EXECUTED / UNREVIEWED / NOT_ADMITTED.**

Frozen signed native X6 foundation: `awdawmip/enterprise-math@59538f585d037d09ef687b28715c4bc1a3f9fe03:definitions/ENTERPRISE_X6_NATIVE_SPATIAL_CELL_TORSOR_20260905.md`, blob `b4d49a1bbcccad0521618c6d20f6dcfa242b420a`. Real frozen A3 source: `awdawmip/enterprise-math@fd2bcff10ca6e147348b6c1236027fc0d2877df3:src/enterprise_math/weighted_relation_field.py`, blob `e50bf991e4dc4280063556a7aad1028f9f9404ed`, consumer functions `merge_weighted_relation_field`, `coarsen_weighted_relation_field`, `split_two_block_totals_from_internal_relation`, `recover_totals_from_weighted_field`. Actual tests `tests/test_weighted_relation_field.py` (blob `51748dfe340c385907c4f2218fa1ae5ae2260522`). The checker below independently implements source-equivalent formulas, not a direct import or native R063 execution.

## Exact theorem: one discarded relation restores the entire fine relation field

For arbitrary six positive source capacities `m_i`, integer native endpoint `z∈Z^6`, and distinct named axis indices `l,r`, the real source relation is `Z_ij=m_j z_i-m_i z_j`. Source `merge_weighted_relation_field` retains all four other singleton axes, appends the merged pair `P={l,r}` with capacity `m_P=m_l+m_r`, and returns the new coarse relation matrix `W` together with the **discarded internal relation** `δ=Z_lr=m_r z_l-m_l z_r`.

For each retained singleton index `j`, source coarsening gives `W_Pj=Z_lj+Z_rj`; therefore

```text
Z_lj = (m_l W_Pj + m_j δ)/(m_l+m_r),
Z_rj = (m_r W_Pj - m_j δ)/(m_l+m_r).
```

All other fine entries `Z_ij` are the corresponding coarse singleton entries, with `Z_lr=δ`, diagonal zero and antisymmetry. All displayed fractions are integers for actually generated source fields. Thus the frozen source representation mapping

```text
Z (fine six-axis weighted relation field) <-> (W coarsened field, δ lost internal relation)
```

is **exact and bijective on generated fields**, for arbitrary positive `m`; this is a precise source-backed lift of the existing frozen `split_two_block_totals_from_internal_relation` API. A compatible absolute grand total `G=Σ z_i` recovers the actual endpoint through frozen `recover_totals_from_weighted_field`:

```text
z_i = (m_i G + Σ_j Z_ij)/Σ_j m_j.
```

Alternatively, when the length `n` of signed native primitive events from a chosen Cell anchor is fixed, Unit187's exact finite source-field fiber inversion replaces the grand total with the finite ranked lift set. Therefore **all exact endpoint-resolved BRC multiplicities** and every function of them are computable from `(m,W,δ,n)`. This statement concerns counts of *named paths to each endpoint*, not the identity of an individual ordered path.

## Sharp observer residual and path provenance boundary

The coarsened field `W` alone loses one independent integer relation coordinate in the merge, for all positive m: the perturbation `z_l→z_l+1, z_r→z_r−1` preserves all group totals and hence W, but changes `δ` by `m_l+m_r>0`. By Unit188's kernel rank theorem, W has free kernel rank two for a single merge; adding δ restores the fine field with its one-dimensional primitive capacity gauge kernel. **One additional independent additive scalar is necessary and sufficient to restore fine field information**; the source-provided δ supplies it. This is an algebraic rank statement, not a fixed bit-count claim.

A finite-horizon witness at **n=1** is stronger than an unbounded formal distinction: the native endpoints `z=e_l` and `z'=e_r` produce identical W but discarded relations `δ=m_r` and `δ'=-m_l`. For `m=(1,2,1,2,1,2)`, merge axes 1 and 2, δ is 2 versus −1. Thus W loses even a one-step **named native direction**.

The scalar δ reconstructs a *fine endpoint relation field*, but cannot recover **individual ordered native word identities**. At n=2, the two named primitive paths `(+e_l,+e_r)` and `(+e_r,+e_l)` have the same endpoint, fine field, W, δ and n. Their exact signed-native BRC multiplicity is 2, which the restored field and finite-horizon formula correctly calculate, but order-specific future path operations require explicit path provenance. Hence multiplicity reconstruction and event-history reconstruction have different minimal carriers.

## Executed exact independent computation

The committed standalone JavaScript checker uses BigInt to compute native six-axis path counts under twelve primitive signed steps. Independently, for each reachable endpoint it computes the full factorial expansion from frozen X6 P000:

```text
N_n(z) = n! Σ_{k_1+…+k_6=(n−||z||_1)/2}
                  ∏_{i=1}^6 1/[(max(z_i,0)+k_i)!(max(-z_i,0)+k_i)!].
```

Three capacity vectors, all fifteen source binary merges, and all horizons 0 through 5 are tested. Exact totals: 4043 native endpoint DP/factorial comparisons; 181935 genuine source-equivalent merge computations; 181935 complete restored-fine-field comparisons; 181935 absolute grand-total inversions; 169905 whole-fiber BRC mass comparisons; and 45 one-step plus 45 ordered-path witnesses. Every comparison succeeded; total path mass was also checked as 12^n. This is author-executed exact finite testing plus a general integer proof, not independent Driver review, a live production integration or a repetition of the completed original R063 benchmark.

## Preservation and next obligation

Unit188 exact BRC coarsening and Unit187 finite weighted field fibers were consumed without claiming their proofs anew. Native semantic PROGRESS last actually authenticated was Unit174; author Units175–189 require the real Research lane's fresh winning CLAIM/RUN capability before semantic association. Original Units149–152 remain unassociated. Suspected historical LP011/LP019 offending code still lacks real typed `commit:path:line`; correct source arithmetic is not reclassified as a fault. Independent review `UNREVIEWED / NOT_ADMITTED`.

A discriminating next scientific step is to classify a **genuine future source operation that depends on per-axis path order or BRC weights**, with an exact pair of native histories colliding under (W,δ,n), and determine which minimal labelled event or order-residual must be retained. Do not change P000 or the frozen pins.
