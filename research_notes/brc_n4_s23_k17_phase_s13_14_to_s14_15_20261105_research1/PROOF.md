# BRC N=4 S23 K=17 T/B auxiliary phase: exact global integer optimizer on [13/14,14/15]

Date: 2026-11-05. Status: AUTHOR_ANALYTIC_PROOF / EXACT_RATIONAL_EXECUTED / UNREVIEWED / NOT_ADMITTED.
Scientific source is frozen to `43ec6098b1330ae86d0a7863be336c5d97f6ef34`. Parent proof: `c800088b125a572def37d6e1565cd615e9890839` (12/13 to 13/14). This is the typed auxiliary observation optimization, not a promoted ten-label S23 minimax result.

## Exact experiment and optimization problem

Let a=11/21, b=10/21, s in [13/14,14/15]. Complete source readout T has distributions P_T=(as,1-s,bs) and Q_T=(bs,1-s,as). The coarser B readout has P_B=(as,1-as) and Q_B=(bs,1-bs). The projection T -> B merges two T labels; they are distinct observers.

Define f_T(t,s)=-ln[1-s+s(a^t b^(1-t)+b^t a^(1-t))] and f_B(t,s)=-ln[(as)^t(bs)^(1-t)+(1-as)^t(1-bs)^(1-t)]. The mixed Chernoff tilt t in [0,1] is COMMON to every sample. Let F(m,n;s)=max_t (m f_T(t,s)+n f_B(t,s)) and C_T=F(1,0;s), C_B=F(0,1;s), H=f_B(1/2,s). Maximize F over integer m,n>=0 with (2-s)m+n<=17.

## Theorem

There is exactly one alpha with **92867/100000 < alpha < 92869/100000**. The complete integer argmax on the REAL continuum is:

* 13/14 <= s < alpha: (m,n)=(14,2), uniquely.
* s=alpha: precisely (14,2) and (0,17).
* alpha < s < 14/15: (0,17), uniquely.
* s=14/15: (15,1), uniquely.

Numerical orientation alpha approximately 0.92867792658 (not part of the proof).

## Exact cost hull

For fixed m, positive B information makes n_m=17-2m+floor(ms) optimal among the permitted n. Exhaustive rational k/m enumeration, m=1,...,17, gives no interior breakpoint: only 13/14 and 14/15 lie in the closed interval. The non-endpoint chamber [13/14,14/15) has upper-hull vertices (0,17),(14,2),(15,0); at s=14/15 the upper hull is (0,17),(15,1). All hull edges are primitive: differences (14,-15),(1,-2),(15,-16). Since F is a supremum of affine functions in (m,n), a maximum over integer feasible points is achieved at the upper-hull vertices, while primitive edges exclude additional integer optimizers in a two-vertex tie. Strict positivity of f_T,f_B at interior tilts excludes smaller n.

## Certified continuum comparison

Set u=s sqrt(ab), L=ln(a/b), J=ln((1-bs)/(1-as)), rho=J/(L+J). Then

C_T=-ln(1-s+2u), H=-ln(u+sqrt((1-as)(1-bs))),
C_B=rho ln(rho/(as))+(1-rho)ln((1-rho)/(1-as)).

The formula for C_B follows from the Bernoulli Chernoff minimizer's equal-KL condition. For all s, 14 C_T+2 H <= F(14,2;s) <= 14 C_T+2 C_B.

For every fixed tilt t, the T overlap is affine positive in s; the B overlap is concave positive in s as a weighted geometric mean. Thus f_T,f_B and F are convex in s; C_T,C_B also are.

Define G(s)=F(14,2;s)-17 C_B(s), D(s)=17 C_B(s)-15 C_T(s). Subdivide [13/14,14/15] into 16 equal rational cells [x,y], let delta=1/10000. Convexity and the bounds above yield, for every interior derivative point z in each cell,

F'(14,2;z) <= [14 C_T(y+delta)+2 C_B(y+delta)-14 C_T(y)-2 H(y)]/delta,
C_B'(z) >= [C_B(x)-C_B(x-delta)]/delta,
C_T'(z) <= [C_T(y+delta)-C_T(y)]/delta.

The executable rational checker proves for EVERY cell

17 [C_B(x)-C_B(x-delta)] > 14 [C_T(y+delta)-C_T(y)]+2 [C_B(y+delta)-H(y)],
17 [C_B(x)-C_B(x-delta)] > 15 [C_T(y+delta)-C_T(y)].

Thus G strictly decreases and D strictly increases over the entire real interval, including between grid nodes.

The checker also proves these six strict endpoint/bracketing signs:

(1) 14 C_T(13/14)+2H(13/14)>17 C_B(13/14);
(2) 17 C_B(13/14)>15 C_T(13/14);
(3) 14 C_T(0.92867)+2H(0.92867)>17 C_B(0.92867);
(4) 17 C_B(0.92869)>14 C_T(0.92869)+2C_B(0.92869);
(5) 15 C_T(14/15)+H(14/15)>17 C_B(14/15);
(6) 15 C_T(14/15)+H(14/15)>14 C_T(14/15)+2C_B(14/15).

Continuity plus G monotonicity proves the unique alpha and exact tie; D>0 excludes (15,0) throughout the open chamber. At right, (15,1) beats (0,17) and hence is unique.

## Mathematical and computational verification scope

The self-contained `VERIFY.py` applies Fraction, integer isqrt, 1e36 outward-rounded square-root bounds and the exact atanh logarithm series (34 terms) with remainder <= 2 |v|^69/[69(1-v^2)] for |v|<1/3. It checks 16+16 strict cell-wise bounds and six strict signs (=38), complete rational cost-breakpoint enumeration and exact convex hull. `RUN_EVIDENCE.txt` transcribes observed stdout from the locally executed equivalent typeset version; published checker has identical mathematical expressions, parameters, assertions and error bounds. Formal independent review remains open.

The original ten-label S23 minimax risk bracket [1/2,2/3] remains the mother objective. A provenance-preserving encoder/decoder risk inequality is the next bridge.

Next interval: [14/15,15/16], starting at (15,1); also prioritize exact ten-label risk bridge rather than indefinitely extending only auxiliary parameter intervals.
