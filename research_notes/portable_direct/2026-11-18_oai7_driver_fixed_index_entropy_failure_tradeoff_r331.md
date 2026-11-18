# OAI7 r331 — Fixed-index codebook entropy/failure tradeoff and a universal marginal-entropy floor

Date: 2026-11-18. Evidence class: new author-side mathematical derivation and a scoped audit of r329–r330, not a frozen Native Result, independent review, Task completion, native Heartbeat-X6 implementation or Source/Activity admission. Preserve the original OAI7 researcher EM-EMF6D046-5A2844 and all prior mathematical authors.

## Theorem A: adjustable all-test-set codebook

Adopt exactly the external finite cyclic shared-displacement model, all logarithms natural, and the definitions of r329/r330:
\((p)\) prime tending to infinity, \(u=\lceil\sqrt p\rceil\), \(L=\log p\),
\(b=17/64\), \(J=1-b+b\log b>0\), \(c_*=(4J)^{-1}\), and any fixed
\(d>4\log A_b\), where \(A_b=((1-b)\sqrt{2\pi b c_*})^{-1}\).
Set

\[
n=\left\lceil c_*\sqrt p\,(L-2\log L+d)\right\rceil<p.
\]

Choose any sequence of targets \(\zeta_p\) such that, for all sufficiently large \(p\),

\[
p^{-1/32}\le \zeta_p\le 1/100.
\tag{331.1}
\]

There exists a fixed deterministic codebook of \(M_p\) pairwise-distinct \(n\)-subsets of \(\mathbb F_p\), allowing repeated members *between* codebook entries, where

\[
M_p=\left\lceil \frac{32u}{\zeta_p}\right\rceil,
\tag{331.2}
\]

and a single random joint diagonal-shift vector \(H=(h_0,\ldots,h_{n-1})\), each
\(h_l\in\mathbb Z^{4097}\), such that:

1. In every realization the \(n\) shifts are pairwise distinct modulo \(p\).
2. For \(Y\) independent of \(H\), the **complete integer-valued** laws of \(Y+h_l\) agree for all \(l\).
3. For each of the \(8194\) signed coordinate residues and every deterministic test \(u\)-set \(K\), with the exact r330 small-list failure definition,
   \[
   \max_{|K|=u}\Pr_H\{V_H^{(c)}(K)>p^{3/4}\}\le\zeta_p.
   \tag{331.3}
   \]
   The maximum over fixed \(K\) is outside the schedule probability.
4. The sampled shift-vector entropy obeys the uniform tradeoff
   \[
   \boxed{H(H)\le L+\log L+\log(1/\zeta_p)+O_d(1).}
   \tag{331.4}
   \]

In particular choosing \(\zeta_p=1/100\) yields
\[
\boxed{H(H)\le\log p+\log\log p+O_d(1),\quad q_c\le 0.01.}
\tag{331.5}
\]
This reduces the previous r330 bound \(\log p+2\log\log p+O_d(1)\) by one \(\log\log p\) term, at the same fixed \(4097\)-index and sharp second-order \(n\)-scale. Choosing \(\zeta_p=L^{-a}\) for any fixed \(a>0\) gives \(q_c\le L^{-a}\) and \(H(H)\le L+(1+a)\log L+O_d(1)\).

For the constant choice \(\zeta_p=1/100<111/4352\), the exact r307 shared-tail inequality and the same \(k=s=4097\) information budget used in r330 continue to hold for sufficiently large primes. Hence the terminal signed marginals attain the same stated coverage conclusion in the external model. No claim of \(q_c\to0\) is made for the constant-failure construction.

## Proof

By r329's dual Johnson-slice calculation, for any fixed deterministic \(u\)-subset \(K\) and a uniform random \(n\)-subset \(W\),
\[
\Pr_W\{V_W(K)>p^{3/4}\}\le\varepsilon_p,
\qquad \varepsilon_p=O_d(p^{-1/4}L).
\]
Thus \(\varepsilon_p\le p^{-1/8}\) eventually, uniformly in \(K\).

Sample independently \(M_p\) uniform \(n\)-subsets \(W_i\). For fixed \(K\), their failure indicators \(Z_i(K)\) are independent, each with mean at most \(p^{-1/8}\). The elementary exponential-moment Chernoff inequality gives
\[
\Pr\left\{\frac1{M_p}\sum_{i=1}^{M_p}Z_i(K)>\zeta_p\right\}
\le \left(\frac{e\,p^{-1/8}}{\zeta_p}\right)^{M_p\zeta_p}.
\]
By (331.1), \(\log(e p^{-1/8}/\zeta_p)\le 1-3L/32\le-L/16\) for large \(p\). Hence the fixed-\(K\) probability is at most
\[
\exp(-M_p\zeta_p L/16)\le\exp(-2uL).
\]
The number of test subsets satisfies \(\log\binom pu\le u\log(ep/u)\le uL\) eventually. A union bound therefore gives probability at most \(\exp(-uL)<1\) that **any** deterministic \(K\) violates (331.3). Fix a successful codebook.

For each codebook member fix an ordering of its \(n\) distinct shifts. Sample independently a uniform codebook index \(I\in\{1,\ldots,M_p\}\) and a uniform cyclic position \(R\in\{0,\ldots,n-1\}\); use the cyclically rotated ordered shifts of \(W_I\), copying each chosen integer representative into every one of 4097 coordinates of \(h_l\). Every position has exactly the same full displacement-vector law, since
\[
\Pr(h_l=([a]_p,\ldots,[a]_p))
=\frac1{M_p n}\sum_i {\bf1}_{a\in W_i}
\]
is independent of \(l\). Independence of \(Y\) gives identical full lattice-valued marginals. Rotation does not change the small-list counts, and sign reversal replaces \(K\) by \(-K\). The codebook union bound covers both.

Finally \(H(H)\le H(I,R)=\log(M_p n)\). Since
\(M_p=O(u/\zeta_p)\), \(u=O(\sqrt p)\), and \(n=O_d(\sqrt p L)\), (331.4) follows. For the information budget of r307,
\[
H(H)+4097[-\log(1-u/p)]
\le L+\log L+\log(1/\zeta_p)+O_d(1)+o(1).
\]
For \(\zeta_p=1/100\), this is eventually below \(4097L/4096\). The bound \(R_0\le1/100<111/4352\) verifies the other affected transfer hypothesis; the original r330 argument supplies the remaining signed entropy and symmetry checks.

## Theorem B: unavoidable schedule entropy from marginal equality

Let \(V=(V_0,\dots,V_{n-1})\) be **any finite-valued** random sequence such that all position marginals coincide and every realized sequence has pairwise distinct entries. Then
\[
\boxed{\max_v\Pr(V=v)\le 1/n,\qquad H_\infty(V)\ge\log n,\qquad H(V)\ge\log n.}
\tag{331.6}
\]
Indeed, if one particular realized sequence \(v=(v_0,\ldots,v_{n-1})\) occurs with probability \(t\), its distinct entries satisfy \(\Pr(V_l=v_l)\ge t\) for every \(l\). The common marginal \(\nu\) thus has \(\nu(v_l)\ge t\) for \(n\) distinct values, whence \(1\ge\sum_l\nu(v_l)\ge nt\). This proves the min-entropy and Shannon-entropy bounds.

Applying the statement to the distinct realized diagonal shifts in Theorem A gives the universal necessary floor
\[
H(H)\ge\log n=\tfrac12\log p+\log\log p+O_d(1).
\]
It is a floor for the **equal-per-position-marginal, distinct-schedule** model, rather than an optimality claim for the \(L+\log L\) upper bound. An additional gap remains between this universal entropy floor and the codebook construction.

## Audit, lineage, and scope

The proof independently rechecks r330's union-bound mechanism and exact r307 numerical inequality, replacing the target \(\zeta=1/L\) by a tunable tolerance with a correspondingly smaller codebook. The derivation of the dual uniform-subset failure estimate remains attributed to r329; r330 supplies the cyclic full-lattice-marginal mechanism. This is a new author-side refinement in the *external finite cyclic model*, preserving all earlier sources and the original OAI7 researcher contribution. It has not undergone a separate independent Native Result review.

Source pins: r329 @f1f35331daf48fbbbe01d8cf0cd43342dff85c01; r330 @67f57ab662493b6744df560c8358a293a08d1165; r307 @baaaabaacaf8543f62a45a00cdfcf03e95389075. Open: direct explicit codebook, tighter advice/storage cost, correspondence with valid ordered Heartbeat-X6 trajectories, frozen Result and native Source/Activity association.
