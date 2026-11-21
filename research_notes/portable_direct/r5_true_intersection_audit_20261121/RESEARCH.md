# R5 research correction: true multi-event intersections at a primitive 16th root

**Date:** 2026-11-21 (Asia/Shanghai). **Status:** AUTHOR_EXACT_COUNTEREXAMPLE / FINITE_CYCLOTOMIC_CHECKED / NOT_REVIEWED. **Scope:** frozen 256-hypothesis scalar R5 cost observer with prices 214..314, not native X6/BRC dynamics. No formal CLAIM, Result, or Driver review is asserted. P000 remains unchanged.

## Original source and falsified reasoning step

Read-only predecessor: [all-threshold primitive-16 report at immutable 49ead3e7](https://github.com/awdawmip/enterprise-math/blob/49ead3e7754e3df58b407393a917024bc0400b8b/research_notes/portable_direct/r5_primitive16_allm_20261121/RESEARCH.md) and its companion VERIFY_PRIMITIVE16_ALL_M.py. The earlier [R5 source definition at bf88b495](https://github.com/awdawmip/enterprise-math/blob/bf88b495f9e727ab355f7ff330a01c31c03e66fa/research_notes/portable_direct/r5_primitive13_n6_universal_20261121/RESEARCH.md) defines E_i as the condition that the **sum of multiplicities on S_i is less than m**, and F_m(N) as the number of weighted price vectors satisfying at least one E_i.

The 16th-root proof replaces all pair/triple intersections of E0,E1,E2 by E_U = {sum_{p in U} a_p < m}, where U=S0 union S1 union S2={214,...,221}. That is false for m>=2: the actual intersection E_i intersection E_j requires **two separate inequalities**; a bound on multiplicity on the union is strictly stronger. For m=1 they agree, because each restricted count must vanish.

The source sets are S0={214,215,216,217,218}, S1={214,216,217,218,219,220,221}, S2={215,216,217,218,219,220,221}, S3={223,...,290}, S4={296,...,312}.

## Exact single-vector counterexample in the full five-event model

Set m=2 and choose the original 101-price vector with a_215=1, a_219=1, a_223=2, a_296=2 and all other multiplicities zero. Its cost is N=215+219+2*223+2*296=1472. The five conditions have truth values (E0,E1,E2,E3,E4)=(true,true,false,false,false). The **true** union indicator is 1. Yet the predecessor's reduction

    1_E0 + 1_E1 + 1_E2 - 2 * 1_{sum_U a < 2}

equals **2**, because sum_U a=2. E3 and E4 were deliberately made false; this is not an artifact of excluding them. Consequently the replacement is not a pointwise identity for the actual original counting problem.

## Correct leading Fourier numerator

Let z denote any primitive 16th root, with field Q[z]/(z^8+1). Six prices in 214..314 are divisible by 16: 224,240,256,272,288,304. Only the seven nonempty inclusion-exclusion masks I subseteq {0,1,2} leave all six unrestricted. Define U_I=union_{i in I} S_i and

    B_{m,I}(z)=sum_{a_p>=0 (p in U_I), ALL i in I: sum_{p in S_i}a_p<m} z^(sum_{p in U_I} p*a_p).

All variables in this sum are bounded by m-1. The **exact** primitive-16 order-six numerator is

    A_true_m(z)=sum_{empty!=I subseteq {0,1,2}} (-1)^(|I|+1)
                 * prod_{p in U_I}(1-z^p) * B_{m,I}(z).

The prior A_old_m replaces B_{m,I} by the different finite sum with only sum_{p in U_I}a_p<m. This difference directly changes the root-of-unity Fourier pole coefficient.

## Exact finite calculation

Enumerated all seven conjunctions without imposing an extra union cap, using integer polynomial reduction z^8=-1, and independently evaluated the prior union-cap expression:

| m | A_true_m, coefficients of 1,z,...,z^7 | A_old_m, published coefficients |
|---|---|---|
| 1 | (16,10,-4,-10,-16,-18,-20,-22) | same |
| 2 | (-16,4,24,40,44,48,40,36) | (-100,-76,-40,0,40,80,104,116) |
| 3 | (-8,-14,-16,-14,-8,-2,0,6) | (280,266,216,130,24,-90,-184,-250) |
| 4 | (16,4,-8,-24,-32,-36,-32,-24) | (-376,-444,-444,-372,-248,-84,92,252) |
| 5 | (24,8,-4,-12,-24,-28,-36,-32) | (232,380,476,496,440,320,148,-44) |

For m=2 the exact discrepancy is **(84,80,64,40,4,-32,-64,-80)** in Q[z]/(z^8+1), definitely nonzero. Both original and corrected m=2 coefficients are individually nonzero at every primitive 16th root (cyclotomic irreducibility). The original m=2 claim of a nonzero 16th-root contribution survives, but its published coefficient is incorrect. The previous supposedly independent DP validated the same union-cardinality substitution, not the true intersections.

## Effect on claims and next frontier

The prior threshold generating function G(t,z)/(1-t^16), its listed m>=2 coefficient table and the **proof of the all-m four-way minimal-period classification at remainder O_m(N^4)** must be treated as requiring correction. This audit does **not** claim the eventual period formula is false, only that its advertised proof and numerical coefficients do not establish it. The m=1 result is unaffected by this particular error. Primitive-17 claims whose maximal pole comes only from the single event S0 are not automatically affected, but all shared-intersection arguments must be audited individually.

The corrected data above are **finite exact results for m=1..5**, not an all-threshold theorem. Next: compute an exact threshold generating function using the genuine conjunctions of event-specific bounds, classify primitive-16 zeros for all m, and audit affected lower-root proofs. At the next Laurent order include possible five-free-multiple terms from S4. Maintain original authorship and frozen scientific inputs. Do not equate this scalar Fourier observer with a native X6 physical state without a separately proved typed bridge. This is precisely an overlap-residual fidelity problem: joint constraints cannot be discarded before proving a sufficient quotient.

Reproduce with companion VERIFY_INTERSECTION.py and compare to exact RESULT.json. No external packages. All underlying R5 commits remain unmodified; this is an independent corrective research artifact.
