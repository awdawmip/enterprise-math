# T6: universal elimination of every 2⁸ denominator factor from six full moments

Date 2026-11-23 Asia/Taipei. Mathematical contribution: RESEARCH_DRIVER **EM-DVR-DEBB5E**, authentic original SID `MCP-9b4714dc46b948afa4875a86c89c713c`. One new scoped finite exact proof, not an accepted Native Result, independent Source Review or global Task closure.

## Exact proposition

For two finite multisets `A,B` of positive integer exponents `e>=1`, assume **separately** `sum_{e in A} e<=2331` and `sum_{e in B}e<=2331`. Put `H_k(X)=sum_{e in X}(e/(e+1))^k`. If `H_k(A)=H_k(B)` for all `0<=k<=6`, then for every denominator `d=e+1` with `256|d` the multiplicities agree:

`m_A(d)=m_B(d)`.

The conclusion is universal: no maximal-prime restriction, no imposed isolated rational p-primary moment equality, no assumption of distinct atomic exponents. It does not remove the entire 2-primary part nor resolve global T6=2332.

## Proof

Use the exact reciprocal moments `S_k(X)=sum_{e in X}(e+1)^(-k)`. Binomial inversion from `H_0,...,H_6` proves exact `S_k(A)-S_k(B)=0` for `k=1,...,6`. Denominators `d=e+1` range in `[2,2332]`; as `2^12=4096>2332`, the 2-adic layers `v=v_2(d)>=8` occur **only** at `v=11,10,9,8`.

Induct down these exact denominator valuations. Assume the higher layers have already been proved to have equal multiplicities and have been cancelled; write exact-v denominators as `2^v j` with odd `j`. Multiply each full equality `S_k(A)-S_k(B)=0` by `2^(vk)`, then reduce modulo `2^k`. Contributions from each smaller valuation `<=v-1` vanish modulo `2^k`; higher ones have cancelled, so

`sum_{odd j} (m_A(2^v j)-m_B(2^v j))*j^(-k) ≡ 0 (mod 2^k)`, `k=1,...,6`.

The inverse of every odd `j` exists modulo `2^k`. The profile on **each original side** is constrained by its actual budget `sum_{odd j}(2^v j-1)m_j<=2331`. The finite set of all such nonnegative vectors is exhaustively enumerated, and a separate coefficient DP of `prod_j(1-z^(2^v j-1))^(-1)` through degree 2331 verifies the count.

| v₂(d) exact | Admissible odd j types | Complete side profiles | First injective prefix K of signature |
|---:|---:|---:|---:|
| 11 | 1 | 2 | 1 |
| 10 | 1 | 3 | 2 |
| 9 | 2 | 7 | 3 |
| **8** | **5** | **33** | **6** |

The mixed-precision map on profiles is
`sig_K(m)=(sum_j m_j*j^(-k) mod 2^k)_{k=1,...,K}`.
For v=8 the entire prefix table (number of distinct signatures; distinct unordered colliding profile pairs) is

`K1: 2/262; K2: 4/124; K3: 15/33; K4: 25/9; K5: 31/2; K6: 33/0.`

Thus the six-moment signature is injective on all 33 legal v8 profiles. For v9, K1..K3 have `2/9;4/3;7/0`; for v10, K1..K2 have `2/1;3/0`; v11 has 2 distinct K1 signatures. Descending induction therefore cancels each of the four high valuation layers exactly, proving all `256|d` multiplicities equal. QED.

## Finite arithmetic and scope of admission

A self-contained Python standard-library exact checker performs exhaustive original-side multiplicity enumeration, an independent DP count, and full modular signature collision verification with only integer inverses, no floating point:

[Fixed checker](https://github.com/awdawmip/enterprise-math/blob/845a88948dc434a4873be44782e18f65e662b436/research_checks/T6_P2_EIGHTH_SIX_MOMENT_INJECTION_20261123.py).

The original research execution independently enumerated the same complete profiles and all signature collision counts using integer arithmetic. The fixed checking file was written and byte-read back from the above immutable GitHub commit. Original T6 p19/p17/q14 author provenance, prior results, existing TASK owner, full-moment constraints and native admission boundaries are preserved.

This is one **new exact mathematical subunit**. Native Review accepted 0, Result accepted 0, formal Task complete 0, mother objective complete 0. In particular, at v₂=7 the corresponding six-moment profile signature of the larger original-side set is *not injective*; this finite method alone does not justify a universal 2^7 cancellation claim.
