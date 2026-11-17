# OAI7 — Exact joint entropy and sparse support under a common Bernoulli displacement

Date: 2026-11-17. Research-driver source-level mathematical audit and new consequence.
Original finite construction and two-shift coverage thresholds: `EM-EMF6D046-5A2844`.
Independent checking and new joint-law theorem below: `EM-DVR-DEBB5E`.
Scope: the auxiliary finite signed-residue model in task `RS-OAI7-028-C-20261007-6F2A81`. This is author-side mathematics, not a native Result admission or a native X6 carrier theorem.

## Precise hypotheses

Fix a prime `p`, an integer `k>=1`, and `1<=m<=p/2`. Write `L=p-m`, `D=p-2m`, and `rho=D/L`. In the cyclic group `F_p`, set `A={m,...,p-1}`, `A_1=A+m`, with `|A|=|A_1|=L` and `|A intersect A_1|=D`. Let `Y=(Y_1,...,Y_k)` be uniform on `A^k` and let an independent `B~Bernoulli(q)`, `0<q<1`, act *once and jointly* through `Z=Y+m B (1,...,1) mod p`. All logarithms and entropies below are natural. Put `h(q)=-q log q-(1-q) log(1-q)`.

The signed coordinate maps are `phi_(j,+)(y)=y_j`, `phi_(j,-)(y)=-y_j`, mod `p`. The same `B` governs every signed coordinate, never an independently chosen time or shift.

## Theorem: exact joint distribution, entropy, information and holes

Under these hypotheses:

1. `support(Z)=A^k union A_1^k`, hence
   [
   |mathrm{supp}(Z)|=2L^k-D^k,qquad
   |mathbb F_p^ksetminusmathrm{supp}(Z)|=p^k-2L^k+D^k.
   ]
   For `k=2` the number of completely missing residue vectors is exactly `2m^2`.

2. The full Shannon entropy and the entropy of one marginal are exactly
   [
   H(Z)=klog L+(1-ho^k)h(q),qquad
   H(Z_j)=log L+(1-ho)h(q).
   ]
   Equivalently, `H(B|Z)=rho^k h(q)` and `I(B;Z)=(1-rho^k)h(q)`.

3. The coordinate total correlation (multi-information) is
   [
   sum_{j=1}^k H(Z_j)-H(Z)
     =[k(1-ho)-(1-ho^k)]h(q).
   ]
   In particular `I(Z_1;Z_2)=(m/L)^2 h(q)` for `k=2`. The correlation is strictly positive for `k>=2` and `m>0` when `0<q<1`.

4. Set `m=ceil(p^(1-beta))`, `0<beta<1`, and `0<tau<=3/8`, for sufficiently large primes with `2m<=p`. The original author's exact coverage threshold `a=tau L/p` implies that, for every `q in [a,1-a]`, **all** `2k` signed coordinate marginals have zero residues with probability below `tau/p`. Despite this, the joint law has the missing vectors in (1).

5. Along primes `p -> infinity`, choose `k_p=ceil((p/m) log p)` and any `q in [a,1-a]`. Then
   [
   rac{|mathrm{supp}(Z)|}{p^{k_p}}
    =2(1-m/p)^{k_p}-(1-2m/p)^{k_p}
    le 2/plongrightarrow0,
   ]
   while
   [
   rac{H(Z)}{k_plog p}ge
   rac{log(p-m)}{log p}longrightarrow1.
   ]
   Thus maximal-quality *relative* joint Shannon entropy and full signed **marginal** coverage coexist with vanishing **joint support density**, even with one shared displacement bit and a single consistent joint experiment.

## Proof

Conditional on `B=b`, `Z` is uniform on `A_b^k` (`A_0=A`, `A_1=A_1`). The two conditional supports each have `L^k` points, with common intersection `D^k`; this proves (1). A value `z` in the intersection has equal likelihood `L^(-k)` under either `b`, so its posterior for `B` is the prior Bernoulli(q), of entropy `h(q)`. Outside the intersection the support uniquely determines `B`. Moreover, under each `b`, the intersection has conditional probability `D^k/L^k=rho^k`; it therefore has the same unconditional probability. Consequently `H(B|Z)=rho^k h(q)` and `I(B;Z)=(1-rho^k)h(q)`. The chain rule `H(Z)=H(Z|B)+I(B;Z)` and `H(Z|B)=k log L` yield (2); repeat with `k=1` for a marginal. Subtraction gives (3), whose nonnegativity follows from `1-rho^k<=k(1-rho)`, with strict inequality for `k>=2`, `0<=rho<1`.

For (4), the three disjoint marginal regions `A\A_1`, `A_1\A`, and `A intersect A_1` have respective probabilities `(1-q)/L`, `q/L`, and `1/L`. At `a<=q<=1-a` they all meet `tau/p`. Inversion of a signed coordinate only permutes these probabilities. For (5), use `(1-x)^k<=exp(-kx)` and the choice of `k_p`; since `m/p ->0`, `log(p-m)/log p ->1`. No independence across signed coordinates has been inserted.

## Reproducible finite checks

The following standard-library check enumerates exact rational masses and verifies the entropy formula numerically only after the exact counts and rational masses have been constructed.

```python
from fractions import Fraction
from itertools import product
from math import log
for p,m,k,q in [(7,2,2,Fraction(1,4)),
                (7,2,3,Fraction(1,4)),
                (11,3,2,Fraction(1,4))]:
    A=range(m,p); L=p-m; D=p-2*m; pmf={}
    for b in (0,1):
        weight=(1-q,q)[b]/L**k
        for y in product(A,repeat=k):
            z=tuple((v+b*m)%p for v in y)
            pmf[z]=pmf.get(z,Fraction(0))+weight
    assert sum(pmf.values())==1
    assert len(pmf)==2*L**k-D**k
    h=-sum(float(x)*log(float(x)) for x in (q,1-q))
    H=-sum(float(x)*log(float(x)) for x in pmf.values())
    assert abs(H-(k*log(L)+(1-(D/L)**k)*h))<1e-11
```

Checked `(p,m,k)=(7,2,2),(7,2,3),(11,3,2)` with exact rational pmfs; support counts `41,223,103` respectively and entropy formulas agreed to numerical tolerance `1e-11`. For the author's `p=101,m=11,k=2,q=135/404` witness, the exact support count is `9959`, the missing-vector count is `242`, and `H(Z)=9.145834175401014` nats (formula; independently enumerated).

## Scope and remaining step

Theorem (1)–(5) is a property of the independently sampled product-box initial law and the same Bernoulli shift acting on every coordinate; it does not assert independent conditional coverage at a fixed exact checkpoint `A=Y`, nor identify a physical admissible Gaussian walk or a native X6/Link/Port path. The parent task requires source-level treatment of the exact-checkpoint conditional iid displacement kernel and any native transfer to preserve ordered path and branch provenance.

The original OAI7 construction and finite checks remain attributed to `EM-EMF6D046-5A2844`; the joint-entropy/sparsity theorem and its proof are subsequent Driver-authored work. Formal review/admission of this new theorem requires a distinct independent reviewer.

## Exact source references

- Original researcher shared-shift proof: [enterprise-math fixed blob](https://github.com/awdawmip/enterprise-math/blob/356f46499b642e131b124f2d53b9ae1f47d10c25/research_artifacts/mcp/RS-OAI7-028-C-20261007-6F2A81/MCP-c618a61189764f23846a391a08518a1a/6df1b102f9d377956aeb/OAI7_028_C_SHARED_SHIFT_COVERAGE_PROOF_20261117.md).
- Original researcher exact Bernoulli threshold: [enterprise-math fixed blob](https://github.com/awdawmip/enterprise-math/blob/356f46499b642e131b124f2d53b9ae1f47d10c25/research_artifacts/mcp/RS-OAI7-028-C-20261007-6F2A81/MCP-c618a61189764f23846a391a08518a1a/6df1b102f9d377956aeb/OAI7_028_C_BERNOULLI_SHIFT_COST_20261117.md).
- External conditional transfer theorem: [openai/math fixed source](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/Bounded-Step-Walks-on-Gaussian-Primes-September-26-2026/build/coverage-transfer.tex).
- Independent previous Driver exact conditional source audit: [enterprise-math fixed note](https://github.com/awdawmip/enterprise-math/blob/cf3e2674bbdd8c533d29f570cd701981e054402e/research_notes/driver/2026-11-17_oai7_conditional_coverage_shared_entropy_feasibility_audit.md).
