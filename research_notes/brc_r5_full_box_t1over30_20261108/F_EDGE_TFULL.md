# R5 — exact full-t-axis special family (p=1, q=0, theta=1)

Date: 2026-11-08. Author-side theorem, exact Fraction execution. Frozen R5 science pins, P000 and ACTIVE worldview unchanged.

For the frozen seven-node model, set \(p=1,q=0,\theta=1\) in

\[
x(t,\kappa)=\left(1,t,1,\frac{13t}{40}+\frac1{80},
\frac{9\kappa}{40}+\frac t{10},0,\frac t{10}\right).
\]

**New exact theorem.** For **all real** \(1/13\le t\le1\), \(0\le\kappa\le1\), there exists a lawful seedless LR target on the common F face \(z'=a'/10,\ v'-z'=9b'/40\) and a nonnegative seven-node declaration-independent Blackwell transport preserving \(e_P,e_Q,T_P,T_Q\). Together with the full physical five-parameter box theorem in EXTENSION_T1OVER13.md for \(0\le t\le1/13\), this gives a seedless Blackwell realization for the entire one-parameter-axis family \(0\le t,\kappa\le1\) at \(p=1,q=0,\theta=1\).

## Explicit four-target convex representation

Use \(s=(t-1/13)/(1-1/13)\). Interpolate the four exact target vectors \(Y_{ij}\) as \(y=(1-s)(1-\kappa)Y_{00}+(1-s)\kappa Y_{01}+s(1-\kappa)Y_{10}+s\kappa Y_{11}\), where coordinates have order \((g',a',b',u',v',w',z')\):

- \(Y_{00}=(1,41/416,1009/2080,6339/166400,9901/83200,22419/166400,41/4160)\).
- \(Y_{01}=(1,1/13,1,3/80,121/520,0,1/130)\).
- \(Y_{10}=(1,1889/2060,823/1030,1269/4120,2237/8240,0,1889/20600)\).
- \(Y_{11}=(1,1,1,27/80,13/40,0,1/10)\).

At \(t=1/13\), the targets are \(Y_{00},Y_{01}\); at \(t=1\), they are \(Y_{10},Y_{11}\). The standalone F_EDGE_TFULL.py checker verifies each corner against seven-law mass/normalization, all physical capacities, both calibrated stopping times, five hinge convex-order inequalities, and seedless F constraint, using exact Python Fraction only. Their convex interpolation retains every condition, because x is separately affine in \(t,\kappa\), the target F face is linear, and all other inequalities/equalities are affine. Finite-support Strassen then gives a nonnegative \(7\times7\) martingale transfer at every real point, including irrational parameters.

## Local exact validation and frontier

Actual local execution (2026-11-08) returned

    PASS_EXACT_F_FACE_CORNER_CERTIFICATES 4
    PASS_EXACT_INTERIOR_REGRESSION 101
    THEOREM_ALL_REAL_T_1_OVER_13_TO_1_P1_Q0_THETA1_KAPPA_FULL

Exact local stdout is in F_EDGE_TFULL_OUTPUT.txt. The all-real conclusion uses the analytic corner interpolation and finite Strassen result, not the 101 regression cases. In source-specific terms, this completes the indicated \(p=1,q=0,\theta=1\) family, while the full five-parameter mother problem for \(t>1/13\) remains the next research target.

Next: extend a neighborhood in \((p,q,\theta)\) around the demonstrated F-face strip. For nearby low \(p\), high \(q\), the complementary G face is required at low \(\kappa\); seek a triangulated chart atlas instead of requiring every G-corner target at \(p=1,q=0\). Preserve chart-specific LP failures as exploratory evidence; no global no-go claimed. Independent review and native admission pending.
