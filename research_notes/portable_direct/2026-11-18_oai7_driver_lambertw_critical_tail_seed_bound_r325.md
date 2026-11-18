# OAI7 r325 — Lambert-W sharp entropy-envelope threshold for the exact critical shared schedule

Date: 2026-11-18. Status: **independent-portable mathematical derivation preserved during research-console unavailability**; source-exposed author-side work, **not** a Native Result, independent Driver review, CLAIM, Activity, Task completion, or parent completion. This contribution follows the historical EM-DVR-DEBB5E Driver derivation line; current active DA/session is unverified because the private gateway returned `BACKEND_IDENTITY_CHECK_UNAVAILABLE` with `operation_sent=false`. Preserve the original OAI7 researcher EM-EMF6D046-5A2844 and the distinct r307/r321/r322/r323/r324 author-side contributions.

## Theorem: improved finite-independence lower-tail lemma

Let $0<b<1$, $0<\rho<1$, $n\ge t$ and $t$ be a positive even integer. Let $I_1,\dots,I_n$ be $t$-wise independent Bernoulli($\rho$) variables, $X=\sum_i I_i$, $\mu=n\rho\ge2/b$, and $h=\lfloor b\mu\rfloor$. Define
\[
J(b)=1-b+b\log b,\qquad x_0=1/W_0(e^{-1})=3.5911214766686221\ldots,\qquad
a_b=b+x_0.
\]
Here $W_0$ denotes the principal real Lambert-W function. Equivalently, $x_0>e$ is the unique solution to $x(\log x-1)=1$, which is a definition requiring no special-function library.

**Claim.** For $t\ge a_b\mu$,
\[
\boxed{\Pr(X\le b\mu)
\le\frac{e^{-J(b)\mu}}{\sqrt\mu}
\left[
\frac{e^{b\mu\rho}}{(1-b)\sqrt{\pi b}}+
\frac{2}{\sqrt{2\pi a_b}}
\right].}\tag{R325.1}
\]
The bound requires only finite $t$-wise independence, not independent samples.

### Proof

Reuse the *pointwise* even Bonferroni mass majorant in r323 and the exact parity grouping in r324. Both follow directly from factorial moments of order at most $t$. For an independent $B\sim\mathrm{Bin}(n,\rho)$ the resulting error is
\[
\Pr(X\le h)-\Pr(B\le h)
\le T_t+T_{t+1},\qquad
T_N=\frac{\mu^N}{N!}\sum_{j=0}^h\binom Nj.\tag{R325.2}
\]
This is r324 equation (R324.4) with both nonnegative terms retained; it is valid for even $t$ and $h<t/2$.

For $0\le h\le N/2$, the binomial entropy bound and the Stirling lower bound including its square-root prefactor give
\[
T_N\le\frac{1}{\sqrt{2\pi N}}e^{\Psi(N,h)},\quad
\Psi(N,h)=N\log(e\mu/N)+N\mathsf H(h/N),\quad
\mathsf H(z)=-z\log z-(1-z)\log(1-z).
\tag{R325.3}
\]
Since $a_b>b+1$ and $a_b>2b$ for all $0<b<1$,
\[
\partial_N\Psi=\log\frac{\mu}{N-h}<0,\qquad
\partial_h\Psi=\log\frac{N-h}{h}>0
\]
on $N\ge a_b\mu, 0<h\le b\mu$, with continuous extension at $h=0$. Hence
\[
\Psi(N,h)\le\Psi(a_b\mu,b\mu)
=-E(a_b,b)\mu,
\quad
E(a,b)=a(\log a-1-\mathsf H(b/a)).
\tag{R325.4}
\]
An exact algebraic simplification gives
\[
E(a,b)=b\log b+(a-b)\log(a-b)-a,
\quad
E(a,b)-J(b)=(a-b)(\log(a-b)-1)-1.
\tag{R325.5}
\]
Thus **exactly** $E(a_b,b)=J(b)$, because $a_b-b=x_0$ and $x_0(\log x_0-1)=1$. There is no numerical approximation in this cancellation. Equations (R325.2)–(R325.4) now yield
\[
T_t+T_{t+1}\le\frac{2e^{-J(b)\mu}}{\sqrt{2\pi a_b\mu}}.\tag{R325.6}
\]
The binomial lower tail from r323 (R323.6)–(R323.7) is
\[
\Pr(B\le h)\le
\frac{e^{b\mu\rho}}{(1-b)\sqrt{\pi b\mu}}e^{-J(b)\mu},
\qquad\mu\ge2/b.\tag{R325.7}
\]
Combining (R325.6) and (R325.7) proves (R325.1).

The factor $\mu^{-1/2}$ from Stirling is essential: it permits **equality** at $E(a_b,b)=J(b)$. For the entropy-envelope estimate (R325.3), $a_b$ is its exact equality threshold, because $\partial_a E(a,b)=\log(a-b)>0$ for $a>b+1$. This is a threshold for this proof bound; no minimal-order claim is made for all possible $t$-wise-independent schemes.

## Corollary: smaller seed at the exact r321/r323 critical sampling coefficient

Use the same external finite-cyclic setup as r322–r324: $G=\mathbb F_p$, $u=\lceil\sqrt p\rceil$, $\rho=u/p$, $b=17/64$,
\[
c_*=[4J(b)]^{-1},\quad
n=\lceil c_*\sqrt p\log p\rceil,\quad
\mu=n\rho,\quad
t=2\left\lceil\frac{(b+x_0)\mu}{2}\right\rceil,\quad
s=k=4096t+1.
\]
Choose a uniformly random degree-$(t-1)$ polynomial $P\in\mathbb F_p[z]$, evaluate at the $n<p$ distinct sites, and use the original common integer lattice shifts
$h_\ell=([P(\ell)]_p,\dots,[P(\ell)]_p)\in\mathbb Z^k$.
Let the initial integer coordinates be independent uniform representatives of the complement of the same fixed (u)-set $B_0\subset\mathbb F_p$, with the original signed $±$ observers.

For all sufficiently large primes, $t\le n<p$. Vandermonde invertibility yields $t$-wise uniform polynomial evaluations and $H(\mathcal H)=t\log p$ exactly. Full-lattice terminal samples have identical laws, terminal signed marginals are uniform, and the initial signed marginals retain their specified entropy deficit.

By (R325.1), for every signed coordinate and fixed deterministic (u)-set $K$ chosen before the shared schedule, the same $p$-start counting/Markov step gives
\[
q_c\le\frac{p^{1/4}e^{-J(b)\mu}}{\sqrt\mu}
\left[
\frac{e^{b\mu\rho}}{(1-b)\sqrt{\pi b}}+
\frac{2}{\sqrt{2\pi(b+x_0)}}
\right]
=O((\log p)^{-1/2}).\tag{R325.8}
\]
Indeed $\mu\ge c_*\log p$, so $p^{1/4}e^{-J\mu}\le1$, and $\mu\rho\to0$. The unchanged r307 entropy budget holds because $t=O(\log p)$ and $\epsilon=O(p^{-1/2}/\log p)\ll[4096(4096t+1)]^{-1}$. The original integrated-tail bound follows as $R_0\le\max_c q_c\to0$.

The required independent polynomial coefficients have decreased from the r324 value $t\sim4\mu$ to
\[
\boxed{t\sim(b+x_0)\mu=3.8567464766686221\ldots\mu},
\]
a **3.5813380833%** asymptotic seed-length reduction at the same exact $n=\lceil c_*\sqrt p\log p\rceil$ and $q_c\to0$. For a fully rational practical sufficient choice, $t=2\lceil31\mu/16\rceil$ also works because $31/8>b+x_0$.

## Reproducibility, attribution, and unresolved target

The identity (R325.5) and the two monotonic derivatives furnish a symbolic proof. The decimal values are merely computational cross-checks:
$J(17/64)=0.3822439754975195594\ldots$,
$x_0=3.5911214766686221366\ldots$,
$b+x_0=3.8567464766686221366\ldots$,
$1-(b+x_0)/4=0.0358133808328444658\ldots$.
The finite proof uses no unproved target lemma, sorry/admit, or formal checker claim.

**Exact dependency/source lineage:** r307 @ baaaabaacaf8543f62a45a00cdfcf03e95389075 (integrated-tail model); r321 @ 3c411d17ca496dfcfcdb91082643597981f6b9d2 (universal necessary length coefficient, not re-proved here); r322 @ 1435b6f0c7ccb246d3d71c2177f531c36bdf1e97 (shared polynomial construction); r323 @ 9b9ad2468d3431939c5441832b10e1330f26cf42 (point-mass Bonferroni and binomial prefactor); r324 @ 10ac6bc662a67555d21d6a9e7285c03002449a53 (entropy binomial partial sum). The new contribution is the exact Lambert-W threshold and recovery of the Stirling prefactor in the **truncation** error.

This is an **external finite-cyclic shared-sampling** mathematical proposition. No claim is made that the diagonal lattice displacement already realizes a typed ordered native six-axis Heartbeat X6 path, preserves required native Port/Link/composite history, or solves the actual Gaussian-prime walk. Those are distinct open source-safe transfer problems. Formal original OAI7 task RS-OAI7-028-C-20261007-6F2A81 remains to be checked by live canonical control; this fallback preservation is not an operational task or review mutation.
