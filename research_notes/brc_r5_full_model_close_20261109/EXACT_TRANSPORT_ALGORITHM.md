# R5: constructive exact martingale Blackwell kernel from a seedless target

2026-11-09, frozen seven-node P/Q-BRC statistical observer. **Algorithmic artifact / exact author-side mathematical verifier**, no admission assertion. Related: RESEARCH.md all-real triangular prism and VERIFY_PGEQ.py.

## Input / output interface

Input: two rational lawful flows \(x,y\) in the frozen seven-node model, with equal \(T_P,T_Q\), whose \(Q\)-terminal LR masses satisfy the required convex-order relation. Output: a \(7\times7\) nonnegative **rational** matrix \(E\) satisfying
\[
\sum_jE_{ij}=M_i(y),\quad
\sum_iE_{ij}=M_j(x),\quad
\sum_i r_iE_{ij}=r_jM_j(x).
\]
The standalone module EXACT_COUPLING_SIMPLEX.py exports exact_coupling(x,y) and **verifies all returned equalities again** before returning.

## Exact construction

Introduce \(49\) unknown \(E_{ij}\ge0\) and \(21\) equations (7 target rows, 7 source columns and 7 source likelihood-ratio-weighted columns). Append one nonnegative artificial variable to each equation. Because every right-hand side is a Q mass or positive LR-weighted mass, the artificial-variable basis supplies an initial feasible solution. Maximize
\[
-\sum_{k=1}^{21} a_k.
\]
The exact tableaux use Python Fraction, Gauss–Jordan pivots and **Bland's smallest-index entering/leaving variable rules** (finite termination even in degenerate cases of an unconstrained run). If the exact phase-I optimum is zero, all artificial variables vanish; the original \(E\) is feasible. If the optimum is negative, the source/target pair is outside martingale-coupling feasibility for this exact model. The code uses a practical 10000-pivot cap; a cap hit is reported as unfinished computation, not infeasibility.

Bland's rule plus the exact LP feasibility theorem establishes the correctness of the algorithm under its hypotheses. The finite-support convex-order theorem establishes existence of a zero phase-I objective for the lawful F-face targets in the triangular theorem. The matrix is constructed **after** the target y is chosen; choosing a target for other R5 sectors still follows the appropriate verified G/F chart.

## Executed exact checks

Executed locally under Python standard library alone:
- Six different rational source/target pairs, including boundary and mixed points, all had exact matrices: 45–77 pivots and 6–14 positive entries, with every mass and moment equality verified.
- **120 additional rational points** across \(t\in[1/13,1/5]\), \(0\le q\le p\le1\), \(\theta,\kappa\in[0,1]\) all returned exact verified matrices. Maximum observed pivots **66**; support counts: 94 with 14 positive edges, 23 with 15 edges, 3 with 13 edges. These are empirical data from the declared 120 points, not worst-case complexity bounds.
- One concrete explicit independent 12-edge rational certificate is in EXPLICIT_12_EDGE.md / VERIFY_EXPLICIT_MATRIX.py.

Reproduce the library self-tests: `python -S EXACT_COUPLING_SIMPLEX.py`; reproduce fixed 120-point regression: `python -S REGRESSION_COUPLING.py`. No SciPy or SymPy is used by the published algorithm. The exploratory one-example edge support in EXPLICIT_12_EDGE.md was LP-assisted, but the published general generator is exact phase-I simplex.

## Resource account and next problem

There are 70 tableau variables and 21 constraints, with at most 49 nonnegative original edges. A pivot performs rational row operations over a 21×71 tableau, and each pivot's **bit cost** depends on numerators and denominators; measured sample pivot counts above establish only sample behavior. This is a known exact linear-programming method, **not a novel complexity breakthrough**. Next: derive improved constructive monotone/left-curtain transport for this fixed ordered LR grid, prove bit-complexity and sparsity bounds, and integrate target selection for the entire stitched model domain. Preserve frozen scientific pins and independent mathematical review.
