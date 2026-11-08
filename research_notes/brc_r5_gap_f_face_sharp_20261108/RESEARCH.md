# R5: exact F-face bridge across the middle triangular gap and sharp local capacity threshold

Date: 2026-11-08. Evidence class: AUTHOR_PROVED / EXACT_FRACTION_EXECUTED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY.

Frozen scientific inputs preserved verbatim: GK pin `a01383f825ef9d43b4b754254303298c64041568`, EM pin `86149263e38c22292c9def1e0f69092efa1be77e`. Current rules consulted separately: GK canonical main b99b7ead083488933cf0e97236b88bfb87b003a4, EM canonical main 8b3cf66ff1cd1a2992897916b20e2081093e2a00. Protected P000 and ACTIVE worldview unchanged. Scope: the frozen **seven-node P/Q-BRC terminal-observer statistical model**; this note makes no native X6 physical-dynamics claim.

## Theorem — new all-real five-parameter F-face region

For arbitrary real parameters
\[
\boxed{\frac3{20}\le t\le\frac7{39},\qquad
\frac{303}{2450}\le p\le1,\qquad
0\le q,\theta,\kappa\le1},
\]
the lawful FULL_HIST flow, in coordinates \((g,a,b,u,v,w,z)\),
\[
x=\left(1,t,1,
(\tfrac{13t}{40}+\tfrac1{80})p,
\tfrac{9\kappa}{40}+\tfrac{t\theta}{10},
(\tfrac{3t}{40}+\tfrac{21}{80})q,
\tfrac{t\theta}{10}\right)
\]
admits a lawful seedless LR target \(y\) **on the single linear F face**
\[
\boxed{z'=a'/10,\quad v'-z'=9b'/40}
\]
with a nonnegative declaration-independent \(7\times7\) Blackwell martingale transport that preserves all seven randomized terminal declarations and the calibrated stopping times \((T_P,T_Q)\), hence \((e_P,e_Q,T_P,T_Q)\).

The likelihood-ratio nodes are \(r=(1/10,1/2,3/4,1,5/4,3/2,19/10)\). The exact mass maps \(M_i(f)\), both time maps, physical bounds and five hinge functionals \(H_k(f)=\sum_i(r_i-r_k)_+M_i(f)\) are explicitly reproduced in `VERIFY.py`.

### Exact finite-to-real argument

The standalone `VERIFY.py` contains 32 seven-coordinate **exact rational targets**, indexed by
\[
(t,p,q,\theta,\kappa)\in\{3/20,7/39\}\times\{303/2450,1\}\times\{0,1\}^3.
\]
At every vertex it independently checks nonnegative physical capacities, all seven LR masses and unit probability/LR first moments, the F-face seedless relation \(9b'z'=4a'(v'-z')\), both exact time equalities and all five convex-order hinges \(H_k(y)\ge H_k(x)\).

For an arbitrary real point use nonnegative product barycentric weights for
\[
s=\frac{t-3/20}{7/39-3/20},\quad
u=\frac{p-303/2450}{1-303/2450},\quad q,\theta,\kappa.
\]
The source is separately affine in these parameters; the mixed coordinates \(tp,tq,t\theta\) are reconstructed *exactly* by the same weights. The target vertices lie on one common linear F face. Thus every physical inequality, mass, time equality and hinge inequality survives convex interpolation. Finite-support Strassen convex-order duality then gives at each real point a nonnegative matrix \(E\) satisfying
\[
\sum_j E_{ij}=M_i(y),\quad
\sum_i E_{ij}=M_j(x),\quad
\sum_i r_iE_{ij}=r_jM_j(x).
\]
It follows for **all real values**, including irrational parameters and all boundaries. Branch-specific Q/P contributions remain explicitly represented up to this declared observer. Reference: Leskelä and Vihola, *Conditional convex orders and measurable martingale couplings*, Bernoulli 2017, arXiv:1404.0999, finite-support case.

## Sharp single-F-face obstruction (exact dual identity)

Fix \(t=3/20,q=1,\theta=\kappa=0\), letting \(p\in[0,1]\). Then
\[
x(p)=\bigl(1,3/20,1,(49/800)p,0,219/800,0\bigr).
\]
**There exists a time-preserving lawful Blackwell realization on the F face if and only if**
\[
\boxed{\frac{303}{2450}\le p\le1}.
\]

Indeed for any F-face candidate \(y=(g,a,b,u,v,w,z)\) define the lawful nonnegative capacity slacks \(A=a,\ B=g-b,\ C=u,\ D=3a/40+21b/80-w\), and \(E_P=T_P(y)-T_P(x(p)), E_Q=T_Q(y)-T_Q(x(p))\). The following is an **exact affine identity for all real variables on F**:
\[
\boxed{p-\frac{303}{2450}
=\frac{222}{49}A+\frac{164}{49}B+\frac{800}{49}C
+\frac{472}{49}D+\frac{1272}{49}E_P-\frac{1436}{49}E_Q.}
\]
If both times match, the last two terms vanish and the four remaining terms are nonnegative. This proves necessity. For sufficiency the two rational target certificate rows at \(t=3/20,q=1,\theta=\kappa=0,p=303/2450\) and \(p=1\) satisfy the five hinges, physical capacities and times. Affine interpolation in \(p\) and finite Strassen give every intermediate point. The verifier checks the affine identity on its constant and all six basis directions \((p,g,a,b,u,w)\), plus the exact endpoint certificates.

This is an **F-face-specific boundary**; the full seedless LR model permits other faces.

## Actual verification, relation to frontier, next unit

Local command on 2026-11-08: `python -S VERIFY.py` (Python standard-library fractions.Fraction, exit 0). The exact stdout in `EXACT_OUTPUT.txt` reports 32 rational vertex checks, seven exact dual-basis checks, 201 rational interior regressions and 32 boundary regressions. Floating LP guided discovery, but no floating point or tolerance is used in proof-facing validation. The general theorem follows from the verified finite certificate plus analytic multiaffine interpolation and finite Strassen, not from sampled regressions.

Other immutable, **author-side** results: PR #1821 covers all physical p/q parameters through t<=1/13; PR #1823 covers the whole p<=q triangle through t<=3/20 and a later F-face strip from t=7/39 to 1/5; PR #1824 covers all t∈[0,1] with p>=5/7. This new F-face bridge fills the interval 3/20<=t<=7/39 for all q,theta,kappa and p>=303/2450, shrinking the remaining p<=q triangular gap to p<303/2450. The smaller-p region is the next exact problem. Independent mathematical review and formal Task CLAIM / Result / checkpoint are still pending.
