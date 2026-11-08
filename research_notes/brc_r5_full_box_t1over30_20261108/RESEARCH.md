# R5 — complete five-parameter exact Blackwell prism through t = 1/30

**Date:** 2026-11-08. **Status:** AUTHOR_PROVED / EXACT_FRACTION_EXECUTED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY.

**Inherited immutable science pins:** GLOBAL_KNOWLEDGE a01383f825ef9d43b4b754254303298c64041568; Enterprise Math 86149263e38c22292c9def1e0f69092efa1be77e. Current normative rules were separately consulted through both repositories' current canonical main. Predecessor: PR #1820 at 731114d52c8d3d5a38e131e13746602b4a7dbcb8 (complete box through t=1/40). Protected P000 and ACTIVE worldview unchanged. This is a seven-node P/Q-BRC terminal-observer model theorem, not a native physical X6 assertion.

## Theorem — all real parameters

For arbitrary reals

\[
0\le t\le \frac1{30},\qquad 0\le p,q,\theta,\kappa\le1,
\]

consider the lawful FULL_HIST flow

\[
x=(1,t,1,(\tfrac{13t}{40}+\tfrac1{80})p,\,
\tfrac{9\kappa}{40}+\tfrac{t\theta}{10},\,
(\tfrac{3t}{40}+\tfrac{21}{80})q,\,
\tfrac{t\theta}{10}).
\]

There is a lawful seedless LR flow \(y=(g',a',b',u',v',w',z')\) and a nonnegative \(7\times7\) declaration-independent Blackwell matrix \(E\), for likelihood ratios \(r=(1/10,1/2,3/4,1,5/4,3/2,19/10)\), such that

\[
\sum_j E_{ij}=M_i(y),\quad
\sum_i E_{ij}=M_j(x),\quad
\sum_i r_i E_{ij}=r_j M_j(x),\quad (i,j=0,\ldots,6),
\]

and \(T_P(y)=T_P(x),\ T_Q(y)=T_Q(x)\). Consequently every randomized terminal declaration has its four observable values \((e_P,e_Q,T_P,T_Q)\) exactly preserved. This includes irrational parameters and every boundary of the box.

The explicitly calibrated seven masses \(M_i\) and the two time functionals are fully reproduced in VERIFY.py.

## Exact proof

**Convex order replaces 49-variable transport search.** Every lawful \(f\) satisfies \(M_i(f)\ge0\), \(\sum_i M_i(f)=\sum_i r_iM_i(f)=1\). Set \(H_k(f)=\sum_i(r_i-r_k)_+M_i(f)\) for \(k=1,\ldots,5\). For two such finite likelihood-ratio laws, a martingale coupling with target row masses \(M_i(y)\), source column masses \(M_j(x)\), and weighted column identities as above exists iff \(H_k(y)\ge H_k(x)\) for each interior hinge. Necessity follows from Jensen; sufficiency follows from convex order on finite ordered support (hinges generate convex functions modulo affine functions), and the finite Strassen martingale-coupling theorem. The direction is source-LR \(X\) smaller in convex order than target-LR \(Y\), with \(\mathbb E[Y\mid X]=X\). Reference: Leskelä–Vihola, *Conditional convex orders and measurable martingale couplings*, Bernoulli 2017, arXiv:1404.0999; see also Econlib Probability.Order.Strassen.DiscreteGeneral for a discrete formalization.

**Exact rational chart seam.** Define the bilinear \(S(p,q)\) on \([0,1]^2\) by the corner values

\[
S(0,0)=S(1,1)=\tfrac34,\quad S(0,1)=\tfrac9{10},\quad S(1,0)=\tfrac12
\]

and let

\[
\boxed{h(t,p,q)=1-30t(1-S(p,q))\in[\tfrac12,1]}.
\]

For \(0\le\kappa\le h\), put \(\lambda=\kappa/h\), interpolate targets from chart **G**, the linear seedless face \(a'=z'=0\). For \(h\le\kappa\le1\), put \(\lambda=(\kappa-h)/(1-h)\) when \(h<1\), and interpolate chart **F**, the linear seedless face \(z'=a'/10,\ v'-z'=9b'/40\). At \(t=0\) the identity target works. Both faces satisfy the seedless polynomial \(9b'z'=4a'(v'-z')\).

**Finite exact certificate.** VERIFY.py embeds 32 rational seven-coordinate target rows, 16 per chart, at \(t=1/30\) and \((p,q,\theta,\lambda)\in\{0,1\}^4\); it also verifies 32 identity rows at \(t=0\). At each endpoint it checks: all physical nonnegative capacities and LR normalizations; both exact stop-time equalities; all five exact rational hinge inequalities; and the selected seedless face. Exact fractional Gaussian elimination from numerical LP exploration furnished the rational vertex rows; the published certificate is fully checked by standard-library fractions.Fraction without numerical tolerances.

**Extension to every real value.** For each chart, \(\kappa_G=\lambda h\) or \(\kappa_F=h+\lambda(1-h)\). The source is separately affine in \(t,p,q,\theta,\lambda\), including the mixed terms. Use the 32 nonnegative product weights of those five coordinates to interpolate target rows. Each chart's target rows lie on a *common linear seedless face*. The allowed physical inequalities are affine, the mass/time maps are affine and the five hinge differences are affine; therefore all the verified equalities and inequalities persist throughout the chart. Strassen supplies \(E\) at each real point. G and F cover the full \(\kappa\) interval, proving the theorem.

## Reproduction and next question

Run: python3 VERIFY.py

Actual Python 3 standard-library Fraction execution returned 64/64 exact endpoint checks, 251/251 rational interior regressions and 32/32 physical boundary cases (see EXACT_OUTPUT.txt). Universal quantification follows from the analytic interpolation and finite Strassen theorem, not from extrapolating the regression samples. The predecessor threshold \(t\le1/40\) has been strictly expanded to \(t\le1/30\).

Next exact experiment: test the same chart family at \(t=1/25\), looking for 32 exact corner targets; if a corner fails, vary \(S\) or permit additional seedless faces and distinguish a chart-specific obstruction from the overall FULL_HIST mother question. A second route is an explicit sparse analytic martingale kernel derived from the hinge certificates. Independent proof review and native Task/Result admission remain unperformed; no formal CLAIM is asserted.
