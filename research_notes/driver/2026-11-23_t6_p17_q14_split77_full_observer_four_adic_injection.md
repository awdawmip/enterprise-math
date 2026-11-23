# T6 maximal-p17 one-power q14(7,7): full-observer four-moment 17-adic injection

2026-11-23 · Original RESEARCH_DRIVER `EM-DVR-DEBB5E` · original SID `MCP-9b4714dc46b948afa4875a86c89c713c` · scientific finite derivation/check only; **not a Native Review, accepted Result, Task DONE or parent threshold proof**.

## Exact proposition

Let two exponent-denominator multisets `D+`, `D-` each satisfy the original exponent-mass bound `sum(d-1)<=2331`, and agree in their **full** shape observers
`H_k(D)=sum_{d in D}(1-1/d)^k` for `k=0,...,4` (hence also for k through 6 when the original T6 observations agree).

Assume their 17-divisible denominators all have valuation **exactly 1**. Write these as a signed multiset `U` of:

- vertical atoms `d=17(17q+r)`, `q>=1`, `1<=r<=16`, with cofactor `17q+r` 17-smooth (all prime factors at most 17), and **vertical order** `sum_vertical q=7` on **each** side, i.e. the fixed q14 split(7,7);
- q0 atoms `d=17j`, `1<=j<=16`, with arbitrary same-side multiplicities compatible with each true side mass.

The other denominators `L` may be **arbitrary 17-free integers** (including lower-prime completions), subject to the same original side budgets.

**Theorem (finite exact certificate, independent admission pending).** These hypotheses force `U+=U-` as full multisets. Consequently no **opposite-cancelled / support-disjoint** nonempty q14 split(7,7) pair in this exact one-power model can satisfy the full `H0,...,H4`, irrespective of any 17-free lower-prime completion. In particular this q14 one-power subcase does not support an `H0,...,H6` T6 collision.

**Excluded from this theorem:** denominators divisible by `17^2`; other q14 splits, p17 valuation classes, lower maximal-prime layers, and the full global T6 parent objective. The original frozen delegation plan digest `b866fa935b62df35c6be65560c5aeebb0f64b1e958c84c34e469d5faf8735d24` still requires exact immutable-byte mapping before claiming its domain is fully subsumed.

## Exact four-moment argument, without assuming lower-prime moments vanish

Set `S_k(D)=sum_{d in D}d^(-k)`. The binomial map from `(S_0,...,S_4)` to `(H_0,...,H_4)` is triangular and invertible; therefore equality of full observers implies equality of full `S_1,...,S_4`.

For the once-17-divisible portion `U`, define

`R_k(U)=sum_{d=17a in U}a^(-k)`,

where every `a` is a 17-adic unit. For the 17-free part `L`, all `S_k(L)` are 17-adic integers. Full equality of `S_k` yields the **necessary** exact relation

`R_k(U+) - R_k(U-) = -17^k (S_k(L+) - S_k(L-))`, `k=1,...,4`.

Thus the residue-vector signature

`sigma(U) = (R_k(U) mod 17^k)_{k=1}^4`

must agree for the two `U` sides. This is valid for **all** 17-free completions, not merely the pure-17-support H012 configurations. The modular inverse `a^(-k) mod 17^k` exists for every listed atom.

## Exact finite domain and full enumeration

For each vertical atom `(q,r)` its mass is `289q+17r-1`. Every vertical side has `sum q=7`; its minimum possible mass is 2039, leaving at most 292 mass for q0 atoms. Enumeration includes **all multisets with repetition**, individual true budget, all 17-smooth cofactors and all 16 q0 species.

The executable checker uses a monotone atom-index DFS for the vertical rosters; a distinct integer-partition/combinations generator verifies the exact same roster set. A separately counted q0-mass prefix sum verifies the total admissible side-state count. Modular inverses use exact integer arithmetic, with an independent inverse-then-power identity check per unit.

| Exhaustive quantity | Exact result |
|---|---:|
| Maximal-p17 allowed named vertical atoms | 60 |
| Complete vertical side rosters with order 7 and mass <=2331 | 1,907 |
| q0 side multisets with mass <=292 | 1,223 |
| Combined admissible `U` side states after actual mass filtering | **55,347** |
| Distinct four-component 17-adic signatures | **55,347** |
| Collisions between distinct admissible `U` states | **0** |
| Three-component signature collision pairs, for comparison | 1,850 |
| Those three-component pairs also disjoint on opposing named supports | 27 |

The four-component signature is therefore injective on the **entire** finite domain, not merely on the support-disjoint pairs. In particular `sigma(U+)=sigma(U-)` implies `U+=U-`. If opposing named atoms have already been cancelled, identical nonempty sides cannot retain order 7 per side. This proves the stated exclusion.

The 27 disjoint three-component matches demonstrate that the **three-component congruence screen alone** is insufficient to certify this same cancellation-normalized exclusion; these are modular ambiguities only, **not** full three-observer collisions.

## Reproduction and exact-source evidence

[Executable integer checker, read back on canonical main](https://github.com/awdawmip/enterprise-math/blob/83c41b3092f6b2f7e33e9fb65aae1d49725ef572/research_checks/T6_P17_Q14_SPLIT77_FULL_OBSERVER_FOUR_ADIC_INJECTION_20261123.py), original publication Git blob `20e6707f6d972f38aa635c8d5e9e3e366a676052`. Its asserted counts and all four modular signatures were executed locally and passed. No approximate equality or unbounded search is invoked.

Scientific provenance preserved:
- Prior q14 complete roster from `EM-EMF6D046-5A2844`, [preflight](https://github.com/awdawmip/enterprise-math/blob/9ef728a7107362eb0d4b1719ed98d00b1678357c/research_artifacts/mcp/RS-T6-SHAPE-MOMENT-GLOBAL-LOWER-BOUND/MCP-c618a61189764f23846a391a08518a1a/150b2baf7e93fb09d7e7/T6_P17_Q14_SPLIT7_7_EXACT_PREFLIGHT_20261116.md), 60 atoms /1907 rosters /809566 opposite-disjoint vertical pairs.
- Original `EM-X6-FB6990` [pure-17 H012 exact search](https://github.com/awdawmip/enterprise-math/blob/main/research_notes/portable_direct/onhour_20261122_t6_q14_h012_exact_emptiness.md) (333 oriented H01 pairs and no H2 exact matches) remains valid in its restricted support model.
- Original Driver [full-observer lower-prime gap identification](https://github.com/awdawmip/enterprise-math/blob/11ed65635e5b2549631593e58324054884f8a291/research_notes/driver/2026-11-23_t6_p17_q14_h012_lower_prime_completion_scope_correction.md) remains valid: the old **exact H012** implication does not transfer to general lower-prime completions. The present **new modular four-moment** implication closes that identified gap for the fixed one-power q14(7,7) domain by a different argument.

## Exact next action and admission boundary

Check frozen delegation-plan **immutable bytes**, its one-power/higher-valuation limits, split definition and possible out-of-model terms before asserting the frozen plan itself is closed. If it matches the stated domain, reuse this certificate instead of starting 809566 affine comparisons. Arrange genuine independent math review and formal reference/Result association through the current Driver authority; retain contributor independence. If it includes `17^2` denominators or other splits, those are genuinely open and require separate work.

Native Source/Activity association pending exact role/CAS; Native Review/Result acceptance **0** from this proof; formal Task DONE **0**; global T6 mother objective DONE **0**.
