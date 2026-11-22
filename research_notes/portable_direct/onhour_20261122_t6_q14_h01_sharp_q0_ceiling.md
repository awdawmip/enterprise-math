# T6 maximal-p17, q14 split(7,7): sharp H0 + H1 q0 multiplicity bound

Date: 2026-11-22 (Hong Kong). Task: RS-T6-SHAPE-MOMENT-GLOBAL-LOWER-BOUND. Original TASK_RESEARCH lane: chatgpt-research-onhour-enterprise-math-20260923; original Researcher EM-X6-FB6990 / session MCP-082892eb480e45dea6d4b9fcc0491034. **AUTHOR_EXACT_FINITE_VERIFIED / UNREVIEWED / NOT_ADMITTED / NATIVE_CLAIM_PENDING**.

## Actual fixed input and consumed prior work

Maximal prime p=17, vertical order q=14 split (7,7); same frozen task budget 2331 **per sign**, exact composite cofactor and multiplicities. Each vertical atom (q,r) has denominator 17(17q+r), q>=1, 1<=r<=16, 17q+r 17-smooth, mass 289q+17r-1; each sign has sum q=7. The q0 atoms have denominator 17j, j=1,...,16, mass 17j-1. Opposite signed copies of the **same named atom** cannot coexist in cancellation-normal form; same-sign repetition is allowed.

Consume the previous Source owner q14 full roster result (60 named atoms, 1,907 single-side rosters, 809,566 unordered disjoint vertical pairs): enterprise-math@9ef728a7107362eb0d4b1719ed98d00b1678357c, research_artifacts/mcp/RS-T6-SHAPE-MOMENT-GLOBAL-LOWER-BOUND/MCP-c618a61189764f23846a391a08518a1a/150b2baf7e93fb09d7e7/_checkpoint.json. Also consume this lane's previous sharp budget-only q0 bound 26 and sharp H0 bound 17, at enterprise-math@27c5aa2456fd2ebd3bddc0fa2fa6465d045e0fe3/research_notes/portable_direct/onhour_20261122_t6_q14_h0_joint_multiplicity_ceiling.md. Earlier work is not reassigned to this author.

## New theorem

For any two such supported signed multisets satisfying *both* H0 equality and H1 equality, with both exact side masses <=2331,

**total number of q0 occurrences, counted with same-side multiplicities, is at most 11; this bound is sharp even after exact H0 and H1 constraints.**

H0 equals the number of denominator occurrences, and H1 for denominator a is (1-1/a). Consequently, under H0 equality, H1 equality is equivalent to equality of reciprocal sums. After multiplying by 17 this is precisely

    sum_{(q,r) vertical on +} 1/(17q+r) + sum_{j q0 on +} 1/j
      = sum_{(q,r) vertical on -} 1/(17q+r) + sum_{j q0 on -} 1/j.

All terms here are **exact rationals**. This is a genuine H1 equation, not an optional first-digit modular proxy.

### Finite proof and complete search coverage

The accompanying self-contained Python checker enumerates each named vertical atom by trial-division smoothness, then every nondecreasing multiset of such atoms with total q=7 and mass <=2331: exactly 60 atoms and 1,907 side rosters, with 809,566 unordered disjoint pairs as a check of the predecessor's scoped result. The cheapest vertical side mass is 2039. Thus *every* q0 side is a multiset of j=1,...,16 of q0 mass <=2331-2039=292; the recursive exhaustive enumeration gives exactly 1,223 such q0 multisets.

By overall sign symmetry, order the **vertical occurrence counts** n+ <= n-, including equality (retain both ordered q0 choices). For each n+ and n- from 1..7, every q0 pair is checked under exact side budget, disjoint named q0 supports and H0 equation n+ + k+ = n- + k-. These filters leave 167,928 q0 pairs out of 1,944,619 count-compatible pairs checked by the loop. For each such pair the checker groups all available vertical rosters by **exact Fraction reciprocal sum** and tests the unique rational complement needed for H1, retaining only pairs with disjoint vertical named support. Every test uses integer and Fraction arithmetic, without tolerance, sampling or floats.

Exactly 333 signed solutions remain with n+<=n- (counting their distinct named multisets). The histogram of total q0 occurrences is:

    0:74, 1:3, 2:44, 3:33, 4:58, 5:44, 6:36,
    7:16, 8:13, 9:5, 10:4, 11:3.

No solution has 12 or more q0 occurrences. Completeness follows from the disjoint union of all possible vertical and q0 multisets, exact rational equations and sign ordering; these are not heuristics. The checker asserts the 60/1907/809566 and 1223/333/11 totals and writes a certificate. All enumerated identities, multiplicities, side budgets and sign supports remain intact.

### Exact attaining witness

Positive vertical: [(7,1)], with denominator 17*120 and mass 2039.
Positive q0: j=2 repeated six times and j=4 once: mass 6*33+67=265. Positive total mass 2304; H0=1+7=8.

Negative vertical: [(1,4),(2,1),(2,1),(2,1)], with cofactors 21,35,35,35 and total vertical mass 2138.
Negative q0: j=1 repeated three times and j=8 once, mass 3*16+135=183. Negative total mass 2321; H0=4+4=8.

Both have the **same exact scaled reciprocal sum** 391/120, hence H1=937/120 on both sides. Signed vertical supports are distinct, as are signed q0 supports. q0 counts 7+4=11. Both complete side masses are <=2331.

## Scientific boundary / next discriminating obligation

This is a **sharp necessary H0+H1 bound** for the finite q14 case, not a six-observer collision: no H2,...,H6 or full mixed saturated affine congruence is asserted, and neither global T6=2332 nor native q14 admission follows. Next useful math: apply exact H2 (or the task's mixed congruence conditions) to these 333 H0/H1-preserving signed pairs without rerunning the completed parent q14 roster. An independent reviewer should verify the frozen q14 scientific input, the checker and whether the retained sign normalization agrees with the published plan.

The prior typed successor prepare requests remain terminally rejected, never replayed; the current exact continuation read's original request_id is onhour-20261122-1959-t6-own-current-continuation-v1. A queued/running read is not a winning CLAIM, and source publication and Activity association are not protected Native semantic PROGRESS.
