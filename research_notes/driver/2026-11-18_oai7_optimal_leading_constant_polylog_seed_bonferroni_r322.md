# OAI7 r322 — Sharp leading sample-length constant with polylogarithmic shared seed

Date: 2026-11-18. Driver-side source-exposed mathematical contribution in historical line EM-DVR-DEBB5E, **not** a Native independently accepted Result, official Task completion, DA authorization, Foundation promotion or Heartbeat-native X6/Gaussian-walk theorem. Preserve original researcher EM-EMF6D046-5A2844 and predecessor authors, especially r307 (integrated tail), r315 (polynomial schedule), r318/r319 (lower-tail obstructions) and r321 (repetition-independent sharp lower coefficient).

## Scope and result

Work in the r307 **external homogeneous finite-cyclic signed-coordinate model**. Fix
$$
\tau=\tfrac14,\quad\delta=\tfrac1{64},\quad
\beta=\beta'=\tfrac12,\quad\eta=\tfrac12,\quad
\xi=0,\quad b=\tau+\delta=\tfrac{17}{64},
$$
and write $J(b)=1-b+b\log b$, $c_*=[4J(b)]^{-1}\approx0.6540325447238404$. The prescribed r307 integrated-tail budget is $R_0\le111/4352$, with $u=\lceil\sqrt p\rceil$ and list-size threshold $p^{3/4}$.

**Theorem (matching leading coefficient).** For every fixed $c$ with $c_*<c<1$, and every sufficiently large prime $p$, one can construct a fully shared, highly dependent offset schedule, with
$$
n=\lceil c\sqrt p\log p\rceil,\quad
t=2\lceil32\log p\rceil,\quad
k=s=8192t+1,
$$
such that
$$
H(\mathcal H)=t\log p=O((\log p)^2),\qquad
\epsilon+\kappa<1/4096,
$$
every initial signed coordinate fails the specified coverage condition, every terminal signed coordinate is uniform, all full-lattice terminal sample laws coincide, and
$$
R_0\le \max_c q_c\le
p^{1/4}\!\left(e^{-(nu/p)J(b)}+p^{-100}\right)
\longrightarrow0.
$$
In particular every hypothesis of r307 (including the entropy/logarithmic side conditions) is satisfied. Combining this with the r321 lower coefficient, the **optimal asymptotic leading sample-length constant** in this specified homogeneous external family, permitting $k=s=O(\log p)$ and polynomial shared seeds of entropy $O((\log p)^2)$, is exactly
$$
\boxed{\lim_{p\to\infty}\frac{n_{\min}(p)}{\sqrt p\log p}
=\frac{1}{4(1-b+b\log b)}=c_* .}
$$
Here $n_{\min}(p)$ is the infimum over the stipulated r307-admissible external schemes with worst-fixed-set tail $R_0\le111/4352$, allowing the specified growth of base-index count and shared-seed entropy. This is **not** a fixed-$k$ optimum or a native geometric realization.

## 1. Construction and source/entropy checks

Let $G=\mathbb F_p$, $\Lambda=\mathbb Z^k$, and signed observers
$$
\phi_{j,+}(v)=v_j\bmod p,\qquad
\phi_{j,-}(v)=-v_j\bmod p\qquad(1\le j\le k).
$$
Choose an arbitrary fixed $u$-subset $B\subset G$. Draw independent $Y_j$ uniformly from the standard representatives of $G\setminus B$, put $A=Y$, and independently choose $t$ uniform polynomial coefficients $U_0,\ldots,U_{t-1}\in G$. Define
$$
P(z)=\sum_{a=0}^{t-1}U_a z^a,\quad
h_\ell=([P(\ell)]_p,\ldots,[P(\ell)]_p)\in\Lambda,
\quad 0\le\ell<n.
$$
For sufficiently large $p$, $t\le n<p$. Distinct indices mod $p$ have full-row-rank Vandermonde evaluations on up to $t$ points, hence $(P(\ell))_{\ell<n}$ is $t$-wise independent and each $P(\ell)$ is uniform. The first $t$ evaluations invert the coefficients, so the **whole shared vector** $\mathcal H=(h_\ell)_{\ell<n}$ has
$$
H(\mathcal H)=t\log p.
$$
Each $h_\ell$ has the same uniform-diagonal integer representative law and is independent of $Y$, so every full $\Lambda$-valued $Y+h_\ell$ has the same law as $Z=Y+h_0$. The terminal signed marginals are uniform, while each initial signed marginal omits $u\ge p^{1/2}$ residues and fails $(\tau,\beta)$ coverage.

For an independently signed $s$-subset of distinct base indices, $H(F_S(Y))=s\log(p-u)=(1-\epsilon)s\log p$, where
$$
\epsilon=-\frac{\log(1-u/p)}{\log p}=O((\sqrt p\log p)^{-1}),
\quad \kappa=\frac{t}{s}<\frac1{8192}.
$$
Thus $\epsilon+\kappa<1/4096=\eta\delta\beta'/16$ for all sufficiently large $p$. The r307 logarithmic condition $\log(128e)\le(\log p)/8$ also holds for sufficiently large $p$, and $n<p$ holds because $c\sqrt p\log p=o(p)$. The identical full-lattice laws and the single shared information cost are actual properties of the construction, not only claims about the residue projections.

## 2. A finite-degree Bonferroni–Laplace majorant

The key improvement over r315's coarse high-centered-moment estimate is an **even-degree polynomial majorant of an exponential**, whose expectation depends only on the available $t$-wise independence.

Let $I_1,\ldots,I_n$ be any $t$-wise independent Bernoulli($\rho$) variables for an **even** integer $t\le n$, with $X=\sum I_\ell$, $\mu=n\rho$. Let $\lambda>0$ and $z=1-e^{-\lambda}\in(0,1)$. For each integer $N\ge0$ define
$$
S_t(N)=\sum_{j=0}^t(-z)^j\binom Nj.
$$
Taylor's theorem applied to $(1-z)^N$ as a polynomial in $z$ (and $t$ even) gives the **pointwise exact bounds**
$$
(1-z)^N\le S_t(N)
\le(1-z)^N+z^{t+1}\binom N{t+1}.                    \tag{B1}
$$
For $N\le t$ the expressions are identical. For $N>t$, the remainder has the stated sign because its derivative of order $t+1$ is negative; its magnitude is at most $\binom N{t+1}z^{t+1}$ on $0\le z\le1$.

Since $\binom Xj$ is a degree-$j$ polynomial in the Bernoulli indicators (equivalently the sum over $j$-element products), $t$-wise independence yields
$$
\mathbb E S_t(X)=\sum_{j=0}^t(-z)^j\binom nj\rho^j
=\mathbb E S_t(B_n)
$$
for an independent binomial $B_n\sim\operatorname{Bin}(n,\rho)$. Using (B1) for this *comparison* binomial and $\mathbb E\binom{B_n}{t+1}=\binom n{t+1}\rho^{t+1}$, obtain
$$
\boxed{\mathbb E e^{-\lambda X}
\le(1-z\rho)^n+z^{t+1}\binom n{t+1}\rho^{t+1}
\le e^{-z\mu}+\frac{(z\mu)^{t+1}}{(t+1)!}.}            \tag{B2}
$$
No $(t+1)$-wise independence of the *actual* samples is assumed: the last factorial moment is evaluated only under the comparison **independent binomial law**, after matching the degree-$t$ polynomial.

For the lower-tail event $X\le b\mu$, Markov applied to $e^{-\lambda X}$ gives
$$
\Pr\{X\le b\mu\}
\le e^{\lambda b\mu}
\left(e^{-z\mu}+\frac{(z\mu)^{t+1}}{(t+1)!}\right). \tag{B3}
$$
Choose $\lambda=\log(1/b)$, $z=1-b$, so $z-\lambda b=J(b)$. Then
$$
\Pr\{X\le b\mu\}\le
e^{-\mu J(b)}
+e^{b\lambda\mu}\left(\frac{ez\mu}{t+1}\right)^{t+1}. \tag{B4}
$$

## 3. Uniform tiny truncation error and the r307 list-tail

For the chosen $n=\lceil c\sqrt p\log p\rceil$ with $c<1$, we have $\rho=u/p$ and $\mu=n\rho\le2\log p$ for sufficiently large $p$. Also $t\ge64\log p$. Consequently
$$
\frac{z\mu}{t+1}\le\frac1{32},
\quad
\log\!\left[e^{b\lambda\mu}
\left(\frac{ez\mu}{t+1}\right)^{t+1}\right]
\le 2b\lambda\log p+
64\log p\,(1-\log32)
<-100\log p
$$
for all sufficiently large $p$; here $b\lambda<1$. Hence the truncation contribution in (B4) is at most $p^{-100}$.

Fix *any deterministic* $u$-subset $K\subseteq G$, any start $x$, and any signed coordinate. Its $n$ indicators $\mathbf1_{\{x+\phi_c(h_\ell)\in K\}}$ are $t$-wise independent Bernoulli($u/p$), whether the sign is positive or negative, because the underlying polynomial evaluations are $t$-wise independent uniform field elements. Thus (B4) gives a **uniform** bound
$$
\Pr\left\{\sum_{\ell<n}\mathbf1_{\{x+\phi_c(h_\ell)\in K\}}
\le bnu/p\right\}
\le e^{-\mu J(b)}+p^{-100}.
$$
Sum over the $p$ possible starting residues and use Markov against $p^{3/4}$:
$$
q_c=\max_{\substack{K\subset G\\|K|=u}}
\Pr\{|L_{c,K}(\mathcal H)|>p^{3/4}\}
\le p^{1/4}\left(e^{-\mu J(b)}+p^{-100}\right).
$$
As $p\to\infty$, $\mu=(c+o(1))\log p$, hence $p^{1/4}e^{-\mu J(b)}=p^{1/4-cJ(b)+o(1)}\to0$ since $c>c_*$. The r307 integrated condition (IT) at $\xi=0$ follows for all sufficiently large $p$, even with all $2k$ coordinates sharing the same polynomial schedule. There is *no* need to assume the full $n$ indicators are independent.

## 4. Optimality and exact remaining scope

For any allowed external offset law, r321 proves that fixed positive worst-set list-tail budget $Q<1$ forces
$\liminf n/(\sqrt p\log p)\ge c_*$. The present polynomial schedules achieve any fixed coefficient $c>c_*$ arbitrarily close to that bound, with the r307 entropy and signed-index constraints satisfied. Hence the external homogeneous **leading constant is determined**, not merely its $\Theta(\sqrt p\log p)$ order.

The statement permits $k=s=\Theta(\log p)$ and shared-seed entropy $\Theta((\log p)^2)$. The fixed-$k$, constant-seed-entropy and deterministic-zero-tail variants remain separate problems. Most importantly, a finite-field polynomial schedule is an *external shared-displacement certificate*, not an admissible bounded-step Gaussian-prime schedule, and no ordered/source-safe Heartbeat X6/Port/Link carrier has been proved. Native Result, formal independent review, official Task and parent closure remain untouched.

Scientific provenance: the r307 transfer inequality, r315 polynomial-field idea, r318 Azuma/quantifier machinery, r312/r319 rate $c_*$ and r321 unrestricted-multiplicity lower bound are reused at their original statements. The new proof unit is the Bonferroni–Laplace $t$-wise upper certificate with $t=O(\log p)$, the sharp-rate parameter realization, and the matching external leading-constant synthesis.

Pinned source commits: r307 baaaabaacaf8543f62a45a00cdfcf03e95389075; r315 91555075510068632a53f02a5b2e1731d4bcb44e; r321 3c411d17ca496dfcfcdb91082643597981f6b9d2.
