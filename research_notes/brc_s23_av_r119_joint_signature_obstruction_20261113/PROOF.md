# R119.1 — Exact joint-signature obstruction for two newly added S23 times

Date: 2026-11-13. Companion to R118, author-side S23 auxiliary directed-circle observer. Scientific input remains frozen at 43ec6098b1330ae86d0a7863be336c5d97f6ef34. Complete time/branch identities and history provenance are unaffected.

## A whole rational one-parameter family

Fix j in Z, a=0, c=1, a rational x with 0<x<1, and old open atom J=(0,1). No old time source is required; the A,C,A-C integer crossings do not split the open atom. Introduce *two distinct new times* t0=j and t1=j+1 simultaneously. Eligibility M_t(theta) is fractional membership in the positively directed half-open arc from {0}=0 to {theta}=theta on J.

**Theorem (exact joint two-time characterization).** For all theta in (0,1),

M_t0(theta)=1 if and only if theta>x;
M_t1(theta)=1 if and only if theta>=1-x.

Consequently:
- If 0<x<1/2, the **exact attainable** bit pairs (M_t0,M_t1) are (0,0), (1,0), (1,1), while (0,1) is impossible.
- If x=1/2, the exact attainable pairs are (0,0), (0,1) (only at theta=1/2), (1,1), while (1,0) is impossible.
- If 1/2<x<1, the exact attainable pairs are (0,0), (0,1), (1,1), while (1,0) is impossible.

In all three cases each individual new bit attains both 0 and 1 on J, but **one combination of their individually feasible values is not jointly realizable**. Thus per-time R118 feasible-bit sets cannot be simply Cartesian-multiplied to obtain an exact multi-new-time signature set.

**Proof.** On J the directed arc is [0,theta). For t0=j the unwrapped candidate is Y_t0=x, so x lies in [0,theta) precisely when theta>x. For t1=j+1 the candidate is Y_t1=x+theta. If theta<1-x then x+theta<1 and its fractional part is x+theta>theta, so it is excluded. If theta>=1-x then its fractional part is x+theta-1, which lies in [0,theta) because 0<x<1; note that equality theta=1-x maps to fractional part 0 and is INCLUDED. Hence M_t1=1 precisely for theta>=1-x. Intersecting the two threshold sets and their complements gives the stated three exact classifications, including the singleton boundary x=1/2. Each listed pair has a rational witness because x is rational and the non-singleton intervals have rational endpoints; impossible pairs contradict the derived inequalities. QED.

## Exact sample checks

File check_r119_joint.py evaluates the direct original fractional-circle predicate on 719 interior rational grid points, plus both threshold endpoints, for x=1/10, 1/2, 4/5. The observed signature sets agree with the theorem. This finite check confirms the implementation examples; the universal result for all rational x in (0,1) follows from the displayed inequalities.

## Next useful task

For two arbitrary high-frequency times in the actual S23 six-affine-phase predicate, find a joint lattice/semilinear feasibility certificate with exact rational witness and controlled bit complexity, without forming all new cut points. The present family proves that independent single-time oracles alone are not sufficient for arbitrary simultaneous introduction.

Status: author-side mathematical proof and exact finite test, pending independent review. No native X6 event authorization or canonical task CLAIM is asserted.