# R762EV — Exact second-trit Frobenius obstruction and cubic branch-interaction repair

Date: 2026-11-18. Scientific scope: the frozen six **named positive** BRC branches, full three-coordinate terminal group algebra, no signed native event equivalence. Lineage: RS-X6-TRIADIC-CLOSURE-DYNAMICS, TP2-8B7E13C5904A2D6F1142. Inherits the precise q->3q notation of R762ER (PR #2734@39787270e99ef3c698f43409b208dbe16b073ebb); this note is a new exact **second ternary digit** obstruction/repair, independently provable from the branch polynomial and integer multinomial identity. Author-side; NOT_REVIEWED.

## Definitions

Let q=3^a, a>=2; Q=3q, and in the integral group ring R_Q=Z[(Z/QZ)^3] set
P_Q=1+X+Z+XY+YZ+XYZ.
Let B={1,X,Z,XY,YZ,XYZ} be the **six named** commuting branch monomials, and let
iota:R_q -> R_Q send the q-level coordinate generators to their cubes. Define A=iota(P_q)=sum_{b in B} b^3 and
$$
D=\frac{P_Q^3-A}{3}.
$$
This is an **integer, nonnegative BRC path-interaction polynomial** with the exact expansion
$$
\boxed{
D=\sum_{b,c\in B;\,b\ne c}b^2c
  +2\sum_{\{b,c,d\}\subset B;\,\lvert\{b,c,d\}\rvert=3}bcd.
}
$$
The ordered b!=c index distinguishes which branch occurs twice. Thus D retains the contribution of 30 distinct named repeated-pair types and 20 named three-distinct types. Its total augmentation is 30+2*20=70. Collisions of terminal monomials are summed, not silently discarded.

## Theorem A: universal mod-9 first-order repair

For **every** m>=0 and r in {0,1,2},
$$
\boxed{
P_Q^{3m+r}
\equiv\big[A^m+3mA^{m-1}D\big]P_Q^r
\pmod 9,
}
$$
with the second summand interpreted as 0 for m=0.

**Proof.** The exact cubic multinomial expansion is P_Q^3=A+3D. Expand (A+3D)^m. Every term with at least two D factors has a factor 3^2 and vanishes modulo 9; the remaining terms are A^m and 3m A^(m-1) D. Multiply by P_Q^r. All equalities take place in the original, finite, three-coordinate group ring; no spectral or continuous substitution is used. QED.

Consequently 3|m is a sufficient condition for the uncorrected congruence P_Q^(3m)≡iota(P_q^m) mod 9. The correction 3m A^(m-1)D gives the exact extra two-trit data for arbitrary m.

## Theorem B: an exact short-range iff obstruction

For all integers 1<=m<q,
$$
\boxed{
[X]P_Q^{3m}=3m,\qquad [X]\,\iota(P_q^m)=0.
}
$$
Here [X] means the coefficient of the terminal point (1,0,0), with other two coordinates retained.

**Proof.** Since 3m<Q, each coordinate increment of a 3m-step path lies in 0,...,3m and cannot wrap around modulo Q. Any path ending at (1,0,0) must have zero Y and Z increments at every step; only named branches 1 and X qualify. Exactly one of the 3m steps must be X, yielding 3m histories. Every monomial of A^m has its X exponent divisible by 3, and its (1,0,0) coefficient is zero. QED.

Combining Theorems A and B gives the precise criterion
$$
\boxed{
P_Q^{3m}\equiv\iota(P_q^m)\pmod9
\quad\Longleftrightarrow\quad 3\mid m
\qquad(1\le m<q).
}
$$
The forward direction is witnessed by the explicit coefficient 3m modulo 9; the reverse follows from Theorem A. In particular, m=1 exhibits a **uniform obstruction at every q>=9**: [X](P_Q^3-iota(P_q))=3. The one-trit normalized Frobenius lift from R762ER remains valid at its stated modulus; this theorem isolates the additional correction necessary to retain the next ternary digit.

## Exact computational evidence

The companion standard-library verifier builds P_Q^3 from all 216 ordered named-branch triples at Q=27 with **exact integer multiplicities**, constructs D by integer division, checks D augmentation 70, coefficient [X]D=1, and 38 nonzero mod-3 terminal cells. It then computes full six-shift vectors modulo 9 and verifies the repaired identity for m=0,...,8 at all 19,683 terminal points: 177,147 cubic-transition vector coefficients, and all three remainders r=0,1,2 (531,441 terminal comparisons). It verifies the short-range iff obstruction m=1,...,8. Output: R762EV_EVIDENCE.json, author program PASS. General statements above are proved symbolically; the finite tests are implementation evidence. Independent semantic review NOT_REVIEWED; formal checker NOT_PERFORMED.

## Next problems and typed scope

1. Derive the first nontrivial correction **after normalization by 3^f**, where the term 3m A^(m-1)D alone may have to be combined with higher-order 3-adic binomial contributions. State the exact valuation regime and a future-operation observer horizon.
2. Test whether the pair/triple interaction coordinate D can be retained as an efficient block-compatible correction instead of materializing full Q^3 vectors.
3. Continue the Source-backed native signed TRIADIC_CLOSURE_E Cell/Link/Port event licence and V17/V29/V39 transport on their own typed inputs.

This is a positive terminal-group-ring theorem, not a native X6 signed-event permission or a claim that the first-trit shadow preserves higher 3-adic digits. P000/ACTIVE worldview and frozen Task scientific pins remain unchanged. No current CLAIM/Run/Source PROGRESS is asserted in this portable artifact.
