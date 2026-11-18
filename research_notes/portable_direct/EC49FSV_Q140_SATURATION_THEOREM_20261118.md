# EC49FSV — Exact native q140 price-saturation transitions and swap-gap plateau

Date: 2026-11-18. Continuation of EC49FSU PR #2725 at immutable head `8205f22fda309f3ddf9aecfee13ad03fd91fdcc5`. Frozen science: `awdawmip/enterprise-math@fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`. Status: **AUTHOR_PROVED / EXACT_PRIMARY_8_ANCHORS / INDEPENDENT_2_ANCHORS / NOT_REVIEWED**.

## Exact model

Use the original BRC16943 population: 310 configurations, 141 distinct *named joint-response* profiles under the uniform profile prior, and all 228 separate *physical named observations*. No physical-index aliases are collapsed. All complete strict-splitting adaptive decision trees are eligible.

Query costs are `(1-a)t` for physical q32, `(1-b)t` for q34, `(1-z)t` for q140, and `t>0` otherwise. Let `F(a,b,z)=141 V(a,b,z)/t`, where `V` is the optimal average named-profile cost. Compare the actual orientations:
- `D(z)=F(2/3,7/16,z)` (direct);
- `S(z)=F(7/16,2/3,z)` (physical q32/q34 prices swapped).

## Theorem (all real z in [5/8,1])

```
D(z) = min(3351/16 - 40 z,  4387/16 - 141 z).
S(z) = min( 453/2  - 93 z, 12403/48 - 141 z).
```

The exact first q140 **universal-path optimal-saturation** thresholds are
`z_D=259/404` and `z_S=1531/2304`.
For `z>=z_D` direct has an optimal tree using q140 on all 141 named paths; for `z>=z_S` swapped has one. Below these respective values the optimum has strict slope `-40` or `-93`, so universal-path q140 optimal saturation is impossible.

The exact price-swap penalty is
```
D(z)-S(z) =
    -273/16 + 53 z   if 5/8       <= z <= 259/404
     763/16 - 48 z   if 259/404   <= z <= 1531/2304
     379/24          if 1531/2304 <= z <= 1.
```
Its **sharp attained range** is `[379/24, 27335/1616]`. The maximum occurs at `z=259/404`; the minimum persists for all `z∈[1531/2304,1]`. Above both saturation thresholds, both optima have slope `-141`, and their difference is identically `379/24`.

## Complete native tree witnesses

Each tuple is `(total physical-query uses U, q32 uses, q34 uses, q140 uses)`, counted across 141 complete named-state paths.

| Orientation | z interval | complete feasible tree vector |
|---|---|---|
| direct | [5/8,259/404] | (324,141,47,40) |
| direct | [259/404,1] | (319,18,75,141) |
| swapped | [5/8,1531/2304] | (324,8,141,93) |
| swapped | [1531/2304,1] | (327,9,97,141) |

Two additional native endpoint tie witnesses, `(316,141,43,30)` and `(318,10,141,82)`, are retained in the self-contained source certificate. All six trees were replayed over all 141 named profiles against their original physical observer indices; their uncompressed byte SHA256 values and lengths are in the companion JSON. Four of the six are used over intervals of positive length. The other two tie only at the left boundary.

## Full real-parameter proof

A feasible complete decision tree with query-use vector `(U,N32,N34,N140)` has exact affine total cost
`U-a*N32-b*N34-z*N140`. The unrestricted value is the pointwise minimum of all feasible tree costs, hence concave in `z`. Every exhibited complete tree provides an upper bound.

The full original-data `Fraction` Bellman oracle over all 228 physical observations was evaluated at every candidate intersection of the actual tree-line arrangements in `[5/8,1]`: **four direct** points `{5/8,71/111,259/404,1}`, and **four swapped** points `{5/8,1861/2832,1531/2304,1}`. At all eight, the unrestricted exact optimal value coincides with the exhibited feasible-tree lower envelope. Some tested pairwise intersections are internal arrangement vertices, not actual phase changes.

On the interval between each successive arrangement vertex, the proposed lower envelope is affine. Tree feasibility bounds the true optimum above it; true concavity and its exact endpoint Bellman values bound the true optimum below that same affine line. Thus these finite complete checks prove the displayed optimum for **every real z in the interval**. Exact subtraction and evaluation of the three affine gap intervals establishes the sharp range.

For saturation: if a 141-path tree is globally optimal at `z_0` and uses q140 in every path, its price decreases by exactly `141(z-z_0)` for larger `z`; any competing strict-splitting tree can use q140 at most 141 times, so cannot overtake it. Earlier nonsaturated slope intervals cannot have an optimal saturated tree, proving the first occurrence values.

## Original-source and verification evidence

The reproducible evidence archive `EC49FSV_NATIVE_BRC_Q140_SATURATION_SWEEP_FULL_EVIDENCE_20261118.tar.xz` has **13 members, 213188 bytes, SHA256 `0e95f7082427bba2d0155ffcd59942f259706c8eabc4a3402ac3476717b7e44a`**. It contains:
- Frozen raw source `frozen_original_master.txt` (SHA256 `cd9a50799536d2b96230777b5392b1d742ceee896da05bb49aa097cf351e1d5e`) and named profile CSV (SHA256 `a61a3ee4d2f13f9d216f52cd3529c72d395c1250bfb1d7ae96a1adf5a6837c1f`).
- Native full-228 solver, independent raw 94-family decoder, and all six entire losslessly compressed native trees in `CERT.json` (SHA256 `5d9a9b55e158809395b189dc26cb50bd8134ff94a328ec0a1b43be70a5e787e3`).
- `DERIVE.py`, `VERIFY.py`, exact eight-vertex results, derivation logs, original solver logs, and per-file checksums.

Run from the extracted archive root: `python VERIFY.py --oracle --independent`, then `sha256sum -c SHA256SUMS.txt`. In the recorded actual execution, all eight native Bellman anchors were recomputed, every complete tree and SHA was replayed, and the independent 94-family decoder matched the **direct 259/404** and **swapped 1531/2304** transition anchors. Remaining review level: author-verified exact calculation with partial independent numerical reconstruction, not independent substantive review.

## Open question and control provenance

Next: allow `a,b` to vary around `(2/3,7/16)` and determine exact saturation boundary surfaces `z_D(a,b),z_S(a,b)`, additional three-price Pareto witnesses, and stability of the constant-gap region. Inherited scientific pins/P000 and named-observer preservation remain unchanged.

The current native task read `r4-ec49fsv-20261118-1900-exact-task-read-01` returned `SUCCEEDED / NO_CANONICAL_PUBLICATION_DIRECTORY` for the `RS-EC49AS` topic at Source `b3a25442cd5ee1fafb037d2c2052f8fbb1da3ec1`; that read is not a full live-owner projection. Historical research attribution: `EM-DIRECT-8454C6`; historical Activity `RA-ED136F89271FD89288F3E58D`. This is independent portable GitHub scientific preservation, not a formal CLAIM, Result, Review or activity CAS.
