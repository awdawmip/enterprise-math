# R043-C2 — G0 Future Sufficiency Modulo Shielded Components Return

Status: `DONE / RETURNED / REDUCED_TO_CONNECTED_INTERACTING_EXTENSION_LEMMA / NOT CANONICAL`

Researcher-ID: `EM-R043C2-4B73D9`  
Task: `RS-R043C2-G0-FUTURE-SUFFICIENCY-MODULO-SHIELDED-COMPONENTS`  
Taskbook: `research_tasks/R043C2_G0_FUTURE_SUFFICIENCY_MODULO_SHIELDED_COMPONENTS_20260824.md`  
Parent C1 head: `018dbcc3ee68862af0d834683b20d6211eed1192`  
Driver base: `main@501c2e35cb04d176c5a2d15bc0ee29d61c4a6be4`

Primary verdict:

`REDUCED_TO_CONNECTED_INTERACTING_EXTENSION_LEMMA`

No global stationary theorem for `G0` is promoted, and no harmful same-`G0` collision is claimed.

## 1. Exact new theorem — complement-component factorization

Let `Lambda` be either frozen FCC or frozen HCP contact graph. Let `C` be any finite connected occupied set and let

`U = Lambda \ C`

be the current unoccupied graph. Write its connected components as

`U = disjoint_union_i Omega_i`.

For each component define its current frontier slice

`F_i = F(C) intersect Omega_i`.

Then:

### R043C2-T1 — component separation

1. `F(C)=disjoint_union_i F_i`.
2. There is no current frontier edge between `F_i` and `F_j` for `i!=j`. If two unoccupied frontier vertices were adjacent, they would lie in the same connected component of `U`.
3. Hence abstract weighted `G0(C)` is a graph-disjoint union of the induced weighted frontier slices.

### R043C2-T2 — one-component locality of addition

Choose an action `x in F_i` and set `C'=C union {x}`. Then

`U' = U \ {x}`.

Deleting one vertex from `Omega_i` may keep it connected or split it into several components, but it cannot change or merge any `Omega_j`, `j!=i`.

Moreover no vertex of `F_j` is adjacent to `x`: such an edge would already connect `Omega_i` and `Omega_j` in `U`. Therefore every frontier vertex, frontier edge and attachment weight belonging to every other `Omega_j` is exactly unchanged by the action.

So one addition modifies only the unoccupied component containing the chosen action.

### R043C2-T3 — all-horizon asynchronous factorization

By induction over an addition sequence, descendants of distinct current unoccupied components remain dynamically independent. Operations in one component can split that component but can never merge it with another current component, because addition only deletes vertices from `U` and never adds unoccupied edges or vertices.

Thus the declared addition-only transition system factorizes asynchronously over current unoccupied components. Relative native placement between **different** `Omega_i` is future-irrelevant once each component's own rooted deletion/erosion transition system is fixed.

This theorem is graph-theoretic and does not depend on metric radius, Euclidean geometry, continuum surface notions, or bounded animal enumeration.

## 2. C1 is a strict special case

The C1 shielded singleton cavity is a finite unoccupied component

`Omega={h}`.

Its frontier slice is one isolated weight-12 vertex and its only internal action deletes that component. Relocating it changes `K_partial` embedding but not the per-component transition system. C1's all-horizon bisimulation is therefore the one-vertex case of R043C2-T3.

The same conclusion extends immediately to relocation/permutation of arbitrary distinct unoccupied components **provided their own rooted transition systems are preserved**. Raw native placement among independent components is not information that a minimal addition-only future carrier must retain.

## 3. Important boundary — G0 components are not yet proved to equal unoccupied components

R043C2-T1 gives only

`each connected component of G0 lies inside one Omega_i`.

It does **not** prove the converse: one connected unoccupied component `Omega_i` could, in principle, have a current frontier slice `F_i` whose induced `G0` is disconnected. Those disconnected frontier pieces may be joined through deeper currently non-frontier unoccupied cells.

This distinction is now the sharpest latent-interaction obstruction.

If the same abstract `G0` admits two realizations in which disconnected frontier pieces are grouped differently — separate `Omega` components in one realization but the same `Omega` in another — then relative placement may become future-relevant. In the same-`Omega` realization, future additions can expose the deeper connection; in the separate-components realization no sequence of additions can ever merge them.

Therefore a harmful C2 counterexample can arise in exactly two ways:

1. **component-grouping ambiguity** — `G0` does not determine which disconnected frontier pieces belong to the same unoccupied component;
2. **single-component rooted-extension ambiguity** — even after fixing one `Omega_i`, its weighted current frontier does not determine the rooted deletion/erosion successor.

A connected-`G0` collision is automatically in case 2 and remains the cleanest high-value negative witness.

## 4. Corrected future-relative state diagram

The operational hierarchy is now

```text
native K_partial
   |
   | forget future-irrelevant relative placement of distinct unoccupied components
   v
per-unoccupied-component rooted transition systems
   |
   | current visible projection
   v
abstract weighted G0
```

C1 proves the first arrow is non-injective. C2-T3 proves that at least the relative placement part of that non-injectivity is future-safe.

The only unresolved arrow is whether current abstract `G0` reconstructs the required component grouping and each component-local rooted extension.

## 5. Finite pressure checks — evidence only

These checks are diagnostic and are not used as proofs of the global reduction.

### FCC random induced-path pressure

A deterministic-seed random pressure run generated `30,000` induced occupied paths with sizes sampled from `N=9..26`.

- exact same-`G0` encounters under the strong invariant plus exact weighted graph isomorphism: `25`;
- all 25 were native-congruent under the frozen 48 FCC point symmetries plus translations;
- non-native same-`G0` pair: `0`;
- harmful rooted-successor witness: `0`.

This is not exhaustive and makes no probability claim. It only failed to produce an exterior interacting counterexample cheaply.

### Small deep-cavity pressure

Starting from the 13-cell closed native neighborhood of one interior void cell and adding two void cells gives:

- FCC: `38` frozen-symmetry void shapes at size 15; `6` exact current cavity-boundary `G0` collisions found; all collided pairs had isomorphic full induced void graphs.
- HCP: `123` frozen-symmetry void shapes at size 15; `54` exact current cavity-boundary `G0` collisions found; all collided pairs had isomorphic full induced void graphs.

No claim is made that these collisions exhaust rooted identifications at larger cavity size. Their role is only to show that the first deep-cavity ambiguities encountered are still compatible with the component-local deletion picture rather than immediately exposing a harmful future split.

## 6. What is now proved safe to forget

For the declared addition-only Boolean language, one may forget **relative native placement between distinct current unoccupied components**, provided their internal rooted transition systems are held fixed.

This is strictly stronger than C1's singleton-hole statement and strictly weaker than global `G0` sufficiency.

Do not interpret it as permission to forget:

- grouping of disconnected frontier pieces into unoccupied components;
- hidden within-component connectivity through deeper exterior cells;
- rooted successor-extension data inside one component;
- multiplicity, provenance, probability or amplitude semantics outside the task language.

## 7. Exact remaining lemma

The global mother question is reduced to the following FCC/HCP-specific statement.

### R043C2-L1 — interacting-component extension lemma

For every finite connected reachable occupied cluster and every unoccupied component `Omega`, determine whether the abstract weighted induced graph on its current frontier slice, together with a rooted action orbit, uniquely determines the successor weighted frontier decomposition generated by deleting that action from `Omega`.

A sufficient positive route must also show that abstract `G0` determines the partition of its disconnected visible pieces by `Omega`, or prove that any ambiguity of this partition is future-equivalent.

A negative route needs only one globally realizable pair with:

```text
G0(C) ~= G0(D),
(C,x) and (D,y) matched as rooted abstract G0 states,
but G0(C+x) !~= G0(D+y),
```

or the first finite `B_h` split after one-step recoalescence.

This is strictly smaller than raw `K_partial` reconstruction and strictly sharper than naive larger-`N` animal census.

## 8. Regression matrix

| surface | required behavior | result |
|---|---|---|
| R043 `N<=8` atlas | no raw same-G0 collision | inherited PASS |
| C1 FCC `N=20` cavity relocation | raw same-G0 / native-non-equivalent | PASS / consumed |
| C1 HCP `N=20` cavity relocation | raw same-G0 / native-non-equivalent | PASS / consumed |
| C1 matched outer/hole actions | reject as future failure | PASS by C1 theorem |
| C2 distinct-unoccupied-component action | leave all other components unchanged | PROVED globally by T2 |
| C2 all-horizon component independence | no cross-component merge under addition | PROVED globally by T3 |
| interacting same-G0 successor split | find or kill | OPEN |

## 9. Tool / ownership classification

Reused:

- frozen FCC/HCP contact relations and symmetry quotients;
- exact graph-isomorphism / rooted-orbit concepts;
- future-safe quotient / operation-closure semantics.

New surface-specific content:

- complement-component factorization of addition-only native surface dynamics;
- separation of harmless relative component placement from potentially harmful component-grouping ambiguity;
- exact reduction to a single-unoccupied-component rooted extension problem.

No new generic graph, quotient, SAT/CSP or BRC framework is claimed.

## 10. Weakest supported statement

> In both frozen FCC and HCP worlds, addition-only surface dynamics factorizes exactly over connected components of the current unoccupied graph. Relative placement of distinct unoccupied components is therefore permanently irrelevant to the declared future once their own rooted transition systems are fixed. Raw `K_partial -> G0` noninjectivity from such placement is harmless. Global stationary sufficiency of `G0` remains open only at the component-grouping / single-component rooted-extension layer.

No Foundation or canonical theorem promotion is requested.
