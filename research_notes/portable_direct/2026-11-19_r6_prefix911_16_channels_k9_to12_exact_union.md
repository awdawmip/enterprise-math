# PREFIX-911 — Sixteen opposite-parity endpoint multiplier channels (9 <= k <= 12)

Date: 2026-11-19 Asia/Shanghai. Lane: 进取数论研究6. Independent, provenance-retaining BRC/two-port named-XOR auxiliary study. Predecessor: PREFIX-910 (immutable scientific source `enterprise-math@762febb58bbe0f4691e132c9a5bd0ccf1670170d`), previous exact explicit certificate union `7,784,240,442`. Frozen scientific input identifier is preserved: `f42f2906d77f24085c123f3ccfe9667d41caa96d`. Current normative rules were consulted separately; the research is not an X6 native event admission or a shared X6 CLAIM.

## Result and exact scope

Let `N=2^32`, and let `Q={262145,262147,...,524287}`, with `|Q|=131072`. Named trajectories are `Z_x=(x,x)` and `F_x^j=(x,x XOR 2^j)` for `0<=x<N`, `0<=j<32`. The two-port observer is `Phi_(a,b)(u,v)=(u mod a,v mod b)`. These are typed auxiliary provenance-preserving tracks; source index and port identity are not erased.

For coprime integers `k>ell>=1` with `k-ell` odd, and `1<=i<=22`, `s in {-1,+1}`, assume `k*a-ell*b=2^i+s` for `a,b in Q`. Define
```
x = (1-k%2) if s=+1 else k%2
y = x+k*a
F_x^i=(x,x+2^i), F_y^0=(y,y-s).
```
Since `a` is odd, the parity of `y` is `x+k mod 2`, hence `y` is odd for `s=+1`, even for `s=-1`. Thus `y XOR 1=y-s`. Also `x in {0,1}` has bit `i>=1` unset; hence `x XOR 2^i=x+2^i`. The starting states differ by `ka`, and ending states by `ka-(2^i+s)=ell*b`. For the tested `k<=12` we have `y<=1+12*524287<2^32` and `x+2^i<=1+2^22<2^32`, so both are legal distinct named trajectories and share the observer readout. This proves one collision for every accepted integer solution; it does not assume any unproved X6 physical/triadic event.

## Complete finite scan and exact de-duplication

Enumerate all coprime opposite-parity `1<=ell<k`, `9<=k<=12` (16 families), every `a in Q`, every `1<=i<=22` and `s=+/-1`; accept `b=(k*a-(2^i+s))/ell` precisely if the division is integral and `b in Q`. One implementation traverses `a`; an independent Python implementation traverses odd `b` using arithmetic progressions solving the modular congruence. Both verify named XOR endpoints and agree on each raw family count. The predecessor C910 is reconstructed from its exact class formulas: four sufficient families (total capacity, maximal fibers, zero-step LCM, special rows/columns), established gap families, high-gap and low-bit classes, the old three opposite-parity families and the eleven 5<=k<=8 families. Before extending, the C910 reconstruction independently reproduces `|A_910|=1,785,732`, `|A_910 intersect A_910^T|=8`, and the net prior extension `3,571,456`.

| (k,ell) | Parameter witnesses | Unique oriented pairs | Outside C910 (oriented) |
|---|---:|---:|---:|
| (9,2) | 29,127 | 29,127 | 9,910 |
| (9,4) | 58,254 | 58,254 | 27,264 |
| (9,8) | 524,287 | 511,544 | 269,651 |
| (10,1) | 26,216 | 26,216 | 20,031 |
| (10,3) | 34,952 | 34,952 | 16,415 |
| (10,7) | 344,528 | 337,038 | 165,847 |
| (10,9) | 480,596 | 468,945 | 247,684 |
| (11,2) | 35,748 | 35,748 | 19,367 |
| (11,4) | 41,704 | 41,704 | 20,049 |
| (11,6) | 135,038 | 133,052 | 52,657 |
| (11,8) | 336,619 | 329,171 | 164,196 |
| (11,10) | 443,261 | 432,537 | 228,990 |
| (12,1) | 21,846 | 21,846 | 12,048 |
| (12,5) | 43,690 | 43,690 | 21,663 |
| (12,7) | 174,762 | 171,641 | 74,843 |
| (12,11) | 411,088 | 401,158 | 211,648 |

The oriented residual set `A` is the **union across all sixteen families after excluding C910**, not the sum of the last column. Exact set operations give
```
|A| = 1,562,215
|A intersect transpose(A)| = 34
|new certified ordered pairs| = 2|A| - |A intersect transpose(A)| = 3,124,396
|C911| = 7,784,240,442 + 3,124,396 = 7,787,364,838
|Q^2 minus C911| = 17,179,869,184 - 7,787,364,838 = 9,392,504,346.
```
Transpose validity follows from reversal of each named trajectory combined with port exchange, preserving the source-bit label.

A first novel concrete witness is `a=278061, b=509757, k=11, ell=6, i=7, s=+1`. The trajectories `F_0^7=(0,128)` and `F_3058671^0=(3058671,3058670)` have start difference `3,058,671=11*a` and end difference `3,058,542=6*b`. Both are exactly legal XOR tracks.

## Verification, sources, classification and next unit

The complete C++17 exact-integer program (PREFIX911_R6_MULTIPLIERS_9_12_EXACT.cpp) checks all 16 families and all witnesses, reconstructs the earlier C910 new-set counts as an internal regression, and applies symmetric set exclusion and transpose de-duplication. The separate Python exact-integer recount (PREFIX911_R6_INDEPENDENT_RECOUNT.py) solves for the other endpoint by modular arithmetic rather than iterating the original first endpoint and rechecks all 3,141,716 parameter witnesses. Local actual execution of both succeeded; the latter checks raw-family counts, not the entire new C910 overlap computation. No Monte Carlo, floating point or extrapolation is used.

Mathematical grade: `AUTHOR_PROVED / EXACT_FINITE_COMPUTED / INDEPENDENT_FAMILY_RECOUNT / NOT_INDEPENDENTLY_REVIEWED / NOT_ADMITTED`. This counts a specified sufficient-collision certificate union only; the unclassified complement is not certified injective. The larger question `B_fix,odd(32) in {19,20}` remains open. A useful next direction is deriving an exact parameterized coverage bound for general k and ell, and using a complete two-flip carry criterion on the complement; independently, check whether observer labels and future operations admit a deeper BRC factorization. Maintain full joint-modulus relation and provenance, rather than assuming a coarser quotient is lossless.

The shared native X6 Task has a separately read control state and no CLAIM is made here. No native X6 event or triadic law is inferred from the auxiliary observer.
