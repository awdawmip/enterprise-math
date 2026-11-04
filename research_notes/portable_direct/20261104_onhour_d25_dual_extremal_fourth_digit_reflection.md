# D25 dual extremal-layer p-adic reflection and the fourth-digit source port

**Date:** 2026-11-04. **Scope:** AUTHOR-DERIVED / EXACT RATIONAL-PROOF / FINITE-EXACT CHECKED / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING. This is neutral GitHub research material, not a Source-native CLAIM/checkpoint/Result.

**Task:** `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`; publication `TP2-B6F4FC938FF94941C1B7`; frozen scientific pin `c47e13e4aba0e006366f989d6334d443f6333ae3`. Research logical lane `chatgpt-research-onhour-enterprise-math-20260923`; maintenance `chatgpt-hourly-enterprise-math-20260921` is separate. Reuses existing signed fourth-digit observation, Green/two-seam, other researcher's Clausen source, and the already-proved Guo–Zudilin (2019) quartic theorem; none are re-claimed.

## Original coefficients and exact all-prime theorem

For every prime `p>=5`, all indices `0<=k<p`, retain original rational coefficients

[
a_k=rac{(2k)!(3k)!}{(k!)^5,216^k}
=rac{inom{2k}{k}^{2}inom{3k}{k}}{216^k},qquad
b_k=rac{(4k)!}{(k!)^4,2304^k}
=rac{inom{2k}{k}^{2}inom{4k}{2k}}{2304^k}.
]

Let `m_a=floor((p-1)/3)`, `m_b=floor((p-1)/4)`. For each `1<=k<=m_a`, the low coefficient `a_k` is a `p`-unit, `v_p(a_{p-k})=3`, and

[
oxed{k^3a_k(a_{p-k}/p^3)equiv-1/18pmod p.} 	ag{A}
]

For each `1<=k<=m_b`, likewise `b_k` is a `p`-unit, `v_p(b_{p-k})=3`, and

[
oxed{k^3b_k(b_{p-k}/p^3)equiv-1/96pmod p.} 	ag{B}
]

### Proof (all primes, not an interpolation)

Legendre's formula applied to the original rational coefficients, whose denominator bases are units for `p>=5`, gives exactly `v_p(a_j)=floor(2j/p)+floor(3j/p)` and `v_p(b_j)=floor(4j/p)` for `j<p`. These floors give the stated low (0) and reflected high (3) valuations, including `p=5,7`.

Exact recurrences, with unit denominators for `j<p-1`, are

[
R_a(j)=rac{(2j+1)(3j+1)(3j+2)}{36(j+1)^3},quad
R_b(j)=rac{(4j+1)(4j+2)(4j+3)}{576(j+1)^3}.
]

For `1<=k<m_a` (respectively `k<m_b`), the corresponding numerators are units, and direct substitution `j=p-k-1` gives

[
rac{R_a(k)}{R_a(p-k-1)}
equivrac{k^3}{(k+1)^3},qquad
rac{R_b(k)}{R_b(p-k-1)}
equivrac{k^3}{(k+1)^3}pmod p.
]

Hence both `k^3 a_k a_{p-k}/p^3` and `k^3 b_k b_{p-k}/p^3` are constant over their full specified index intervals. These divisions are in `Z_(p)` after precisely three factors of `p` are removed. To compute each constant, use Wilson's theorem and p-block factorization:

[
(2p-2)!/pequiv-1,quad
(3p-3)!/p^2equiv-1,quad
(4p-4)!/p^3equiv-1pmod p.
]

The second and third residues follow by extracting `p(2p)`, respectively `p(2p)(3p)`, then multiplying the surviving p-free blocks, which are `-1/2`, respectively `-1/6`. Since `(p-1)!equiv-1`, `216^{p-1}equiv2304^{p-1}equiv1`, both endpoint normalized coefficients are `a_{p-1}/p^3=b_{p-1}/p^3=-1 (mod p)`. Finally `a_1=1/18` and `b_1=1/96`; (A) and (B) follow. QED.

## Exact source-faithful valuation-three port (all primes p>=5)

Define the **complete original valuation-three layers**, preserving every index and signed weight:

[
A_3=sum_{n=p-m_a}^{p-1}(6n+1)a_n,qquad
B_3=sum_{n=p-m_b}^{p-1}(8n+1)b_n.
]

Reindex `n=p-k`, use (A),(B) and `6(p-k)+1equiv1-6k`, `8(p-k)+1equiv1-8k`, yielding

[
oxed{rac{A_3}{p^3}equiv-rac1{18}
sum_{k=1}^{m_a}rac{1-6k}{k^3a_k}pmod p},qquad
oxed{rac{B_3}{p^3}equiv-rac1{96}
sum_{k=1}^{m_b}rac{1-8k}{k^3b_k}pmod p}. 	ag{C}
]

All denominators on the right are units. In particular the old p³ truncation omitted a fourth-digit population which is now exactly reconstructible from its paired low source.

Let `W_p=sum_{n=0}^{p-1}(6n+1)a_n`, `V_p=sum_{n=0}^{p-1}(8n+1)b_n`, `epsilon_p=(-3/p)`, `J_p=W_p-2V_p+epsilon_p*p`, `H_a=A_3/p^3 (mod p)`, `H_b=B_3/p^3 (mod p)`. Denote the **actual lower-valuation bulk** by `J_bulk=(W_p-A_3)-2(V_p-B_3)+epsilon_p*p`. Unconditionally, including when the proposed fourth-digit law fails,

[
oxed{J_pequiv J_{m bulk}+p^3(H_a-2H_b)pmod{p^4}.} 	ag{D}
]

The optional universal `J_p≡0 (mod p^4)` is **a conjecture**, not proved by (D). Only in the case `p^3mid J_{m bulk}` may a normalized bulk digit `J_bulk/p^3mod p` be used to express its requisite cancellation. The frozen hard target remains the original `W_p-V_p≡0 (mod p^3)` and corresponding `Delta_p-R_p≡0 (mod p)` in classes 13,19 mod24; this stronger fourth-digit route is diagnostic, not a new gate.

## Reproducible exact certificate and discriminating examples

Companion `d25_dual_extremal_reflection_checker_20261104.py` actually executed over every one of the **667 primes 5<=p<=5000**. The original coefficient recurrences were evaluated with exact integers modulo `p^4`; it checked **515709 low/high a pairs + 386697 b pairs = 902406 original-source reflection equalities**, all PASS; (C) and (D) passed for all 667. Every original coefficient at `p=5,7,11,13,19,97,373` was also independently reconstructed using integer `math.comb` rather than the recurrence (PASS). The earlier finite `J_p≡0 (mod p^4)` conjecture passed 667/667, a regression only.

| p | H_a | H_b | H_a-2H_b mod p | J_bulk/p³ mod p (finite only) |
|---:|---:|---:|---:|---:|
| 11 | 6 | 1 | 4 | 7 |
| 13 | 5 | 6 | 6 | 7 |
| 19 | 4 | 16 | 10 | 9 |
| 97 | 44 | 68 | 5 | 92 |
| 373 | 278 | 119 | 40 | 333 |

The sum of the last two columns is zero modulo the displayed prime in each finite sample. Across all 667, `H_a-2H_b` is **nonzero for 665 primes**, and zero only at `p=107,1289` in this interval: the high layer cannot generally be discarded at the fourth digit. BRC observer = indexed ordered original source pairs `(k,p-k)`, exact unit residues, valuation class, signed weight and reduction mod `p^4`. This is not a native X6/H0/B0 experiment.

## Recovery, obligations, and next exact action

Existing original control `target_request_id=research-onhour-20261031-0205-dispatch-r15` has a **full original GitHub receipt** (bridge Issue #6633): `COMPLETE/FAILED: UPSTREAM_CODE_REVIEW_REQUIRED`, not NO_DISPATCH. A historical 2026-10-30 recovery_status (bridge Issue #6632) reported its own active Researcher session `MCP-de3e5bafb24f43f4a5e6285e7601676a` but no unopened claim, run or pending transport; this old read-only projection grants no present Source ownership. Historical three staging files were neutrally archived through `preserve-staging-20261007-1114-onhour-01` (bridge Issues #6634-6636), not merged into an accepted Result. No new role-bound request was issued, and neither native CLAIM/OPEN/checkpoint nor Research admission was established in this author's client. Existing support #1558 is for control; **#1559 remains the original fixed373 H0/B0 native-evaluator support, unexecuted/pending owner**.

Next research action: seek an independent terminating WZ/Green/Clausen certificate for the actual **p³ original W216−V2304 cancellation**; separately use the proved high-source port (C) to distinguish candidate fourth-digit mechanisms by signed bulk and boundary tests at 11,13,19,97,373. Preserve the exact p373 native [X]U mod139129, module rank, semilinear Frobenius, signed observer and independent reproduction as unexecuted. Preserve frozen scientific pin and separate logical lanes; no scheduler, notifications, or other automation modifications.
