# P000 framed Full-Cell `S4` lift universality, canonicality and relation-residue classification V13 — Research Return

Status: `FROZEN RESEARCH RETURN / DRIVER REVIEW REQUIRED`

Researcher-ID: `EM-P000FCC13-8D2C41`  
Task-ID: `RS-P000-L1-NATIVE-CARRIER-CONTACT-BRIDGE`  
Publication-ID: `TP2-6E1A9C3B7D5048F2A611`  
Claim-ID: `chatgpt-p000fcc13-20260830-1024-8d2c41`  
Execution-record-ID: `ER-2050E1BD7919C3C6F710`  
Result-ID: `RR-E1438E73B8EDBA797602`  
Execution branch: `research/p000-s4-lift-universality-extension-v13-em-p000fcc13-8d2c41`  
Execution base: `6a4c6ff9e0b2e916af659d2681f9b666d59db682`

Hard target:

`P000_FRAMED_FULL_CELL_S4_LIFT_UNIVERSALITY_CANONICALITY_AND_RELATION_RESIDUE_EXACTLY_CLASSIFIED`

Primary terminal classes:

- `NONTRIVIAL_FULL_CELL_RELATION_EXTENSION_OF_S4_EXACTLY_CLASSIFIED`
- `BARE_P000_UNIVERSAL_OR_CANONICAL_S4_LIFT_EXACTLY_OBSTRUCTED_WITH_MODEL_CLASS_BOUNDARY`

## 1. Executive result

V13 closes the structural lifting question at the exact **extension/readout criterion** level and separates four logically different issues which Gen12 could not decide from one positive witness.

Let `M` be a declared framed/PF-10 Full-Cell model, let `Aut_enr(M)` be its actual enriched automorphism group, and let `Gtilde` be the subgroup whose axis-type readout lies in the frozen carrier-compatible `S4` action. Define the actual readout homomorphism

`q : Gtilde -> S4`

and

`K = ker(q)`.

Then:

1. an exact simultaneous carrier-`S4` lift is precisely a homomorphic section `s:S4->Gtilde` with `q∘s=id`; such a section is automatically injective, hence faithful;
2. if `q` is surjective but no such section exists, the model is a **nonsplit extension** and exact native `S4` closure fails even though every carrier element has enriched preimages;
3. if the image of `q` is smaller than the frozen `S4`, there is a direct **no-lift** obstruction before extension theory enters;
4. splitting does not imply canonicality: a section is canonical only if it is invariant under the primitive-preserving automorphisms of the declared model/extension data.

The deterministic checker supplies four finite separating regimes:

| model | `|Gtilde|` | `|K|` | `|im q|` | split? | canonical? | decisive feature |
|---|---:|---:|---:|---|---|---|
| accepted Gen12 regression | 24 | 1 | 24 | yes | not asserted from bare P000 | exact faithful witness |
| 4 two-Cell fibers | 384 | 16 | 24 | yes | **no** | `C2^4 ⋊ S4`, actual within-fiber Cell swaps |
| hidden `F3^2` relation | 48 | 2 | 24 | **no** | n/a | `GL(2,3) -> PGL(2,3)`, invariant `(AB)^4=-I` |
| native `P4` adjacency | 2 | — | 2 | no lift | n/a | Cell-adjacency automorphism image too small |

Consequently Gen12 proves existence in one model, but current bare P000 does **not** force universal existence or a canonical section. The correct frozen boundary is

`UNIVERSAL_BARE_P000_S4_LIFT_NOT_DERIVABLE`

together with

`LIFT_EXISTS_BUT_NO_CANONICAL_SECTION`

for the explicit split nontrivial-kernel model below.

This does not refute P000 and does not promote `S4` to the complete native P000 rotation group. It isolates the extra relational content required for such a promotion.

## 2. Frozen carrier action and tagged-sort regression

Use the accepted four carrier vertices `A,B,C,D` only as a carrier atlas. The frozen generators are

`a=(B C D)`, `b=(A B)`,

and their six-edge action is

`a_xi=(E1 E2 E3)(E4 E6 E5)`,

`b_xi=(E2 E4)(E3 E5)`,

with `E1,E6` fixed under `b_xi`.

The checker independently obtains:

- `a^3=id`;
- `b^2=id`;
- `(ab)^4=id`;
- `|<a,b>|=24`;
- the six-edge image also has order `24` and trivial kernel.

Every V13 model uses disjoint typed identifiers such as

`("CarrierVertex","A")`

versus

`("NativeCell",...)` or `("NativeCellLine",...)`.

Thus the regression freezes

`CARRIER_VERTEX_TAG != NATIVE_CELL_ID_TAG`.

No theorem below depends on numeric aliasing between carrier vertices and native Cell identities.

## 3. General lifting object and exact split criterion

For a declared model `M`, `Gtilde` is not a formally adjoined group. It consists only of actual enriched automorphisms preserving the retained native Cell relations, PF-10 data, retained connection data and hidden relational state, with frozen axis readout in the carrier `S4`.

The map

`q:Gtilde->S4`

is induced by that readout. Its kernel contains precisely those actual enriched automorphisms invisible to the frozen axis readout.

### Theorem 3.1 — section criterion

The following are equivalent.

1. The full frozen carrier `S4` has an exact simultaneous enriched lift in `M`.
2. There exists a homomorphism `s:S4->Gtilde` with `q∘s=id`.
3. The exact sequence over the frozen image splits.

Moreover any such `s` is injective: if `s(g)=id`, then `g=q(s(g))=id`. Therefore a split lift is automatically a faithful enriched representation of the carrier `S4`.

A set-theoretic section is insufficient; it need not preserve multiplication. A chosen homomorphic section is also not automatically canonical.

This theorem is a structural criterion, not a claim that every possible extension group has been classified up to isomorphism.

## 4. Relation residues and change of lift

Let `A,B in Gtilde` satisfy

`q(A)=a`, `q(B)=b`.

Define

`z_a=A^3`, `z_b=B^2`, `z_ab=(AB)^4`.

Because the corresponding carrier words are identity,

`q(z_a)=q(z_b)=q(z_ab)=id`,

so all three residues lie in `K`.

If `A' = kA` with `k in K`, then

`(kA)^m = k (A k A^-1) ... (A^(m-1) k A^(-(m-1))) A^m`.

Thus a residue may change by a genuine twisted norm in the kernel. It is not legitimate to erase that kernel action by quotient and then announce an exact native `S4`.

The examples below show all relevant possibilities:

- residues can be lift-dependent and removable;
- residues can be noncentral in the full enriched group even when `K` is abelian;
- a residue can be central and **invariant under every allowed lift choice**, giving an exact nonsplitting certificate.

## 5. Gen12 regression: `K=1 / SPLIT / FAITHFUL / RESIDUE_TRIVIAL`

The accepted Gen12 common model is retained exactly as a regression, not re-proved as a new P000 axiom.

It has four opaque native Cells with `K4` adjacency, uniform PF-10 state, a frame-induced identity connection, and strict lifts of the frozen `a,b`.

The checker recovers:

- enriched group order `24`;
- axis image order `24`;
- `K=1`;
- exact relations `A^3=B^2=(AB)^4=id`.

Hence Gen12 remains the trivial-kernel split corner of the V13 classification.

## 6. Exact split nontrivial-kernel Full-Cell model

### 6.1 Native semantic model

Take eight distinct opaque native Cells

`x_(i,epsilon)`, `i in {A,B,C,D}`, `epsilon in C2`.

They are partitioned into four **unoriented two-Cell fibers**. Declare native Cell adjacency between every pair belonging to different fibers; equivalently the Cell graph is the complete four-partite graph `K_(2,2,2,2)`. No `0/1` orientation inside a fiber is declared as primitive data.

Use uniform PF-10 ingress/egress and `M=I_6`, together with a frame-induced trivial-holonomy connection. These decorations impose no extra symmetry breaking.

An enriched automorphism may:

- independently swap the two actual Cell identities in any of the four fibers;
- permute the four fibers.

Therefore the actual enriched symmetry group is

`Gtilde = C2^4 ⋊ S4 = C2 wr S4`

of order

`16*24 = 384`.

The readout `q` records only the induced permutation of the four fibers and then the accepted six-edge carrier action. Hence

`K=C2^4`

has order `16` and consists of **actual native Cell permutations**, not inert labels.

The checker exhaustively verifies all 384 transformations preserve the native Cell adjacency relation.

### 6.2 Splitting

The zero-flip lift

`s0(sigma)=(0,sigma)`

is a homomorphic section. Therefore this model is split and carries an exact faithful enriched `S4` despite its nontrivial kernel.

For the frozen generator fibers there are `16*16=256` choices of enriched lifts `(A,B)`. Exact enumeration gives:

- `16` distinct residue triples `(z_a,z_b,z_ab)`;
- exactly `16` generator pairs have all three residues identity;
- each all-trivial pair generates an order-24 complement, hence a homomorphic section.

The residue sets are:

`z_a in {0000,1000,0111,1111}`,

`z_b in {0000,1100}`,

`z_ab in {0000,1111}`

for the checker's fixed coordinate convention.

Only `0000` and `1111` are central in the full wreath product; therefore some lift-dependent residues are genuinely noncentral enriched-state data.

### 6.3 Exact noncanonicality

The `16` homomorphic sections split into exactly two conjugacy orbits under the primitive-preserving kernel `K`, each of size `8`.

More strongly, the checker computes

`C_Gtilde(K)=K`.

Suppose a section were canonical under every primitive-preserving within-fiber Cell swap. Then for every `k in K` and `g in S4`,

`k s(g) k^-1 = s(g)`.

Thus `s(g)` would lie in `C_Gtilde(K)=K`. But then

`q(s(g))=id`,

contradicting `q(s(g))=g` for any nonidentity `g`.

Therefore no homomorphic section is fixed by all primitive-preserving kernel conjugations:

`LIFT_EXISTS_BUT_NO_CANONICAL_SECTION`.

This is a direct automorphism-orbit certificate, not a philosophical uniqueness argument.

## 7. Exact surjective nonsplit model: `GL(2,3)`

### 7.1 Semantic hidden relation

Let the hidden relational sort be

`V=F3^2`

with its exact addition relation. Introduce four distinct native Cell-line anchors, one for each one-dimensional subspace of `V`, and retain the incidence relation

`Inc(v,C_L) <=> v is a nonzero vector on line L`.

Give the four Cell-line anchors `K4` adjacency and uniform PF-10 / frame-induced connection data.

Every additive automorphism of `V` is an element of `GL(2,3)`, and incidence determines its induced permutation of the four Cell-line anchors. Conversely every `GL(2,3)` matrix preserves addition and incidence. Thus the declared enriched automorphism group is exactly

`Gtilde=GL(2,3)`

of order `48`.

Projectivizing its action on the four one-dimensional subspaces yields exactly the 24 permutations of the accepted carrier `S4`. The checker does not assume the isomorphism from a name: it enumerates all 48 matrices, obtains 24 projective permutations, and verifies equality with the frozen `S4` set.

The kernel is

`K={I,-I}`.

It is an actual hidden relational symmetry: `-I` fixes every projective Cell-line anchor and every axis readout, but sends each nonzero hidden vector `v` to `-v`.

### 7.2 Frozen generator residues

For the fixed carrier generators the two possible matrix lifts of `a` are

`A1=[[1,1],[0,1]]`, `-A1=[[2,2],[0,2]]`

over `F3`.

The two lifts of `b` are

`B1=[[0,1],[1,0]]`, `-B1=[[0,2],[2,0]]`.

All four lift pairs are exhaustively checked.

For every pair:

- `B^2=I`;
- `(AB)^4=-I`;
- `<A,B>` has order `48`.

For `A^3`, one scalar choice gives `I` and the other gives `-I`.

Because the kernel is central, changing lifts by scalars `epsilon,delta in {I,-I}` gives

`A -> epsilon A`, `B -> delta B`.

Then

`A^3 -> epsilon^3 A^3`,

`B^2 -> delta^2 B^2 = B^2`,

`(AB)^4 -> (epsilon delta)^4 (AB)^4 = (AB)^4`.

Hence the product relation residue

`z_ab=-I`

is invariant under **every** allowed lift choice.

No homomorphic section can exist: a section would send the frozen `a,b` to one of these four lift pairs and would have to satisfy the exact carrier relation `(ab)^4=id`, contradicting `(AB)^4=-I`.

Thus this is an exact, semantically realized, central nonsplit extension. The projective `S4` readout is valid, but quotienting away `-I` is not permission to call the enriched native action an exact `S4`.

## 8. Exact no-lift model from native adjacency

Take four opaque native Cells with path adjacency

`x0 - x1 - x2 - x3`.

Use uniform PF-10 data and a frame-induced identity connection so those decorations introduce no obstruction.

The exact automorphism group of the native `P4` adjacency has order `2`: identity and path reversal.

The frozen base generator `a=(BCD)` has order `3` and is not an automorphism of this Cell relation. Under the fixed labels `b=(AB)` is also absent.

Therefore the enriched readout image cannot contain the frozen `S4`, and there is no simultaneous lift.

The obstruction is concrete:

`CELL_ADJACENCY_AUTOMORPHISM_IMAGE_TOO_SMALL`.

It occurs before any hidden-kernel or cohomological issue.

## 9. Bare-P000 universality

The current accepted dependencies explicitly preserve the following boundary:

- Gen11: bare P000 does not assert that a global `r_b` exists;
- Gen12: bare P000 does not force the four-Cell `K4` witness or canonically choose `r_a,r_b`;
- the global P000/FCC algebra keeps `NATIVE_S4_NOT_GRANTED=true`.

At the current task strength, native adjacency is retained data that a strict lift must preserve, but no root axiom forces every Full-Cell model to have the Gen12 `K4` adjacency or the required PF-10/connection symmetries.

Therefore the positive Gen12 model and the explicit `P4` no-lift model separate existence from universality.

Freeze:

`UNIVERSAL_BARE_P000_S4_LIFT_NOT_DERIVABLE`.

This is a model-class boundary. If a later Foundation/Driver action adds relational axioms excluding the `P4`-type countermodel and forcing an appropriate split extension, the conclusion must be revisited under that stronger theory.

## 10. Canonicality is strictly stronger than existence

V13 now has an exact independence witness:

- the wreath model admits `16` homomorphic sections;
- all are moved in two 8-element kernel-conjugacy orbits;
- `C_Gtilde(K)=K`, so no section can be invariant under all primitive-preserving kernel automorphisms.

Hence even a split extension with many exact faithful `S4` lifts need not carry a canonical one.

This closes the logical implication error

`LIFT_EXISTS => CANONICAL_LIFT`.

It is false in the declared Full-Cell model class.

## 11. Structural classification theorem

For the current framed/PF-10 Full-Cell lifting problem, once the actual enriched automorphism group and readout `q` are fixed, the exact decision tree is:

1. **Readout failure**: if `im(q)` does not contain the frozen carrier `S4`, no simultaneous lift exists.
2. **Surjective nonsplit**: if `q` is onto but has no homomorphic section, individual carrier transformations may lift, but there is no exact enriched `S4`; relation residues provide finite certificates when computed.
3. **Split**: if a homomorphic section exists, it is injective and gives an exact faithful enriched `S4` lift.
4. **Canonicality**: after splitting, canonicality requires a section fixed by the primitive-preserving automorphism action on the section set; it is an additional condition and can fail.

The Gen12, wreath, `GL(2,3)` and `P4` models realize these distinctions exactly.

This is an exact structural classification of the lifting regimes. It is **not** a classification up to isomorphism of every finite group extension of `S4`.

## 12. Connection and PF-10 boundary

The new obstructions do not depend on abusing connection terminology.

- The split wreath and `GL(2,3)` models use uniform PF-10 data and frame-induced connections with trivial loop holonomy.
- The `P4` model also uses trivial-holonomy connection data, so its failure is purely native adjacency.
- V11's theorem remains in force: an independent connection with nontrivial holonomy can still admit a symmetry if the holonomy representation transforms equivariantly.

Accordingly V13 uses

`TRIVIAL_HOLONOMY / SYNCHRONIZABLE / PURE_GAUGE_TRANSPORT`

where global synchronized framing is meant. It does not assert standard `flat <=> global frame`.

## 13. Classical-method boundary

The language of kernels, exact sequences, sections, split extensions, wreath products, `GL(2,3)`, projective actions and group cohomology is classical machinery.

V13 makes no historical novelty claim for it.

No `H^2` computation is used. In particular, the noncentral behavior in the wreath model is handled by exact semidirect-product enumeration, while the `GL(2,3)` obstruction is demonstrated directly by all four generator lift pairs. This avoids applying ordinary abelian-coefficient `H^2` outside its hypotheses.

The project-specific content is the typed Full-Cell realization, the carrier/native readout firewall, and the exact model boundary under the currently frozen P000 primitives.

## 14. Deterministic evidence

Checker:

`research_checks/P000_S4_LIFT_UNIVERSALITY_EXTENSION_V13_CHECK_20260830.py`

Model-class certificate:

`research_artifacts/P000_S4_LIFT_UNIVERSALITY_EXTENSION_V13/MODEL_CLASS_CERTIFICATE.json`

Exact checker output:

```text
PASS P000_S4_LIFT_UNIVERSALITY_EXTENSION_V13_CHECK
terminal_class=NONTRIVIAL_FULL_CELL_RELATION_EXTENSION_OF_S4_EXACTLY_CLASSIFIED / BARE_P000_UNIVERSAL_OR_CANONICAL_S4_LIFT_EXACTLY_OBSTRUCTED_WITH_MODEL_CLASS_BOUNDARY
gen12_split_faithful_K_order=1
tagged_carrier_native_cell_disjoint=true
frozen_axis_image_order=24
wreath_group_order=384
wreath_kernel_order=16
wreath_axis_image_order=24
wreath_generator_lift_pairs=256
wreath_distinct_residue_triples=16
wreath_exact_homomorphic_sections=16
wreath_section_K_conjugacy_orbits=2
wreath_section_orbit_sizes=8,8
wreath_centralizer_of_kernel_order=16
wreath_canonical_section_fixed_by_kernel=false
gl23_group_order=48
gl23_kernel_order=2
gl23_axis_image_order=24
gl23_generator_lift_pairs=4
gl23_all_product_relation_residue=-I
gl23_homomorphic_section_exists=false
p4_native_adjacency_aut_order=2
p4_frozen_a_lift_exists=false
universal_bare_p000_s4_lift_not_derivable=true
full_native_rotation_group_promoted=false
carrier_kernel_quotiented_to_manufacture_s4=false
time_rotated=false
```

The checker uses only the Python standard library and performs exact finite enumeration.

## 15. Hard-target disposition

Hard-target disposition: `SUCCESS AT STRUCTURAL MODEL-CLASS BOUNDARY`.

What is exactly classified:

- the readout/section/splitting criterion;
- relation residues as genuine kernel elements;
- a split faithful model with nontrivial semantic Cell kernel;
- exact noncanonicality in that split model;
- a semantically realized central nonsplit extension with an invariant relation residue;
- an exact adjacency-based no-lift countermodel;
- non-derivability of a universal or canonical lift from the currently frozen bare-P000 primitives.

What is **not** claimed:

- complete classification of all finite `S4` extensions up to isomorphism;
- bare P000 has native rotation group `S4`;
- carrier equality identifies native Cell identity;
- hidden kernel may be quotiented away to manufacture a native theorem;
- local channel `S6` is promoted to native symmetry;
- Gen12's `K4` Cell graph is canonical;
- every independent connection has trivial holonomy;
- time rotates;
- any classical group-extension method is new.

Recommended Driver disposition:

Accept V13 at the exact structural model-class strength above. Freeze the four-regime decision tree, `UNIVERSAL_BARE_P000_S4_LIFT_NOT_DERIVABLE`, and the explicit noncanonical/nonsplit certificates. Any stronger theorem that P000 itself supplies a canonical native `S4` requires **new primitive relational axioms or a new theorem excluding the countermodels**, not another relabeling of the carrier atlas.
