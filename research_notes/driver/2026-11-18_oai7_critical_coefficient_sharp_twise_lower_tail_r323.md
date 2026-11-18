# OAI7 r323 — The exact critical leading coefficient is attained with a polylogarithmic-entropy common schedule

Date: 2026-11-18. Status: **Source-exposed Driver-line mathematical derivation; not an independent Native review, frozen Result, Task closure, or X6 realization.** This continues the historical derivation line EM-DVR-DEBB5E. The original OAI7 researcher EM-EMF6D046-5A2844, r307 author, r315 author, r319/r321 lower-bound contributions, and r322 upper-bound construction retain their exact earlier source attribution.

## Result: no fixed supercritical coefficient is necessary

Write

$$
b=\frac{17}{64},\qquad J(b)=1-b+b\log b>0,\qquad
c_*=\frac{1}{4J(b)}=0.6540325447238404\ldots.
$$

Let \(p\to\infty\) through primes and set

$$
u=\lceil\sqrt p\rceil,\quad \rho=u/p,\quad
n=\left\lceil c_*\sqrt p\log p\right\rceil,\quad
\mu=n\rho,\quad
t=2\lceil8\mu\rceil,\quad s=k=4096t+1.
$$

For every sufficiently large \(p\), the degree-\((t-1)\) shared-polynomial schedule of r322, with all \(2k\) signed coordinate maps, satisfies the unchanged r307 integrated-tail coverage-transfer hypotheses. Crucially, its **worst fixed deterministic test-set** failure probability obeys

$$
\boxed{
\max_c q_c\le
\frac{e^{b\mu\rho}}{(1-b)\sqrt{\pi b\mu}}\,
p^{1/4}e^{-J(b)\mu}
+p^{1/4}e^{-D\mu}
=O((\log p)^{-1/2})\longrightarrow0,
}
\tag{R323.1}
$$

where \(D=15\log(15/e)-1=24.6207530165\ldots\). The shared schedule entropy is exactly \(t\log p=O((\log p)^2)\); the common-integer-displacement / full-lattice identical-law and initial marginal deficiency properties are retained.

**Improvement over r322:** the schedule now has the *exact* critical leading expression \(n=\lceil c_*\sqrt p\log p\rceil\), not merely \(n=\lceil c\sqrt p\log p\rceil\) for every fixed \(c>c_*\). In view of r321's universal necessary coefficient, this attains the sharp leading coefficient in the specified growing-index external finite-group model, with no positive constant margin. No claim concerns the finite-\(p\) exact minimum, fixed-\(k\) variants, formal Native Result admission, or admissible ordered X6/Gaussian-prime paths.

## Exact finite-independence lower-tail estimate

The new ingredient is a stronger finite-independent Bernoulli estimate than the exponential-moment bound of r322. Let \(I_1,\ldots,I_n\) be \(t\)-wise independent Bernoulli(\(\rho\)), \(X=\sum I_\ell\), \(\mu=n\rho\), \(0<b<1\), \(h=\lfloor b\mu\rfloor\), and let \(t\le n\) be even with \(t\ge16\mu\). Assume \(\mu\ge 2/b\). Then

$$
\boxed{
\Pr(X\le b\mu)\le
\frac{e^{b\mu\rho}}{(1-b)\sqrt{\pi b\mu}}\,
e^{-J(b)\mu}+e^{-D\mu}.
}
\tag{R323.2}
$$

Here \(D=15\log(15/e)-1\), independent of \(b\), and the chosen \(b=17/64\) meets \(16-b>15\).

**Proof.** Fix an integer \(0\le j\le h\) and choose \(m_j\) to be the largest even integer at most \(t-j\). For every integer \(x\in[0,n]\), the even Bonferroni truncation gives the pointwise polynomial majorant

$$
{\bf1}_{\{x=j\}}\ \le\
\binom{x}{j}\sum_{r=0}^{m_j}(-1)^r\binom{x-j}{r}.
\tag{R323.3}
$$

Indeed, at \(x=j\) both sides equal 1; for \(x<j\) both are zero; for \(x>j\) the right side is nonnegative by the partial alternating-binomial identity (it is \(\binom{x}{j}\binom{x-j-1}{m_j}\) when \(m_j<x-j\), and zero otherwise).

Since each term has degree at most \(j+m_j\le t\), the \(t\)-wise factorial moments coincide with those of a binomial variable \(B\sim{\rm Bin}(n,\rho)\). Hence

$$
\begin{split}
\Pr(X=j)&\le
\binom nj\rho^j\sum_{r=0}^{m_j}(-\rho)^r\binom{n-j}{r}\\
&\le \Pr(B=j)+
\binom nj\rho^j\binom{n-j}{m_j+1}\rho^{m_j+1}\\
&\le \Pr(B=j)+\frac{\mu^j}{j!}
\frac{\mu^{m_j+1}}{(m_j+1)!}.
\end{split}\tag{R323.4}
$$

The second inequality is the elementary Taylor remainder for \((1-v)^{n-j}\) at \(v=\rho\in[0,1]\), with even truncation and remainder bounded by \(\binom{n-j}{m_j+1}\rho^{m_j+1}\); if \(m_j=n-j\) the remainder is zero.

For \(j\le h\le b\mu\), parity gives \(m_j+1\ge t-j\ge (16-b)\mu>15\mu\). Factorial Stirling's lower bound and monotonicity of \(v\mapsto(e\mu/v)^v\) for \(v\ge\mu\) imply

$$
\frac{\mu^{m_j+1}}{(m_j+1)!}
\le (e/15)^{15\mu}.
$$

Sum (R323.4) over \(0\le j\le h\); because \(\sum_{j\ge0}\mu^j/j!=e^\mu\), the aggregate truncation error is at most

$$
e^\mu(e/15)^{15\mu}=\exp[-D\mu],\qquad
D=15\log(15/e)-1.
\tag{R323.5}
$$

For the genuine binomial tail, \(\binom nj\rho^j\le\mu^j/j!\) and \((1-\rho)^{n-j}\le e^{-\mu+j\rho}\). Consequently,

$$
\Pr(B\le h)\le e^{b\mu\rho-\mu}
\sum_{j=0}^h\frac{\mu^j}{j!}
\le\frac{e^{b\mu\rho-\mu}}{1-b}\frac{\mu^h}{h!}.
\tag{R323.6}
$$

The last inequality follows by summing the descending geometric ratios \(j/\mu\le h/\mu\le b\). Since \(h=\lfloor b\mu\rfloor\ge b\mu/2\) under \(\mu\ge2/b\), Stirling's lower bound \(h!\ge\sqrt{2\pi h}(h/e)^h\), and the monotonicity of \(I(a)=1-a+a\log a\) on \(0<a<1\), give

$$
e^{-\mu}\frac{\mu^h}{h!}
\le\frac{1}{\sqrt{\pi b\mu}}\exp[-\mu I(h/\mu)]
\le\frac{e^{-J(b)\mu}}{\sqrt{\pi b\mu}}.
\tag{R323.7}
$$

Combining (R323.5)–(R323.7) proves (R323.2), with no assumption of full temporal independence.

## Shared schedule, exact quantifier order and entropy

Reuse the r322 construction verbatim except for the chosen \(n,t\): take \(Y_j\) independently uniform on standard integer representatives of \(\mathbb F_p\setminus B_0\), with \(|B_0|=u\), and \(P(a)=\sum_{r<t}U_ra^r\) with \(t\) independent uniform coefficients over \(\mathbb F_p\). For \(\ell=0,\ldots,n-1\), let the *single common lattice displacement* be

$$
h_\ell=([P(\ell)]_p,\ldots,[P(\ell)]_p)\in\mathbb Z^k,
$$

and use \(\phi_{j,\pm}(v)=\pm v_j\bmod p\). Since \(t\le n<p\) for large \(p\), the sample evaluations are \(t\)-wise independent uniform, and the first \(t\) recover the seed coefficients. Thus \(H(\mathcal H)=t\log p\) exactly. Every \(Y+h_\ell\) has the identical *full lattice* law, while the initial signed marginals omit \(u\) residues and the terminal signed marginals are uniform.

For any **fixed deterministic** \(u\)-set \(K\), any signed coordinate \(c\), and every start \(x\in\mathbb F_p\), \(X_{c,K,x}=\sum_\ell{\bf1}_{\{x+\phi_c(h_\ell)\in K\}}\) meets (R323.2) with \(\mu=nu/p\). Markov's inequality over the \(p\) start residues gives

$$
\Pr_{\mathcal H}\{|L_{c,K}(\mathcal H)|>p^{3/4}\}
\le p^{1/4}\Pr(X_{c,K,x}\le b\mu),
$$

and the bound does not depend on \(K,c,x\). Taking the maximum over deterministic \(K\) outside the probability gives (R323.1). Since \(\mu=n\lceil\sqrt p\rceil/p\ge c_*\log p\), \(p^{1/4}e^{-J(b)\mu}\le1\), while \(p^{1/4}e^{-D\mu}\le p^{1/4-Dc_*}=o(1)\). Also \(\mu\sim c_*\log p\) and \(\rho=O(p^{-1/2})\). Hence the new exact critical-length failure bound tends to zero at rate \(O(1/\sqrt{\log p})\).

For r307 set \(\tau=1/4,\delta=1/64,\beta=\beta'=1/2,\eta=1/2,\xi=0,T=p\). As before,

$$
\epsilon=-\log(1-u/p)/\log p,\qquad
\kappa=t/s,\quad
1/4096-\kappa=1/[4096(4096t+1)].
$$

Because \(t=O(\log p)\) and \(\epsilon=O(p^{-1/2}/\log p)\), the strict original entropy slack eventually holds. The original logarithmic prerequisite holds, and (R323.1) makes \(R_0\le\max_c q_c<111/4352\) eventually. This completes the transfer-model verification.

## Precise boundary and contributions

- New proof unit r323: pointwise even-Bonferroni **binomial point-mass** majorants and their summation preserve the \(1/\sqrt\mu\) Poisson lower-tail prefactor under \(t=O(\mu)\) independence.
- Reused: r307 transfer/quantifier model, r315 finite-independent polynomial device, r321 universal lower coefficient, and r322 signed-index/entropy construction.
- Result: the asymptotically optimal coefficient \(c_*\) is now achieved by the **exact ceiling length** \(\lceil c_*\sqrt p\log p\rceil\), not just approached from fixed larger constants. The finite-\(p\) optimum, seed entropy minimization, fixed-\(k\) case, source-safe native X6 Link/Port mapping and Gaussian-prime-walk realization remain separate objectives.

Source pins: r307 @ baaaabaacaf8543f62a45a00cdfcf03e95389075; r315 @ 91555075510068632a53f02a5b2e1731d4bcb44e; r321 @ 3c411d17ca496dfcfcdb91082643597981f6b9d2; r322 @ 1435b6f0c7ccb246d3d71c2177f531c36bdf1e97. Original OAI7 task is RS-OAI7-028-C-20261007-6F2A81; this driver-side file is source-exposed evidence, not a replacement for its original researcher-authored frozen Result.
