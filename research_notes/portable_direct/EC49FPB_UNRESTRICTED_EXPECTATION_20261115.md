# EC49FPB — Unrestricted expectation-optimal adaptive terminal sensing in two frozen native BRC classes

Date: 2026-11-15 (Asia/Shanghai). Research state: AUTHOR_PROVED / EXACT_FINITE_CHECKED / NOT_REVIEWED.

## Exact continuation and strengthened conclusion

This result strengthens EC49FPA ([PR #2459](https://github.com/awdawmip/enterprise-math/pull/2459)) by **removing the worst-case-depth-three restriction**. It reuses the same original immutable input and the same 432 valid complete assignments per class. The science pin stays `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`, and the original native evidence is preserved in EC49FOZ ([PR #2454](https://github.com/awdawmip/enterprise-math/pull/2454), commit `62826f378a05a2243472e67ff4fb94752d75f20c`).

For each of the **complete** original legal-root-domain classes represented by native configuration 14304 and 14309, there are 75 native configurations, 40 distinct reachable-root cost profiles, and 432 complete legal assignments. A query chooses one legal assignment and observes its exact integer terminal cost; the goal is to identify the hidden root-cost profile.

**Theorem (no depth limit).** Among all terminating deterministic adaptive policies, with no preassigned depth cap, the minimum expected query count is:

| Original class | Prior: uniform among 40 root profiles | Prior: uniform among 75 native configurations | Minimum worst-case depth among expectation-optimal policies |
|---|---:|---:|---:|
| 14304 | **73/40 = 1.825** | **177/75 = 2.36** | **3** |
| 14309 | **73/40 = 1.825** | **177/75 = 2.36** | **3** |

The root-profile multiplicity distribution is 38 profiles occurring once, one twice, and one 35 times for each class, verified from original configuration-to-profile data.

**All expectation-optimal first assignments, without a depth restriction:**

| Original class | Prior | First assignment(s) achieving the global expected minimum | Minimum worst-case depth conditional on that first assignment |
|---|---|---|---|
| 14304 | Uniform root profiles | **78**, 99, 177 | 3, 4, 4, respectively |
| 14304 | Uniform native configurations | **78** | 3 |
| 14309 | Uniform root profiles | **119**, 153, 191 | 3, 4, 4, respectively |
| 14309 | Uniform native configurations | **119** | 3 |

In particular, EC49FPA's first assignments 78 and 119 remain expectation-optimal even when arbitrarily deep policies are permitted. Two *additional* expectation-optimal initial assignments exist for the **uniform root-profile** prior; their best depth is 4, so the depth-three-restricted first-action uniqueness in EC49FPA remains correct.

The optimal depth-three policy has 15 distinct profiles identified at depth 1, 17 at depth 2, and 8 at depth 3, giving total 15 + 2·17 + 3·8 = 73. Under uniform original configurations, its 75 input configurations split across those depths as 15, 18 and 42, yielding 15 + 2·18 + 3·42 = 177.

## Complete global optimality proof

Let `C` be the finite set of 40 root profiles. Each profile `p` has a vector of 432 *exact integer* terminal costs `T_p(a)`. For every nonempty subset `F ⊆ C`, define `w(F)=Σ_(p∈F)w_p`, with positive integer weights `w_p=1` or the precise multiplicities in the 75-config prior. Each assignment `a` partitions the current candidate fiber `F` into nonempty level sets `Π_a(F)` according to the observed terminal cost. Only separating assignments (at least two nonempty outcome cells) need be considered at non-singleton `F`: a nonseparating assignment costs `w(F)>0` while preserving the same information and can be removed from any finite policy without loss of discrimination.

Define the minimum *total weighted number of future observations* from information state `F` by:

```
V_w({p}) = 0

V_w(F) = w(F) + min_{a : |Π_a(F)|>1}
                        Σ_{G∈Π_a(F), |G|>1} V_w(G).
```

Every child `G` of a separating assignment is a **strict subset** of `F`; the recurrence is therefore well-founded by induction on `|F|`. The equation is exact: every policy pays one query for every candidate profile in the present fiber; after observing the outcome, independent conditional subpolicies incur optimal residual costs. Conversely, choosing a minimizing action for every fiber assembles a valid deterministic policy. Randomized policies cannot improve the expectation, since a mixture of first actions and conditional policies has expected cost no smaller than its best deterministic component at that information state.

The finite exact evaluator constructs all 432 integer query columns from the frozen native root-subset cost data, memoizes all actually reachable candidate fibers, and minimizes this recurrence over **every** separating assignment. Its computed `V_w(C)` is 73 for the profile-uniform prior, and 177 for the configuration-uniform prior, in both classes. A second independently implemented evaluator represents each fiber as a sorted tuple of profile indices and tests **distinct partitions** instead of integer-bitset partitions. Both return exactly the same minima and the complete sets of minimizing initial assignments. A separate optimizer lexicographically minimizes `(total weighted expected cost, worst-case depth)`, yielding the depth classifications in the preceding table.

| Class | Bitset evaluator states (40-profile / 75-config) | Independent tuple-partition evaluator states | Lexicographic depth evaluator states |
|---|---:|---:|---:|
| 14304 | 1,664 / 1,442 | 1,783 | 1,787 |
| 14309 | 1,653 / 1,423 | 1,782 | 1,787 |

These are *memoized states actually visited by the algorithms*, not an assertion that all 2⁴⁰ subsets were materialized. Unrestricted termination and the optimality equation hold for every deterministic decision tree on the exact finite state space: nonseparating observations are strictly removable, and all remaining paths have strictly decreasing finite candidate sets.

## Verification and preserved evidence

Independent exact implementations used:

1. `EC49FPB_UNRESTRICTED_EXPECTATION.py` — integer bitset unrestricted Bellman DP with traced optimal tree.
2. `EC49FPB_INDEPENDENT_PARTITION_DP.py` — independent tuple-fiber, distinct-partition evaluator for *all* optimal initial observations.
3. `EC49FPB_OPTIMAL_FIRST_DEPTH.py` — tie-breaker verifying the minimum depth of expectation-optimal policies conditional on each optimal first assignment.
4. Prior immutable `EC49FOZ_verify.py` — reconstruct original integer terminal observation matrices from SHA256-pinned original BRC input and native root-subset-cost records; prior proof and source pinned in EC49FPA/EC49FOZ evidence.

The exact saved JSON certificates and execution logs are included in the companion evidence archive. Each verifier actually executed successfully for both classes and both priors; all objectives are integer totals and use no floating-point comparison or numeric approximation. The companion remote source code is provided alongside this note.

The result concerns two *specific complete frozen finite native legal-root classes*, exact-cost adaptive observations, and the two explicitly stated priors. It does not alter P000 or accept the theorem into Foundation. All prior provenance and the existing three native all-assignment gauge-cancellation pairs are preserved.

## Next scientific questions

1. On the original three nonzero terminal-invisible gauge pairs found in EC49FOR, characterize the equivalence relation of all possible adaptive terminal-only policies. An identical full `T` function makes every adaptive observation sequence identical, so the unobservability theorem follows by induction over the policy transcript; investigate what *additional typed branch/root observation* can break that equivalence.
2. Apply the unrestricted Bellman recurrence to other frozen root domains with nonconstant root-subset structure, quantify efficiency and identify groups where depth or prior materially changes the optimum.
3. Study the minimal sufficient statistic of a terminal-cost observation policy, and how a root-/branch-preserving readout interacts with P000's residual-fidelity requirement.

This result supersedes the *open research question* in EC49FPA about the unrestricted optimal expectation, not its established restricted-depth result, inputs, or published evidence.
