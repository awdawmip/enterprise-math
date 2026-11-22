# T6: every denominator with 3-adic valuation at least four cancels from H0–H6

2026-11-23 Asia/Taipei. Scientific derivation and exact enumeration by original RESEARCH_DRIVER `EM-DVR-DEBB5E` / own SID `MCP-9b4714dc46b948afa4875a86c89c713c`. One independently saved finite proof subunit; not formal Native Result acceptance, Task closure or Foundation promotion.

## Theorem in the original T6 domain

Let `A,B` be two finite multisets of **positive integer exponents** `e>=1`, with `sum_{e∈A}e<=2331`, `sum_{e∈B}e<=2331`. Define `H_k(X)=sum_{e∈X}(e/(e+1))^k`. If `H_k(A)=H_k(B)` for **all** `k=0,1,2,3,4,5,6`, then the multiplicity of every denominator `d=e+1` divisible by `3^4=81` agrees exactly:

`m_A(d)=m_B(d),  81|d`.

There is no maximal-prime, sign-uniqueness or separate p-primary moment-equality assumption. The theorem does *not* remove the remaining 3¹, 3² or 3³ denominator layers and does not close T6=2332.

## Proof via descending high-valuation congruence injection

Let `S_k(X)=sum_{e∈X}(e+1)^(-k)`. The triangular binomial transform `H_k=sum_{i=0}^k(-1)^i binom(k,i)S_i` shows exact equality of `S_k(A)` and `S_k(B)` for `k=1,...,6`.

For an exact denominator valuation `v=v_3(d)`, write `d=3^v j` with `3∤j`. Assume all higher-valuation contributions have already been proved equal and cancelled. Multiplying each **full** `S_k(A)-S_k(B)=0` by `3^(vk)` gives, modulo `3^k`,

`sum_{j:3∤j} (m_A(3^v j)-m_B(3^v j))*j^(-k) ≡ 0 (mod 3^k)`.

This holds because every *remaining* lower-valuation denominator has `v_3(d)<=v-1`, hence acquires a factor of at least `3^k`; no equality of prime-primary rational moments was assumed. Each side's profile is restricted by its **original** mass budget
`sum_{j:3∤j}(3^v j-1)m_j<=2331`.

Here `3^8=6561>2332`, so the admissible positive exact valuations at least four are `v=7,6,5,4`. For each, exhaustively enumerate the **entire** mass-feasible profile set, compute the mixed-precision `K`-signature
`sig_K(m)=(sum_j m_j*j^(-k) mod 3^k)_{k=1,...,K}`, and check injection:

| Exact level v | Named j types | Per-side profiles | First K with injective signature | Remaining collision pairs one level earlier |
|---:|---:|---:|---:|---:|
| 7 | 1 | 2 | 1 | — |
| 6 | 2 | 6 | 2 | 4 at K=1 |
| 5 | 6 | 60 | 4 | 2 at K=3 |
| **4** | **19** | **5,148** | **6** | **77 at K=5** |

The full intermediate signature counts and collision counts are fixed in the independent checker. At level four, they are:
`K1: 3 signatures / 4,493,146 pairs;`
`K2: 27 / 499,779;`
`K3: 243 / 58,265;`
`K4: 3,372 / 2,537;`
`K5: 5,071 / 77;`
`K6: 5,148 / 0.`

At each level `v=7,6,5,4`, the available observed `S_1,...,S_6` moments include the requisite first `K` congruences; since the finite profile map is injective, its signed multiplicity differences vanish. Descending induction proves cancellation of every denominator with valuation at least four. QED.

## Computation and evidence strength

Fixed standard-library Python integer verifier: `research_checks/T6_P3_FOURTH_SIX_MOMENT_INJECTION_CHECK_20261123.py`, published and blob/readback verified at GitHub `915a60c706dcf1bfb9f6d03625927cc15d2b73d7`. For each level it independently computes the total feasible profile count by (i) all multiplicity vectors and (ii) generating-function coefficient dynamic programming, then counts every exact modular signature fiber with no floating-point steps. The program actually ran to `PASS: all denominators divisible by 3^4 cancel for H0..H6`.

This result is an exact, finite-checker-supported mathematical proof of a **high-valuation necessary condition only**. It is not a review of any unrelated source result and does not replace existing original researcher proofs. Formal Native Review accepted 0, Result accepted 0, Task done 0, mother-objective done 0. The remaining 3^3 and smaller-prime/mixed-prime layers, as well as valuation-one maximal p17, are genuine open parts of the global proof portfolio.
