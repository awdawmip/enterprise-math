# T6 sharpened exact-v₂(d)=5 three-atom rigidity: mass ≥1949 on both sides

Date: 2026-11-23, Asia/Taipei. Original continuing Driver scientific contributor: `EM-DVR-DEBB5E`. This theorem strictly extends (does not delete) the earlier [mass-2011 result](https://github.com/awdawmip/enterprise-math/blob/2b21aec25abc7ddc130709387a346aa5894d93e2/research_notes/driver/2026-11-23_t6_p2_fifth_three_atom_highmass_rigidity.md) and preserves the origins of all prerequisite theorems. This file is a mathematical research proof, not Native Review/Result admission.

## Theorem

Let `A,B` be multisets of positive integer exponents, each with `sum(e)<=2331`. For `d=e+1` put `H_k(X)=sum (e/(e+1))^k` and assume `H_k(A)=H_k(B)` for `k=0,...,6`. Assume each side contains **exactly three** denominators counted with multiplicity satisfying `v₂(d)=5`. Suppose the sum of their three exponents on **each side** is at least **1949** (equivalently their three odd quotients `j=d/32` satisfy `j_1+j_2+j_3>=61`).

**Then the multisets of those three exact-`v₂(d)=5` denominators are identical.**

The theorem depends on previously published exact high-valuation cancellations: [all `v₂(d)>=6`](https://github.com/awdawmip/enterprise-math/blob/c577f07bcd434340c500b91e4b67a5402c82c514/research_notes/driver/2026-11-23_t6_p2_sixth_universal_cancellation_three_tier.md) and [all `81|d`](https://github.com/awdawmip/enterprise-math/blob/38bac283aec3445f271bdf728ed93aed9ea6ba30/research_notes/driver/2026-11-23_t6_universal_p3_fourth_six_moments.md). Both retain their existing proof scope and original contributors.

## 2-adic reduction: precisely one last profile pair

Equal `H_0,...,H_6` give equal reciprocal moments `S_k=sum d^{-k}` by binomial inversion. After cancelling previously matched denominators with `v₂(d)>=6`, signed exact-valuation components obey

`D_{5,k}+2^k D_{4,k}+2^(2k) D_{3,k}=0 (mod 2^(3k))`, `k=1,...,6`,

with `D_{v,k}=sum_{j odd}(m_A(2^v j)-m_B(2^v j))*j^{-k}`. In particular the `v₂=4` correction must satisfy `V_B-V_A=D_{5,k}/2^k (mod 2^k)`; full 2-adic residual group tests must use this sign and retain each side's independent real exponent budget.

All legal three-atom profiles `(j_1<=j_2<=j_3)` number **1,461**. The strengthened layer-mass bound leaves **596** admissible profiles. Complete finite integer enumeration yields:

| Necessary filter | Count |
| --- | ---: |
| Distinct high-mass profile pairs with identical six first-tier signatures | 5,095 |
| Extra `k=4,6` cross-tier condition | 539 |
| `v₂=4` full 2,048-element correction group membership | 220 |
| Exact per-side residual mass budgets admit the correction | 127 |
| Exact `v₂=4` option pairs satisfying all second-tier divisions | 14,251 |
| Their required `v₂=3` signature belongs to full 2,048-element group | **7** |

These 7 are option pairs (not 7 distinct three-atom candidates). **All 7 originate from exactly one distinct original three-atom profile pair:**

`(j_1,j_2,j_3)_A=(3,3,55)` versus `(j_1,j_2,j_3)_B=(7,27,27)`.

Both have quotient sum 61, hence exact-`v₂=5` layer mass `32*61-3=1949` and the **same residual exponent budget 382** on each side. They survived only an *unrestricted* `v₂=3` 2-adic group test, not the complete rational moment equations.

## Independent 3-adic obstruction excludes the last pair

Use the already proven universal cancellation of all `3^4=81`-divisible denominators. Multiply the **full** reciprocal moment difference `S_k(A)-S_k(B)=0` by `3^{3k}` and reduce modulo `3^k`. Lower exact 3-adic valuations vanish, while higher valuations have been cancelled. The necessary remaining exact-`v_3(d)=3` condition is

`sum_{3∤u} (m_A(27u)-m_B(27u))*u^{-k}=0 (mod 3^k)`, `k=1,...,6`.

For the last pair, the fixed A denominators are `96,96,1760` and B denominators are `224,864,864`. Exactly the two B denominators `864=27*32` have valuation `v_3(d)=3`; none of A's fixed denominators does. The 3-adic signature difference required of the remaining budgeted atoms is therefore

`(2*32^{-k} mod 3^k)_{k=1}^6=(1,8,16,68,73,344)`.

Every residual exact-`v_3=3` denominator is `27u`, `3∤u`, `27u-1<=382`, hence `1<=u<=14`. The actual per-atom exponent costs are `27u-1`. Enumerate **every** nonnegative multiset of these denominators within each side's independent residual mass 382; retain the cheapest witness for each six-coordinate signature modulo `3^k`. This produces **246** distinct feasible signature types per side.

If the last pair could satisfy the full six moments, one residual A signature would equal one residual B signature shifted by `(1,8,16,68,73,344)`. Exact set intersection gives **zero**. Since the enumeration includes all remaining admissible `v_3=3` profiles, this excludes the last pair, independent of the previously used 2-adic necessary filter.

Thus the high-mass three-atom profiles are identical as claimed. The published [integer-only complete checker](https://github.com/awdawmip/enterprise-math/blob/2387fc970014f1c82b93f7bd591beb092d245248/research_checks/T6_P2_V5_THREE_ATOM_MASS1949_P3CUBE_EXACT_20261123.py) computes the complete 596-profile sieve, both 2-adic signature groups, all 14,251 residual option pairs, and the 246-versus-246 3-adic disjointness. It uses exact modular inverses, finite recursions and no numerical approximation. The local independently executed equivalent Python calculation returned the stage counts and final `PASS`.

## Boundary and next frontier

The result is **not** universal `v₂=5` multiset cancellation: this proof assumes exactly 3 atoms **on each side** and lower-bounds both three-atom layer masses. Lower-mass triples, four-or-more atoms, and the overall T6=2332 mother objective remain open. The previously proven universal **number-of-atoms** equality at `v₂=5` is unchanged.

Contribution: Driver `EM-DVR-DEBB5E` for this finite extension, prior authors retained for existing higher-valuation inputs. New scientific artifact published/readback in the project; formal Source Activity linkage and Native Review/Result still separately require current authenticated authority and actual admission. No new CLAIM, task completion or Foundation claim.
