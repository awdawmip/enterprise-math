# Tool Discovery — Native Oriented-Matroid / Circuit Calculus — Research Return

Status: `RESEARCH_RETURN / DRIVER_REVIEW_REQUIRED`
Date: `2026-08-22`
Researcher-ID: `EM-TDOM-BH6ND3`
Task: `RS-TD-OM-NATIVE-ORIENTED-MATROID-CIRCUIT-CALCULUS`
Owner branch: `research/tool-native-oriented-matroid-circuits`
Frozen source: `awdawmip/enterprise-math@00765cc76ea71f789481fbe91c29d852bbf6b209`

Leading verdict:

`NATIVE_CIRCUIT_CALCULUS_DISCOVERED`

This verdict is intentionally narrower than “the three Enterprise positive directions themselves form a canonically oriented matroid.” That stronger direction-only claim fails the native-admissibility audit. The successful construction is instead a full **oriented graphic matroid / circuit-cocircuit calculus on any finite component-typed native transition/incidence skeleton**. It uses only finite states, typed incidences, support, signs, and composition. Metric length, the carrier angle, Euclidean coordinates, slopes, determinants, and the carrier relation `e_1+e_2+e_3=0` are absent from the primitive interface.

The construction is standard mathematics at the oriented-graphic-matroid level. The Enterprise-specific result is the exact refoundation map from the current typed transition/incidence objects to that calculus, together with a native/carrier typing barrier and two independent Enterprise reuse demonstrations.

---

## 1. Mother-question answer

A substantial nonmetric fragment of the current Enterprise discrete geometry survives after metric/carrier erasure:

- path dependence and path equivalence relative to a typed transition skeleton;
- minimal local branch/recoalescence dependencies;
- circuit elimination / rerouting certificates;
- minimal transition separators (cocircuits/bonds);
- circuit-cocircuit duality;
- provenance defects between two same-endpoint witnesses;
- invariance under state/edge relabeling and edge-reference reorientation;
- exact rejection of carrier-only edges that are not members of the native typed skeleton.

The following do **not** survive this abstraction and are not claimed to be recovered:

- native line-gauge magnitudes;
- Pythagorean readouts;
- carrier angles or lengths;
- circle radius / overlap area;
- path multiplicity from Boolean support alone;
- a direction-only signed dependency among `E_1,E_2,E_3`;
- a global chirotope on the three positive directions without additional native orientation/dependency semantics.

Thus the discovered tool is not a replacement for the current metric/gauge layer. It is a reusable **incidence/provenance calculus below metric readout**.

---

## 2. Exact no-go boundary: do not orient the three positive directions by importing the carrier

The current native foundation explicitly separates the three positive native axis families from the classical planar carrier relation. In particular:

- `e_1+e_2+e_3=0` is a carrier-presentation relation, not a native vector identity;
- reverse-third-family endpoint shortcuts are carrier-only and do not preserve native component trace;
- same carrier endpoint does not imply same native line identity.

Therefore the tempting signed circuit

`(+E_1,+E_2,+E_3)`

cannot be justified natively by the classical triangular-carrier vector dependency. Doing so would copy an implementation-carrier relation into the native premises.

There is an unsigned support observation: a single sector-local trace uses at most two of the three positive direction families, so the family of direction supports behaves like the independence sets of `U_{2,3}`. But that alone does not provide a native signed dependency orientation. Any signed circuit on `{E_1,E_2,E_3}` would require an additional sign/dependency semantics not presently supplied by the native direction labels themselves.

Result:

`DIRECTION_ONLY_NATIVE_CHIROTOPE = NOT_DERIVED`

`CARRIER_VECTOR_DEPENDENCY_AS_NATIVE_CIRCUIT = FORBIDDEN_TARGET_LEAKAGE`

This failed route is important because it forces the successful ground set to be the actual native relational/transition incidences rather than the carrier direction vectors.

---

## 3. Successful ground structure: finite typed transition/incidence skeleton

Let

`Gamma = (V,E,s,t,tau)`

be any finite Enterprise transition/incidence skeleton where:

- `V` is a finite set of typed native states;
- `E` is a finite set of typed transition/incidence occurrences;
- `s(e),t(e) in V` are the incident endpoints of `e` when a native direction is already present;
- `tau(e)` retains the native semantic type required by the source theory, e.g. `R_i`, `R_j`, start-incidence type, or another relation label.

If the source relation is intrinsically directed, use that direction as the default reference orientation. If only undirected incidence is available, choose an arbitrary reference orientation for each edge. Such a choice is **gauge only**; the native object is its reorientation-equivariant circuit system.

No metric, coordinate, angle, slope, circle equation, determinant, or continuum embedding is part of `Gamma`.

### 3.1 Integer 1-chains and boundary

For a chosen edge-orientation gauge `o`, define the finite free integer chain group

`C_1(Gamma)=Z^E`.

For an edge basis element `e`, define its combinatorial boundary

`partial_o(e)=t(e)-s(e)`.

Extend linearly to

`partial_o : Z^E -> Z^V`.

This is incidence algebra only. The minus sign records the chosen orientation of an incidence; it is not a negative Enterprise number axis and does not assert a physically admissible reverse transition.

### 3.2 SIGN

For `z in Z^E`, define

`SIGN_o(z)(e) = +` if `z_e>0`,

`SIGN_o(z)(e) = -` if `z_e<0`,

`SIGN_o(z)(e) = 0` if `z_e=0`.

The support is

`supp(z)={e:z_e != 0}`.

`SIGN_o` is gauge-covariant: reversing the reference orientation of an edge flips only that edge coordinate in every sign vector.

### 3.3 CIRCUITS

A nonzero chain `c in ker(partial_o)` is a **primitive incidence circulation** when the gcd of its nonzero coefficients is one.

An Enterprise incidence circuit is

`C = SIGN_o(c)`

for a primitive nonzero `c in ker(partial_o)` having support minimal among nonzero circulations.

For an ordinary finite graph skeleton this is exactly a signed simple cycle. Parallel transitions and loops are handled by the usual graphic-matroid multigraph conventions.

The native circuit object is not one fixed arbitrary sign gauge. It is the typed support together with its full reorientation-covariant signed class.

### 3.4 ELIMINATE

Let signed circuits `C_1,C_2` have opposite signs at an edge `e`, and assume `C_1 != -C_2`.

Choose primitive circuit chains `c_1,c_2` whose coefficients at `e` are `+1` and `-1`. Then

`z=c_1+c_2`

is a nonzero circulation with `z_e=0`. Decompose `z` conformally into support-minimal primitive circulations. Any circuit in that decomposition that witnesses the remaining support gives an elimination output `C_3` with

- `e notin supp(C_3)`;
- positive signs drawn only from the positive signs of `C_1` or `C_2`;
- negative signs drawn only from the negative signs of `C_1` or `C_2`.

This is the signed circuit-elimination operation.

### 3.5 SEPARATE / cocircuits

For `S subset V`, define the signed cut chain `delta_o(S)` by

- `+` on reference-oriented edges leaving `S`;
- `-` on reference-oriented edges entering `S`;
- `0` elsewhere.

A support-minimal nonzero cut is a **bond**. Its sign vector is a cocircuit.

`SEPARATE(A,B)` searches for a support-minimal bond whose two sides place the requested disjoint state sets `A,B` on opposite sides. The returned cocircuit is therefore a minimal transition-removal obstruction to connecting the two sides inside the selected typed skeleton.

### 3.6 DUAL

Define

`DUAL(Gamma)`

as the cographic oriented-matroid dual in which circuits are the cocircuits/bonds of the original system and cocircuits are the original circuits.

No planar dual drawing is required. If a planar realization exists, it may be used afterward as a carrier realization, not as the definition of the dual.

### 3.7 REALIZATION_CHECK

`REALIZATION_CHECK` accepts a candidate realization only if there is a typed incidence isomorphism from the declared native skeleton to the candidate skeleton, together with an allowed edge-reorientation map.

It checks:

1. state incidence is preserved;
2. transition semantic types `tau` are preserved where task-critical;
3. circuit supports correspond;
4. cocircuit supports correspond;
5. signed circuits correspond after the declared reorientation gauge map.

Metric/coordinate payloads are ignored. Adding a carrier-only edge, deleting a native edge, or erasing a theorem-critical component label is therefore a semantic failure even if the carrier endpoint geometry still looks correct.

---

## 4. Axiom audit: full oriented graphic matroid on every finite typed skeleton

### Proposition 4.1 — signed circuit axioms

For every finite `Gamma`, the signed circuit family above satisfies the finite oriented-matroid circuit axioms.

#### C0 — nonzero

The zero chain is excluded by definition.

#### C1 — sign symmetry

If `c` is a primitive support-minimal circulation, then `-c` is also primitive, support-minimal, and has sign vector `-C`.

#### C2 — incomparability

If two circuit supports satisfy

`supp(C_1) subseteq supp(C_2)`,

minimality forces equality of supports. On one simple cycle support, flow conservation determines the primitive circulation up to global sign, hence

`C_1=C_2` or `C_1=-C_2`.

#### C3 — signed elimination

Suppose `C_1 != -C_2` and the two circuits have opposite sign at `e`. Orient representatives so the coefficients at `e` cancel in `c_1+c_2`. The sum is nonzero because the circuits are not global negatives, and it remains in `ker(partial_o)`. Every finite nonzero integer circulation admits a conformal decomposition into primitive simple-cycle circulations. Selecting a conformal circuit from this decomposition yields the required eliminated circuit avoiding `e` and introduces no sign outside the signs already present in `C_1,C_2`.

Therefore the construction is a full oriented graphic matroid, not merely an independence system or heuristic cycle detector.

Freeze candidate for Driver review:

`FINITE_TYPED_NATIVE_INCIDENCE_SKELETON -> ORIENTED_GRAPHIC_MATROID`

### Proposition 4.2 — circuit/cocircuit orthogonality

For any circulation `c` and any cut `delta(S)`,

`<c,delta(S)>=0`.

This follows directly from `partial(c)=0`: the net signed flow across a cut vanishes. Consequently a circuit and cocircuit cannot meet in exactly one edge, and their sign intersections satisfy the standard oriented circuit/cocircuit orthogonality relation.

This gives the requested dual/separation law without metric input.

---

## 5. Relabeling and gauge invariance

Let `phi_V` relabel states and `phi_E` relabel transition occurrences while preserving incidence and task-critical type labels. Let `rho subset E` be any set of edges whose reference orientations are reversed.

Then:

- chain boundary commutes with the transported incidence map;
- circuit supports are carried bijectively by `phi_E`;
- cocircuit supports are carried bijectively by `phi_E`;
- reorienting `rho` multiplies the corresponding signed coordinates by `-1` and changes nothing else;
- elimination, separation, and circuit/cocircuit orthogonality commute with this transport.

Thus no vertex name, edge name, coordinate chart, drawing orientation, or arbitrary reference-edge orientation becomes part of the native semantic content.

The invariant object is the typed circuit/cocircuit structure with its reorientation action.

---

## 6. Metric-erasure pressure test

Take two realizations of the same typed incidence skeleton and assign them arbitrarily different:

- point coordinates;
- edge lengths;
- carrier shapes;
- angles;
- numerical metric payloads.

As long as the typed incidence isomorphism is unchanged, `SIGN`, `CIRCUITS`, `ELIMINATE`, `SEPARATE`, `DUAL`, and the circuit-support outputs are unchanged up to the allowed reorientation map.

Conversely, if a carrier realization adds a nearest-neighbor shortcut not present in the native typed transition skeleton, `REALIZATION_CHECK` rejects the extra edge even if it joins the same carrier endpoints.

Therefore:

`SAME_TYPED_INCIDENCE + DIFFERENT_METRIC/CARRIER => SAME_CIRCUIT_CALCULUS`

but

`DIFFERENT_TYPED_INCIDENCE => NOT_CERTIFIED_BY_SAME_NATIVE_CALCULUS`.

This is the exact metric/carrier erasure property required by the taskbook.

---

## 7. Compact TOOL API

```text
NativeCircuitTool(Gamma):
    input:
        finite typed transition/incidence skeleton Gamma
    no primitive input:
        coordinates, metric, length, angle, slope, determinant, carrier embedding

SIGN(z, orientation_gauge) -> sign_vector
    sign of an integer edge chain

CIRCUITS(Gamma, orientation_gauge) -> signed_circuit_family
    primitive support-minimal nonzero ker(boundary) sign vectors

ELIMINATE(C1, C2, e) -> C3 or witness-set
    signed circuit elimination at an oppositely signed shared edge

SEPARATE(A, B) -> signed_cocircuit/bond or NONE
    support-minimal transition cut separating requested state sets

DUAL(Gamma) -> cographic_dual_interface
    circuits <-> cocircuits

PATH_DEFECT(p, q) -> z = chain(p)-chain(q)
    if p,q have the same typed endpoints then boundary(z)=0

CIRCUIT_DECOMPOSE(z) -> multiset/list of signed circuits
    conformal decomposition of a nonzero integer circulation

REALIZATION_CHECK(Gamma, candidate, incidence_map, reorientation_map) -> PASS/FAIL
    ignores metric payload; checks typed incidence and circuit/cocircuit transport
```

Complexity notes:

- boundary and path-defect computation are linear in touched transitions;
- cycle/cocircuit enumeration can be exponential in the worst case and should not be the default implementation on large graphs;
- practical implementations should use spanning forests, fundamental cycle bases, cut bases, and task-local sparse certificates;
- the mathematical API is circuit-based; exhaustive enumeration is only a finite validation method.

---

## 8. Cross-domain demonstration A — native line/path incidence

Use the frozen R061 component-typed transition skeleton for one translated sector. The two legal `(1,1)` path representatives

`X_i X_j`

and

`X_j X_i`

have the same typed start and typed terminal. Their edge-chain difference has zero boundary and is exactly the signed 4-edge commuting-diamond circuit.

Therefore the circuit calculus certifies the local rerouting

`X_i X_j <-> X_j X_i`

without using:

- `120 degrees`;
- native length;
- jump count;
- carrier coordinates;
- a third-family vector relation.

For the `(3,4)` trace fiber:

- there are `35` legal shuffle witnesses;
- the finite typed prefix skeleton has `20` states and `31` transition edges in the implementation checker;
- its cycle rank is `12`;
- the `12` unit commuting diamonds form an integer circuit basis;
- all `C(35,2)=595` pairs of distinct path witnesses have nonzero provenance defects that decompose exactly over those circuits.

Thus all legal shuffle representatives are connected by circuit-level local reroutings while remaining distinct path witnesses.

### Reverse-third shortcut gate

The reverse-third carrier shortcut to the `(1,1)` endpoint is **not** an edge of the declared `{X_i,X_j}` component-typed native transition skeleton.

If one first forgets types and inserts the carrier shortcut into an unlabeled carrier graph, it creates additional graph circuits. Those circuits are correct for that larger carrier graph but are not native-line circuits.

Therefore the tool enforces the same source-theory rule as R061/R062:

`COMPONENT_TYPED_FIRST -> CIRCUIT_CALCULUS_SECOND`.

This solves the spatial/incidence-facing problem “same carrier endpoint versus same native line/path family” without metric input.

---

## 9. Cross-domain demonstration B — generic BRC provenance loss

Now remove the spatial interpretation entirely and consider a generic typed Boolean-BRC relation diamond:

```text
s -> a -> t
 \       /
  -> b ->
```

There are two exact branch witnesses:

`p_1 = s-a-t`

`p_2 = s-b-t`.

Canonical Boolean BRC records terminal support `t` once. It does not retain which path produced it.

In the circuit calculus,

`PATH_DEFECT(p_1,p_2)=chain(p_1)-chain(p_2)`

has zero boundary and is the unique 4-edge signed circuit of the diamond.

Hence:

- Boolean terminal support = `1`;
- path witnesses = `2`;
- circuit rank = `1`;
- provenance defect = nonzero signed circuit.

This gives a general relation-level diagnostic:

> If two typed BRC witnesses have the same endpoints, their chain difference is a circulation. If it is nonzero, at least one circuit certificate witnesses provenance information that Boolean support discards.

The result applies to arbitrary finite typed relation skeletons, not only the Enterprise plane. It therefore provides the requested second, genuinely different Enterprise reuse domain: branch/recoalescence provenance rather than spatial line geometry.

The tool does **not** invert Boolean BRC after provenance has been erased. It must be attached to the typed transition skeleton before or alongside the Boolean projection.

---

## 10. Executable finite checks

Checker:

`experiments/tool_discovery_native_oriented_matroid_circuit_calculus_check.py`

The checker is standard-library-only and uses coordinates solely as an implementation label for finite grid states. None of its circuit definitions reads a metric, length, angle, slope, determinant, or Euclidean geometry.

Validated cases:

### 10.1 Nontrivial oriented-matroid axiom audit — `2x2` typed window

- vertices: `9`;
- edges: `12`;
- cycle rank: `4`;
- unsigned simple circuits: `13`;
- signed circuits: `26`;
- signed cocircuits: `106`;
- signed circuit-elimination instances checked: `912`;
- circuit/cocircuit orthogonality checks: `2756`;
- mismatch count: `0`.

### 10.2 Minimal commuting diamond

- legal trace paths: `ij`, `ji`;
- path count: `2`;
- cycle rank: `1`;
- path defect equals the unique signed circuit;
- reverse-third carrier edge is absent from the native typed skeleton.

### 10.3 `(3,4)` path fiber

- path witnesses: `35`;
- pairwise provenance-defect checks: `595`;
- vertices: `20`;
- edges: `31`;
- cycle rank: `12`;
- unit-face circuit basis size/rank: `12/12`;
- all pair defects exactly integer-decomposable over the circuit basis;
- maximum absolute face coefficient in these pair decompositions: `1`.

### 10.4 Generic nonspatial BRC diamond

- Boolean terminal support: `1`;
- path witnesses: `2`;
- cycle rank: `1`;
- provenance defect is the unique circuit.

### 10.5 Relabeling / reorientation gauge

A deterministic state relabeling plus four edge-reference reversals transported every signed circuit to a signed circuit of the transformed graph, preserving circuit-support counts.

### 10.6 Metric-erasure payload test

Two deliberately unrelated coordinate/length payload assignments on the same `2x2` typed graph produced the same combinatorial circuit signature.

The checker is a finite regression suite, not the proof of the general theorem; the proof is the incidence/circulation argument in Sections 3–5.

---

## 11. Historical comparison and novelty audit

Historical comparison only:

- Björner, Las Vergnas, Sturmfels, White, Ziegler, *Oriented Matroids*, 2nd ed., Cambridge University Press, 1999 — standard oriented-matroid circuit/cocircuit/chirotope theory;
- the graphic oriented matroid construction — signed graph cycles as circuits and signed minimal cuts/bonds as cocircuits;
- standard circuit elimination and circuit/cocircuit duality.

No claim is made that graphic oriented matroids, signed cycle elimination, or bond duality are new mathematics.

Enterprise-specific contribution of this task:

1. identifies the **component-typed native transition/incidence skeleton**, not the three carrier directions, as the admissible ground structure;
2. proves an exact native/carrier separation rule for circuit membership;
3. turns same-endpoint path differences into metric-free circuit certificates;
4. exposes a reusable BRC provenance-defect observable before Boolean collapse;
5. supplies a compact API and finite checker aligned with current Enterprise line/BRC semantics.

A chirotope exists for the resulting oriented graphic matroid by standard oriented-matroid equivalences, but it is deliberately not used as the primitive Enterprise interface. A basis ordering and sign convention add bookkeeping that the circuit-first interface does not need.

The construction always lies in the graphic/regular/realizable part of oriented-matroid theory. This task does not discover or require a nonrealizable oriented matroid.

---

## 12. Native-semantics admissibility ledger

### Claim TD-OM-01 — relation-only circuit construction

- declared base carrier: finite typed Enterprise transition/incidence skeleton;
- N0 primitives used: state identity, declared incidence/relation membership, task-critical type labels where already native;
- N1 operations used: only when the supplied skeleton itself is an accepted path/process relation such as the R061 trace skeleton;
- N2 readouts used: none in the circuit definition;
- N3 continuum objects used: none;
- implementation carriers used: finite labels for states/edges in the checker only;
- introduced choices: optional edge reference orientation;
- choice-independence certificate: exact reorientation equivariance;
- target leakage audit: `e_1+e_2+e_3=0`, carrier angle, metric and reverse-third shortcut are withheld;
- verdict: `NATIVE_ADMISSIBLE` as a relation-level definable tool when the input incidence relation is N0; otherwise `CONDITIONAL_DERIVED` on the declared accepted N1 skeleton.

### Claim TD-OM-02 — full oriented-matroid status

- critical object: signed support-minimal primitive circulations;
- certificate strength: circuit axioms C0–C3 proved at full signed-circuit strength;
- dual certificate: support-minimal cuts/bonds with circuit/cocircuit orthogonality;
- verdict: `NATIVE_ADMISSIBLE` as the oriented-graphic-matroid structure functorially rebuilt from the typed incidence skeleton, modulo declared reorientation gauge.

### Claim TD-OM-03 — direction-only chirotope

- attempted base: only `{E_1,E_2,E_3}` and current positive-direction labels;
- missing native premise: signed dependency/orientation relation among the three direction elements;
- prohibited substitute: carrier vector identity `e_1+e_2+e_3=0`;
- verdict: `UNRESOLVED / NOT_DERIVED` for a direction-only native chirotope.

### Claim TD-OM-04 — metric erasure

- circuit-calculus dependency DAG contains only typed incidence, finite integer chain arithmetic, support minimality, and orientation gauge;
- metric/carrier payload does not occur;
- exact invariance follows under typed incidence isomorphism and reorientation;
- verdict: `NATIVE_ADMISSIBLE`.

---

## 13. Failure modes and scope limits

The tool must be rejected or retyped when any of the following occurs:

1. **Unlabeled carrier inflation** — a carrier edge is inserted although it is not a native typed transition.
2. **Type erasure** — component labels required to decide native-line membership are forgotten before circuit construction.
3. **Metric promotion** — a circuit support is interpreted as determining length/angle/gauge magnitude.
4. **Boolean inversion claim** — a Boolean-BRC result support is claimed to reconstruct provenance that was already discarded.
5. **Direction-vector leakage** — carrier vector dependency is used to create a signed circuit among the positive Enterprise directions.
6. **Infinite extrapolation without finitary control** — this task proves the finite typed-skeleton calculus. Infinite oriented-matroid extensions are not part of the verdict.

---

## 14. Final classification

All positive-verdict requirements in the taskbook are met:

- coordinate-free primitive definition: **yes**;
- nontrivial signed elimination: **yes**;
- cocircuit/separation and duality: **yes**;
- relabeling/gauge invariance certificate: **yes**;
- metric/carrier erasure pressure test: **yes**;
- executable finite checks: **yes**;
- spatial/incidence reuse: **yes**;
- distinct BRC/provenance reuse: **yes**;
- native versus carrier separation: **yes**;
- conservative historical novelty statement: **yes**.

Final research verdict:

`NATIVE_CIRCUIT_CALCULUS_DISCOVERED`

Driver-review boundary:

This return does **not** modify Foundation definitions and does **not** self-promote the tool into the canonical Foundation/router. If accepted, the strongest reusable payload is the relation-only functor

`TYPED_NATIVE_INCIDENCE_SKELETON -> ORIENTED_GRAPHIC_CIRCUIT/COCIRCUIT_CALCULUS`

plus the provenance diagnostic

`SAME_ENDPOINT_PATH_PAIR -> ZERO-BOUNDARY PATH_DEFECT -> CIRCUIT_DECOMPOSITION`.
