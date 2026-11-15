# Fixed-budget parameter reentrance in source-labelled BRC N=4 / S23 Chernoff sampling

Date 2026-11-04. Author analytic proof with exact rational arithmetic verification; UNREVIEWED / NOT_ADMITTED. Frozen scientific source: awdawmip/enterprise-math@43ec6098b1330ae86d0a7863be336c5d97f6ef34. Follows exact all-K s=1/9 author analysis in PR #1765 at commit 3b717ebf5b6d09c9b84aed20a82bb6d90f405b69.

## Model and exact result

Set h=1/42, 0<s<1, a=s(1/2+h), b=s(1/2-h). The three-point source-retaining T experiment has P=(a,1-s,b), Q=(b,1-s,a). The coarse Bernoulli B experiment has P=(a,1-a), Q=(b,1-b). One T costs c=2-s and one B costs 1. For X=T,B let f_X(t)=-log(sum P_X(y)^t Q_X(y)^(1-t)) and C_X=max_{t in [0,1]} f_X(t). A mixed allocation (m,n) has information max_t[m f_T(t)+n f_B(t)] using the same t for all observations. Only m,n nonnegative integers with c*m+n<=17 are feasible.

**Theorem (three exact parameter witnesses).** At the fixed integer budget K=17, each of the following has a unique Chernoff-optimal allocation:

| parameter | s exactly | unique optimal (m T,n B) |
| --- | --- | --- |
| left | 1/9-1/1000000 = 999991/9000000 | (0,17) |
| near_right | 1/9+1/1000000 = 1000009/9000000 | (9,0) |
| far_right | 1/9+1/100000 = 100009/900000 | (0,17) |

In particular, the integer optimal policy is not two-sided locally constant at s=1/9. Within the closed interval from near_right to far_right, a transition between the pure-T and pure-B regimes occurs (by continuity of 9C_T(s)-17C_B(s)). No uniqueness claim for the transition parameter is made.

## Exact analytic reduction

T is symmetric under swapping first and last labels, hence its unique maximizing exponent is t=1/2 and

C_T=-log(1-s+2 sqrt(ab)).

Set E=C_T-(2-s)C_B. For each of the three parameter witnesses, the accompanying Fraction program gives strict **rational interval** certificates

C_B > 1/100000, E < 1/100000000, 8 E < C_B/10.

At all three points, 10T exceeds budget 17. For every 1<=m<=8, take n<=floor(17-(2-s)m) and let u=17-(2-s)m-n. Since (2-s)=17/9 +/- epsilon where epsilon=1/10^6 or 1/10^5, the fractional unused budget at maximal n is

u_min = m/9 +/- m epsilon

with both sign choices occurring across the three parameter values. For 1<=m<=8 this is strictly >1/10 and <1. A smaller n only increases u. Consequently, using the common-exponent Chernoff upper bound,

C(m,n) <= m C_T+n C_B = 17 C_B + m E-u C_B
         <=17 C_B+8E-C_B/10 <17 C_B.

If m=0, n=17 uniquely maximizes information among pure B configurations because C_B>0.

For left s, 9c>17, so no m>=9 is feasible. Thus (0,17) is uniquely optimal.

For the two right-hand s values, 9c=17-9epsilon lies strictly between 16 and 17; therefore the only additional feasible allocation with m>=9 is (9,0). The exact program encloses the decisive difference 9C_T-17C_B in the following strict rational intervals (the decimal endpoints are rounded OUTWARDS for display; the program compares Fractions):

- near_right: [5.28300454e-9, 5.28300456e-9], strictly positive;
- far_right: [-1.16535064e-10, -1.16535059e-10], strictly negative.

The stated unique optimal allocations follow. QED.

## Why the finite interval certificate encloses the true maximizers

Write U=sqrt(ab), V=sqrt((1-a)(1-b)), l1=log(a/b), l2=log((1-a)/(1-b)), Delta=l1-l2. For a rational delta=37375/10^7 and t0=1/2+delta,

Z_B(t0)=U exp(delta*l1)+V exp(delta*l2),
f_B(t0)=-log Z_B(t0),
f_B'(t0)=-(U exp(delta*l1)*l1+V exp(delta*l2)*l2)/Z_B(t0).

B's curvature is -f_B''(t)=w(t)(1-w(t))*Delta^2 where w(t) lies in [b,a], hence -f_B''(t)>=b(1-a)Delta^2 =: m_B>0. Global strong concavity yields the rigorous enclosure

f_B(t0) <= C_B <= f_B(t0)+[f_B'(t0)]^2/(2 m_B).

The verifier constructs rational outward intervals for square roots with isqrt and grid 10^32; logarithms use log(x)=2 sum_{j=0}^{N-1} y^(2j+1)/(2j+1)+R for y=(x-1)/(x+1), |R|<=2|y|^(2N+1)/((2N+1)(1-y^2)), N=13; exponentials on |x|<1/100 use the degree-9 Taylor polynomial with remainder <=3|x|^10/10!. Each operation rounds outward to the 10^(-32) rational grid. The script verifies all input conditions and decisive signs with exact Fraction comparisons; its floats are display only.

## Scope and next problem

This result concerns the frozen two-experiment source-labelled classical Chernoff information model at integer budget 17, h=1/42, at three exact rational values of s. It is an independently reproducible author-side local result. This comparison does not invoke native BRC–Shor arithmetic or change P000. The ten-label S23 minimax mother objective remains in its recorded open bracket [1/2,2/3].

Next determine the exact transition s* in (1/9+1/10^6,1/9+1/10^5) where 9C_T=17C_B, and determine whether the difference is strictly monotone in that interval. More broadly, classify how the budget-residue endpoint theorem changes when the rational cost denominator jumps at nearby s. Preserve frozen scientific pins and the single common Chernoff exponent.
