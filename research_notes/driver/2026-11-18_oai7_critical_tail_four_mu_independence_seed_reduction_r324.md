# OAI7 r324 — Critical coefficient with the original four-mean independence order

Date: 2026-11-18. Status: **Driver-line source-exposed mathematical proof**, not a fresh independent Native Result review or Task closure. Original OAI7 researcher EM-EMF6D046-5A2844 retains original frontier credit; r307, r315, r321, r322 and r323 retain their own source-verified contribution scope. The novelty here is a stronger uniform truncation-error calculation, preserving r323's sharp binomial lower-tail prefactor with *one-quarter* as many polynomial coefficients.

## Sharpened critical-length result

Fix
$$
b=17/64,\quad J=1-b+b\log b=0.3822439754975195\ldots,\quad
c_*=(4J)^{-1}=0.6540325447238404\ldots.
$$
For every sufficiently large prime \(p\), set
$$
u=\lceil\sqrt p\rceil,\quad \rho=u/p,\quad
n=\lceil c_*\sqrt p\log p\rceil,\quad \mu=n\rho,\quad
t=2\lceil2\mu\rceil,\quad s=k=4096t+1.
$$
Then the exact r322 shared polynomial schedule (same diagonal lattice displacement and the \(2k\) signed homomorphisms) meets all r307 entropy/marginal/list-tail hypotheses with
$$
\boxed{
H(\mathcal H)=t\log p,\quad
t=(4c_*+o(1))\log p,\quad
q_c=O((\log p)^{-1/2})\to0
}
$$
for every signed coordinate \(c\), uniformly over fixed deterministic test sets chosen before sampling. The preceding r323 point-mass argument used \(t\ge16\mu\); the new argument works at \(t\ge4\mu\), exactly the smaller order used in r322. Thus no enlarged seed or signed-index budget is needed to attain the sharp critical ceiling length.

## Improved truncated factorial-moment lemma

Let \(X=\sum_{i=1}^n I_i\) for \(t\)-wise independent Bernoulli(\(\rho\)) indicators, with \(\mu=n\rho\), \(t\le n\) even, and \(t\ge4\mu\). Fix \(0<b<1\), \(h=\lfloor b\mu\rfloor\), and \(h\ge1\). Let
$$
\mathsf H(z)=-z\log z-(1-z)\log(1-z),\quad
E_4(b)=4\bigl(\log4-1-\mathsf H(b/4)\bigr).
$$
Then, whenever \(4-b>1\) and \(\mu\ge2/b\),
$$
\boxed{
\Pr(X\le b\mu)
\le
\frac{e^{b\mu\rho}}{(1-b)\sqrt{\pi b\mu}}\,
e^{-J(b)\mu}
+2e^{-E_4(b)\mu}.
}
\tag{R324.1}
$$
At the value \(b=17/64\), 
$$
E_4(b)=0.56820853782048\ldots
>J(b)=0.38224397549752\ldots.
\tag{R324.2}
$$

**Proof.** For each \(0\le j\le h\), use the even inclusion-exclusion point-mass majorant from r323:
$$
{\bf1}_{\{X=j\}}
\le\binom Xj\sum_{r=0}^{m_j}(-1)^r\binom{X-j}{r},
$$
where \(m_j\) is the largest even integer at most \(t-j\). The expectations of all falling-factorial terms agree with \({\rm Bin}(n,\rho)\) by \(t\)-wise independence. The even Taylor remainder of \((1-\rho)^{n-j}\) consequently gives
$$
\Pr(X=j)-\Pr(B=j)
\le \frac{\mu^j}{j!}\,\frac{\mu^{m_j+1}}{(m_j+1)!},
\quad B\sim{\rm Bin}(n,\rho).
\tag{R324.3}
$$

Since \(t\) is even, if \(j\) is odd then \(m_j+1=t-j\); if \(j\) is even then \(m_j+1=t-j+1\). Summing all \(j\le h\) and dropping the parity restriction in each part bounds the *total* truncation error by
$$
\begin{split}
E_{\rm trunc}
&\le \frac{\mu^t}{t!}\sum_{j=0}^{h}\binom tj
+\frac{\mu^{t+1}}{(t+1)!}\sum_{j=0}^{h}\binom{t+1}j.
\end{split}\tag{R324.4}
$$

For any integer \(N\ge2h\), the standard entropy bound for binomial partial sums is
$$
\sum_{j=0}^{h}\binom Nj\le
\exp\bigl(N\mathsf H(h/N)\bigr).
\tag{R324.5}
$$
For completeness, take \(a=h/N\le1/2\): the binomial weights \(a^j(1-a)^{N-j}\) for \(j\le h\) are at least \(a^h(1-a)^{N-h}=\exp[-N\mathsf H(a)]\), while their weighted sum is at most one. The case \(h=0\) is immediate.

By \(N!\ge(N/e)^N\), each term in (R324.4) is bounded by
$$
\exp \Psi(N,h),\qquad
\Psi(N,h):=N\log(e\mu/N)+N\mathsf H(h/N),\quad N\in\{t,t+1\}.
$$
For real \(N\ge4\mu\) and \(0<h\le b\mu\), one has
$$
\partial_N\Psi(N,h)=\log\frac{\mu}{N-h}<0,\qquad
\partial_h\Psi(N,h)=\log\frac{N-h}{h}>0.
$$
Thus the maximum on \(N\ge4\mu,\ 0\le h\le b\mu\) is attained at \(N=4\mu,\ h=b\mu\), giving
$$
\Psi(N,h)\le
4\mu\bigl(1-\log4+\mathsf H(b/4)\bigr)
=-E_4(b)\mu.
$$
Both terms of (R324.4) are at most \(e^{-E_4(b)\mu}\). The independent binomial part obeys the r323 Poisson-prefactor upper bound:
$$
\Pr(B\le h)\le
\frac{e^{b\mu\rho}}{(1-b)\sqrt{\pi b\mu}}
e^{-J(b)\mu}.
$$
Equations (R324.3)–(R324.5) prove (R324.1). No full temporal independence was assumed.

## Implication for the exact r307 shared-data certificate

Use the original r322 setup with \(G=\mathbb F_p\), \(\Lambda=\mathbb Z^k\), independent initial \(Y_j\) uniform outside a fixed \(u\)-set, and
\(h_\ell=([P(\ell)]_p,\ldots,[P(\ell)]_p)\), with \(P\) a random degree-\((t-1)\) polynomial, at \(n\) distinct evaluation sites. Uniformity and \(t\)-wise independence of its values preserve the same identical *full-lattice* terminal law and signed-coordinate coverage setup.

For any deterministic \(K\) of size \(u\), signed \(c\) and start \(x\), the count of sampled hits of \(x+\phi_c(h_\ell)\) in \(K\) obeys (R324.1) with \(\mu=nu/p\). Counting \(p\) starts and applying Markov at the r307 list threshold \(p^{3/4}\) gives
$$
q_c\le p^{1/4}\left[
\frac{e^{b\mu\rho}}{(1-b)\sqrt{\pi b\mu}}e^{-J\mu}
+2e^{-E_4(b)\mu}\right].
\tag{R324.6}
$$
Because \(n=\lceil c_*\sqrt p\log p\rceil\) and \(\mu\ge c_*\log p\), the first term is \(O((\log p)^{-1/2})\). The second is \(O(p^{1/4-E_4(b)c_*})=O(p^{-0.1216268759\ldots})\). Hence the worst fixed-set tail tends to zero.

Moreover \(H(\mathcal H)=t\log p\) by recovery of the first \(t\) polynomial evaluations. With \(s=k=4096t+1\), the r307 budget holds because
$$
1/4096-t/s=1/[4096(4096t+1)]
$$
dominates \(\epsilon=-\log(1-u/p)/\log p=O(p^{-1/2}/\log p)\) for large \(p\). The original r307 logarithmic and parameter hypotheses are unchanged; the integrated-tail condition holds as \(R_0\le\max_cq_c\to0\).

## Scientific and admission boundary

r323 first proved critical-coefficient attainability using 16-mean independence. r324 keeps the *same critical-length result* and reduces its polynomial seed/required independent order by a factor asymptotically four, through the entropy-of-binomial-sums bound (R324.5). Original contributor identities and prior result proofs are retained. The strength claimed is a finite-cyclic external shared-sampling theorem; a typed ordered Heartbeat X6 Link/Port carrier, the true Gaussian-prime walk model, frozen Native Result and independent review remain separate.

Pinned predecessors: r307 Git baaaabaacaf8543f62a45a00cdfcf03e95389075; r321 Git 3c411d17ca496dfcfcdb91082643597981f6b9d2; r322 Git 1435b6f0c7ccb246d3d71c2177f531c36bdf1e97; r323 Git 9b9ad2468d3431939c5441832b10e1330f26cf42.
