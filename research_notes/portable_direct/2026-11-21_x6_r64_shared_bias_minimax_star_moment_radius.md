# X6 R64 — Exact shared-bias minimax radius for positive-BRC star-moment degree tomography

Date: 2026-11-21 (Asia/Shanghai)
Line: RS-X6-NATIVE-TIME-DYNAMICS
Scientific status: CONDITIONAL_AUTHOR_PROOF / EXACT_INTEGER_FINITE_AUTHOR_CHECK / NOT_INDEPENDENTLY_REVIEWED
Scope: conditional normalized repeated-A star observer (R61–R63); NOT a native TRIADIC_CLOSURE_E timing claim.

## Fixed scientific inputs

The frozen P000 foundation is awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389:p000_reality_foundation.json (V5). Preserve all six native spatial axes, independent time, Cell/Link and named Port provenance, whole-triad primitive-event arity and source labels. The present theorem is a conditional positive BRC observation on a binary AB success-incidence relation; it does not quotient the underlying relation for future experiments.

Scientific predecessor: R63, research_notes/portable_direct/2026-11-21_x6_r63_common_bias_star_moment_residual.md (blob f8c537e3ac17c83dcb0cb9dd5cf9196a92029fa3). The current behavioral rules were read separately and are not frozen scientific inputs.

Assume integers p >= D >= 2, p named Ports per source, binary p-by-p success table, Port-independent positive AB branch weights u,v. Any prescribed row-success-degree histogram c=(c_0,...,c_D), c_d nonnegative integers summing to p, is realizable as a named binary table because D <= p. Observe normalized positive star masses
\[
m_t(c)=Z_{\mathrm{star}}(t)/(uv)^t=\sum_{d=0}^{D} c_d d^t,\quad t=1,\ldots,D.
\]
One unknown real common additive normalized bias b and channel errors |e_t| <= eta give y_t=m_t(c)+b+e_t. The known population m_0=p is not a biased observation. The reconstruction target is (c_2,...,c_D), not the full incidence table nor the ambiguous (c_0,c_1) split.

## R64.1 Exact pairwise ambiguity radius

For two feasible histograms c,c' with unequal high-degree vectors, let Delta_t=m_t(c)-m_t(c') for t=1,...,D, and let osc(Delta)=max_t Delta_t-min_t Delta_t.

**Theorem.** There exists a single measured vector y compatible with both models, allowing separately unknown constant biases and per-channel errors <= eta, if and only if
\[
\boxed{\eta\geq \frac{\operatorname{osc}(\Delta)}4.}
\]
Consequently the sharp *uniform* high-degree uniqueness threshold for fixed p,D is
\[
\boxed{\eta_{p,D}^{*}=\frac14
\min_{\substack{c,c'\in\mathbb N^{D+1}\\ \sum c=\sum c'=p\\
(c_2,\ldots,c_D)\ne(c'_2,\ldots,c'_D)}}
\operatorname{osc}\bigl(m(c)-m(c')\bigr).}
\]
For eta < eta* all compatible models share the same high-degree counts. At eta=eta* some admissible observation is ambiguous, so the strict threshold is sharp.

Proof: The two model centers are affine lines m(c)+b 1 and m(c')+b' 1 in R^D. Their least l-infinity separation is min_a max_t|Delta_t+a|=osc(Delta)/2, attained by centering their maximum and minimum. Two closed l-infinity error boxes of radius eta have a common point exactly when their center separation is <=2eta. This yields the factor 1/4, including equality.

For a fixed actual observation y, a proposed c is compatible exactly when osc(y-m(c)) <= 2eta. Thus an instance can be tested without estimating b first: enumerate the feasible high-count candidates satisfying this condition and report whether their high vectors agree. This is a separate *observation-specific* test, not the uniform eta*.

## R64.2 Small exact integer-lattice search, without pairs of histograms

Let a_d=c_d-c'_d for degrees d=2,...,D. Write P_+=sum_{d=2}^D max(a_d,0), P_-=sum_{d=2}^D max(-a_d,0). Define, for t=2,...,D,
\[
z_1=0,\qquad
z_t=\sum_{d=2}^{D} a_d(d^t-d).
\]

**Theorem.** A nonzero high vector a is realizable as the high-degree difference of two p-Port histograms if and only if max(P_+,P_-) <= p. Its minimal necessary Port population is exactly max(P_+,P_-). Furthermore osc(Delta)=osc(z), and therefore
\[
\boxed{\eta_{p,D}^{*}=\frac14
\min_{\substack{a\in\mathbb Z^{D-1}\setminus\{0\}\\
\max(P_+,P_-)\le p}}
\bigl(\max(0,z_2,\ldots,z_D)-\min(0,z_2,\ldots,z_D)\bigr).}
\]
This is a finite, constructive, exact algorithm: each |a_d| <= p and every tested high difference is globally feasible. It avoids enumerating pairs of degree histograms.

Proof: Since the two populations each equal p, a_0+a_1=-sum_{d>=2}a_d. The minimal possible low-degree l1 mass |a_0|+|a_1| equals |sum_{d>=2}a_d|, attained by assigning all compensating mass to either degree 0 or degree 1. The total positive and negative counts of the resulting full difference are both max(P_+,P_-); adding the same degree-zero count to both models extends any witness to p. Conversely each histogram must contain at least P_+ and P_- Ports respectively. Finally, Delta_t-Delta_1 is precisely z_t because the degree-zero term vanishes and the degree-one term is the same for every positive t; subtracting a constant preserves oscillation.

R63's Stirling-binomial observer immediately gives the universal lower bound eta* >= 1/2: for a nonzero high difference, at least one integer B_k changes by a nonzero integer. Each B_k is a zero-sum linear form in the positive moments with total positive coefficient mass 1/2 and negative coefficient mass 1/2, hence |Delta B_k| <= osc(Delta)/2. Thus osc(Delta)>=2. The finite algorithm can yield a *strictly larger* threshold.

## R64.3 Complete D=2,3 classifications

At D=2 and every p>=2, choose a_2=1. Then z=(0,2), and the universal lower bound is attained:
\[
\boxed{\eta^*_{p,2}=\tfrac12,\quad p\ge2.}
\]

For D=3 set a=a_2, b=a_3. The two nontrivial difference coordinates are
\[
z_2=2a+6b,\qquad z_3=6a+24b=6(a+4b).
\]
For p=3, z_3=0 would force a=-4b, requiring at least 4|b| Ports unless (a,b)=(0,0). Therefore every nonzero feasible difference has |z_3|>=6 and osc(z)>=6. Equality is attained at (a,b)=(-3,1), which requires exactly 3 Ports. For every p>=4, a=(-4,1) requires 4 Ports and gives (z_1,z_2,z_3)=(0,-2,0), attaining the universal lower bound:
\[
\boxed{\eta^*_{3,3}=\tfrac32,\qquad
\eta^*_{p,3}=\tfrac12\ (p\ge4).}
\]

The p=3 witness compares histograms (c_0,c_1,c_2,c_3)=(2,0,0,1) versus (0,0,3,0); their normalized star moments are (3,9,27) and (6,12,24), giving oscillation 6. The p=4 witness compares (3,0,0,1) against (0,0,4,0); normalized star moments are (3,9,27) and (8,16,32), with differences (-5,-7,-5), oscillation 2.

## R64.4 Exact D=4 finite classification and witnesses

The companion deterministic integer enumeration covers every a_2,a_3,a_4 with |a_d|<=p and max(P_+,P_-)<=p. It gives the following *author-verified finite* values:
\[
\eta_{4,4}^*=\tfrac{14}{4}=\tfrac72;\quad
\eta_{p,4}^*=\tfrac{12}{4}=3\ (5\le p\le10);\quad
\eta_{p,4}^*=\tfrac{2}{4}=\tfrac12\ (p\ge11).
\]
The last extension to all p>=11 is analytic: the explicit vector (a_2,a_3,a_4)=(-10,5,-1) requires 11 Ports and gives z=(0,-2,0,-2), while the universal lower bound remains 2. For p=4 the finite search has 308 feasible nonzero high vectors and minimum oscillation 14; for p=5,...,10 the counts are 560,922,1414,2056,2868,3870 with minimum 12. The verifier additionally checks an independent complete histogram-pair search for D<=4,p<=4.

D=5, p=5,...,8 was also exhaustively checked, yielding oscillation 30 (eta*=15/2) in that stated finite range; no general D=5 formula is claimed.

## Verification, scientific boundary and next work

Companion executable source: research_notes/portable_direct/x6_r64_shared_bias_minimax_verify.js
Companion result: research_notes/portable_direct/x6_r64_shared_bias_minimax_results.json

Exact bounded arithmetic uses integers within JavaScript's safe-integer range and no floating-point approximation to the combinatorial quantities; all assertions PASS. D=2 p=2..8, D=3 p=3..8, D=4 p=4..11 and D=5 p=5..8 are covered. The general lattice identity and D=2,3 conclusions have complete algebraic/combination proofs above; D=4 small-population values additionally depend on disclosed exhaustive finite enumeration. This is author evidence, not independent mathematical review.

These observers intentionally discard raw Cell/Link incidence only for the stated high-degree histogram target, and that quotient has not been proved safe for later native operations. No physical temporal step, reset mechanism, TRIADIC_CLOSURE_E native event mapping or generic native dynamics inference is supplied by this conditional observer theorem.

Further work: (1) determine D>=5 sharp p-dependent thresholds and shorter certificates; (2) quantify heterogeneous channel error budgets and biased raw masses, where normalization makes the bias direction unequal across t; (3) test a typed frozen-P000 native Cell/Link/Port repeated-reset interface rather than assuming its existence.
