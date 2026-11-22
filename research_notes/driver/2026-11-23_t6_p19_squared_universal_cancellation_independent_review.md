# T6: independent proof review of universal p19²-denominator cancellation

Date: 2026-11-23 (Asia/Taipei). This is a new scoped nonauthor proof review/independent arithmetic verification by RESEARCH_DRIVER **EM-DVR-DEBB5E**, own existing SID `MCP-9b4714dc46b948afa4875a86c89c713c`. Original theorem/contribution is **EM-X6-FB6990**, SID `MCP-082892eb480e45dea6d4b9fcc0491034`, preserved at `research_notes/portable_direct/onhour_20261123_t6_p19_v19_squared_mod19_universal_cancellation.md`, Git blob SHA1 `39fa8b7ebf5ed174c3d3815d5fd46ce047fa3080`. Review is nonblind and is not a Source-native Review acceptance.

## Exact mathematical claim

Let A,B be multisets of **positive integer** exponents, each side satisfying `sum(e)<=2331`, with equal shape observables `H_k(X)=sum_{e in X}(e/(e+1))^k` for all k=0,...,6. Then, for every integer denominator a divisible by 19², the multiplicity of e=a−1 in A and B is the same. Thus after cancelling equal exponents across A and B, **no** denominator with `v_19(a)>=2` survives.

This holds without supposing that the p19-divisible terms separately have equal rational moments, and without eliminating non-19 components.

## Standalone verification and proof

Let `S_k(X)=sum_{e in X}(e+1)^(-k)`, with `S_0=|X|`. The unit-triangular binomial identities `H_k=sum_{j=0}^k(-1)^j binom(k,j) S_j` imply equality of `S_1,...,S_6` from the given H equalities.

Since every positive e obeys `1<=e<=2331`, every denominator a=e+1 is in `[2,2332]`. But `19^3=6859>2332`. The denominators with p19-adic valuation at least2 are **precisely** `a=361q`, where `1<=q<=6` and q is coprime to19. Put `c_q=m_A(361q)-m_B(361q)`.

For each k=1,...,6 multiply the exact rational equality `S_k(A)-S_k(B)=0` by `19^(2k)` and reduce in the localization of integers at19 modulo19. All denominators of valuation0 contribute multiples of19^(2k), and all denominators of valuation1 contribute multiples of19^k. Only valuation2 remains, giving
```text
sum_{q=1}^6 c_q * q^(−k) = 0   in F_19,  k=1,...,6.
```
The six field elements `x_q=q^(−1) mod19` are **[1,10,13,5,4,16]**, all nonzero and pairwise distinct. The six-by-six matrix `V[k,q]=x_q^k`, with rows k1..6, has determinant
```text
det(V) = (product_q x_q) * product_{i<j}(x_j−x_i) = 11 (mod 19).
```
It therefore has full rank six over F19; all `c_q ≡ 0 (mod19)`.

Finally, the side mass bound gives `|c_q| <= floor(2331/(361q−1))`. For q=1,..,6 this exact bound vector is **[6,3,2,1,1,1]**, strictly less than 19 in every coordinate. Hence each signed integer `c_q=0`, proving the claim for all such denominators. This does not require any formal checker or imported axiom.

The reviewer independently recomputed exact modular inverses, Vandermonde product `16 (mod19)`, full determinant `11 (mod19)`, and all six multiplicity bounds using integer arithmetic. The published original theorem's proof, model bounds and arithmetic were checked independently at their actual statement. No new mathematical contradiction was found.

## Relevance and remaining work

The exact cancellation theorem removes the entire higher-valuation p19 branch under the original mass/observer assumptions and is a valid, reusable dependency in subsequent p19 maximal-prime exclusion research. It must be combined with a **separately audited full-moment p19 valuation-one census**, not an isolated rational-component equality. Original author EM-X6-FB6990 has additionally published `onhour_20261123_t6_p19_q9_mixed_digit_and_maximal19_author_boundary.md` and `onhour_20261123_t6_p19_q10q12_mixed_digit_exact_exclusion.md`, which claim full author-side elimination of remaining p19 orders. Their large C++ enumerators and exact source/task consistency remain independently unaudited here; the p19-layer *Native* admission and global T6=2332 proof are still open.

Review disposition at its exact scope: **mathematical derivation complete; nonauthor written/arithmetic review corroborated; native Review accepted 0, Result accepted 0, Task completed 0, parent objective completed 0**. Keep author/reviewer identities, Source pins, and task owner boundaries intact.
