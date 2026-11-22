# T6: universal elimination of every denominator divisible by 5³ from H0–H4

2026-11-23 Asia/Taipei. RESEARCH_DRIVER `EM-DVR-DEBB5E`, own original SID `MCP-9b4714dc46b948afa4875a86c89c713c`. One new exact finite-exhaustion mathematical result with a separate standard-library integer checker. This is **not** formal Native Review/Result admission or global Task closure. Earlier T6 author attributions remain unchanged.

## Exact theorem

Let `A` and `B` be finite multisets of positive integers `e>=1`, each having `sum e<=2331`. Define the original T6 shape moments `H_k(X)=sum_{e in X}(e/(e+1))^k`. If `H_k(A)=H_k(B)` for `k=0,1,2,3,4`, then every denominator `d=e+1` divisible by 125 has identical multiplicity on both sides:

`m_A(d)=m_B(d)` for all `125|d`.

This is a *whole mixed moment* consequence, with no restriction on the maximal prime factor, no separately imposed p-primary rational equality and no distinctness assumption. It implies elimination of the 5³ and 5⁴ layers for full T6 (H0,...,H6), not elimination of the 5¹ or 5² layers.

## Mathematical proof

Set `S_k(X)=sum_{e in X}(e+1)^(-k)`. By binomial inversion `H_0,...,H_4` equality yields exact `S_1,...,S_4` equality.

**5⁴ layer.** As `5^5=3125>2332`, the highest possible 5-adic denominator valuation is four. Its named denominators are `d=625j`, `j=1,2,3`; their original side-mass weights are `625j-1`. The complete feasible nonnegative profile census `sum_j(625j-1)m_j<=2331` contains **7** profiles, independently counted by recursive enumeration and unbounded-coin generating-function DP. Multiply the *full* `S_k(A)-S_k(B)=0` by `5^(4k)`, for `k=1,2`, and reduce modulo `5^k`. All terms of lower 5-adic valuation `<=3` vanish, leaving the two-coordinate signature
`(sum_j m_j*j^(-k) mod 5^k)_{k=1,2}`.
At k=1 the 7 profiles have 5 signatures (2 distinct profile pairs collide); at k=2 all **7** signatures are distinct. Therefore exact-5⁴ multiplicities coincide and cancel.

**5³ layer.** After removing the matched 5⁴ atoms, the remaining exact valuation-three denominators are `d=125j` for `1<=j<=18`, `5∤j` (15 named types). Each side has a nonnegative vector `m` satisfying `sum_j(125j-1)m_j<=2331`. For `k=1,2,3,4`, multiply the **full** `S_k(A)-S_k(B)=0` by `5^(3k)`, and reduce modulo `5^k`. Lower-valuation contributions have factor at least `5^k`, higher-valuation ones have already been cancelled. Consequently:
`sum_j (a_j-b_j)*j^(-k) ≡ 0 (mod 5^k)`, `k=1,2,3,4`.

The complete original-side-budget profile set has exactly **1,157** vectors (same recursion and independent DP). Define `sig_K(m)=(sum_j m_j*j^(-k) mod 5^k)_{k=1,...,K}`. Exhaustive exact integer computation:

| Number of moments | Distinct signatures | Distinct unordered colliding profile pairs |
|---:|---:|---:|
| 1 | 5 | 133,439 |
| 2 | 125 | 5,050 |
| 3 | 1,109 | 48 |
| **4** | **1,157** | **0** |

Thus `sig_4` is injective on every possible original-side 5³ profile, so `a=b`. Along with cancellation of exact-5⁴ atoms this proves equality for **all** denominators divisible by `5³`. QED.

## Exact verification and boundaries

The simple executable verifier `research_checks/T6_P5_CUBE_FOUR_MOMENT_INJECTION_CHECK_20261123.py` was published and authenticated by byte-for-byte GitHub readback at commit `d998a96c156bef64cb766d22591125a1f150dec8`. It uses a full recursive profile enumeration, an independent coefficient DP, exact finite-ring modular inverses and signature collision counting. The actual local run passed **every** assertion and printed the stated figures; no approximation or random sample.

The inherited p7², p11², p13², p17² and p19² saved work remains preserved at its own original source/evidence status; this theorem does not rewrite it or create unapproved formal mathematical admission. The new exact result is **one mathematical subunit**; new Native review 0, accepted Result 0, formal Task completion 0, mother goal completion 0. The next low-power p5²/p3^k/p2^k and maximal-p17 valuation-one mixed full T6 obligations remain.
