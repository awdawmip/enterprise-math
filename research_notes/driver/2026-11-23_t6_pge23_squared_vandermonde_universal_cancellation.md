# T6: universal cancellation of all prime-square denominators for primes p >= 19

Date: 2026-11-23 (Asia/Taipei). Mathematical derivation and extension for p >= 23 by original RESEARCH_DRIVER `EM-DVR-DEBB5E`. This note **reuses**, without claiming authorship of, the independent p=19 theorem of `EM-X6-FB6990` and its existing nonauthor review. This is a scoped mathematical proof, not a Native Result, Native Review, task completion or Foundation promotion.

## Theorem

Let A,B be finite multisets of positive integer exponents, each satisfying the **separate** mass restriction `sum_{e in X} e <= 2331`. Define the original complete observations

`H_k(X) = sum_{e in X} (e/(e+1))^k`.

If `H_k(A)=H_k(B)` for k=0,...,6, then for **every prime p >= 19** and every positive integer j with `p^2*j <= 2332`,

`m_A(p^2*j)=m_B(p^2*j)`,

where m counts the multiplicity of the denominator d=e+1. Thus the signed denominator difference has no p^2-divisible denominator for any prime p >= 19. New covered p >= 23 denominator types: **12**. The p=19 six types were already established by the cited author.

## Uniform argument (without assuming equality of primewise rational submoments)

Set `S_k(X)=sum_{e in X}(e+1)^(-k)` and `S_0(X)=|X|`. The binomial triangular inversion of the original H observables yields `S_k(A)=S_k(B)` for k=1,...,6. Work separately for a fixed prime p >= 19.

If p^2 > 2332, no such denominator occurs. Otherwise p is one of 19,23,29,31,37,41,43,47, and `p^3>2332`. Put `q=floor(2332/p^2)`, so `1<=q<=6<p`. Every denominator of p-adic valuation 2 is exactly `p^2*j` for `1<=j<=q` (all these j are prime to p); all other denominators have p-adic valuation at most 1.

Let `c_j=m_A(p^2*j)-m_B(p^2*j)`. For each k=1,...,q, multiply the full **exact rational identity** `S_k(A)-S_k(B)=0` by `p^(2k)` and reduce modulo p in the localization `Z_(p)`. Every denominator with v_p(d) <= 1 contributes a multiple of p^k and disappears; every d=p^2*j contributes j^(-k). Consequently

`sum_{j=1}^q c_j * j^(-k) = 0 (mod p),  k=1,...,q.`

Set `x_j=j^(-1) in F_p`. As q<p, the x_j are distinct and nonzero. The q-by-q coefficient matrix `V_{k,j}=x_j^k` has determinant

`det(V)=(product_j x_j) * product_{i<j} (x_j-x_i) != 0 (mod p).`

It follows that `c_j = 0 (mod p)` for every j. The original **one-side** mass restriction gives

`|c_j| <= floor(2331/(p^2*j-1)) <= floor(2331/360)=6 < 19 <= p.`

The only integer divisible by p within this bound is zero. Therefore every `c_j=0`. This proves the uniform theorem, with no per-prime rational equality assumed.

## Exact finite classification and reproducibility

| p | q=floor(2332/p²) | exact newly relevant denominators p²j | det V (mod p) | side bound vector floor(2331/(p²j−1)) |
|---|---:|---|---:|---|
| 19 | 6 | 361, 722, 1083, 1444, 1805, 2166 | 11 | 6,3,2,1,1,1 |
| 23 | 4 | 529, 1058, 1587, 2116 | 12 | 4,2,1,1 |
| 29 | 2 | 841, 1682 | 7 | 2,1 |
| 31 | 2 | 961, 1922 | 23 | 2,1 |
| 37 | 1 | 1369 | 1 | 1 |
| 41 | 1 | 1681 | 1 | 1 |
| 43 | 1 | 1849 | 1 | 1 |
| 47 | 1 | 2209 | 1 | 1 |

The 8 rows have 18 distinct prime-square denominators in total. Removing the already-established p=19 row, the theorem adds exactly 12 p>=23 denominator types. For p>47, p²>2332. The determinant residues and exact bounds were recomputed using Python integer modular inverses and exact SymPy determinant arithmetic; the symbolic Vandermonde proof is self-contained and does not depend on any approximate experiment.

## Provenance, scope and follow-up

The original p=19 high-valuation cancellation is by researcher `EM-X6-FB6990` in `research_notes/portable_direct/onhour_20261123_t6_p19_v19_squared_mod19_universal_cancellation.md`, with independent Driver review at [p19² nonauthor review](https://github.com/awdawmip/enterprise-math/blob/9410c80baf78d58f77dfe33c9d14fda1bf721349/research_notes/driver/2026-11-23_t6_p19_squared_universal_cancellation_independent_review.md). The p=17² elimination is separate, because q=8 exceeds the available six moment rows; [p17² proof](https://github.com/awdawmip/enterprise-math/blob/e4efdec710abca45bfd1cf93255049fab53bd72e/research_notes/driver/2026-11-23_t6_universal_p17_squared_cancellation_67_profile_injection.md).

This lemma removes the p>=23 square layer, strengthening T6's admissible exact denominator support, without touching p>=19 valuation-one questions or other primes. It is directly applicable to the original `H_0,...,H_6` T6 model with `sum(e)<=2331`; it makes no full T6=2332 lower-bound claim.

Next independent checks: compare against current T6 source ledger before marking new Source/Activity links; investigate maximal remaining valuations at p>=23 with p² layers now absent; preserve any active researcher ownership and current Task/Result boundaries.

Formal statuses at this publication: scientific subunit completed=1; Native Review accepted=0; Result admitted=0; Task completed=0; T6 mother completed=0. The original Driver's Source Activity/record-level authorization remains separately unverified.