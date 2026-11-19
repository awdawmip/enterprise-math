# OAI7 r386 — A conditional-sampler replacement for iid coverage transfer and a one-seed cyclic certificate

Date: 2026-11-19. Status: **author-side mathematical derivation with finite exact checker; not a Native Result, independent Review, or task closure**. Scope: finite abelian residue groups of the *pinned* external transfer theorem, not an assertion about actual Gaussian walk or X6/BRC availability.

## 1. Statement (same-checkpoint, correlated version)

Retain the notation of the exact \`coverage-transfer.tex\` theorem: lattice \(\Lambda\), signed homomorphisms \(\phi_c:\Lambda\to G_c\), \(|G_c|=p_c\in[T,2T]\), independent random signed subset \(S\) of size \(s\), exact finite checkpoint \(A\), and **\(Y=y(A)\)**. Conditional on \(A=a\), take *any jointly distributed* finite lattice displacements \(h_1,\ldots,h_n\) with a **common one-trial marginal** \(\nu_a\); do not assume conditional independence. Let \(\mathcal H=(h_1,\ldots,h_n)\), \(Z=Y+h_1\). Entropies use natural logarithms.

Fix the original parameters
\[
0<\tau\le3/8,\quad0<\delta\le1/64,\quad
\rho=\tau+4\delta,\quad0<\beta'\le\beta<1,\quad
0<\eta\le1,\quad 0\le\eta'\le\eta\delta/100.
\]
For each \(c\), set \(u_c=\lceil p_c^{1-\beta}\rceil\). At each supported \(a\), assume all but at most an \(\eta'\)-fraction of signed coordinates have strict \((\rho,\beta')\) coverage for \(\phi_c(y(a)+h_1)\mid A=a\); explicitly,
\[
 E_{a,c}:=\{v:\Pr(\phi_c(y(a)+h_1)=v\mid A=a)<\rho/p_c\},
\qquad |E_{a,c}|<p_c^{1-\beta'}.
\]
In what follows, call these coordinates **good at \(a\)**. The translation from \(\phi_c(y(a)+h_\ell)\) to \(\phi_c(h_\ell)\) can be made in the definition of \(E_{a,c}\); we henceforth use the latter (translated) exceptional set.

Replace *only* the original conditionally-iid/Chernoff assumption by the following **conditional lower-tail sampler property (CS)**: at every supported \(a\), every good \(c\), every \(K\subset G_c\) of cardinality \(u_c\), and every \(x\in G_c\) satisfying
\[
 |(K-x)\cap E_{a,c}|\le\delta u_c,
\]
the jointly distributed vector \(\mathcal H\mid A=a\) obeys
\[
 \boxed{\Pr\!\left(
    \sum_{\ell=1}^n{\bf1}_{\{x+\phi_c(h_\ell)\in K\}}
      \le n(\tau+\delta)u_c/p_c\ \middle|\ A=a
              \right)\le \frac{\delta}{100p_c}. }\tag{CS}
\]
No independence across \(\ell\) is part of (CS).

Also retain the external theorem's entropy/budget assumptions
\[
\mathbb E_S H(F_S(Y))\ge(1-\epsilon)s\bar L,\quad
H(\mathcal H)\le\kappa s\bar L,\quad
\epsilon+\kappa\le\eta\delta\beta'/16,
\]
and its two geometric inequalities
\[
\delta^{-1}<p_c^{\beta'/2}\quad\text{for each }c,
\qquad
\log(2e/\delta)\le(\beta'/4)\log T.
\]
The original Chernoff-size condition \(p_c\exp(-\delta^2n p_c^{-\beta}/2)\le\delta/100\) is **not assumed**: it is one sufficient mechanism for (CS) when the samples are conditionally iid.

**Theorem.** Under the preceding hypotheses, all but at most an \(\eta\)-fraction of signed coordinates have strict \((\tau,\beta)\) coverage for \(\phi_c(Z)\). In particular the original implication remains valid under this weaker, verifiable *sampler* requirement without the iid entropy replication.

## 2. Complete proof

Let \(c\) be deficient for \(\phi_c(Z)\). As in the pinned source, choose \(K_c\) of size \(u_c\) from residues having terminal probability \(<\tau/p_c\), and form the common-data list
\[
 \mathcal L_c(\mathcal H)=\left\{x:
 \sum_{\ell=1}^n{\bf1}_{\{x+\phi_c(h_\ell)\in K_c\}}
 \le n(\tau+\delta)u_c/p_c\right\}.
\]
The \(h_\ell\) have the same one-trial conditional marginal at each \(a\); because \(Y=y(A)\) and the distribution of \(A\) is unchanged, each \(Y+h_\ell\) has the same unconditional law as \(Z\). Therefore
\(\mathbb E\sum_\ell{\bf1}_{\{\phi_c(Y+h_\ell)\in K_c\}}
  <n\tau u_c/p_c\).
Markov's inequality, without trial independence, implies
\[
 \Pr\{\phi_c(Y)\in\mathcal L_c(\mathcal H)\}
 \ge\delta/(\tau+\delta)\ge\delta. \tag{1}
\]

Fix \(A=a\) and a good coordinate \(c\). Double counting gives
\[
 \sum_{x\in G_c}|(K_c-x)\cap E_{a,c}|
      =u_c|E_{a,c}|.
\]
Thus fewer than \(|E_{a,c}|/\delta <p_c^{1-\beta'}/\delta
 <p_c^{1-\beta'/2}\) candidates violate the overlap condition in (CS).
For every remaining candidate (CS) bounds the probability of list membership by \(\delta/(100p_c)\); a union bound over at most \(p_c\) candidates shows
\[
 \Pr\{|\mathcal L_c(\mathcal H)|>p_c^{1-\beta'/2}\mid A=a\}
 \le\delta/100. \tag{2}
\]
This is exactly the conclusion for which the pinned source invoked conditional iid and Chernoff. Every later step of its proof is unchanged: averaging the probability of bad conditional coordinates gives at most \(\eta'/\theta<\delta/100\) among a putative fraction \(\theta>\eta\) of deficient terminal coordinates. Combining (1) and (2) yields mean good-list success \(\bar a\ge\delta/2\). The same source short-list entropy inequality, concavity of binary entropy, and
\(\log(2e/\delta)\le(\beta'/4)\log T\) imply the mean conditional entropy deficit over deficient coordinates is at least \((\delta\beta'/8)\log T\). Thus the all-coordinate deficit is \(>(\eta\delta\beta'/16)\bar L\), contradicting the shared conditioning-cost lemma and \(\epsilon+\kappa\le\eta\delta\beta'/16\). QED.

The logical replacement is exact: **common marginal** is required by (1), **(CS)** by (2), **entropy/budget** by the final contradiction. No new mathematical axiom or independence assumption was introduced.

## 3. Correlated one-seed construction and entropy separation

Let any integer \(p\ge2\), \(\Lambda=\mathbb Z^k\), \(G_{j,\pm}=\mathbb Z/p\mathbb Z\), and \(\phi_{j,+}(v)=v_j\bmod p\), \(\phi_{j,-}(v)=-v_j\bmod p\). Choose \(A=Y\) uniformly from \(\{0,\ldots,p-1\}^k\) and an independent uniform seed \(R\) from \(\{0,\ldots,p-1\}\). Set \(n=p\), and let
\[
 h_\ell=[(R+\ell-1)\bmod p]\,(1,\ldots,1)\in\mathbb Z^k,
 \qquad 1\le\ell\le p.
\]
All the \(h_\ell\), conditional on the exact \(A=a\), have the **same lattice-valued law**: uniform on the \(p\) diagonal lifts \(\{0,\ldots,p-1\}(1,\ldots,1)\). They are not conditionally independent. For each \(j,\pm\), seed \(R\), residue \(x\), and subset \(K\) of cardinality \(u\), the multiset
\(\{x+\phi_{j,\pm}(h_\ell):1\le\ell\le p\}\) is exactly all \(p\) residues; consequently the hit count is **exactly \(u\)**. Since \(\tau+\delta<1\), (CS) has failure probability **zero** (for every \(K,x,a,c\)). Every conditional one-trial coordinate law is uniform, hence \(E_{a,c}=\varnothing\), and every terminal \(\phi_c(Z)\) is uniform.

Each distinct coordinate index of \(Y\) is independent and uniform. Thus for any signed \(S\) with distinct indices,
\[
 H(F_S(Y))=s\log p,\qquad H(\mathcal H)=H(R)=\log p.
\]
Choose \(s=k\ge\lceil16/(\eta\delta\beta')\rceil\) and \(\epsilon=0\), \(\kappa=1/k\). Then all shared entropy budget inequalities hold. For fixed admissible \(\tau,\delta,\eta,\beta',\beta\), sufficiently large \(p=T\) also satisfies the retained two geometric inequalities (indeed the original Chernoff-size inequality with \(n=p\) holds for sufficiently large \(p\), although iid does not). This gives a fully specified family of models satisfying the *new* transfer theorem, with only **\(\log p\)** entropy in the shared vector, while a conditionally iid vector drawn from the same uniform diagonal one-trial law would cost **\(p\log p\)** conditional entropy.

This is a **changed-model information mechanism**, not an implementation of the pinned Gaussian-walk schedule. Conditional iid cannot be dropped from the *original* theorem without replacing its Chernoff step; here it is replaced by the exact (CS) certificate. It does not contradict r385's \(n\Phi_*\) bound, which explicitly depends on iid.

## 4. Exact finite checker for the cyclic certificate

The following exhausts \(p\in\{5,7,11\}\), the two signs, all \(p\) seeds, all \(p\) candidate residues and all \(\binom p{\lceil\sqrt p\rceil}\) subsets; it checks the **integer** hit count and the exact \(\tau=3/8,\delta=1/64\) threshold (no floating arithmetic).
 
~~~python
from itertools import combinations
from math import isqrt, comb
for p in (5, 7, 11):
    u = isqrt(p) + (isqrt(p)**2 < p)  # ceil sqrt(p), beta=1/2
    count = 0
    for K in combinations(range(p), u):
        K = set(K)
        for R in range(p):
            for x in range(p):
                for sign in (+1, -1):
                    hits = sum(((x + sign*((R+i)%p))%p) in K
                               for i in range(p))
                    assert hits == u
                    assert 64*hits > 25*u
                    count += 1
    assert count == 2*p*p*comb(p,u)
    print(p, u, count)
# 5 3 500
# 7 3 3430
# 11 4 79860
~~~

The universal construction and theorem are proved algebraically; this finite test is a separate sanity check.

## 5. Dependencies, provenance, and next scientific gate

- External frozen statement and its conditioning/list lemma: [openai/math@adc7f124, \`coverage-transfer.tex\`](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/Bounded-Step-Walks-on-Gaussian-Primes-September-26-2026/build/coverage-transfer.tex), theorem \`thm:transfer\`.
- [r385](https://github.com/awdawmip/enterprise-math/blob/7541049857493e92fd9489705cc05ed77528ea68/research_notes/portable_direct/2026-11-19_oai7_028c_strict_coverage_min_entropy_iid_cost_r385.md): exact *iid* entropy floor and numerical feasibility condition, reused at its original assumptions.
- Task \`RS-OAI7-028-C-20261007-6F2A81\`, publication \`TP2-96FAC49786245691AE19\`. Preserve original author/researcher \`EM-EMF6D046-5A2844\` and their separate frozen exact results.
- Open scientific interface: Can the actual Gaussian-walk displacements admit a shared-seed or other correlated conditional sampler obeying (CS) while retaining the correct later-step law? This requires a new legitimate schedule/conditional law and is *not* established here. X6/BRC transfer remains a separate typed-carrier problem.
- Authorship and status: this Driver conversation's mathematical derivation, **not independent acceptance of a frozen native Result**; Source/Activity and formal review need their own current authorization and provenance.

