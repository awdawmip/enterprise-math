# RS-NOLLM-EISENSTEIN-ROTATION-ATLAS — Research Return

- Researcher-ID: `EM-NOLLM-F697FD`
- Publication: `TP2-983B1B8DB12B245368D9`
- Claim: `chatgpt-nollm-atlas-20260828-claim1`
- Execution branch: `research/nollm-eisenstein-rotation-atlas-em-nollm-f697fd`
- Taskbook blob: `afe40fd2687e264717aa1f24636ca4cc2b52091a`
- Verdict: **THEOREM PACKAGE COMPLETE FOR H1–H5; H6 BOUNDED RESIDUE; H7 REUSE-ONLY**

## 0. Executive result

The frozen NollM/进取 planar bridge admits a clean exact integration without replacing native Cell semantics by the geometric carrier.

The main theorem package is:

1. the unit triangular center lattice has a unique-address regular-hexagonal Voronoi core of side `1/sqrt(3)` whose vertices are exactly the triple boundary intersections of the radius-`1/sqrt(3)` circle family;
2. the center-to-triple-intersection refinement is the exact Eisenstein index-three extension `alpha^{-1} Lambda`, split into three cosets and classified in pointy-top axial coordinates by `q-r mod 3`;
3. the existing path jet is precisely a normalized oriented triangle moment, hence its closed-path tower inherits exact subdivision, reversal, concatenation, translation and affine covariance laws;
4. rotation/scale phase is finite exactly at lattice commensurability, not merely at nesting; Eisenstein nested refinement has phase count `3^k`, while `a=2/3` gives a minimal useful commensurable-but-nonnested example with nine phases;
5. these pieces compose only as a typed mixed invariant: native displacement/positive-axis data stay native, chart holonomy stays chart-typed, and Euclidean moment tensors stay carrier/readout unless separately promoted;
6. in characteristic `p`, `(x^p-x)^(p-1)` is an explicit `F_p semidirect F_p^*` invariant of degree `p(p-1)`, but no canonical map from that affine invariant to the enterprise path-jet first-bad obstruction was derived. The equal degree/order is therefore retained only as a structural lead.

No new broad tool family is justified. Existing T3/T5/T7/T9 families cover incidence, refinement, finite symmetry and holonomy; only a task-local exact checker was added.

---

## 1. H1 — Circle halo / hex core

Let `Lambda=Z[omega]`, with nearest-neighbor distance one, and put a circle of radius `R=1/sqrt(3)` at every lattice point.

### Theorem H1.1 — Voronoi core

The Voronoi cell `V_0` at the origin is a regular hexagon with

- inradius `1/2`,
- circumradius `1/sqrt(3)`,
- side length `1/sqrt(3)`.

**Proof.** The six nearest neighbors lie at the six Eisenstein units. Their perpendicular bisectors are all at distance `1/2` from the origin and differ by sixty-degree rotations, hence bound a regular hexagon. The intersection of two adjacent bisectors is the circumcenter of a unit equilateral triangle, so its distance to each of the three triangle vertices is the equilateral circumradius `1/sqrt(3)`. A regular hexagon has side equal to circumradius. QED.

### Theorem H1.2 — Triple intersections are exactly Voronoi vertices

Every Voronoi vertex is the circumcenter of an elementary unit equilateral triangle and therefore lies on exactly the three radius-`1/sqrt(3)` circle boundaries centered at that triangle's vertices. Conversely every triple boundary intersection of three nearest-center circles arises as such an elementary-triangle circumcenter, hence is a Voronoi vertex.

In Eisenstein coordinates one representative is

`c=(2+omega)/3`.

Its squared distances to `0`, `1`, and `1+omega` are all `1/3`.

### Theorem H1.3 — Non-overlapping transfer kernel

Choose a deterministic half-open boundary convention for the Voronoi cells `{V_t}` so that they form a measurable disjoint partition. For any finite source measure `mu_s`, define

`K(s->t) := mu_s(V_t)`.

Then

`sum_t K(s->t) = mu_s(R^2)`.

The proof is countable additivity on a disjoint partition. This is the correct mass-conserving cross-layer transfer. Summing overlapping target circles is forbidden because it double-counts halo overlap.

**Semantic status.** Circle Cell/triple incidence remain native candidates. The hexagon is a unique-address carrier partition, not a replacement native Cell.

---

## 2. H2 — Exact center/intersection refinement

Let

`alpha=1-omega`, `N(alpha)=3`, `c=alpha^{-1}=(2+omega)/3`.

### Theorem H2.1 — Three-coset decomposition

`alpha^{-1} Lambda = Lambda disjoint_union (c+Lambda) disjoint_union (2c+Lambda)`.

**Proof.** Multiplication by `alpha` has lattice index `N(alpha)=3`, so `alpha^{-1}Lambda/Lambda` has order three. Since `c notin Lambda` and `3c=2+omega in Lambda`, the class of `c` has exact order three and generates the quotient. QED.

The two nonzero cosets are the two orientations of elementary-triangle circumcenters/triple intersections. A triple intersection becomes a center only after attaching the finer-layer tag.

### Theorem H2.2 — Exact axial matrix and classifier

Use pointy-top axial basis

`z=q+r*zeta`, where `zeta=1+omega`.

Equivalently in the algebraic basis, `Q=q+r`, `R=r`, so `z=Q+R*omega`.

Multiplication by `c` gives

`c(Q+R*omega)=((2Q-R)/3)+((Q+R)/3)*omega`.

Therefore `cz in Lambda` iff `Q+R=0 mod 3`, which in axial coordinates is

`q-r = 0 mod 3`.

In axial coordinates the fine map is

`c(q,r)=((q-r)/3, (q+2r)/3)`,

with rational matrix

`C=(1/3) [[1,-1],[1,2]]`.

The inverse coarse map, multiplication by `alpha`, is

`A=[[2,1],[-1,1]]`, `det A=3`.

This explains why the taskbook's `q-r mod 3` classifier is compatible with the Eisenstein algebraic basis rather than contradicting it.

### Theorem H2.3 — Two steps are scale 1/3 up to unit

Direct multiplication gives

`alpha^2=-3 omega`.

Hence

`alpha^{-2}=(-omega^2)/3`.

Thus two refinement steps are Euclidean scale `1/3` followed by multiplication by an Eisenstein unit, i.e. a lattice-preserving rotation.

---

## 3. H3 — Path jet equals normalized oriented moment

For

`T(u,v)=conv{0,u,u+v}`,

parameterize `x=s u+t v`, `0<=t<=s<=1`, and then write `t=s r`.

The oriented area element becomes `det(u,v) s ds dr`, so

`int_T x^{odot n} dA_or`

`= det(u,v)/(n+2) * int_0^1 (u+r v)^{odot n} dr`.

The coefficient of `u^{odot(n-k)} odot v^{odot k}` is therefore

`det(u,v) * C(n,k) / ((n+2)(k+1))`.

Meanwhile

`((X+Y)^{n+1}-X^{n+1})/Y`

has coefficient `C(n+1,k+1)`, and

`C(n+1,k+1)=((n+1)/(k+1)) C(n,k)`.

Therefore:

### Theorem H3.1 — Normalized oriented-moment identity

`J_n(u,v)=(n+1)(n+2) int_T x^{odot n} dA_or`.

For a closed polygonal path `gamma=(P_0,...,P_m=P_0)` with `D_i=P_i-P_{i-1}`, define

`A_n(gamma)=sum_i J_n(P_{i-1},D_i)`.

It follows from oriented integration that:

1. **subdivision:** inserting a point on an edge leaves `A_n` unchanged;
2. **reversal:** `A_n(gamma^{-1})=-A_n(gamma)`;
3. **concatenation:** closed-path concatenation is additive;
4. **linear covariance:** `A_n(L gamma)=det(L) L^{odot n} A_n(gamma)`;
5. **translation:**

`A_n(gamma+a)=sum_{k=0}^n C(n,k) * ((n+1)(n+2))/((k+1)(k+2)) * a^{odot(n-k)} odot A_k(gamma)`.

At `n=0`,

`A_0=sum_i det(P_{i-1},D_i)`,

which is the twice-signed-area coordinate and hence the frozen `Omega_2` normalization. At `n=1`, `A_1` belongs to `det(V) tensor V`; this is exactly the determinant-twist of the standard representation, i.e. the signed-standard component.

**Semantic status.** These are Euclidean chart tensors. Equality with an already-native scalar invariant at `n=0` does not automatically promote every higher moment to native status.

---

## 4. H4 — Rotation/scale phase classification

For nonzero complex scalar `a`, define the translation-phase quotient

`Phi(a)=(a Lambda + Lambda)/Lambda`.

There is a canonical isomorphism

`Phi(a) ~= a Lambda / (a Lambda intersection Lambda)`.

Hence:

### Theorem H4.1 — Finite phase iff commensurable

`Phi(a)` is finite iff `a Lambda` and `Lambda` are commensurable, and then

`|Phi(a)|=[a Lambda : a Lambda intersection Lambda]`.

For the Eisenstein lattice this occurs iff `a in Q(omega)^*`.

**Proof.** If the lattices are commensurable, the displayed finite-index quotient is finite. Conversely finite phase means the intersection has finite index in `aLambda`, and symmetry of two full rank lattices gives commensurability. If `aLambda` is commensurable with `Lambda`, then `a*1` lies in the rational span `Q tensor Lambda=Q(omega)`. Conversely if `a in Q(omega)^*`, clearing denominators gives a common finite-index sublattice. QED.

### Regime classification

1. **Exact resonant:** `aLambda=Lambda`. For scalar multiplication this means `a` is one of the six Eisenstein units `+-1, +-omega, +-omega^2`.
2. **Commensurable nested:** for `a=alpha^{-k}`, the phase count is exactly `3^k`.
3. **Commensurable nonnested:** finite phase but neither lattice contains the other. Example `a=2/3`: intersection is `2Lambda`, so
   `[ (2/3)Lambda : 2Lambda ]=3^2=9`.
4. **Noncommensurable/nonresonant:** `a notin Q(omega)`, so the phase orbit is infinite.

No density/equidistribution statement is claimed in regime 4; that requires an additional Diophantine theorem.

---

## 5. H5 — Integrated typed invariant

The correct integration object is not one untyped geometric tuple. Define

`H_{<=N}(gamma)=(D_net,H_+; Hol_chart; A_0,...,A_N)`

with the following mandatory attachments:

- `D_net`, `H_+`: native relational/positive-axis data;
- `Hol_chart`: typed source-chart -> target-chart transport data;
- each `A_n`: value in `det(V) tensor Sym^n(V)` at a declared Euclidean carrier chart;
- `layer_id` and refinement direction;
- exact `phase_class` when finite, or `NONCOMMENSURABLE_PHASE` otherwise;
- coordinate convention and orientation tag.

Composition is legal only when source/target types, layer, phase, and orientation agree.

Recommended failure certificates:

- `TYPE_MISMATCH`
- `LAYER_MISMATCH`
- `PHASE_UNRESOLVED`
- `NONCOMMENSURABLE_PHASE`
- `ORIENTATION_LOST`
- `GEOMETRIC_ONLY`
- `BOUNDARY_DOUBLE_COUNT`

This preserves the project's native/derived hierarchy while still allowing NollM's atlas machinery to serve as an exact readout/transport carrier.

---

## 6. H6 — Prime-index bridge: theorem plus bounded residue

Let `p` be prime and let `AGL(1,p)=F_p semidirect F_p^*` act on `F_p[x]` by `x -> a x+b`.

Put

`f_p(x)=x^p-x`.

For `b in F_p`, Freshman's dream gives

`f_p(x+b)=(x+b)^p-(x+b)=x^p-x`.

For `a in F_p^*`,

`f_p(a x)=a(x^p-x)`.

Therefore

### Theorem H6.1 — Explicit affine invariant

`I_p(x)=(x^p-x)^{p-1}`

is invariant under the full affine group, and

`deg I_p=p(p-1)=|AGL(1,p)|`.

This makes the repeated `p(p-1)` genuinely structural on the finite-affine side: it comes from translation invariance at degree `p` plus removal of the multiplicative character by power `p-1`.

### Obstruction to the requested path-jet identification

No canonical morphism/intertwiner was derived from this invariant polynomial to the enterprise path-jet first-bad obstruction module. The latter depends on modular symmetric-power/divisibility structure, while the former lives in a one-variable affine invariant ring. Equal degree and equal group order alone do not identify those modules.

**Disposition: `BOUNDED_RESIDUE`.** The affine-side theorem is proved; the bridge to path-jet first-bad degree is not.

**First exact next lemma:** construct the mod-`p` representation carrying the first nonzero path-jet obstruction at degree `p(p-1)` and test whether its obstruction line admits an `AGL(1,p)`-equivariant map from the line spanned by `I_p`. A zero Hom-space would refute the bridge cleanly; a one-dimensional Hom-space would turn the degree coincidence into a genuine structural candidate.

---

## 7. H7 — Tool reuse matrix

| Required capability | Existing Enterprise tool family | Disposition |
|---|---|---|
| center/intersection precision change | `T5_PRECISION_REFINEMENT` — Integer Precision / Refinement Calculus | REUSE |
| finite phase/orientation group action | `T7_FINITE_SYMMETRY_EQUIVARIANCE` — Finite Symmetry / Orbit / Equivariance Calculus | REUSE |
| triple/path incidence certificates | `T3_TYPED_INCIDENCE_CIRCUIT` — Typed Incidence Circuit Calculus | REUSE |
| chart/loop transport | `T9_HOLONOMY_COCOYCLE_GLUING` — Holonomy / Cocycle / Gluing-Obstruction Calculus | REUSE |
| exact task integration checks | task-local `scripts/check_nollm_eisenstein_rotation_atlas.py` | NEW LOCAL ONLY |

No general capability gap remains that justifies a new top-level tool family.

---

## 8. Exact tests and adversarial checks

The stdlib-only exact checker uses integers and `Fraction`; no floating nearest-point selection appears.

Passed checks include:

- H1: exact squared circumradius/side `1/3`, inradius `1/4`, representative triple intersection;
- H2: `alpha^2=-3omega`, index `3`, 625 axial points checked against `q-r mod 3`;
- H3: 861 exact binomial/moment coefficient identities through degree 40; translation coefficients through degree 20;
- H4: nested phase counts through `k=8`, six Eisenstein units, and the `a=2/3` nine-phase nonnested counterexample to a nesting-only criterion;
- H6: characteristic-`p` polynomial prerequisites for `p=2,3,5,7,11,13,17,19`.

Artifacts:

- checker: `scripts/check_nollm_eisenstein_rotation_atlas.py`
- report: `research_artifacts/NOLLM_EISENSTEIN_ROTATION_ATLAS/exact_check_report.json`
- checker SHA256: `c6d423d31bac94ab0bc01c0b37e41c9c2a632fac38c6174bed32e8f42ecc0993`
- report SHA256: `7289b33d43199d0250edcb8b02e276aecdaeb56f6899a3259e7a884d2b74c1f2`

---

## 9. Failed branches / semantic downgrades

1. **Finite phase = nested refinement** — false. `a=2/3` is a nine-phase commensurable nonnested counterexample.
2. **Nonresonant phase is automatically dense/equidistributed** — not proved; downgraded to infinite phase only.
3. **Circle disks can be target partition cells** — rejected because overlaps double-count mass. Voronoi hex cores supply the non-overlapping partition.
4. **Triple intersection = same-layer center** — rejected. It is a center only in the tagged refined layer.
5. **All higher Euclidean moments are native invariants** — rejected absent a separate semantic derivation.
6. **`p(p-1)` equality proves the prime/path-jet bridge** — rejected. Only the affine invariant theorem survives; the cross-module relation remains unresolved.

---

## 10. Research frontier

The strongest next move is not more numerical sweeping. It is representation-theoretic and exact:

> Compute the mod-`p` path-jet obstruction module at the first-bad degree and determine the `AGL(1,p)` Hom-space from the affine invariant line generated by `(x^p-x)^{p-1}`.

In parallel, the H4 phase quotient can be attached to NollM's rotation atlas as an exact resonance classifier: finite atlas phases exactly on `Q(omega)^*`, with `3^k` phases on the canonical `alpha^{-k}` refinement chain. This supplies an exact mathematical control layer for later recursive shell-alignment / three-dimensional rotating-coordinate research without confusing carrier geometry with native semantics.
