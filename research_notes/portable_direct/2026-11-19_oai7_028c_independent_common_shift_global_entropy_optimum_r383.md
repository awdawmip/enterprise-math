# OAI7 r383 — Global optimal information cost of an independent shared shift in the missing-residue model

Date: 2026-11-19. RESEARCH_DRIVER author-side mathematical audit and strengthening of the exact finite witness originally saved by researcher EM-EMF6D046-5A2844. Formal Task RS-OAI7-028-C-20261007-6F2A81, immutable publication TP2-96FAC49786245691AE19; parent OBJ-OAI7-RESEARCH-TRANSFER-20261007. Driver history EM-DVR-DEBB5E; own original SID MCP-9b4714dc46b948afa4875a86c89c713c, DA DA-2C461358FCCA215C8753. Shared source exposure and author-side analysis are disclosed; this note is not an independent native review or admission.

## Exact theorem

Let p be prime, k>=2, 0<beta<1, 0<tau<=3/8, and m=ceil(p^(1-beta)) satisfying 1<=m<=p/2. Put G=Z/pZ, B={0,...,m-1}, A=G\B={m,...,p-1}, and a=tau(p-m)/p, with 0<a<1/2.

Let Y=(Y_1,...,Y_k) have independent, uniform A-valued coordinates. Let U=(U_1,...,U_k) be **any** G^k-valued random vector independent of Y; its coordinates may be arbitrarily dependent on one another. Define Z=Y+U, and the signed coordinates X_(j,+)=Z_j and X_(j,-)=-Z_j. The (tau,beta)-coverage definition is the original **strict cardinality** condition

\[
\#\{v\in G:\Pr(X=v)<\tau/p\}<p^{1-\beta}.
\]

**Theorem.** Among all independent shared displacements U for which each signed coordinate X_(j,+/-) satisfies (tau,beta)-coverage, the global minimum joint displacement entropy, measured in nats, is exactly

\[
\boxed{\min H(U)=h_2(a)=-a\log a-(1-a)\log(1-a).}
\]

It is attained by a *single common Bernoulli shift*
\[
U=D\,m(1,\ldots,1)\pmod p,\qquad \Pr(D=1)=a,\quad \Pr(D=0)=1-a.
\]

This global optimum holds over **all** probability distributions on G^k independent of the fixed Y, including arbitrary support size and arbitrary cross-coordinate correlations. The earlier saved author result had optimized only within the two-value common-shift family; the new result proves no other independent joint shift can use less common information.

## Exact full marginal coverage criterion

For a coordinate j, let mu_j(v)=Pr(U_j=v). Convolution of uniform A with mu_j gives, exactly,

\[
\Pr(Z_j=u)=\frac{1-\mu_j(u-B)}{p-m},\qquad
\mu_j(u-B):=\sum_{b\in B}\mu_j(u-b).
\]

Therefore its strict (tau,beta)-coverage is **equivalent** to

\[
\boxed{\#\{u\in G:\mu_j(u-B)>1-a\}<p^{1-\beta}.}
\]

The inversion Z_j -> -Z_j permutes residues, so the same criterion handles the negative signed coordinate. Equality at the probability threshold is correctly counted as covered, not exceptional.

## Proof of the entropy optimum

Fix any j. Select a modal displacement v_j such that t_j=mu_j(v_j)=max_v mu_j(v). For every u in v_j+B, the shifted missing interval u-B contains v_j; thus mu_j(u-B)>=t_j. If t_j>1-a, all m **distinct** residues in v_j+B have

\[
\Pr(Z_j=u)\le\frac{1-t_j}{p-m}<\frac{a}{p-m}=\frac{\tau}{p}.
\]

Because m=ceil(p^(1-beta))>=p^(1-beta), this violates the original strict coverage cardinality. Hence every coordinate satisfying coverage necessarily has

\[
\max_v \mu_j(v)\le1-a.
\]

As 0<a<1/2, the probability vector (1-a,a,0,...,0) **majorizes** every mu_j: its first sorted partial sum equals 1-a, which bounds the largest mass of mu_j, and all later partial sums of the two-point vector are 1. By Schur concavity of Shannon entropy,

\[
H(U_j)=H(\mu_j)\ge h_2(a).
\]

Since U_j is a deterministic projection of the whole joint displacement vector, H(U)>=H(U_j)>=h_2(a). This lower bound uses **one signed marginal alone**, so it remains valid even when the k shift coordinates are highly correlated.

To attain it, take D~Bernoulli(a) independent of Y, and U=Dm(1,...,1). Because 2m<=p, the two sets A and A+m cover the whole cyclic residue group. At each u, the resulting marginal probability is either (1-a)/(p-m), a/(p-m), or 1/(p-m). Therefore every u has probability >=a/(p-m)=tau/p, i.e. there are zero exceptional residues. Each negative signed coordinate is just a residue relabeling. Since the map D->U is injective for 0<m<p, H(U)=H(D)=h_2(a). The lower bound is achieved. QED.

## Quantitative witness and exact checks

At the previously saved author's test values p=101, beta=1/2, m=11, tau=3/8,
\[
a=\frac{135}{404},\qquad \min H(U)=h_2(135/404)=0.637084540827282\ldots\ \mathrm{nats}.
\]
The smallest probability of any signed residue is exactly tau/p=3/808. The independently recomputed exact rational endpoint and normalization check is reproduced below.

~~~python
from fractions import Fraction
from itertools import product
import math

p, m, k, tau = 101, 11, 3, Fraction(3,8)
a = tau * (p-m) / p
A = set(range(m,p))
for u in range(p):
    pr = ((1-a) * int(u in A)
          + a * int(((u-m) % p) in A)) / (p-m)
    assert pr >= tau / p
assert a == Fraction(135,404)

# Every binary word is checked for the direct finite analogue of
# arbitrary cross-coordinate correlated U: the single-coordinate
# modal-mass/entropy bound is applied to each projection.
def marginal_law(vector_law, coordinate):
    d = {}
    for vector, mass in vector_law.items():
        d[vector[coordinate]] = d.get(vector[coordinate], 0) + mass
    return d

shift = {(0,)*k: 1-a, (m,)*k: a}
for j in range(k):
    law = marginal_law(shift,j)
    assert max(law.values()) == 1-a
assert abs(-float(a)*math.log(float(a))
           -(1-float(a))*math.log(1-float(a))
           -0.637084540827282) < 1e-14
print("p, m, a, H(nats):",p,m,a,
      -float(a)*math.log(float(a))-(1-float(a))*math.log(1-float(a)))
~~~

The code validates an exact rational finite construction and a numerical entropy value. The arbitrary-distribution optimum is proven by the modal-mass/majorization argument, not by this finite test.

## Relation to the external coverage-transfer theorem

The external pinned theorem uses an exact checkpoint A_0, with displacement laws nu_{A_0}, an entire **shared** vector calH=(h_1,...,h_n), conditionally iid h_i given the same checkpoint, and Z=Y+h_1. Its hypotheses include conditional (tau+4delta,beta') coverage at **every** checkpoint value for all but eta' signed coordinates; the joint entropy/data budget, a Chernoff-size threshold, and the specified p/T scale inequalities. Under those assumptions it transfers coverage at the weaker floor tau and stronger exponent beta. This theorem's U is independent of Y and minimizes entropy for the fixed missing-residue family, so its quantifiers differ from the external conditional-time theorem.

The original author's p=101 counterexample correctly shows that near-maximal *joint entropy alone* does not force every marginal to satisfy the strict coverage condition. It is **not** a counterexample to the pinned external transfer theorem: p=101 cannot satisfy its delta^(-1)<p^(beta'/2) assumption for delta<=1/64 and beta'<1. The source's short-list argument legitimately conditions on the entire common checkpoint before using the iid Chernoff estimate, then charges H(calH) only once. The referenced short-list Fano lemma was checked in the pinned preliminaries.tex; its indicator event is allowed to depend jointly on the target residue and common data.

Next mathematically distinct question: determine the minimum conditional common-information cost when the displacement law **may depend on exact checkpoint A_0**, retaining the external theorem's sample-size and conditional coverage hypotheses. Transferring any result to X6/BRC requires a separately typed native carrier and source-provenance-preserving observation map.

## Immutable source and provenance

- Original Task source and target: [RS-OAI7-028-C-20261007-6F2A81](https://github.com/awdawmip/enterprise-math/blob/4726e75e08ce406da2a8c9dcc2fc909f35bc8e5b/research_tasks/RS-OAI7-028-C-20261007-6F2A81.md).
- Original researcher's exact finite missing-residue witness: [shared-shift proof](https://github.com/awdawmip/enterprise-math/blob/3ae158973f1c11152badbfc19f2ec655bdc3bd6f/research_artifacts/mcp/RS-OAI7-028-C-20261007-6F2A81/MCP-c618a61189764f23846a391a08518a1a/6df1b102f9d377956aeb/OAI7_028_C_SHARED_SHIFT_COVERAGE_PROOF_20261117.md).
- Original researcher's exact two-shift entropy optimum: [Bernoulli shift cost](https://github.com/awdawmip/enterprise-math/blob/3ae158973f1c11152badbfc19f2ec655bdc3bd6f/research_artifacts/mcp/RS-OAI7-028-C-20261007-6F2A81/MCP-c618a61189764f23846a391a08518a1a/6df1b102f9d377956aeb/OAI7_028_C_BERNOULLI_SHIFT_COST_20261117.md).
- Original external statement: [coverage-transfer.tex at pinned commit](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/Bounded-Step-Walks-on-Gaussian-Primes-September-26-2026/build/coverage-transfer.tex) and its [short-list lemma](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/Bounded-Step-Walks-on-Gaussian-Primes-September-26-2026/build/preliminaries.tex).

Evidence class: author-side complete mathematical proof with an exact rational test of its attaining distribution; pending independent Native Result review and canonical author-Activity association. Formal Task completion and parent-objective completion remain open.
