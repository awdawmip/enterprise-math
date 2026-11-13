# R134.6 — Bit-polynomial vocabulary and witness enumerator for every K

Date: 2026-11-14 (Asia/Shanghai). Frozen S23 auxiliary scientific input: 43ec6098b1330ae86d0a7863be336c5d97f6ef34. This supplements PROOF.md and CONSTRUCTIVE_LIFT.md, without changing the native X6/P000 type.

## Exact problem and theorem

For given positive integers K and m, enumerate exactly the length-m words and one rational phase witness theta in (0,1) for each word of

S_i^(K)(theta)=1[{(K+i)theta}<{theta}]
             =floor((K+i)theta)-floor((K+i-1)theta).

**Theorem R134.6.** There is a deterministic exact arithmetic algorithm using polynomial time in m and log(K+1), producing the complete set of attainable words and one rational witness per word. In a straightforward rational-operations model the algorithm uses O(m^5) operations, with polynomial bit lengths (including all output witness numerators/denominators) in m+log(K+1). In particular the exponential-in-log(K) raw-event explosion of R131 for fixed m does not persist for this exact vocabulary/witness query.

## Hybrid proof

Case 1: K>=4m^3+2. Apply R134's exact uniform saturation theorem: the vocabulary equals the complete length-m finite Sturmian language. Generate candidates from the Farey order-m slope intervals and every intervening intercept gap as in CONSTRUCTIVE_LIFT.md. The number of generated rational certificates is O(m^3), each needing O(m) floor evaluations, so O(m^4) rational operations plus sorting and deduplication. The bit size of each witness theta is O(log(K+1)+log(m+1)); no iteration is proportional to K.

Case 2: 1<=K<4m^3+2. The floor-increment representation shows that every possible change of any S_i occurs at an integer crossing of n theta, for some n in {K-1,K,...,K+m-1}. Collect the exact rational cut set C={0,1} union {p/n: 1<=p<n, K-1<=n<=K+m-1, n>0}. Sort distinct cuts. For each interior singleton cut c, evaluate the exact word S(c); for each consecutive pair c<c', evaluate S((c+c')/2). This exhausts every phase atom of (0,1), preserving strict/equality behavior because all floor functions are locally constant between these cuts.

The number of generated cut fractions is at most sum_{n=K-1}^{K+m-1} max(n-1,0)=O(m(K+m))=O(m^4) under the Case-2 bound; there are at most twice this many point/interval candidates, and each word takes m floor operations. Thus O(m^5) rational operations, plus sorting O(m^4 log m), is sufficient. Numerators and denominators of cuts are O(m^3); midpoints have polynomial bits in log(m+1), and all stored words are length m. 

Both cases produce valid certified rational witnesses and their union covers **every** positive integer K,m. Since there are at most the Mignosi F_m=Theta(m^3) distinct words for any K by PROOF.md, the output size is polynomial as well.

## Exact validation

check_r134_hybrid.py runs all K=1..74 and m=1..8 (592 exact exhaustive comparisons to an independent raw event atom enumerator), checks 15,519 recovered rational witnesses, then tests m=1..8 at K=10^90+7 (8 more exact huge-K cases, all realizing their full Sturmian counts). Returned R134_HYBRID_BIT_POLY_PASS.

This theorem is about enumerating distinct finite words and rational existence witnesses in the specified auxiliary S23 subfamily. It does not assert an efficient chronological raw event trace, which remains Omega(K) for fixed m by R131, nor native Cell/Port permissions.

## Next

Determine the smallest K_min(m) yielding full saturation; characterize the finite exceptional vocabulary below threshold in non-raw-event terms; compare with general signed (A,d,E,x) S23 bit complexity using R126/R127 integer feasibility.
