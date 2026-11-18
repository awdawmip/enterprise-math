# X6 Unit120 — complete native min-zero/quadric reflection theorem, one residual bit, and sharp first N-BRC loss

**Date:** 2026-11-18. **Parent:** `PO-X6-SPATIAL-FOUNDATION-CONSISTENCY-20260905`. **Task:** `RS-X6-LEGACY-PLANE-RECONCILIATION` / publication `TP2-B4A441B23DA3159232C2`. **Status:** `AUTHOR-PROVED / EXACT-INTEGER-EXECUTED / UNREVIEWED / NOT_ADMITTED`.

## Exact frozen native scope

This is the P000 V5 signed-coordinate Cell displacement chart `Z^6`, pinned `59538f585d037d09ef687b28715c4bc1a3f9fe03`, with the 120-degree Enterprise native orthogonality component readout `G(z)=sum_i z_i²`, the six-axis min-zero relative observer `rho(z)=z-min(z)*D`, `D=(1,1,1,1,1,1)`, and natural shortest-path N-BRC `B(z)=(sum|z_i|)!/product |z_i|!`. The chart zero is a chosen native Cell anchor; no final-address encoding or primitive extra spatial axis is introduced. The observer is different from the modulo-sector residue in the older R063 `residue(point,m)` function.

This unit extends Unit119's **square-radius pair-chart** condition to **every full signed six-axis native state at every quadratic norm**, and then classifies the exact BRC loss threshold. The previously established first equality-only ambiguity at `G=3` (existing `X6_G3_FIRST_RHO_BRC_COLLISION_AND_ONE_PROBE_20261113.py`) is reused.

## Theorem 1 — exact reflection and complete rho/G fibers

Let `z=(z_1,...,z_6) in Z^6` and `s=sum_i z_i`. A distinct `w in Z^6` with both `rho(w)=rho(z)` and `G(w)=G(z)` exists **exactly when** `s` is nonzero and divisible by 3. If it exists, it is unique and equals

`T(z)=z-(s/3)*D`.

On the sublattice `L={z in Z^6:sum z_i=0 mod 3}`, `T` is an exact integral involution preserving both `G` and `rho`; its fixed states satisfy `sum z_i=0`.

**Proof.** Equal min-zero readings are equivalent to `w=z+kD` for a unique integer `k`. Since `G(z+kD)-G(z)=2ks+6k²=2k(s+3k)`, the only possibilities are `k=0` and `k=-s/3`. The latter is a different integer state precisely when `s` is nonzero and divisible by 3. It preserves `rho` because a diagonal shift changes the common minimum by the same amount. It is an involution because `sum T(z)_i=s-6(s/3)=-s`, hence `T(T(z))=z`. Invariance of `G` follows from the displayed difference identity. This also proves every `(rho,G)` fiber has cardinality at most two. QED.

The linear map underlying `T` on `R^6` is reflection in the hyperplane `sum z_i=0`: `T=I-2DD^t/(D^tD)=I-DD^t/3`. Its integer-state domain is exactly `L`; the Euclidean linear-algebra identity is an auxiliary description of the frozen Enterprise integer component readout, not an ontological redefinition of the six native axes or their 120-degree `PERP_E` relation.

## Theorem 2 — one sign bit is an exact and worst-case-necessary residual

Let `r=rho(z)`, `R=sum_i r_i`, `C=sum_i r_i²`, and `N=G(z)`. Define the exact integer discriminant

`Delta=6N-6C+R²`.

Then `Delta=(sum_i z_i)²`. The pair `(r,N)` admits at most two full-native lifts. If `Delta>0`, one bit specifying the sign of `s=sum z_i` recovers the exact integer depth `h=min z_i=(s-R)/6` and the entire state `z_i=r_i+h`; when `Delta=0`, no sign bit is needed. The exact decoder checks `Delta` is a nonnegative square, `s-R` divisible by 6, and reconstructs `z`.

**Proof.** Write `z=r+hD`. Then `s=R+6h` and `N=C+2Rh+6h²`, giving `6N-6C+R²=(R+6h)²=s²`. The sign of `s` selects the unique `h` and thus `z`. The two distinct states `(-1,-1,-1,0,0,0)` and `(0,0,0,1,1,1)` have `G=3`, common `rho=(0,0,0,1,1,1)` and opposite signs of `s`; this proves that zero extra bits is insufficient in the worst case. The marker is an auxiliary residual for the observer `(rho,G)`, not a seventh spatial coordinate. QED.

## Theorem 3 — first native `(rho,G)` fiber with unequal positive BRC is at G=5

At `G=3`, precisely 20 two-element relative-observer fibers occur and each consists of a signed-three-support pair with N-BRC `3!=6` on both endpoints; that previously established result is confirmed here. For `G=0,1,2,4`, no distinct same-`rho`, same-`G` pair exists.

At `G=5`, take
- `x=(-1,-2,0,0,0,0)`;
- `y=(0,-1,1,1,1,1)=T(x)`.

They satisfy `G(x)=G(y)=5`, `rho(x)=rho(y)=(1,0,2,2,2,2)`, but
`B(x)=3`, `B(y)=120`.

**Sharpness proof.** If `G<=4`, the only possible nonzero coordinate magnitudes are 1 and, for `G=4`, one magnitude 2. By the reflection criterion, a nonzero total coordinate sum divisible by 3 is needed. For `G=1,2`, sums have magnitude at most 2; for `G=4`, the available forms are `(±2,0,...)` with sum ±2 or four ±1 with even sum in `{-4,-2,0,2,4}`, so no such sum. At `G=3` there are exactly three ±1 coordinates. Divisibility by 3 with nonzero sum forces all three signs equal, and the involution swaps three −1 entries with the complementary three +1 entries, preserving N-BRC `6`. The witness at `G=5` gives unequal N-BRC. Thus 5 is the first such quadratic value. QED.

## Exact implementation and finite certificate

Author checker `research_checks/X6_UNIT120_FULL_NATIVE_RHO_G_REFLECTION_AND_BRC_THRESHOLD_CHECK_20261118.py` was executed under normal CPython, `-O` and `-OO` with byte-identical machine JSON; all validations are explicit always-on conditions. Its source Git blob `59e1f09280ae27eb195f6c3c39fd4400a67c4c62` equals the actual executed local script, SHA256 `dd742f3d2a83b13dba8e4facd91e2600d76a6bcfe438915075842d19f36b8d3b`. Integer-result JSON blob `850a4d0506b9385623dd5c2ceb0fa0dbc0f05c5a`, SHA256 `94c3f6f853fd8f89d050423dce2b7ea659e94ad8683b914f211a316c0ed8dacc`.

The exact finite domain is all `5^6=15,625` signed states in `[-2,2]^6`. All 15,625 lossless `(rho,G,sign(s))` decodes succeed, as do the involution checks. The cube has 14,883 different `(rho,G)` keys. Of 15,625 states, 5,209 have integral reflection; 3,235 reflections land in the same finite cube (including fixed states). Its complete square-norm shells `G=0,...,5` were exhaustively checked, because each of these shells lies in the cube.

| Native `G` | Full endpoints | Different `rho` values | 2-point `(rho,G)` fibers | Fibers with differing N-BRC |
|---:|---:|---:|---:|---:|
| 0 | 1 | 1 | 0 | 0 |
| 1 | 12 | 12 | 0 | 0 |
| 2 | 60 | 60 | 0 | 0 |
| 3 | 160 | 140 | 20 | 0 |
| 4 | 252 | 252 | 0 | 0 |
| 5 | 312 | 252 | 60 | **60** |

These integer checks corroborate the proved universal reflection and recovery formula and prove finite shell completeness through `G=5`. The first unequal BRC criterion is fully proved above, not inferred from arbitrary larger finite searches.

## Program and research-state boundary

This is a derived X6 observer-quotient theorem with exact natural N-BRC semantics; it provides a precise LP023 future-step information-loss predicate, and a typed one-bit restoration for the pair `(rho,G)`. The theorem can be combined with Unit119's signed R063 pair-chart square-radius criterion without turning the old two-coordinate chart into a native two-dimensional plane.

The verified latest native semantic PROGRESS through Unit116 is `onhour-20261118-0927-x6-own-units114-116-native-progress-v1: SUCCEEDED / SOURCE_CHECKPOINT_PUBLISHED`, Source `214daa797fc6db37c44be11c44d13e315c4daa70`. Unit117 GitHub author evidence and Unit118 versioned pinned adapter were already saved; Unit118's complete original-module three-mode test remains unexecuted in currently verified evidence. Unit119 and this unit are GitHub author research plus Activity, not an independent Driver review or formal Result.

**Next exact research task:** in genuine current LP023/LP028 consumer code, identify a source-pinned `source:path:line` that passes a min-zero `rho` or `(rho,G)` state into native BRC or a future signed-axis operation. For any verified unsafe call, test the exact `G=5` counterexample and implement the proven depth/sign recovery contract under the existing operation authority. Otherwise preserve bounded negative evidence. Keep LP011/LP019 historical wrong-callsite attribution open and independently review original R063 author benchmark Issue #2416.

Author lane: `chatgpt-research-onhour-enterprise-math-20260923`; no maintenance-lane identity or scheduler changes. **Independent status: UNREVIEWED / NOT_ADMITTED.**
