# T6 p=17 q14 split(7,7): sharp joint q0 mass and multiplicity ceiling

Date: 2026-11-22. Research state: **AUTHOR_PORTABLE / EXACT_INTEGER_VERIFIED / UNREVIEWED / NOT_ADMITTED / NO_NATIVE_TASK_PROGRESS**. This is a strictly new *budget-only corollary* of the already frozen 2026-11-16 q14 pre-affine side roster. No q0 congruence feasibility, affine search, Result, review, or global T6 threshold claim is made.

## Source and ownership boundary

Task: RS-T6-SHAPE-MOMENT-GLOBAL-LOWER-BOUND, publication TP2-34B106D2512A298C9647. Exact prior Source: \`enterprise-math@9ef728a7107362eb0d4b1719ed98d00b1678357c:research_artifacts/mcp/RS-T6-SHAPE-MOMENT-GLOBAL-LOWER-BOUND/MCP-c618a61189764f23846a391a08518a1a/150b2baf7e93fb09d7e7/_checkpoint.json\`, with the 23,894-byte canonical side roster and independent reproducer in the same directory. This prior owner already produced **60 admissible atoms, 1,907 side rosters, 809,566 unordered disjoint-support vertical pairs**; these are reused, not new results here. P000 and joint/composite observer preservation retained. Researcher: EM-X6-FB6990, SID MCP-082892eb480e45dea6d4b9fcc0491034. Formal T6 CLAIM/OPEN unverified while this portable bound was derived. No role-bound work is implied by preserving it.

## Exact hypotheses

One-power maximal-p17 vertical atom (q,r): 1<=q<=7, 1<=r<=16, smooth cofactor a=17q+r (all prime factors <=17), mass w=289q+17r-1. Each signed vertical side has sum q=7, mass <=2331. Same-side repeated atoms retained; opposite equal named atoms cancel. Overall sign exchange is quotiented once. q0 atoms, if later present, have j=1,...,16 and mass 17j-1; opposite equal named q0 atoms must not coexist after cancellation. Only nonnegative integer multiplicities and budget constraints are considered here.

For a side R with n vertical atom occurrences, the exact identity is

    M(R) = 2023 + 17 * sum_{(q,r) in R} r - n.

### Proposition 1: unique minimum joint vertical cost

The side R0={(7,1)} is admissible because a=120=2^3*3*5, and M(R0)=2039; R1={(7,2)} is admissible because a=121=11^2, and M(R1)=2056.

For n>=3, M>=2023+16n>=2071. For n=2, the putative cost 2055 would require r=r'=1 and q partition (1,6), (2,5), or (3,4). In each case one cofactor is 103, 86=2*43, or 69=3*23 respectively, so the pair is not admissible; every admissible two-atom side costs >=2072. For n=1, q=7 and M=2023+17r-1, so R0 is the unique minimum and R1 the unique second minimum.

Opposite-disjoint signed sides cannot both contain R0's atom. Thus:

    min_{admissible sign-disjoint vertical pairs} [M(R+)+M(R-)]
      = 2039+2056 = 4095,

with unique unordered minimizer {R0,R1}. Consequently the sum of the two *remaining* q0 mass budgets is bounded sharply:

    B0_plus + B0_minus <= 2*2331-4095 = 567.

Equality holds as a cost-budget statement at {R0,R1}; it is not an affine/mixed-congruence survivor certificate.

### Proposition 2: sharp budget-only q0 multiplicity ceiling

Let N0 be the total number of q0 atom occurrences on both sides after signed cancellation, *ignoring the six mixed congruences*. The cheapest q0 atom is j=1 of mass 16; every other j has mass >=33. If both q0 sides are nonempty, only one side can contain j=1, since opposite equal atom supports must be disjoint. The other side's occurrences each cost >=33.

Every vertical side has remaining q0 budget at most 292. The only side realizing 292 is R0. If one vertical side equals R0, its opposite disjoint vertical side has remaining budget at most 275 (R1); otherwise both sides have budgets at most 275. Hence

    N0 <= max(floor(292/16)+floor(275/33),
              floor(292/33)+floor(275/16),
              floor(275/16)+floor(275/33), floor(292/16))
       = max(26,25,25,18) = 26.

The bound is **sharp in the budget-only relaxation**: choose R+=R0, R-=R1; put 18 copies of q0 atom j=1 on the first side (mass 288<=292) and 8 copies of q0 atom j=2 on the second (mass 264<=275). There are exactly 26 occurrences, with disjoint signed supports. This extremal budget configuration is unique up to simultaneous sign exchange: attaining 26 forces the 18 j1 side, therefore R0; it forces the other side to admit 8 j2, therefore R1; neither side has enough budget for heavier alternatives.

**Scope guard:** This does not assert any q0 assignment solves T1,...,T6 mixed congruences; it is an exact sharp resource upper bound for a budget-only relaxation. Do not infer q14 EMPTY, an affine feasibility classification, H0 closure, or T6=2332.

## Computational verification and provenance

A fresh pure-integer Python enumeration over the same complete cofactor rule, q partitions, same-side repetitions, both side budgets and named support disjointness independently checked:

- 60 admissible named atoms; 1,907 admissible vertical side rosters;
- 809,566 unordered opposite-disjoint vertical pairs;
- unique minimum joint vertical mass 4,095 and residual mass sum maximum 567;
- sharp maximum budget-only q0 occurrence count 26, attained for exactly one unordered vertical pair.

The checked core (integer-only, no affine search) is: recursively enumerate nondecreasing admissible atom indices with sum q=7 and sum mass<=2331; form each support bitmask; for each pair i<j with (mask_i & mask_j)==0, update min(mass_i+mass_j) and max over the two assignments of 16/33 cheapest disjoint q0 weights. The locally executed independent script and full cost histogram have SHA256 provenance in the separately preserved author handoff. They are not misrepresented as a native Source execution.

## Exact continuation

Preserve the existing native q14 roster/checkpoint, q1-q4 accepted boundaries and original ownership. Consume the pending original native prepare request \`onhour-20261122-1758-t6-selected-own-prepare-v1\` by its ID, do not replay or infer a CLAIM. Once the actor's *own* winning Task claim/open and source-authority are verified, submit this scoped corollary as a scientific contribution and obtain a genuine nonauthor design/math review against the original q14 plan SHA256 b866fa935b62df35c6be65560c5aeebb0f64b1e958c84c34e469d5faf8735d24. Continue the existing task's original q0 affine work only if its actual resource and review prerequisites are satisfied.
