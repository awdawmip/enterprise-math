# EC49FTE — sharp native q140-saturation middle bridge

2026-11-19 | AUTHOR_PROVED / EXACT_PRIMARY_10_BELLMAN_ANCHORS / INDEPENDENT_RAW94_2 / FOUR_ORIGINAL_INDEX_TREES / NOT_REVIEWED.

## Frozen input and definitions

Scientific input is the unchanged immutable `awdawmip/enterprise-math@fc0f038e7bfd12c886b4d37f900bfb770c0f61ab` (BRC16943): 310 native configurations, 141 individually named joint-response profiles, and 228 original indexed physical observations. Source SHA256: `frozen_original_master.txt=cd9a50799536d2b96230777b5392b1d742ceee896da05bb49aa097cf351e1d5e`; `EC49FPG_PROFILE.csv=a61a3ee4d2f13f9d216f52cd3529c72d395c1250bfb1d7ae96a1adf5a6837c1f`. This continues [EC49FTD PR #2760](https://github.com/awdawmip/enterprise-math/pull/2760) without changing native state or observer identities. No claim about X6 physical dynamics follows.

Normalize per-query baseline price to 1 and standardized identification cost to `F=141V/t` for baseline price `t>0`. Under D the discounts `(a,b,z)` attach to original q32, q34, q140; under S only a and b are exchanged. Every other observer retains undiscounted cost 1.

## Exact continuous theorem

For **all real**
```
3/4 <= a <= 4/5
7/16 <= b <= 57/128
1709/2080 <= z <= 1,
```
the **unrestricted** 228-observer native Bellman optima are exactly
```
D(a,b,z) = min(329 - 36a - 68b - 141z, 333 - 40a - 70b - 141z)
S(a,b,z) = 333 - 105a - 9b - 141z.
```
The moving D-policy switch is `a=1-b/2`. Both optimal pricing assignments admit decision trees observing q140 exactly once on every one of the 141 named-profile paths. The price-exchange gap is independent of z and has **attained sharp bounds**
```
2749/128 <= D-S <= 405/16.
```
The lower bound is attained at `(a,b)=(3/4,57/128)`, the upper at `(4/5,7/16)`, for every z in the interval.

**Sharp lower face.** The value `z0=1709/2080` is the smallest *uniform lower discount* for which both orientations admit q140-saturated global optima for all (a,b) in this rectangle. For any z<z0 at `(a,b)=(4/5,7/16)`, the S orientation has no fully q140-saturated global optimum.

## Proof and load-bearing native evidence

Four actual original-index feasible identifying decision trees were reconstructed and replayed on all 141 named profiles. Their usage vectors are `(U,N32,N34,N140)`:

| Tree | Original-index usage | Applied orientation |
| --- | --- | --- |
| Dmid | (329,36,68,141) | D |
| Dhi | (333,40,70,141) | D |
| Smain | (333,9,105,141) | S |
| Tnonsat | (340,8,141,115) | S |

These furnish global upper bounds with the displayed affine costs. In the swapped orientation, the a coefficient is the original q34 count and the b coefficient is q32 count. Complete tree hashes and original input hashes are retained in `EXACT_CERT.json`; full tree bytes and frozen input are also in the accompanying self-contained evidence archive.

At `z=z0` the D-plane intersection is `4-4a-2b=0`, splitting the rectangle into two convex cells. Their joint vertices are four corners plus `(a,b)=(25/32,7/16)` and `(199/256,57/128)` (six D vertices). The S candidate has a single affine cost and needs only the four corners (four S vertices). **All ten vertices were recomputed with exact-rational, unrestricted Bellman minimization over all 228 original indexed observations**, matching the candidate costs exactly. Two selected anchors were separately checked by an independent raw-94-family decoding and Bellman implementation. See the ten actual values and two independent values in `EXACT_CERT.json`.

For either orientation, the optimal Bellman cost is the pointwise infimum of affine costs of all feasible complete identifying trees and hence is concave in a,b. On each convex D cell, a single feasible witness has affine cost L equal to the exact Bellman optimum at each cell vertex. Concavity implies `B(x)>=L(x)` throughout the cell, while the witness gives `B(x)<=L(x)`. Equality holds for **every real (a,b)** in each cell. The same argument applies to the entire S rectangle.

No irredundant deterministic identifying tree queries the same observation twice on the same named-profile path; its outcome is already known after the first query, so a repeat cannot refine that path. Therefore `N140<=141`. For any z>=z0 and one of the optimal saturated witnesses T* at z0, every competing tree T satisfies
```
C_z(T) = C_z0(T) - (z-z0)*N140(T)
      >= C_z0(T*) - 141*(z-z0) = C_z(T*).
```
This lifts the Bellman equality to all real z through 1. The two gap pieces are `-4+69a-59b` and `65a-61b`; both increase in a and decrease in b. The opposite rectangle corners give the stated attained gap bounds.

For sharpness, the valid Tnonsat has swapped cost `340-141a-8b-115z`. Subtracting Smain gives `7-36a+b+26z`, and at `a=4/5,b=7/16` this equals **`26(z-1709/2080)`**. At z0 the saturated Smain is globally optimal by the native exact certificate; all fully saturated trees have identical -141 slope as z changes. At every z<z0 Tnonsat is cheaper than each such saturated tree at this corner, proving the uniform lower threshold sharp. Tnonsat need not itself remain globally optimal throughout the lower interval.

## Reproducibility and next question

The companion `EXACT_CERT.json` gives the 10 exact anchor fractions, original data digests, two independent recalc values, four complete original-index tree hashes, and the sharpness witness. Local checks: unrestricted rational Bellman primary 10/10; raw-94 independent 2/2; original-index 141-state replay 4/4. Original pinned native scripts and unabridged proof/trees/logs are provided in the companion full evidence archive; external mathematical peer review remains pending.

Next independent work: `4/5<a<31/32` at high q140 discounts, where further saturated strategy vectors appear; construct a new exact rational policy fan and prove its sharp desaturation boundary. Keep the unchanged frozen pin and all named observer distinctions.

**Control provenance:** Portable independent research; no formal TASK CLAIM, Result, Review or Activity checkpoint is asserted by this GitHub publication.
