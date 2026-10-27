# R043-C1 — Native Slot Completion / G0 Injectivity Return

Status: `DONE / RETURNED / PI NONINJECTIVE / SHIELDED-CAVITY FUTURE EQUIVALENCE PROVED / NOT CANONICAL`

Researcher-ID: `EM-R043C1-7D91A4`  
Task: `RS-R043C1-NATIVE-SLOT-COMPLETION-G0-INJECTIVITY`  
Taskbook: `research_tasks/R043C1_NATIVE_SLOT_COMPLETION_G0_INJECTIVITY_20260824.md`  
Parent R043 owner head: `566babdb8008db901f8bd057c01a24412cc1495a`  
Current taskbook-policy digest: `sha256:9c1f03a5086432f83d1a3821893be5589124293bc5be5b14d4b7e196220271c7`

Primary verdict:

`PI_NONINJECTIVE_BUT_BOOLEAN_FUTURE_EQUIVALENT_AT_TESTED_SCOPE`

The terminal label is intentionally weaker than one theorem established below: for the explicit shielded-singleton-cavity collision family, Boolean/G0 future equivalence is proved for **all finite addition-only horizons**, not merely bounded by computation.

## 1. Result in one line

The forgetful map

`pi: K_partial -> G0`

is not globally injective in either frozen FCC or frozen HCP world. A deep singleton cavity can be relocated inside the same finite occupied base without changing the abstract weighted current-frontier graph. The relative embedded position retained by `K_partial` changes, but that position is dynamically shielded from the declared addition-only surface future.

Thus the parent reconstruction conjecture `R043-C1_NATIVE_SLOT_CUT_RECONSTRUCTION` is **killed as a raw native-embedding injectivity statement**, while the stronger operational possibility

`ker(G0) subseteq ker(all finite Boolean surface futures)`

remains alive and is positively verified on the collision family by theorem.

## 2. Exact shielded-cavity factorization lemma

Let `Lambda` be either frozen 12-regular native contact world. Let `R` be a finite occupied set, and let `h in R` satisfy

`N(h) subseteq R`.

Assume `C = R \ {h}` is connected. Then:

1. `h` becomes a frontier cell of `C`;
2. `k_C(h)=12`;
3. `h` has no frontier-frontier edge, because all 12 of its neighbors remain occupied;
4. every old outer-frontier cell of `R` has the same weight after removing `h`, because no outer-frontier cell is adjacent to `h`;
5. no other frontier cell is created.

Therefore exactly

`F(C) = F(R) disjoint_union {h}`

and

`G0(C) ~= G0(R) disjoint_union isolated_vertex(weight=12)`.

This is a direct contact-set identity; no metric, radius, Euclidean distance, continuum object, or floating-point argument is used.

### Consequence: cavity relocation collision

If the same finite base `R` contains two such cells `h1,h2`, both `R\{h_i}` are connected, and the two embedded frontier states are not related by a declared native symmetry, then

`C1=R\{h1}`, `C2=R\{h2}`

are globally realizable non-equivalent `K_partial` completions with exactly the same abstract weighted `G0`.

This passes all three C1 gates:

- `LOCAL_INCIDENCE_FEASIBLE`: yes, because the weights come from actual clusters;
- `NATIVE_SLOT_CONSISTENT`: yes, because inward slots are actual frozen contact slots;
- `GLOBALLY_REALIZABLE`: yes, because the witness clusters are explicit finite connected occupied sets and their frontiers are reconstructed exactly.

## 3. FCC exact witness, N=20

Use the frozen FCC contact steps, and define the common 21-cell base

```text
R_FCC = {
(-1,-1,0),(-1,0,-1),(-1,0,1),(-1,1,0),
(0,-2,-2),(0,-1,-1),(0,-1,1),(0,0,0),(0,1,-1),(0,1,1),(0,2,0),
(1,-1,0),(1,0,-1),(1,0,1),(1,1,0),(1,2,-1),(1,2,1),
(2,0,0),(2,1,-1),(2,1,1),(2,2,0)
}.
```

Set

`h1=(0,0,0)`, `h2=(1,1,0)`.

Both are native-adjacent and both have all 12 neighbors inside `R_FCC`. Define

`C1=R_FCC\{h1}`, `C2=R_FCC\{h2}`.

Exact certificate:

- `|C1|=|C2|=20`;
- both are connected;
- common outer frontier `|F(R_FCC)|=60`;
- each cluster frontier has 61 vertices;
- the hole vertex has weight 12 and frontier degree 0;
- `S(C1)=S(C2)=136`;
- each `G0` has 61 vertices and 144 edges;
- under the explicit isomorphism that fixes every outer-frontier vertex and maps `h1 -> h2`, all weights and edges agree exactly;
- the embedded frontier point sets are **not** congruent under the frozen 48 FCC native symmetries plus translations;
- the occupied clusters are likewise not congruent.

Hence `pi` is not injective in FCC.

## 4. HCP exact witness, N=20

Use the frozen HCP contact relation, and define

```text
R_HCP = {
(-1,0,-1),(-1,0,0),(-1,0,1),(-1,1,0),
(0,-2,-1),(0,-1,-1),(0,-1,0),(0,-1,1),(0,0,-1),(0,0,0),(0,0,1),(0,1,0),
(1,-1,-1),(1,-1,0),(1,-1,1),(1,0,-1),(1,0,0),(1,0,1),(1,1,0),
(2,-1,0),(2,0,0)
}.
```

Set

`h1=(0,0,0)`, `h2=(1,0,0)`.

Again all 12 neighbors of each hole candidate lie in the common base. For

`C1=R_HCP\{h1}`, `C2=R_HCP\{h2}`,

the exact certificate is:

- `|C1|=|C2|=20`;
- both are connected;
- common outer frontier `|F(R_HCP)|=60`;
- each cluster frontier has 61 vertices;
- hole weight 12, hole frontier degree 0;
- `S(C1)=S(C2)=134`;
- each `G0` has 61 vertices and 151 edges;
- identity on the outer frontier plus `h1 -> h2` is an exact weighted-graph isomorphism;
- the embedded frontier point sets are not congruent under the frozen 24 HCP symmetry representatives plus declared translations;
- the occupied clusters are not congruent.

Hence `pi` is not injective in HCP either.

The inherited HCP crystallographic-completeness caveat remains the same as R039/R043: the certificate is relative to the frozen declared HCP symmetry quotient. The two states are already separated under that task-authorized quotient.

## 5. All-horizon future equivalence of the collision family

The same construction also gives an exact bisimulation argument.

For `C_i=R\{h_i}` there are only two action types.

### A. Outer action

Choose `x in F(R)`. Then

`C_i + x = (R + x) \ {h_i}`.

Since `N(h_i) subseteq R subseteq R+x`, the hole remains fully shielded after the action. Applying the factorization lemma again gives

`G0(C_i+x) ~= G0(R+x) disjoint_union isolated_vertex(weight=12)`.

Thus the same identity-on-outer-frontier / hole-swap correspondence survives every outer action.

### B. Hole action

Choosing the isolated weight-12 action fills the cavity:

`C_i + h_i = R`.

Both states collapse to the exact same occupied base and hence the same `G0`.

### Induction

After every matched action, either the hole has been filled and the two states coincide, or it remains a shielded isolated weight-12 frontier component over a common evolved outer base. Therefore the relation is preserved step by step for every finite addition sequence.

Consequently the two witness states have isomorphic full abstract-`G0` transition trees, so in particular

`B_h(C1)=B_h(C2)`

for every finite Boolean horizon `h` in the declared addition-only surface language.

This is theorem-level for the shielded-cavity family, not a bounded enumeration inference.

## 6. Why this did not appear in the N<=8 atlas

The parent R043 finite result remains correct. The complete frozen FCC/HCP atlases through `N<=8` have no same-`G0` collision. The present witness first appears at `N=20` in the explicit construction used here, so there is no conflict.

No claim is made that `N=20` is the globally minimal same-`G0` collision over all possible mechanisms. It is the smallest explicit realizable collision found in this task. Within the present adjacent-two-hole/common-base construction, the two 13-cell closed neighborhoods overlap in the two centers plus four common neighbors, giving a 20-cell symmetric core; one extra asymmetry-breaking occupied cell yields the 21-cell base and hence the 20-cell one-hole states.

## 7. Exact change in the reconstruction problem

The C1 injectivity route is now closed negatively:

`K_partial -> G0` forgets at least the relative native placement of dynamically shielded frontier components.

But that forgotten information is not automatically future information. The explicit collision lies inside the kernel of every finite Boolean future.

Therefore the correct next mother question is no longer raw reconstruction of all native slot/embedding identity. It is a **future-relative quotient** question:

> after quotienting shielded independent frontier-component placement, does abstract `G0` determine its own successor transition system for every reachable state?

Equivalently, search for a same-`G0` collision whose hidden completion changes a rooted successor-extension orbit. A collision caused only by relocation of permanently shielded components is a negative control, not a `G0`-future failure.

A useful next split is:

1. `DISCONNECTED_SHIELDED_COMPONENT_COLLISIONS` — now structurally understood and future-harmless;
2. `CONNECTED_OR_INTERACTING_FRONTIER_COLLISIONS` — still the high-value route for killing stationary `G0` sufficiency;
3. `FUTURE_EQUIVALENT_NONINJECTIVITY` — should be quotiented rather than repaired by reintroducing all slot coordinates.

## 8. Machine certificate

Frozen with this return:

- `research_artifacts/R043C1_slot_completion/cavity_collision_check.py`;
- `research_artifacts/R043C1_slot_completion/CAVITY_COLLISION_CERT.json`.

The checker uses only exact integer contact relations and the frozen finite symmetry actions. It verifies in each world:

- both holes have all 12 native neighbors in the common base;
- both one-hole clusters are finite and connected;
- frontier factorization is exact;
- the explicit same-`G0` isomorphism preserves every vertex weight and frontier edge;
- embedded frontier and occupied cluster native-congruence tests fail;
- all 60 matched current outer actions preserve same-`G0` correspondence;
- filling the hole sends both states to the same base.

The all-horizon conclusion uses the structural induction in Section 5; the 60-action check is implementation validation.

## 9. Tool / method ownership

No new generic graph-isomorphism, CSP, quotient, or BRC tool family is claimed.

Reused method families:

- finite collision / fiber separation;
- finite native symmetry quotient;
- operation-safe future equivalence / recoalescence reasoning.

Surface-specific new content is the **shielded-cavity relocation factorization** and its consequence for the `K_partial -> G0` forgetful map.

## 10. Weakest supported statement

The strongest unsupported statement remains forbidden: this task does **not** prove global stationary sufficiency of `G0`.

The weakest exact returned statement is:

> In both frozen FCC and HCP worlds there exist explicit finite connected `N=20` clusters with non-equivalent native slot-cut frontier embeddings but exactly isomorphic abstract weighted `G0`. Thus raw global injectivity of `pi:K_partial->G0` fails. For the constructed shielded-singleton-cavity collision family, the lost native placement is provably irrelevant to every finite addition-only Boolean surface future.

No Foundation or canonical theorem promotion is requested by this research return.
