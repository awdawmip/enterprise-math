# R022 Twelfth-Pass Deepening — Adaptive Signature Acquisition and On-Demand Probe Depth

**Researcher-ID:** `EM-R022-HC7B4A`  
**Task:** `RS-R022-HASHCLASH-BRC-TOOL-MINING`  
**Taskbook base:** `89fb6c99fa2a00e42f58c1fc11ea016b7421f3be`  
**Owner PR:** `#497`  
**Status:** `TWELFTH_PASS / RESEARCH ADDENDUM / NOT CANONICAL`

## Executive result

Pass 11 showed that a minimum static raw-feature signature is a distinction-cover problem: choose a fixed feature subset whose columns distinguish every pair that the target precision requires split.

Pass 12 asks whether those features must all be read eagerly for every state.

No. If feature acquisition may be adaptive, a runtime may query one feature, inspect its value, and ask another feature only if the remaining possible continuations still disagree. This is a direct branch-on-demand realization of BRC refinement.

On the md5collgen source-shaped 9-bit routing model:

- every one of the 9 raw coordinates is needed somewhere, so the minimum static raw-coordinate signature uses all 9;
- materializing that signature eagerly costs 9 raw-bit reads per state in the abstract model;
- the source's `&&` short-circuit order, charging a raw bit only on first use and reusing cached bits, averages **3.015625** raw-bit reads over the uniform 512 assignments, worst case 9;
- an exact expected-cost-optimal adaptive raw-bit decision tree averages **2.140625** reads under the same uniform distribution, worst case still 9;
- every leaf of the optimal tree is route-pure, so this is exact routing rather than heuristic prediction.

Thus static signature width, worst query depth and expected query work are independent resource coordinates.

The generic algorithmic root is standard decision-tree/function-evaluation theory. The Enterprise Math residue is using it as the execution form of branch-on-demand signature refinement while keeping exactness proof-carrying and charging the distribution/cost assumptions explicitly.

Recommended classification:

`BRC_ADAPTIVE_SIGNATURE_ACQUISITION_FOUND / STATIC_SIGNATURE_VS_QUERY_DEPTH_SEPARATED / MD5_ROUTER_EXPECTED_PROBE_PARETO_DEMONSTRATED / PROOF_CARRYING_DECISION_ROUTER_FOUND / NOT_CANONICAL`.

---

## 1. Static cover versus adaptive acquisition

A static Raw Feature Signature Basis selects one global feature set `J`. Every state can be encoded by reading all selected features.

An adaptive signature router instead stores a decision node

`query feature j -> branch on observed value -> next query or route leaf`.

A leaf is exact when every fine state compatible with the observed query answers has the same continuation route/semantic target class.

This may reduce expected work because a feature needed to distinguish rare fine worlds need not be read after a common world has already been identified.

It does **not** invalidate pass 11: every raw feature appearing anywhere in the tree may still be globally necessary. The optimization objective has changed from

`number of distinct coordinates used globally`

to

`query cost along an execution path`.

## 2. md5collgen source-shaped model

Use the nine source-derived route-relevant bits:

- three bit-31 coordinates;
- three bit-25 coordinates;
- two bit-0 coordinates;
- `IV[1]` bit 6.

The bounded model enumerates all `2^9=512` assignments and applies the exact `S11/S10/S01/S00/Wang` route rule.

Route populations under uniform assignments:

- Wang: 504;
- S00/S01/S10/S11: 2 each.

This distribution is a property of the bounded uniform bit model, not a claim about actual MD5 intermediate-state frequencies.

## 3. Source short-circuit cost

Model the C++ logical order in `block1.cpp` and charge each raw coordinate at most once, reusing a previously read bit.

The abstract source order checks:

1. bit31 equality of IV1/IV2;
2. bit31 equality of IV1/IV3;
3. IV3 bit25 = 0;
4. IV2 bit25 = 0;
5. IV1 bit25 = 0;
6. bit0 equality of IV2/IV1;
7. if eligible, IV1 bit6 selects the Stevens variant while IV1 bit0 is already known.

Over the 512 uniform assignments, cached raw-bit read depth distribution is:

- depth 2: 256 states;
- depth 3: 128;
- depth 4: 64;
- depth 5: 32;
- depth 6: 16;
- depth 8: 8;
- depth 9: 8.

Average: **3.015625**. Worst: 9.

This does not measure compiled C++ word loads or CPU time; it is only the source-shaped bit-query accounting model required for comparison with the 9-bit signature.

## 4. Expected-optimal adaptive tree

Dynamic programming is run over partial 9-bit assignments.

For a partial assignment `p`:

- if every compatible full assignment has the same route label, stop;
- otherwise choose an unqueried feature `j` minimizing

`1 + sum_v Pr[value_j=v | p] * Opt(p,j=v)`

under the uniform distribution.

The root's optimal first query is `IV[1]` bit 25. Half of all assignments have that bit equal to 1 and are immediately known to be Wang.

Result:

**optimal expected depth = 2.140625 raw-bit queries**.

Depth distribution:

- depth 1: 256 states;
- depth 2: 128;
- depth 3: 64;
- depth 5: 32;
- depth 6: 16;
- depth 8: 8;
- depth 9: 8.

Worst-case optimal depth remains **9** because the rare Stevens routes require all relevant conditions to be certified.

So this is an expected-work improvement, not a reduction of the worst-case information requirement.

## 5. Pareto interpretation

Three exact representations/executions now coexist for the same source-shaped route function.

### Eager static raw signature

- global raw features: 9;
- per-state raw reads: 9;
- simple direct lookup/route.

### Source short-circuit router

- still uses the same relevant raw feature family;
- average cached reads in bounded uniform model: 3.015625;
- worst: 9.

### Expected-optimal adaptive router

- same semantic route;
- average bounded-uniform reads: 2.140625;
- worst: 9;
- requires a more specialized decision tree and distribution-sensitive optimization.

Ratios in this abstract model:

- eager-static / optimal expected read work: about `4.204x`;
- source-order / optimal expected read work: about `1.409x`.

No advantage is claimed without charging the decision-tree/code size, caching behavior and assumed state distribution.

## 6. Exactness verifier

A candidate adaptive tree need not be trusted.

For each leaf, collect the fine assignments consistent with the queried answers and verify that their route labels are identical.

The exact optimal tree generated in the bounded model has 13 leaves, covers all 512 assignments, and every leaf is route-pure.

Thus the architecture is again proof-carrying:

`tree proposer/optimizer -> leaf-purity verifier -> exact adaptive router`.

## 7. Relationship to distinction cover

Pass 11's static feature basis must globally cover all required pair distinctions.

An adaptive tree does not select one global subcover for every execution. Instead, after an answer removes many candidate worlds, only distinctions still possible inside the surviving branch require further tests.

Thus:

- static cover cost = global feature inventory;
- adaptive depth = path-local distinction acquisition;
- expected depth = distribution-weighted execution work;
- worst depth = strongest path-local information demand.

This is the exact BRC interpretation of "split only when the live world still needs the distinction."

## 8. Prior-art/rooting boundary

Adaptive evaluation of a discrete function by querying variable values and optimizing expected/worst query cost is classical decision-tree/function-evaluation work. R022 does not claim a new generic decision-tree algorithm.

The source-specific contribution is the exact md5collgen routing reconstruction and quantitative comparison against the static raw-signature baseline. The Enterprise Math abstraction is to make adaptive feature acquisition a first-class BRC execution strategy with exact leaf certificates and explicit storage/work/depth accounting.

## 9. R021 feedback

Recommended additions:

1. Add `adaptive_signature_router` beside static `branch_signature_router`.
2. Distinguish:
   - global feature inventory;
   - static token bits;
   - expected query depth/work;
   - worst query depth;
   - decision-tree/code size;
   - state-distribution assumption.
3. Permit on-demand feature acquisition after earlier answers have pruned possible worlds.
4. Require route-pure leaf certificates for exact adaptive routers.
5. Do not infer worst-case compression from expected-depth gains.
6. Use md5collgen's source-shaped 9-bit model as a concrete positive Pareto witness, not as a novelty claim about decision-tree theory.

No correction is requested to R023.

## 10. Twelfth-pass classification

`BRC_ADAPTIVE_SIGNATURE_ACQUISITION_FOUND / STATIC_GLOBAL_COVER_VS_PATH_LOCAL_REFINEMENT_SEPARATED / MD5_SOURCE_SHAPED_EXPECTED_DEPTH_GAIN_DEMONSTRATED / WORST_CASE_RAW_REQUIREMENT_UNCHANGED / PROOF_CARRYING_ADAPTIVE_ROUTER_FOUND / R021_FEEDBACK_READY / NOT_CANONICAL`.
