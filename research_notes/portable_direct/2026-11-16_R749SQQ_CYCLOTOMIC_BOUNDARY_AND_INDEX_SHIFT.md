# R749SQQ — Cyclotomic boundary terms and strict-prefix indexing

Date: 2026-11-16 (Asia/Shanghai). Status: **AUTHOR_EXACT_NOT_REVIEWED**.
Independent auxiliary positive labeled-source Walsh observer; frozen scientific input: awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389. Predecessor: R749SQP, PR #2516, commit f13f230e2d33a1578cc5cfa95c47aee947620fc9. This is independent scientific research without a shared X6 Task CLAIM.

## Population and indexing

For positive integer weights s=(s_1,...,s_d) with marked index j and h=s_j, define

\[
\Omega_r(s)=\{k\in\mathbb Z_{\ge0}^d:\sum_i s_i k_i\le r-1\},\
C_r=|\Omega_r|,\quad T_r=h\sum_{k\in\Omega_r} k_j,\quad E_r=T_r/(rC_r).
\]

Equal-weight labels remain distinct. The exact generating functions, for C_0=T_0=0, are

\[
\boxed{F_s(z)=\sum_{r\ge0}C_rz^r=\frac{z}{1-z}\prod_{i=1}^d(1-z^{s_i})^{-1},\quad
N_s(z)=F_s(z)\frac{hz^h}{1-z^h}.}
\]

**Index correction to R749SQP:** that paper prints F without the leading z while defining \(\sum_i s_i k_i\le r-1\). The printed F describes \(\sum_i s_i k_i\le r\). Its program nevertheless uses the *correct shifted coefficients*: r(r+1)...(r+k-1)/k! = [z^{r-1}](1-z)^{-k-1}, not the [z^r](1-z)^{-k} identified by the program comment. Hence the prior independently checked sixth-order numeric coefficient is not invalidated by this notation correction. The proof's generating-function declaration is repaired above.

## Theorem: first nontrivial cyclotomic term

Let \(\zeta\ne1\) be a root of unity, with at least one weight divisible by its order, and define

\[
I_\zeta=\{i:\zeta^{s_i}=1\},\quad m=|I_\zeta|\ge1,\quad
W=\prod_i s_i,\quad q=d-m+1,
\quad A_\zeta=
\frac{\zeta}{(1-\zeta)\prod_{i\in I_\zeta}s_i
\prod_{i\notin I_\zeta}(1-\zeta^{s_i})}.
\]

The first contribution from the pole at \(\zeta\) to the full normalized mean \(E_r\), beyond the smooth \(z=1\) component, equals

\[
\boxed{\frac{d!WA_\zeta\,\zeta^{-r}}{r^{q}}
\begin{cases}
(d+1-m)/((d+1)m!),&\zeta^h=1,\\
-1/((d+1)(m-1)!),&\zeta^h\ne1,
\end{cases}
+O(r^{-q-1}).}
\]

The error refers to *subsequent orders of that pole*. Other poles may have different leading orders. If \(m_*\) is the maximum multiplicity of any nontrivial pole and \(q_*=d-m_*+1\), the full mean through order \(q_*\) is its smooth \(z=1\) expansion plus the displayed contributions from poles with \(m=m_*\), uniformly for integer \(r\), with \(O(r^{-q_*-1})\) remainder.

**Proof.** Put \(w=1-z/\zeta\). For \(i\in I_\zeta\), \(1-z^{s_i}=s_iw+O(w^2)\); otherwise \(1-z^{s_i}\) is nonzero at \(\zeta\). Thus \(F_s(z)=A_\zeta w^{-m}+O(w^{-m+1})\), including the crucial strict-prefix factor \(\zeta\) in \(A_\zeta\). If \(\zeta^h=1\), the marked multiplier \(hz^h/(1-z^h)=w^{-1}+O(1)\), giving \(N_s=A_\zeta w^{-m-1}+O(w^{-m})\); otherwise the numerator has pole order at most \(m\).

The coefficient of \(w^{-p}\) is \(\zeta^{-r}r^{p-1}/(p-1)!+O(r^{p-2})\). At \(z=1\) the leading terms are \(C_r=r^d/(d!W)+O(r^{d-1})\) and \(T_r/r=r^d/((d+1)!W)+O(r^{d-1})\). Expanding \(E_r=(T_r/r)/C_r\) to the first order in the \(\zeta\)-contribution yields the boxed expression. Smooth lower-order coefficients and products of periodic corrections affect only subsequent orders. Finitely many poles and rational coefficient extraction give uniformity across integer residues. QED.

**Minimal periodic carrier.** At the first order where nontrivial roots contribute, sum the coefficients at identical root frequencies, discarding zero terms. The resulting periodic sequence has least period equal to the lcm of the orders of roots with nonzero net coefficient: root characters are linearly independent on a cyclic group containing these orders. A nonzero term \(b(-1)^r\) therefore has minimal period two and needs one parity residual if the precision observer has discarded \(r\bmod2\). This concerns the auxiliary source observer, not an identified spatial coordinate or signed-amplitude transport.

## Two exact onset examples

Mark the first unit source in each alphabet, so \(h=1\), and define \(H_{s,q}(r)=\sum_{j=0}^q a_j(s)/r^j\) as the smooth \(z=1\) Laurent-ratio expansion.

1. **Fifth-order parity:** \(s=(1,1,1,2,2,2,3)\), \(d=7\), \(W=24\). The unique highest-order nontrivial pole is \(\zeta=-1\), multiplicity \(m=3\); all others have multiplicity one. Here \(A_{-1}=-1/256\), so
\[
\boxed{E_r=H_{s,5}(r)+\frac{945}{32}\frac{(-1)^r}{r^5}+O(r^{-6}).}
\]
The exact smooth coefficients \(a_0,\dots,a_5\) are
\[
(1/8,\ 3/16,\ -119/96,\ 1309/192,\ -18599/384,\ 296989/768).
\]

2. **Sixth-order parity:** \(t=(1,1,1,2,2,3,5)\), \(d=7\), \(W=60\). The unique highest-order nontrivial pole is again \(\zeta=-1\), now multiplicity \(m=2\); all others have multiplicity one. Here \(A_{-1}=-1/256\), hence
\[
\boxed{E_r=H_{t,6}(r)+\frac{4725}{32}\frac{(-1)^r}{r^6}+O(r^{-7}).}
\]
The smooth coefficients \(a_0,\dots,a_6\) are
\[
(1/8,\ 3/8,\ -133/48,\ 931/48,\ -16583/96,\ 165767/96,\ -10655477/576).
\]

Both parity amplitudes are nonzero and consequently give *minimal* period two. These are exact fifth- and sixth-order periodic interruptions of an otherwise smooth source-moment hierarchy. R749SQP's bound \(m_\zeta\le d-2m\) for its even-order theorem is consistent: it excludes all periodic terms through order \(2m\). The present theorem describes precisely what appears as the pole multiplicity exceeds this bound.

## Exact evidence and future question

The dependency-free companion Python certificate executes integer and Fraction arithmetic. It returned **PASS** on 2026-11-16 for 48,002 marked-deletion checks at r=1,...,24001 across the two examples, 64 independent recursive counts, exact Laurent coefficients and pole amplitudes, and exact scaled samples at r=500,501,1000,1001,4000,4001,12000,12001,24000,24001. It also checked the complete 1,...,100 range of the two-weight alphabet (1,2) against its exact parity formulas. The unbounded result is the root-of-unity proof above, not a finite numeric extrapolation.

**Next:** classify simultaneous root contributions of higher orders and identify the minimal cyclic source residual under *families of future observer operations*, including marked sources divisible by the relevant cyclotomic order. Compare with existing BRC typed provenance ports before asserting an operational lift.

Current claim status: AUTHOR_EXACT_NOT_REVIEWED; no mathematical admission, formal shared Result, or TASK CLAIM is asserted.
