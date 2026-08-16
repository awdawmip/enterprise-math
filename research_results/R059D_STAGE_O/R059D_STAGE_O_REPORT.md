# R059D Stage O — Completion-Neighbor / Symmetry No-Go / Minimal Context

Researcher-ID `EM-R059D-9C6B2A` · taskbook `daae6ff47b02648435ec0f3aed082ba9b345b5e8` · frozen parent `cacbd211a9811e96f361606d56e66bffdf83bf53`.

## Frozen disposition

`ADJACENT_COMPLETED_STATE_GATE_IS_DEFINITIONAL_GIVEN_COMPLETION_LAYER`.

For an ordered discrete completion layer `C`, on the declared gap domain where both adjacent completed neighbors exist,

`COLL_C(q;b)=PREV_C(q)+(NEXT_C(q)-PREV_C(q))b`, `b∈{0,1}`, `b²=b`.

Thus `{PREV_C(q),NEXT_C(q)}` is the legal endpoint set by the completion-neighbor primitive itself; it is not a selector. For `C=Z,q=-1/2`, PREV/NEXT are exactly `-1,0`. For the nonnegative square layer and `q=5`, they are `4,9`. Under `T(x)=2x+3`, `Z,q=1/2` map to `3+2Z,q=4` with neighbors `3,5`. Positive affine transforms preserve PREV/NEXT order when the completion layer transforms with the state; negative transforms reverse it, so `PREV_{-C}(-q)=-NEXT_C(q)` and `NEXT_{-C}(-q)=-PREV_C(q)`.

Stage N froze the displacement module `Lambda={(dx,dy,dz)∈Z³:dx+dy+dz=0}`. Therefore the completed displacement-coordinate layer used by the transfer theorem is inherited as `C=Z`; `-1/2` is an unresolved auxiliary rational precollapse value, not a completed coordinate or packet weight. Freeze: `COORDINATE_COMPLETION_Z_INHERITED_FROM_INTEGER_DISPLACEMENT_MODULE`. No new coordinate-minimality axiom is required in this typed scope.

## Two branches and D6

For recipient event `dy=+1`, the already-frozen transverse exchange symmetry gives the unresolved compensation `dx*=dz*=-1/2`. Integer completion-neighbor collapse gives `dx=-1+b_x`, `dz=-1+b_z`. Affine conservation yields

`(-1+b_x)+1+(-1+b_z)=0`, hence `b_x+b_z=1`.

The exact Boolean solutions are `(0,1),(1,0)`, producing `(-1,1,0)` and `(0,1,-1)`. Coordinate permutation gives

`{e_i-e_j:i!=j}`

with cardinality six, exactly `{+u,-u,+v,-v,+w,-w}`. Freeze: `D6_EMERGES_FROM_AFFINE_PLUS_COMPLETION_NEIGHBOR_PRIMITIVE`; the Stage-N separate ad hoc minimality dependency is removed.

Boundary: affine conservation + event + integer completion **without a rule fixing the unresolved transverse q values** does not identify D6. The positive rederivation still uses the frozen transverse-exchange-symmetric half-state construction. This is a symmetry/typing dependency, not a hidden minimality axiom.

## Stateless symmetry no-go

Let `tau` exchange the two transverse coordinates. At the symmetric input, `s=tau(s)`, while branch action is `b→1-b`. A deterministic stateless equivariant selector would require

`f(tau(s))=1-f(s)`,

hence `f(s)=1-f(s)`, impossible for `b∈{0,1}`. Freeze:

`STATELESS_EXCHANGE_EQUIVARIANT_UNIQUE_BRC_SELECTOR_IMPOSSIBLE_AT_SYMMETRIC_STATE`.

`{0,1}` as a set-valued output is equivariant but not unique. A symmetric randomized law is nondeterministic and is not promoted to native BRC or physical probability. Hidden label ordering and coordinate-name bias break equivariance. History/external context changes the input space and is therefore analyzed explicitly rather than treated as a loophole.

## Minimum context and straight continuation

Take previous branch bit `h`. Under transverse exchange, `h→1-h`. The four one-bit Boolean functions are `0,1,h,1-h`. Exchange covariance `F(1-h)=1-F(h)` leaves exactly `{h,1-h}`: a finite selector equivalence class.

For fixed recipient `y`, `t_1=(-1,1,0)` and `t_0=(0,1,-1)` are Z-linearly independent (the x,y minor is `-1`). Therefore a repeated transfer sequence spans a rank-one integer submodule iff it never mixes the two branch vectors. Straight continuation thus requires

`b_{k+1}=b_k`.

With `h=b_k`, the unique straight continuation rule is `b_next=h`; it kills the symmetry-only alternative `1-h`. Zero context bits are impossible by the no-go, while one bit suffices, so freeze `ONE_BIT_BRANCH_MEMORY_MINIMAL_FOR_EQUIVARIANT_STRAIGHT_CONTINUATION` and `STRAIGHTNESS_ONE_BIT_MEMORY_CONTINUATION_LAW_ESTABLISHED_WITH_INITIAL_BRANCH_UNIDENTIFIED`.

This law cannot determine `b_0`: memory exists only after a branch has occurred. Previous donor/recipient relation is a coordinate-free representation equivalent to one bit for a fixed recipient. Ingress/orientation is not promoted from the allowed Stage-N algebraic inputs; it would be useful only if an exact frozen transformation law supplied a tau-odd two-state distinction. An upstream exact constraint can force a branch when its Boolean solution set is singleton, but is not necessary for one-bit straight continuation.

The continuation law is transverse-exchange covariant (`h,b` both complement), coordinate-permutation covariant in donor-relation form, and globally inversion covariant because `T_{k+1}=T_k` maps to `-T_{k+1}=-T_k`. No Euclidean distance, angle, norm, trig, shortest path, or visual straightness is used.

## Contextual Boolean selector family

Let `A(s)⊆{0,1}` be the exact legal bit set after completion legality and any exact local/upstream constraints. The canonical contextual partial selector is:

- `A=∅`: inconsistent/undefined;
- `A={0}`: `0`;
- `A={1}`: `1`;
- `A={0,1}` with previous bit `h`: `h` under straight continuation;
- `A={0,1}` without `h`: `SELECTOR_STILL_NONIDENTIFIED`.

Hence `UNIQUE_CONTEXTUAL_SELECTOR_FAMILY` holds on the explicit continuation domain, while `INITIAL_SELECTOR_STATUS=SELECTOR_STILL_NONIDENTIFIED`. No multibranch initial state is silently forced unique.

## Scalar/vector bridge and scale covariance

For scalar `5` in the square completion layer, legal endpoints `4,9` come from completion typing; Stage O does **not** identify which is realized, nor transfer the vector straightness-memory rule to scalar square collapse. The three-axis result only teaches the separation: completion set determines legality, exact higher constraints may couple bits, and context may resolve continuation without resolving initiation.

For completion scale `a>0`, take completed displacement layer `aZ`, recipient event `+a`, and symmetric unresolved transverse value `-a/2`. Then PREV/NEXT are `-a,0`, collapse is `-a+ab`, conservation again gives `b_1+b_2=1`, and transfer set is `{a(e_i-e_j):i!=j}`. Checker probes `a=1,2,5` and exact backgrounds around `10^36`; `(K-a,a,0)` and `(K,a,-a)` both sum exactly to `K`. Large background is coordinate/system scale only, not length, norm, probability, or selector strength.

## Checker / firewalls

Deterministic checker: `12834/12834 PASS`, failures `0`, digest `b960d3ca62ccb7453dfc4d1d1a8ed6c176d7f26cf6c732e9d2ebd3de1707deb7`.

Checker source SHA256 `fffd5d40895ab02c5e5b7afc38316b145adb10d66ed82d3deee4f10dd2bcca3c`, Git blob `4fcbcb72b4e52484d9bcaa53717d4e54b7c8523e`.

Checker output SHA256 `e00131833b7b4b0332232d4658c1c7a35b361967606b20ab8496d42a8d1c80ad`, Git blob `7c902195470929c3ebbcd76b122c62bbc6cc92cb`.

Hard negatives: no nearest rounding, endpoint argmax, arbitrary reward weights, ML fitting, path-language selector, physical probability, hidden label order, coordinate-name bias, randomized native selector, or use of straightness to choose the initial branch.

Final scientific boundary: `INITIAL_BRC_BRANCH_SELECTOR = NOT_ESTABLISHED_AT_SYMMETRIC_STATE_WITHOUT_EXTERNAL_OR_HISTORY_CONTEXT`.

After manifest/checkpoint and parent compare: `STOP_FOR_DRIVER_REVIEW`.
