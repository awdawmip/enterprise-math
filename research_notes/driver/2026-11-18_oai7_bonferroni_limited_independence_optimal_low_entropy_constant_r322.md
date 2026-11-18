# OAI7 r322 — Optimal positive-tail leading coefficient with a polylogarithmic-entropy shared schedule

Date: 2026-11-18. **Source-exposed author-side mathematical proof, not a Native independent review or admitted Result.** Continues the historical Driver research line EM-DVR-DEBB5E, preserving earlier OAI7 researcher EM-EMF6D046-5A2844 and the independent contributions of r307 (integrated list-tail transfer), r315 (growing-wise-independence construction), r319 (distinct-offset bound), and r321 (universal repeated-offset lower bound). This note contributes a new *matching low-entropy upper construction* using Bonferroni truncation; it does not reassign the lower-bound discovery.

## The matching theorem

Fix \(b=17/64\), \(z=1-b=47/64\), \(J(b)=1-b+b\log b>0\) and
\[
c_*=\frac1{4J(b)}=0.6540325447238404\ldots.
\]
For **every fixed constant \(c>c_*\)** and all sufficiently large primes \(p\), set
\[
u=\lceil\sqrt p\rceil,\quad \rho=u/p,\quad
n=\lceil c\sqrt p\log p\rceil,\quad\mu=n\rho,
\]
let \(t\) be the smallest **even** integer at least \(4\mu\), and put
\[
s=k=4096t+1,\qquad G=\mathbb F_p,\qquad \Lambda=\mathbb Z^k.
\]
There is a common-vector \(n\)-sample displacement schedule \(\mathcal H\) supported on at most \(p^t\) schedules such that:

1. The full \(\Lambda\)-valued variables \(Y+h_\ell\) have **one identical law** for all \(\ell\); every initial signed marginal fails the \((1/4,1/2)\) coverage condition, while all terminal signed marginals are exactly uniform.
2. All \(2k\) signed coordinates satisfy, **uniformly over every fixed deterministic** \(K\subset G\) of size \(u\),
\[
q_c=\max_{|K|=u}\Pr_{\mathcal H}\!\left\{\left|
 \left\{x\in G:\ \sum_{\ell<n}{\bf1}_{\{x+\phi_c(h_\ell)\in K\}}\le bnu/p\right\}
 \right|>p^{3/4}\right\}
\le 2p^{1/4}e^{-J(b)\mu}
\le 2p^{1/4-cJ(b)}\longrightarrow0.
\]
3. The shared-data entropy is **exactly**
\[
H(\mathcal H)=t\log p=O_c((\log p)^2),
\]
and with the indicated \(s=k\), the original r307 entropy requirement
\(\epsilon+\kappa<1/4096=\eta\delta\beta'/16\) holds for all sufficiently large \(p\), where \(\kappa=t/s\) and \(\epsilon=-\log(1-u/p)/\log p\), with \(\eta=1/2,\delta=1/64,\beta=\beta'=1/2,\tau=1/4,T=p,\xi=0\).

Together with the verified lower bound **as stated** in r321, this proves that, **in this finite-cyclic shared-schedule model allowing \(k=s=O_c(\log p)\) and shared entropy \(O_c((\log p)^2)\)**, the infimum asymptotic leading coefficient for a positive fixed worst-set failure budget is precisely \(c_*\). Precisely, for every fixed \(c>c_*\) a low-entropy schedule exists with \(q_c\to0\), whereas every schedule (even of arbitrarily large entropy or with repeats) with \(q_p\le Q<1\) eventually has \(\liminf n_p/(\sqrt p\log p)\ge c_*\). There is no assertion of attainability *at* the exact boundary \(c=c_*\).

## Construction and independent indicators

Let \(B\subset G\) be a deterministic set of cardinality \(u\). Draw independent \(Y_j\), each uniform over the standard integer representatives of \(G\setminus B\), for \(1\le j\le k\), and put \(Y=(Y_1,\dots,Y_k)\in\Lambda\). Independently draw \(t\) uniform coefficients \(U_0,\dots,U_{t-1}\in\mathbb F_p\) and let
\[
P(a)=\sum_{r=0}^{t-1}U_r a^r,\qquad a\in\mathbb F_p.
\]
For \(\ell=0,\dots,n-1\), define the **one common integer displacement**
\[
h_\ell=\big([P(\ell)]_p,\dots,[P(\ell)]_p\big)\in\Lambda.
\]
For sufficiently large \(p\), \(t\le n<p\). Vandermonde invertibility makes evaluations at any \(t\) distinct indices jointly uniform; each individual evaluation is uniform and independent of \(Y\). Consequently all full-lattice \(Y+h_\ell\) have the same distribution, and the first \(t\) evaluations recover the coefficients exactly, proving \(H(\mathcal H)=t\log p\).

Use the \(2k\) signed homomorphisms \(\phi_{j,\pm}(v)=\pm v_j\bmod p\). Each fixed coordinate's sequence \(\phi_c(h_\ell)\) is \(t\)-wise independent uniform on \(G\). Fix one such \(c\), one **deterministic** \(K\) of size \(u\), and \(x\in G\). Then \(X=\sum_{\ell<n}{\bf1}_{\{x+\phi_c(h_\ell)\in K\}}\) is a sum of \(t\)-wise independent Bernoulli(\(\rho\)) variables, with \(\mathbb EX=\mu\). No independence across all \(n\) samples is assumed.

## Even Bonferroni truncation: exact Chernoff exponent from finite independence

For any integer \(X\in[0,n]\), \(0<z<1\), and even integer \(t\le n\), the alternating Bonferroni inequality gives the **pointwise** majorant
\[
(1-z)^X\le \sum_{j=0}^t(-z)^j\binom Xj.
\tag{B1}
\]
For example, the right side is the even inclusion-exclusion truncation of the probability that none of \(X\) independently \(z\)-thinned events occurs. All its coefficients involve only moments of degree \(\le t\).

Taking expectation and using \(t\)-wise independence,
\[
\begin{aligned}
\mathbb E b^X
&\le\sum_{j=0}^t(-z)^j\binom nj\rho^j\\
&\le(1-z\rho)^n+\binom n{t+1}(z\rho)^{t+1}\\
&\le e^{-z\mu}+\frac{(z\mu)^{t+1}}{(t+1)!}.
\end{aligned}\tag{B2}
\]
The middle bound is Taylor's exact remainder estimate for the polynomial \((1-v)^n\) at \(v=z\rho\in[0,1]\); for \(t=n\) the remainder vanishes.

Since \(b\in(0,1)\), the event \(X\le b\mu\) forces \(b^X\ge b^{b\mu}\). Hence
\[
\Pr(X\le b\mu)
\le b^{-b\mu}\left(e^{-z\mu}+\frac{(z\mu)^{t+1}}{(t+1)!}\right).
\tag{B3}
\]
The first term is \(\exp[-(z+b\log b)\mu]=e^{-J(b)\mu}\). For the second, \((t+1)!\ge((t+1)/e)^{t+1}\) and \(t+1\ge4\mu\), giving
\[
b^{-b\mu}\frac{(z\mu)^{t+1}}{(t+1)!}
\le \exp[-C_b\mu],\quad
C_b=4\log\frac4{ez}+b\log b
=2.4279883465\ldots>J(b)=0.3822439754\ldots.
\tag{B4}
\]
Here \(ez/4<1\), so replacing \(t+1\) by its lower bound \(4\mu\) is valid. Therefore
\[
\boxed{\Pr(X\le b\mu)\le2e^{-J(b)\mu}.}\tag{B5}
\]

For a fixed \(K,c\), sum (B5) over all \(p\) possible starts \(x\) and apply Markov to \(L_{c,K}\):
\[
\Pr(|L_{c,K}|>p^{3/4})\le 2p^{1/4}e^{-J(b)\mu}.
\tag{B6}
\]
This is uniform in \(K\) and \(c\), so taking the maximum over deterministic \(K\) **outside** the probability retains precisely r307's quantifier order. Since \(u\ge\sqrt p\), \(\mu\ge c\log p\), proving the claimed decay for every \(c>c_*\).

## Shared-entropy budget and boundary

Let \(S\) select \(s=k\) distinct base indices and one sign at each, as in the original shared-entropy transfer model. Independence of the \(Y_j\) implies
\[
H(F_S(Y))=s\log(p-u)=(1-\epsilon)s\log p,\quad
\epsilon=-\log(1-u/p)/\log p.
\]
The schedule entropy ratio is \(\kappa=t/s=t/(4096t+1)\), so the exact slack is
\[
\frac1{4096}-\kappa=\frac1{4096(4096t+1)}.
\]
Because \(t=O_c(\log p)\) and \(u/p=O(p^{-1/2})\), \(\epsilon=O(p^{-1/2}/\log p)\) is eventually strictly smaller than this positive slack. The log prerequisite \(\log(128e)\le(\log p)/8\) also holds eventually, and (B6) makes \(R_0\le\max_c q_c<111/4352\) eventually. Thus the exact r307 hypotheses hold with \(H(\mathcal H)=t\log p\), not an unrecorded \(n\log p\) independent-sample cost.

The result closes the **leading asymptotic coefficient** for the specified abstract external finite-group positive-tail/low-entropy class, subject to r321's lower theorem. It does not solve the fixed-\(k\) problem, the minimal seed constant, the finite-\(p\) exact optimum, or the typed ordered native X6/Gaussian-prime-walk realization. No change to original author provenance, formal Task ownership, Native Result admission or Foundation state follows from publication of this note.

## Source relations and falsifiable checks

- r307 integrated list-tail transfer, original conditional information/slack and deterministic-\(K\) quantifiers: \`research_notes/driver/2026-11-18_oai7_integrated_list_tail_transfer_r307.md\`, pinned main commit \`baaaabaacaf8543f62a45a00cdfcf03e95389075\`.
- r315 logarithmic-wise-independent polynomial schedule and information budget: \`research_notes/driver/2026-11-18_oai7_logarithmic_independence_sqrt_p_log_p_schedule_r315.md\`, pinned \`91555075510068632a53f02a5b2e1731d4bcb44e\`.
- r319 distinct-offset lower coefficient: \`research_notes/driver/2026-11-18_oai7_distinct_offsets_positive_tail_large_deviation_lower_r319.md\`, pinned \`d292f14db079dd59fe12b6ee2ce638afb6617723\`.
- r321 arbitrary-repeat lower coefficient (new matching lower theorem, **different contribution**): \`research_notes/driver/2026-11-18_oai7_arbitrary_repetitions_sharp_distinct_class_lower_coefficient_r321.md\`, pinned \`3c411d17ca496dfcfcdb91082643597981f6b9d2\`.
- Calculation check (illustrative, not a substitute for the inequalities): \(b=17/64\), \(J(b)=0.38224397549751954\), \(C_b=2.4279883465755354\), \(c_*=0.6540325447238404\). Standard finite Bernoulli inclusion-exclusion and real Taylor remainders suffice; no unproved target premise or formal checker exception is used.
