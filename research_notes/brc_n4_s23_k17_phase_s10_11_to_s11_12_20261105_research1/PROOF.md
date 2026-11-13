# Exact BRC S23 auxiliary Chernoff phase: K=17, 10/11 ≤ s ≤ 11/12

Date: 2026-11-05. **AUTHOR_ANALYTIC_PROOF / EXACT_RATIONAL_EXECUTED / UNREVIEWED / NOT_ADMITTED**.
Frozen science pin `43ec6098b1330ae86d0a7863be336c5d97f6ef34`. Prior frontier `41c51ae8ee270d0ca4376f15f648fb7aa651f5e6`.

## Complete theorem

Put a=11/21, b=10/21. T is the source-preserving three-label experiment P=(as,1-s,bs), Q=(bs,1-s,as), while B is the *different*, explicitly projected Bernoulli experiment P_B=(as,1-as), Q_B=(bs,1-bs). Costs are 2-s for T and 1 for B. For common tilt t∈[0,1] define

f_T(t,s)=-log(1-s+s[a^t b^(1-t)+b^t a^(1-t)]),
f_B(t,s)=-log[(as)^t(bs)^(1-t)+(1-as)^t(1-bs)^(1-t)],
F(m,n;s)=max_t(m f_T+n f_B), C_T=F(1,0;s), C_B=F(0,1;s).

Counts m,n are nonnegative integers with (2-s)m+n≤17. There is one and only one transition α with **9092/10000<α<9093/10000**. All global optimizer sets are:
* 10/11≤s<α: only **11T+5B**.
* s=α: exactly **11T+5B and 17B**.
* α<s<11/12: only **17B**.
* s=11/12: only **12T+4B**.

## Exhaustive feasible lattice-hull proof

For each feasible T count m, the best B count is n_m=17-2m+floor(ms), since B has strictly positive Chernoff information. Enumerate k/m for 1≤m≤17, 0≤k≤m in [10/11,11/12]; the only breakpoints are the two interval endpoints. Exact integer cross-products give upper hull vertices (0,17),(11,5),(15,0) throughout [10/11,11/12), and (0,17),(12,4),(15,0) at 11/12. The verifier enumerates all filled feasible points and tests the hull exactly.

F is convex as a function of (m,n), being the supremum of affine functions, so an integer maximizer cannot exceed all upper-hull vertices. The displacement vectors of all upper-hull edges are primitive: (11,-12),(4,-5),(12,-13),(3,-4) have gcd 1. Thus there is no additional lattice count inside these upper edges. A strict best vertex gives a unique count optimizer; equality of the first two vertices gives exactly those two integer optimizers.

## Closed-form bounds and continuum proof

Set H(s)=f_B(1/2,s). Reflection symmetry gives C_T=-log(1-s+2s√(ab)), and H=-log[s√(ab)+√((1-as)(1-bs))]. With L=log(a/b), J=log((1-bs)/(1-as)), ρ=J/(L+J), C_B=D_Bernoulli(ρ || as). For any nonnegative m,n,

m C_T+n H ≤ F(m,n;s) ≤ m C_T+n C_B.

For each fixed t, f_T is convex in s (negative log of a positive affine expression). The B overlap is concave in s, since its first term is affine and its second is a positive weighted geometric mean of positive affine functions, hence f_B is convex; maxima over t preserve convexity. Thus F and C_B are convex in s. Let G=F(11,5;s)-17C_B(s) and D=17C_B(s)-15C_T(s).

Split the full interval [10/11,11/12] into 16 rational cells [x,y], with δ=1/10000. For almost every z∈[x,y], convexity and the preceding upper/lower bounds give

F'(11,5;z) ≤ [11C_T(y+δ)+5C_B(y+δ)-11C_T(y)-5H(y)]/δ,
C_B'(z) ≥ [C_B(x)-C_B(x-δ)]/δ,
C_T'(z) ≤ [C_T(y+δ)-C_T(y)]/δ.

VERIFY.py establishes *both* strict inequalities for *all 16* cells:

17[C_B(x)-C_B(x-δ)] > 11[C_T(y+δ)-C_T(y)]+5[C_B(y+δ)-H(y)],
17[C_B(x)-C_B(x-δ)] > 15[C_T(y+δ)-C_T(y)].

Consequently G is strictly decreasing and D strictly increasing **on all real parameters** in the interval, not merely the 16 tested points.

The verifier proves six further rigorous endpoint/crossing signs:
(1) 11C_T(10/11)+5H(10/11)>17C_B(10/11);
(2) 17C_B(10/11)>15C_T(10/11);
(3) 11C_T(9092/10000)+5H(9092/10000)>17C_B(9092/10000);
(4) 17C_B(9093/10000)>11C_T(9093/10000)+5C_B(9093/10000);
(5) 12C_T(11/12)+4H(11/12)>17C_B(11/12);
(6) 12C_T(11/12)+4H(11/12)>15C_T(11/12).

Signs (1,3,4) and strict decrease of continuous G give the unique α and exact two-way tie. Sign (2), then D strictly increasing, excludes 15T throughout the open interval. Signs (5,6) prove 12T+4B is the unique right-end optimizer. Combined with primitive lattice edges these exhaust every feasible integer configuration.

## Strict source/projection loss (independent typed observer lemma)

B merges two T labels; it is **not** a lossless replacement. For 0<t<1, 0<s<1, strict weighted-geometric-mean superadditivity yields

((1-s)+bs)^t((1-s)+as)^(1-t) > (1-s)+(bs)^t(as)^(1-t).

Therefore B's Chernoff overlap exceeds T's at the same tilt, and f_B(t,s)<f_T(t,s). The T/B cost advantage and information loss are separate typed variables. The present auxiliary continuum s,t is a declared analytical readout of the finite-alphabet experiment; it is not an extra native spatial dimension or an identification with the P000 Heartbeat World state.

## Reproducibility and scope

Run `python VERIFY.py` with Python 3 standard library. `RUN_EVIDENCE.txt` contains 38 strict-rational assertion results (32 real-continuum monotonicity certificates, six point signs) plus the exact lattice hull test. The verifier uses Fraction, isqrt, 10^36 outward-root brackets and 34 atanh log terms with rigorous remainder 2|v|^69/[69(1-v²)] for |v|<1/3. No float enters any assertion; all signs are rigorous. Author-side scope only, pending independent mathematical review and formal native Result acceptance. The original ten-label S23 minimax mother risk interval [1/2,2/3] remains open: no numerical Chernoff-to-decision-risk bridge has been assumed.
