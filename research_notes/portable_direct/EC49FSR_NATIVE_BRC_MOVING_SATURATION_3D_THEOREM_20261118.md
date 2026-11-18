# EC49FSR — Exact native BRC moving saturation surface in a three-price prism

Date: 2026-11-18. Frozen science pin: fc0f038e7bfd12c886b4d37f900bfb770c0f61ab. This portable result continues EC49FSQ PR #2715@b38bf22508ff2822d469587760878fb7593f2c76 and EC49FSN PR #2706@0842017a6bfdc83e7af59c6d2be0493dd53d58da. Scientific status: AUTHOR_PROVED / EXACT_PRIMARY_12_VERTICES / INDEPENDENT_2_VERTICES / NOT_REVIEWED. No formal Task CLAIM, Activity checkpoint, Result or Review is asserted.

## Original-native problem and exact result

Keep all 310 original configurations, 141 distinct original named joint-response profiles with uniform prior, and all 228 physically named deterministic observations. No outcomes or sensors are collapsed. Every complete adaptive deterministic identification tree is allowed.

Prices are (1-a)t on q32, (1-b)t on q34, (1-z)t on q140 and t>0 on all remaining original observations. Let F(a,b,z)=141 V(a,b,z)/t be the unrestricted exact Bellman optimum total normalized cost.

**Theorem.** For every real (a,b,z) satisfying

    1/2 <= a <= 1,
    27/64 <= b <= 29/64,
    31/64 <= z <= 1/2,

the unrestricted direct and price-exchanged optima are exactly

    D(a,b,z) = F(a,b,z)
      = min(319 - 18a - 75b - 141z,
            313 - 141a - 43b - 24z),

    S(a,b,z) = F(b,a,z)
      = 311 - 141a - 10b - 69z.

The internal saturation boundary is the full affine surface

    a_*(b,z) = (32b + 117z - 6)/123.

The first direct plane is optimal for a<=a_*; the second for a>=a_*, and they tie on the boundary. Across the rectangle a_* ranges from 1369/2624 to 67/123, strictly between 1/2 and 1. This is a genuinely three-dimensional continuum result: b and z both vary.

The exact price-exchange difference is

    D-S = 8 + 123a - 65b - 72z, if a<=a_*;
    D-S = 2 - 33b + 45z,        if a>=a_*.

It is positive over the *entire closed prism*. Its sharp minimum is 259/64, attained at (a,b,z)=(1/2,29/64,1/2). For fixed b,z, the exchange difference grows linearly with a before saturation and then becomes constant.

## Original feasible full decision trees

For a full original named tree, (U,N32,N34,N140) counts all tests and the q32, q34, q140 uses summed over the 141 named state paths. Three exact full-tree witnesses, already independently preserved losslessly in their source PRs, are:

| witness | (U,N32,N34,N140) | exact cost | prior immutable source |
|---|---|---|---|
| A, q140-saturated | (319,18,75,141) | 319-18a-75b-141z | EC49FSN PR #2706@0842017a, original 15 trees |
| B, q32-saturated | (313,141,43,24) | 313-141a-43b-24z | EC49FSQ PR #2715@b38bf225, full new original tree |
| C, exchanged q34-saturated | (311,10,141,69) | 311-10b-141a-69z | EC49FSN PR #2706@0842017a, original 15 trees |

All three represent original named observations and distinguish all 141 distinct response profiles. The finite solver uses the original strict-splitting response partitions for every one of the 228 named observations.

## Twelve load-bearing exact native Bellman endpoints

At the b,z corner pairs below, the solver independently evaluates all unrestricted 228-observer choices at a=1/2 in both orientations, and again at a=a_*(b,z) for the direct orientation.

| b | z | D(1/2,b,z) | a_* | D(a_*,b,z) | S(1/2,b,z) |
|---|---|---|---|---|---|
| 27/64 | 31/64 | 3361/16 | 1369/2624 | 275089/1312 | 12983/64 |
| 27/64 | 1/2 | 13303/64 | 22/41 | 543695/2624 | 6457/32 |
| 29/64 | 31/64 | 6647/32 | 4171/7872 | 135911/656 | 12963/64 |
| 29/64 | 1/2 | 13153/64 | 67/123 | 537161/2624 | 6447/32 |

Each value is a Fraction-exact exhaustive Bellman optimum and equals the corresponding feasible tree cost. Primary computation covers all 141 profiles and all 228 named observations. A separate independent raw 94-family decoder reproduced (i) D(1369/2624,27/64,31/64)=275089/1312 (9845 reachable subproblems) and (ii) S(1/2,29/64,1/2)=6447/32 (9535 subproblems). Full machine certificate, executable verification program and stdout logs are included in the self-contained evidence bundle.

## Proof for every real point

1. The normalized total cost of each fixed complete original named tree is affine in (a,b,z). Since the unrestricted optimum is the pointwise minimum of feasible affine costs, F is jointly concave and cannot exceed the cost of any fixed feasible tree.
2. Let P_low be the closed polytope given by the b,z rectangle and 1/2<=a<=a_*(b,z). The upper boundary is affine and stays strictly above 1/2. Thus P_low is exactly the convex hull of its eight vertices, one at a=1/2 and one at a=a_*(b,z) above each of four b,z corners.
3. At these eight vertices, exact exhaustive Bellman gives the cost of feasible tree A. By concavity, the Bellman optimum is at least the affine cost of A throughout P_low; feasibility provides the opposite inequality. Equality follows everywhere on P_low.
4. At each of four corner points on the crossing surface a=a_*(b,z), feasible tree B has the same cost as A and hence the exact unrestricted Bellman optimum. The crossing surface is an affine image of the rectangle. Concavity and tree B feasibility again give exact global optimality of tree B over its entire continuous surface.
5. Tree B observes q32 on all 141 named-profile paths. The EC49FSQ saturation lemma says that from a globally optimal tree with N32=141, further lowering q32's price makes the unrestricted optimum decrease by exactly 141 times the additional discount. Apply at every crossing point, extending tree B optimality to all a>=a_*(b,z), through a=1.
6. On the exchanged orientation, the four Bellman values at a=1/2 equal the feasible q34-saturated tree C. Concavity and its feasibility extend equality to the entire b,z base rectangle. Since N34=141, the same saturation lemma lifts its optimality to every a>=1/2.
7. Subtraction yields the two exact gap expressions. In the lower phase the gap grows with a and is minimized at a=1/2. On that face, it decreases with b and z, reaching 8+123/2-65(29/64)-72/2=259/64. The upper phase is continuous and constant in a for fixed b,z, proving the sharp global minimum.

This proof checks 12 finite vertices and uses exact concavity plus an existing algebraically proved saturation lemma; it is not numerical grid interpolation.

## Adjacent-face counterexample and next question

At (a,b,z)=(1,27/64,33/64), above the proved upper z face, unrestricted original Bellman equals 9049/64, with a complete original named tree having (U,N32,N34,N140)=(316,141,43,30). Retaining the tree-B plane from the theorem would yield 9055/64, an excess of 3/32. Those two feasible planes differ by 3-6z and cross at z=1/2. This is a scoped counterexample to extending *that fixed witness plane* beyond the upper face; it makes no claim about the complete adjacent Pareto fan.

New full named challenger tree and reproduction scripts are in the associated evidence package. The next scientific unit is to resolve the adjacent three-price cell at z>1/2, where the q140=30 tree competes with the prior q140=24 tree and new swapped policies. Preserve the frozen observations, P000 and all 141 named response paths.

## Research and control scope

The calculation is a finite native BRC observer identification optimization, not a continuous-time BRC trajectory or claim about heartbeat elapsed time. The original science pin is unchanged. Independent mathematical review and authenticated Activity correlation remain open. Historical Researcher-ID EM-DIRECT-8454C6, SID MCP-44cfc4e6f2094f96861854ebefc77e84, historical RA-ED136F89271FD89288F3E58D; the current formal task identity remains unpublished in the last verified control snapshot. This portable source publication does not claim new execution authority.
