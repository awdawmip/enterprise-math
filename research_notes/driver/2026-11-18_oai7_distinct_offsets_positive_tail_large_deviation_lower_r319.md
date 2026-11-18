# OAI7 r319 — Positive-tail large-deviation obstruction for pairwise-distinct shared offsets

Date: 2026-11-18. Source-exposed mathematical continuation in the historical Driver line EM-DVR-DEBB5E; no independent Native Result admission, no official Task completion and no native X6 realizability assertion. Original research provenance remains with EM-EMF6D046-5A2844 and the distinct-schedule hypergeometric lower-bound contributor of r312. This paper adds a concentration argument to turn the r312-style *zero-tail* obstruction into a **positive-tail** obstruction for the same distinct-offset class.

## Scope and link to r318

The general arbitrary-repetition r318 theorem, Git f770d2b71bf6371679b37dc9686603fb85abec19, proved \(\liminf n/(\sqrt p\log p)\ge1/4\) for every fixed worst-set tail failure budget \(Q<1\). Distinct offsets permit a stronger hypergeometric lower tail because the number of hits is an unweighted hypergeometric variable. The present theorem needs pairwise distinct offsets in **every** realization; r315 does not assert that property and is not silently imported into this narrower class.

Pinned previous results: r307 at baaaabaacaf8543f62a45a00cdfcf03e95389075; r312 at 34ac9052d5acd8cadb0ea75bf30d4fe07e346e70; r318 at f770d2b71bf6371679b37dc9686603fb85abec19.

## Theorem 1: Exact finite lower bound for any random distinct-offset schedule

Let \(G\) be a finite group of order \(p\), let \(1\le u\le p\), \(1\le n\le p\), \(b\ge0\), and \(0\le L_*\le p\). Let \(W=(w_1,\ldots,w_n)\) be an arbitrary random vector whose entries are pairwise distinct for every realization. For each fixed deterministic \(u\)-subset \(K\subset G\), put
\[
 L_K(W)=\left\{x\in G:
 \sum_{\ell=1}^n{\bf1}_{\{x+w_\ell\in K\}}\le bnu/p\right\},
\quad
 q=\max_{|K|=u}\Pr_W\{|L_K(W)|>L_*\}.
\]
Set \(j_*=\lfloor bnu/p\rfloor\) and define the exact hypergeometric tail
\[
 T(p,n,u,b)=\sum_{j=0}^{\min(j_*,n,u)}
       \frac{\binom n j\binom{p-n}{u-j}}{\binom p u},
\]
using the standard zero value for impossible binomial choices. Then
\[
 \boxed{\quad
 q\ge1-\exp\left[
  -\frac{\bigl(pT(p,n,u,b)-L_*\bigr)_+^2}{8un^2}
 \right].\quad} \tag{D1}
\]
No temporal independence, uniform marginal sampling or randomness of \(W\) is required. Only pairwise distinct entries of each realization are required.

### Proof

Fix any realized pairwise-distinct \(w\). Choose \(K\) uniformly among all \(u\)-subsets of \(G\), independent of \(w\). For every \(x\in G\), the \(n\) points \(x+w_\ell\) are distinct; consequently the number of them belonging to random \(K\) has the hypergeometric law
\[
 \Pr_K\!\left(\sum_\ell{\bf1}_{\{x+w_\ell\in K\}}=j\right)
 =\binom n j\binom{p-n}{u-j}/\binom p u.
\]
It follows by summing over \(x\) that
\[
 \mathbb E_K|L_K(w)|=pT(p,n,u,b),                   \tag{1}
\]
independently of the particular distinct-offset arrangement.

If \(K,K'\) differ by swapping one included element with one excluded element, the total hit count can change only for at most \(2n\) translated starting points. Therefore
\[
 \bigl||L_K(w)|-|L_{K'}(w)|\bigr|\le2n.            \tag{2}
\]
Exposing \(K\) by \(u\) uniform draws without replacement and coupling two choices at each exposure step by a label transposition, (2) bounds each conditional-expectation martingale difference by \(2n\). Azuma's inequality gives
\[
 \Pr_K\{|L_K(w)|\le pT-t\}
       \le \exp[-t^2/(8un^2)].
\]
Taking \(t=(pT-L_*)_+\) when positive, then averaging over the arbitrary \(W\) and using that the maximum over fixed deterministic \(K\) dominates their average, proves (D1). The order of quantifiers is exactly the r307 worst-set tail order. \(\square\)

## Theorem 2: Sharp necessary logarithmic-scale coefficient for positive tails

Let \(p\) tend to infinity through primes, \(u=\lceil\sqrt p\rceil\), \(L_*=p^{3/4}\), and take the r307/r312 counting threshold \(b=17/64\). Define
\[
 J(b)=1-b+b\log b>0,\qquad
 c_*=\frac{1}{4J(b)}=0.6540325447\ldots.
\]
For every sequence of random *pairwise-distinct* shared-offset schedules of lengths \(n_p\) such that the corresponding worst-fixed-set failure probabilities satisfy \(q_p\le Q<1\) eventually, necessarily
\[
 \boxed{\quad
 \liminf_{p\to\infty}\frac{n_p}{\sqrt p\log p}
 \ge c_*.\quad}                                     \tag{D2}
\]
More quantitatively: for every fixed \(0<\varepsilon<c_*\), if
\(1\le n\le(c_*-\varepsilon)\sqrt p\log p\), then uniformly in the distribution and arrangement of the distinct offsets,
\[
 q_p\ge1-\exp\left[
  -\Omega_\varepsilon
  \bigl(p^{\varepsilon J(b)}/\log^{O(1)}p\bigr)
 \right]\longrightarrow1.                          \tag{3}
\]
This is a necessary coefficient. It does not construct a schedule at \(c_*\).

### Proof of the hypergeometric lower-tail exponent

Let \(\mu=nu/p\), so \(\mu=O(\log p)\) in the claimed range, and choose \(j=\lfloor b\mu\rfloor\). By the exact hypergeometric formula,
\[
 T(p,n,u,b)\ge
 \binom n j\binom{p-n}{u-j}/\binom p u.              \tag{4}
\]
For \(u=\lceil\sqrt p\rceil\), \(n\le C\sqrt p\log p\), and \(j\le b\mu=O(\log p)\), expand the last fraction as
\[
 \frac{\binom n j\binom{p-n}{u-j}}{\binom p u}
 =\binom n j\frac{(u)_j}{(p)_j}
  \prod_{i=0}^{u-j-1}
       \left(1-\frac{n-j}{p-j-i}\right).             \tag{5}
\]
The falling factorials in (5) satisfy, uniformly over the stated \(n,j\),
\[
 \binom n j\frac{(u)_j}{(p)_j}
 =\frac{\mu^j}{j!}(1+o(1)),
\qquad
 \prod_{i=0}^{u-j-1}\left(1-\frac{n-j}{p-j-i}\right)
 =e^{-\mu}(1+o(1)).                                 \tag{6}
\]
For clarity, the logarithmic relative errors are bounded by
\(O(j^2/n+j^2/u+j^2/p+nu(n+u)/p^2+jn/p+ju/p)\);
these are \(o(1)\), including when \(j=0\). Here \(j^2/n=O(n/p)\) because \(j\le bnu/p\) and \(u=O(\sqrt p)\). Thus (4)–(6) give uniformly
\[
 T(p,n,u,b)\ge e^{-\mu}\frac{\mu^j}{j!}(1+o(1)).
\]
Stirling's estimate, with the bounded-\(\mu\) case treated directly at \(j=0\), yields
\[
 \log T(p,n,u,b)
 \ge-\mu J(b)-O(\log(\mu+2))-O(1)+o(1).              \tag{7}
\]
The conversion \(j=\lfloor b\mu\rfloor\) changes the exponent by only \(O(1)\) for large \(\mu\).

For \(n\le(c_*-\varepsilon)\sqrt p\log p\), and \(u/\sqrt p\to1\), eventually
\[
 \mu\le(c_*-\varepsilon/2)\log p.
\]
Equation (7) then gives, uniformly in the entire specified \(n\) range,
\[
 pT(p,n,u,b)
 \ge\frac{p^{3/4+\varepsilon J(b)/2}}{(\log p)^{O(1)}}.
\]
It dominates \(L_*=p^{3/4}\) and \(n\sqrt u=O(p^{3/4}\log p)\) by a positive power of \(p\). Insert into (D1) to obtain (3). As in r318, a subsequence with asymptotic coefficient strictly below \(c_*\) contradicts any fixed bound \(q_p\le Q<1\). \(\square\)

## Interpretation and contribution boundaries

r312 had already derived the same numerical coefficient \(c_*\) as a **zero-failure** necessary condition for pairwise-distinct schedules. r319 does not claim that coefficient as newly discovered. Its new contribution is the proof that the same coefficient is necessary even for every fixed **positive** worst-set failure allowance, via concentration over the deterministic-test-set ensemble. r318 remains the broader law-independent result for schedules allowing repetitions, with the weaker \(1/4\) coefficient.

The complete order \(\Theta(\sqrt p\log p)\) from r318 plus r315 remains true in the homogeneous external finite-cyclic certificate class. No statement here upgrades the special distinct-offset constant to all correlated schedules, nor establishes an actual bounded-step Gaussian-prime walk, a typed native X6/Link/Port carrier, formal Result acceptance, official Task closure or Foundation status.

Independent Native review and Source/Activity admission continue to require exact frozen Result evidence and current contribution/authority checks.
