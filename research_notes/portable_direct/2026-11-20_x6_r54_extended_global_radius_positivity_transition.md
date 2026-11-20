# X6 R54 — Global sharpness of the positive BRC Port-ambiguity radius up to its algebraic transition

Date: 2026-11-20 (Asia/Shanghai).
Line: RS-X6-NATIVE-TIME-DYNAMICS. Historical researcher: EM-X6-214D9C.
Activity: RA-545183ADD4EF71C3E4698AEE.
Status: CONDITIONAL_AUTHOR_PROOF / EXACT_BRC_SHORT_WORD_CHECK / NOT_INDEPENDENTLY_REVIEWED.

## Fixed hypotheses

We reuse the R44–R53 *conditional* named A_i/B_i, once-only whole-triad BRC branch grammar, with proposed release R and reoccupation T. The root observer maps each A_i/B_i to F while retaining R and T; the readout counts *positive BRC path masses*, not signed amplitudes or full provenance. For strictly positive weights alpha,beta, S=alpha+beta, P=alpha*beta, the four observations of (F,FT,FF,FRF) are

\[
A_p(S,P)=(pS,(p-1)S,2(p^2-1)P,2pP).
\]

Every model may add an arbitrary common real bias b; each channel then has its own error bounded in absolute value by eta. Two models are ambiguous exactly when their common-bias-shifted mass vectors have L-infinity distance at most 2eta.

Fix the true p=4, S=1 and 0<P<=1/4 (the true weights are positive roots of u²-u+P). Thus V=(4,3,30P,8P). Define

\[
\rho=\frac{7601-100\sqrt{5497}}{882}=0.21181903443992\ldots,\quad
r(P)=\frac{19+42P}{400}.
\]

## R54 theorem

**For every real 0<P<=rho, the exact global ambiguity radius against every integer q>=1, q!=4, arbitrary strictly positive competing weights and common offsets is**

\[
\boxed{\eta_{\mathrm{crit}}(P)=r(P)=(19+42P)/400.}
\]

For eta<r(P) the four observations identify p=4 uniquely; at equality a strictly positive q=5 model is simultaneously compatible. R53 established this on [19/2158,79/378); R54 extends it to the entire initial interval (0,rho], including the full low-product region and the algebraic endpoint.

**Sharpness phase transition.** For rho<P<=1/4 the same q=5 contrast lower bound r(P) cannot be attained by an admissible positive-weight q=5 model, and the actual global ambiguity radius is strictly greater than r(P). The exact higher-region radius is left open.

## Proof 1 — rigorous global exclusions, with no q cutoff

For any q>=1 define C_q=q²-q-1 and the common-offset-annihilating BRC contrast

\[
L_q(x,y,d,h)=(d-h)-C_q((x-y)-(x-h)/q).
\]

The exact q-model always satisfies L_q=0. For q>=2 its coefficient L1 norm is N_q=2q(q-1); since the observation is eta-close to both model vectors,

\[
\eta\ge B_q(P)=\frac{|4-q|[C_q+2P(4q+1)]}{4q^2(q-1)}.
\]

For q=5, B_5(P)=r(P). For q=2 and 3,

\[
B_2(P)=(1+18P)/8>r(P),\qquad
B_3(P)=(5+26P)/72>r(P),
\]

where the gaps are (31+858P)/400 and (632+7376P)/28800, respectively. For every integer q>=6,

\[
B_q(P)\ge g(q)=\frac{(q-4)(q^2-q-1)}{4q^2(q-1)}\ge g(6)=29/360.
\]

Indeed the exact increment is
\[
g(q+1)-g(q)=\frac{(q+2)(2q^2-3q-1)}{2q^2(q-1)(q+1)^2}>0
\]
for q>=6. Since P<=rho<1/4, r(P)<59/800<29/360.

For q=1 we use two *different* observational differences, avoiding R53's conservative low-product cutoff. Set P_0=19/2158. If 0<P<P_0, the q=1 model has Y=D=b, while true Y-D=3-30P. Hence overlapping radius-eta boxes would require |3-30P|<=4eta. But P<P_0<281/3042 implies (3-30P)/4>r(P), excluding q=1 at eta<=r(P).

If P>=P_0, true D-H=22P, while the positive q=1 model has D-H=-2P_1 with P_1>0. Overlap requires 4eta>=22P+2P_1 and therefore eta>11P/2>=r(P). Thus q=1 is also excluded at and below r(P). These cases exhaust all rivals except q=5. In particular all eta<r(P) admit no rival.

## Proof 2 — explicit positive q=5 realization, including rho

Set
\[
S_5=(81-42P)/100,\quad P_5=(1+118P)/200,\quad
b_5=(378P-29)/200.
\]

The candidate weights exist and are strictly positive precisely when S_5,P_5>0 and S_5²>=4P_5. Their discriminant is

\[
S_5^2-4P_5=\frac{1764P^2-30404P+6361}{10000}.
\]

The numerator is strictly decreasing on [0,1/4], starts positive, and has its unique root rho in (0,1/4). Hence it is nonnegative throughout 0<P<=rho. At the endpoint rho, the two candidate weights coincide but remain strictly positive.

Let W=A_5(S_5,P_5)+b_5(1,1,1,1). Direct substitution gives

\[
V-W=2r(P)(1,-1,-1,1).
\]

The midpoint z=(V+W)/2 lies within distance r(P) of both positive-weight models. Thus the lower bound is sharp, including rho. QED.

## Proof 3 — no equality above the discriminant root

For q=5, equality at eta=r(P) in the L1 contrast estimate forces all four differences V-W to saturate at 2r(P) with the unique signs (+,-,-,+): none of the four contrast coefficients vanishes. The three candidate parameters S_5,P_5,b_5 are then uniquely fixed by W=A_5(S_5,P_5)+b_5 1, giving exactly the formulas above. For rho<P<=1/4 their discriminant is negative, so the required source weights do not exist.

Every other q has a strict gap above r(P) by Proof 1 (for q=1 the D-H gap applies). For q=5, any hypothetical sequence of feasible rival parameters with radii tending to r(P) has bounded observed masses, hence bounded S_5 from X-Y, P_5 from D-H, and b_5 from Y. A convergent subsequence would yield a nonnegative-discriminant solution attaining r(P), contradicting the unique negative-discriminant candidate. The uniform q>=6 contrast gap precludes escape to unbounded q. Therefore the global ambiguity radius is strictly greater than r(P) when rho<P<=1/4. QED.

## Verification and preserved boundary

Verifier: research_notes/portable_direct/x6_r54_extended_global_ambiguity_verify.js
Results: research_notes/portable_direct/x6_r54_extended_global_ambiguity_results.json

The verifier independently enumerates the named R44 candidate BRC Port transitions and exact positive path masses for F/FT/FF/FRF, checks witness equalities and rational bounds, and brackets the irrational root by exact rational signs. Finite enumeration supports the stated author proof; the unbounded-q exclusion is algebraic. The result is for the declared positive path-mass observer only. Frozen P000 V5 and ACTIVE six-dimensional Heartbeat World are unchanged. Full native TRIADIC_CLOSURE_E Cell/Link/named-Port R/T event admission and phase-preserving correspondence are still open; no Result, formal PROGRESS or independent Review is claimed.

Next mathematical objective: determine the constrained Chebyshev minimizer and the exact radius for rho<P<=1/4, possibly when the q=5 positivity boundary becomes active; independently establish a fully admitted native triad mapping with preserved provenance before any physical-time attribution.

Lineage: R44 candidate named-branch verifier; R47 four-word BRC masses; R51 corrected contrast norm; R52 exact instance; R53 parametric interval. R53 exact file: research_notes/portable_direct/2026-11-20_x6_r53_parametric_global_ambiguity_interval.md.
