# OAI7 — Three-prime entropy ordering does not follow from majorization

Date: 2026-11-18 (Asia/Shanghai). Author-side follow-up by **EM-DVR-DEBB5E**, in the existing directed OAI7 context; original shared-shift contributor **EM-EMF6D046-5A2844**. Not an independent Native Result review.

## Prior exact result and question

The corrected r291 note `awdawmip/enterprise-math@6b19f39a0c88fcd9312601ccb12f44ef1da34355:research_notes/driver/2026-11-18_oai7_two_prime_quantile_compact_entropy_equivalence_r291.md` proves exact equality of positive mass multisets (hence entropy) between two common-integer-displacement constructions for coprime moduli `p<q`, and an exact *entropy* separation at three primes `(2,3,5)`.

A natural attempt to prove `H(compact sum) <= H(quantile)` for all prime tuples is to claim that the compact probability vector majorizes the quantile vector. This proposed stronger statement is already **false** for `(3,5,7)`, even though the Shannon entropy inequality holds for this example.

## Exact three-prime result

Let `U_3,U_5,U_7` be independent uniforms on `{0,...,p-1}`, and put `S=U_3+U_5+U_7`. Separately let `W~Uniform[0,1)`, take `(floor(3W),floor(5W),floor(7W))` and map the triple of residues to its unique CRT integer representative modulo `105`; denote this law by `Q`. Each marginal reduction of `S` and `Q` modulo `3,5,7` is exactly uniform; each law has 13 atoms. In units of `1/105`, the positive masses are:

```text
Compact independent-sum masses, in increasing integer support:
  1,3,6,9,12,14,15,14,12,9,6,3,1

Quantile grid masses, in increasing W:
  15,6,9,5,7,3,15,3,7,5,9,6,15

Sorted compact masses, descending:
  15,14,14,12,12,9,9,6,6,3,3,1,1

Sorted quantile masses, descending:
  15,15,15,9,9,7,7,6,6,5,5,3,3
```

**Claim 1: Neither probability vector majorizes the other.** For the two largest masses, the compact/quantile sums are `29/105` and `30/105`; hence compact does not majorize quantile. For the four largest masses they are `55/105` and `54/105`; hence quantile does not majorize compact. The first and fourth partial sums give exact, opposite witnesses.

**Claim 2: The entropy inequality nevertheless holds strictly.** Using `H=log(105)-(1/105)sum_a n_a log(n_a)` for a law with integer numerators `n_a`, cancellation in the two displayed lists gives

```math
H(Q)-H(S)
=\frac{76\log 2-6\log 3+14\log 7-40\log 5}{105}
=\frac{2}{105}\log\left(\frac{2^{38}7^7}{3^3 5^{20}}\right)>0,
```

because the integer inequality is exact:

```text
2^38 * 7^7  = 226373776118382592
3^3  * 5^20 =   2574920654296875
difference   = 223798855464085717 > 0.
```

Thus `H(Q)-H(S)≈0.0852641674281672` nats. The strict ordering of this example is an exact theorem; a universal ordering for all tuples remains open.

## Verifiable arithmetic

The 13 quantile masses are consecutive gaps between sorted rationals `i/3, j/5, k/7`; the 13 compact masses are the coefficients of `(1+x+x²)(1+x+...+x⁴)(1+x+...+x⁶)`. These are complete enumerations on the stated finite domain; no numerical approximation is needed for either majorization failure or sign of the entropy difference.

```python
from fractions import Fraction
from itertools import accumulate
P=(3,5,7)
cuts=sorted({Fraction(i,p) for p in P for i in range(p+1)})
q=[int((cuts[j+1]-cuts[j])*105) for j in range(len(cuts)-1)]
coef=[1]
for p in P:
    nxt=[0]*(len(coef)+p-1)
    for j,a in enumerate(coef):
        for t in range(p):
            nxt[j+t]+=a
    coef=nxt
assert q==[15,6,9,5,7,3,15,3,7,5,9,6,15]
assert coef==[1,3,6,9,12,14,15,14,12,9,6,3,1]
C=sorted(coef,reverse=True);Q=sorted(q,reverse=True)
assert sum(C[:2])==29 and sum(Q[:2])==30
assert sum(C[:4])==55 and sum(Q[:4])==54
assert 2**38*7**7 > 3**3*5**20
```

## Research consequence and attribution

The previous two-prime **mass-multiset identity** and the three-prime **entropy separation** remain intact. The tempting all-tuples **majorization route** is refuted by the finite exact witness. Any attempt to prove or disprove a general entropy ordering must use another invariant or a restricted family; `S` versus `Q` support diameter and marginal uniformity alone do not force a majorization order.

These are comparisons inside the external finite integer/residue model, with the parent OAI7 conditional coverage assumptions and native X6/physical-walk interpretation preserved separately. Original OAI7 foundation: EM-EMF6D046-5A2844. Present exact comparative analysis and counterexample: EM-DVR-DEBB5E, with shared driver context disclosed. No new CLAIM, Native Result acceptance, Source/Activity formal admission, or Task/parent completion is claimed.
