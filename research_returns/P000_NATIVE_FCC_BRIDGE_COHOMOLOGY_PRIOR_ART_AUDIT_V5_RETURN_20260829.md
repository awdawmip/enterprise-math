# P000 native/FCC signed-K4 上同调、S4 提升与双覆盖外部先例审计 V5 — Research Return

Status: `RESEARCH_RETURN_FROZEN / HARD_TARGET_CLOSED_AT_PRIOR_ART_BOUNDARY / AWAITING_DRIVER_REVIEW`

Task: `RS-P000-6D-ROTATION-PRIOR-ART-DUPLICATION-AUDIT`  
Publication: `TP2-63DEB843280700CC0701`  
Researcher-ID: `EM-P0006DPA5-842510`  
Claim: `chatgpt-p0006dpa5-20260829-1502-7f4c2a`  
Execution branch: `research/p000-6d-rotation-prior-art-audit-v5-em-p0006dpa5-842510`

Hard target:

`P000_NATIVE_FCC_S4_COHOMOLOGY_EXTERNAL_DUPLICATION_BOUNDARY_CLASSIFIED`

## 1. Terminal verdict

Freeze the task-level verdict as:

`SUCCESS / CARRIER_DUPLICATION_BOUNDARY_CLASSIFIED / SIGNED_K4_ANTIBALANCE_CLASSICAL / CAMERON_GAMMA_ZERO / CANONICAL_DOUBLE_COVER_BETA_ZERO_AND_SPLIT / P000_NATIVE_COMPATIBILITY_REMAINS_SEPARATE`

The decisive result is stronger and cleaner than the seed note anticipated.

The frozen chart transition signature

`q_AB=-1, q_AC=-1, q_AD=+1, q_BC=-1, q_BD=+1, q_CD=+1`

is not merely “close to” a classical signed-graph object. It is exactly the classical **antibalanced switching class on `K4`**. An explicit vertex switching

`h_A=h_B=h_C=+1, h_D=-1`

takes it to the all-negative signature:

`h_i q_ij h_j = -1` for every edge `ij`.

Consequently:

1. every odd cycle of `K4` is negative and every even cycle is positive;
2. the graph-switching/cochain class is classical;
3. the all-negative representative is strictly fixed by the entire vertex-permutation `S4`;
4. therefore Cameron's invariant-representative obstruction `gamma` vanishes for this carrier instance;
5. in the original gauge, the required correction is an explicit 1-coboundary
   `g_sigma(i)=h_i h_{sigma^{-1}(i)}`;
6. under the standard signed-complete-graph/canonical-cover construction, the double cover is
   `K_{4,4}` minus the same-label perfect matching, hence isomorphic to the cube graph `Q3`;
7. the `S4` action lifts strictly by
   `sigma(i,epsilon)=(sigma(i),epsilon)`, while the deck flip
   `z(i,epsilon)=(i,-epsilon)` is central;
8. therefore the carrier-level extension is the **split** extension
   `S4 x C2`, and Cameron's double-cover obstruction `beta` vanishes;
9. for carrier generators `a=(BCD)`, `b=(AB)`, one may choose lifts with
   `A~^3=e`, `B~^2=e`, `(A~B~)^4=e`, so the central residues are
   `(alpha,beta,gamma)=(0,0,0)`.

This eliminates a major ambiguity for Gen6:

> the accepted `q`-holonomy does **not** force binary octahedral `2O`, `GL(2,3)`, `A4⋊C4`, or any other nonsplit `C2` extension of `S4`.

Those groups are legitimate, classical comparison objects. But if a non-split/projective/groupoid residue later appears in the P000 programme, it must be derived from **P000-native mixed-slice/state legality**, not from the signed-`K4` carrier transition data alone.

No novelty claim is made.

---

## 2. Frozen internal input and typing boundary

This audit accepts only the already frozen carrier interface:

- carrier charts: `A,B,C,D`;
- carrier six lines: the six edges of `K4`;
- physical proper-rotation skeleton: `S4`;
- chart transition signature `q` as listed above;
- every chart triangle loop product is `-1`;
- native six positive axes remain primitive P000 types;
- FCC is only a carrier/readout;
- switching a carrier sign is not a native state operation.

The following guards remain in force:

`CARRIER_SWITCHING_EQUIVALENCE != NATIVE_STATE_EQUIVALENCE`

`EQUAL_CARRIER_READOUT != EQUAL_NATIVE_STATE`

`CHART_SIGN != PRIMITIVE_NATIVE_NEGATIVE_AXIS`

The external prior-art reduction below acts only on the **carrier sign/switching object**.

---

## 3. Exact signed-K4 reduction

Let negative sign be `1 in F2` and positive sign be `0`.

In edge order

`AB, AC, AD, BC, BD, CD`

the frozen signature is

`x=(1,1,0,1,0,0)`.

### 3.1 Cycle certificate

The four triangles have sign:

- `ABC: (-1)(-1)(-1)=-1`;
- `ABD: (-1)(+1)(+1)=-1`;
- `ACD: (-1)(+1)(+1)=-1`;
- `BCD: (-1)(+1)(+1)=-1`.

The three Hamilton 4-cycles have sign `+1`.

Since every simple cycle in `K4` has length 3 or 4, this is the exact antibalance criterion:

`sign(C)=(-1)^{|C|}`.

Equivalently, the signature is switching-equivalent to all-negative.

### 3.2 Explicit switching normal form

Choose

`h=(+1,+1,+1,-1)` on `(A,B,C,D)`.

Then for every edge:

`q'_ij = h_i q_ij h_j = -1`.

Thus the minimal normal form is simply:

`q' = -K4`.

There is no residual asymmetry in the representative.

### 3.3 Graph cohomology / cut-code coordinates

For graph cellular cohomology over `F2`,

`dim H^1(K4;F2)=|E|-|V|+1=3`.

Using spanning tree `AB,AC,AD` and the three fundamental triangles associated to chords `BC,BD,CD`, the cycle-parity coordinate of `[q]` is

`(1,1,1)`.

Equivalently, in the Solé-Zaslavsky coding language, switching by vertex cuts moves inside one coset of the cocycle/cut code; the frozen `q` and all-negative `K4` are two representatives of the same coset.

This class is nonzero as a graph `H^1` class, because triangles are negative. That fact must not be confused with Cameron's **group-cohomological** obstruction `gamma`; these are different cohomology groups answering different questions.

---

## 4. External duplication: balance, antibalance, switching and holonomy

Harary/Zaslavsky signed-graph theory already supplies the relevant structure:

- switching changes edge signs by vertex signs;
- cycle signs are switching invariant;
- balanced means switching-equivalent to all-positive;
- antibalanced means switching-equivalent to all-negative, equivalently even cycles positive and odd cycles negative.

Therefore the following carrier-level statements are not new mathematics:

- triangle products as gauge invariants;
- impossibility of switching this `q` to all-positive;
- interpretation as an antibalanced signed `K4`;
- cut/cocycle-code quotient;
- loop signature / `Z2` holonomy language.

Modern magnetic-signature literature explicitly treats switching as gauge equivalence and the cycle product as the switching-invariant cycle signature. Discrete principal-bundle literature likewise supplies the cochain/curvature/holonomy formalism.

The P000-specific content begins only before or after that abstraction:

- **before** it: the internal FCC chart construction that produced this particular six-entry `q`;
- **after** it: whether carrier data can be realized by legal transformations of full native Cell state.

---

## 5. Cameron cohomology: the first obstruction vanishes

Cameron's 1977 switching-class/two-graph framework is direct prior art for the question:

> a group preserves the switching class; does the class contain a representative fixed by the whole group?

Zaslavsky's annotated bibliography records Cameron's class

`gamma in H^1(G,B^1)`

with the criterion:

`gamma=0` iff `G` fixes a graph/signature in the switching class.

For this task, no abstract computation of a complicated cocycle is required: the all-negative representative is already visibly fixed by every permutation of the four vertices.

Hence:

`G=S4`

and

`gamma=0`.

### 5.1 Original-gauge correction

The original `q` is related to the all-negative representative `q0` by

`q_ij = -h_i h_j`.

For `sigma in S4`, define

`g_sigma(i)=h_i h_{sigma^{-1}(i)}`.

Then switching `sigma.q` by `g_sigma` returns exactly `q`.

Moreover,

`g_{sigma tau}(i) = g_sigma(i) (sigma.g_tau)(i)`.

Thus the gauge-correction system is itself an explicit group 1-coboundary. There is no hidden first-obstruction residue in the carrier sign atlas.

The finite checker exhausts all `24` permutations and all `24^2` composition pairs.

---

## 6. Cameron canonical double cover: the second obstruction also vanishes

Cameron's second cohomology class

`beta in H^2(G, B~^0)`

controls whether the switching-class automorphism group can be realized on the canonical double covering graph.

For the present instance, we can bypass ambiguity by constructing the lift explicitly.

### 6.1 Cover graph

In the all-negative gauge, use vertices

`(i,+), (i,-)` for `i in {A,B,C,D}`.

Each negative edge `ij` lifts across sheets:

`(i,+)--(j,-)` and `(i,-)--(j,+)`.

Therefore the cover is:

`K_{4,4} - {same-label perfect matching}`.

It has:

- `8` vertices;
- `12` edges;
- degree `3`.

An explicit cube-coordinate isomorphism is:

- `A+ -> 000`
- `B+ -> 011`
- `C+ -> 101`
- `D+ -> 110`
- `A- -> 111`
- `B- -> 100`
- `C- -> 010`
- `D- -> 001`.

Adjacency is exactly Hamming distance one. Hence the cover is `Q3`.

### 6.2 Strict lift

For every `sigma in S4`, define

`L_sigma(i,epsilon)=(sigma(i),epsilon)`.

Because the all-negative signature is strictly invariant, `L_sigma` is a graph automorphism and

`L_sigma L_tau = L_{sigma tau}`.

The deck involution

`z(i,epsilon)=(i,-epsilon)`

commutes with all `L_sigma`.

The intersection of the lifted `S4` with `<z>` is trivial, so the generated order-48 group is

`S4 x C2`.

Therefore an explicit section `S4 -> Aut(cover)` exists and:

`beta=0`.

This is stronger than merely saying “some double cover exists”: the exact carrier extension class is split.

---

## 7. Generator presentation and the nonappearance of a central residue

Freeze carrier generators:

`a=(BCD)`,
`b=(AB)`.

They satisfy:

`a^3=e`,
`b^2=e`,
`(ab)^4=e`.

Choose their strict cover lifts through the split section.

Then:

`A~^3=e`,
`B~^2=e`,
`(A~B~)^4=e`.

Thus in the Gen6 notation

`A~^3=z^alpha`,
`B~^2=z^beta`,
`(A~B~)^4=z^gamma`

we obtain:

`(alpha,beta,gamma)=(0,0,0)`.

Associativity is not inferred from these three relations alone; it is already guaranteed because the lift was constructed as an honest permutation representation on the eight cover vertices. The checker verifies the homomorphism and central deck commutation directly.

This closes the carrier-level extension question at task strength.

---

## 8. Comparison with all relevant order-48 C2-over-S4 candidates

External group databases contain the standard split and nonsplit comparison objects.

The three nonsplit central `C2` extensions represented by the GroupNames entries include:

- `C2._1 S4 ~= A4 ⋊ C4` — `SmallGroup(48,30)`;
- `C2._2 S4 ~= CSU(2,3)` — binary octahedral `2O`, `SmallGroup(48,28)`;
- `C2._3 S4 ~= GL(2,3)` — `SmallGroup(48,29)`.

Each has center `C2` and quotient `S4`.

The present carrier data instead admits the explicit split section and therefore realizes:

`C2 x S4`.

So the logical relation is:

`KNOWN_NONSPLIT_2.S4_OBJECTS = VALID_COMPARISON_OBJECTS`

but

`FROZEN_q => NONSPLIT_2.S4`

is false.

In particular:

`Z2_TRIANGLE_HOLONOMY != BINARY_OCTAHEDRAL_OBSTRUCTION`.

If later P000-native generator composition produces a nonsplit residue, that will be additional native structure not contained in the frozen signed-`K4` carrier class.

---

## 9. Star/complement obstruction is also standard carrier combinatorics

The six carrier lines are the six vertices of

`J(4,2)=L(K4)`,

the octahedral graph.

The physical `S4` is induced by permutations of the four underlying `K4` vertices.

For `J(4,2)`, the full graph automorphism group is larger:

`Aut(J(4,2)) ~= S4 x C2`.

The extra `C2` is 2-subset complementation:

`{i,j} -> {A,B,C,D}\{i,j}`.

It commutes with the induced `S4`.

A vertex star in `K4` consists of the three 2-subsets containing a given vertex. Complementation sends it to the complementary triangle on the other three vertices. No vertex permutation in the physical `S4` does this.

Therefore the previously proved P000/FCC carrier fact

`STAR cannot be sent to COMPLEMENTARY_TRIANGLE by physical S4`

is an exact instance of standard `J(4,2)` automorphism structure, not a new carrier theorem.

What remains project-specific is why the old native clone-product factor exchange attempted precisely that star/complement move.

---

## 10. Cameron-Wells, discrete connections, and Rubik methods: exact scope

### Cameron & Wells

`Signatures and signed switching classes` is a genuine external antecedent for the general signed switching formalism. Bibliographic identity was verified. This audit does not attribute a narrower theorem to it beyond what was accessible and crosschecked; the hard lifting criteria are pinned instead to Cameron 1977 through Zaslavsky's annotated theorem summary.

### Discrete connection / magnetic signature literature

This literature is an exact antecedent for:

- signature as gauge data;
- switching equivalence;
- cycle product / loop signature;
- cochain and holonomy language.

It does not supply the P000-native state typing.

### Rubik commutators

Conjugation, commutators and setup moves are standard Rubik-group tools. They are useful as an **adjacent manipulation method** only. They do not determine which `S4` extension is realized by P000 and do not create a native automorphism.

---

## 11. Claim-by-claim external boundary

| Internal claim | Classification | External boundary / exact residue |
|---|---|---|
| `O_FCC ~= S4` | `EXACT_DUPLICATE` | Classical octahedral proper rotation group. |
| faithful `S4` action on six `K4` edges | `EXACT_DUPLICATE` | Standard action on 2-subsets. |
| star/complement obstruction inside physical `S4` | `EXACT_DUPLICATE` | Extra complement `C2` belongs to full `Aut(J(4,2))`, not physical `S4`. |
| exact six-entry internal `q` table | `PARTIAL_ANTECEDENT` | External theory classifies it; internal atlas derives its concrete values. |
| `[q]` is antibalanced | `EXACT_DUPLICATE` | Classical signed-graph class; explicit switching is the finite specialization. |
| triangle holonomy / switching invariance | `EXACT_DUPLICATE` | Signed graph and graph-signature theory. |
| no all-positive switching trivialization | `EXACT_DUPLICATE` | Classical balance theorem. |
| cut-code / switching-class quotient | `EXACT_DUPLICATE` | Solé-Zaslavsky. |
| full `S4` stability of `[q]` | `PARTIAL_ANTECEDENT` | Cameron framework exact; project input specializes to all-negative `K4`. |
| invariant representative / `gamma` obstruction | `PARTIAL_ANTECEDENT` | Cameron criterion exact; `gamma=0` is computed for this input. |
| group-cohomological lift obstruction | `EXACT_DUPLICATE` | Cameron's `H^1/H^2` framework. |
| canonical double-cover lift criterion | `EXACT_DUPLICATE` | Cameron `beta` criterion. |
| this cover is `Q3` and lift is `S4 x C2` | `PARTIAL_ANTECEDENT` | Classical machinery + exact finite specialization. |
| split versus nonsplit `C2` extensions | `EXACT_DUPLICATE` | Standard finite-group extension objects. |
| binary octahedral / `GL(2,3)` comparison | `EXACT_DUPLICATE` | Known order-48 groups; neither is forced here. |
| discrete `Z2` connection language | `EXACT_DUPLICATE` | Magnetic/discrete-connection literature. |
| Rubik commutator/conjugation method | `ADJACENT_METHOD` | Standard technique, no native theorem. |
| P000 mixed native slice geometry | `NO_MATERIAL_MATCH` | No external theorem found that supplies project-specific Cell realization. |
| legal P000 state-level `S4` automorphism | `NO_MATERIAL_MATCH` | Carrier double-cover lift is not a native Cell-state lift. |
| operation-safe prohibition on carrier quotient of native states | `NO_MATERIAL_MATCH` | Internal type/safety condition; no exact external match found. |

Machine-readable exact rows are frozen in:

`research_artifacts/P000_NATIVE_FCC_BRIDGE_COHOMOLOGY_PRIOR_ART_AUDIT_V5/claim_map.json`.

---

## 12. What remains after importing the classical mathematics

The prior-art audit sharply reduces the Gen6 frontier.

The following carrier-level chain is now closed:

`signed q`
`-> antibalanced K4`
`-> all-negative invariant representative`
`-> gamma=0`
`-> canonical cube double cover`
`-> beta=0`
`-> split S4 x C2 lift`.

Therefore Gen6 should **not spend research budget trying to discover a carrier cohomology obstruction that is not there**.

The surviving hard questions are precisely the P000-native ones:

1. Do `J_B={1,4,5}`, `J_C={2,4,6}`, `J_D={3,5,6}` carry legal native Cell slice structures at the required strength?
2. Can the carrier permutations be realized as automorphisms of full native or minimally extended state, not merely axis labels / cover vertices?
3. What hidden state, if any, is required by native support/domain/incidence typing?
4. Does native composition introduce a residue that is absent from the carrier cover?
5. Can all of this be done while preserving:
   `CARRIER_SWITCHING_EQUIVALENCE != NATIVE_STATE_EQUIVALENCE`?

If a nontrivial extension appears there, it is **new input from native legality**, not a consequence of the frozen chart-sign cohomology.

---

## 13. Source-specific audit notes

The source ledger is frozen separately at:

`research_artifacts/P000_NATIVE_FCC_BRIDGE_COHOMOLOGY_PRIOR_ART_AUDIT_V5/source_ledger.json`.

Load-bearing verified sources include:

- Cameron, `Automorphisms and cohomology of switching classes`, JCTB 22 (1977), DOI `10.1016/0095-8956(77)90079-X`;
- Cameron, `Cohomological aspects of two-graphs`, Math. Z. 157 (1977), DOI `10.1007/BF01215145`;
- Cameron & Wells, `Signatures and signed switching classes`, JCTB 40 (1986), DOI `10.1016/0095-8956(86)90088-2`;
- Harary, `On the notion of balance of a signed graph`, DOI `10.1307/mmj/1028989917`;
- Solé & Zaslavsky, `A Coding Approach to Signed Graphs`, DOI `10.1137/S0895480189174374`;
- Lange-Liu-Peyerimhoff-Post, DOI `10.1007/s00526-015-0935-x`;
- Fernández-Juchani-Zuccalli, arXiv `2109.08928`;
- Encyclopedia of Mathematics, `Octahedron`;
- literature giving `Aut(J(4,2))=S4 x S2`;
- GroupNames entries for the order-48 central `C2`-over-`S4` comparison groups;
- Timothy Sun, `Commutators in the Rubik's Cube Group`, DOI `10.1080/00029890.2023.2263158`;
- Zaslavsky's annotated signed/gain-graph bibliography, DOI `10.37236/29`, used to pin the theorem-strength statement of Cameron's `gamma` and `beta` invariants.

No source was treated as proof of novelty by nonappearance.

---

## 14. Reproducibility

Exact checker:

`research_checks/P000_NATIVE_FCC_BRIDGE_COHOMOLOGY_PRIOR_ART_AUDIT_V5_CHECK_20260829.py`

It uses only the Python standard library and verifies:

- all triangle and 4-cycle signs;
- all-negative switching normal form;
- graph `H^1` fundamental cycle coordinates;
- all `24` elements of `S4`;
- every original-gauge correction `g_sigma`;
- all `24^2` cocycle-composition identities;
- the signed cover has 8 vertices, 12 edges, degree 3;
- explicit graph isomorphism to `Q3`;
- strict `S4` cover lift;
- central deck involution;
- split section and generator relations;
- faithful six-edge action;
- complement involution commuting with `S4` but lying outside the physical vertex-permutation `S4`;
- star -> complementary-triangle action of the extra `C2`.

Expected terminal output begins:

`PASS`

and records:

`q_normal_form=all-negative K4`

`gamma_obstruction=0`

`carrier_lift=S4xC2 split`

`carrier_generator_residues=(alpha,beta,gamma)=(0,0,0)`.

The finite data certificate is frozen at:

`research_artifacts/P000_NATIVE_FCC_BRIDGE_COHOMOLOGY_PRIOR_ART_AUDIT_V5/finite_certificate.json`.

---

## 15. Hard-target disposition

The hard target is closed **at prior-art-audit strength**:

`P000_NATIVE_FCC_S4_COHOMOLOGY_EXTERNAL_DUPLICATION_BOUNDARY_CLASSIFIED = YES`.

Exact boundary:

- carrier symmetry, six-edge action, signed switching, antibalance, holonomy, Cameron lifting theory, standard `C2` extensions, and Rubik manipulation methods are classical or direct finite specializations;
- this specific carrier `q` has no nontrivial Cameron `gamma` or `beta` obstruction;
- its canonical cover admits a split `S4 x C2` action;
- P000 mixed native geometry, native legal state automorphisms, and operation-safe no-quotient constraints remain outside the imported classical theorem package.

`NO_MATERIAL_MATCH != NOVELTY`.

Novelty remains undecided and is not claimed.

## 16. Driver recommendation

Driver should consume this return as a **no-reinvention boundary** for the already active Gen6 native-lift task:

1. freeze carrier `gamma=0`, `beta=0`, split `S4 x C2` as baseline;
2. prohibit inference from triangle `Z2` holonomy to binary octahedral/Schur-cover behavior;
3. move all remaining effort to native mixed-slice construction/obstruction and full Cell-state legality;
4. if a non-split/projective/groupoid residue appears, require it to be derived from native state composition/support/domain constraints and compared against the split carrier baseline;
5. preserve the no-quotient typing guard.

No Foundation or Working-Truth promotion is requested by this research return.
