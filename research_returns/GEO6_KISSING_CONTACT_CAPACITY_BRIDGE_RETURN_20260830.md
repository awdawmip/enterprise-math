# GEO6 Kissing Contact Capacity Bridge — Research Return

Task: `RS-GEO6-KISSING-CONTACT-CAPACITY-BRIDGE`  
Publication: `TP2-3CB258C85A117CBD20A5`  
Researcher: `EM-G6KISS-AAC55F`  
Claim: `chatgpt-g6kiss-20260830-1114-d45c79`  
Execution branch: `research/geo6-kissing-contact-capacity-bridge-em-g6kiss-aac55f`  
Date: `2026-08-30`  
Terminal verdict: `SUCCESS`  
Hard-target disposition: `P000_NATIVE_6D_CONTACT_CAPACITY_ATLAS_CONSTRUCTED_AND_EUCLIDEAN_TRANSFER_OBSTRUCTED_AT_CURRENT_READOUT_STRENGTH`

## 1. Result in one paragraph

A metric-free finite native contact model can be defined without identifying P000 with Euclidean `R^6`: take one opaque central Cell, one opaque neighboring Cell for each of the six native axis types, and declare center-to-axis-neighbor contact only. The accepted carrier-compatible `S4` action permutes the six axis labels and preserves the six contact edges, giving an exact center capacity `6`, one contact orbit of size `6`, and edge stabilizer order `4`. Independently, the external `E6` kissing witness is regenerated from an integral `6 x 6` Gram matrix by Weyl reflections, producing exactly `72` roots of norm `2`; the resulting external contact graph (`<alpha,beta>=1`) is `20`-regular with `720` edges. A faithful contact embedding into the current seven-Cell axis star or into the six-axis readout is therefore impossible. More importantly, rotation compatibility alone does not canonically select contact: on the natural four-Cell `S4` orbit, the only invariant simple contact graphs are the empty graph and `K4`, with capacities `0` and `3`. Thus the present P000 rotation/carrier data support exact finite contact atlases, but do **not** yet canonically determine a native kissing number. Transferring the 72-point `E6` witness requires additional native state/contact data rather than an untyped import of Euclidean metric structure.

## 2. Evidence typing

The following types are deliberately kept separate.

### `EXTERNAL_THEOREM`

As of the research date, the maintained classical six-dimensional kissing bounds are

`72 <= tau_6 <= 77`.

The lower witness is supplied by the `E6` root configuration. The exact upper bound `77` is proved by de Laat, Leijenhorst and de Muinck Keizer in the work whose primary purpose is the exact `D4` result but which also improves the dimension-six upper bound.

External references used only as comparison data:

- Nebe–Sloane lattice catalogue, `E6`: https://www.math.rwth-aachen.de/~Gabriele.Nebe/LATTICES/E6.html
- de Laat–Leijenhorst–de Muinck Keizer, *Optimality and uniqueness of the D4 root system*: https://arxiv.org/abs/2404.18794
- Henry Cohn, maintained kissing-number table: https://cohn.mit.edu/kissing-numbers/

No classical bound is promoted to a P000 theorem.

### `NATIVE_DEFINITION`

Define the task-local **six-axis Cell-star model**

`M_* = (X_*, A, G, C_*)`

by:

- `A={E1,...,E6}` is the six native axis-type set fixed by P000;
- `X_*={c} union {n_e : e in A}` consists of seven opaque and pairwise distinct Cell identities;
- `G=S4` is used only at the accepted carrier-compatible/downstream action strength;
- `G` fixes `c` and permutes the six `n_e` through the accepted `K4`-edge action on axis types;
- `C_*(c,n_e)=C_*(n_e,c)=true` for each `e`;
- there are no other `C_*` contacts.

Local admissibility is therefore entirely relational:

1. contact is symmetric;
2. contact is irreflexive;
3. each of the six native axis types labels exactly one declared neighboring Cell in this model;
4. no Euclidean norm, distance, angle, sphere or inner product occurs in the native definition.

This is a **declared finite model**, not a claim that bare P000 canonically forces one-neighbor-per-axis contact.

Its exact capacity data are:

- `cap(c)=6`;
- `cap(n_e)=1`;
- all six contact edges form one `S4` orbit;
- the contact-edge stabilizer has order `24/6=4`.

### `TRANSFER_THEOREM`

For an external finite contact graph `(V,E_ext)` and a native finite contact model `(X,C)`, call

`f:V -> X`

a **faithful contact embedding** when `f` is injective and, for distinct `u,v`,

`{u,v} in E_ext  <=>  C(f(u),f(v))`.

This definition does not presuppose Euclidean semantics on the native side.

For the regenerated `E6` graph, no faithful contact embedding exists into:

- the declared seven-Cell axis-star model;
- the six-element current axis readout;
- the four-Cell natural `S4` orbit.

The first obstruction is already cardinality (`72>7`, `72>6`, `72>4`). There is also a local-degree mismatch: every external `E6` vertex has contact degree `20`, while the declared star has maximum degree `6`, the six-axis orbital atlas has maximum degree `5`, and the four-Cell invariant atlas has maximum degree `3`.

If a future transfer is required to factor through the current six-axis readout plus a finite residual label of uniform size `r`, injectivity alone forces

`6 r >= 72`, hence `r >= 12`.

This `12` is only a **resource lower bound for labels**. It does not assert that twelve residual states per axis are sufficient to reproduce the `E6` contact graph.

### `OBSTRUCTION`

There are two exact obstructions.

#### O1. Rotation compatibility does not determine contact

Take a four-element opaque Cell set `X={A,B,C,D}` with the natural `S4` action. The action is transitive on the six unordered Cell pairs. Therefore every `S4`-invariant simple undirected contact relation is a union of pair orbits, and there is only one pair orbit. Consequently the invariant contact relations are exactly

`C_0 = empty`

and

`C_1 = K4`.

Their local capacities are respectively `0` and `3`.

Thus **rotation invariance by itself cannot select a unique native contact predicate or capacity**.

This statement is intentionally at the rotation-reduct level. It does not claim every complete PF-10/Full-Cell expansion realizes both contact relations. Its relevance to the current P000 frontier is supplied by the accepted foundation boundary: the existing Gen12 common-model `S4` witness is existential, its particular `K4` witness is not canonically forced by bare P000, and the contact route is not required (`Omega_b=false` in the accepted positive witness).

#### O2. The six-axis carrier readout is too small for faithful `E6` transfer

Under the accepted `S4` action on the six axis types (the six edges of `K4`), unordered axis pairs split into exactly two orbitals:

- disjoint axis pairs: orbit size `3`, stabilizer order `8`;
- incident axis pairs: orbit size `12`, stabilizer order `2`.

Therefore the only `S4`-invariant simple graphs on the six axis labels are unions of these two orbitals, with regular degrees/capacities

`0, 1, 4, 5`.

This is an exact carrier-readout atlas, not a native Cell-identity theorem. It confirms that the existing six-label readout alone cannot encode the `20`-regular 72-vertex `E6` contact graph faithfully.

### `COMPUTATIONAL_REGRESSION`

The deterministic checker does not hard-code a list of 72 roots.

It starts from the integral Gram matrix

```
[ 2  0 -1  0  0  0]
[ 0  2  0 -1  0  0]
[-1  0  2 -1  0  0]
[ 0 -1 -1  2 -1  0]
[ 0  0  0 -1  2 -1]
[ 0  0  0  0 -1  2]
```

and generates the Weyl orbit of the first simple root using

`s_i(v) = v - (Gv)_i e_i`.

The checker establishes exactly:

- `|Phi(E6)|=72`;
- every generated root has norm `2`;
- each simple reflection preserves the root set and Gram pairing;
- relative to every root the pairing distribution is
  `2:1, 1:20, 0:30, -1:20, -2:1`;
- external contact rule `<alpha,beta>=1` gives degree `20`;
- the external contact graph has `720` edges;
- the four-Cell natural `S4` action has one unordered-pair orbit and exactly two invariant graphs;
- the six-axis action has pair-orbit sizes `3` and `12` and exactly four invariant orbital graphs;
- the declared native axis star is rotation-invariant and has capacity `6`;
- the current-readout transfer lower bound is `r>=12`;
- the adversarial empty/complete four-Cell contact models have capacities `0` and `3`.

The checker is finite regression/certification for the declared finite models. It is not an upper bound on a universal native P000 kissing number.

## 3. Exact reconstruction of the external 72-point witness

Let `G` be the integral Gram matrix printed above and let `alpha_i` be its simple-root basis. Because this is simply laced, the simple reflection in `alpha_i` acts on an integer coefficient vector `v` by

`s_i(v)=v-<v,alpha_i> alpha_i = v-(Gv)_i e_i`.

Starting with `e_1` and closing under the six reflections gives a finite orbit `Phi` of size `72`. Direct exact arithmetic shows `v^T G v=2` for every `v in Phi`.

For every fixed `alpha in Phi`, the multiset of pairings with all roots is:

- one `+2` (itself);
- twenty `+1`;
- thirty `0`;
- twenty `-1`;
- one `-2` (its antipode).

After the standard external kissing rescaling, two distinct outer spheres touch exactly when the corresponding roots have inner product `1`. Hence the external contact graph is 20-regular. By the handshake lemma it has

`72*20/2 = 720`

edges.

This is the independent finite certificate required by the task. The checker derives the `72`, `20` and `720` from the Gram/reflection rules.

## 4. Native contact-orbit atlas

The task uses the accepted six native axis types together with the **carrier-compatible** `S4` permutation pattern. The typing firewall is:

`CARRIER_S4 != FULL_NATIVE_P000_ROTATION_GROUP`.

### 4.1 Four opaque Cells

On the natural four-Cell orbit:

- vertex orbit size: `4`, stabilizer order: `6`;
- unordered-pair orbit size: `6`, stabilizer order: `4`;
- invariant simple contact capacities: `{0,3}`.

If one adds the extra axiom "there exists at least one contact edge", then symmetry forces `K4` and capacity `3` **inside that declared four-Cell model**. The extra axiom is not supplied by rotation invariance itself.

### 4.2 Six axis labels

Identify the six axis types only as a readout with the six two-subsets of `{A,B,C,D}`. Two unordered axis labels are either incident or disjoint. These are the two pair orbitals.

The corresponding invariant readout graphs are:

1. empty: degree `0`;
2. disjoint-only matching: degree `1`;
3. incident-only line graph `L(K4)`: degree `4`;
4. complete: degree `5`.

Again, this is a readout classification, not an identity of axis labels with native Cells.

### 4.3 Seven-Cell six-axis star

The declared model `M_*` promotes only the minimal information needed for an actual Cell-contact example: one center plus six separately tagged axis-neighbor Cells. Its contact capacity at the center is exactly `6`. This is a genuine finite native relational construction, while its non-canonicity is explicit.

## 5. What this says about the Enterprise Math bottleneck

The useful obstruction is not "P000 cannot contain 72 contacts." No such theorem has been proved.

The proved statement is narrower and more actionable:

> Current six-axis/carrier-rotation information does not contain enough typed state to make the external 72-vertex contact code a faithful native object, and rotation compatibility does not by itself select a unique contact relation.

Therefore a meaningful successor would have to add or derive one of the following, with operation-safe semantics:

1. a native local-neighborhood state space carrying more than the six axis labels;
2. a canonical relation/metric readout that decides when two neighboring Cell states are in contact;
3. an equivariant residual state coordinate whose role is not erased by the carrier projection;
4. a proof that existing PF-10/Full-Cell relations already define such a contact predicate.

The minimum `12` residual labels per axis is a first cardinality pressure test, not a proposed axiom.

## 6. Tool reuse / no-new-tool boundary

Existing Enterprise tool families were reused conceptually rather than duplicated:

- `T7_FINITE_SYMMETRY_EQUIVARIANCE`: orbit/stabilizer and invariant-choice obstruction;
- `T4_FINITE_FIBER_CAPACITY_COLLISION_MINIMA`: capacity/fiber pressure at a declared readout;
- ordinary exact finite graph counting for the task-local checker.

No new general-purpose Enterprise tool is proposed by this result.

## 7. Adversarial checks and nonclaims

The following stronger statements are **not** made:

- `tau_native=72`;
- `tau_native<=77`;
- `E6` is the P000 carrier;
- the accepted FCC carrier is replaced by `E6`;
- the carrier `S4` is the complete native P000 rotation group;
- the four-Cell `K4` contact model is canonically forced;
- twelve residual states per axis suffice for an `E6` embedding;
- the finite checker proves a universal packing theorem;
- no novelty claim follows from this construction.

The declared axis-star model and the empty/complete adversarial pair are deliberately small. Their role is to expose exactly what is and is not determined by current primitives.

## 8. Frozen artifacts

- Return: `research_returns/GEO6_KISSING_CONTACT_CAPACITY_BRIDGE_RETURN_20260830.md`
- Checker: `research_checks/GEO6_KISSING_CONTACT_CAPACITY_BRIDGE_CHECK_20260830.py`
- Atlas: `research_artifacts/GEO6_KISSING_CONTACT_CAPACITY_BRIDGE/CONTACT_ATLAS_V1.json`
- Execution record: `research_execution_records/RS-GEO6-KISSING-CONTACT-CAPACITY-BRIDGE/ER-7B1E833DA5F6F1598275.json`
- Result record: `research_result_records/RS-GEO6-KISSING-CONTACT-CAPACITY-BRIDGE/RR-953997C3D28C7E318C12.json`

## 9. Next control-plane recommendation

Driver review should accept this task at the finite-contact-atlas / current-readout-obstruction strength if the evidence chain is intact. A successor is justified only if it targets the newly isolated missing datum: a canonical or explicitly declared residual native contact-state layer beyond the six-axis readout. Do not reopen FCC-vs-E6 carrier selection and do not translate the classical `72..77` interval into a native theorem.
