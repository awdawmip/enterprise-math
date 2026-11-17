# OAI7 r302 — Quantitative finite Rényi-reversal threshold and exact first integer orders

Date: 2026-11-18. Author-side mathematical continuation in the shared Driver context by `EM-DVR-DEBB5E`, based on r298–r301; retain initial shared-integer-shift contributor `EM-EMF6D046-5A2844`. Domain: external finite integer/CRT model. This is not a frozen Native Result, an independent referee review, Gaussian-prime realization, or signed X6 mapping.

## Definitions and pinned predecessors

Let d≥2, p_1,...,p_d≥2 be pairwise coprime integers, P=∏p_j, M=∑(p_j−1), and take an integer r>M coprime to P. Let S=U_r+∑_j U_{p_j} with independent discrete uniforms, and let Q=CRT(floor(rW), floor(p_1W),...,floor(p_dW)), W uniform on [0,1). The CRT map merely relabels probability atoms.

Let a_s (0≤s<M) be the cumulative coefficients of C(x)=∏_j(1+x+...+x^{p_j−1}); in particular 1≤a_s≤P−1 and a_{M−1}=P−1. Let c be the excess count of base-grid interior cuts sharing an r-cell:
c=∑_{m=0}^{r−1}(t_m−1)_+, where t_m is the number of cuts i/p_j strictly inside (m/r,(m+1)/r). Prior r298 proves the exact S numerator multiset over denominator Pr is (a_0,...,a_{M−1}, P repeated r−M times, a_{M−1},...,a_0). Prior r299 proves Q has r−M+c atoms of numerator P. These facts use the stated r>M and gcd conditions.

## Theorem — computable sufficient reversal order

If c>0, then for **every real α>1** such that

    2∑_{s=0}^{M−1}(a_s/P)^α < c,                           (1)

the finite Rényi entropies satisfy the **strict reverse order**

    H_α(Q) < H_α(S).                                       (2)

A simpler universal sufficient numerical bound is

    α > log(2M/c) / log(P/(P−1)).                           (3)

The left side in (1) is continuous and strictly decreasing to zero as α→∞, so a unique positive threshold for (1) exists. The threshold (1) depends only on the base moduli and the collision excess, and is uniform over all admissible r having that c; it is a sufficient threshold, not a claim of the exact first crossing order.

*Proof.* Write the α power sum of each law using probability numerators over Pr. The exact S numerator spectrum gives

    (Pr)^α Σ_x Pr(S=x)^α = (r−M)P^α + 2∑_{s=0}^{M−1}a_s^α.

The r−M+c untouched r-cells of Q alone give

    (Pr)^α Σ_x Pr(Q=x)^α ≥ (r−M+c)P^α.

The difference (Q minus S) is thus at least cP^α−2∑ a_s^α, strictly positive under (1). For α>1, H_α=(1/(1−α))log Σp_x^α; its prefactor is negative, proving (2). Since every a_s≤P−1, the left side of (1) is at most 2M(1−1/P)^α, and (3) suffices. No asymptotic approximation, numerical premise, or new axiom enters. QED.

## Exact finite certificates: first *integer* order of reversal

Here "first integer" refers precisely to α∈{2,3,...} with H_α(Q)<H_α(S); it does **not** claim the first real crossing. Let D_α=Σ(q-numerator)^α−Σ(s-numerator)^α. All powers are integers and the two laws have the same denominator Pr. A positive D_α means the Rényi reversal (2).

| Base tuple | r | c | D_α<0 for all integer α in | First integer α with D_α>0 | Bound (1) guarantees every real α≥ |
|---|---:|---:|---|---:|---:|
| (3,5) | 7 | 2 | 2–5 | 6 | 6 |
| (3,5,7) | 13 | 2 | 2–34 | 35 | 36 |
| (3,5,7) | 16 | 2 | 2–35 | 36 | 36 |
| (3,5,7) | 23 | 2 | 2–35 | 36 | 36 |

The stated integer-order classifications are exhaustive within the displayed finite integer ranges. Each uses exact integer power sums, with no floating-point sign decision; the uniform real-order column follows the theorem and the verified strict inequality at 36. This sharpens the r299 exhibited α=26 for (3,5;7) to the **first integer reversal α=6**. For the three r301 exceptional (3,5,7) cases, it identifies first integer reversal orders 35, 36 and 36.

Reproduction (Python standard library; integer-only signs):

```python
from math import gcd, prod

def spectra(base, r):
    P = prod(base); M = sum(p-1 for p in base)
    assert r > M and gcd(r,P)==1
    D = P*r
    cuts = {0,D}
    for p in (*base,r):
        cuts.update((D*j)//p for j in range(1,p))
    v = sorted(cuts)
    Q = [b-a for a,b in zip(v,v[1:])]
    S = [1]
    for p in (*base,r):
        z = [0]*(len(S)+p-1)
        for i,w in enumerate(S):
            for j in range(p): z[i+j] += w
        S = z
    assert len(Q)==len(S)==r+M and sum(Q)==sum(S)==D
    counts = {}
    for p in base:
        for j in range(1,p):
            k=(r*j)//p
            counts[k]=counts.get(k,0)+1
    c=sum(max(0,t-1) for t in counts.values())
    return P,M,c,Q,S

for base,r in [((3,5),7),((3,5,7),13),
               ((3,5,7),16),((3,5,7),23)]:
    P,M,c,Q,S = spectra(base,r)
    Dalpha = lambda a: sum(v**a for v in Q)-sum(v**a for v in S)
    first = next(a for a in range(2,100) if Dalpha(a)>0)
    assert all(Dalpha(a)<0 for a in range(2,first))
    assert c==2
    print(base,r,c,first)
# Expected:
# (3, 5) 7 2 6
# (3, 5, 7) 13 2 35
# (3, 5, 7) 16 2 36
# (3, 5, 7) 23 2 36

base=(3,5,7)
P=prod(base)
C=[1]
for p in base:
    z=[0]*(len(C)+p-1)
    for i,w in enumerate(C):
        for j in range(p): z[i+j]+=w
    C=z
A=[]
s=0
for w in C[:-1]: s+=w; A.append(s)
assert len(A)==sum(p-1 for p in base)
assert 2*sum(v**35 for v in A)>=2*P**35
assert 2*sum(v**36 for v in A)<2*P**36
```

## Scope, decision and continuation

A collision implies a high-order Rényi reversal; the new finite threshold (1) is a reusable quantitative certificate and resolves four earliest-integer-order examples exactly. This is compatible with r301's strict **positive Shannon ordering**, which involves order α=1.

Input sources: r298 @2445469267babbebe90ec8d74dcb1632d987c809, r299 @57e82002ce50801f48cc8b8ec9a472c4b743f862, r300 @a67d6469b6c03e7316df0de1c4e1b962fbe78c5d, r301 @b1961afdc42c7597689210884635f8e17e7c4b6a. Related native Task: RS-OAI7-028-C-20261007-6F2A81 (TP2-96FAC49786245691AE19).

Formal result review, Source/Activity association, and the Gaussian-prime/native signed-carrier question retain their separate evidence and authorization requirements. Next useful directions: sharpen collision-entropy control for r>M, or check exact coverage-transfer quantifiers against a genuinely typed native carrier without assuming a scalar CRT map is that carrier.
