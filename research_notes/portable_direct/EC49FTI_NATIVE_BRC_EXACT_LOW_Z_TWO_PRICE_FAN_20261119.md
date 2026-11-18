# EC49FTI — Exact two-parameter native BRC16943 low-z price fan

Date: 2026-11-19. Scientific status: **AUTHOR_PROVED / EXACT_PRIMARY_18 / INDEPENDENT_RAW94_4 / NOT_REVIEWED**. Predecessor: [EC49FTH PR #2769](https://github.com/awdawmip/enterprise-math/pull/2769). Frozen original scientific pin: `awdawmip/enterprise-math@fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`.

## Exact model and theorem

The native BRC16943 finite identification model retains **310 original configurations, all 141 separately named response profiles, and all 228 original-index physical observations**. No state, observer, or profile quotient was imposed. This theorem is about exact original-index query-decision costs; it makes no unproved claim of an X6 physical transfer, and preserves P000/ACTIVE worldview unchanged.

Let `a,b,z` be discounts on q32, q34, q140, respectively, and let all other queries have baseline positive price `t`. For a valid complete tree, its aggregate path usage vector `(U,N32,N34,N140)` gives normalized total cost `F=141V/t=U-a*N32-b*N34-z*N140`. The swapped orientation exchanges the discounts on q32 and q34, without altering the query menu. Define `D` and `S` to be the **unrestricted native optimal** normalized costs for direct and swapped pricing.

**Theorem.** Fix `a=3/4`. For **every real** `7/16 <= b <= 57/128` and `3/8 <= z <= 3/5`, the exact global optima are:

```
D(b,z) = min(
  313 - 141*a - 47*b - 20*z,  # D20
  313 - 141*a - 43*b - 24*z,  # D24
  316 - 141*a - 43*b - 30*z   # D30
)
S(b,z) = min(
  309 - 28*b - 141*a - 46*z,  # S46
  311 - 28*b - 141*a - 51*z,  # S51
  311 - 10*b - 141*a - 69*z,  # S69
  315 - 10*b - 141*a - 77*z   # S77
)
```

The exact regions for a minimum-achieving native tree are:

| Orientation | z-interval (closed) | Witness | q140-use count |
|---|---|---|---|
| D | `[3/8,b]` | D20 | 20 |
| D | `[b,1/2]` | D24 | 24 |
| D | `[1/2,3/5]` | D30 | 30 |
| S | `[3/8,2/5]` | S46 | 46 |
| S | `[2/5,b]` | S51 | 51 |
| S | `[b,1/2]` | S69 | 69 |
| S | `[1/2,3/5]` | S77 | 77 |

Ties are allowed on switching sheets; no uniqueness is asserted. The direct and swapped optimizers **synchronize two phase changes** at `z=b` (q140 use 20→24 and 51→69) and `z=1/2` (24→30 and 69→77). The swapped side alone switches at `z=2/5` (46→51). Across the stated domain, `3/8 < 2/5 < b < 1/2 < 3/5`.

The swap gap `G=D-S` is exactly:

| Joint optimal cell | G |
|---|---|
| D20/S46, `3/8 <= z <= 2/5` | `4-19*b+26*z` |
| D20/S51, `2/5 <= z <= b` | `2-19*b+31*z` |
| D24/S69, `b <= z <= 1/2` | `2-33*b+45*z` |
| D30/S77, `1/2 <= z <= 3/5` | `1-33*b+47*z` |

Consequently, the **attained sharp bounds** throughout the full rectangle are

```
677/128 <= D(b,z)-S(b,z) <= 1181/80.
```

The minimum is realized at `(b,z)=(57/128,3/8)`; the maximum at `(7/16,3/5)`. For fixed b, the gap increases strictly with z, with successive exact slopes `26,31,45,47`.

## Proof with complete finite anchor certificate

**Feasible original-index witnesses.** The seven *complete native* decision trees archived alongside this proof have aggregate usage vectors:

```
D20=(313,141,47,20), D24=(313,141,43,24), D30=(316,141,43,30)
S46=(309,28,141,46), S51=(311,28,141,51)
S69=(311,10,141,69), S77=(315,10,141,77)
```

Every one has been followed across each of the 141 original named profile paths using the frozen original 228-observation arrays, checking legal index `0..227`, no repeated query on a profile path, and the exact original named leaf. Thus each is a globally feasible affine upper bound.

**Unrestricted finite Bellman anchors.** The exact, rational, full **all-228** dynamic program over every non-singleton set T of original named profiles computes

`B_p(T) = min_{q splitting T} ( |T|*(1-delta_q) + sum_r B_p(T_{q,r}) ), B_p({s})=0`.

The tested native code performs integer-scaled exact rational operations, distinguishing all original states. At **all eight D-specific and all ten S-specific cell vertices**, its unrestricted optimum equals the listed feasible witness. The full 18-row rational certificate (with source/tree hashes) is in the companion JSON; for independent exact review, the values are:

| Orientation | b | z | exact unrestricted F |
|---|---|---|---|
| D | 7/16 | 3/8 | 2867/16 |
| D | 57/128 | 3/8 | 22889/128 |
| D | 7/16 | 7/16 | 2847/16 |
| D | 57/128 | 57/128 | 22709/128 |
| D | 7/16 | 1/2 | 2823/16 |
| D | 57/128 | 1/2 | 22541/128 |
| D | 7/16 | 3/5 | 2775/16 |
| D | 57/128 | 3/5 | 22157/128 |
| S | 7/16 | 3/8 | 695/4 |
| S | 57/128 | 3/8 | 5553/32 |
| S | 7/16 | 2/5 | 863/5 |
| S | 57/128 | 2/5 | 27581/160 |
| S | 7/16 | 7/16 | 2731/16 |
| S | 57/128 | 57/128 | 21769/128 |
| S | 7/16 | 1/2 | 1331/8 |
| S | 57/128 | 1/2 | 10643/64 |
| S | 7/16 | 3/5 | 6347/40 |
| S | 57/128 | 3/5 | 50751/320 |

All 18 exact native Bellman anchors have been rerun as 3 batches of 6. Four independent source-derived raw-94-family reconstruction and separate exact Bellman checks match D at `(57/128,3/8)`, D at `(7/16,1/2)`, S at `(57/128,2/5)`, and S at `(7/16,3/5)`.

**Proof for every real parameter.** The unrestricted optimal cost is the pointwise minimum of finitely many feasible affine complete-tree costs, and hence jointly **concave** in `(b,z)`. Each witness-optimal region above is a *closed convex polygon* (here a quadrilateral with its four exact vertices among the listed 18 anchor rows). Let `L` be the corresponding feasible affine tree cost on its region `P`. For `p = sum lambda_i*v_i` any convex combination of vertices, by concavity and vertex optimality, `B(p) >= sum lambda_i B(v_i) = sum lambda_i L(v_i) = L(p)`; by feasibility `B(p) <= L(p)`. Therefore `B(p)=L(p)` for **every** real point in each cell, including irrational values and ties. Exact pairwise affine comparisons yield the phase boundaries. Exact affine gap extrema on vertices of the four joint cells establish sharp bounds. The slopes prove strict increasing gap with z.

**Validation/source scope.** Scientific input source files: `frozen_original_master.txt` SHA256 `cd9a50799536d2b96230777b5392b1d742ceee896da05bb49aa097cf351e1d5e`; `EC49FPG_PROFILE.csv` SHA256 `a61a3ee4d2f13f9d216f52cd3529c72d395c1250bfb1d7ae96a1adf5a6837c1f`. All raw sources, seven native trees, original-index and raw-94 solvers, proof, rational certificate, runnable verifier and original execution logs are in the separately delivered self-contained file `EC49FTI_NATIVE_BRC_2D_LOW_Z_FAN_EVIDENCE_20261119.tar.xz`, SHA256 `b5b0b38f12ffb5bb8a675417a1400de9f2a8964226a1f65160044a99f2b255eb`. The archive manifest covers 23 source/evidence files, and each was read back and SHA256 checked. Reproduction: from extracted archive, run `python EC49FTI_VERIFY.py --evidence-root .`, optionally `--full --start 0 --stop 6` (then 6:12, 12:18) and `--independent`.

**Next:** lift the 2D strip above `z=3/5` with the first D40/S87 rival trees; probe the new D16/S32 candidates below `z=3/8`; and lift a away from `3/4` to test a 3D open neighborhood. This author proof is not a separate independent mathematical review or formal Result/Review.

**Control:** the Source task lookup `emr4-fti-20261119-0453-read-task-01` returned `SUCCEEDED / NO_CANONICAL_PUBLICATION_DIRECTORY` at Source `5182f5cb492106d96312ffdfaefd3ad22cc91bf8`. Topic `RS-EC49AS` has no canonical formal Task publication in that snapshot, and the read is not a full native owner projection; formal CLAIM and current authenticated Researcher execution remain unconfirmed. The present output is independent portable scientific publication, not shared-owner execution or a canonical Activity checkpoint.
