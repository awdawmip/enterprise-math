# R059D Stage AS — Proof

Researcher: `EM-R059D-AS-6E2A91`

Task: `RS-R059D-STAGE-AS-GENERAL-RADIUS-SEGMENT-FOOTPRINT-TRIANGLE-FLIP-ESCAPE`

## 1. Typing

Let the signed native origin be `O_E=[+1]=[-1]`. Native zero does not exist. Use the auxiliary A2 vertex chart only for incidence. The six primitive directions are

`(1,0),(0,1),(-1,1),(-1,0),(0,-1),(1,-1)`.

For `r>=1`, `r` is an external primitive segment-unit count. A radius-r positive-axis anchor is reached by the straight chain

`(0,0),(1,0),...,(r,0)`

in the auxiliary chart; after `ENC_SIGNED`, the moved native coordinate has magnitude `r+1`. This is not an assertion that coordinate magnitude `r+1` is the segment length.

## 2. Exact carrier underdetermination

Consider an ordered simple primitive-edge chain

`P=(v_0=O_E,v_1,...,v_m=p)`.

The straight axis anchor has `m=r`.

Two pre-circle side-state lifts satisfy every mandatory Stage-B consistency rule.

### 2.1 Terminal-side lift

Store only

`(P,C_terminal)`

where `C_terminal` is one of the two elementary triangles incident to the terminal edge `[v_(m-1),v_m]`.

Each visible axis anchor has exactly two lifts. At `r=1` this is exactly the AR state `(e,C)`.

### 2.2 Edgewise strip lift

Store

`(P,C_1,...,C_m)`

with one incident side triangle for every primitive edge.

A straight radius-r axis anchor has `2^r` side lifts. At `r=1` it again reduces exactly to AR.

Both constructions are native-incidence-only, D6 covariant, reversal covariant, translation covariant, and prefix consistent on axis seeds. Neither reads AK orbit membership, AL A8, source angle, or the prior circle.

At `r=2`, the first model has 2 lifts over each visible anchor, while the second has 4. Hence they are not isomorphic over the visible-anchor projection. No frozen pre-circle observable distinguishes them. Therefore the general-radius segment carrier is underdetermined from `r>=2` onward.

## 3. Triangle flip grammar

Let one edge `[x,y]` of a chain bound an elementary triangle `{x,y,z}`.

If inserting `z` preserves the declared simple-chain condition, the boundary flip

`[x,y] -> [x,z],[z,y]`

is a local `1->2` move. It preserves the two endpoints of the replaced subpath and changes chain edge count by `+1`.

Conversely, whenever consecutive edges `[x,z],[z,y]` bound an elementary triangle and replacing them by `[x,y]` preserves simplicity, the local `2->1` move changes edge count by `-1` and preserves subpath endpoints.

A terminal pivot is different. For terminal edge `[x,y]` and side triangle `{x,y,z}`, replacing only the terminal edge by `[x,z]` changes the free endpoint from `y` to `z` and keeps chain edge count unchanged. At `r=1`, with `x=O_E`, this is exactly the AR incidence turn.

Thus the user's earlier up/down intuition has a literal realization for chain cardinality:

- `1->2` is `+1` raw edge-count drift;
- `2->1` is `-1` raw edge-count drift.

A paired `1->2` and `2->1` can have zero net edge-count drift, but incidence does not select which sites are to be paired or synchronized. No general-radius axis-completion law follows from one-cell incidence alone.

## 4. Length underdetermination

Two source-free D6-invariant observables agree on all radius-r axis anchors and at `r=1` but disagree on a legal triangular footprint.

### 4.1 Chain cardinality

`L_chain(P)=|E(P)|`.

On a straight radius-r axis chain, `L_chain=r`. A `1->2` flip changes it by `+1`; a `2->1` flip by `-1`; a terminal pivot leaves it unchanged.

### 4.2 Endpoint displacement

`L_disp(P)=d_primal(O_E,p)`.

On every radius-r axis anchor, `L_disp=r`. All endpoint-preserving `1<->2` flips leave it unchanged. Terminal pivots can change it.

### 4.3 Exact witness

In the auxiliary chart, the two-edge path

`(0,0)->(1,0)->(0,1)`

uses two primitive edges, so `L_chain=2`, but its free endpoint `(0,1)` is one primitive graph step from the origin, so `L_disp=1`. The direct third edge `(0,0)->(0,1)` has the same free endpoint.

Both observables are native and agree on the straight anchor calibration. Existing axioms do not identify either one as the carrier-independent physical/native segment length. Hence a unique general-radius pre-circle length semantics is not derived.

## 5. Candidate-relation dependence on length typing

If the ordered-chain model is adopted and fixed length means `L_chain=r`, a raw `1<->2` move leaves the fixed class and can be excluded by a pre-circle native invariant. Terminal `1->1` pivots remain.

If fixed length instead means `L_disp=r`, all endpoint-preserving `1<->2` moves remain legal, while a terminal pivot is legal only when its new endpoint stays at primal distance `r`.

Therefore the transition relation itself is not fixed before the length semantics is fixed.

## 6. Escape-score underdetermination

Two native D6-covariant scores already disagree at radius 2.

Take the straight chain

`(0,0)->(1,0)->(2,0)`.

Expanding the inner edge through `U(0,0)` and expanding the outer edge through `U(1,0)` both leave the free endpoint at `(2,0)`. Hence a free-endpoint shell score assigns both score 2.

AQ's exact dual-cell shell gives

`SHELL(U(i-1,0))=2(i-1)`.

Thus `U(0,0)` has shell 0 while `U(1,0)` has shell 2. A newly-entered-cell shell score strictly prefers the outer expansion.

Both scores are source-free and D6 covariant. Therefore no unique segment escape score is implied by current pre-circle axioms.

## 7. Diagnostic Arm A: fixed chain cardinality

Adopt `TERMINAL_SIDE_CHAIN` and fixed `L_chain=r`. Then the only elementary one-cell move retained in the fixed class is the terminal `1->1` pivot.

For a straight axis seed, let the terminal edge direction be `k mod 6` and the retained side sign be `d in {+1,-1}`. Each pivot rotates the terminal edge around the fixed penultimate vertex by one direction step `d`.

At `r=1`, the prefix contains only the origin. The terminal edge visits all six directions and returns after six pivots, exactly reproducing AR.

For every `r>=2`, the prefix also contains `v_(r-2)`, the neighbor of `v_(r-1)` in direction `k+3d`. Starting at direction `k`, the first two pivots reach `k+d` and `k+2d`. The third proposed pivot would place the terminal endpoint at `v_(r-2)`, already in the prefix. This violates the simple-chain carrier and is rejected.

Thus every axis lift at `r>=2` has exactly two legal transitions and then terminates. Across six axis orientations and two sides, J=0,1,2 each contain 12 distinct diagnostic states, 36 total, and no cycle.

## 8. Diagnostic Arm B: raw strip flips

Adopt the edgewise side strip before choosing chain cardinality as a hard fixed-length invariant. On a straight radius-r axis seed, each of the r primitive edges has a stored-side `1->2` expansion. Every such expansion preserves the free endpoint on primal shell r. The first terminal tangential pivot also leaves the endpoint on shell r.

Therefore under `FREE_ENDPOINT_SHELL`, all these candidates are tied maximizers and must survive. Every expansion has `L_chain=r+1`. Hence if chain cardinality is later interpreted as primitive segment length, all-path fixed-length closure has already failed at J=1.

The purpose of this arm is not to define a preferred dynamics. It is an exact first-divergence counterarm showing that another equally pre-circle-compatible state/score typing retains length-drift branches that Arm A excludes.

## 9. Intrinsic closure consequence

The two diagnostic arms have incompatible dynamics:

- Arm A: r=1 closes; every r>=2 axis lift blocks after two pivots;
- Arm B: raw length-increasing farthest-tied branches survive at the first step.

Because the state carrier, length semantics, and escape score are themselves underdetermined, there is no canonical general-radius all-path graph on which to state the preferred closure theorem. One cannot select the old circle-compatible arm without violating the circularity firewall.

## 10. AL support arm

After the primary theorem is frozen, add the accepted support cap `K_E(r)` with A8 disabled.

For the outer positive-axis edge `[(r-1,0),(r,0)]`, one legal upper `1->2` expansion uses third vertex `(r-1,1)`. In the accepted first-sector support certificate,

`q(r-1,1)=r^2-r+1`

and

`SUP(r-1,1)=9r^2-18r+21 <= 9r^2`

for every `r>=2`.

Thus the immediate chain-count-increasing branch lies inside the support carrier. The cap does not choose a carrier, length observable, or escape score and does not repair the underdetermination.

## 11. Post-freeze circle comparison

At `r=1`, the terminal-side fixed-chain arm is exactly AR and therefore has the accepted AP/AK/AL visible radius-1 endpoint cycle.

At `r>=2`, Arm A has no cycle while Arm B contains extra raw drift branches. Hence neither all-path diagnostic object equals the accepted canonical circle. Whether a canonical-circle path embeds somewhere in a wider footprint graph is not established and is not used to select a model.

## 12. Final theorem status

Stage AS proves the exact stronger countertheorem:

`MULTIPLE_INEQUIVALENT_GENERAL_RADIUS_SEGMENT_LIFTS_SURVIVE__PRE_CIRCLE_LENGTH_AND_ESCAPE_LAW_UNDERDETERMINED__TRIANGLE_FLIP_CHAIN_DRIFT_PROVED`.

The preferred general-radius all-path fixed-length closure theorem is therefore not justified from the currently frozen native inputs. The missing object is an independent Enterprise-native principle selecting the long-segment ontology and its length/escape semantics; it cannot be supplied by old-circle fit, source geometry, or AL A8.
