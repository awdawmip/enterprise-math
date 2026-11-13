> **Subsequent stronger theorem (2026-11-08):** `UNIFORM_THEOREM.md` and `VERIFY_UNIFORM.py` establish symbolic epsilon-uniform calibrated Blackwell kernels for **every real 0<t<=1/100000** (all p,q capacities, theta∈[3/4,1], kappa=3/4). This closes the previously open 0<t<10^-6 gap described below. The independent 64-vertex four-slab proof remains useful exact evidence for the middle range. `NEXT_UNIT.md` now names variable kappa as the next unit.

# R5 — Four exact common-chart slabs to t = 10^-6

Date: 2026-11-08. Status: AUTHOR_PROVED / EXACT_FRACTION_EXECUTED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY.

Source science pins (unchanged): Global a01383f825ef9d43b4b754254303298c64041568; Enterprise Math 86149263e38c22292c9def1e0f69092efa1be77e. Native author Researcher-ID EM-DIRECT-7CD960, session MCP-5243475206364d6bb15b904ce6831563, activity RA-20FC5EC4B18E1949386AF83E (verified Source activity commit 4055c859bdbf74424419441f6c492d35c5c811a4); GitHub actor awdawmip. No formal Task CLAIM, Owner or mathematical admission is asserted. P000 and ACTIVE worldview unchanged.

## New exact all-real positive-residual theorem

Fix kappa=3/4. For every real t,p,q,theta satisfying

    1/1000000 <= t <= 369/43076, 0 <= p,q <= 1, 3/4 <= theta <= 1,

set the lawful FULL_HIST source flow

    x=(g,a,b,u,v,w,z)
     =(1,t,1,(13*t/40+1/80)*p,
       t*theta/10+27/160,
       (3*t/40+21/80)*q, t*theta/10).

There is a lawful seedless-LR target y and nonnegative declaration-independent 7×7 calibrated Blackwell transport Q, preserving the full observer (eP,eQ,TP,TQ) for every seven-node terminal decision rule. The conclusion also holds for any interpolant (1-h)x+h*y, h in [0,1], with the same seedless target.

All real parameter points, including irrational points, are covered by these four **closed** t-slabs, each with one exact rational chart C_tau:

| t interval | tau |
| --- | --- |
| [1/1000000, 1/100000] | 300001/400000 |
| [1/100000, 1/10000] | 30001/40000 |
| [1/10000, 1/1000] | 3001/4000 |
| [1/1000, 369/43076] | 301/400 |

Each chart is C_tau={z'=tau*a'/10, v'-z'=9*tau*b'/40}. Its defining equalities imply 9*b'*z'=4*a'*(v'-z') exactly, the seedless constraint. All charts obey tau in [0,1].

The source signed history residual is R=9*t*(theta-3/4)/10. Thus the result covers positive residual for t>0,theta>3/4 and zero residual at theta=3/4, with complete independent capacities p,q in [0,1].

Combining this theorem with PR #1804's author-side exact result for t in [369/43076,1/5], theta in [3/4,1] extends positive-residual full-capacity coverage to t in [10^-6,1/5]. Combining PR #1803's author-side negative-residual chart C_(3/4) for t in [0,1/5], theta in [0,3/4] establishes **all real t in [10^-6,1/5] and p,q,theta in [0,1]**, kappa=3/4, for the stated four-dimensional statistical observer.

## Full calibrated seven-node model and verification equations

Frozen likelihood ratios:

    r=(1/10,1/2,3/4,1,5/4,3/2,19/10).

For f=(g,a,b,u,v,w,z), Q-masses and stops are

    M0 = 509*u/900+47*z/180+67*(v-z)/162+w/100
    M1 = 13*a/40+b/80-u
    M2 = (g-a)/2
    M3 = 1-g+a/10+9*b/40-v+191*(u+w)/450+43*z/90+14*(v-z)/81
    M4 = (g-b)/2
    M5 = 3*a/40+21*b/80-w
    M6 = u/100+47*z/180+67*(v-z)/162+509*w/900
    TP = 1+g+3*a/8+5*b/8+u/2+v+3*w/2
    TQ = 1+g+(a+b)/2+u+v+w.

Lawfulness requires 0<=a,b<=g<=1, 0<=u<=13a/40+b/80, 0<=w<=3a/40+21b/80, 0<=z<=a/10, 0<=v-z<=9b/40, nonnegative masses, sum_i M_i=1, and sum_i r_i*M_i=1. The calibrated transport is a nonnegative matrix Q_ij satisfying for each i,j

    sum_j Q_ij = M_i(y)          (7 row equations)
    sum_i Q_ij = M_j(x)          (7 column equations)
    sum_i r_i Q_ij = r_j*M_j(x)  (7 P-weighted column equations)
    TP(y)=TP(x), TQ(y)=TQ(x)   (2 stopping-time equations).

These relations preserve every seven-node terminal decision via Q pullback together with both stopping times.

## Exact certificate construction and analytic proof

For every slab [l,h] with fixed tau, all 16 vertices (t,p,q,theta) in {l,h}×{0,1}×{0,1}×{3/4,1} have **an exact rational lawful target and calibrated nonnegative kernel**. Across four slabs, there are **64 vertices and 642 positive kernel entries**, reconstructed *exactly* by the self-contained executable VERIFY.py.

VERIFY.py contains a literal embedded 64-token support table (16 per slab) with rational fixed-free-variable seeds. The 54 unknowns are the 49 flattened Q_ij followed by five target variables (g',a',b',u',w'); each token encodes the allowed nonzero subset of these unknowns, plus an optional exact rational free-variable pin. The script assembles the **full rational system above** and performs exact Fraction Gauss-Jordan elimination on each sparse support to uniquely reconstruct every vertex kernel and target; it checks every equality, positivity, seedless equality, flow capacity and mass normalization. No external solver, float, or binary file is needed to reproduce the 64 complete matrices: execute python3 VERIFY.py. A reproducible transcription of actual stdout is in EXACT_OUTPUT.txt.

For a real (t,p,q,theta) within one slab, define s=(t-l)/(h-l), vtheta=4*(theta-3/4). For a vertex e assign the product weight

    W_e=(s if e_t=h else 1-s)
       *(p if e_p=1 else 1-p)
       *(q if e_q=1 else 1-q)
       *(vtheta if e_theta=1 else 1-vtheta).

Every W_e is >=0 and their sum is 1. The source is *separately affine* in t,p,q,theta, so x=Σ_e W_e x_e holds identically for all real parameters. Put y=Σ_e W_e y_e and Q=Σ_e W_e Q_e. Every source/target physical constraint, both stops and calibrated mass equations are affine; all 16 target vertices share the same fixed chart C_tau. Accordingly y is lawful seedless, Q is nonnegative calibrated, and both stops agree, across the entire real slab. The consecutive slabs join without a gap at 10^-5,10^-4,10^-3. For x_h=(1-h)x+h*y, use Q_h=(1-h)Q+h*diag(M(y)).

This is a complete all-real proof conditional only on the exact rational vertex certificates reconstructed and independently asserted in VERIFY.py. The 1004 seeded rational interior and source-target-interpolant regressions actually passed, but are implementation tests rather than the continuous proof. SciPy LP discovered candidate sparse supports; final published verification is standard-library exact Fraction with no LP dependencies.

At t=0 the source is itself seedless on C_(3/4). The remaining small positive-t question is 0<t<10^-6 when theta>3/4; fixed-chart C_(4/5) separation from PR #1804 is preserved as an exact **chart-specific** obstruction, not a global no-go. The result establishes equivalence for the frozen typed seven-node P/Q-BRC statistical observer, and does not assert an unrestricted future native X6 state quotient.

## Next exact unit

Try a symbolic family of charts tau=3/4+epsilon/4 on t∈[epsilon/10,epsilon] for all 0<epsilon<=10^-5, construct symbolic rational kernels for the 16 vertices and prove their nonnegative support. A single parameter-uniform proof would close 0<t<10^-6. Independently vary kappa beyond 3/4 and preserve the joint P/Q likelihood-weighted and stop-time observers. See NEXT_UNIT.md.
