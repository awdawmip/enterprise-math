# R22: translated full-fibre theorem and exact S23 risk epochs

Date 2026-11-09. Original frozen science: awdawmip/enterprise-math@43ec6098b1330ae86d0a7863be336c5d97f6ef34. Prior source-labelled risk result: r21 PR #1882, commit 7fe79d88a45054c15f83dc3caac1c9bae4bb095f. Author-side independent research, review pending. The object is the scalar S23/AV auxiliary irrational-circle observer, not native X6 dynamics.

## Definitions and general theorem

For irrational 0<theta<1 write phi_j={j theta} and P_t={phi_j:0<=j<t}. Fix m historical cuts. Each clockwise historical interval I is refined by P_t into an ordered list of source-labelled subintervals with exact lengths. Let M_t(I) denote the maximum of those lengths. The full-block Bayes risk is R(m,t-m)=1-sum_I M_t(I).

**Translated full-fibre theorem.** Fix t0>=m and a historical clockwise adjacent pair (u,v), with u,v<m. Suppose phi_t0 lies inside their historical interval I_0. For any s>=0 such that u+s,v+s<m and the interval I_s=(phi_(u+s),phi_(v+s)) is again a historical adjacent interval, the complete ordered list of subintervals of I_s immediately before insertion of phi_(t0+s) is the index-translation by s of that of I_0 before insertion phi_t0. Lengths, source indices, multiplicities, and the position and lengths of the impending split are preserved. Thus the risk increments at cut counts t0+1 and t0+s+1 are exactly equal.

Proof: rotating by s theta maps I_0 and the labels 0,...,t0-1 to I_s and labels s,...,t0+s-1. The remaining predecessor labels 0,...,s-1 are all historical because s<=u+s<m. As I_s is a historical *adjacent* arc, none of these labels lies in its interior. Thus every interior cut and gap is precisely the translated predecessor. The new cut translates too. Only the owner historical arc changes at that insertion; its maximal-gap change is identical under translation. QED.

**Tie-max corollary.** If the interval about to be split has length g=x+y>0, and M_other is the maximum among all unaffected gaps belonging to the same historical arc (zero if none), then its exact risk increment is

Delta R = max(g,M_other)-max(x,y,M_other).

This formula uses the full observer-retained carrier, including tie multiplicity. A split of one of two tied longest gaps has Delta R=0; splitting a unique longest gap can increase risk. The theorem transports the entire source-labelled fibre, not merely the scalar length.

## S23 parameter and one-time adjacency certificates

Take m=128 and the inherited certified interval

262204504569236716045286 / 10^24 < theta < 262204504569236716045287 / 10^24.

Set a=164 theta-43, b=59-225 theta, c=102-389 theta=b-a, d=16-61 theta=a+b. Strict endpoint arithmetic gives 0<a<c<b<d. Write H=42 theta-11=a+2d and G=103 theta-27=a+d. For every theta in this interval, the phase floors of indices 0..492 and relative order of the associated cuts are fixed.

F42: the historical pairs (25+s,67+s), s=0..35, have clockwise length H. Any possible interior historical label j must have displacement k=j-(25+s) in [-60,102]. One endpoint-certified test of all k in this range, excluding k=0,42, gives {k theta}>H, so the pairs are adjacent. At s=36, historical j=0 becomes admissible, with k=-61 and 0<{-61 theta}=d<H. Thus this labelled translation family has exactly 36 historical-adjacency shifts.

F103: pairs (s,103+s), s=0..24, have clockwise length G. All eligible displacements k belong to [-24,127], and for k not in {0,103}, the strict endpoint comparison gives {k theta}>G. At s=25, index 128 would be an endpoint and is not historical. Thus 25 shifts.

F61: pairs (61+s,s), s=0..66, have clockwise length d. The inherited and independently checked closest-return certificate says d=min_{1<=j<128} ||j theta||, attained uniquely at j=61. Therefore these arcs are historical adjacent. At s=67, index 128 would cease to be historical. Thus 67 shifts.

The finite displacement tests are *one-time* checks over the indicated integer ranges, not one risk recomputation for each n. They establish adjacency throughout the strict parameter interval because the relevant integer floors and affine comparisons are stable at both rational enclosure endpoints.

## Five source-labelled base fibres

Each base fibre below is immediately before insertion t0. The ordered consecutive pairs retain their actual source labels, with their exact lengths after a colon:

| t0 | historical owner -> successor | ordered base fibre | insertion effect | shifts s | new n | Delta R |
|---|---|---|---|---|---|---|
| 292 | 25 -> 67 | 25->189:a; 189->128:d; 128->67:d | second d -> a,b, first d survives | 0..35 | 293..328 | 0 |
| 328 | 0 -> 103 | 0->164:a; 164->103:d | d -> a,b; new max b | 0..24 | 329..353 | a |
| 353 | 25 -> 67 | 25->189:a; 189->128:d; 128->292:a; 292->67:b | unique d -> a,b; new max b | 0..35 | 354..389 | a |
| 389 | 61 -> 0 | 61->225:a; 225->0:b | unique b -> a,c; new max c | 0..66 | 390..456 | a |
| 456 | 25 -> 67 | 25->189:a; 189->353:a; 353->128:b; 128->292:a; 292->67:b | last b -> a,c, other b survives | 0..35 | 457..492 | 0 |

The six base full-partition tests include these five and the restart base at t0=492. By the translated full-fibre theorem and one-time adjacency checks, this table proves **all 200 updates n=293..492**, including two exactly 36-step plateaux, without using a stepwise full-refinement reconstruction as the proof method. The three intervening positive families concatenate to 25+36+67=128 consecutive increases by a.

From the r21-certified exact value R(128,292-128)=-4928+18796 theta, the complete risk law is:

* For 292<=n<=328: R(128,n-128)=-4928+18796 theta.
* For 328<=n<=456: R(128,n-128)=-4928+18796 theta+(n-328)(164 theta-43).
* For 456<=n<=492: R(128,n-128)=-10432+39788 theta.

The next cut n=493 (label t=492) enters the historical arc 0->103. Immediately before it, that arc has the labelled gaps 0->164:a, 164->328:a, 328->103:b. The new cut splits the unique longest b into a,c. Because c>a, the increment is a. Thus R(128,493-128)=-10475+39952 theta.

## Exact certificate and scope

The accompanying standard-library Fraction checker validates both rational endpoints, floor/order invariance through index 492, one-time displacement-range exclusion, minimum return over indices 1..127, all base labelled fibres, and (independently) the full partitions and risk increments at every n=293..493. Its exhaustive cross-check is implementation evidence; the mathematics across 200 steps is from the full-fibre translation theorem and three finite adjacency certificates. The inherited theta enclosure is a frozen scientific input and is not rederived from logarithms in this r22 checker.

BRC use: source-labelled gap fibres preserve branch/provenance, exact maxima, and equal-max multiplicity under declared future cut insertions; reuse disposition REUSE_APPLIED (typed observer retention), not an assertion of a new native BRC arithmetic operation or an X6 result. The theorem is a general circle statement with a finite exact S23 specialization.

Follow-up: derive the post-493 growth/plateau endpoints from translated base fibres, preferably with Farey/continued-fraction jumps, test all bit/precision/preprocessing costs, and seek independent mathematical review. Existing formal task publication and live owner authorization still govern any shared CLAIM or Result admission.
