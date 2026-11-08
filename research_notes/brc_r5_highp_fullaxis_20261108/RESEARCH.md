# R5 — complete high-p full-t-axis Blackwell equivalence on one F face

**Date:** 2026-11-08. **Evidence status:** AUTHOR_PROVED / EXACT_FRACTION_EXECUTED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY.

## Source and frozen scientific inputs

Inherited exact R5 statistical inputs are frozen at GLOBAL_KNOWLEDGE \`a01383f825ef9d43b4b754254303298c64041568\` and Enterprise Math \`86149263e38c22292c9def1e0f69092efa1be77e\`, as recorded in [PR #1821](https://github.com/awdawmip/enterprise-math/pull/1821). Its established author-side result covers the entire five-parameter box \`0<=t<=1/13\`.

Current applicable operational rules were separately read from canonical main on 2026-11-08, including account bootstrap/manual, Source research continuation protocol/current normative context, P000, ACTIVE worldview, and the portable research method. This is a seven-node P/Q-BRC **terminal-observer model** theorem. The observer is the seven randomized terminal claims together with two stopping-time readouts. Its scope is not equality of latent FULL_HIST paths or native X6 dynamics.

## New theorem: exact high-p five-parameter slab

For **every real parameter** satisfying

\[
\boxed{\frac1{13}\le t\le1,\quad \frac57\le p\le1,\quad 0\le q,\theta,\kappa\le1},
\]

take the lawful FULL_HIST flow, in coordinate order \((g,a,b,u,v,w,z)\),

\[
x=\left(1,t,1,
\left(\frac{13t}{40}+\frac1{80}\right)p,\;
\frac{9\kappa}{40}+\frac{t\theta}{10},\;
\left(\frac{3t}{40}+\frac{21}{80}\right)q,\;
\frac{t\theta}{10}\right).
\]

There exists a lawful seedless LR target \(y\) on one fixed linear F face

\[
\boxed{z'=a'/10,\quad v'-z'=9b'/40}
\]

and a nonnegative declaration-independent seven-by-seven Blackwell martingale coupling. The coupling exactly preserves all seven randomized terminal declaration observables and the two calibrated stopping times \(T_P,T_Q\), therefore all four readouts \((e_P,e_Q,T_P,T_Q)\).

Combined with PR #1821's author-side full box for \(0\le t\le1/13\), the proved **high-p full-axis family** is

\[
\boxed{0\le t\le1,\quad 5/7\le p\le1,\quad 0\le q,\theta,\kappa\le1}.
\]

The new non-overlapping mathematical contribution is the upper-t strip \(1/13<t<1\) for this interior high-p capacity family. This also expands the earlier exact full-t special line \(p=1,q=0,\theta=1\) to a five-parameter region.

## Exact certificate and proof

The LR node list is

\[
r=(1/10,1/2,3/4,1,5/4,3/2,19/10).
\]

The pinned exact mass and time maps \(M_i(f),T_P(f),T_Q(f)\) are reproduced explicitly in \`VERIFY.py\`. Define for each of the five interior LR nodes

\[
H_k(f)=\sum_{i=0}^6(r_i-r_k)_+M_i(f),\qquad k=1,\ldots,5.
\]

The certificate contains 32 rational target vectors \(Y_{ijklm}\), one for every corner

\[
t_i\in\{1/13,1\},\quad p_j\in\{5/7,1\},
\quad (q,\theta,\kappa)=(k,l,m)\in\{0,1\}^3.
\]

The pure-standard-library \`Fraction\` verifier checks at every corner:

1. All source and target physical-capacity inequalities; nonnegative seven-node masses; exactly unit mass and unit LR first moment.
2. The target F face, implying the seedless polynomial \(9b'z'=4a'(v'-z')\).
3. \(T_P(Y_{ijklm})=T_P(x_{ijklm})\) and \(T_Q(Y_{ijklm})=T_Q(x_{ijklm})\) exactly.
4. All five exact hinge inequalities \(H_k(Y_{ijklm})\ge H_k(x_{ijklm})\).

For arbitrary real parameters let

\[
s=\frac{t-1/13}{1-1/13},\quad u=\frac{p-5/7}{1-5/7},
\]

and form the nonnegative weights

\[
W_{ijklm}=s^i(1-s)^{1-i}u^j(1-u)^{1-j}
q^k(1-q)^{1-k}\theta^l(1-\theta)^{1-l}
\kappa^m(1-\kappa)^{1-m}.
\]

Define the target \(y=\sum W_{ijklm}Y_{ijklm}\). The weights sum to one. The source is separately affine in \(t,p,q,\theta,\kappa\), so the exact equality \(x=\sum W_{ijklm}x_{ijklm}\) holds. Physical legality, LR mass/normalization, two stop-time equalities and the five hinge inequalities are affine and persist under this common convex combination. All target vertices lie on the same **linear** F face, so the interpolated \(y\) is seedless. This is a proof for *all real parameters*, not an extrapolation from a finite grid.

The seven LR laws have equal unit mass and unit LR mean. Nonnegative differences of their five interior hinge functionals characterize their convex order. The finite martingale-coupling theorem (Strassen) therefore supplies a nonnegative \(7\times7\) matrix \(E\) with

\[
\sum_j E_{ij}=M_i(y),\qquad
\sum_i E_{ij}=M_j(x),\qquad
\sum_i r_iE_{ij}=r_jM_j(x).
\]

These are the exact Blackwell equations for the declared P/Q terminal observer; \`E\` need not depend on the terminal declaration. The full joint branch mass vector is retained for the certificate rather than erased to a scalar.

Reference: Leskelä & Vihola, *Conditional convex orders and measurable martingale couplings*, Bernoulli (2017), arXiv:1404.0999 (finite-support use).

## Reproduction and frontier

Run \`python3 VERIFY.py\` using Python standard library only. The published \`EXACT_OUTPUT.txt\` is:

\`\`\`text
PASS_EXACT_F_FACE_32_CORNERS 32
PASS_EXACT_307_INTERIOR_REGRESSIONS
PASS_ALL_REAL_F_FACE_INTERPOLATION_T_1_13_TO_1_P_5_7_TO_1
\`\`\`

The 307 exact rational regression samples check the interpolation implementation. The all-real proof is the corner and multiaffine argument plus finite Strassen coupling theorem.

**Next exact research unit:** On the F face at \((t,q,\kappa,\theta)=(1/13,1,0,0)\), determine the sharp rational threshold in \(p\) for which the F-face representation is feasible. Exact test \`p=7/10\` against \`p=71/100\`, then reconstruct a rational dual obstruction or a constructive target. Seek a new face/triangle chart extending below \`p=5/7\`. Preserve any obstruction only for the tested representation, and keep the full FULL_HIST mother objective open.

**Control scope:** author proof and portable evidence; native Researcher-ID, live task ownership/CLAIM, checkpoint, Result, independent review and mathematical admission require their own actual receipts.