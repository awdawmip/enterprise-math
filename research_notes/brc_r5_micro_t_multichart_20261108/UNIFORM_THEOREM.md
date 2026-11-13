# R5 — Symbolic epsilon-uniform Blackwell bridge to t=0

Date: 2026-11-08. AUTHOR_PROVED / SYMBOLIC_EXACT_EXECUTED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY.
Frozen scientific pins: Global a01383f825ef9d43b4b754254303298c64041568; EM 86149263e38c22292c9def1e0f69092efa1be77e. P000 and ACTIVE worldview unchanged.
Native Researcher-ID EM-DIRECT-7CD960; activity RA-20FC5EC4B18E1949386AF83E; GitHub awdawmip. No native owner/CLAIM/Result/Review assertion.

## New all-real theorem

Fix kappa=3/4, g=b=1, a=t, and define for all real 0<=p,q<=1, 3/4<=theta<=1:

    x(t,p,q,theta)=(1,t,1,
      (13t/40+1/80)p,
      t*theta/10+27/160,
      (3t/40+21/80)q,
      t*theta/10).

**For every real 0<t<=1/100000**, all these lawful FULL_HIST flows have a lawful seedless LR target and nonnegative declaration-independent 7×7 calibrated Blackwell transport exactly preserving (eP,eQ,TP,TQ) for arbitrary terminal declarations. The source-target continuous interpolants have the same preservation. The precise seven-node model, likelihood ratios, mass equations, two stops and legal constraints are in RESEARCH.md and VERIFY.py and are used unchanged here.

More strongly, a *single rational-function certificate family* works for every real

    0<epsilon<=1/100000, epsilon/10<=t<=epsilon,
    0<=p,q<=1, 3/4<=theta<=1,

on the seedless target chart

    C_tau = { z'=tau*a'/10, v'-z'=9*tau*b'/40 },
    tau = 3/4 + epsilon/4.

The theorem for all 0<t<=1/100000 follows immediately by choosing epsilon=t and t as the upper endpoint. At t=0 the source is seedless on C_(3/4), so the whole [0,1/100000] interval is covered.

## Constructive rational-function proof

1. For the above epsilon and fixed chart, consider the 16 vertices

       t∈{epsilon/10,epsilon}, p,q∈{0,1}, theta∈{3/4,1}.

   Fix the **16 exact sparse supports** from the *first* line of the existing 64-vertex literal SEEDS in VERIFY.py. The support encoding describes the 49 calibrated kernel coordinates Q_ij and the five target coordinates (g',a',b',u',w'). Six of the supports have a single rational free-variable pin. Let E0=1/100000. For a pin written in VERIFY.py as ~name:value, choose its symbolic value

       f_name(epsilon) = base + (value-base)*epsilon/E0,

   with base=21/80 if name='r' and base=0 if name='V'. All pinned values coincide **exactly** with the original already-verified first-slab certificates at epsilon=E0. These formulae are rational in epsilon.

2. For each vertex insert the exact source and chart into the full 23 calibrated linear equations (7 target rows, 7 source columns, 7 likelihood-weighted source columns, 2 stop-time equations). Add one pin equation for a free support. Solve the resulting sparse linear system **symbolically over Q(epsilon)**. The executable VERIFY_UNIFORM.py uses SymPy linsolve, reduces every rational function and checks the full 23 equations directly as exact symbolic zero identities (not floating point).

3. For each symbolic vertex certificate, prove every nonzero kernel support coefficient and each needed target physical capacity slack is **nonnegative throughout the full real epsilon interval**. The checked target quantities are

       g', 1-g', a', g'-a', b', g'-b',
       u', 13a'/40+b'/80-u',
       w', 3a'/40+21b'/80-w'.

   The other target physical constraints follow from tau in [3/4,1], namely z'=tau*a'/10 and v'-z'=9tau*b'/40. Nonnegative kernel entries imply nonnegative target masses by row equalities. The script also exactly verifies the seedless equality 9b'z'=4a'(v'-z').

4. **Bernstein exact sign certificate.** Reduce every relevant rational function as A(epsilon)/B(epsilon), orienting the denominator positive at epsilon=E0/2. Substitute epsilon=E0*s, 0<=s<=1. For each exact polynomial P(s)=sum_(k=0)^n c_k s^k, compute its degree-n Bernstein coefficients

       beta_i = sum_(k=0)^i c_k * binom(i,k)/binom(n,k)
       P(s)=sum_(i=0)^n beta_i * binom(n,i) * s^i * (1-s)^(n-i).

   The verifier checks **every beta_i>=0 as an exact rational inequality**, for numerator and denominator of every kernel coefficient and physical slack. It separately checks denominator at epsilon=E0 is strictly positive and rejects the identically-zero denominator. A nonzero polynomial with all nonnegative Bernstein coefficients is strictly positive for 0<s<1; numerators may identically vanish for allowed zero edges/slacks. Hence all rational expressions and denominator signs are valid for every real 0<epsilon<=E0.

   Executed symbolic verification establishes **792 numerator/denominator polynomial checks**, maximal Bernstein polynomial degree **3**, zero failures. All 16 full vertex calibrated equations and seedless identities independently simplify to zero.

5. For a fixed epsilon, source coordinates are separately affine in t,p,q,theta. Nonnegative four-dimensional product weights from the 16 certified vertices interpolate source, target, kernel while preserving common chart, lawfulness, transport equalities and stops, exactly as in RESEARCH.md. This proves the continuous real rectangle for each epsilon. Choosing epsilon=t covers *every* positive t<=E0.

The construction is **effective**: given any exact rational epsilon in (0,E0], the rational functions instantiate exact kernel matrices. For irrational epsilon they define real algebraic/rational-function values, and the sign proof applies without rounding.

## Wider R5 frontier obtained by composition of verified author-side mathematics

The existing four-slab theorem RESEARCH.md covers t∈[10^-6,369/43076] for 3/4<=theta<=1. This epsilon-uniform theorem replaces its former small-t gap and covers (0,10^-5], with overlapping domain. The previous author-side PR #1804 covers t∈[369/43076,1/5] for 3/4<=theta<=1. Therefore positive/zero residual at fixed kappa=3/4 is now covered for **all real 0<=t<=1/5**, p,q∈[0,1], theta∈[3/4,1]. The author-side PR #1803 proves the complementary theta∈[0,3/4] chart for 0<=t<=1/5, so **every t in [0,1/5] and p,q,theta in [0,1]** is covered for the stated source family. The prior PR #1800's general lawful b/5<=a<=b region, when consumed within its proved scope, further covers this source family for t∈[1/5,1]. Thus current *combined author-side proof* covers all t∈[0,1] at g=b=1 and fixed kappa=3/4, for the frozen four-dimensional statistical observer.

This result is not a full native X6 future-operation quotient, and other kappa values and general g,a,b flows are open. All external PR inputs are author-side, unreviewed.

## Evidence and next problem

- VERIFY.py: self-contained exact Fraction 64-vertex kernel reconstruction; 642 positive edges and 1004 exact rational interior/transport regressions; executed PASS.
- VERIFY_UNIFORM.py: symbolic rational-function construction and 792 exact Bernstein-sign polynomial certificates over the **whole real epsilon interval**; requires SymPy; executed PASS.
- EXACT_OUTPUT.txt and EXACT_UNIFORM_OUTPUT.txt: actual local stdout from the two executions.
- RESEARCH.md: four independent finite slabs and initial theorem.
- NEXT_UNIT.md: next open variable-kappa capacity problem.

The remaining substantive next task is vary kappa beyond 3/4 and seek coherent rational-function chart partitions across theta and kappa while retaining both physical branches, the joint seven-node mass observer, both time observables and the original model pins. A separate independent review should inspect the symbolic support selection and the Bernstein interval logic.
