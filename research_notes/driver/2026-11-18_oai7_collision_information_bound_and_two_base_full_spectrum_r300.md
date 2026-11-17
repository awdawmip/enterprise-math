# OAI7 r300 — Collision-excess information bound and collision-free full-spectrum theorem for (2,q)

Date: 2026-11-18. Author-side mathematical continuation by EM-DVR-DEBB5E, retaining the original directed shared-shift contributor EM-EMF6D046-5A2844. **Model: external integer/CRT comparator only.** No claim of native signed-X6 equivalence, Gaussian-prime walk realization, independent Result review, Source/Activity admission, or Task completion.

## Setup and frozen predecessor facts

Let d >= 2 and p_1,...,p_d >= 2 be pairwise coprime integers, P = product_j p_j, M = sum_j(p_j-1). Fix integer r > M with gcd(r,P)=1. Compare the compact integer shift S = U_r + sum_j U_{p_j}, with independent discrete uniforms, to the common-quantile CRT shift Q = CRT(floor(rW),floor(p_1 W),...,floor(p_d W)) with one W uniform on [0,1). The CRT map only relabels atoms. All logarithms use natural units.

For the m-th open r-cell I_m=(m/r,(m+1)/r), let t_m be the number of base cuts i/p_j (1 <= i < p_j) strictly inside it. As r>M >= p_j and the r-grid does not meet a base cut, cuts in each cell come from distinct coordinates. Put

c = sum_{m=0}^{r-1} (t_m-1)_+ = M - #{m:t_m>0}.

Retain from r295/r298 the *proved* strict K_base>0, expressed via base convolution prefixes A and cut integers B, and the exact identity

H(Q)-H(S) = K_base/r - C_r,     C_r = sum_j H(T_j|J)-H(T|J),

where J=floor(rW), T_j=floor(p_j W), T=(T_1,...,T_d). This note proves a new explicit information bound and a universal all-r family.

## Theorem A — Explicit cell formula and collision-excess bound

For each m with t=t_m >= 1, write the sorted interior base-cut coordinates in local cell units as
0 < u_1 < ... < u_t < 1,  u_i = r x_i-m.
Let h(u)=-u log u-(1-u)log(1-u), and let
g=(u_1,u_2-u_1,...,u_t-u_{t-1},1-u_t).

Then the exact conditional-total-correlation contribution at J=m is

C(m) = sum_{i=1}^t h(u_i) - H(g),

and C(m)=0 for t=0. Moreover

0 <= C(m) <= (t-1) log 2  for t>=1,

so the complete **nonasymptotic**, all-coprime-moduli estimate is

0 <= C_r <= (c/r) log 2,

and consequently

**H(Q)-H(S) >= (K_base-c log 2)/r.**

Thus the finite, checkable condition K_base > c log 2 guarantees **strict Shannon entropy dominance H(Q)>H(S)** even when base cuts collide and neither full probability vector majorizes the other. The bound does not claim full-spectrum majorization or positivity when K_base <= c log 2.

*Proof.* Conditional on J=m the continuous location Z=rW-m is uniform on (0,1). Each of the t different coordinates with a cut is a nondegenerate, monotone binary threshold at u_i. Its entropy is h(u_i). The vector of all these coordinates has exactly t+1 possible ordered states, with probabilities g. This proves the formula. Conditional total correlation is nonnegative by entropy subadditivity. Joint entropy is at least the entropy of any one marginal; hence
C(m) <= sum_i h(u_i) - max_i h(u_i) <= (t-1)log 2.
Cells with t=0 or 1 contribute zero. Average over the r equiprobable cells and sum (t_m-1)_+=c. Substitution into the existing r298 exact identity completes the proof.

## Theorem B — A complete collision-free family below the old pair-product threshold

Take exactly two base moduli (p_1,p_2)=(2,q), where q>=3 is any **odd integer** (prime or composite). For **every integer r>q with gcd(r,2q)=1**, there are no base-cut collisions, c=0. Therefore (by the exact r298 mass-spectrum and r295 strict base-prefix comparison)

**L(S) strictly majorizes L(Q), and H_alpha(S)<H_alpha(Q) for every finite alpha>0.**

In particular the exact Shannon gap equals K_base/r>0 and the endpoint Renyi entropies remain equal: H_0=log(r+q), H_infty=log r.

*Proof.* The 2-grid has only one interior cut, x=1/2. Since gcd(r,2q)=1, r is odd. Hence the unique r-cell containing 1/2 is centered at 1/2, with endpoints 1/2 ± 1/(2r). Every q-grid interior cut i/q has distance at least 1/(2q) from 1/2, since q is odd. Because r>q, no q-grid cut lies inside the cell containing 1/2. All other cells contain only q-grid cuts; each has length 1/r<1/q, so it contains at most one such cut. Thus c=0. The established collision-free spectrum theorem and strict A-majorizes-B lemma give the stated all-order conclusion.

This is a strict extension of the sufficient condition r >= R=2q from r297: **every** r>q meeting the coprimality gate works, including q<r<2q. No special feature of prime q is used.

## Reproducible finite checks

Using exact Fraction grid locations and integer convolution mass numerators (floating point enters only reported logarithms):

| base tuple | r | collision excess c | K_base | C_r | exact identity H(Q)-H(S) | proved lower bound |
|---|---:|---:|---:|---:|---:|---:|
| (2,9) | 11 | 0 | 0.555605904 | 0 | 0.050509628 | 0.050509628 |
| (2,15) | 17 | 0 | 0.602111391 | 0 | 0.035418317 | 0.035418317 |
| (3,5) | 7 | 2 | 0.783168283 | 0.026617016 | 0.085264167 | -0.086160868 |
| (3,5,7) | 13 | 2 | 2.417135060 | 0.020066602 | 0.165866864 | 0.079295438 |
| (3,5,7) | 17 | 0 | 2.417135060 | 0 | 0.142184415 | 0.142184415 |

All table entries follow from the rational cut partition, the integer coefficients of product_j(1+x+...+x^(p_j-1)), and the r298 entropy identity. The (3,5,7), r=13 row is an explicit **colliding** regime certified to have H(Q)>H(S) from the coarse bound alone; r298 additionally proves its full spectra are incomparable.

Example verification algorithm, executable with standard Python:

```python
from fractions import Fraction
from math import gcd, prod, log
def verify(p,r):
    P=prod(p); M=sum(x-1 for x in p)
    assert r>M and gcd(r,P)==1
    cells=[[] for _ in range(r)]
    for modulus in p:
        for i in range(1,modulus):
            cells[(r*i)//modulus].append(Fraction(r*i,modulus)-((r*i)//modulus))
    c=sum(max(len(row)-1,0) for row in cells)
    def H(v):
        return -sum(float(x)*log(float(x)) for x in v if x)
    C=0.
    for row in cells:
        row.sort()
        if len(row)<2: continue
        gaps=[row[0]]+[row[i]-row[i-1] for i in range(1,len(row))]+[1-row[-1]]
        C+=sum(H([u,1-u]) for u in row)-H(gaps)
    C/=r
    cuts={0,P*r}
    for m in range(1,r):cuts.add(P*m)
    for modulus in p:
        for i in range(1,modulus): cuts.add((P//modulus)*r*i)
    cuts=sorted(cuts)
    HQ=H([Fraction(b-a,P*r) for a,b in zip(cuts,cuts[1:])])
    coeff=[1]
    for modulus in p+[r]:
        v=[0]*(len(coeff)+modulus-1)
        for i,x in enumerate(coeff):
            for j in range(modulus):v[i+j]+=x
        coeff=v
    HS=H([Fraction(v,P*r) for v in coeff])
    return c,C,HQ-HS
for pair in [([2,9],11),([2,15],17),([3,5],7),([3,5,7],13),([3,5,7],17)]:
    print(pair,verify(*pair))
```

## Dependencies, limits, and useful next question

Predecessors: r295 @73baa83b4b6041ab1530cf0eb09786861c055f15 (base prefix majorization), r298 @2445469267babbebe90ec8d74dcb1632d987c809 (exact entropy/TC identity and collision-free spectrum), r299 @57e82002ce50801f48cc8b8ec9a472c4b743f862 (high-Renyi reversal at c>0). This note is an author-side new mathematical lemma with explicit conditions and reproducible finite examples; no new axiom or assumed native interpretation.

Next discriminating question: can the new cell formula sharpen the coarse c log 2 penalty enough to settle the Shannon sign for all r>M, including collision-rich tuples where K_base <= c log 2? If not, seek a certified exact reversal. This remains distinct from original OAI7 Gaussian-prime geometry and signed native carrier requirements.
