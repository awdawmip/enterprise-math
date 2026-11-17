# OAI7 r301 — Complete Shannon sign and Rényi-exception classification for the (3,5,7) CRT family

Date: 2026-11-18. Author-side proof by EM-DVR-DEBB5E, building on r295–r300, with original shared-shift idea attributed to EM-EMF6D046-5A2844. External integer/CRT comparator only; not a Gaussian-prime realization, signed-X6 adaptation, Native Result, independent review, or mother-objective completion.

## The exact question

Use the three *base* moduli (3,5,7), hence P=105, M=12, and let **r>12 be any integer coprime with 105**. Compare the independent compact integer displacement
S=U_3+U_5+U_7+U_r
to the single-quantile CRT displacement
Q=CRT(floor(3W),floor(5W),floor(7W),floor(rW)), W uniform on [0,1).

The earlier r299 theorem shows that cut collisions force an eventual high-order Rényi reversal; it did not settle the Shannon sign in every colliding instance. r300 proves that if c counts excess base-cut collisions inside the r-cells, then

  H(Q)-H(S) >= (K_base-c log 2)/r,

where K_base is the exact positive base-prefix entropy constant from r298.

## Theorem — Strict Shannon ordering at every admissible r; exactly three collision exceptions

For *every* r>12 with gcd(r,105)=1,

  **H(Q)>H(S).**

More precisely, collision excess c is zero except for

  (r,c,collided r-cell indices) = (13,2,{5,7}), (16,2,{6,9}), (23,2,{9,13}).

For those three and **only** those three admissible r, c=2. In particular:

* For r not in {13,16,23}, the established r298/r299 full-spectrum result applies: S strictly majorizes Q and H_alpha(S)<H_alpha(Q) at every finite alpha>0.
* For r in {13,16,23}, **Shannon entropy still satisfies H_1(S)<H_1(Q)**, but r299 gives the opposite inequality H_alpha(S)>H_alpha(Q) for all sufficiently large finite alpha. Thus there is at least one crossing in (1,infinity) for each of these three r.
* At alpha=0 and alpha=infinity both entropies match, as established in r298. Neither crossing nor Shannon positivity implies a native-walk statement.

## Proof

### 1. Exhaust the only possible collision range with integer arithmetic

The established r296 large-modulus separation theorem guarantees c=0 whenever r >= R=max(3*5,3*7,5*7)=35. Thus examine the finite interval 13<=r<=34.

A base cut i/p belongs to r-cell floor(r*i/p); the 12 cuts have p in {3,5,7} and 1<=i<p. The following exact table lists all r in the interval with gcd(r,105)=1 and every cell index that occurs more than once:

| r | collided cells | c |
|---:|:---|---:|
| 13 | 5,7 | 2 |
| 16 | 6,9 | 2 |
| 17 | none | 0 |
| 19 | none | 0 |
| 22 | none | 0 |
| 23 | 9,13 | 2 |
| 26 | none | 0 |
| 29 | none | 0 |
| 31 | none | 0 |
| 32 | none | 0 |
| 34 | none | 0 |

The table is exhaustive because the omitted integers have a common factor with 105. Its reproducible *integer-only* certificate is:

```python
from math import gcd
from collections import Counter
for r in range(13,35):
    if gcd(r,105)!=1: continue
    counts=Counter((r*i)//p for p in (3,5,7) for i in range(1,p))
    excess=sum(max(n-1,0) for n in counts.values())
    collided=sorted(m for m,n in counts.items() if n>1)
    print(r,excess,collided)
```

Hence 0<=c<=2 for all admissible r>12.

### 2. A strict *exact-integer* bound K_base > 2 log 2

Let c_t be the 3*5*7 convolution coefficients, A_s=sum_{t=0}^s c_t for s=0,...,11, and B the cut integer multiset from r298. Their complete vectors are:

  A=(1,4,10,19,31,45,60,74,86,95,101,104),

  B=(15,21,30,35,42,45,60,63,70,75,84,90).

The preceding source proves

  K_base=(2/105) [sum_{a in A}a log(a) - sum_{b in B}b log(b)].

By exact prime factorization of the two finite integer products, the inequality K_base>2 log 2 is equivalent to

  **19^114 31^31 37^74 43^86 101^101 13^104 > 2^15 3^573 5^285 7^315.**

The left integer has **767 decimal digits**, the right **744 decimal digits**, a direct exact certificate of this strict inequality. These counts follow from integer exponentiation, independent of approximated logarithms. Numerically K_base ~ 2.4171350604519137, whereas 2log 2 ~ 1.3862943611198906.

### 3. Apply the r300 information bound, then the r299 high-order theorem

For every admissible r,

  H(Q)-H(S) >= (K_base-c log 2)/r >= (K_base-2 log 2)/r > 0.

If c=0, apply r298's collision-free strict majorization. If c=2, apply r299's exact maximum-mass multiplicity obstruction: S has r-12 maximizers, while Q has r-10, so

  lim_{alpha->infinity}(alpha-1)(H_alpha(S)-H_alpha(Q))
   = log((r-10)/(r-12)) > 0.

Since Shannon-order difference H_1(S)-H_1(Q)<0, continuity of alpha-order Rényi entropy implies a finite-order crossing in (1,infinity). These implications use the external finite-distribution laws only. QED.

## Scientific significance, source trail, and unresolved boundary

This finishes the Shannon sign for a full, nontrivial three-base-modulus family **for every admissible r**, including collision cases that cannot obey the full-spectrum majorization theorem. It also identifies precisely three finite exceptional r with genuine entropy-order crossings, replacing an open-ended numerical observation with an exhaustive certificate and an exact integer inequality.

Scientific dependencies: r295 @73baa83b4b6041ab1530cf0eb09786861c055f15 (strict base-prefix comparison); r296 @bf3058ebce5a55f758114f86222262cd8dedba43 (r>=R collision-free); r298 @2445469267babbebe90ec8d74dcb1632d987c809 (Shannon gap identity); r299 @57e82002ce50801f48cc8b8ec9a472c4b743f862 (high Rényi reversal); r300 @a67d6469b6c03e7316df0de1c4e1b962fbe78c5d (information bound).

The next broad scientific question is whether an admissible family with K_base<=c log 2 exhibits a true negative Shannon gap, or whether a stronger structural inequality enforces positive Shannon dominance. Full OAI7 work also requires independent examination of coverage-transfer hypotheses, Gaussian-prime-walk geometry, and typed signed-X6 carrier safety. Neither GitHub authorship nor the Driver transport checkpoint constitutes a native Result or independent decisive review.
