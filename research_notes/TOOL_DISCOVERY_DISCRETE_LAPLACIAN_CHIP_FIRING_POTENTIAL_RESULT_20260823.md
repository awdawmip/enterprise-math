# Tool Discovery A+ — Discrete Laplacian / Chip-Firing / Potential Calculus

Researcher-ID: `EM-TDLP-F0577C`

Task-ID: `RS-TD-LP-DISCRETE-LAPLACIAN-CHIP-FIRING-POTENTIAL-CALCULUS`

Hard target: `ENTERPRISE_DISCRETE_LAPLACIAN_CHIP_FIRING_POTENTIAL_TOOL_CLASSIFIED`

Owner branch: `research/tool-discrete-laplacian-chip-firing-potential`

## 1. Frozen verdict

**Strongest final classification: `NEW_GLOBAL_TOOL_FAMILY`.**

Proposed interface label:

`ENTERPRISE_DISCRETE_TOPPLING_POTENTIAL_CALCULUS`

This classification does **not** mean new graph-Laplacian, chip-firing, sandpile, critical-group, or least-action mathematics was proved. Those mathematical ingredients are classical. The positive classification is narrower and Enterprise-specific:

> the current toolbox has no reusable semantic interface that accepts an explicitly declared finite incidence/toppling carrier plus an integer defect state, enforces legal local conservative redistribution, certifies termination, returns an order-independent stabilization and odometer, and exposes a compact least-action certificate with exact failure boundaries.

The result is not `L=D-A`, and it is not a renamed classical theorem. The accepted payload is the reusable **typed state-transition/certificate interface** and the fact that the same interface works on two genuinely different Enterprise families: an incidence/provenance skeleton and a non-symmetric mixed-radix carry system.

No Foundation mutation, registry mutation, or successor stage was opened.

## 2. Exact source baseline

Controlling taskbook:

- `research_tasks/TOOL_DISCOVERY_DISCRETE_LAPLACIAN_CHIP_FIRING_POTENTIAL_CALCULUS_20260823.md`
- taskbook source: `0eda7eb9c7a0bdca1edf5d62d487015df6d6bd00`

Taskbook-declared current-tool baseline:

- `enterprise_toolbox_registry.json@f83f349d1521185ac3e99db574959d0b797cacf2`
- `research_method_inventory.json@f83f349d1521185ac3e99db574959d0b797cacf2`
- `tool_invocation_policy.json@f83f349d1521185ac3e99db574959d0b797cacf2`
- `docs/ENTERPRISE_TOOL_INVOCATION_PROTOCOL.md@f83f349d1521185ac3e99db574959d0b797cacf2`

Declared comparison source:

- `src/enterprise_math/adjoint_boundary_precision.py`

The taskbook wrote the suffix `@a1e73b6d97f116cbb1127d1ba08a47a061318897`. GitHub cannot resolve that value as a commit ref. Reading the file at the taskbook source commit `0eda7eb...` returns blob SHA exactly `a1e73b6d97f116cbb1127d1ba08a47a061318897`; therefore the source identity is recoverable and exact. The value is a blob SHA, not a commit SHA.

Execution-time exact-term repository searches for `toppling`, `sandpile`, `odometer`, and `laplacian` returned no additional current source owner. This corroborates the taskbook's baseline capability-gap audit; it is not used as a proof of mathematical novelty.

## 3. Dedup / current-tool coverage

| Current owner | Existing declared capability | Missing capability required here | Dedup verdict |
|---|---|---|---|
| T3 — Typed Incidence Circuit Calculus | cycles, cuts/cocircuits, signed cycle certificates, same-endpoint path-defect decomposition | legal integer firing, sink stabilization, order-independent odometer, least action, finite toppling equivalence | **insufficient; composable input owner, not output owner** |
| T5 — Integer Precision / Refinement | exact projection/recomposition, carry/borrow, precision chain transport | arbitrary finite incidence redistribution, legal-order independence, graph sink stabilization, generic odometer certificate | **one specialization of the new interface, not global owner** |
| T6 — Operation-Safe Quotient | descent tests, predictive partitions, operation-family closure | firing-lattice dynamics and legal stabilization | **orthogonal; must not identify cokernel equivalence with safe quotient** |
| T9 — Holonomy / Cocycle / Gluing | loop defect, cocycle obstruction, strict-gluing no-go | local divergence/toppling stabilization and least-action normal form | **orthogonal; may feed a defect field but does not stabilize it** |
| `adjoint_boundary_precision.py` | order-adjoint threshold pullback and finite boundary-orbit closure | no chip state, no local conservation, no legal toppling, no odometer, no cokernel | **name-level overlap only (`stabilize` means boundary-orbit closure)** |

### Why this is not `EXTEND_T3`

The proposed interface does not subsume T3 and is not a strict superset of its circuit/cocircuit calculus. It consumes an incidence carrier **plus new semantic state data** and produces a dynamic legal-normalization certificate. Conversely, the same toppling interface applies to the mixed-radix carry matrix in Application B, which is non-symmetric and is not an undirected incidence Laplacian under an orientation gauge.

Therefore T3 is a possible upstream carrier constructor, not the unique semantic owner.

### Why this is not `EXTEND_T5`

T5 already owns carry/borrow as precision machinery. Application B by itself would therefore be a T5 specialization. The capability gap only survives because the same legal-toppling/least-action law applies unchanged to Application A, where no precision chain is present.

### Why this is not `COMPOSE_EXISTING_TOOLS`

No composition of the declared T3/T5/T6/T9 interfaces returns the missing object:

`(stable_state, odometer, least_action_certificate, termination_obstruction)`.

Obtaining that object requires adding the legal toppling relation and its theorem-backed certificate law. That is the exact missing I/O contract.

## 4. Typed core interface

### 4.1 Undirected incidence layer

Input:

- finite loopless vertices `V`;
- finite undirected edges with explicitly supplied positive integer multiplicities/weights;
- arbitrary auxiliary orientation only for incidence presentation;
- explicit sink set `S`;
- nonnegative integer state on active vertices.

Choose an arbitrary edge orientation and let `B` be the incidence matrix. Let `W` be the positive integer diagonal edge-weight matrix.

Operations:

- `INCIDENCE -> B`
- `DIV(B,f) = B f`
- `LAPLACIAN(B,W) = B W B^T`
- `REDUCED_LAPLACIAN -> L_A` after removing sink coordinates
- `FIRE(c,i) = c - L_A e_i` when `c_i >= (L_A)_{ii}`
- `STABILIZE`
- `ODOMETER`
- `LEAST_ACTION_CERT`
- `EQUIVALENCE_CLASS` modulo `L_A Z^A`
- `OBSTRUCTION`

Typed edge labels are preserved metadata. They do not alter weights or dynamics unless an explicit map from type to integer transfer coefficient is supplied.

### 4.2 Generic toppling layer

The reusable cross-domain core is slightly more general than an undirected graph Laplacian.

Input an integer matrix `Delta` satisfying

- `Delta_ii > 0`;
- `Delta_ij <= 0` for `i != j`;

and a state `c in N^n`.

A site `i` is legal iff

`c_i >= Delta_ii`.

A firing is

`c -> c - Delta e_i`.

A strict termination witness is a positive integer vector `q` with

`q^T Delta > 0`

coordinatewise.

This layer includes sink-reduced undirected graph Laplacians, but also includes the non-symmetric mixed-radix carry system used in Application B.

## 5. Theorem / status ledger

### DL-1 — orientation-presentation invariance

**Status: proved; classical linear algebra, Enterprise typing audited.**

Reversing the auxiliary orientation of edge `e` multiplies one column of `B` by `-1`. Hence

`B W B^T`

is unchanged. A physical edge flow is represented by negating its coordinate when the edge presentation is reversed, so `DIV(B,f)` is unchanged as well.

Therefore graph Laplacian, legal firing, stabilization, and odometer are independent of arbitrary auxiliary edge orientation.

### DL-2 — potential/divergence identity

**Status: proved.**

For a vertex potential `phi`,

`grad(phi) = B^T phi`

and weighted edge flow is `W B^T phi`. Therefore

`DIV(W grad(phi)) = B W B^T phi = L phi`.

This is the exact finite potential object used by the odometer: the total redistribution from firing vector `u` is `L_A u`.

No metric, Euclidean energy, continuum PDE, or spectral geometry is inferred from this identity.

### DL-3 — controlled conservation / sink dissipation

**Status: proved.**

For the full undirected Laplacian, every column sums to zero. Thus a full-state firing conserves total integer chip/defect mass exactly.

After sink coordinates are removed, firing active vertex `i` decreases active total by exactly the total edge weight from `i` to the declared sink set. The sink receives exactly that amount.

For a generic toppling matrix, any declared linear quantity `p^T c` changes under firing `i` by

`-(p^T Delta)_i`.

Thus exact conservation and exact dissipation are both typed by an explicitly declared linear functional.

### DL-4 — strict-potential termination certificate

**Status: proved.**

Let `Delta` have positive diagonal and nonpositive off-diagonal. Let `q > 0` satisfy

`m = q^T Delta > 0`.

A legal firing preserves nonnegativity: the fired coordinate remains nonnegative by legality, and all other coordinates can only increase.

Define

`P(c)=q^T c`.

Firing site `i` lowers `P` by the positive integer `m_i`. Therefore every legal firing sequence terminates after at most

`floor(P(c_0) / min_i m_i)`

firings.

This is a compact exact termination certificate, not a finite-state-size argument.

### DL-5 — exact sink criterion for finite undirected graphs

**Status: proved.**

For a finite loopless undirected positive-integer multigraph with sink set `S`, universal stabilization of every nonnegative active state holds iff every active connected component has a path to `S`.

**Sufficiency.** The reduced Laplacian satisfies

`x^T L_A x =
 sum_{active-active edges uv} w_uv (x_u-x_v)^2
 + sum_{active-sink edges us} w_us x_u^2`.

If every active component touches a sink, the right side vanishes only for `x=0`, so `L_A` is positive definite and invertible.

Solve exactly over `Q`:

`L_A q = 1`.

By the discrete minimum principle, `q` is strictly positive: if a minimum coordinate were nonpositive, the corresponding coordinate of `L_A q` would be nonpositive, contradicting `1`.

After clearing denominators, `Q>0` and, by symmetry,

`Q^T L_A > 0`.

DL-4 then gives termination.

**Necessity for universal termination.** If an active component has no path to a sink, firing inside it conserves its total chip mass. Taking the degree vector on that sinkless component gives total mass `sum d_v`, whereas every stable nonnegative state has total at most `sum(d_v-1)`. Hence no stable state can be reached from that initial state.

### DL-6 — least action

**Status: proved; classical abelian-toppling argument written at the exact matrix strength used here.**

Suppose a legal firing sequence has firing vector `u` and reaches a stable state. Let `v >= 0` be any vector for which `c-Delta v` is stable.

Assume a legal sequence first attempts to make some firing count exceed `v_i`. Immediately before that firing, its prefix count `w` satisfies

`w <= v` and `w_i=v_i`.

Let

`x=c-Delta w`,
`y=c-Delta v`.

Site `i` is legal in `x`, so `x_i >= Delta_ii`. Since `y` is stable, `y_i < Delta_ii`.

But

`x_i-y_i = [Delta(v-w)]_i
           = sum_{j != i} Delta_ij (v_j-w_j) <= 0`

because every off-diagonal entry is nonpositive. Hence `x_i <= y_i`, contradiction.

Therefore

`u <= v`

coordinatewise for every nonnegative stabilizing firing vector `v`.

### DL-7 — abelian/order-independent stabilization

**Status: proved from DL-4 + DL-6.**

Toppling translations commute algebraically. Under a termination hypothesis every maximal legal sequence is finite and ends stable.

If two legal stabilizations have odometers `u` and `v`, DL-6 gives both `u<=v` and `v<=u`. Therefore

`u=v`

and their stabilized states coincide.

The canonical object is therefore the stabilized state **from the declared initial state under legal topplings**, together with its unique odometer. It is not a canonical representative of every algebraic cokernel class.

### DL-8 — compact least-action certificate

**Status: proved interface property.**

A certificate stores only

- initial state `c`;
- final stable state `c^o`;
- odometer vector `u`.

The verifier checks

`c^o = c - Delta u`,
`u >= 0`,
`c^o` stable,

then deterministically consumes the counts in `u` by legal firings. No firing-order log is stored.

Once a legal realization of `u` is verified, DL-6 proves that `u` is the unique least-action odometer. Certificate storage is `O(|V|)` integers rather than a log of `sum u_i` firing choices.

The checker intentionally reconstructs legality; it does not claim constant-time verification when firing counts are large.

### DL-9 — reduced Laplacian / cokernel invariant

**Status: proved at the required finite level.**

For an undirected sink-accessible graph, `L_A` is an invertible integer matrix, so

`Z^A / L_A Z^A`

is finite, with cardinality `|det L_A|`.

Every firing preserves this algebraic class.

Small exact checker examples:

- triangle with one sink: `L_A=[[2,-1],[-1,2]]`, Smith factors `(1,3)`, cokernel order `3`;
- two active vertices joined by two parallel edges and each joined once to sink: `L_A=[[3,-2],[-2,3]]`, Smith factors `(1,5)`, cokernel order `5`.

The group is a derived invariant, not native ontology.

### DL-10 — stabilization is not a cokernel normal form

**Status: explicit minimal-active-count counterexample.**

For the triangle-with-sink matrix

`L_A=[[2,-1],[-1,2]]`,

both

`(0,0)` and `(1,1)`

are stable, but

`(1,1)-(0,0) = L_A (1,1)`.

Thus they lie in the same firing-lattice class.

With only one active vertex, a reduced matrix `[d]` has stable states `0,...,d-1`, which are distinct residue classes mod `d`. Hence two active vertices are the minimum active count at which this failure can occur.

This is the exact reason `EQUIVALENCE_CLASS` must not be conflated with `STABILIZE`, and it sharply separates this calculus from T6 quotient semantics.

### DL-11 — relabeling covariance

**Status: proved and checked.**

For a vertex permutation matrix `P`,

`Delta' = P Delta P^{-1}`,
`c' = P c`.

Legality, firing, stabilized state, and odometer transform covariantly:

`stab(c') = P stab(c)`,
`odo(c') = P odo(c)`.

No distinguished vertex name is created by the tool; only explicitly supplied sinks/types remain distinguished.

## 6. Two-domain reuse gate

### Application A — incidence/path/provenance skeleton

Carrier: a finite diamond-like provenance graph with active vertices `0,1,2`, sink `s`, and edges

`0-1, 0-2, 1-s, 2-s, 1-2`.

Reduced Laplacian:

`Delta_A =
 [[ 2,-1,-1],
  [-1, 3,-1],
  [-1,-1, 3]]`.

Initial local defect:

`c=(10,0,0)`.

Exact result:

- stable state: `(0,2,2)`;
- odometer: `(8,3,3)`;
- total firings: `14`;
- exhaustive legal firing orders: `144`;
- every legal order returns the same `(stable_state, odometer)` pair;
- sink absorbs `6` units.

T3 can classify cycles/cuts/path defects of this skeleton. It does not output the 14-step legal redistribution normal form or the 3-integer least-action odometer. Here the new layer compresses 144 legal order choices to one exact odometer certificate.

### Application B — mixed-radix precision/carry redistribution

Use the explicitly declared non-symmetric toppling matrix

`Delta_B =
 [[ 2, 0, 0],
  [-1, 3, 0],
  [ 0,-1, 2]]`.

Interpretation:

- firing level 0: remove two fine units, add one middle unit;
- firing level 1: remove three middle units, add one coarse unit;
- firing level 2: remove two coarse units into an external sink.

Initial state:

`c=(5,8,3)`.

Exact result:

- stable state: `(1,1,0)`;
- odometer: `(2,3,3)`;
- total firings: `8`;
- exhaustive legal firing orders: `209`;
- every legal order returns the same result.

A strict termination witness is `q=(1,1,1)`:

`q^T Delta_B=(1,2,2)>0`.

With place values

`p=(1,2,6)`

and top sink quantum `12`,

initial value is `39`,
final active value is `3`,
sink value is `36`,

so

`39 = 3 + 36`.

This application is genuinely different from Application A:

- `Delta_B` is non-symmetric;
- it is not produced by merely choosing a different orientation of an undirected `BWB^T`;
- the conserved semantic quantity is place value, not raw chip count;
- it is a T5 carry specialization, while Application A is an incidence/provenance redistribution.

The shared toppling/least-action layer therefore survives outside precision.

## 7. Hard boundaries and smallest counterexamples

### 7.1 No declared incidence/toppling carrier

No adjacency/transfer matrix means no firing neighborhood, threshold, divergence, or Laplacian is determined. The tool is not applicable.

The executable interface rejects an empty carrier rather than guessing adjacency.

### 7.2 Sinkless nontermination

Smallest positive-degree loopless connected example:

two vertices joined by one edge, no sink.

Reduced/full toppling matrix:

`[[1,-1],[-1,1]]`.

State:

`(1,0)`.

Legal firings give the exact period

`(1,0) -> (0,1) -> (1,0) -> ...`.

Finite state size does not imply termination.

### 7.3 A declared but inaccessible sink is insufficient

Add an isolated declared sink to the previous two-vertex active component. The active dynamics remain periodic. Sink presence is not the condition; active-to-sink accessibility or another exact termination witness is.

### 7.4 Directed edges are semantic, not orientation gauge

For two active sites plus a sink, compare

`Delta_ab=[[2,0],[-1,1]]`

with

`Delta_ba=[[1,-1],[0,2]]`.

These correspond to reversing the semantic direction of the active-active transfer while retaining dissipative sink exits.

From initial `(2,0)`:

- first system odometer: `(1,1)`;
- second system odometer: `(2,0)`.

Therefore directed edge reversal is not a presentation symmetry.

The generic toppling theorem remains valid for directed/non-symmetric systems only when the explicit Z-matrix sign contract and a termination certificate such as `q^T Delta>0` are supplied. No undirected symmetry/energy theorem is silently imported.

### 7.5 Negative/signed weights

Arbitrary signed weights can violate positive diagonal / nonpositive off-diagonal toppling semantics. Even a one-active-site signed "edge" of weight `-1` would produce a negative threshold and growth rather than dissipation under the naive formula.

Core result: **unsupported without separate semantics**.

### 7.6 Loops

The core graph constructor rejects loops. Standard graph-Laplacian loop conventions and chip-firing threshold conventions can disagree about whether a loop contributes to the firing threshold while returning chips to the same vertex. A loop may be admitted only after an explicit normalization rule is declared.

### 7.7 Cokernel does not imply operation-safe quotient

DL-10 shows two different stable states in the same cokernel class. Therefore algebraic chip-firing equivalence is not automatically a T6-safe semantic quotient.

### 7.8 Potential is not geometry

Potential values are integer/rational certificates on the declared finite carrier. They do not automatically define distance, Euclidean energy, conductance, spectral dimension, harmonic measure, continuum PDE structure, or a continuum limit.

### 7.9 Holonomy is not divergence

A T9 loop defect can be used as input data to a local redistribution problem only after a vertex/transition defect field is explicitly declared. Nonzero holonomy and nonzero Laplacian/divergence are different invariants.

## 8. Classical prior-art / novelty ledger

| Layer | Classification |
|---|---|
| Graph incidence matrix, `L=BWB^T` | classical theorem / linear algebra |
| Chip firing / toppling operators | classical |
| Abelian stabilization | classical |
| Least-action odometer principle | classical |
| Reduced Laplacian cokernel / critical-group algebra | classical |
| T3 incidence specialization | pre-existing Enterprise owner for cycles/cuts, not stabilization |
| T5 carry specialization | pre-existing Enterprise carry domain |
| T6 quotient semantics | pre-existing but non-equivalent |
| T9 holonomy semantics | pre-existing but non-equivalent |
| Exact typed toppling + termination + least-action certificate API shared across A and B | **new Enterprise semantic interface** |
| New mathematical theorem claimed | **none** |

Therefore:

`CLASSICAL_THEOREM_PACKAGED_FOR_ENTERPRISE != NEW_MATHEMATICS`

is preserved.

The positive tool result rests on the missing reusable Enterprise contract and two-domain reuse, not on claiming the classical theory as novel.

## 9. Deterministic exact checker

Required executable:

`scripts/tool_discovery_discrete_laplacian_chip_firing_potential_check.py`

Reusable candidate module:

`src/enterprise_math/discrete_laplacian_chip_firing.py`

Local exact execution of the frozen contents:

```text
CHECKS=174
MISMATCHES=0
FINAL=PASS
```

Coverage includes:

- path with sink;
- cycle with sink;
- tree;
- genuine parallel-edge multigraph;
- all auxiliary edge-orientation choices on small fixtures;
- divergence orientation compensation;
- `div grad = Laplacian`;
- conservation / exact sink loss;
- exhaustive legal firing orders for finite small states;
- unique stabilization and odometer;
- bounded exhaustive least-action comparison;
- vertex relabeling covariance;
- reduced-Laplacian determinant and small Smith factors;
- stable same-cokernel-class counterexample;
- sinkless period;
- inaccessible-sink period;
- semantic directed-orientation counterexample;
- signed-weight rejection;
- both cross-domain applications.

Enumeration is regression evidence only. General statements DL-1 through DL-11 are proved above at the exact strength claimed.

Frozen content digests:

- `src/enterprise_math/discrete_laplacian_chip_firing.py` SHA256 `04a51628eca861859866852117b6f7db27ce779d5b061aa3f72a1285f2d89e12`
- `scripts/tool_discovery_discrete_laplacian_chip_firing_potential_check.py` SHA256 `afaeb3ebc1d82357a2d450c92e5cbcd4dfde6bacf17db8949aa753f813d2c404`

## 10. Acceptance-gate audit

1. **Reusable I/O interface:** PASS.
2. **Nontrivial structural law/certificate:** PASS — strict termination potential, abelian stabilization, least-action odometer.
3. **Exact negative/failure boundary:** PASS.
4. **Two genuinely different Enterprise problem families:** PASS.
5. **Real compression/canonical certificate:** PASS — Application A collapses 144 legal orders to one odometer; Application B collapses 209 legal orders to one odometer.
6. **Dedup against T3/T5/T6/T9 and executable-source baseline:** PASS.
7. **No false new-mathematics claim:** PASS.

## 11. Final classification

Frozen strongest classification:

`NEW_GLOBAL_TOOL_FAMILY`

Proposed family scope:

> finite typed integer local-redistribution/toppling systems with explicit legality, exact termination certificates, canonical legal stabilization, odometer/least-action certificates, and optional reduced-Laplacian/cokernel invariants.

The undirected graph Laplacian is one constructor for this family, not the family itself.

The mixed-radix carry system is another constructor/specialization, which is why the result is not merely T3 or T5 under a new name.

No further stage is opened from this return.

**Hard target closed:**

`ENTERPRISE_DISCRETE_LAPLACIAN_CHIP_FIRING_POTENTIAL_TOOL_CLASSIFIED`
