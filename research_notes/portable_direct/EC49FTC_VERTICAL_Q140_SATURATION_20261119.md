# EC49FTC — full-path q140 saturation over a nonrectangular 3D price region

Date: 2026-11-19. Status: AUTHOR_PROVED / EXACT_RATIONAL_ANALYTIC_EXTENSION / PRIMARY_4_NEW_TOP_ANCHORS / INDEPENDENT_2_NEW_TOP_ANCHORS / NOT_REVIEWED.

## Frozen model and verified prior theorem

Scientific input remains **awdawmip/enterprise-math@fc0f038e7bfd12c886b4d37f900bfb770c0f61ab**: 310 original configurations, 141 named joint-response profiles, and all 228 original physical observations. Price q32=(1-a)t, q34=(1-b)t, q140=(1-z)t; all other prices t>0. D and S are unrestricted optimal **standardized total** identification costs 141V/t, with S swapping a,b at q32,q34 (not swapping native outcome identities).

Source: [EC49FTA PR #2750](https://github.com/awdawmip/enterprise-math/pull/2750), immutable scientific commit eba1555f5763c76008c1788254a031e9a1e9912b, which proves over the full real box 133/246<=a<=1, 7/16<=b<=57/128, 1/2<=z<=9/16:
- D=min(319-18a-75b-141z,316-141a-43b-30z);
- S=min(315-141a-10b-77z,323-89a-12b-141z).

The EC49FTA proof uses exact unrestricted original-228-observation Bellman values at all 23 vertices of the two policy subdivisions, plus complete feasible native 141-profile trees and the concavity interpolation argument. Two relevant replayed tree usage vectors (U,N32,N34,N140) are D1=(319,18,75,141), C=(323,12,89,141), interpreted under their respective D and S price orientations. It is an author proof awaiting independent review.

## New exact theorem

For **every real** triple in the positive-volume closed region

\[
\boxed{\frac7{16}\le b\le\frac{57}{128},\quad
\frac{133}{246}\le a\le\frac{14+b}{26},\quad
\frac{4+26a-b}{32}\le z\le1,}
\]

the unrestricted native optimal costs are exactly

\[
\boxed{D=319-18a-75b-141z,\quad S=323-89a-12b-141z.}
\]

Both orientations have globally optimal native identification trees using q140 **on every one of the 141 named-profile paths**. Their exact swap gap is

\[
\boxed{D-S=-4+71a-63b,\quad
\frac{99683}{15744}\le D-S\le\frac{3271}{416}.}
\]

The lower bound is attained at (a,b)=(133/246,57/128), and the upper bound at (a,b)=(231/416,7/16), **for every z** above the respective permitted lower surface. The bounds are sharp over the displayed region, and all swap gaps are strictly positive.

## Proof

Define the inherited switch surfaces
\[
z_D=(3+123a-32b)/111,\quad z_S=(4+26a-b)/32.
\]
The base polygon in (a,b) is the convex quadrilateral with vertices
(133/246,7/16), (133/246,57/128), (231/416,7/16), (1849/3328,57/128).
Direct rational evaluation at these four corners gives **1/2<z_S<=9/16** and **z_D<z_S**. The two differences are affine, so these inequalities hold throughout the polygon.

For z_S<=z<=9/16, the inherited exact prism theorem selects D1 and C simultaneously as global native optima: D1 is optimal whenever z>=z_D; C is optimal whenever z>=z_S. In particular, at z0=9/16 both trees are globally optimal and both use q140 on all 141 input-profile paths.

**Full-path saturation lemma.** In any deterministic finite-profile identification tree with 141 profiles, repeated applications of the same observer along a single path are redundant and may be eliminated. Hence every nonredundant admissible tree T has 0<=N_q(T)<=141 total profile-path uses of q. If only q has a changing discount z, its exact cost is C_z(T)=C_z0(T)-(z-z0)N_q(T). For any optimal T* at z0 with N_q(T*)=141, any admissible T and z>=z0 satisfy

\[
C_z(T)=C_{z_0}(T)-(z-z_0)N_q(T)
\ge C_{z_0}(T^*)-141(z-z_0)=C_z(T^*).
\]

Thus T* remains globally optimal for all z0<=z<=1. Apply the lemma to original-price D1 and swapped-price C separately, extending both inherited optimal planes vertically from z0=9/16 through z=1. The two z-intervals join exactly to give the stated theorem.

Their difference cancels -141z. The affine function -4+71a-63b is increasing in a. At fixed a=133/246 it decreases in b, so its minimum is at b=57/128. On the upper base boundary a=(14+b)/26 its b-slope equals 71/26-63<0, so the maximum is at b=7/16. Arithmetic gives 99683/15744 and 3271/416, respectively. All extremizers belong to the closed allowed domain.

## New exact native checks at the previously unproved top face z=1

Four new unrestricted original 228-observer exact-rational Bellman runs were executed using the unchanged pinned scientific input:

| a | b | orientation | exact optimum F | native q140 path count |
|---|---|---|---|---|
| 133/246 | 7/16 | D | 88859/656 | 141 |
| 133/246 | 7/16 | S | 63287/492 | 141 |
| 231/416 | 7/16 | D | 3515/26 | 141 |
| 231/416 | 7/16 | S | 52969/416 | 141 |

An independent original-94-family data decoder coupled to a separate full 228-observer Bellman implementation recomputed the first D/S pair: exact agreement at 88859/656 and 63287/492. The inherited author-level 23-anchor proof and both complete named native trees were also locally replayed successfully. The separate machine-readable observations and check program are provided alongside this paper; the complete local execution log and original input are part of the separately retained self-contained evidence archive.

Original input SHA256: frozen_original_master.txt = cd9a50799536d2b96230777b5392b1d742ceee896da05bb49aa097cf351e1d5e; EC49FPG_PROFILE.csv = a61a3ee4d2f13f9d216f52cd3529c72d395c1250bfb1d7ae96a1adf5a6837c1f.

## Validation and continuation

The theorem for continuous parameters is established by the inherited **exact** finite Bellman certificate plus the proved saturation lemma, rather than uncountably many numerical samples. Four new full-native top-face checks and two independent checks corroborate it. This is author-checked, not independently reviewed or formally promoted. The scientific publication is independent portable research; the topic label RS-EC49AS has no established current formal Task/CLAIM binding in the last canonical control receipt.

Next: combine this low-a fully saturated family with the high-a family in [EC49FTB PR #2754](https://github.com/awdawmip/enterprise-math/pull/2754). Investigate the intermediate a-interval by mapping the original native policy fan on z=1, then find the **first downward q140 desaturation threshold** for each orientation. Require full named-observer tree or unrestricted exact Bellman verification before asserting a new policy cell.