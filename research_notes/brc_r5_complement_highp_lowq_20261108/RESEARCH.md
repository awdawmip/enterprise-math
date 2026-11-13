# R5 — complementary high-p / low-q full-κ Blackwell prism on one seedless F face

Date: 2026-11-08. Classification: AUTHOR_PROVED / EXACT_FRACTION_EXECUTED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY. This is a result within the frozen seven-node P/Q-BRC terminal-observer model, not a change to P000 or native X6 geometry.

Predecessor: [PR #1817](https://github.com/awdawmip/enterprise-math/pull/1817), research branch research/r5-kappa-full-two-chart-20261108-t2040. The inherited immutable scientific inputs are GK a01383f825ef9d43b4b754254303298c64041568 and EM 86149263e38c22292c9def1e0f69092efa1be77e; current normative rules were read separately. Definitions and calibrated seven-node Q-mass formula are reproduced by VERIFY_EXACT.py.

## Theorem (full-real complementary five-dimensional prism)

Let t,p,q,θ,κ be arbitrary real numbers satisfying

    0 <= t <= 1/50,
    77/152 <= p <= 1,
    0 <= q <= 17/2112,
    0 <= θ <= 1,
    0 <= κ <= 1.

For the lawful FULL_HIST flow

    x=(1,t,1,(13t/40+1/80)*p, 9κ/40+tθ/10,
       (3t/40+21/80)*q, tθ/10),

there exist a lawful *seedless* LR target y=(g',a',b',u',v',w',z') and a nonnegative 7×7 declaration-independent transport matrix E such that, for likelihood ratios

    r=(1/10,1/2,3/4,1,5/4,3/2,19/10),

all 7 target row equations, all 7 source Q-column equations, all 7 source P-weighted column equations, and the two stopping-time equations hold:

    ∑_j E_ij=M_i(y),
    ∑_i E_ij=M_j(x),
    ∑_i r_i E_ij=r_j M_j(x),
    T_P(y)=T_P(x),   T_Q(y)=T_Q(x).

Every target lies on the **same linear seedless F face**

    z'=a'/10,    v'-z'=9b'/40.

Therefore 9b'z'=4a'(v'-z'), and any randomized seven-node terminal declaration has the same four-dimensional observable (eP,eQ,TP,TQ) after the Blackwell transport. The line (1-h)x+h y also admits the same target observable for every h∈[0,1], using (1-h)E+h diag(M(y)).

The theorem is an additional region, complementary to #1817's p≤77/152, q≥17/2112 rectangle, and includes the opposite physical corner p=1,q=0 for all t,θ,κ in the stated ranges.

## Exact proof

1. Let V={0,1}^5 be the 32 vertices of the stated box in coordinate order (t,p,q,θ,κ). In VERIFY_EXACT.py, TABLE gives for each vertex (a) the allowed flattened E indices 7i+j and (b) a few target-face/active-capacity linear constraints. A Fraction-only exact Gaussian elimination solves all 7 row, 14 column, 2 stop, 2 face, and selected active-capacity equations **uniquely**. The program then separately checks every nonnegative target capacity, the seedless polynomial, both normalizations, all 21 Blackwell equations and both stopping times. It constructs 32 complete *rational* certificates, consisting of 288 strictly positive E entries, with smallest positive entry 77/1216000.

2. Write each real parameter as a convex mixture of its two declared interval endpoints. For a multi-index α∈V, define W_α as the product of the five one-dimensional nonnegative weights. Since x is separately affine in all five variables, x=Σ_α W_α x_α exactly. Define y=Σ_α W_α y_α and E=Σ_α W_α E_α.

3. All target tuples y_α lie in the SAME LINEAR F face. The lawful physical constraints and nonnegative transport cone are convex; therefore y is lawful, E≥0, and the seedless relation holds for y. M, T_P, T_Q and the row/column/weighted-column equations are affine in flow coordinates (and linear in transport). Hence the vertex identities combine to exactly the desired identities at every interior or boundary real parameter, including irrational values. This proves the theorem without numerical extrapolation.

4. The 101 additional deterministic interior Fraction regressions in VERIFY_EXACT.py check the implementation of the interpolation and the complete target transport. The general real proof is Step 2–3. All computations are finite exact rational arithmetic, with no floating-point term in the verifier.

## A small independent rational witness for p=1, q=0

At (t,p,q,θ,κ)=(1/50,1,0,0,1), a particularly readable lawful target is

    y=(1,1/50,399/400,119/6400,3623/16000,7/32000,1/500).

A separately solved 13-edge transfer has flattened entries (7i+j : E_ij):

    0:93421/900000, 3:893/14400000, 9:3/8000,
    16:7831/16000, 17:9/16000, 24:3423101/72000000,
    26:13609/72000000, 30:3/16000, 31:3143/4000000,
    33:1107/4000000, 40:421/1600,
    47:5893/14400000, 48:83921/900000.

Direct exact solution verifies all row/column/moment/time equations and the physical capacities. This witness uses a **variable b'<1** F chart; fixing g'=b'=1, as in one earlier F subfamily, would miss this valid corner. The 32-corner verifier uses its own exact basic solution at that vertex.

## Verification and scope

Local Python 3 stdlib-Fraction checker built and actually executed on 2026-11-08: 32/32 exact corners passed, 288 positive edges, smallest positive edge 77/1216000; 101/101 exact mixed-parameter regressions passed. The GitHub artifact preserves the corresponding standalone mathematical checker and the local execution summary in EXACT_OUTPUT.txt. GitHub file readback is source persistence, not remote program execution. Floating LP was used *only to discover supports*; the proof checker reconstructs them by exact rational elimination.

This new region does not include all p,q simultaneously. The currently unjoined rectangles p<77/152,q<17/2112 and p>77/152,q>17/2112, as well as t>1/50, remain concrete continuation units. Current authored proofs await independent mathematical review and native task/result admission. 
