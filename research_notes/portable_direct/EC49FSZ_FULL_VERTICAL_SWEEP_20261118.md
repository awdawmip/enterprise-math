# EC49FSZ — Complete exact vertical q140-price sweep and synchronized native BRC policy switches

**2026-11-18; author-reported scientific contribution; not independently reviewed.** Scientific provenance: frozen `awdawmip/enterprise-math@fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`; immediately previous EC49FSY [PR #2741](https://github.com/awdawmip/enterprise-math/pull/2741) @ `ba1eabe707242f5f5a3ea3184167fd28a503f059`. EC49FST [PR #2722](https://github.com/awdawmip/enterprise-math/pull/2722) supplies an earlier overlapping phase. The frozen finite native experiment has **310 configurations, 141 distinguishable named joint-response profiles, 228 physically named observations**. This is a theorem about this mathematical adaptive-identification model, not a physical measurement.

## New exact theorem (complete real interval)

Fix discounts `a=2/3`, `b=57/128` for physical observations q32 and q34, and allow `z` for physical q140 to vary over **every real** `z in [1/2,1]`. All other physical observations have cost `t>0`. Normalized unrestricted native Bellman cost is `F=141 V/t`. Write `D(z)=F(a,b,z)` and `S(z)=F(b,a,z)`, where the swap is a **physical** price swap, not a relabeling of observations.

The exact globally optimal costs are

~~~
D(z) = min(25965/128 - 30z,
           26761/128 - 40z,
           35021/128 -141z)

S(z) = min(13859/64 - 77z,
           14051/64 - 82z,
            7125/32 - 87z,
            3623/16 - 93z,
           24799/96 -141z).
~~~

Direct q140 usage counts switch **30 → 40 → 141** at `199/320`, `2065/3232`. Swapped q140 usage counts switch **77 → 82 → 87 → 93 → 141** at `3/5`, `199/320`, `121/192`, `3061/4608`. Every interval has positive length and every switch is a tie of two complete globally optimal native decision trees.

A new **synchronous native transition** occurs at precisely `z=199/320`: D changes **30→40** while S changes **82→87**. For the four corresponding abstract feasible-tree policy vectors, the affine cost differences obey
`D40-D30=8-4b-10z=2(4-2b-5z)=2(S87-S82)`,
independently of a. This identity implies coincident candidate crossings `z=(4-2b)/5`; **their joint global optimality is established here only for the certified slice**, not the whole three-parameter space.

Define physical exchange defect `G(z)=D(z)-S(z)`. It is **strictly positive** with sharp, attained interval

~~~
1255/128 <= G(z) <= 213257/12928
~~~

(minimum at `z=1/2`, maximum at `z=2065/3232`). From `z=3061/4608` through 1, the defect is exactly the constant `5867/384`.

The six explicit affine defect segments are:

| z interval | G(z) |
|---|---|
| [1/2, 3/5] | -1753/128 + 47z |
| [3/5, 199/320] | -2137/128 + 52z |
| [199/320, 121/192] | -1739/128 + 47z |
| [121/192, 2065/3232] | -2223/128 + 53z |
| [2065/3232, 3061/4608] | 6037/128 - 48z |
| [3061/4608, 1] | 5867/384 |

## Proof (exact finite Bellman certificate implies continuum)

For each deterministic strict-splitting complete *physical-index* native tree, its total expected cost over the 141 uniform named profiles is the affine function `U-a N32-b N34-z N140`. The physical-use vector `(U,N32,N34,N140)` counts full paths, not unique observation types. The **unrestricted** optimum is a pointwise minimum of these feasible affine functions, and therefore concave in the real price parameters.

Eight verified complete physical-observation trees supply the feasible affine upper envelopes:

~~~
D30  (316,141,43, 30)  D40  (324,141,47, 40)  D141 (319,18,75,141)
S77  (315,10,141,77)  S82  (318,10,141,82)  S87  (322,12,141,87)
S93  (324, 8,141,93)  S141 (325,12,92,141).
~~~

For the last S tree, `(325,12,92,141)` and an inherited alternative `(323,12,89,141)` have the same affine cost **at a=2/3**, producing the last displayed S plane; do not extrapolate their tie to general a.

The full original **228-physical-observation unrestricted Fraction Bellman DP** was executed at *both orientations* for the seven rational knots:

~~~
z = 1/2, 3/5, 199/320, 121/192, 2065/3232, 3061/4608, 1.
~~~

All 14 true Bellman values equal the corresponding displayed feasible-policy envelope **exactly**, not approximately. Exact values, native DP state counts and four independent checks are retained in `EC49FSZ_CERT.json`. Eight tree JSONs are verified for all 141 named profiles, strict splitting, actual physical response keys, no repeated physical observation along a path, and complete per-path use counts. Their SHA256 are in the certificate.

On each interval between consecutive knots, a single one of the eight feasible trees attains the candidate optimum at **both endpoints**. Concavity makes the unrestricted optimum at least its affine chord; feasibility makes it at most that same tree's affine cost, hence they agree for **every real z** throughout the interval. Exact rational intersection arithmetic yields every stated transition. The six affine defect slopes and knot values establish the sharp extrema. No finite-grid-to-continuum extrapolation is used.

Independent cross-check: four load-bearing knots (`D/S @ 199/320`, `S @ 121/192`, `D @ 2065/3232`) were recomputed by the separately decoded **raw 94-family** observation matrix and a second exact Bellman implementation. All agree.

## Reproduction and evidence provenance

The companion **self-contained EC49FSZ evidence archive** holds the immutable frozen raw master and named profile CSV, original native code, the distinct independent raw-family implementation, 8 complete native tree JSONs, 14 exact DP anchor outputs, 4 independent rechecks, detailed proof and Python reproducibility program `EC49FSZ_RECHECK.py`. Run the no-DP SHA256/rational/native-tree validation with `python EC49FSZ_RECHECK.py`; rerun the actual exhaustive original-data oracle with `python EC49FSZ_RECHECK.py --native --independent` from the extracted archive root. The full archive is delivered as a conversation file, not represented as a Git blob by this PR.

Source SHA256: raw master `cd9a50799536d2b96230777b5392b1d742ceee896da05bb49aa097cf351e1d5e`; profile CSV `a61a3ee4d2f13f9d216f52cd3529c72d395c1250bfb1d7ae96a1adf5a6837c1f`. The companion certificate contains all eight saved tree hashes and exact 14-knot fractions. Previous proof and verification: EC49FSY [#2741](https://github.com/awdawmip/enterprise-math/pull/2741), EC49FST [#2722](https://github.com/awdawmip/enterprise-math/pull/2722).

**Status:** `AUTHOR_PROVED / PRIMARY_14_EXACT_ALL228_KNOTS / INDEPENDENT_4_RAW94_KNOTS / EIGHT_NATIVE_TREES_REPLAYED / NOT_REVIEWED`. This is a portable-science output, without an asserted formal CLAIM, Result, Review, authenticated Activity checkpoint, P000 change or Foundation admission.

**Next discriminating problem:** Is there a positive-volume neighbourhood around `(a,b,z)=(2/3,57/128,199/320)` where the two candidate-switch pairs are jointly globally active? The algebraic coincidence alone does not settle optimality. Construct exact three-dimensional Bellman polytope vertex certificates (or an original-native counterexample), preserving the physical 87-use tree. Below `z=1/2`, investigate the 24/69-use boundary ties and the next true optimal phases.
