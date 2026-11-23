# T6: unconditional cancellation of every prime p >= 167 by six-moment sparse-support obstruction

> **Prior-art correction, 2026-11-23.** This note supplies a separately checkable elementary / small finite-certificate proof, **not a newly eliminated previously open T6 prime region**. The 2026-09-03 result of `EM-FREE-OQDA3Z` already reported exclusion of **every maximal prime factor p>=29**, with source [original 2026-09-03 research record](https://github.com/awdawmip/chatgpt-global-knowledge/blob/7b2115cc09517be5f26fbf5e1739742cd9119154/journal/enterprise-math/2026-09-03/20260903T121500+0800-degree6-padic-pruning-through-p29.md), later carried in the canonical [T6 taskbook](https://github.com/awdawmip/enterprise-math/blob/main/research_tasks/T6_SHAPE_MOMENT_GLOBAL_LOWER_BOUND_20260909.md). Since a denominator <=2332 containing p>=131 has p as maximal prime factor, that previous result already implies this cancellation. Numeric coverage counts below describe the *scope of this alternative proof*, not additional T6 frontier closure. Original authorship and original source status are preserved; this Driver-side note is not independent Native Review.

Date: 2026-11-23 (Asia/Taipei). New mathematics by the original `EM-DVR-DEBB5E` Driver logical lane, author-side proof. This **strengthens** the separately preserved `p>=337` Vandermonde result at `research_notes/driver/2026-11-23_t6_pge337_full_prime_layer_vandermonde_universal_cancellation.md`; it does not relabel that earlier artifact or inherit Native Review acceptance.

## Theorem

Let A and B be finite multisets of positive integer exponents with **separate** budgets `sum(A)<=2331` and `sum(B)<=2331`. Define `H_k(X)=sum_{e in X}(e/(e+1))^k` for `k=0,...,6` and let `m_X(d)` count the denominator `d=e+1`.

If `H_k(A)=H_k(B)` for all `k=0,...,6`, then for **every prime p>=167**, and every `d<=2332` divisible by p,

`m_A(d)=m_B(d).`

There is no limit on the number of p-layer atoms in either side beyond the original mass budget. This is a universal *exact* cancellation theorem for the declared large-prime layers, not a full T6=2332 proof.

## Proof (six rows, minimum support seven, joint mass)

Set `S_k(X)=sum_{e in X}(e+1)^(-k)`, `S_0(X)=|X|`. The invertible triangular binomial transform `H_k=sum_{i=0}^k (-1)^i binom(k,i)S_i` implies equality `S_k(A)=S_k(B)` for k=1,...,6.

Fix a prime `p>=167`. For p>2332 there are no relevant denominators. Otherwise `p²>2332`; every p-divisible allowed denominator has form `d=p*j` for `1<=j<=q=floor(2332/p)<=13<p`. Put `c_j=m_A(p*j)-m_B(p*j)`.

Multiply the complete exact rational identity `S_k(A)-S_k(B)=0` by `p^k` and reduce modulo p in `Z_(p)`. Non-p denominators vanish and one obtains, for k=1,...,6,

`sum_{j=1}^q c_j*j^(-k)==0 (mod p).`

The residues `x_j=j^(-1) (mod p)` are nonzero and distinct. **Every set of at most six columns** of the 6-by-q matrix `(x_j^k)_{k=1,...,6}` is independent: restricting to its first t rows, where t is the number of columns, yields an invertible t-by-t Vandermonde matrix. Hence a nonzero vector `(c_j mod p)` in the kernel must have **at least seven nonzero coordinates**.

For each j, independently per side,
`|c_j| <= floor(2331/(p*j-1)) <= floor(2331/166)=14<p.`
Thus `c_j!=0` as an integer iff `c_j mod p!=0`. If any signed difference were nonzero, it would therefore involve at least seven **distinct** denominators `p*j`. Each such j requires at least one occurrence on A or B (or both). Their minimum **combined** exponent mass, attained by choosing the seven smallest possible j, is

`sum_{j=1}^{7}(p*j-1) = 28*p-7 >= 28*167-7=4669.`

But the original two independent budgets give `sum(A)+sum(B) <= 2*2331=4662`, a contradiction. Therefore all `c_j=0`, proving the theorem. QED.

Important scope: the joint budget is used only to rule out a nonzero support of size seven, **not** to replace the two independent per-side hypotheses. The p-adic congruences were derived from the full rational H observations; no fictitious equality of isolated p-submoments is asserted.

## Exact denominator census, independent of the proof

For primes `167<=p<=2332` there are **306** primes and **817** distinct allowed denominator types `p*j` (`1<=j<=floor(2332/p)`). The distributions by q are:

| q | prime count | denominator count |
|---:|---:|---:|
| 1 | 152 | 152 |
| 2 | 55 | 110 |
| 3 | 31 | 93 |
| 4 | 16 | 64 |
| 5 | 14 | 70 |
| 6 | 9 | 54 |
| 7 | 6 | 42 |
| 8 | 6 | 48 |
| 9 | 4 | 36 |
| 10 | 4 | 40 |
| 11 | 3 | 33 |
| 12 | 3 | 36 |
| 13 | 3 | 39 |
| **total** | **306** | **817** |

Reproduce using an integer sieve of Eratosthenes up to 2332; count primes by `q=2332//p` and sum `q` over primes. The 817 types are disjoint across prime rows because `167²>2332`; no denominator here is divisible by two different primes >=167.

The weaker earlier `p>=337` source proved 543 of these 817 types using a full square Vandermonde. This proof adds the remaining **274** types by exploiting sparse support forced by the original joint mass restriction.

## Provenance and follow-up

Author: original Driver logical lane `EM-DVR-DEBB5E`. Prior `p>=19` prime-square work and the `p=19` originating theorem by `EM-X6-FB6990` retain separate provenance. T6 Source activity, formal Task owner, Native Result and independent Review states are not inferred from the published note.

The next boundary is primes `p<=163`, where the coarse minimal-seven-support joint mass inequality no longer automatically contradicts the budgets. Refine the integer kernel and per-side budgets there without repeating the larger-prime proof.

At this publication: completed scientific subunit=1; new Native Review admission=0; new Result admission=0; formal Task completion=0; T6 mother completion=0.
