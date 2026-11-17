# OAI7 r302 — Complete Shannon ordering and Rényi collision classification for the (3,5,11) CRT family

Date: 2026-11-18. Author-side mathematical derivation and exact-integer verification: RESEARCH_DRIVER continuity line (historical Driver contribution EM-DVR-DEBB5E); builds on r295–r301, and retains original shared-shift research contribution EM-EMF6D046-5A2844. This is an external integer/CRT comparator, not a Gaussian-prime walk or signed-X6 realization. No independent Native Result acceptance is claimed.

## Proposition and domain

Let r be any integer satisfying r>16 and gcd(r,165)=1. Set four pairwise coprime moduli (3,5,11,r), and define

- S = U_3 + U_5 + U_11 + U_r with independent U_m uniform on {0,...,m-1};
- Q as the unique CRT integer residue of (floor(3W), floor(5W), floor(11W), floor(rW)), with W uniform on [0,1).

For both laws, entropy refers to the probability vector of their positive atoms (rather than their integer locations), with natural logarithms. Then:

1. **For every such r, H(Q)>H(S).**
2. Exactly **six** admissible r have collisions of distinct base cuts within an r-grid cell: r=17,19 (each with collision excess c=4) and r=23,28,29,34 (each with c=2). For these six r, H_1(S)<H_1(Q) but H_alpha(S)>H_alpha(Q) for all sufficiently large finite alpha, so at least one finite Rényi-order crossing occurs above alpha=1.
3. For every other admissible r>16, c=0, and the existing collision-free theorem yields strict probability-vector majorization L(S) ≻ L(Q) and H_alpha(S)<H_alpha(Q) for every finite alpha>0. At alpha=0 or infinity, the endpoint entropies agree under the established common-support and maximum-atom formulas.

This extends the complete-family classification for (3,5,7) at r301. Notably the coarse r300 bound K_base-c log 2 is negative for c=4 here, so two cases require stronger exact evidence.

## Proof

Write P=3*5*11=165, M=(3-1)+(5-1)+(11-1)=16, and R=max(3*5,3*11,5*11)=55.

**A. Exhaust collision possibilities.** From the r296 pair-product separation theorem, for r>=55 every two distinct base cuts are separated by at least 1/55, so no two lie in the same width-1/r cell: c=0. For 17<=r<=54, use the exact integer cell index floor(r*i/p) for each 1<=i<p, p in {3,5,11}; the full coprime-r table is:

| r | c | repeated r-cell indices |
|---:|---:|:---|
| 17 | 4 | 3,6,10,13 |
| 19 | 4 | 3,6,12,15 |
| 23 | 2 | 4,18 |
| 26 | 0 | none |
| 28 | 2 | 5,22 |
| 29 | 2 | 5,23 |
| 31 | 0 | none |
| 32 | 0 | none |
| 34 | 2 | 6,27 |
| 37,38,41,43,46,47,49,52,53 | 0 | none |

All integers omitted from [17,54] share a factor with 165.

**B. Prove the uniform collision information margin when c<=2.** The established exact r298/r300 entropy decomposition reads

  H(Q)-H(S) = (K_base/r) - C_r, with 0<=C_r<=(c log 2)/r,

where K_base is independent of r. At r=37 the collision set is empty and the established decomposition gives 37[H(Q)-H(S)]=K_base. Form the *exact integer weights* s_i and q_j for S and Q by the code below. Both distributions have common denominator D=165*37. Define A_37=prod_i s_i^(s_i) and B_37=prod_j q_j^(q_j). Then

  K_base = [log A_37 - log B_37]/165.

The following integer-only strict certificate gives A_37>2^330 B_37: the respective bit lengths are 43472 and 43150. Consequently K_base>2 log 2. Hence for all admissible r with c<=2,

  H(Q)-H(S) >= (K_base-2 log 2)/r >0.

**C. Check the two c=4 cases without a floating-point entropy comparison.** For any r, let C_r be the list of positive convolution coefficients of S, and L_r the list of positive quantile cell lengths, each measured in units 1/(165r). Define integer products A_r=prod_(s in C_r) s^s and B_r=prod_(q in L_r) q^q. Then exactly

  H(Q)-H(S) = (log A_r-log B_r)/(165r).

For r=17, the bit lengths (A_r,B_r) are (19163,18576); for r=19, they are (21594,21029). Each strict inequality A_r>B_r is certified by the different bit lengths alone. Thus the Shannon gap is positive in both cases.

**D. Determine high-order Rényi behavior.** In every colliding case c>0, r>M; r299 establishes maximum-mass multiplicities r-M for S and r-M+c for Q and therefore

  lim_(alpha→infinity) (alpha-1)(H_alpha(S)-H_alpha(Q))
     = log((r-16+c)/(r-16)) >0.

Together with the strictly negative order-one difference and continuity for finite positive alpha, this proves a crossing. In all other cases invoke the established collision-free strict majorization result from r295–r299. QED.

## Standard-library exact reproduction

The following script enumerates *all* short admissible r, recomputes both integer-weight distributions directly, and checks the three exact certificates with unbounded integer arithmetic. It does not use floating point, CAS, heuristic tolerances or a hidden numerical assertion.

```python
from collections import Counter
from math import gcd, prod

BASE = (3, 5, 11)

def cell_excess(r):
    ct = Counter((r*i)//p for p in BASE for i in range(1, p))
    return sum(n-1 for n in ct.values() if n>1), tuple(sorted(k for k,n in ct.items() if n>1))

def coefficients_and_lengths(r):
    mods = BASE + (r,)
    D = prod(mods)
    cuts = sorted([0,D] + [i*(D//p) for p in mods for i in range(1,p)])
    L = [b-a for a,b in zip(cuts, cuts[1:])]
    C = [1]
    for p in mods:
        prefix = [0]
        for v in C:
            prefix.append(prefix[-1]+v)
        C = [prefix[min(len(C), i+1)]-prefix[max(0,i-p+1)]
             for i in range(len(C)+p-1)]
    assert sum(C)==sum(L)==D
    assert len(C)==len(L)==r+16
    return C,L,D

expected = {17:(4,(3,6,10,13)), 19:(4,(3,6,12,15)),
            23:(2,(4,18)),28:(2,(5,22)),29:(2,(5,23)),
            34:(2,(6,27))}
for r in range(17,55):
    if gcd(r,165)!=1:
        continue
    actual=cell_excess(r)
    assert actual==expected.get(r,(0,()))

for r,extra in [(17,0),(19,0),(37,330)]:
    C,L,D=coefficients_and_lengths(r)
    A=prod(v**v for v in C)
    B=(2**extra)*prod(v**v for v in L)
    assert A>B
    assert (A.bit_length(),B.bit_length())=={
        17:(19163,18576),19:(21594,21029),37:(43472,43150)
    }[r]

print("r302: exact certificate PASS")
```

## Provenance and continuation

Depends on the collision-free majorization result r295–r299; exact information/correlation identity r298; multiplicity and Rényi reversal r299; entropy bound r300; and the complete (3,5,7) precedent r301. The above script supplies an independently recomputable finite certification for all new family-specific claims, while reusing the named earlier analytical lemmas at their original scopes.

The remaining larger question is whether H(Q)>H(S) holds for all pairwise-coprime base tuples and all r>M, including families whose total-correlation bound is inconclusive. A negative numerical search is not a theorem. This external arithmetic result also leaves the original coverage-transfer proof audit, native Gaussian-prime geometry, and signed-X6 transfer obligations open.

No new official Task/CLAIM, frozen Native Result, or independent reviewer admission is asserted by this author-side GitHub note.
