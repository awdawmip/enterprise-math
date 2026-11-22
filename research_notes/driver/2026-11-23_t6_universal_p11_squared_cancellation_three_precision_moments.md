# T6: universal cancellation of the 11² denominator layer from three reciprocal moments

**Date:** 2026-11-23 (Asia/Taipei). **Original scientific contribution:** RESEARCH_DRIVER `EM-DVR-DEBB5E`, continuing own session `MCP-9b4714dc46b948afa4875a86c89c713c`. **Evidence status:** exact finite-exhaustion theorem and locally executed independent integer checker, not Native Review, accepted Result, formal Task closure or mother-objective closure. This note extends the author's own p7³/p11³/p13² cancellation observation in `research_notes/driver/2026-11-23_t6_universal_p7cube_p11cube_p13square_cancellation.md`.

## Exact theorem

Let `A,B` be finite **multisets** of positive integers `e>=1`, with separate budgets `sum(A)<=2331` and `sum(B)<=2331`. For `k=0,1,2,3` define `H_k(X)=sum_{e in X}(e/(e+1))^k`. If `H_k(A)=H_k(B)` for `0<=k<=3`, then for every `d>=2` divisible by `11²`, the multiplicity of `e=d-1` is the same in `A` and `B`:

`m_A(d)=m_B(d)` whenever `121|d`.

There is **no hypothesis** restricting the maximal prime factor or requiring rational moments of one primary component to agree separately. The result applies, in particular, to full T6 equality through H6. It does not eliminate remaining denominator layers of valuation one, nor close the global T6=2332 lower-bound objective.

## Proof

Write `S_k(X)=sum_{e in X}(e+1)^(-k)`. Since `(e/(e+1))^k=(1-1/(e+1))^k`, the binomial triangular transformation from `S_0,...,S_k` to `H_0,...,H_k` is invertible. The assumptions imply `S_1(A)-S_1(B)=S_2(A)-S_2(B)=S_3(A)-S_3(B)=0` as exact rationals.

**First remove 11³.** The only admissible denominator with 11-adic valuation at least 3 is `d=1331`: `11⁴>2332`, and `2*1331>2332`. Each side can contain at most one copy because its exponent weighs 1330. Multiply exact `S_1(A)-S_1(B)=0` by `11³` and reduce modulo 11 in `Z_(11)`. All lower-valuation denominators disappear, leaving `m_A(1331)-m_B(1331) ≡ 0 (mod 11)`. This difference lies in `{-1,0,1}`, so it is zero. Cancel the matched copies from both sides.

**Strong mixed-valuation signatures.** The remaining denominators of exact 11-adic valuation two are `d=121j`, where `1<=j<=19` and `11∤j` (18 named denominator types). Write `a_j=m_A(121j)`, `b_j=m_B(121j)`, each satisfying independently
`sum_{j}(121j-1)a_j <=2331`, respectively the same condition for `b`.

For each `k=1,2,3`, multiply the **full**, unseparated equality `S_k(A)-S_k(B)=0` by `11^(2k)`. Terms with denominator valuation one are divisible by `11^k`; terms with valuation zero by `11^(2k)`; higher valuation has just been cancelled. Hence, without assuming componentwise rational equality,

`sum_j (a_j-b_j) * j^(-k) = 0 (mod 11^k),  k=1,2,3.`

All inverses exist because `11∤j`.

**Finite injection.** Let `P` be **all** nonnegative integer vectors `a=(a_j)` with `sum_j(121j-1)a_j<=2331`. Define the exact integer-vector signature
`sig_K(a) = (sum_j a_j * j^(-k) mod 11^k)_{k=1,...,K}`.

The supplied independent standard-library checker exhausts **all** `P` and uses a separate unbounded generating-function coefficient DP to cross-check the total. Exact results:

| Signature `K` | Different signature fibers | Distinct unordered colliding profile pairs |
|---:|---:|---:|
| 1 | 11 | 184,537 |
| 2 | 1,038 | 1,498 |
| **3** | **2,020** | **0** |

Both independent profile-count paths return **2,020** feasible vectors, and two modular-inverse implementations agree for each `K=3` signature. Thus `sig_3` is injective on the entire feasible per-side profile set. The three congruences force `a=b`; together with the 1331 cancellation this eliminates **every** denominator divisible by 121. QED.

An explicit witness that the first two signatures alone are insufficient for this finite argument is the empty profile versus `7×(d=121)+2×(d=242)+1×(d=484)`, of side mass `7*120+2*241+483=1805`: the first two signatures are both zero, but the third is 444 mod 1331.

## Fixed reproducibility and research boundaries

- Program: `research_checks/T6_P11_SQUARED_THREE_MOMENT_EXACT_PROFILE_20261123.py`, published at commit `19d11e26b7bd124357202a4f3790b3e0092994b7`, verified byte-identically after GitHub write.
- Execution in the original Driver turn: `K1: 2020/11/184537; K2: 2020/1038/1498; K3: 2020/2020/0; PASS`. No approximate floating-point step.
- Mathematical assumption and data stay in the original T6 two-side full moment model. No isolated p-primary moment equality, custom axiom, borrowed researcher identity, prior author's proof replacement, or unaudited global completion.
- Existing original scientific authors, q14 delegation ownership and Native review state remain unchanged. This is **one new independent mathematical subunit**. Native Review accepted 0, Result accepted 0, formal Task done 0, mother objective done 0.
- Next relevant global frontier: apply the high-valuation cancellation collection to the remaining maximal-p=17 once-power and lower-prime mixed-modulus possibilities, with original cost and full H0..H6 constraints; verify exact q14 delegation bytes before formal nonauthor review.
