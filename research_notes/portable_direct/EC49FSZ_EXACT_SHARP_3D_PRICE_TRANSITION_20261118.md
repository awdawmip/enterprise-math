# EC49FSZ — Sharp native-BRC three-price transition prism below z=21/32

Date: 2026-11-18. Scientific predecessor: EC49FSY, [PR #2741](https://github.com/awdawmip/enterprise-math/pull/2741). Original scientific input remains frozen at `awdawmip/enterprise-math@fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`; source master SHA256 `cd9a50799536d2b96230777b5392b1d742ceee896da05bb49aa097cf351e1d5e`, 141 named profile CSV SHA256 `a61a3ee4d2f13f9d216f52cd3529c72d395c1250bfb1d7ae96a1adf5a6837c1f`.

## Exact theorem

Work in the immutable BRC16943 native physical-query identification experiment: 310 original configurations, 141 distinguishable named joint-response profiles with uniform prior, 228 physically named observations. Adaptive trees use genuine named observation indices, strict splits and full 141-profile discrimination. Prices of q32, q34, q140 are `(1-a)t,(1-b)t,(1-z)t`, and all other prices are `t>0`. Define normalized optimal total cost `F=141V/t`, direct `D=F(a,b,z)`, swapped `S=F(b,a,z)`.

**For every real** `1/2<=a<=133/246`, `7/16<=b<=57/128`, `1/2<=z<=21/32`, the unrestricted exact native Bellman optima are

```text
D(a,b,z) = 319 - 18a - 75b - 141z
S(a,b,z) = min(315 - 141a - 10b - 77z,
               323 -  89a - 12b - 141z)
```

Swapped coefficients count actual q34/q32 uses after interchanging their prices, not relabeled physical observations. The S boundary is the **moving exact plane**

```text
z*(a,b) = (4+26a-b)/32.
```

The native price-swap gap therefore has the full exact piecewise law

```text
D-S = 4+123a-65b-64z,   z <= z*(a,b)
    = -4+71a-63b,       z >= z*(a,b)
```

and **attained sharp bounds** `441/128 <= D-S <= 161/16`. The lower bound occurs at `a=1/2,b=57/128,z>=z*(a,b)`; the upper bound at `a=133/246,b=7/16,z=1/2`. Hence the physical observer-price interchange has strictly positive asymmetry across this entire solid prism.

The upper a-face is **sharp for the stated D plane over the complete b,z rectangle**: at `b=7/16,z=1/2,a=133/246`, the alternative complete native D tree `313-141a-43b-24z` ties. For `a=133/246+epsilon`, epsilon positive and sufficiently small, this actual feasible tree lowers the displayed D plane by `123epsilon`. Native Bellman explicitly confirms improvement `123/1024` for `epsilon=1/1024`.

## Proof: actual finite native calculations and continuum certificate

1. Three complete native, strict-splitting trees supply **feasible upper planes**: D has path-use vector `(U,N32,N34,N140)=(319,18,75,141)`; P has `(315,10,141,77)`; C has `(323,12,89,141)`. Their 141 named profile paths and all physical query indices were replayed. The checks require no 2D projection, classical pi/trigonometry or alternate model.
2. The 3D box is cut by the plane `64z=8+52a-2b`. It intersects exactly four z-parallel box edges, with z-coordinates at (a,b)=(1/2,7/16): `265/512`, (1/2,57/128): `2119/4096`, (133/246,7/16): `34675/62976`, and (133/246,57/128): `277277/503808`. Together with the eight box corners this gives exactly **12 polyhedral vertices**. Direct D has eight box-corner vertices.
3. Each of the **12 S vertices and 8 D vertices** was recomputed by unrestricted exact-Fraction Bellman over all 228 native physical observations on the frozen 141-profile input. The observed exact values coincide with the displayed feasible planes. All 20 anchor values, explored Bellman subset counts and winning tree use counts are preserved in `EC49FSZ_NATIVE_3D_CERT.json`. The two new upper-a crossover points were additionally checked by an independent decoder of the original 94-family source: `12091177/62976` and `96699527/503808`; both match the first oracle exactly.
4. The unrestricted finite-tree optimum is a pointwise minimum of affine feasible tree costs and is **jointly concave** in `(a,b,z)`. On each of the two convex S-policy polyhedra and on the whole D box, equality at all vertices plus a feasible tree on that cell forces equality for **every real interior point**, by convex interpolation and concavity. This establishes the full three-dimensional theorem without assuming a finite grid captures the continuum.
5. The gap is affine on each of the two polyhedra, so its extrema occur at vertices. Exact rational evaluation yields `[441/128,161/16]`. The alternative direct tree gives the stated sharpness obstruction immediately past the upper a-boundary.

The result extends the earlier EC49FSY three-price fan from `z>=21/32` down to `z=1/2` on a sharp initial a-strip; it is genuinely 3D, not merely the previously solved fixed-(a,b) line.

## Evidence and status

Original source: frozen `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`; proof/oracle code and complete-tree source reuse EC49FSY PR #2741 and its self-contained provenance, with additional EC49FSZ local re-execution and two independent checks. Exact local commands: `python EC49FSZ_NEW_VERIFY.py --orientation D`; `python EC49FSZ_NEW_VERIFY.py --orientation S --independent`. The local complete evidence bundle preserves both original source inputs, four native Python modules, exact 20-anchor JSON outputs, three witness trees, executable, terminal logs, proof and SHA256 manifest. The GitHub reproduction file in this change set is `EC49FSZ_PRISM_RECHECK.py` and can validate the same theorem when copied beside those native inputs. No formal Lean acceptance or independent mathematical reviewer is claimed. Status: `AUTHOR_PROVED / EXACT_PRIMARY_20_NATIVE_BELLMAN_VERTICES / INDEPENDENT_2_RAW_94_FAMILY / THREE_FULL_141_PROFILE_TREES / NOT_REVIEWED`.

Research control: the historical topic `RS-EC49AS` is not assumed to be an immutable published task or currently claimed by this author. This note is an independent portable research artifact, not a CLAIM, Result, Review or Activity authorization.

**Next exact research unit:** remove the upper-a restriction or descend below `z=1/2`, locate additional 69/77/93/141-use q140 strategy interfaces and certify the resulting 3D polyhedral cells; retain named physical observation provenance.
