# R538 | signed BRC Toeplitz order 61: exact all-positive-integer sign classification

Date 2026-11-05. Frozen scientific input R462 @ `18783e01e3646c72b7aab3b16d3f565e83e6446f`; prior verified author-side R537 @ `9b1db0818af3d3a1d7e6cbd8f2f2f17e7c96ebc9`. **Status: AUTHOR-SIDE EXACT COMPUTER-ASSISTED CONDITIONAL PROOF, NOT ADMITTED.**

## Statement and assumptions

For k∈Z≥1 set r=2k+1, C_k=binom(2k,k)/(k+1)>0. Let
H_k(t)=binom(r+t,2t)[x^r](1-x)(1+x)^(2t)(1+x²)^(r-t) for 2≤t≤r and zero otherwise.
The signed ballot–Catalan expression from frozen R462 is
B_k(t)=binom(r+t,2t) Σ_{q=0}^{min(floor((t-1)/2),k)} binom(t-1,2q)4^q C_(k-q),
with B_k(t)=0 outside 2≤t≤r.
**Shared frozen premise:** H_k(t)=B_k(t), and the R536 fixed-t lemma derived from it: p_t(k)=H_k(t)/C_k is a rational polynomial of degree≤2t on all positive k.

Define D_m(k)=det(H_k(3+i-j)) for 0≤i,j<m. Under that common premise,

**D_61(k)>0 for k=1,...,7 and all k≥16; D_61(k)<0 for k=8,...,15.**
There are no zeros for k≥1. In odd-r terms the negative interval is r=17,19,...,31 and positivity is permanent for odd r≥33.

In combination with R537: D_60(8)>0>D_61(8); and D_60(k)<0<D_61(k) for all 16≤k≤22.

## Full finite certificate and proof of the infinite tail

The Toeplitz–Hessenberg determinant satisfies f_0=1 and
f_n(k)=Σ_{a=1}^n (-1)^(a-1) p_(a+2)(k) p_2(k)^(a-1) f_(n-a)(k),
where f_n=D_n/C_k^n.
Under fixed-t polynomiality, induction gives deg f_n≤6n; in particular deg f_61≤366.

Set G(k)=[k(k+1)(2k+1)(2k+3)]^61(k+2), strictly positive on positive k, and deg G=245.
For each k=1,...,122, compute the reduced exact fraction
f_61(k)/G(k)=D_61(k)/(C_k^61 G(k)).
Let L be the positive least common multiple of all reduced denominators and δ_0,...,δ_121 the 122 exact forward differences at k=1 of L f_61(k)/G(k).
Define the explicit integer-coefficient Newton polynomial S(k)=Σ_{j=0}^{121}δ_j binom(k-1,j).
Every integer L, δ_j and the tail-shift coefficients ε_j is recorded in R538_EVIDENCE.json.

The exact BigInt program verifies L D_61(k)=C_k^61 G(k) S(k)
for ALL 367 distinct positive integers k=1,...,367.
Both normalized sides are rational polynomials of degree≤366, since
deg(GS)≤245+121=366. Therefore they are identical rational polynomials for all k and the identity holds on every positive integer.

The exact certificate shows S(k)>0 for 1≤k≤7 and S(k)<0 for 8≤k≤15.
At k=16 all 122 forward differences ε_j=Δ^j S(16) are STRICTLY POSITIVE.
Thus for every integer u≥0, S(16+u)=Σ_{j=0}^{121} ε_j binom(u,j)>0.
As C_k,G(k),L are positive, the sign classification follows for all k≥1.

## Scope, checks, and regeneration

`node R538_VERIFY.js > R538_EVIDENCE.json` gives `R538_EXACT_JS_PASS`:
367 exact identity points, 20 original signed 61×61 Bareiss determinants independently checked against B-based recurrence, 1220 exact raw H/B checks on k=1..20 t=2..62, and 22754 exact raw H/B checks on the complete k=1..367 t=2..63 grid. All operations use arbitrary-precision integers, no floating point.

These checks cross-check two integer formulas for the frozen premise on a FINITE grid; they do **not** establish unconditional H=B. The infinite-domain argument is conditional on that premise and the derived fixed-t lemma. There has been no independent Driver review, formal CLAIM/Result/Review, nor native X6 physical interpretation; this is an auxiliary scalar signed BRC Toeplitz theorem only. P000 / ACTIVE worldview and frozen R462 remain unchanged.

## Next

s=3,m=62: check degree≤372, 124 Newton coefficients, 373-point identity, and tail shifts. In parallel, consider proving the frozen H=B identity without relying on finite grids and analyze the fixed-k denominator/dominant-pole mechanism for order-dependent sign windows. Preserve all author/Driver/Task authority distinctions.
