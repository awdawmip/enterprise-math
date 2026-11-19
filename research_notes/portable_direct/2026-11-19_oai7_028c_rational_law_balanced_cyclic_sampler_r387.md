# OAI7 r387 — Exactly preserve every rational checkpoint law with one cyclic seed: zero-tail sampler and type-entropy cost

Date: 2026-11-19. Mathematical status: **new author-side proved finite sampling lemma and exact finite check**, not an independently admitted Native Result. This continues the correctly scoped OAI7-028-C coverage-transfer investigation.

## 1. Balanced cyclic sampling theorem

Let \(A\) have finite support; conditional on \(A=a\), let \(\nu_a\) be any finitely supported **rational** probability law on a common lattice \(\Lambda\). There may be several distinct conditional laws. Let \(T(A)\) denote the finite **law type** of \(\nu_A\) (two values of \(A\) have the same type precisely when their conditional displacement laws coincide, including the actual lattice support). Choose an integer \(n\ge1\) such that every \(n\nu_a(h)\) is an integer for all \(a,h\), e.g. a common multiple of the reduced denominators.

For each type \(t\), canonically fix an ordered length-\(n\) word \(w_t=(w_{t,0},\ldots,w_{t,n-1})\) in \(\Lambda\), containing exactly \(n\nu_t(h)\) copies of each lattice displacement \(h\). Independently sample a **single** \(R\sim\operatorname{Unif}\{0,\ldots,n-1\}\). Define, simultaneously for all \(1\le\ell\le n\),
\[
 \boxed{h_\ell=w_{T(A),(R+\ell-1)\bmod n}.}\tag{1}
\]
Then, for each \(a\) and each \(\ell\), the exact conditional lattice-valued marginal is unchanged:
\[
 \boxed{\mathcal L(h_\ell\mid A=a)=\nu_a.}\tag{2}
\]
For every function \(f:\Lambda\to\mathbb R\), the following *empirical identity* holds surely, not merely in expectation:
\[
 \boxed{\sum_{\ell=1}^n f(h_\ell)
       =n\sum_{h\in\Lambda}\nu_A(h)f(h).}\tag{3}
\]
The shared vector \(\mathcal H=(h_1,\ldots,h_n)\) satisfies
\[
 \boxed{H(\mathcal H\mid A)\le\log n,\quad
        H(\mathcal H)\le H(T(A))+\log n.}\tag{4}
\]
These are entropy upper bounds; if some \(w_t\) has repeated cyclic periods, the true costs may be smaller.

**Proof.** For fixed \(a,\ell\), \((R+\ell-1)\bmod n\) is uniformly distributed among all word indices, and the frequency of displacement \(h\) is exactly \(n\nu_a(h)\). This proves (2). Any rotation of a multiset has the same sum for every \(f\), giving (3). Since \(\mathcal H\) is a deterministic function of \((T(A),R)\), the data-processing inequality and independence of \(R,A\) give (4). QED.

## 2. Consequence for strict residue coverage: the r386 sampler condition holds with zero failure

Use the *same exact checkpoint* and finite signed homomorphisms of the pinned external \`coverage-transfer.tex\` theorem and [r386](https://github.com/awdawmip/enterprise-math/blob/9c5b8c0da18f6a85b640da07664fdd9b8cb4c92b/research_notes/portable_direct/2026-11-19_oai7_028c_dependent_conditional_sampler_coverage_transfer_r386.md). For a supported \(a\), a conditionally \((\rho,\beta')\)-covered coordinate \(c\), and any \(K\subset G_c\) of size \(u_c=\lceil p_c^{1-\beta}\rceil\), let \(E_{a,c}=\{v:\Pr(\phi_c(h_1)=v\mid A=a)<\rho/p_c\}\) with \(|E_{a,c}|<p_c^{1-\beta'}\). For each candidate \(x\) with \(|(K-x)\cap E_{a,c}|\le\delta u_c\), identity (3), applied to an indicator, gives
\[
 \sum_{\ell=1}^n{\bf1}_{\{x+\phi_c(h_\ell)\in K\}}
 =n\,\nu_a\{h:x+\phi_c(h)\in K\}
 \ge n\rho(1-\delta)u_c/p_c.
\]
When \(\rho=\tau+4\delta,\ 0<\tau\le3/8,\ 0<\delta\le1/64\),
\[
 \rho(1-\delta)-(\tau+\delta)
 =\delta(3-\tau-4\delta)>0.
\]
Therefore for every such \(a,c,K,x\),
\[
 \boxed{\Pr\!\left\{\sum_\ell {\bf1}_{\{x+\phi_c(h_\ell)\in K\}}
 \le n(\tau+\delta)u_c/p_c\ \middle|\ A=a\right\}=0.}\tag{5}
\]
This verifies the entire conditional sampler hypothesis (CS) of r386 **simultaneously for all signed coordinates and all test sets**, even when the conditional law has an arbitrary small exceptional set. No conditional iid, concentration limit, coordinate-specific entropy payment, or change to the **one-trial displacement law** is used.

**Corollary (rational-law transfer).** Under the other r386 hypotheses, its conclusion holds for the balanced cyclic sequence (1) whenever the **actual unconditional shared-data budget**
\[
 H(T(A))+\log n\le\kappa s\overline L
\]
and \(\epsilon+\kappa\le\eta\delta\beta'/16\) are satisfied. Here \(n\) is any common law denominator; unlike the iid proof, there is no \(\Theta(n)\) replication term. For a fixed type (constant \(\nu_a\)), \(H(T(A))=0\), and the shared entropy is at most \(\log n\).

This is a *sufficient bound* for the actual shared-data entropy, not an equality assertion. The original iid theorem remains correct under its own hypotheses, and r385's \(n\Phi_*\) lower bound applies only when the samples are conditionally iid.

## 3. Nonuniform, nontrivial finite certificate

Take \(\Lambda=\mathbb Z,\ p=11,\ G=\mathbb Z/11\mathbb Z,\ \phi(h)=h\bmod11\). Put
\[
 \nu(0)=11/20,\quad
 \nu(j)=1/20\ (j=1,\dots,9),\quad
 \nu(10)=0.
\]
Let \(n=20\), \(w=(0,\ldots,0,1,2,\ldots,9)\) (eleven zeros and one copy of each \(1,\ldots,9\)), and take its uniformly random cyclic rotation. The common one-trial marginal is exactly \(\nu\); it is **not uniform**, and the exception set at \(\rho=7/16,\ \beta'=1/2\) is precisely \(E=\{10\}\), since \(1/20> (7/16)/11\) and \(1<\sqrt{11}\). Take \(\beta=1/2,\ \tau=3/8,\ \delta=1/64\), so \(u=\lceil\sqrt{11}\rceil=4\).

Every set \(K\) of four residues and candidate \(x\) whose translate avoids residue 10 has at least four hits in the word: each included nonexceptional residue occurs at least once. The list threshold is
\[
 n(\tau+\delta)u/p=20(25/64)(4/11)=125/44<4.
\]
Thus (5) holds for every rotation, all \(K\) and all eligible \(x\), even though the one-step law is nonuniform.

The twenty distinct rotations encode the seed exactly, so the shared-vector entropy here is
\[
 H(\mathcal H)=\log20\approx2.99573227\ \text{nats},
\]
while *twenty conditionally iid samples from the same exact marginal* would have entropy
\[
 20H(\nu)=20\left[-\frac{11}{20}\log\frac{11}{20}
               -9\frac1{20}\log\frac1{20}\right]
 \approx33.53779747\ \text{nats}.
\]
This finite example checks the sampling/entropy mechanism, **not** the full high-entropy or size-budget hypotheses of the transfer theorem at \(p=11\).

### Exact finite checker

~~~python
from itertools import combinations
from math import comb
p,n,u=11,20,4
w=[0]*11+list(range(1,10))
assert len(w)==n
assert len({tuple(w[(R+i)%n] for i in range(n))
            for R in range(n)})==n
assert all(sum(w[(R+i)%n]==v for R in range(n)) ==
           (11 if v==0 else (1 if 1<=v<=9 else 0))
           for i in range(n) for v in range(p))
checks=0
for K0 in combinations(range(p),u):
    K=set(K0)
    for x in range(p):
        if (x+10)%p in K: continue  # overlap with E is >delta*u
        for R in range(n):
            hits=sum(((x+w[(R+i)%n])%p) in K for i in range(n))
            assert hits >= 4
            assert 64*p*hits > 25*n*u
            checks+=1
assert checks==46200
print(checks)  # 46200
~~~

The theorem itself is an exact finite counting identity and does not depend on the finite checker.

## 4. Scope, source and outstanding applicability

1. Frozen external input: [openai/math pinned \`coverage-transfer.tex\`](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/Bounded-Step-Walks-on-Gaussian-Primes-September-26-2026/build/coverage-transfer.tex), with its exact common checkpoint \(A\), original conditional iid hypothesis, and common information budget.
2. Prior work [r385](https://github.com/awdawmip/enterprise-math/blob/7541049857493e92fd9489705cc05ed77528ea68/research_notes/portable_direct/2026-11-19_oai7_028c_strict_coverage_min_entropy_iid_cost_r385.md) and r386 retain their narrower exact assumptions. This note proves a different, mathematically valid *correlated-sampling transfer route*; it is not a correction to the source's logical implication.
3. **Remaining scientific question:** whether the Gaussian-walk argument permits replacing an auxiliary conditional iid sampling vector with the balanced sequence (1), and whether the actual checkpoint law types and their common denominator satisfy \(H(T(A))+\log n\ll s\bar L\) without changing the intended geometric schedule. For irrational conditional distributions, an approximation would need explicit error and strict-threshold margins, and is not asserted here. Actual X6/BRC carrier, Link/Port provenance and native event predicates remain independently open.
4. Task attribution: \`RS-OAI7-028-C-20261007-6F2A81\`, publication \`TP2-96FAC49786245691AE19\`. Preserve original contributor \`EM-EMF6D046-5A2844\`; this new derivation is from this Driver research continuation. No Native Result, independent review, formal Task DONE or parent completion is implied by a GitHub note.
