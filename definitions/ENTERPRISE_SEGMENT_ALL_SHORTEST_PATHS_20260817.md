# 进取线段：原点到坐标的全部最短路径族

Status: `ACTIVE / CANONICAL / FOUNDATIONAL`
Date: `2026-08-17`
Driver: `EM-DVR-9GP3M7 / CONTROL_PLANE`
Depends on: `definitions/ENTERPRISE_SIGNED_ORIGIN_ONE_COORDINATE_20260817.md`

## 1. Foundational freeze

For the native Enterprise vertex-adjacency graph `G_E`, fixed origin `O_E=(±1,±1,±1)` and native coordinate/state `P`, define native graph distance

`d_E(O_E,P) = minimum number of primitive native adjacency edges in any path from O_E to P`.

The integer path count used by `d_E` is an external combinatorial count. It does not create a native coordinate `0`; native zero remains nonexistent.

The Enterprise line segment from `O_E` to `P` is **not one selected shortest path**. It is the complete geodesic path family

`SEG_E(O_E,P) = GEO_E(O_E,P) = { gamma : O_E -> P | |gamma| = d_E(O_E,P) }`.

Freeze:

`ALL_SHORTEST_PATHS_ARE_THE_SEGMENT`.

No shortest path may be privileged or deleted merely to obtain a desired turn/circle.

## 2. Native segment length

Define

`L_E(O_E,P) = d_E(O_E,P)`.

Thus length is the common primitive-edge count of every path in `SEG_E(O_E,P)`.

On one native axis, the signed-origin coordinate `±n (n>=2)` has coordinate magnitude `n` but

`L_E(O_E,±n)=n-1`.

This preserves the frozen distinction between coordinate magnitude and adjacency-step count.

## 3. Segment footprint

The segment footprint is derived, not separately axiomatized:

- `VERT(SEG_E)` = union of vertices over all geodesics;
- `EDGE(SEG_E)` = union of primitive edges over all geodesics;
- any triangle/strip representation is secondary incidence data induced by this full geodesic family.

Therefore a chosen ordered chain, terminal-side chain, edgewise side strip, packet stack, or other single carrier is not the line-segment ontology unless proved equivalent to the complete geodesic family.

## 4. One-step reduction

If `L_E(O_E,P)=1`, there is one primitive radial edge from `O_E` to `P`, so the segment itself is that edge.

Stage AR's extra side triangle `C` may remain useful as a **turn/sweep state augmentation**, but it is not part of the identity of the one-step segment itself. The two AR side lifts are two local turn states over one underlying segment.

## 5. Auxiliary chart firewall

The zero-centered A2 chart may be used only as an auxiliary computation/incidence certificate via the accepted signed-origin conjugacy.

If `P` decodes to auxiliary `(a,b)`, a later theorem may prove a closed form for `d_E`; that formula is not inserted here as an axiom.

## 6. Local deformation consequence to test

A local triangle `1->2` replacement between the same two subpath endpoints increases primitive path length by one and therefore cannot remain in `SEG_E(O_E,P)` unless some other change alters the endpoints/target or restores geodesicity by an independently proved mechanism.

The natural geodesic-preserving local ambiguity is expected to be equal-length path replacement (for example a `2<->2` rhombus/step-order exchange where valid), but this must be proved rather than assumed.

## 7. Fixed-length endpoint set

For integer `r>=1`, define the native fixed-length endpoint sphere

`SPHERE_E(O_E,r) = { P : d_E(O_E,P)=r }`.

This is the immediate candidate endpoint set swept by a fixed-length Enterprise segment. Whether its intrinsic adjacency graph is the correct Enterprise circle, its circumference law, and its relation to historical AK/AL/AI circle objects are theorem questions, not frozen here.

No historical circle result is protected from an exact contradiction produced by this new foundational segment definition.

## 8. Supersession / prior-result typing

Stage AS (old carrier-classification task) correctly proved underdetermination under the weaker axioms: in particular `L_chain` and `L_disp` both survived. This foundational definition resolves that underdetermination by selecting `L_disp=d_E` and the complete shortest-path family as the segment ontology.

Historical results that define segment length through membership in a previously selected turn orbit must be re-audited against this definition. Algebraic/combinatorial identities may survive even if their native `line segment / circle` interpretation changes.
