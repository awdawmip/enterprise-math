# R5 additional exact F-face strip beyond the t≤1/13 full box

Date: 2026-11-08. Classification: AUTHOR_PROVED / EXACT_FRACTION_EXECUTED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY. Frozen seven-node P/Q-BRC source pins unchanged; this is a special-case extension, not yet a full-box extension beyond 1/13.

## Theorem

For all reals

\[
\frac1{13}\le t\le\frac1{12},\qquad 0\le\kappa\le1,\qquad
p=1,\ q=0,\ \theta=1
\]

the lawful FULL_HIST flow

\[
x(t,\kappa)=\left(1,t,1,\frac{13t}{40}+\frac1{80},
 \frac{9\kappa}{40}+\frac t{10},0,\frac t{10}\right)
\]

admits a lawful seedless LR flow \(y(t,\kappa)\) on the **single F face**
\(z'=a'/10,\ v'-z'=9b'/40\), and a nonnegative 7×7 martingale/Blackwell kernel preserving all seven Q/P mass equations and \(T_P,T_Q\). Thus every randomized terminal declaration is four-observer equivalent.

## Exact four-vertex targets

Let \(s=(t-1/13)/(1/12-1/13)\in[0,1]\), \(k=\kappa\). Set

\[
y(t,k)=(1-s)(1-k)Y_{00}+(1-s)kY_{01}
        +s(1-k)Y_{10}+skY_{11}
\]

with coordinates \((g',a',b',u',v',w',z')\):

- \(Y_{00}=(1,41/416,1009/2080,6339/166400,9901/83200,22419/166400,41/4160)\), \(t=1/13,k=0\).
- \(Y_{01}=(1,1/13,1,3/80,121/520,0,1/130)\), \(t=1/13,k=1\).
- \(Y_{10}=(1,101/960,31/64,3091/76800,4589/38400,3457/25600,101/9600)\), \(t=1/12,k=0\).
- \(Y_{11}=(1,1/12,1,19/480,7/30,0,1/120)\), \(t=1/12,k=1\).

For all four corners, the reusable seven-node mass/time/hinge verifier computes **exactly** legal capacities, \(T_P(y)=T_P(x),T_Q(y)=T_Q(x)\), and the five interior hinge convex-order inequalities \(H_j(y)\ge H_j(x)\). Every corner target lies on the same linear F face; interpolated targets remain lawful and seedless by convexity. Source \(x(t,k)\) is separately affine in \(t,k\), so the two-variable nonnegative barycentric interpolation preserves the equalities and five hinge inequalities for **all real** \(t,k\) in this rectangle. Finite Strassen gives the sought nonnegative declaration-independent coupling.

## Executed verification and continuation

Local Python 3 Fraction verifier F_EDGE_T12.py run 2026-11-08 printed:

    PASS_EXACT_F_FACE_CORNER_CERTIFICATES 4
    PASS_EXACT_INTERIOR_REGRESSION 101
    THEOREM_ALL_REAL_T_1_OVER_13_TO_1_OVER_12_P1_Q0_THETA1_KAPPA_FULL

The full-real result follows from exact corner verification and the analytic interpolation/Strassen lemma, not from the 101 regressions. Floating LP was used only for discovering rational corner targets. Reproduction: python3 F_EDGE_T12.py in this directory (imports the calibrated VERIFY.py).

Next seek a chart atlas that includes the t=1/12 p=1,q=0,theta=1 strip and nearby p,q,theta values. A numerical exploratory LP scan found the selected G face infeasible at this corner for tested kappa values, while F is feasible. This is a representation-specific observation and suggests using F on that part of parameter space and G only where necessary (e.g., p=0,q=1 at low kappa); possible triangular interpolation instead of forcing a global two-chart corner box.
