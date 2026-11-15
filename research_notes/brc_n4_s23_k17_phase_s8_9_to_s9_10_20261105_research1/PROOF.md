# BRC N=4, S23 K=17: exact Chernoff design phase over 8/9 <= s <= 9/10

Date: 2026-11-05. Science input frozen at 43ec6098b1330ae86d0a7863be336c5d97f6ef34. Status: AUTHOR_ANALYTIC_PROOF / EXACT_RATIONAL_EXECUTED / UNREVIEWED / NOT_ADMITTED. Previous author-side phase: c34bb3e8357feb794dc09d27cc07dd5819f9c0f7.

## Model and theorem

Let a=11/21,b=10/21. The three-label T experiment has laws (as,1-s,bs) versus (bs,1-s,as); the Bernoulli-projected B experiment has laws (as,1-as) versus (bs,1-bs). The two observers are distinct; no source-label sufficiency, original mother-problem equivalence or native-P000 transfer is assumed.

For one common Chernoff tilt 0<=t<=1 define
fT(t,s)=-ln[1-s+s(a^t b^(1-t)+b^t a^(1-t))]
fB(t,s)=-ln[(as)^t(bs)^(1-t)+(1-as)^t(1-bs)^(1-t)]
F(m,n;s)=max_t[m fT(t,s)+n fB(t,s)], CT=F(1,0;s), CB=F(0,1;s), H=fB(1/2,s).
Optimize over integers m,n>=0 with (2-s)m+n<=17.

THEOREM: There is exactly one alpha in (88903/100000,88906/100000). The full global optimizer set on the entire real interval [8/9,9/10] is:
- 8/9<=s<alpha: exactly 9T+7B;
- s=alpha: exactly 9T+7B and 17B;
- alpha<s<9/10: exactly 17B;
- s=9/10: exactly 10T+6B.

## Entire feasible set and upper hull (exact integer arithmetic)

Since B is a genuine positive-information channel, the largest n at fixed feasible m is n_m=17-2m+floor(ms); m>17 is infeasible. Every feasible-set change requires a rational cost breakpoint k/m with 1<=m<=17. Exhaustive exact Fraction enumeration within the closed domain yields only 8/9 and 9/10. Upper convex-hull checks for the complete feasible point set give (0,17),(9,7),(15,0) throughout 8/9<=s<9/10 and (0,17),(10,6),(15,0) at s=9/10. F is a supremum of affine functions of (m,n), hence convex in the count vector. An optimal count must be on an upper hull extremum. Strict increase with B count discards all fixed-m counts with smaller n.

## Analytic continuum proof and 38 exact interval certificates

For fixed t, fT(t,s) is minus log of a positive affine function. In fB, the first term of its exponential is affine in s and the second a concave weighted geometric mean of positive affine functions; therefore fB(t,s) is convex in s. The supremum F and CB are convex in s. The symmetry of T implies its optimum t=1/2. For every s:
L(m,n;s)=m CT(s)+n H(s) <= F(m,n;s) <= U(m,n;s)=m CT(s)+n CB(s).

Define G(s)=F(9,7;s)-17CB(s). Split [8/9,9/10] into 16 equal rational cells [x,y], delta=1/10000. At a.e. z in [x,y], convex secant bounds give:
F'(z) <= [U(9,7;y+delta)-L(9,7;y)]/delta;
CB'(z) >= [CB(x)-CB(x-delta)]/delta.
The verifier proves for each of the 16 cells the strict exact inequality
17[CB(x)-CB(x-delta)] > U(9,7;y+delta)-L(9,7;y).
Hence G decreases strictly across every real parameter in the entire interval.

The same 16-cell derivative enclosure proves
17[CB(x)-CB(x-delta)] > 15[CT(y+delta)-CT(y)].
Consequently D(s)=17CB(s)-15CT(s) is strictly increasing. The exact left-end sign 17CB(8/9)>15CT(8/9) excludes the 15T hull vertex on the full interval.

Six further exact signs are established by rational intervals:
(1) 9CT(8/9)+7H(8/9)>17CB(8/9);
(2) 17CB(8/9)>15CT(8/9);
(3) 9CT(88903/100000)+7H(88903/100000)>17CB(88903/100000);
(4) 9CT(88906/100000)<10CB(88906/100000);
(5) 10CT(9/10)+6H(9/10)>17CB(9/10);
(6) 6H(9/10)>5CT(9/10).
Continuity, the first/third/fourth signs and strict G decrease give the exactly one alpha. The last two signs show the newly feasible 10T+6B strictly dominates both other upper hull vertices at 9/10.

Full tie check: upper-hull edge difference vectors are (9,-10),(6,-7) on the left, (10,-11),(5,-6) on the right. The coordinate pairs are coprime, so no other integer point is on the relative interior of any upper hull edge. Every feasible point strictly below such an edge has strictly less F than a convex combination of adjacent vertices at that m, by increasing B count; the convex combination cannot beat the largest vertex. Therefore the listed optimizer set contains all ties, including at alpha.

## Rigorous computation and scope

The Python standard-library verifier computes interval bounds with Fraction and isqrt. The sqrt enclosure uses scale 10^35; 32 terms of the atanh log series have a rigorous remainder 2|v|^65/(65(1-v^2)) for |v|<1/3. The Bernoulli Chernoff optimum is computed via rho=J/(L+J), L=ln(a/b), J=ln[(1-bs)/(1-as)], CB=D(rho||as). Products, divisions and log calls enclose every exact intermediate. There are 16 G, 16 D and 6 endpoint/crossing assertions (38), plus exhaustive integer floor/hull assertions. The executed independent local verifier returned PASS_BRC_S23_K17_PHASE_S8_9_TO_S9_10_EXACT_20261105; its full numerical output is supplied in RUN_EVIDENCE.txt. The deposited verifier is a source-equivalent adaptation of the preceding phase's already published exact routine; arithmetic procedure and assertion parameters match the executed local check, while remote source-byte identity is separately reported when available.

This is an auxiliary two-observer K=17 Chernoff-information optimization theorem. The original ten-label S23 minimax remains independently open on its previously stated bounds [1/2,2/3].
