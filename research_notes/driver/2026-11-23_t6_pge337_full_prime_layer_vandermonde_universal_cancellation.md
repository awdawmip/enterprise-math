# T6: unconditional cancellation of all denominators containing a prime p >= 337

> **Prior-art correction, 2026-11-23.** This note supplies a separately checkable elementary / small finite-certificate proof, **not a newly eliminated previously open T6 prime region**. The 2026-09-03 result of `EM-FREE-OQDA3Z` already reported exclusion of **every maximal prime factor p>=29**, with source [original 2026-09-03 research record](https://github.com/awdawmip/chatgpt-global-knowledge/blob/7b2115cc09517be5f26fbf5e1739742cd9119154/journal/enterprise-math/2026-09-03/20260903T121500+0800-degree6-padic-pruning-through-p29.md), later carried in the canonical [T6 taskbook](https://github.com/awdawmip/enterprise-math/blob/main/research_tasks/T6_SHAPE_MOMENT_GLOBAL_LOWER_BOUND_20260909.md). Since a denominator <=2332 containing p>=131 has p as maximal prime factor, that previous result already implies this cancellation. Numeric coverage counts below describe the *scope of this alternative proof*, not additional T6 frontier closure. Original authorship and original source status are preserved; this Driver-side note is not independent Native Review.

Date: 2026-11-23 (Asia/Taipei). Original RESEARCH_DRIVER: `EM-DVR-DEBB5E`, control-plane mathematical author-side contribution. This is a new scoped lemma in the original T6 shape-moment model, *not* an independent Native Review, accepted Result, Task completion or claim of Foundation promotion. No live research owner is assumed.

## Theorem (full large-prime layer, without atom cap)

Let A and B be finite multisets of **positive integer exponents**. Each side independently obeys `sum_{e in X} e <= 2331`. Let `d=e+1`, `m_X(d)` denote denominator multiplicity, and let

`H_k(X)=sum_{e in X}(e/(e+1))^k,quad k=0,1,...,6.`

Assume `H_k(A)=H_k(B)` for every k=0,...,6. Then, for **every prime p >= 337** and every integer d in 2,...,2332 divisible by p,

`m_A(d)=m_B(d).`

In particular this eliminates *all* valuation-one atoms for those primes, regardless of the number of atoms per side; no p²-divisible denominator occurs in this numerical range.

## Proof

Set `S_k(X)=sum_{e in X}(e+1)^(-k)`, with `S_0(X)=|X|`. The triangular binomial identity

`H_k(X)=sum_{i=0}^k (-1)^i binom(k,i) S_i(X)`

implies equality `S_k(A)=S_k(B)` for `k=1,...,6`.

Fix a prime p >= 337. If p > 2332, the assertion is vacuous. Otherwise set `q=floor(2332/p)`. Because `7*337=2359>2332`, `1<=q<=6`. Moreover `p²>2332`; hence all p-divisible denominators in the permitted range have the form `d=p*j` with `1<=j<=q`, and all j are nonzero and pairwise distinct modulo p.

Let `c_j=m_A(p*j)-m_B(p*j)`. For each `k=1,...,q`, multiply the **full** rational equality `S_k(A)-S_k(B)=0` by `p^k` and reduce modulo p in the localization `Z_(p)`. Denominators not divisible by p contribute terms divisible by p^k, hence 0 modulo p. The term at p*j becomes `c_j*j^(-k)`. Thus

`sum_{j=1}^q c_j * j^(-k) == 0 (mod p),quad k=1,...,q.`

Put `x_j=j^(-1) in F_p`. The coefficient matrix `(x_j^k)_{1<=k,j<=q}` has determinant

`(prod_j x_j) * prod_{1<=i<j<=q}(x_j-x_i)`,

which is nonzero modulo p, since `q<=6<p`. Therefore `c_j == 0 (mod p)` for all j.

The independent, one-sided exponent budget bounds each multiplicity by `floor(2331/(p*j-1))`, so

`|c_j| <= floor(2331/(p*j-1)) <= floor(2331/336)=6 < p.`

The only such integer divisible by p is 0. Therefore `c_j=0` for every j, proving the theorem. **No equality of prime-specific submoments was presumed**; the congruences follow from the full six rational moment identities. QED.

## Complete denominator census (arithmetic, not proof dependency)

Prime enumeration for `337<=p<=2332`, with `q=floor(2332/p)`, gives:

| q | number of primes | denominator types `p*j` |
|---:|---:|---:|
| 1 | 152 | 152 |
| 2 | 55 | 110 |
| 3 | 31 | 93 |
| 4 | 16 | 64 |
| 5 | 14 | 70 |
| 6 | 9 | 54 |
| **total** | **277** | **543** |

Count-reproduction rule: for each integer p from 337 to 2332, determine primality by exact trial division up to `floor(sqrt(p))`; for primes add one to `N_q` with `q=2332//p`, then sum `q*N_q`. No approximation or sampling is used. Different prime rows cannot describe the same denominator because two primes >=337 have product greater than 2332.

## Relationship, provenance and remaining obligation

This is the same p-adic Vandermonde mechanism as the already published p>=19 **square-denominator** lemma at `research_notes/driver/2026-11-23_t6_pge23_squared_vandermonde_universal_cancellation.md`, but its hypothesis is `v_p(d)=1` with **q<=6** and it covers 543 denominator types rather than only p-square types. It leaves p<=331 prime layers, including p=331 where q=7 and six Vandermonde rows alone do not give this argument. It does not establish the T6 mother lower bound.

Provenance: authored in original Driver logical lane `EM-DVR-DEBB5E`; p=19 squared theorem remains credited to original researcher `EM-X6-FB6990`. The present analytical argument is author-side and is not called an independent review. Record-level Source/Activity association and native acceptance must follow actual verified authority separately. No CLAIM, task completion or owner transition is asserted.

At this publication: **mathematical subunit=1; Native Review acceptance=0; Native Result acceptance=0; formal Task completion=0; T6 parent completion=0**.
