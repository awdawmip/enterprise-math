VERIFY_R3_MINIMAL_C2_REFOUNDATION

# QRF-R3 Independent Foundation Verification — Oriented Origin Triangle and Positive Atlas

Researcher-ID: `EM-QRF3-BEEA43`
Task: `RS-QRF-R3-INDEPENDENT-FOUNDATION-VERIFICATION`
Taskbook source: `41a1bbdf23831f9ad2af160df4a6bd5603f22547`
Owner branch: `research/qrf-r3-independent-foundation-verification`
Frozen Enterprise source snapshot: `d16877c3b62a7d3b7568780c732f610c260c13c1`
Validation mode: post-freeze falsification-oriented verification with the candidate exposed by the taskbook; this is not relabeled as blind discovery.

## 0. Result in one sentence

Under the task-local substrate exactly as frozen, the smallest sufficient primitive is an **orientation element of the two-sheet orientation torsor of the unlabeled elementary triangle**, together with the already-frozen incidence/translation carrier. No base edge, axis ordering, Euclidean embedding, metric angle, or additional sign choice is required. The min-zero construction is a carrier normal-form decoder and does not induce a native diagonal quotient.

Two typing caveats are theorem-critical:

1. the `C2` datum must mean an element `o in Or(T)` of the triangle's orientation torsor (equivalently one bit only after a presentation-level trivialization), not a detached Boolean whose `0/1` values somehow have a canonical meaning;
2. the directed generators `e1,e2,e3` must be names for the **post-orientation directed boundary translation classes**. If an already-directed triple were admitted in the pre-orientation frozen substrate, it would already select the sheet and the orientation datum would be redundant.

These are type clarifications, not extra primitive structure.

---

## 1. Exact task-local substrate and type split

Let `T` be the unlabeled elementary origin triangle with vertex set `V(T)`, `|V(T)|=3`, inside the triangular translation carrier `L`.

Frozen structure used:

- triangle incidence;
- the carrier translation law;
- elementary-triangle translation classes, so that any two consecutive boundary edge translations generate the rank-two carrier translation group;
- the native address target as a min-zero nonnegative three-channel address space.

Not used as premises:

- Euclidean coordinates;
- clockwise/counterclockwise orientation inherited from an embedding;
- metric angle;
- a distinguished base edge;
- a distinguished first vertex;
- a global axis ordering;
- a native diagonal equivalence relation.

The new primitive being tested is one choice

`o in Or(T)`,

where `Or(T)` is the set of the two cyclic orientations of the unlabeled triangle.

Axis names are introduced only as gauge labels after the orientation has generated a cyclically ordered set of three positive direction classes.

---

## 2. A — Exact no-section theorem

### Theorem A1 — orientation set

Define a cyclic orientation of `T` to be an ordering `(v0,v1,v2)` modulo cyclic rotation:

`(v0,v1,v2) ~ (v1,v2,v0) ~ (v2,v0,v1)`.

There are exactly two such classes:

`[v0,v1,v2]` and `[v0,v2,v1]`.

The full automorphism group of an unlabeled triangle is

`Aut(T) ~= S3`.

Its action on `Or(T)` has kernel `A3`: every even permutation is a cyclic relabeling and preserves a cyclic orientation, while every odd permutation reverses the cyclic orientation. Hence

`Or(T) ~= S3/A3 ~= C2`

as an `S3`-set. More precisely, `Or(T)` is a free transitive torsor for the quotient group `S3/A3 ~= C2`; the `S3` action factors through the sign map.

This is the exact version of the informal phrase “the two orientations form a `C2` torsor under triangle automorphisms.” They are not a free `S3` torsor; the stabilizer of each sheet is `A3`.

### Corollary A2 — reflections exchange the sheets

Every reflection of the triangle is represented by an odd permutation, hence exchanges the two elements of `Or(T)`.

### Theorem A3 — no canonical bare-incidence section

There is no `Aut(T)`-equivariant rule that selects one element of `Or(T)` from the unlabeled triangle alone.

Proof. A canonical selection on the unlabeled object would have to be fixed by every automorphism of that object. But an odd automorphism exchanges the two possible orientations, so neither element is fixed by the full `S3`. Contradiction.

### Translation structure does not remove the obstruction

The obstruction survives the distinguished origin and the translation law. Choose two primitive boundary translations `u,v` from one elementary triangle. The additive automorphism

`R(au+bv)=bu+av`

fixes the origin, preserves the triangular neighbor/triangle incidence structure, swaps `u` and `v`, and reverses the two-dimensional chirality. Thus the frozen translation structure still admits an orientation-reversing automorphism fixing the origin triangle setwise. Any datum canonically definable from that frozen structure must be invariant under `R`, so it cannot select one orientation sheet.

Therefore bare incidence plus the frozen translation structure cannot canonically select a single positive orientation.

---

## 3. B — Sufficiency of one orientation datum

Choose

`o=[v0,v1,v2] in Or(T)`.

Orient the three boundary edges cyclically:

`v0 -> v1`, `v1 -> v2`, `v2 -> v0`.

Let their translation classes be

`d0 = [v1-v0]`,
`d1 = [v2-v1]`,
`d2 = [v0-v2]`.

The notation here means carrier translation differences, not Euclidean vectors.

### B1. No base vertex is required

Replacing `(v0,v1,v2)` by a cyclic representative `(v1,v2,v0)` merely cyclically rotates `(d0,d1,d2)`. The **cyclically ordered three-element set**

`D+(o)={d0,d1,d2}`

is therefore well-defined by the orientation class itself. No first vertex or base edge is required.

### B2. Three positive direction families

For each `d in D+(o)`, define the positive ray semigroup at a carrier point `x` by

`Ray_d(x)={x+n d : n in N_0}`.

Translation of these rays over the carrier gives the three positive direction families.

This uses only:

- the chosen cyclic orientation;
- the carrier translation operation;
- nonnegative iteration count.

No metric or embedding is used.

### B3. Carrier closure relation

The directed boundary translations telescope around the triangle:

`d0+d1+d2=0`.

Because the triangle is elementary, any two consecutive boundary translations generate the rank-two carrier translation group. Hence the only integer linear relation among the three is the common diagonal relation described below.

### B4. Cyclic relabeling equivariance

A cyclic relabeling of the vertices cyclically permutes `D+(o)`. Consequently any gauge labeling

`ell: D+(o) -> {E1,E2,E3}`

that respects the cyclic order changes only by a cyclic permutation. The positive direction family as an unlabeled cyclic object is unchanged.

There are three cyclic gauge labelings. The orientation bit does **not** select a unique absolute `E1`; this is not a deficiency because the task freezes axis names as gauge labels only.

A coordinate-free form removes this apparent hidden choice completely: addresses can be treated as functions

`a: D+(o) -> N_0`

with minimum zero. Choosing `E1,E2,E3` only serializes that function as an ordered triple.

### B5. Reflection behavior

An orientation-reversing carrier automorphism `r` sends

`(T,o) -> (rT,ro)`,

where `ro` is the opposite orientation sheet. It sends every oriented boundary edge to the corresponding oriented boundary edge of the reflected oriented triangle. Thus reflection is an isomorphism **between the two oriented objects**, not a fourth choice layered on one oriented object.

If one reverses the orientation sheet while holding the same carrier displacement fixed, all three positive directions are globally reversed, up to a permutation of the three families. This is exactly the expected two-sheet behavior.

Conclusion: one orientation element is sufficient to generate the three positive direction families. No extra base edge, axis order, metric orientation, or embedding is required.

---

## 4. C — Minimality attack

The following attempts were made to remove the orientation datum or to force extra structure.

| Attack | Result |
|---|---|
| Select a sheet from bare triangle incidence | Fails by Theorem A3: an odd triangle automorphism swaps the sheets. |
| Use the distinguished origin | Fails: an orientation-reversing carrier automorphism can fix the origin while swapping two primitive boundary directions. |
| Use only the abelian translation group law | Fails: the translation carrier admits determinant-reversing automorphisms; the group law contains no canonical chirality. |
| Use integer order or the later `min` normalizer | Fails to choose chirality: componentwise minimum is symmetric under coordinate permutations and appears only after a directed presentation exists. |
| Use an embedded clockwise/counterclockwise convention | Killed by task typing: that would import Euclidean/embedding orientation, which is explicitly withheld. |
| Use a pre-directed generator triple | Would make the bit redundant, but that is precisely why `e1,e2,e3` must be typed as post-orientation outputs. A pre-directed triple is an equivalent chiral datum, not smaller frozen structure. |
| Demand a distinguished base edge to orient all edges | Not needed: a cyclic orientation orients the whole 3-cycle at once; changing starting vertex only cyclically relabels the same three direction classes. |
| Demand a fixed axis ordering to form triples | Not ontically needed: use functions on the cyclic three-direction set. Literal tuple slots arise only after a gauge labeling. |
| Treat the primitive as a naked Boolean `b in {0,1}` | Insufficient without a presentation-level identification of Boolean values with the two sheets. The correct primitive is a torsor element `o in Or(T)`, which carries exactly one bit of choice. |

### Minimality conclusion

For the target “a **single** positive atlas” rather than the unresolved two-sheet orientation fiber, the residual ambiguity is exactly a two-element torsor. A selector therefore needs exactly one binary chiral choice in information content.

No smaller datum in the frozen substrate can select a sheet because every frozen-data-definable candidate must be invariant under the reflection that exchanges the sheets.

The minimal primitive is consequently not `triangle + arbitrary named Boolean`; it is

`triangle + one orientation element of its C2 torsor`.

---

## 5. D — Exact min-zero decoder theorem

Work first coordinate-free on `D=D+(o)`.

Let

`Rep_o = Z^D`

be the carrier coefficient presentation module, and define the carrier map

`Phi_o : Z^D -> L`

by

`Phi_o(z)=sum_{d in D} z(d) d`.

After a cyclic gauge labeling this is the familiar map

`Phi(a,b,c)=a e1+b e2+c e3`.

### Theorem D1 — exact kernel

`ker(Phi_o)=Z*1_D`,

where `1_D` is the constant function with value `1` on all three directions. In gauge coordinates:

`ker(Phi)=Z(1,1,1)`.

Proof. The boundary relation gives `d0+d1+d2=0`, so every constant triple lies in the kernel. Conversely, if

`a d0+b d1+c d2=0`,

use `d2=-d0-d1` to obtain

`(a-c)d0+(b-c)d1=0`.

Because `d0,d1` are primitive generators of the rank-two elementary-triangle translation lattice, `a=c` and `b=c`. Hence `a=b=c`.

No metric statement occurs in this proof.

### Theorem D2 — existence of a min-zero representative

Let `z in Z^D`. Define

`m(z)=min_{d in D} z(d)`

and

`N(z)=z-m(z) 1_D`.

Then:

1. `N(z)(d)>=0` for every `d`;
2. `min_d N(z)(d)=0`;
3. `Phi_o(N(z))=Phi_o(z)` because `1_D` lies in the kernel.

Since the elementary boundary translations generate `L`, every carrier displacement has some integer coefficient representative, hence every carrier displacement has a min-zero representative.

### Theorem D3 — uniqueness

Suppose `a,a' in N_0^D` both have minimum zero and

`Phi_o(a)=Phi_o(a')`.

Then by Theorem D1

`a-a'=k 1_D`

for some integer `k`.

Taking minima gives

`0=min(a)=min(a')+k=k`.

Hence `k=0` and `a=a'`.

Therefore each carrier displacement has exactly one min-zero representative.

After a gauge labeling, the normal-form address set is

`A_E={(a,b,c) in N_0^3 : min(a,b,c)=0}`.

### Theorem D4 — gauge equivariance

For any permutation `pi` of the three coefficient positions,

`N(pi z)=pi N(z)`

because componentwise minimum is permutation-invariant. In particular, the decoder is equivariant under all cyclic gauge relabelings allowed by the oriented triangle.

Thus no first-axis convention is hidden in normalization.

---

## 6. Native quotient leakage audit

This is the decisive semantic audit.

### Layer 1 — carrier presentation only

`Z^D` is a coefficient presentation space for carrier translations. Its diagonal kernel is a theorem about **carrier representation**:

`ker(Phi_o)=Z 1_D`.

The statement “two integer coefficient presentations differ by a common diagonal shift iff they encode the same carrier displacement” is allowed only at this carrier layer.

### Layer 2 — normal-form operation

`N(z)=z-min(z)1_D` is a normalization algorithm on carrier representatives. Kernel invariance proves that `N` depends only on the carrier displacement, so it descends to a well-defined decoder

`Dec_o : L -> A_o`,

where

`A_o={a:D+(o)->N_0 : min a=0}`.

This is a section/canonical representative theorem, not an ontology quotient declaration.

### Layer 3 — native address equality remains literal

Inside `A_o`, equality is ordinary componentwise/function equality.

No relation

`a ~ a+k 1_D`

is installed on native addresses.

In fact the min-zero slice gives a strong syntactic firewall:

- if `a in A_o` and `k>0`, then `min(a+k1_D)=k>0`, so `a+k1_D` is **not in `A_o`**;
- if `a in A_o` and `k<0`, at least one zero component of `a` becomes negative, so `a+k1_D` is **not in `A_o`**.

Therefore no two distinct valid native addresses in `A_o` lie on the same nontrivial diagonal shift. The diagonal orbit exists only in the larger carrier presentation module.

### Layer 4 — forbidden inference explicitly rejected

The decoder theorem does **not** license any of the following:

- enlarging the native state space to all of `N_0^3` and quotienting by diagonal shifts;
- treating `(a,b,c)` and `(a+k,b+k,c+k)` as two native states with the same ontology;
- making native operations automatically invariant under diagonal shifts;
- discarding path/provenance fibers because endpoint carrier displacements agree.

Any later theorem that needs such identifications must prove or declare them separately. QRF-R3 does not provide them.

### Leakage verdict

`NO_NATIVE_DIAGONAL_QUOTIENT_LEAK_FOUND`.

The quotient/kernel appears only as the implementation/carrier proof that the normal-form decoder is well-defined and unique.

---

## 7. E — Representation versus ontology audit

### What is generated

1. **Positive direction families**
   - the oriented triangle canonically gives a cyclically ordered three-element set of directed boundary translation classes;
   - nonnegative iteration gives the three positive ray families.

2. **Gauge-labeled coordinates**
   - a cyclic gauge labeling serializes the coordinate-free address function as `(a,b,c)`;
   - changing cyclic gauge cyclically permutes tuple positions;
   - no absolute `E1` is generated.

3. **Carrier-to-native normal-form decoding**
   - the exact diagonal kernel of the carrier coefficient map gives a unique min-zero representative;
   - the decoder is coordinate-permutation equivariant.

### What is not generated

1. **No native diagonal quotient**
   - diagonal equivalence is not a native equality relation.

2. **No metric angle convention**
   - no 60-degree, 120-degree, clockwise Euclidean, dot-product, or angle premise is used.

3. **No unique global axis labeling beyond gauge**
   - orientation supplies cyclic order, not a distinguished first axis.

4. **No path-fiber collapse**
   - the result addresses carrier direction and endpoint/address decoding only.

5. **No free-standing Boolean semantics**
   - the primitive is a selected orientation sheet, not a detached bit with unexplained reference meaning.

---

## 8. Smallest corrected primitive package

The smallest verified package is:

`P_R3 = (T, L, incidence/translation, o)`

with

`o in Or(T)`.

Here:

- `T`, `L`, and the elementary-triangle translation structure are frozen substrate;
- `o` is the sole added primitive choice;
- `Or(T)` is the two-sheet torsor defined from `T`;
- directed boundary translation classes are derived from `(T,o)`;
- axis names are gauge only;
- min-zero normal form is a typed carrier decoder.

No additional base edge, first vertex, axis name, metric orientation, embedding, or order datum belongs in the primitive package.

If an implementation wants a literal Boolean field, it must store that Boolean **relative to a chosen presentation/trivialization of `Or(T)`**. That trivialization is implementation/gauge metadata and must not be mistaken for an additional native geometric primitive.

---

## 9. Kill-condition disposition

| Taskbook kill condition | Outcome |
|---|---|
| Canonical orientation already determined without bit | Not found; ruled out by the reflection/no-section theorem. |
| One bit insufficient without hidden structure | Not found when the datum is correctly typed as `o in Or(T)` and output axes are gauge-labeled. |
| Atlas depends on metric embedding | Not found; construction uses incidence, translation, integer coefficients, and cyclic orientation only. |
| Normal-form proof reinstates native diagonal quotient | Not found; diagonal relation is confined to carrier coefficient kernel and the min-zero slice intersects each diagonal orbit exactly once. |

No kill condition fires.

---

## 10. Executable pressure test

Companion executable:

`research_outputs/qrf_r3_independent_foundation_verification.py`

It checks, on the finite combinatorial model and bounded carrier representatives:

- exactly two cyclic orientation classes;
- even permutations preserve and odd permutations swap orientation sheets;
- no orientation is fixed by the full `S3` action;
- cyclic representatives define the same directed boundary-edge set;
- opposite orientation reverses all directed edges;
- normalizing integer triples preserves carrier displacement;
- normalization is invariant under bounded common diagonal shifts;
- min-zero representatives are unique in the bounded search;
- normalization commutes with coordinate permutations;
- reversing all positive generators induces the expected complement normal-form transform.

The executable is regression evidence only; the infinite claims are carried by the proofs above.

---

## 11. Final verdict justification

All six strict verification requirements in the taskbook are satisfied:

1. exact automorphism/torsor obstruction: proved;
2. sufficiency of one orientation datum: proved without base edge or metric;
3. no smaller frozen datum selects a sheet: proved by an orientation-reversing automorphism preserving the frozen substrate;
4. exact min-zero uniqueness: proved from the exact carrier kernel;
5. no carrier diagonal relation promoted to native equivalence: audited and explicitly blocked;
6. cyclic relabeling and reflection behavior: stated exactly.

The candidate survives independent falsification pressure at the task-local strength. The only correction is terminological/typing precision: say **“one selected element of the orientation `C2` torsor”**, not merely **“one raw Boolean bit”**.