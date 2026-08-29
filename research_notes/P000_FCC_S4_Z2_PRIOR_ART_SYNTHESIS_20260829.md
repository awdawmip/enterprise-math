# P000 FCC-S4 / Z2 holonomy external prior-art synthesis — 2026-08-29

Status: `DRIVER_EXTERNAL_SYNTHESIS / NO_NOVELTY_CLAIM / INPUT_TO_GEN6`

Driver: `EM-DVR-7C31A8`

## 0. Purpose

This note records a bounded external literature search used to prevent the P000 native/FCC programme from rediscovering standard symmetry, signed-graph, switching, holonomy, group-extension, or Rubik-group mathematics.

It does **not** judge or weaken P000. External conventional dimensionality cannot reduce the native six-axis space.

Search date: `2026-08-29`.

Main search surfaces: general web index, journal/publisher pages, university research portals, arXiv metadata, Encyclopedia of Mathematics.

## 1. Findings already standard in external mathematics

### A. FCC/cuboctahedral proper rotation group ~= S4 — STANDARD

The orientation-preserving octahedral/cubic rotational group has order 24 and is isomorphic to `S4`; the cuboctahedron carries the same proper octahedral rotational symmetry.

Relevant sources:

- Encyclopedia of Mathematics, `Octahedron`, citing Coxeter, *Regular Polytopes*; the octahedral group freely permutes four opposite-face pairs / cube diagonals and is `S4` of order 24.
- Standard group/symmetry lecture notes independently derive the cuboctahedron rotational group as `S4`.

Classification for our programme: `EXACT_ANTECEDENT` for the bare carrier statement `O_FCC ~= S4`.

No novelty may be claimed for this group identification.

### B. S4 action on six K4 edges / 2-subsets — STANDARD

The six edges of `K4` are the six 2-subsets of a four-set. The induced `S4` action is the standard 6-point permutation representation.

Also, `L(K4)` is the octahedral graph / Johnson graph `J(4,2)`.

Important nuance: the **full graph automorphism group** of `J(4,2)` is larger (`S4 x C2`) because complementing a 2-subset is an extra graph automorphism. The 24 proper spatial rotations correspond to the `S4` subgroup, not automatically the whole graph automorphism group.

Relevant sources:

- Lévêque et al., JCTB: `L(K4)` is the octahedron.
- Johnson-graph automorphism literature: `Aut(J(4,2)) = S4 x S2`.
- Standard equivariant representation notes explicitly use the `S4` vertex action on `K4` and the induced six-edge action.

Classification: `EXACT_ANTECEDENT` for the six-edge action; `USEFUL_BOUNDARY` for physical `S4` versus combinatorial extra `C2`.

### C. Edge-sign switching, negative cycle products, balance / antibalance — CLASSICAL

For a signed graph, the product of edge signs around a cycle is invariant under vertex switching/gauge change. A signed graph is balanced iff all cycles are positive; it is antibalanced iff every even cycle is positive and every odd cycle is negative, equivalently iff it is switching-equivalent to the all-negative signature.

Therefore, the accepted FCC chart transition signature on chart graph `K4`, with every triangle loop product `-1`, is not a new abstract phenomenon: it is precisely a classical unbalanced/antibalanced signed-graph switching class.

Relevant sources:

- Harary balance theory as summarized in modern signed-graph literature.
- Zaslavsky, *Negative (and positive) circles in signed graphs: A problem collection*.
- Recent signed-graph work restating: antibalanced iff even cycles are positive and odd cycles negative.

Classification: `EXACT_ANTECEDENT` for switching invariance and no all-positive gauge; `EXACT_REINTERPRETATION` for our `q_ij` chart-sign data as an antibalanced signature on `K4`.

### D. Discrete connection / cycle holonomy — STANDARD

Graph signatures with values in a group are treated as discrete connections; the ordered product around a cycle is the cycle signature/holonomy and is switching invariant up to conjugacy. Discrete connection form/curvature can be formulated cohomologically.

Relevant sources:

- Lange et al., *Frustration index and Cheeger inequalities for discrete and continuous magnetic Laplacians*: cycle signature is the product around a loop and is switching invariant.
- Fernández, Juchani, Zuccalli, *Discrete connections on principal bundles: abelian group case* (2021): discrete connection and curvature as cochains, with discrete loop holonomy formula.

Classification: `EXACT_ANTECEDENT` for abstract `Z2` connection/holonomy language.

### E. Cohomological lifting of automorphisms of switching classes / two-graphs — VERY CLOSE PRIOR ART

This is the most important external antecedent for the current frontier.

Peter J. Cameron studied automorphisms and cohomology of switching classes in 1977. His subsequent work on two-graphs develops cohomological obstructions for whether a group of automorphisms fixes a representative and whether it lifts to the canonical double cover. Cameron and Wells (1986) further developed signatures and signed switching classes.

Zaslavsky's bibliography summarizes the two-graph theory as follows: signed complete graphs are 1-cochains over `GF(2)`; switching adds a 1-cocycle; a switching class is a coset; group-cohomology classes `gamma in H^1(...)` and `beta in H^2(...)` control invariant representatives and lifting to the canonical double cover.

Relevant sources:

- Peter J. Cameron, `Automorphisms and cohomology of switching classes`, JCTB 22 (1977), 297–298.
- Peter J. Cameron, `Cohomological aspects of two-graphs`, Math. Z. 157 (1977), 101–119.
- Peter J. Cameron and A. L. Wells Jr., `Signatures and signed switching classes`, JCTB 40 (1986), 344–361.

Classification: `CLOSE_STRUCTURAL_ANTECEDENT` for our question "does carrier S4 lift through a Z2 chart state / double cover?".

This prior art means the project must compute the exact cohomological class rather than merely observe `Z2 holonomy` and call it new.

### F. Double covers / central extensions of S4 — STANDARD

The proper octahedral group `S4` has well-known nontrivial double covers. In particular, the binary octahedral group `2O` of order 48 is the preimage of the octahedral rotation group under `Spin(3) -> SO(3)`. Literature also distinguishes two Schur covers of `S4`, including `GL(2,3)` and the binary octahedral group.

Relevant sources:

- Springer material on the Hurwitz order / binary octahedral group: `2O -> S4` is a 2:1 central cover of the octahedral group.
- Group-theory literature on the two Schur covers of `S4`.

Classification: `EXACT_ANTECEDENT` for the existence of nontrivial `C2` central extensions of `S4`.

Critical guard: **our chart `Z2` holonomy does not by itself prove that the native lift is binary octahedral, a Schur cover, or any particular central extension.** The extension class must be derived from native composition laws.

### G. Rubik commutators / conjugation / setup moves — STANDARD

Use of conjugates and commutators to move and localize cube actions is standard group-theoretic cubing technique. Modern mathematical treatments explicitly develop commutators and conjugacy in the Rubik group.

Classification: `EXACT_ANTECEDENT` for the method template; no novelty claim.

## 2. What was NOT located as a standard external theorem in this bounded search

The following **combined** problem was not found as an off-the-shelf theorem:

1. six P000-native positive axis types are primitive and not quotiented by carrier relations;
2. FCC is a chosen lower-dimensional coordinate/readout carrier;
3. four overlapping native candidate 3-axis stars `J_A,J_B,J_C,J_D` must each recover the established Enterprise `120 degree` slice geometry at declared strength;
4. chart orientation is allowed to be local carrier state but not a primitive native negative axis;
5. an `S4` carrier action must be lifted to legal transformations of the full native Cell state preserving native adjacency/relations;
6. equal carrier readout may not identify distinct native states;
7. failure must be classified as exact native obstruction, minimal state extension, central extension, cocycle, or groupoid.

This absence is **not a novelty proof**. Part of the non-match is expected because P000/native Cell definitions are project-specific.

Classification: `NO_EXACT_EXTERNAL_MATCH_FOUND_IN_BOUNDED_SEARCH / NOVELTY_UNDECIDED`.

## 3. Main synthesis

The external literature strongly suggests the next task should not start from geometry pictures. It should first convert the accepted chart transition data into standard signed-graph/cohomological language, then ask what survives after imposing P000 native-state legality.

Recommended algebraic pipeline:

`FCC chart transition signs`
`-> signed K4 / switching class`
`-> exact H^1/cycle class`
`-> S4 action on switching class`
`-> group-cohomological lifting obstruction`
`-> candidate C2 extension / double cover / groupoid`
`-> native mixed-slice realization`
`-> native state-level rotation composition`
`-> carrier readout regression`.

## 4. Explicit research guards produced by this search

- `O_FCC ~= S4` is standard, not a novelty target.
- `S4` on six `K4` edges is standard, not a novelty target.
- negative cycle products / switching invariance / antibalance are standard.
- `Z2 holonomy` as a graph-connection concept is standard.
- cohomological obstruction to lifting automorphisms of switching classes has direct prior art.
- `2O` / Schur double covers of `S4` are standard candidate comparison objects.
- the project must **derive**, not guess, whether its native lift is split, centrally extended, projective, groupoid-valued, or impossible.
- any eventual novelty claim must live in the exact P000-native compatibility theorem/obstruction, not in the classical ingredients.

## 5. Recommended successor

Upgrade the current bridge task to a prior-art-informed generation whose hard target is:

`P000_NATIVE_MIXED_STAR_COHOMOLOGY_AND_MINIMAL_ROTATION_LIFT_EXACTLY_CLASSIFIED`.

The first mandatory lemma should identify the accepted chart-sign system as a precise switching/cohomology class on `K4`; the second should compute the `S4` equivariance/lifting obstruction before attempting a native geometric construction.
