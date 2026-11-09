# R30 — Near-return rigidity of provenance-bearing phase-source suffixes

Date: 2026-11-10 (Asia/Shanghai). Frozen scientific input: enterprise-math@43ec6098b1330ae86d0a7863be336c5d97f6ef34. Predecessor: R29 PR #1915, immutable source 56348eeb4d99d6fea7f16440443880640ee6354b. Scope: the auxiliary irrational-circle S23/AV observer, m=128, with preserved source labels. Independent author-side derivation, not a shared task CLAIM, independent review, native X6 dynamics or Foundation promotion.

## 1. General near-return theorem (proved)

Let alpha be irrational; let m,H be positive integers. The historical cuts are {s alpha} for 0<=s<m in R/Z; owner(x) denotes the labeled open oriented historical arc containing x. Define

    mu(m,H;alpha) := min_{1<=d<=m+H-1} ||d alpha||,
    ||x|| := distance(x,Z).

For every integer j>=m+H satisfying

    ||j alpha|| < mu(m,H;alpha),                                  (1)

and every r=1,...,H, we have

    owner({(j-r)alpha}) = owner({-r alpha}).                     (2)

Proof: for each historical endpoint {s alpha}, the circular distance from {-r alpha} to {s alpha} is ||(r+s)alpha||>=mu since 1<=r+s<=m+H-1. The circular shift from {-r alpha} to {(j-r)alpha} has a lift epsilon with |epsilon|=||j alpha||<mu. Such a shift crosses no historical endpoint. Thus it stays in the same historical arc, retaining its exact label. QED.

Consequently the source-labeled ownership word of the terminal H sources, each arc's latest source and its integer age relative to j are invariant for ALL near-return indices j satisfying (1). This is a genuine infinite family: for fixed irrational alpha, the convergent denominators j tend to infinity and satisfy ||j alpha||->0, while mu>0. The result about the word holds for these infinitely many j; application to an R27 Farey risk-event regime separately requires that regime's own neighbor/survivor hypotheses.

## 2. Uniform exact S23 parameter certificate

For an irrational theta in the frozen open interval

    L = 262204504569236716045286 / 10^24,
    U = 262204504569236716045287 / 10^24,

the verifier checks floor(d L)=floor(d U) for every d=1,...,291=m+H-1. Each d theta then lies strictly between the same consecutive integers. On that interval the integer-distance function ||d theta|| is triangular and has its minimum at an endpoint. Thus the exact uniform lower bound is

    mu(128,164;theta) >= mu_0
      = min_{1<=d<=291, x=L,U} ||d x||
      = 192343669352678928363 / 125000000000000000000000
      > 0.0015387.                                              (3)

Both endpoint minimizers occur at d=164. The floor stability simultaneously ensures the historical cut order and all comparisons of template phases {-r theta} to endpoints {s theta} are unchanged throughout (L,U). This is complete coverage of the finite set of 291 difference classes, not a floating-point estimate.

Enumerating ONLY the 164 theta-independent source-age slots r (and the 128 historical cuts) produces exact ownership counts: the shortest covering suffix has length H_min=164, whereas H=163 covers 127 historical arcs. At H=163 the missing arc is phase rank 127, originating at historical source s=61; its first terminal source has age r=164. The smallest r for each of the 128 historical owners is exactly the disjoint set

    {1,...,61} union {98,...,164}.                               (4)

Thus the 128 last-survivor offsets from j form

    {-164,...,-98} union {-61,...,-1}.                           (5)

Under R27/R29's applicable Farey neighbor theorem with q>164, each last-survivor age r corresponds to an event at n=q+j-r+1. Relative to q+j, event positions are two runs

    [-163,-97] (67 events) and [-60,0] (61 events),              (6)

with 36 intervening zero-increment positions. The event *amplitude* remains the exact min of the separately signed Farey errors.

## 3. Validation and broad finite cross-check

The three R29 j values 25339, 168319 and 10899111 satisfy the strict uniform inequality (1) throughout the same open interval. The verifier explicitly checks source owners of j-r and -r at both endpoints and their midpoint for every r<=164.

The earlier R27 event archive is an optional independent finite cross-check, not part of the general lemma proof. Among 78 recorded Farey regimes, 47 complete positive-event regimes satisfy q>164, q<j, determinant 1, opposite signed errors and the near-return bound. For those 47 regimes, the checker reconstructs ALL 6,016 source-labeled event positions from (5)-(6), determines the correct exact affine amplitude by strict rational endpoint inequalities, and matches every pair (index, two integer affine coefficients) against R27. All pass. One further qualifying regime truncated at the 10^12+128 observation horizon has zero events, so no amplitude claim is needed there. Earlier regimes outside the hypotheses are left unchanged.

Run from this directory:

    python VERIFY_R30.py
    python VERIFY_R30.py --regimes /path/to/REGIMES_R27.tsv --events /path/to/EVENTS_R27.tsv --certificate /path/to/CERTIFICATE_R30.json

Python integers and fractions.Fraction determine all comparisons; there is no floating-point phase ordering. PROOF.md plus VERIFY_R30.py, CERTIFICATE_R30.json and RUN_EVIDENCE.txt comprise the author-side reproducible evidence. External novelty and independent mathematical review remain open.

## 4. Next research unit

Build an output-sensitive direct merger of signed Farey batch descriptions into the existing 298 maximal affine risk runs, without first materializing 9,697 intermediate positive events. Preserve interval orientation, source indices, signed error switching and arithmetic/serialization/precision costs. A second useful question is the exact *directional* clearance (sharper than the symmetric sufficient mu_0) and its gain in batch size.
