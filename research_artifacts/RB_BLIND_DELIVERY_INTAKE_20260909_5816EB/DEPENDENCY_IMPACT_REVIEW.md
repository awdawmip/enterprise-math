# RB blind-source intake: precise dependency impact

Status: **source-exposed Driver review; incomplete historical returns preserved**. Driver `EM-DVR-5816EB` did not author the old returns. The auxiliary even-divisor counterexample below was constructed in this review and has now received an independent [qualified paper pass](https://github.com/awdawmip/enterprise-math/blob/61dedaa3528fc32757e1a7c8636b5167da2e959b/research_artifacts/RB_EVEN_DIVISOR_NONAUTHOR_CHECK_20260909_82DF76/REPORT.md) from researcher EM-DIRECT-82DF76. This Driver adopts only that auxiliary-classification consequence, not a verdict on the six-block map-exclusion theorem. No global six-block map or nonexistence result is asserted.

## 1. Two different issues must remain separate

The later A61/6D statements omit a possible local branch already retained by the earliest 7C42A1 source. The original [c73816d3 raw freeze](https://github.com/awdawmip/enterprise-math/blob/c73816d3552b4247861e12e476101e94a4a2ce5a/research_artifacts/RB_ENTERPRISE_DEGREE6_CM24_BLIND_REPLICATION/raw_freeze_reduction.json), fields `payload.exact_reduction.critical_profile` and `payload.exact_reduction.special_fiber_profile`, explicitly states `e_X=2` at an ordinary value, `e_X=4` at a special value, and `(9+s)+(3-s)=12`. Recovering that distinction is reuse of an existing correct frontier, not a new theorem.

A separate dependency audit then finds an incomplete auxiliary Riemann–Roch classification inside the same 7C source's `payload.exact_reduction.six_block_obstruction`. This affects whether the two retained block patterns exhaust the whole search. It does not automatically invalidate conditional counts inside those patterns or the later concrete map certificate.

## 2. Local degrees with the special-value coordinate retained

Let `pi:D→C` be the double cover, `f:D→E` a map with pulled-back differential proportional to phi, and `x:E→P1` the target double cover. Local degrees satisfy

`e_X * e_pi = e_x * e_f`.

At a marked source branch point B, `e_pi=2`, `e_f=1`, and the centered image is target two-torsion, so `e_X=1`. At one of the three Q points `t=-k`, the source cover is unramified and the two lifts have `e_f=2`. Thus a Q has `e_X=2` at an ordinary target value and `e_X=4` at a special target value. Other non-B points over a special value have degree two.

For special fiber v, retain `m_v` marked B points, `r_v` Q points of multiplicity four, and `d_v` ordinary double points. Then

`m_v + 4 r_v + 2 d_v = 6`, `sum m_v=6`, `sum r_v=s`, `sum d_v=9-2s`.

The special ramification is `9+s`; the remaining ordinary Q contribute `3-s`. Total ramification is 12 for every `0≤s≤3`. Therefore total degree/Hurwitz data alone cannot select `s=0`. This describes necessary local types, not their simultaneous global realizability.

The new finite audit reuses the unchanged BRC exact-DIV implementation and T6 `refines` predicate. For each of three occupancy vectors it tests only the 125 placements of three **labelled** Q points among an ordinary label and the four special labels. It retains the target label, multiplicity, and signed pole valuation. The admissible local placement histograms by s are `(1,9,18,6)` for `6+0+0+0` and `4+2+0+0`, and `(1,12,36,24)` for `2+2+2+0`. These numbers are not maps, irreducible components, descent classes, or replacements for the old assignment counts. The original 180/360 search was not rerun.

## 3. Exact counterexample to the auxiliary even-divisor classification

On `C:t²=R³-3R`, let `T0=(0,0)` and

`U = R³ + 2 R t + R² - 3`.

The unchanged task-local integer polynomial ring verifies

`R U = (R²+t)²`.

The same check rejects `U+1`, with residual `-R`. The program checks these polynomial identities; the following divisor implications are paper arguments.

As a function-field identity, `U=R(R+t/R)²`. Since `div(R)=2[T0]-2[O]`, U has an even divisor. It is a polynomial in R,t and is regular at every finite point; its unique leading pole order at O is six, from `R³`, while the remaining terms have orders at most five. Its square class is `[R]`, which is geometrically nontrivial: `T0-O` is a nonzero two-torsion class, and a principal divisor `T0-O` would yield a degree-one function on a genus-one curve.

U contains the nonzero t coefficient `2R`. Consequently it is neither a square from `L(3O)` nor any `(R-r)` times a square from `L(2O)=<1,R>`. It also meets the finite B-point nonvanishing needed for the cited pencil setting: values are `-3` at T0, `±3 sqrt(3)` at the other finite two-torsion points, and `-7-4t` at `R=-2,t=±i sqrt(2)`, all nonzero.

The lost coordinate is an allowed compensating pole of the half-section at T0: `R+t/R` belongs to `L(2O+T0)`, not `L(2O)`. Its pole is cancelled by the zero of R. Requiring the product U to be regular does not require each factor to be regular.

The complete candidate space for a nonzero two-torsion point `T_r=(r,0)` is

`(R-r) * L(2O+T_r)²`, with `L(2O+T_r)=<1,R,t/(R-r)>`,

alongside `L(3O)²` for the trivial class. The degree-three basis is the specialization `S=T_r` of the already published [empty-fiber paper](https://github.com/awdawmip/enterprise-math/blob/108ac80d4af9a1ebe19cc613aaccb7402564100e/research_artifacts/RB_BLIND_BRANCH_PATTERN_COMPLETION_20260908/empty_fiber_obstruction.md), section 5. No new general tool family is required.

**Limit:** U alone is not a triple `G,G-F,G-lambda F`, does not satisfy the full map ODE by this calculation, and does not prove that a six-block map exists for the frozen lambda. It disproves the stated auxiliary exhaustive classification and removes that argument as a sufficient proof of six-block exclusion. The exclusion theorem may still admit a repaired proof.

## 4. Dependency impact table

| Source / claim | Actual dependency and check | Impact |
| --- | --- | --- |
| PR1395 A61 return §5, and the additional forced fiber restriction in §§8/12 | Its `9+3` argument omits the overlap case where a Q is special and has degree four. Its checker verifies constants, pole orders and the master identity interface, not the missing inference | **Revision required:** the prescribed ordinary-Q stratum is not an exhaustive local classification. Keep the unchanged master identity and L6/L7 presentation as separately reviewable material |
| PR1397 6D descended-certificate and final “nine double points plus three simple Q” wording | The wording describes the generic `s=0` case. The fixed-field square-class statement also drops a possible non-square target-twist constant | **Qualification required:** retain special Q and a nonzero constant twist. Keep the incomplete/no-map/no-period verdict and distinguish the narrow trial-route claims |
| Original7C raw `critical_profile`, `special_fiber_profile`, and corrected Hurwitz check | These explicitly retain degrees2/4 and the s-coordinate before either later return | **Unaffected and reusable.** This is the correct predecessor of the local correction |
| Original7C `six_block_obstruction` | Its “every even-divisor element of L6” classification omits `L(2O+T)` half-sections. Its checker verifies exceptional j values but does not establish that classification | **Separate proof gap:** the cited argument does not yet exclude `6+0+0+0`. U is an exact auxiliary-classification counterexample, not a six-block map |
| Archived branch-assignment counts180/360 | [Assignment paper](https://github.com/awdawmip/enterprise-math/blob/108ac80d4af9a1ebe19cc613aaccb7402564100e/research_artifacts/RB_BLIND_BRANCH_PATTERN_COMPLETION_20260908/branch_assignment_classification.md) counts B-label partitions inside `4+2` and `2+2+2`; it explicitly cites the six-block exclusion rather than re-proving it | Counts remain correct **inside those two patterns**. Their interpretation as a complete universe requires a repaired six-block exclusion |
| Fixed-target V4 candidates45/90; no source-sign quotient for fixed k | The group acts on labelled B assignments. It does not erase Q multiplicities; the source-sign restriction uses the distinct zero divisors t=±k | **Unchanged within the stated patterns.** Do not add the new labelled local-type counts to these orbit counts |
| Archived square-class/RR equations,16 compatible twists, dimensions1/2/3 | [RR paper](https://github.com/awdawmip/enterprise-math/blob/108ac80d4af9a1ebe19cc613aaccb7402564100e/research_artifacts/RB_BLIND_BRANCH_PATTERN_COMPLETION_20260908/squareclass_rr_reduction.md) uses effective divisors E_a and D_infinity, which may have multiplicities; a special Q is a double point of that half-divisor. It retains nonzero constants and geometric-versus-arithmetic descent | **Unaffected as a parameterization of the two named patterns.** It must not be advertised as covering an unexamined six-point block |
| RR paper §6, pole-class3O exclusion | The paper explicitly handles ordinary values, special values, zeros and poles. Degree-three g rules out local degree four for g where squaring is unramified | **Unaffected by the ordinary-Q omission**; its local-degree argument already includes the missing case |
| Geometrically square empty-fiber exclusion of180 components | Empty-fiber paper §§2/4/5 explicitly handles special Q, uses the degree-three bound, includes the correct basis `L(2O+S)`, and proves the determinant nonzero for its ten pole classes | **Preserved inside4+2:** no dependence on A61's generic-only assertion or the invalid L2O auxiliary classification |
| Remaining1980=540+1440 | This is the remaining parameter-component count of the analyzed `4+2` and `2+2+2` strata after the180 exclusion | **Retain with scope:**1980 within those two strata; global exhaustiveness is pending six-block proof repair. Do not invent a larger map/component count |
| Later source-exposed explicit certificate, RR-F79FA3D36EF85CC4C6CE | Its [proof](https://github.com/awdawmip/enterprise-math/blob/0f4fc206e6c3a950cdd7c7587a455bfc829d8a33/research_artifacts/RB_CM24_SOURCE_EXPOSED_EXACT_MAP_20260909/exact_map_proof.md) §5 gives the actual full reduced fibers, and §§6–7 give explicit square classes/placement for its4+2 assignment | **Preserved at its independent exact scope.** Existence, degrees, full ODE, target, basepoint and unsquared differential do not depend on global exclusion of all six-block maps |

The archived branch-pattern task's two mathematical whitelist inputs were the original7C raw freeze and checker, not the later A61/6D returns. Therefore the local-degree mistake does not propagate to it by chronology or topic similarity. The six-block dependency does propagate because it is explicitly cited.

## 5. Minimum next mathematical unit

The independent check of U and the corrected half-section space is complete at the qualified scope above. Next repair or explicitly limit the six-block exclusion by considering the complete four-type even-divisor spaces in the pencil `G,G-F,G-lambda F`, preserving the frozen lambda, exact pole/nonvanishing conditions, and the separate ODE gate. No rerun of the two-pattern180/360 enumeration or the already accepted concrete map is required. A locally feasible branch type or a compatible even-divisor member is not a global correspondence.

This review does not rewrite an old return, claim, Result or Driver disposition. It supplies source-pinned qualifications and a new unresolved dependency for the ordinary review process.
