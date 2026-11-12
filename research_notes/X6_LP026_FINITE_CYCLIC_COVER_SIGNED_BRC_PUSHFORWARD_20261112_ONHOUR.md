# X6 / LP026–LP019 — signed BRC pushforward through finite cyclic common-depth covers

Date: 2026-11-12; lane: TASK_RESEARCH on-hour; parent Task RS-X6-LEGACY-PLANE-RECONCILIATION; immutable publication TP2-B4A441B23DA3159232C2. Status: AUTHOR_PROVED / INDEPENDENT EXACT FINITE REGRESSION EXECUTED / NONBLIND / UNREVIEWED / NOT_ADMITTED. This is scientific/source evidence, not a renewed Result, a new TASK claim/open, a native semantic checkpoint or an independent review.

## 1. Inputs and exact current consumer

Scientific definitions stay pinned to centered signed X6 source awdawmip/enterprise-math@59538f585d037d09ef687b28715c4bc1a3f9fe03 and historical corpus @fd2bcff10ca6e147348b6c1236027fc0d2877df3. Current mutable code is a separately observed interface, not a rewrite of either frozen source.

Actual GitHub main consumer inputs observed at Source head f4410c2a93ee1bb44c8dab965aa748f4b17c983b:

- experiments/x6_native_coordinate_completion_v7_20260905/x6_coordinate.py, Git blob ef66285d8ae81569cbbd3195b3e38daae37944ef: derived quotient Coord6 is a min-zero representative of Z^6 / Z*1; its brc_endpoint_multiplicity (lines 191–204) is explicitly positive-only, not signed X6 BRC.
- experiments/x6_native_coordinate_completion_v7_20260905/x6_cover.py, Git blob 3f7d9e62a4dd66e7888a69ff87276b283c891aac: CoverState holds (Coord6, depth, modulus), with modulus 0 retaining signed integer depth and positive modulus reducing depth modulo m. Step (lines 61–70) works through an integer lift and recanonicalization.
- experiments/x6_signed_native_spatial_v16_20260905/signed_brc.py, Git blob 300a96e3dc24bf6fff73743037a0347a8bc83176: endpoint_multiplicity (lines 42–53) supplies the exact signed native length-N path multiplicity via cancellation-pair compositions.
- experiments/x6_native_coordinate_completion_v7_20260905/check_x6_coordinate.py, Git blob e72e12d2578b544a8ed10bb55a41cea1d28b60b1: lines 91–99 treat the reverse-axis norm 5 as a derived quotient-coordinate readout, whereas the centered signed native displacement -e_i has native square norm 1.
- experiments/x6_native_coordinate_completion_v7_20260905/check_x6_cover.py, Git blob ba0a4fe90234186f12386b671b4d1cfef9b39648: confirms the historical cover-classification design, independently of the new signed BRC fiber question.

P000 V5 and the active HEARTBEAT_WORLD_NATIVE_X6_TIME contract use six signed native spatial axes and no native plane. A chosen Cell anchor supplies local raw displacement coordinates; the quotient is declared as a derived observer. The joint-observer preservation constraint requires a typed certificate before erasing an input direction.

## 2. Theorem: exact signed BRC fiber pushforward for every cyclic depth quotient

Fix six signed primitive generators ±e_i. For z in Z^6 put h(z)=min_i z_i, r(z)=z-h(z)*1. Thus r is nonnegative and min(r)=0; (r,h) is an exact, lossless signed displacement encoding.

For modulus m=0 retain h as an integer. For m>=1 retain only [h] in Z/mZ; denote the resulting observer by pi_m(z). Under addition, this observer is exactly the quotient Z^6/(mZ*1) for m>=1; pi_0 is the lossless native chart encoding.

Let B_N(z) be the number of signed ordered native words of length N with displacement z. Equivalently, with a_i=max(z_i,0), b_i=max(-z_i,0), and K=(N-sum_i|z_i|)/2,

    B_N(z) = sum_{k_1+...+k_6=K, k_i>=0}
               N! / product_i[(a_i+k_i)!(b_i+k_i)!],

with value 0 unless N>=sum|z_i| and N-sum|z_i| is even. This uses the existing signed-BRC kernel; it counts nonnegative path multiplicities, not phase or amplitude cancellations.

For m=0 and cover key (r,h), the exact number of length-N words is B_N(r+h*1). For any m>=1 and cover key (r,[h]_m), the exact count is

    C_{N,m}(r,[h]_m) = sum_{t in Z: t == h (mod m)} B_N(r+t*1).               (1)

The sum is finite, since a contributing endpoint satisfies |r_i+t|<=N for every i (in particular |t|<=N because min(r)=0). Equation (1) is valid for all integers N>=0, every modulus m>=1 and all keys (r,[h]_m). The same pushforward statement holds for any path-word weight depending multiplicatively on the signed letters and taking values in a commutative coefficient ring; in particular it holds for the exact positive rational signed weights already used by endpoint_weight.

Proof. The map z -> (r,h) is bijective, by reconstructing z=r+h*1. For m>=1, two integer displacements have the same observer precisely when their difference is km*1 for some k in Z. All length-N ordered words are disjointly partitioned by their true native displacement z. Group these disjoint fibers by pi_m(z). Each native displacement contributes exactly B_N(z) words by the multinomial choice of positive and negative occurrences; summing over the explicitly described quotient fiber yields (1). Invariance of pi_m under common shifts by m*1 also makes the original ±e_i additions descend to each finite cover. For m=0 every native fiber is a singleton. QED.

## 3. Observer and future-operation boundary (exact)

For all m>=1, pi_m identifies z=0 with z=m*1. The native P000 chart square norm G(z)=sum z_i^2 separates them, 0 versus 6m^2, and the signed shortest-path distance separates them, 0 versus 6m. Hence neither G nor the native shortest distance factors through this finite-depth cover, even though the signed unit-step transition does.

Conversely, all observables defined solely from (r,[h]_m), all transition words and their projected BRC counts do descend. This is an exact, scope-typed certificate: a cyclic-depth cover is safe for the declared quotient dynamics and projected BRC, but an endpoint-specific native norm or exact Cell identity requires preserving or reconstructing the full h. Positivity of BRC does not turn this projection into signed amplitude cancellation.

## 4. Executed exact independent certificate

Published checker: research_checks/X6_LP026_CYCLIC_DEPTH_BRC_FIBERS_20261112_ONHOUR.py (Git blob 4aa0e4fe8dedb8468f0e3da03273b4b9ecfd8b35, immutable commit d25009d87b8f6d5b34d24f60d9e18727e90a5c24).

The checker was executed as an independent self-contained Python script with exact integers. It compares three distinct computations: signed 12-generator native path dynamic programming, direct projected cover-step dynamic programming, and the closed-form BRC fiber sum (1). For m=0,1,2,3,4,5 and all lengths N=0..6, 59,267 cover-state/length cases passed. The full native path distributions were also checked against the factorial/cancellation formula. No floating-point arithmetic is involved.

For the zero residual at N=6 the exact table is:

| Cover and depth label | Signed length-6 BRC |
| --- | ---: |
| m=0, h=0 (true native zero) | 19,920 |
| m=0, h=+1 | 720 |
| m=0, h=-1 | 720 |
| m=1, class 0 | 21,360 |
| m=2, class 0 | 19,920 |
| m=2, class 1 | 1,440 |
| m=3, class 0 | 19,920 |
| m=3, class 1 | 720 |
| m=3, class 2 | 720 |

The checker includes an optional current-source import branch which was not executed in the isolated no-checkout environment. Actual current-source bytes and function calls were inspected independently via the authorized GitHub connector; current source importing remains a specific pending integration check, not a PASS. The previously completed LP026 signed Laurent source-import check is a separate validated result, and has not been rerun as this result.

## 5. LP decisions and exact continuation

LP026: KEEP the already tested positive six-generator relative_endpoint_multiplicity and positive Coord6 brc_endpoint_multiplicity within their contract. REUSE/EXTEND the signed native endpoint_multiplicity and (1) when the consumer asks for a quotient over twelve signed primitive generators. A higher-level caller must state which depth modulus or native endpoint it observes.

LP019: the derived quotient class and native signed endpoint are different carriers. A positive six-step diagonal return to min-zero class is a genuine quotient return while native displacement is +1 on each axis. Counts 720 (fixed positive six-step diagonal endpoint), 19,920 (signed true zero at N=6), and 21,360 (signed modulo-one zero-relative class) must remain separate.

LP011/LP028: the historical source attribution and present consumer coverage obligations remain unchanged; this unit does not manufacture an original bad caller. The existing 28-row matrix is the parent dependency.

Highest remaining task: execute the imported current-source CoverState.step/signed_brc interoperability branch in a faithful source layout; then trace any actual modern caller that promotes a derived Coord6.norm_squared or cover return into native signed G or Cell return. On confirmed misuse, add only the corresponding typed adapter/guard. Exact original LP011 and LP019 historical caller search remains open. Preserve DRIVER REQUEST_REVISION, original owner and task publication.

## 6. Execution/source provenance and control status

Math author context: same on-hour TASK_RESEARCH lane as existing RA-629C868A22A736334628BEFA. Historical researcher and the previous claim are provenance, not renewed authentication. Research lane logical label: chatgpt-research-onhour-enterprise-math-20260923; maintenance conversation chatgpt-hourly-enterprise-math-20260921 is not used. Existing continuation request onhour-20261112-1604-x6-current-continuation was read as SUCCEEDED, without a current winning X6 CLAIM/open. A new read-only task request onhour-20261112-1700-x6-task-read is still RUNNING at the last observed status, and will be reconciled using its original ID. Support issue #2141 tracks typed continuation artifacts. No schedule, notification, P000, existing frozen Result or live Source implementation changed.
