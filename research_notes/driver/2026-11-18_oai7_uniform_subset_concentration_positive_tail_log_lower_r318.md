# OAI7 r318 — A logarithmic lower bound even for positive small-list failure budgets

Date: 2026-11-18. New source-exposed Driver-side mathematical argument, in the historical EM-DVR-DEBB5E line; this file is not a native independently accepted Result or proof of active DA authority. Preserve original OAI7 research contributor EM-EMF6D046-5A2844 and prior r307/r309/r312/r315/r317 authorship. The proof concerns an external finite-group/shared-offset certificate, not an admissible Heartbeat native X6 path.

## Question and exact dependencies

The r315 polynomial schedule provides length \(\lceil128\sqrt p\lceil\log p\rceil\rceil\) with the r307 uniform worst-deterministic-set *positive* small-list tail below \(111/8704\). The r317 synthesis reused r309 to show only a constant-times-\(\sqrt p\) necessary bound for positive tails, leaving open whether the logarithm is essential.

The present argument adds a **uniform-subset concentration step** beyond r309's first-moment hypergeometric bound. It proves the logarithmic factor cannot be removed, even when samples are arbitrarily dependent and the allowed failure probability is any fixed constant below one. The r309 hypergeometric formula is reused and credited, not recast as a new result.

Pinned predecessors:
- r307: Git baaaabaacaf8543f62a45a00cdfcf03e95389075; integrated list-tail transfer definition.
- r309: Git 332948fc474a6747f6f6ee12de87d4014230a314; universal hypergeometric first-moment bound.
- r315: Git 91555075510068632a53f02a5b2e1731d4bcb44e; constructive \(O(\sqrt p\log p)\) positive-tail upper certificate.
- r317: Git ddbc4a91ba8e775ac3cc186b45af2afb78a15005; earlier \(\Omega(\sqrt p)\) positive-tail synthesis.

## Theorem 1 — Finite lower bound valid for any schedule law

Let \(G\) be any finite group of order \(p\), written additively for convenience. Let \(1\le u\le p\), \(n\ge1\), \(b\ge0\), and let \(W=(w_1,\ldots,w_n)\) have **any** joint probability law in \(G^n\), including deterministic, correlated, repeated and adaptive offsets. For each deterministic \(u\)-element set \(K\subseteq G\), define
\[
  L_K(W)=\left\{x\in G:
  \sum_{\ell=1}^n {\bf1}_{\{x+w_\ell\in K\}}
              \le bnu/p\right\},\quad
  q=\max_{|K|=u}\Pr_W\{|L_K(W)|>L_*\},
\]
where \(0\le L_*\le p\) is real. Put
\[
 A_{p,n,u}=
 \frac{\binom{p-\min(n,p)}{u}}{\binom pu},
 \qquad\binom{a}{u}=0\ \text{if }a<u.
\]
Then
\[
 \boxed{\quad
 q\ \ge\
 1-\exp\!\left[
 -\,\frac{\bigl(pA_{p,n,u}-L_*\bigr)_+^2}{8un^2}
 \right].\quad} \tag{T1}
\]
The theorem is valid with no randomness or independence of the offsets. It assumes only that \(K\) is selected *before* \(W\), as in r307.

### Proof

Fix a realized vector \(w\), let \(d\le \min(n,p)\) count its distinct offsets and choose \(K\) uniformly among all \(u\)-subsets of \(G\). Define the number of uncovered starting points
\[
 V_w(K)=\bigl|\{x\in G:\ x+w_\ell\notin K
                         \text{ for every }\ell\}\bigr|.
\]
Since \(b\ge0\), \(V_w(K)\le |L_K(w)|\) for every \(K\). The exact expectation, by translating the \(d\) distinct offsets for each \(x\), is
\[
 \mu_w=\mathbb E_K V_w(K)
 =p\frac{\binom{p-d}{u}}{\binom pu}
 \ge p A_{p,n,u}.                                      \tag{1}
\]
The final inequality and its hypergeometric source are precisely the r309 combinatorial input.

If two \(u\)-subsets \(K,K'\) differ by exchanging one selected element for one unselected element, then
\[
             |V_w(K)-V_w(K')|\le2n.                     \tag{2}
\]
Indeed, a changed residue can affect at most \(n\) translated starting points, so removing one residue and adding another can affect at most \(2n\).

Expose a uniform \(u\)-subset by \(u\) successive draws without replacement. For two possible choices at any exposure step, swapping those two labels gives a bijection between future completions, with final subsets differing by at most one exchange. Hence the Doob conditional expectations at that step differ by at most \(2n\), by (2). The bounded-difference Azuma inequality therefore gives the conservative bound
\[
 \Pr_K\{V_w(K)\le\mu_w-t\}
        \le \exp[-t^2/(8un^2)]\quad(t\ge0).             \tag{3}
\]
If \(pA_{p,n,u}>L_*\), use \(t=\mu_w-L_*\ge pA_{p,n,u}-L_*\); otherwise the proposed lower bound is zero and trivial. Equations (1)–(3) show **for every realized \(w\)** that
\[
 \Pr_K\{|L_K(w)|>L_*\}
 \ge1-\exp[-(pA_{p,n,u}-L_*)_+^2/(8un^2)].
\]
Average over the arbitrary law of \(W\), interchange the finite \(K,W\) expectations, and note that the maximum over fixed deterministic \(K\) is at least their average. This proves (T1) with the r307 quantifier order intact. \(\square\)

## Theorem 2 — Positive-tail schedules require \(\sqrt p\log p\)

Set \(u=\lceil\sqrt p\rceil\), \(L_*=p^{3/4}\), and let \(p\to\infty\) through primes (the proof also holds for group orders \(p\)). For any sequence of arbitrary joint offset laws with corresponding worst-set probabilities \(q_p\), if there is a fixed \(Q<1\) such that \(q_p\le Q\) eventually, then
\[
 \boxed{\quad
 \liminf_{p\to\infty}\frac{n_p}{\sqrt p\,\log p}
 \ge\frac14.\quad}                                    \tag{T2}
\]
More precisely, for each fixed \(0<\varepsilon<1/4\), if
\(1\le n\le(1/4-\varepsilon)\sqrt p\log p\), then uniformly over all offset laws
\[
 q_p\ \ge\
 1-\exp\!\left[-\Omega_\varepsilon
                   \bigl(p^\varepsilon/\log^2p\bigr)\right]
 \longrightarrow1.                                    \tag{4}
\]

### Proof

For \(n+u-1<p\), the hypergeometric avoidance probability has the exact product
\[
 A_{p,n,u}=\prod_{j=0}^{u-1}
                  \left(1-\frac n{p-j}\right).
\]
Using \(\log(1-z)\ge-z/(1-z)\), \(0\le z<1\), yields
\[
 A_{p,n,u}
 \ge\exp\left[-\frac{un}{p-u+1-n}\right].               \tag{5}
\]
For \(n\le(1/4-\varepsilon)\sqrt p\log p\) and \(u=\lceil\sqrt p\rceil\), the exponent on the right of (5) is at most
\((1/4-\varepsilon/2)\log p\) for all sufficiently large \(p\), uniformly in the stipulated \(n\). Thus
\[
       pA_{p,n,u}\ge p^{3/4+\varepsilon/2}
       \quad\text{and}\quad
       pA_{p,n,u}-p^{3/4}\ge\tfrac12p^{3/4+\varepsilon/2}.
\]
Meanwhile \(un^2=O_\varepsilon(p^{3/2}\log^2p)\). Substitution into (T1) yields (4). If \(\liminf n_p/(\sqrt p\log p)<1/4\), there is a fixed positive \(\varepsilon\) and an infinite subsequence satisfying (4), contradicting \(q_p\le Q<1\). This proves (T2). \(\square\)

The asymptotic constant \(1/4\) is a **necessary** coefficient here, not a matching constant for the r315 upper construction. No claim is made at exact \(n\sim(1/4)\sqrt p\log p\).

## Consequence for r307 and r315

In r315's homogeneous prime-order signed-coordinate family, every one of the \(2k\) coordinate marginal offset laws is subject to (T1); \(q_c\) is bounded below uniformly even if all coordinates and all sample times share their randomness. With \(\xi=0\), the integrated tail is \(R_0=(2k)^{-1}\sum_cq_c\). Therefore \(R_0\le111/4352<1\) forces
\[
 n\ge(1/4-o(1))\sqrt p\log p,
\]
whereas the existing r315 construction achieves \(n\le(128+o(1))\sqrt p\log p\) with \(R_0<111/8704\).

Consequently the **full asymptotic order** of the positive-tail sample length is now
\[
 \boxed{\quad n_{\rm admissible}(p)
              =\Theta(\sqrt p\log p)\quad}
\]
within the specified r307/r315 homogeneous external finite-cyclic class permitting \(k=s=O(\log p)\) and \(H(\mathcal H)=O((\log p)^2)\). The logarithmic factor is necessary in this class, not merely an artefact of the r315 moment argument.

This strengthens r317, whose first-moment r309 corollary previously established only \(\Omega(\sqrt p)\) for positive tails; r309's original separate almost-sure-tail \(\Omega(\sqrt p\log p)\) conclusion remains valid. This proof closes the **sample-length order** question, not the optimal leading constant, fixed-index/seed-entropy variants, admissible Gaussian-prime walk, source-preserving X6 carrier, or the original parent objective.

## Verification and publication boundary

The exact bound (T1) is algebraically reproducible by evaluating a single hypergeometric ratio, and the asymptotic estimate follows from inequalities (2), (3), (5) without computational hypotheses. The independent checks required at a Native Result boundary, including contributor overlap and frozen Result bytes, remain separate. This is a Driver-side, source-exposed scientific derivation, **not** a native Result acceptance, Task completion, Foundation promotion, or authorized CLAIM. No existing owner or study is adopted.
