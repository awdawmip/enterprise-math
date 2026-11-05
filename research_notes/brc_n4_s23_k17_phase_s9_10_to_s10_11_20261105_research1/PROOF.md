# Exact BRC S23 N=4, K=17 phase: 9/10 ≤ s ≤ 10/11

Date: 2026-11-05. **Author-side exact analytic proof / executed rational certificates / unreviewed / not admitted.**
Frozen scientific input: `43ec6098b1330ae86d0a7863be336c5d97f6ef34`.
Previous immutable frontier: `d567fa97bab9c42add162ac8f7490614b424371d`.

## Precise experiment and theorem

Set a=11/21, b=10/21. The complete three-label T source has competing distributions (as,1-s,bs) and (bs,1-s,as); B is the Bernoulli projection (as,1-as) and (bs,1-bs). These are separate typed observers with source/projection provenance retained. One T costs 2-s, one B costs 1. For a single common Chernoff tilt 0≤t≤1 let

f_T(t,s) = -log(1-s+s[a^t b^(1-t)+b^t a^(1-t)]),
f_B(t,s) = -log[(as)^t(bs)^(1-t)+(1-as)^t(1-bs)^(1-t)],
F(m,n;s)=max_{0≤t≤1}(m f_T(t,s)+n f_B(t,s)).

Write C_T=F(1,0;s), C_B=F(0,1;s), and H=f_B(1/2,s). All optimizations below range over integers m,n≥0 with (2-s)m+n≤17.

**Theorem.** A unique α exists with **9001/10000<α<9002/10000**. The complete global optimizer set over the real interval [9/10,10/11] is exactly:
- 9/10≤s<α: 10T+6B only;
- s=α: 10T+6B and 17B only;
- α<s<10/11: 17B only;
- s=10/11: 11T+5B only.

## Feasible-count and upper-hull exhaustion

For every feasible integer T count m, positive B information implies that the best feasible B count is n_m=17-2m+⌊ms⌋. All integer-cost changes in this interval belong to k/m for 1≤m≤17 and 0≤k≤m; exact Fraction enumeration shows that the **only** such breakpoints in the closed interval are 9/10 and 10/11.

On 9/10≤s<10/11, the upper convex hull of all maximally filled count pairs has vertices (0,17),(10,6),(15,0). At the right endpoint, its vertices are (0,17),(11,5),(15,0). This is proved by rational cross-product tests in VERIFY.py; the feasible count list stays constant on the open interval.

For fixed t the count dependence of m f_T+n f_B is affine. Its supremum F is convex in (m,n); thus no feasible point can outperform all upper-hull vertices. The upper boundary is relevant because f_T,f_B≥0 and B information is strictly positive for 0<s<1. Hull edge integer vectors (10,-11),(5,-6) on the left and (11,-12),(4,-5) on the right are primitive (gcd=1). Therefore there are no other feasible integer points on the relative interiors of these upper edges, ruling out unlisted ties once the vertex comparisons are strict or exactly two-way.

## Continuous strict monotonicity, 38 exact rational signs

The T experiment is symmetric, hence
C_T(s)=-log(1-s+2s√(ab)).
The explicit half-tilt B information is
H(s)=-log[s√(ab)+√((1-as)(1-bs))].
For B set L=log(a/b), J=log((1-bs)/(1-as)), ρ=J/(L+J); then C_B(s)=D_Bernoulli(ρ || as). Its closed expression is evaluated using rigorous rational intervals. For all m,n:
m C_T+n H ≤ F(m,n;s) ≤ m C_T+n C_B.

For each fixed t, f_T is convex in s because it is minus the log of a positive affine function. The first summand inside exp(-f_B) is linear in s; the second is a positively weighted geometric mean of positive affine functions, hence concave. Minus log of their positive concave sum is convex. Thus f_B, F and C_B are convex in s.

Define G(s)=F(10,6;s)-17 C_B(s), D(s)=17 C_B(s)-15 C_T(s). Partition [9/10,10/11] into 16 closed rational subintervals [x,y] and use δ=1/10000. At almost every z in [x,y] convexity gives

F'(10,6;z) ≤ {10 C_T(y+δ)+6 C_B(y+δ) -10 C_T(y)-6 H(y)}/δ,
C_B'(z) ≥ {C_B(x)-C_B(x-δ)}/δ,
C_T'(z) ≤ {C_T(y+δ)-C_T(y)}/δ.

The verifier proves all 16 strict inequalities

17[C_B(x)-C_B(x-δ)] > 10[C_T(y+δ)-C_T(y)]+6[C_B(y+δ)-H(y)]

and all 16 strict inequalities

17[C_B(x)-C_B(x-δ)] >15[C_T(y+δ)-C_T(y)].

Consequently G is strictly decreasing and D strictly increasing throughout the real interval, not merely on the tested rational grid.

Six further exact inequalities are checked:
1. 10 C_T(9/10)+6 H(9/10)>17 C_B(9/10).
2. 17 C_B(9/10)>15 C_T(9/10).
3. 10 C_T(9001/10000)+6 H(9001/10000)>17 C_B(9001/10000).
4. 17 C_B(9002/10000)>10 C_T(9002/10000)+6 C_B(9002/10000).
5. 11 C_T(10/11)+5 H(10/11)>17 C_B(10/11).
6. 11 C_T(10/11)+5 H(10/11)>15 C_T(10/11).

Signs (1,3,4) plus continuity and strict G decrease prove the single crossing α; sign (2) plus increasing D excludes 15T on the whole interval; signs (5,6) prove the right endpoint jump to 11T+5B. Primitivity of hull edges excludes every additional integer tie.

## Exact arithmetic and evidence scope

VERIFY.py uses Python Fraction and isqrt, square-root outward brackets at scale 10^36, and 34-term atanh logarithms with rigorous tail 2|v|^69/[69(1-v²)], |v|<1/3, all interval operations rounded outward when quantized. It executes 32 strict real-monotonicity enclosures and six endpoint/crossing strict signs, plus exact finite feasible-set/hull checks. RUN_EVIDENCE.txt is the recorded local execution output. It proves the stated continuum result under the declared auxiliary model; independent review and native acceptance remain pending.

The original ten-label S23 minimax remains a separate mother question with the previously recorded risk enclosure [1/2,2/3]. The T/B Chernoff model is an auxiliary projected observer; no unproven risk bridge is assumed.
