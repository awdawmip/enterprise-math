# R043-C6 — Single-Component Rooted Successor-Extension Rigidity Return

Status: `FROZEN FINAL RETURN / REDUCED_TO_STRICTLY_SMALLER_HIDDEN_EXTENSION_INVARIANT / NOT CANONICAL`

Date: `2026-08-27`  
Task-ID: `RS-R043C6-SINGLE-COMPONENT-ROOTED-SUCCESSOR-EXTENSION-RIGIDITY`  
Publication-ID: `TP2-AFB98624889A10E1D3D0`  
Researcher-ID: `EM-R043C6-71DFD3`  
Claim-ID: `chatgpt-r043c6-20260827-2145`  
Execution branch: `research/r043c6-single-component-rooted-successor-extension-rigidity-em-r043c6-71dfd3`  
Execution base: `55a4034702fe88a9b89073cb61b5fc00cffa7413`

## 0. Primary verdict

`REDUCED_TO_STRICTLY_SMALLER_HIDDEN_EXTENSION_INVARIANT` in both frozen worlds.

This return does **not** claim global rooted-`G0` rigidity and does **not** claim a harmful collision. Instead it closes a stronger reduction than the input taskbook had available:

> For one addition at a rooted frontier site `x`, every part of the successor weighted frontier is already forced by the current rooted weighted `G0` except one uniformly root-local finite incidence profile `J_x`. No deeper part of `Omega`, no global native embedding, and no full `K_partial` carrier is needed for the one-step update.

The remaining C6 gate is therefore no longer an unbounded hidden-geometry reconstruction problem. It is exactly a realizable-completion uniqueness problem for `J_x` modulo rooted weighted-`G0` automorphisms.

FCC disposition:

`REDUCED_TO_ROOT_LOCAL_J_X_ORBIT_UNIQUENESS_PROBLEM_FCC`.

HCP disposition:

`REDUCED_TO_ROOT_LOCAL_J_X_ORBIT_UNIQUENESS_PROBLEM_HCP`.

## 1. Frozen current observable

Let `C` be a finite connected occupied state in frozen FCC or HCP, let `Omega` be one connected component of the current unoccupied graph, and put

`F = F_Omega = F(C) intersect Omega`.

By accepted R043-C5, `F` is native-contact connected.

Let `G = G0[F]` be the current weighted induced frontier graph:

- vertices are the sites of `F`;
- two vertices are adjacent exactly when the corresponding native sites are 12-contact adjacent;
- the vertex weight is

`w_C(y) = |N(y) intersect C|`.

Choose an admissible rooted action `x in F`. The rooted current observable is the weighted rooted isomorphism class

`[G,x]`.

Equivalently one may name the rooted automorphism orbit `orbit_G(x)`; nothing below depends on a chosen coordinate representative.

## 2. Exact root-neighbor partition

Because `x` and every unoccupied native neighbor of `x` lie in the same unoccupied component `Omega`, the twelve native neighbors of `x` split disjointly as

`N(x) = I_x disjoint_union A_x disjoint_union Z_x`,

where

- `I_x = N(x) intersect C`;
- `A_x = N(x) intersect F`;
- `Z_x = N(x) \ (C union F)`.

The first two cardinalities are already visible in rooted `G0`:

`|I_x| = w_C(x)`

and

`|A_x| = deg_G(x)`.

Hence the number of currently zero-weight neighbors that will be exposed by adding `x` is not hidden at all:

`|Z_x| = 12 - w_C(x) - deg_G(x)`.

Since `x` is a frontier site, `w_C(x)>=1`, so uniformly

`|Z_x| <= 11`.

This is the first exact compression: any missing one-step state is bounded independently of the size or depth of `Omega`.

## 3. The exact missing profile J_x

Define the root-local zero-weight exposure profile `J_x` to consist of:

1. the finite set `Z_x` of newly exposed sites;
2. native-contact edges induced inside `Z_x`;
3. native-contact incidence edges from `Z_x` to the surviving old frontier `F\{x}`.

Coordinates are only an implementation carrier. The invariant content is the extension profile modulo automorphisms of the rooted weighted current graph `[G,x]`.

Write this orbit as

`[J_x]_{Aut(G,x)}`.

A still coarser canonical one-step datum may quotient two such profiles whenever their completed successor weighted graphs are isomorphic over the rooted-current base. That successor-equivalence quotient is, by construction, the coarsest extra datum needed for one-step prediction. This return does not promote either carrier to Foundation state.

## 4. R043C6-T1 — exact one-step reconstruction from [G,x] + J_x

Set `C' = C union {x}`. Consider the full successor frontier descended from the old component `Omega`; deleting `x` may split `Omega`, but this causes no difficulty.

Its weighted graph is obtained exactly as follows.

### Vertex set

Every old frontier site except `x` remains frontier because it already had an occupied neighbor in `C`.

A currently non-frontier neighbor `z` of `x` becomes frontier iff `z in Z_x`.

Therefore

`F' = (F\{x}) union Z_x`.

### Weights on surviving old vertices

For `y in F\{x}`,

`w_{C'}(y) = w_C(y) + 1_{y~x}`.

The indicator is already known from the current graph: `y~x` iff `{x,y}` is an edge of `G`.

### Weights on new vertices

For `z in Z_x`, `z` had no occupied neighbor in `C`; otherwise it would already have belonged to `F(C)`. After `x` is occupied it has exactly one occupied neighbor, namely `x`:

`w_{C'}(z)=1`.

### Edges

All old-old frontier edges are unchanged, so they are exactly the edges of `G-x`.

The only successor edges not already present in `G-x` are edges having at least one endpoint in `Z_x`. Those edges are exactly the incidence records stored in `J_x`.

Therefore the successor weighted frontier graph is a deterministic function

`Succ([G,x], J_x)`.

This proves globally, in both FCC and HCP, that **no other hidden information can affect one-step successor `G0` once `J_x` is fixed**.

The proof uses only frozen 12-contact adjacency and the definition of frontier/attachment weight. It does not use bounded animal enumeration, Euclidean distance, curvature, radius, probability, amplitude, or a continuum surrogate.

## 5. What this removes from the search space

Before C6, a negative mechanism could have been imagined to live arbitrarily deep inside one connected `Omega`.

R043C6-T1 kills that possibility for the one-step question.

For a fixed rooted current `G0`, a harmful collision exists **iff** there are two globally realizable root-local completion profiles `J_x` and `J'_x` compatible with the same rooted weighted state such that

`Succ([G,x],J_x)` and `Succ([G,x],J'_x)`

are not weighted-graph isomorphic.

Thus the global mother question is reduced to:

`ROOTED G0 -> REALIZABLE J_x COMPLETION ORBITS -> SUCCESSOR`.

The new side of every completion has at most eleven vertices. The old frontier may be large, but `J_x` touches only old frontier sites native-adjacent to one of those at-most-eleven new vertices, so the unknown relation is uniformly root-local.

This is strictly smaller than reconstructing full `K_partial`: it stores no inward occupied slot set for unrelated frontier vertices, no full native embedding of the frontier, no deeper exterior, and no deep interior.

## 6. Exact finite root-star classification

A deterministic checker exhausts the most local theorem-discriminating family: connected proper subsets of the twelve native neighbors of a fixed root. The all-twelve cage is excluded because it makes the root a shielded singleton unoccupied component and is outside the C6 single-component target.

The checker uses WL hashes only as safe candidate buckets. Every matched-current comparison and every successor comparison is an exact VF2++ weighted graph isomorphism test.

Results:

| world | legal connected proper root-star states | exact rooted pair tests | harmful successor splits | update-identity mismatches |
|---|---:|---:|---:|---:|
| FCC | 2,432 | 2,351 | 0 | 0 |
| HCP | 2,453 | 2,193 | 0 | 0 |

This census is regression/evidence only. It is **not** used to infer global rigidity.

A separate directed pressure during research also tested dense root-star states with one extra second-ring occupied site and found no mixed successor class, but that larger pressure is intentionally omitted from the frozen proof chain because it adds cost without changing the structural theorem.

## 7. Why no positive G0-rigidity claim is made

R043C6-T1 says the only missing one-step information is `J_x`; it does not yet prove that `[G,x]` uniquely reconstructs the realizable orbit of `J_x`.

That uniqueness would require a structural native completion theorem or an exhaustive theorem-discriminating local-extension classification that covers every globally realizable root neighborhood. The present root-star census is only a strict subfamily.

Therefore:

`ROOTED_SUCCESSOR_EXTENSION_RIGIDITY_PROVED_FCC = NOT CLAIMED`.

`ROOTED_SUCCESSOR_EXTENSION_RIGIDITY_PROVED_HCP = NOT CLAIMED`.

Likewise, no same-rooted-`G0` pair with different successor has been found, so:

`HARMFUL_ROOTED_G0_COLLISION_FCC = NOT CLAIMED`.

`HARMFUL_ROOTED_G0_COLLISION_HCP = NOT CLAIMED`.

The exact unresolved residue is now only:

`J_x REALIZABLE ORBIT UNIQUENESS / COLLISION`.

## 8. All-finite-horizon audit

The reduction is one-step exact but does not by itself prove stationary all-horizon sufficiency of raw `G0`.

There is, however, a clean induction gate:

> If a later theorem proves that for **every reachable FCC/HCP rooted weighted `G0` state** all globally realizable `J_x` completions are successor-equivalent, then R043C6-T1 composes immediately by induction to every finite addition horizon.

The reason is that the one-step successor is again a reachable state to which the same completion-uniqueness theorem applies.

Conversely, a single realizable pair of `J_x` completions yielding nonisomorphic successors kills one-step sufficiency immediately; no later-horizon construction is needed.

Thus no separate recoalescence mechanism remains at the one-step gate once `J_x` completion uniqueness is decided globally.

## 9. Deterministic certificate

Checker:

`scripts/check_r043c6_rooted_successor.py`

Certificate:

`research_artifacts/R043C6_rooted_successor/RESULTS.json`

The checker independently verifies:

- exact FCC/HCP frozen 12-contact neighbors;
- the `Z_x` exposure construction;
- exact successor reconstruction from current rooted `G0 + J_x` on every enumerated root-star state;
- exact rooted weighted-current isomorphism classes versus successor weighted-graph isomorphism;
- zero harmful split in the frozen local regression family.

## 10. Final classification

Primary classification:

`REDUCED_TO_STRICTLY_SMALLER_HIDDEN_EXTENSION_INVARIANT`.

FCC:

`REDUCED_TO_ROOT_LOCAL_J_X_ORBIT_UNIQUENESS_PROBLEM_FCC`.

HCP:

`REDUCED_TO_ROOT_LOCAL_J_X_ORBIT_UNIQUENESS_PROBLEM_HCP`.

Global theorem frozen by C6:

`ROOTED G0 + J_x -> EXACT ONE-STEP SUCCESSOR`,

with

`|Z_x| = 12 - w_G0(x) - deg_G0(x) <= 11`.

Global raw-`G0` rigidity remains open only at realizable `J_x` orbit uniqueness.

No Foundation promotion is requested. No component-grouping, octahedral-pinch, or unrelated R043 stage is reopened inside this return.
