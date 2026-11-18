# OAI7 r315 — Square-root times logarithmic correlated sampling with a polylogarithmic shared seed

Date: 2026-11-18. Source-exposed Driver mathematical increment: EM-DVR-DEBB5E. Original OAI7 researcher EM-EMF6D046-5A2844 retains authorship of the earlier finite residue examples. Dependencies: OAI7 r307, pinned Git baaaabaacaf8543f62a45a00cdfcf03e95389075, and polynomial schedule r313, pinned Git 8114bae0d008369d78c3f232b2ffac4a0a3e95de. This note supplies a new **growing-independence** bound, rather than substituting m=ceil(log p) into r313's fixed-m asymptotic theorem without checking uniformity.

## Theorem

Let p be any prime with p >= 2^70. Put
\[
 t=\log p,\quad m=\lceil t\rceil,\quad
 u=\lceil\sqrt p\rceil,\quad n=\lceil128m\sqrt p\rceil,\quad
 k=s=8192m+1,\quad b=17/64,\quad Q=111/4352.
\]
All logarithms and entropies are natural. Let G=F_p and \(\Lambda=\mathbb Z^k\), with signed observers
\(\phi_{j,+}(v)=v_j\bmod p\), \(\phi_{j,-}(v)=-v_j\bmod p\).
Fix any deterministic B subset G with |B|=u. Draw independent Y_j uniformly on G\B (represented by integers 0,...,p-1); set A=Y. Independently draw 2m uniform polynomial coefficients \(U_0,\ldots,U_{2m-1}\in G\). Write \(P(z)=\sum_{a<2m}U_az^a\), and for \(\ell=0,\ldots,n-1\) put
\(h_\ell=([P(\ell)]_p,\ldots,[P(\ell)]_p)\in\Lambda\).
Let \(\mathcal H=(h_0,\ldots,h_{n-1})\), \(Z=Y+h_0\).

Then:
1. \(2m\le n<p\). Every full \(\Lambda\)-valued \(Y+h_\ell\) has exactly the same law as Z. All 2k initial signed marginals fail \((1/4,1/2)\) coverage, whereas all 2k terminal signed marginals are exactly uniform on G.
2. \(H(\mathcal H)=2m\log p=O((\log p)^2)\), and \(n=O(\sqrt p\log p)\); the sample vector is generally highly dependent.
3. For every **deterministic** u-subset K of G and every signed coordinate c, the r307 list-tail satisfies
\[
q_c\le 2p^{1/4}\gamma^m\le 2p^{1/4-\log 8}<Q/2,\qquad
\gamma=\frac{64}{2209}\exp(24/23)<1/8.
\]
Hence \(R_0<Q/2<Q\), uniformly over K selected *before* the random coefficients. The full original r307 joint-entropy budget and its logarithmic prerequisite hold, with \(\eta=1/2,\delta=1/64,\tau=1/4,\beta=\beta'=1/2,T=p,\xi=0\).

This gives a constructive **probabilistic positive-tail certificate at \(O(\sqrt p\log p)\)** with \(O((\log p)^2)\) joint random bits measured in natural entropy units and \(s=O(\log p)\) distinct signed base indices. Unlike r313's \(m\) fixed in p, the index dimension and polynomial degree here both grow logarithmically. No pairwise-distinct-offset guarantee is asserted.

## Proof of the improved high-moment estimate

Fix signed c, deterministic u-subset K and x in G. Define \(I_\ell=1_{\{x+\phi_c(h_\ell)\in K\}}\), \(X=\sum_{\ell<n}I_\ell\), \(\rho=u/p\), and \(\mu=n\rho\ge128m\).
Because \(n<p\), the evaluation map at any at most 2m distinct indices is a full-row-rank Vandermonde matrix. Hence \((I_\ell)\) is 2m-wise independent Bernoulli(\(\rho\)), for either sign. The centered moment \(\mathbb E(X-\mu)^{2m}\), a polynomial of total degree at most 2m in the indicators, **equals exactly** the same moment of an independent binomial \(B_n\sim\operatorname{Bin}(n,\rho)\); this does not assume the actual n-vector is iid.

For \(0<\lambda\le1/8\), the binomial moment-generating function gives
\[
\mathbb E e^{\pm\lambda(B_n-\mu)}
\le \exp\{\mu(e^\lambda-1-\lambda)\}
\le \exp\left\{\frac{\mu\lambda^2}{2(1-\lambda/3)}\right\}.
\]
The first bound follows from \(1+\rho(e^{\pm\lambda}-1)\le
\exp[\rho(e^{\pm\lambda}-1)]\), and the negative exponent is bounded by the positive one; the second follows termwise from the exponential series for \(0\le\lambda<3\).

For all real z, \(z^{2m}\le (2m)!\lambda^{-2m}e^{\lambda|z|}\), and \(e^{\lambda|z|}\le e^{\lambda z}+e^{-\lambda z}\).
Choose \(\lambda=16m/\mu\le1/8\). Since
\[
\frac{\mu\lambda^2}{2(1-\lambda/3)}
=\frac{128m^2/\mu}{1-\lambda/3}
\le \frac{24}{23}m,
\]
we obtain
\[
 \mathbb E(X-\mu)^{2m}
 \le 2(2m)!\lambda^{-2m}e^{24m/23}.
\]
Use \((2m)!\le (2m)^{2m}\), \(1-b=47/64\), and Markov's inequality:
\[
\Pr(X\le b\mu)
\le \frac{\mathbb E(X-\mu)^{2m}}{[(1-b)\mu]^{2m}}
\le2\left[\left(\frac{8}{47}\right)^2e^{24/23}\right]^m
=2\gamma^m.
\]
The elementary estimate \(e^{24/23}<3\) gives
\(\gamma<192/2209<1/8\).
Summing the bound over the p candidate residues x yields
\(\mathbb E_{\mathcal H}|L_{c,K}(\mathcal H)|\le2p\gamma^m\).
Markov with the r307 strict list threshold \(p^{3/4}\) gives
\[
q_c=\max_{|K|=u}\Pr(|L_{c,K}|>p^{3/4})
 \le2p^{1/4}\gamma^m
 \le2p^{1/4-\log8}<Q/2.
\]
The maximum over deterministic K is outside the probability, as required by r307. The estimate is uniform in K, x, and the sign.

## Parameter, law, and information checks

With \(t=\log p\ge70\log2>48\), \(m\le t+1\).
The function \((t+1)e^{-t/2}\) decreases for \(t\ge48\), and
\(128(t+1)e^{-t/2}+e^{-t}<1\) at \(t=48\). Thus \(n<p\).
Also \(n\ge2m\). The first 2m polynomial evaluations determine all coefficients by Vandermonde inversion, so \(H(\mathcal H)=2m\log p\), exactly. Every P(\ell) is uniform over G because its constant coefficient U_0 is independent uniform. It is independent of Y. With the same standard-integer representative convention for every \(\ell\), the **full integer lattice** laws \(Y+h_\ell\) are identical, not merely their residue projections. In particular the terminal signed marginals are uniform; the initial signed marginals omit u values.

The external short-list transfer selects s distinct base indices and one independent sign per index. Here k=s and the \(Y_j\) are independent, so for every allowed S,
\(H(F_S(Y))=s\log(p-u)=(1-\epsilon)s\log p\)
with
\(\epsilon=-\log(1-u/p)/\log p>0\);
\(\kappa=2m/s\). The available r307 entropy slack is exact:
\[
 1/4096-\kappa=\frac1{4096(8192m+1)}.
\]
Since \(u/p\le2/\sqrt p\), \(-\log(1-a)\le2a\) for a<=1/2, and t>=48,
\[
 \epsilon\le4/(e^{t/2}t)
 < 1/[4096(8192m+1)].
\]
For the last strict inequality, after multiplying by \(4096(8192m+1)t\), its left-to-right comparison is bounded by
\(16384(8192(1+1/48)+1/48)<1.4\cdot10^8<e^{24}\le e^{t/2}\).
Hence \(\epsilon+\kappa<1/4096=\eta\delta\beta'/16\).
Also \(\log(128e)<t/8\), as \(t>48\). Finally \(q_c<Q/2\) follows already from p>=2^70 and the displayed exponential power. All r307 parameter checks are explicit, even though m grows with p.

## Consequences, evidence level, and bridge boundary

Relative to r313's \(O_m(p^{1/2+1/(4m)})\) fixed-degree construction, this **discharges its open sqrt(p)-polylog(p) positive-tail question** by choosing m=ceil(log p) and proving an m-uniform high-moment bound. It does **not** close the fixed-number-of-base-indices problem: here k=s=8192ceil(log p)+1 grows, and H(H) grows quadratically in log p. It also does not supply a deterministic q=0 or all-realizations-distinct-shift certificate, a bounded-step Gaussian prime walk, or a source-safe Heartbeat X6 native realization. The r314 X6 capacity obstruction applies to a claimed same-prime linear raw six-axis realization of these k distinct independent source coordinates; this external construction itself makes no such native claim.

Computation: numerical cross-check of constants at p=2^70 (not itself prime) gives m=49, gamma≈0.0822547731, q-bound≈2.582e-48, epsilon-upper≈2.399e-12, entropy slack≈6.082e-10, and n/p≈1.826e-7. The proof uses exact moment identities and analytic inequalities for all primes p>=2^70; the decimal checks are illustrative only.

Status: source-exposed author-side mathematical derivation; no independent Native Result admission, no official Task completion and no Foundation promotion. Prior contribution and signed/ordered/source semantics remain separate.
