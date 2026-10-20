# R043 — Native Surface Frontier Reconstruction and Stationary Slot-Cut Carrier

Status: `SEMANTIC_CHECKPOINT / G0_BOUNDED_SURVIVAL / SLOT_CUT_STATIONARY_POSITIVE / NOT_CANONICAL`  
Researcher-ID: `EM-R043-8C2F71`  
Task: `RS-R043-NATIVE-SURFACE-FRONTIER-RECONSTRUCTION-MARKOV-CARRIER`  
Taskbook source: `41afbdf37f70b1fc484f7a49bc68880826ead31d`  
Frozen R041 dependency: `688661e76255b3e86df6d5c69695f2932b650740`  
Frozen R039 dependency: `c484fb85385b8498982aaa939171957588c836d7`  
CI: `CI_NOT_REQUIRED_FOR_RESEARCH`

## 0. Verdict

R043 does **not** promote the weighted abstract current-frontier graph `G0` to an unbounded theorem. It survives every exact bounded collision test required by the taskbook, including cross-size collisions through `N<=8` in both frozen worlds, and its action-rooted recursive closure survives exactly through parent size `N<=7` because every child lies in the `N<=8` injective atlas.

The structural result is instead a stronger representation theorem in a different direction:

> The native slot-labeled contact cut admits a fixed-form, frontier-only, recursively exact Markov carrier `K∂` for addition-only surface dynamics. It stores no explicit `L1` and no deep interior provenance. Pair-overlap, shared-future hypergraph, `L1`, and `M3` are derivable on demand from `K∂` and the frozen native contact relation.

Thus explicit exterior depth **does not have to grow with horizon**. R041's `M_h` remains an exact horizon-indexed carrier, but it is not a lower bound on state depth once native slot/embedding identity is retained in the current interface.

The remaining sharp question is now a single reconstruction problem:

```text
π : K∂ -> G0
```

where `π` forgets native slot/embedding identity and retains only `S`, the abstract induced frontier graph, and weights `k_C(x)`.

R043 verifies that `π` is injective on every frozen FCC/HCP cluster class through `N<=8`, but gives neither a global structural proof nor a collision beyond that range. This is the only unresolved step between the proved stationary `K∂` carrier and the stronger conjecture that `G0` itself is stationary Markov.

---

## 1. Frozen inputs consumed without re-owning them

R039 is used as frozen authority for:

- native surface as the oriented contact cut `δ(C)` with native contact-slot labels preferred;
- the frozen FCC/HCP contact relations and symmetry quotients;
- the exact connected-cluster atlas counts through `N<=8`;
- the scalar / histogram / local-type correlation-debt hierarchy.

R041 is used as frozen authority for:

- `R2bar -> B2` exact;
- `R2bar -/-> B3` first at `N=6` in both worlds;
- exact one-layer-shaved carriers `M_h`;
- `M3 = weighted induced graph on L0 union L1` exact for `B3`;
- the earlier bounded `G0` no-collision result through FCC `N<=7` and HCP `N<=6`.

R043 re-materializes the frozen atlas only to visit every exact class with an independent `G0` canonicalizer / collision filter. Atlas cardinalities and R039/R041 theorems are not re-claimed as new results.

---

## 2. R043-T1 — bounded `G0` injectivity through `N<=8`

For each frozen cluster `C`, define

```text
G0(C) = (S(C), weighted induced contact graph on F(C)),
weight(x) = k_C(x).
```

The independent R043 checker uses a weighted Weisfeiler-Lehman digest only as an **isomorphism-invariant bucket filter**. Any exact weighted-graph isomorphism must land in the same digest bucket. Every non-singleton bucket would be sent to an exact weighted graph-isomorphism checker.

There were no non-singleton buckets at all.

### FCC

Frozen class counts:

```text
N:       1  2  3   4    5     6      7       8
states:  1  1  4  20  131  1211  12734  144158
```

At `N=8`:

```text
144158 states
144158 distinct G0 keys
0 WL duplicate buckets
0 exact collision groups
```

Across **all sizes `1<=N<=8`**:

```text
158260 cluster classes
158260 distinct G0 keys
0 cross-size collisions
```

### HCP

Frozen class counts:

```text
N:       1  2  3   4    5     6      7       8
states:  1  2  9  57  460  4641  50353  575375
```

At `N=8`:

```text
575375 states
575375 distinct G0 keys
0 WL duplicate buckets
0 exact collision groups
```

Across **all sizes `1<=N<=8`**:

```text
630898 cluster classes
630898 distinct G0 keys
0 cross-size collisions
```

Hence on the declared bounded atlas,

```text
ker(G0) = exact frozen cluster-class equality.
```

Consequently `G0 -> B3` is exact on that finite atlas (indeed every future observation is constant on a singleton `G0` class there). This is a bounded theorem, **not** a reconstruction proof for arbitrary finite clusters.

---

## 3. R043-T2 — bounded action-rooted recursive closure through parent `N<=7`

A stationary abstract update must respect weighted-frontier automorphisms. If an automorphism of `G0(C)` carries action vertex `x` to `y`, then an isomorphism-covariant update requires

```text
G0(C+x) ~= G0(C+y).
```

R043 checks this adversarially without enumerating the full automorphism group:

1. compute node-level weighted WL subgraph signatures on `G0(C)`;
2. every exact automorphism-related pair must lie in the same node-signature bucket;
3. compare the child `G0` digest for every vertex in each such bucket;
4. if different child digests occur, run exact rooted graph isomorphism to decide whether the pair is a genuine automorphism orbit split.

Results:

```text
FCC parents N<=7: 0 rooted candidate buckets with different child G0 keys
HCP parents N<=7: 0 rooted candidate buckets with different child G0 keys
```

This is exact in the checked range, not merely WL evidence: every child has size `<=8`, and R043-T1 proves the child `G0` key is injective on the complete child atlas. Therefore equal child keys cannot hide a non-isomorphic reachable child state in this range.

So the stronger action-rooted closure candidate also survives through parent `N<=7` in both worlds.

Again, this is bounded survival, not the missing unbounded structural proof.

---

## 4. Reconstruction theorem route: what would be sufficient

R041's `G0` omits exactly the native information needed to identify which missing contact slots are inward occupied slots and which lead to not-yet-frontier exterior cells.

The right comparison object is not full `M3`; it is a current-interface carrier derived from R039's slot-labeled contact cut.

For the frozen native contact world, let each contact slot `s` at a cell `x` have target `T(x,s)`. Define

```text
K∂(C) = (coherently native-embedded frontier F(C), I_C)
I_C(x) = { s : T(x,s) in C }.
```

`K∂` retains:

- the current frontier and its coherent native embedding / slot frame, up to the declared world symmetry;
- for every frontier vertex, exactly which native slots point inward to occupied cells.

It does **not** retain:

- explicit `L1` vertices;
- any deeper exterior layer;
- deep interior cells or their provenance.

The R039 scalar is redundant inside this state:

```text
S(C) = sum_{x in F(C)} |I_C(x)|.
```

The weighted graph is the forgetful quotient

```text
π(K∂(C)) = G0(C),
weight(x)=|I_C(x)|,
```

with frontier-frontier adjacency read from the native embedding.

The global `G0` conjecture is therefore equivalent to asking whether this forgetful map is injective up to declared symmetry / future equivalence on all reachable interfaces.

---

## 5. R043-T3 — stationary slot-cut update theorem

Let `x in F(C)` be the chosen addition action. From `K∂(C)` alone define

```text
U_x = {
  T(x,s) :
  s not in I_C(x),
  T(x,s) not in F(C)
}.
```

These are exactly the cells that become newly exposed when `x` is occupied.

Then

```text
F' = (F - {x}) union U_x.
```

For every old frontier vertex `y != x`,

```text
I'(y) = I(y) union {slot_y(x)}   if y~x,
I'(y) = I(y)                     otherwise.
```

For every new vertex `z in U_x`,

```text
I'(z) = {slot_z(x)}.
```

### Proof

For `z in U_x`, the slot from `x` to `z` is not inward, so `z` was not occupied. Also `z` was not in the old frontier. If `z` had any occupied neighbor before the action it would already have been in `F(C)`, contradiction. Therefore after adding `x`, its unique occupied neighbor is `x` and `I'(z)` is the singleton inward slot to `x`.

Every old frontier vertex remains outside the cluster and remains adjacent to its previous occupied neighbor(s); if it contacts `x`, exactly one new inward slot is added. No cell not adjacent to `x` can become newly frontier after adding only `x`.

Thus the formulas reconstruct exactly the direct carrier of `C union {x}`:

```text
K∂(C), x  ->  K∂(C union {x}).
```

No omitted exterior layer and no interior cluster query is used.

By induction, `K∂` is a fixed-form stationary Markov carrier for every finite addition-only horizon in the frozen FCC/HCP worlds.

This proves H3 `FRONTIER_STATIONARY_MARKOV` for the slot-cut frontier state and kills the strong form of H8 claiming that exact state relation depth must grow explicitly with horizon.

### Executable checks

The direct update identity was checked against independently reconstructed successor carriers for every action from every frozen class through `N<=6`:

```text
FCC through N<=6:  52380 actions, 0 mismatches
HCP through N<=6: 198983 actions, 0 mismatches
```

The theorem itself is the direct set/slot identity above; the bounded checks are implementation validation rather than the proof.

---

## 6. R043-T4 — `L1`, pair overlap, hypergraph, and `M3` are derived from `K∂`

From `K∂`, every neighbor target of every frontier vertex is generable from the frozen native contact relation. A generated target is classified as:

- old frontier if it is already in `F`;
- occupied if its source slot is in `I(x)`;
- otherwise a genuine `L1` cell.

Therefore `K∂` reconstructs exact embedded `L1` without storing it.

Consequently it reconstructs on demand:

```text
O2(x,y) = # { z in L1 : z~x and z~y },
```

and the shared-future multihypergraph

```text
H1(C) = { (z, N(z) intersect F) : z in L1 }.
```

It also reconstructs every `L1-L1` contact and hence the complete R041 `M3` graph.

So the hierarchy is not only

```text
G0 < pair-overlap < shared-future hypergraph < M3.
```

There is a cross-cutting stationary representation:

```text
K∂ -> G0
K∂ -> O2
K∂ -> shared-future hypergraph
K∂ -> M3
K∂ + action -> successor K∂.
```

The pair/hypergraph objects remain useful *diagnostic residuals* if one insists on the abstract unlabeled `G0` representation, but they are not required as stored exterior depth in a native slot-aware carrier.

### Hypergraph identity negative control

A shared-future carrier used for exact successor-graph reconstruction must be a multihypergraph / identity-aware object, not a set of distinct frontier subsets. Already for the HCP singleton, six singleton-frontier subsets occur twice among the 44 `L1` cells. Deduplicating identical subsets would erase actual future cells. This statement concerns exact geometric successor state; it does not by itself assert a Boolean-branch-support failure.

---

## 7. Pair-overlap / hypergraph / slot-cut Pareto

Average combinatorial record counts at `N=6`:

| world | `|F|` | `|L1|` | `E_F` | nonzero `O2` pairs | `F-L1` incidences | `L1-L1` edges | `M3` edges | `K∂` relation records `E_F+S` |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| FCC | 39.025 | 92.239 | 96.561 | 139.467 | 214.917 | 226.752 | 538.230 | 156.820 |
| HCP | 39.107 | 95.216 | 96.901 | 139.128 | 215.187 | 244.451 | 556.539 | 157.197 |

Here `K∂` relation records count frontier-frontier contacts plus inward cut slots. Native slot labels are finite-alphabet labels; the frozen lattice transition table is background world structure and is not counted per state.

### Vertex / relation reduction versus explicit `M3`

Singleton:

| world | `M3` vertices | `K∂` frontier vertices | vertex reduction | `M3` edges | `K∂` relation records | relation-record reduction |
|---|---:|---:|---:|---:|---:|---:|
| FCC | 54 | 12 | 77.78% | 204 | 36 | 82.35% |
| HCP | 56 | 12 | 78.57% | 216 | 36 | 83.33% |

`N=6` atlas mean:

| world | mean `M3` vertices | mean `K∂` vertices | vertex reduction | mean `M3` edges | mean `K∂` relation records | relation-record reduction |
|---|---:|---:|---:|---:|---:|---:|
| FCC | 131.263 | 39.025 | 70.27% | 538.230 | 156.820 | 70.86% |
| HCP | 134.323 | 39.107 | 70.89% | 556.539 | 157.197 | 71.75% |

### Concrete JSON serialization slice

Using the same compact integer-coordinate JSON convention for both carriers:

- `M3`: stores `S`, vertex weights, and induced edges on `L0 union L1`;
- `K∂`: stores frontier coordinates and per-frontier inward slot offsets.

Results:

| world/slice | `M3` bytes | `K∂` bytes | reduction |
|---|---:|---:|---:|
| FCC singleton | 4881 | 397 | 91.87% |
| HCP singleton | 5122 | 390 | 92.39% |
| FCC `N=6` mean | 12616.98 | 1424.12 | 88.71% |
| HCP `N=6` mean | 12495.04 | 1369.67 | 89.04% |

These are representation measurements, not information-theoretic lower bounds.

### Update cost

In degree 12, one `K∂` addition mutates only:

- deletion of the chosen frontier record;
- at most `deg_F(x)<=11` old frontier inward-slot records;
- insertion of `b_x=12-|I(x)|-deg_F(x)<=11` new frontier records.

Thus at most 23 frontier/inward records are inserted/updated/deleted before adjacency regeneration. Each new cell needs at most 12 native neighbor probes, so with hashed frontier membership the transition is bounded local work independent of cluster size.

---

## 8. What happened to the candidate hypotheses

### H1 `G0_B3_SUFFICIENCY`

`BOUNDED_PROVED / GLOBAL_CONJECTURAL`.

- exact through the complete FCC/HCP atlas `N<=8` because `G0` has singleton classes there;
- no structural proof for all finite clusters;
- no counterexample found.

### H2 `G0_RECURSIVE_CLOSURE`

`BOUNDED_PROVED_THROUGH_PARENT_N7 / GLOBAL_CONJECTURAL`.

- no action-rooted automorphism split through parent `N<=7` in either world;
- child injectivity through `N<=8` closes the bounded exactness argument;
- unbounded reconstruction remains open.

### H3 `FRONTIER_STATIONARY_MARKOV`

`PROVED_POSITIVE` for `K∂`.

A fixed-form current-interface state exists and updates exactly for arbitrary finite addition-only horizons.

### H4 `PAIR_OVERLAP_REPAIR`

`NOT_NEEDED_AS_STORED_REPAIR / STANDALONE_SUFFICIENCY_UNPROVED`.

`O2` is derivable from `K∂`. Since `G0` was not killed, no native witness establishes pairwise overlap as the minimal repair. Do not promote it.

### H5 `HYPERGRAPH_DEBT`

`NOT_IRREDUCIBLE` as an explicit exterior-depth requirement.

The full shared-future multihypergraph is derivable from `K∂`; explicit storage is unnecessary in the stationary slot-cut representation. If one insists on abstract `G0` only, hyperedge identity remains a candidate diagnostic residual.

### H6 `INTERIOR_FORGETFULNESS`

`PROVED_POSITIVE` for the declared addition-only surface future given `K∂`.

Deep interior provenance never enters the update. Only the current frontier native embedding and inward cut slots are required.

### H7 `FCC_HCP_RECONSTRUCTION_SPLIT`

`NO_SPLIT_OBSERVED_THROUGH_N8` for `G0` injectivity. The same slot-cut theorem holds in both worlds. HCP has a richer local shared-future multiplicity structure (including duplicate hyperedges at the singleton), but no `G0` reconstruction collision was found.

### H8 `FIXED_STATE_VS_HORIZON_GROWTH`

The strong horizon-growth alternative is **killed**: `K∂` is fixed-form and stationary. Horizon-indexed explicit `M_h` depth is a representation choice, not an exactness necessity once native slot transition structure is retained.

---

## 9. BRC / quotient reading

No generic quotient theorem is re-owned here.

Surface-specific factorization is:

```text
K∂  --π-->  G0
 |           |
 |           ? global injectivity
 v           v
all finite B_h
```

For every `h`, the proved stationary theorem gives

```text
ker(K∂) subseteq ker(B_h).
```

On the exact `N<=8` atlas, R043-T1 additionally gives

```text
ker(G0) = equality,
```

hence bounded suffix-safe recoalescence by `G0` is trivial there.

The unbounded mother question is exactly whether

```text
ker(G0) = ker(K∂)
```

(up to declared native symmetry / future-equivalent relabeling) on all finite connected reachable interfaces.

Boolean set support still must not be conflated with path multiplicity, provenance, probability, or amplitudes. `K∂` gives the exact labeled geometric transition state; downstream branch aggregation semantics remain a separate layer.

---

## 10. Reconstruction theorem candidate and unique next action

### R043-C1 — Native slot-cut reconstruction conjecture

For frozen FCC and frozen HCP separately:

> Every finite connected reachable slot-cut frontier carrier `K∂(C)` is determined up to native symmetry by its weighted abstract frontier graph `G0(C)`.

Equivalent operational form:

```text
G0(C) + chosen abstract action vertex
    -> exact successor G0(C+x)
```

up to weighted graph isomorphism.

Bounded evidence:

- `π` injective over every cluster class through `N<=8` in both worlds;
- action-rooted closure exact through parent `N<=7` in both worlds.

This conjecture is **not** promoted to theorem.

### Unique next action

Do not extend naive animal enumeration first. Build a native **slot-completion / embedding CSP** whose input is only an abstract weighted `G0` and whose solutions are coherent `K∂` completions.

Priority order:

1. reconstruct/branch on native slot frames around one rooted frontier vertex;
2. propagate edge-slot transition consistency across the frontier graph;
3. use `|I(x)|=k_x` and frontier completeness to classify inward versus outward missing slots;
4. quotient completions by native world symmetry and weighted-frontier automorphisms;
5. if two non-equivalent `K∂` completions survive, attempt to realize both by finite connected clusters and compare successor `G0/B3`;
6. if every local completion is forced, extract the weakest finite propagation lemma and prove it separately for FCC and HCP.

This attacks the actual hidden object directly. Increasing `N` without this completion analysis has sharply diminishing value after the exact `N<=8` injective atlas.

---

## 11. External reconstruction-theorem search boundary

A targeted literature search found inverse/reconstruction results for graphs from substantially richer boundary spectral or boundary-distance data, and generic Euclidean framework reconstruction from edge-length data, but no theorem directly matching the present object: an unlabeled weighted induced current-frontier graph of a finite FCC/HCP contact cluster with no distances, spectrum, or coordinates supplied. Those results therefore do not close R043-C1 and are not imported as proof.

---

## 12. Evidence summary

```text
G0 collision atlas:
  FCC N<=8, cross-size: 158260 classes / 158260 distinct G0 keys
  HCP N<=8, cross-size: 630898 classes / 630898 distinct G0 keys

G0 action-rooted closure:
  FCC parent N<=7: no split
  HCP parent N<=7: no split

stationary K∂ update:
  structural proof: PASS
  FCC exhaustive actions through N<=6: 52380 PASS
  HCP exhaustive actions through N<=6: 198983 PASS

CI:
  CI_NOT_REQUIRED_FOR_RESEARCH
```

No hard block remains. The task is at `SEMANTIC_CHECKPOINT`: the global `G0` theorem is intentionally left conjectural, while the fixed-form stationary surface-state question is answered positively by the slot-cut carrier.
