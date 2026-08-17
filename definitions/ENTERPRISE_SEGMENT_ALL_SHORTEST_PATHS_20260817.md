# 进取线段：原点到坐标的全部最短路径族

Status: `SUPERSEDED_AS_FOUNDATIONAL_START_CONVENTION / RETAINED_AS_SPATIAL_TAIL_THEOREM`
Date: `2026-08-17`
Driver: `EM-DVR-9GP3M7 / CONTROL_PLANE`
Superseded by: `definitions/ENTERPRISE_VOID_ORIGIN_EXISTENCE_GEODESIC_20260817.md`

> 本文件“全部最短路径构成线段”的结构保留，但“线段从原点开始、长度等于原点后邻接步数”的 foundational 起点约定已被 supersede。当前最高定义从外部虚无态 `VOID_E=∅` 出发，`VOID_E -> O_E=±1` 为第一步。本文以下 `GEO_E(O_E,P)` 只应解释为完整进取线段删除第一条存在生成边后的 **spatial tail**。

## 1. Retained spatial-tail theorem

For the native Enterprise vertex-adjacency graph `G_E`, fixed origin `O_E=(±1,±1,±1)` and native coordinate/state `P`, define native graph distance

`d_E(O_E,P) = minimum number of primitive native adjacency edges in any path from O_E to P`.

The integer path count used by `d_E` is an external combinatorial count. It does not create a native coordinate `0`; native zero remains nonexistent.

The complete spatial geodesic tail from `O_E` to `P` is

`GEO_E(O_E,P) = { gamma : O_E -> P | |gamma| = d_E(O_E,P) }`.

Freeze as retained structure:

`ALL_SHORTEST_SPATIAL_PATHS_ARE_RETAINED`.

No shortest path may be privileged or deleted merely to obtain a desired turn/circle.

Current full segment is instead

`SEG_E(P)=GEO_(G~_E)(VOID_E,P)`

with unique first edge `VOID_E -> O_E`, so deleting that first edge gives a canonical bijection

`SEG_E(P) <-> GEO_E(O_E,P)`.

## 2. Superseded length statement

The old foundational statement

`L_E(O_E,P)=d_E(O_E,P)`

is no longer the total Enterprise segment length.

Current total/existence length is

`ELL_E(P)=1+d_E(O_E,P)`.

On one signed axis,

`ELL_E(±n)=n` for all `n>=1`.

The old quantity `d_E(O_E,P)` remains a valid **post-origin spatial displacement count**.

## 3. Segment footprint — retained

The spatial footprint is derived, not separately axiomatized:

- `VERT(GEO_E)` = union of vertices over all spatial geodesics;
- `EDGE(GEO_E)` = union of primitive edges over all spatial geodesics;
- any triangle/strip representation is secondary incidence data induced by this full geodesic family.

Therefore a chosen ordered chain, terminal-side chain, edgewise side strip, packet stack, or other single carrier is not the line-segment ontology unless proved equivalent to the complete geodesic family.

## 4. One-post-origin-step reduction — retained with retyping

If `d_E(O_E,P)=1`, there is one primitive radial edge from `O_E` to `P`, so the spatial tail is that edge. The full segment has total existence length `ELL_E(P)=2` because its first edge is `VOID_E -> O_E`.

Stage AR's extra side triangle `C` may remain useful as a **turn/sweep state augmentation**, but it is not part of the identity of the segment itself.

## 5. Auxiliary chart firewall — retained

The zero-centered A2 chart may be used only as an auxiliary computation/incidence certificate via the accepted signed-origin conjugacy.

If `P` decodes to auxiliary `(a,b)`, a later theorem may prove a closed form for `d_E`; that formula is not inserted here as an axiom.

## 6. Local deformation consequence — retained for spatial tails

A local triangle `1->2` replacement between the same two spatial subpath endpoints increases primitive spatial path length by one and therefore cannot remain in `GEO_E(O_E,P)` unless some other change alters the endpoints/target or restores geodesicity by an independently proved mechanism.

The natural geodesic-preserving local ambiguity is expected to be equal-length path replacement (for example a `2<->2` rhombus/step-order exchange where valid), but this must be proved rather than assumed.

## 7. Fixed-length endpoint set — superseded indexing

The old spatial shell

`SPHERE_E(O_E,r)={P:d_E(O_E,P)=r}`

remains a valid graph shell, but it is no longer indexed by the total Enterprise segment length.

Current fixed-existence-length endpoint set is

`EXISTENCE_SPHERE_E(n)={P:ELL_E(P)=n}`

`={P:d_E(O_E,P)=n-1}`.

Whether this shell is the canonical Enterprise circle remains a theorem question.

## 8. Historical typing

Stage AS correctly proved underdetermination under weaker carrier axioms. The later all-shortest-path ontology selected graph distance; the current void-start foundation further shifts the full segment start one step outward from `O_E` to `VOID_E`.

Historical results that define segment length through membership in a previously selected turn orbit must be re-audited. Algebraic/combinatorial identities may survive even if their native `line segment / circle` interpretation changes.
