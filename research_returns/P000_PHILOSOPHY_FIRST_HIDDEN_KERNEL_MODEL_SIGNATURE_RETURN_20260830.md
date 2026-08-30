# P000 Philosophy-First Q15 — Nonsplit Hidden-Kernel Minimal Native Signature Return

Status: `FROZEN RESEARCH RETURN / DRIVER REVIEW REQUIRED`

Researcher-ID: `EM-P000-F9683F`  
Task-ID: `RS-P000-PHILOSOPHY-FIRST-HIDDEN-KERNEL-MODEL-SIGNATURE`  
Publication-ID: `TP2-712F3EA72A8A0CBA7446`  
Claim-ID: `chatgpt-phq15-20260830-1947-132355`  
Execution-Record-ID: `ER-238DA8040F3D84D6D280`  
Execution branch: `research/p000-phil-q15-hidden-kernel-model-signature-em-p000-f9683f`  
Execution base: `6c346f37f2a6a61e984bfd7b249a29c6e22598df`

Hard target:

`P000_HIDDEN_KERNEL_NONSPLIT_MODEL_SIGNATURE_MINIMALITY_CLASSIFIED`

Terminal class:

`MINIMAL_NONSPLIT_HIDDEN_KERNEL_SIGNATURE_FOUND`

## 1. Executive result

Q15 closes positively at an explicit finite-model, typed-relational strength.

Starting from the Driver-accepted Q10 signature, it is enough to add one opaque Hidden sort and exactly two semantic relation roles:

1. `HiddenBalance3 ⊂ binom(HiddenPhase,3)`, an internal ternary compatibility relation;
2. `HiddenAxisInc ⊂ HiddenPhase × AxisType`, a typed bridge from Hidden state to the already-derived Q10 carrier stars.

For one 8-point witness, `HiddenBalance3` is the eight-triple 3-uniform hypergraph that admits the certificate presentation

`HiddenPhase = F_3^2 \ {0}`

and

`{x,y,z} ∈ HiddenBalance3  <=>  x+y+z=0`

for three distinct certificate labels. Those coordinates are **not primitives**: the primitive object is only the opaque 8-point hypergraph plus the typed bridge.

The resulting primitive automorphism group is derived exactly:

`Aut_prim(M_NS) ≅ GL(2,3)`,  `|Aut_prim|=48`.

The four carrier fibres are also derived. For distinct Hidden states `x,y`, define their pair codegree as the number of `HiddenBalance3` triples containing both. Exactly four pairs have codegree zero; every other pair has codegree one. These four zero-codegree pairs are the antipodal/projective fibres. `HiddenAxisInc` identifies each such two-point fibre with one of the four Q10 `CarrierStar3` stars.

Hence restriction to the Q10 carrier gives

`rho_M : Aut_prim(M_NS) -> C_M ≅ S4`

with

`|im rho_M|=24`,  `ker rho_M={1,z} ≅ C2`.

The nonidentity `z` is the **derived** global antipode; no sign involution, `C2`, quotient map or group extension is primitive.

The extension is nonsplit. Across all 24 carrier `(3,2,4)` generator pairs and all 96 Hidden lifts, the exact relation residue is

`(AB)^4 = z != 1`.

A homomorphic section would send the quotient relation `(ab)^4=1` to identity, contradiction. Therefore `rho_M` is surjective with nontrivial kernel and has no homomorphic section.

This internalizes the previously external Q10/Q12 `GL(2,3)->PGL(2,3)≅S4` benchmark as the automorphism/readout of a primitive finite relational model, without naming that extension in the signature.

## 2. Primitive signature extension

Retain all Q10 primitive fields:

- `NativeCell`;
- `AxisType`;
- `CarrierStar3`;
- `CellAxisInc`;
- `NativeAdj`;
- the retained framed/PF-10 shell.

Add only:

### 2.1 Hidden sort

`HiddenPhase`

A finite opaque latent-state sort. No element is a native Cell identity and no distinguished Hidden constants are permitted.

### 2.2 Internal Hidden relation

`HiddenBalance3 ⊂ binom(HiddenPhase,3)`.

Semantic reading: three distinct hidden phase/residue states may form one balanced latent relation packet. The relation is unordered and does not expose addition, coordinates, sign, a group law, a quotient or an action.

### 2.3 Carrier bridge

`HiddenAxisInc ⊂ HiddenPhase × AxisType`.

For a Hidden state `h`, its axis neighbourhood must be a Q10 carrier-star triple. In the nonsplit witness every carrier star has exactly two Hidden preimages.

The witness satisfies the coherence law:

two distinct Hidden states have the same carrier-star neighbourhood **iff** their `HiddenBalance3` pair codegree is zero.

This law aligns a relation-derived Hidden fibre with the existing Q10 carrier; it does not identify Hidden state with carrier state.

## 3. Exact 8-point witness

For certificate computation only, label the eight opaque states by the nonzero vectors of `F_3^2`:

`±u, ±v, ±p, ±q`

with certificate coordinates

`u=(1,0)`, `v=(0,1)`, `p=(1,1)`, `q=(1,2)`.

The eight primitive balance triples are:

- `{v+,u+,p-}`;
- `{v+,p+,q-}`;
- `{v+,q+,u-}`;
- `{v-,u+,q-}`;
- `{v-,p+,u-}`;
- `{v-,q+,p-}`;
- `{u+,p+,q+}`;
- `{u-,q-,p-}`.

Every Hidden state lies in three balance triples. Among the 28 unordered pairs, 24 occur in exactly one balance triple and exactly four occur in none. The four zero-codegree pairs are

`{u+,u-}`, `{v+,v-}`, `{p+,p-}`, `{q+,q-}`.

Thus the antipodal pairing is definable from `HiddenBalance3`; it is not primitive.

### Theorem A — primitive automorphism group

`Aut(HiddenPhase,HiddenBalance3) ≅ GL(2,3)` and has order 48.

There are two exact proofs.

First, every invertible linear transformation of the certificate presentation preserves zero-sum triples, giving 48 primitive automorphisms.

Conversely, `HiddenBalance3` defines the unique antipode of every point as its unique codegree-zero partner. Any ordered pair that is neither equal nor antipodal determines the remaining six states through the balance relation. There are

`8 * 6 = 48`

such ordered basis pairs, so an automorphism is determined by the image of one ordered basis pair. Hence there are at most 48 automorphisms.

The checker independently enumerates all `8! = 40320` permutations and obtains exactly 48; their permutation set equals the 48 certificate `GL(2,3)` actions.

### Theorem B — derived carrier quotient

The four zero-codegree pairs form four Hidden fibres. `HiddenAxisInc` ties these bijectively to the four Q10 carrier stars.

The induced action on the four stars contains all 24 permutations. Its kernel has exactly two elements:

`ker rho_M = {1,z}`,

where `z` swaps the two members of every derived fibre simultaneously.

Therefore

`1 -> C2 -> Aut_prim(M_NS) -> S4 -> 1`

is derived from primitive relational automorphisms.

No `C2`, `S4`, `GL(2,3)`, projective-line sort, quotient map or extension law occurs in the primitive signature.

## 4. Nonsplitting certificate

Use the same quotient generator type accepted in Q5/Q12:

`a^3=b^2=(ab)^4=1`,

with `a,b` generating the carrier `S4`.

There are exactly 24 quotient `(3,2,4)` generating pairs. Each carrier element has exactly two Hidden lifts, so there are 96 lifted `(A,B)` pairs across those quotient pairs.

Exact enumeration gives

`(AB)^4=z`

for all 96.

If a section `s:S4->Aut_prim(M_NS)` existed, then for any quotient generating pair

`A=s(a)`, `B=s(b)`

would satisfy

`(AB)^4=s((ab)^4)=1`,

contradicting the census. Thus:

`SURJECTIVE = TRUE`,  
`KERNEL_NONTRIVIAL = TRUE`,  
`SECTION_EXISTS = FALSE`.

This is the required internal nonsplit witness.

## 5. Same-signature Q10 regressions

The extension does not change the problem category: the same **signature** still contains split and no-lift objects.

### 5.1 Split object

Keep eight Hidden states, two over each carrier star, but interpret `HiddenBalance3` coarsely as every triple whose three points lie over three distinct carrier stars. This relation is sign-blind.

Then

`Aut_prim ≅ C2^4 semidirect S4`,  
`|Aut_prim|=384`,  
`|ker rho|=16`,  
`|im rho|=24`.

A section exists: after a certificate-only two-point enumeration in each fibre, move the carrier star and preserve the local bit.

So `SPLIT` remains realizable in the extended signature.

### 5.2 No-lift object

Keep the exact eight-triple nonsplit Hidden relation and the same Hidden bridge, but replace the four one-per-star Cell adjacency from `K4` by the Q10 `P4` witness.

The carrier action is then restricted to `Aut(P4)≅C2`. Exact enumeration gives

`|Aut_prim|=4`,  
`|im rho|=2<24`.

Therefore there is no lift. So `NO_LIFT` also remains realizable in the same signature.

The three regimes are now all internal:

- split;
- no lift;
- surjective nonsplit.

## 6. Deletion audit and minimality

The positive result is not based on adding a disguised extension label.

### 6.1 Delete `HiddenBalance3`

Retain the 8-point Hidden sort and the two-over-one carrier bridge.

Then the two Hidden states above each carrier star may flip independently:

`Aut = C2^4 semidirect S4`,  
`|Aut|=384`,  
`|ker rho|=16`.

A section exists. The nonsplit obstruction disappears.

Therefore an **intra-Hidden coupling relation** is necessary.

### 6.2 Delete `HiddenAxisInc`

Retain the eight-triple Hidden hypergraph and the Q10 Gen12/K4 base.

The Hidden automorphisms and carrier automorphisms decouple:

`Aut = GL(2,3) × S4`,  
`|Aut|=48*24=1152`.

The pure-carrier `S4` factor gives a section of the Q10 readout. The projective quotient naturally visible inside Hidden state cannot be silently identified with the Q10 carrier because no primitive relation connects them.

Therefore a **cross-sort carrier bridge** is necessary.

### 6.3 Delete `HiddenPhase`

This returns exactly to the Q10 Gen12 split base, whose readout is an isomorphism `S4->S4`.

So the Hidden sort is necessary for any nontrivial hidden kernel.

### 6.4 Tuple-packet irreducibility

The eight balance triples form one orbit under the 48-element primitive automorphism group. Deleting any one representative triple drops the automorphism group to order 6 and the carrier image to order 6.

Thus the full eight-triple packet is not carrying redundant tuple data relative to this witness and its full carrier surjectivity.

### 6.5 Exact scope of “minimal”

The result establishes two kinds of minimality:

1. **deletion minimality** of every added primitive field in the witness;
2. **relation-role minimality under typed semantic discipline**: at least one internal Hidden coupling is needed, and at least one Hidden-to-carrier bridge is needed; the construction uses exactly one relation of each role.

No absolute syntax-symbol minimality is claimed against artificial arity fusion that packs several semantic roles into one giant relation. Such coding would fail the Q8 lowest-sufficient-abstraction discipline even if it reduced the raw symbol count.

## 7. Circularity audit

The following are explicitly absent as primitives:

- the opposite/sign involution;
- a four-element projective quotient sort;
- the central `C2`;
- `GL(2,3)` or any multiplication table;
- the map `GL(2,3)->S4`;
- a section or “no section” predicate;
- a cocycle / obstruction bit;
- the relation residue `(AB)^4`;
- Q12 holonomy.

All are derived after primitive automorphism enumeration.

The only classical coordinates appear in the checker/certificate as a compact presentation proving what the opaque relational structure is isomorphic to. Replacing the labels by any isomorphic 8-point relation table leaves the primitive model unchanged.

Therefore the construction does not obtain nonsplitting by inserting the desired extension, quotient or residue as data.

## 8. Q12 residue / holonomy becomes a genuine derived observable

Q12 accepted the rule that for the untwisted connection induced from the same extension lifts,

`H_ind = R`.

In the Q15 nonsplit model, the extension itself is now derived from `Aut_prim(M_NS)` and `rho_M`. The unique nonidentity kernel element `z` is derived from primitive automorphisms.

For every `(3,2,4)` lifted pair,

`R=(AB)^4=z`.

Applying the already-accepted Q12 induced-connection construction to the actual eight-edge `(ab)^4` relation loop therefore gives

`H_ind=R=z`.

Nothing called residue or holonomy was added to the Q15 primitive signature.

If a later model adds an independent kernel-valued connection twist, Q12/T9 remains the controlling law

`H=R*D`;

Q15 neither erases nor pre-fixes `D`.

## 9. Why this is not merely the old external GL(2,3) benchmark

The old Q10 boundary started with an external group extension and observed its quotient/kernel behavior.

Q15 reverses the direction:

`primitive relational model`  
`-> primitive-preserving automorphisms`  
`-> derived 48-element group`  
`-> derived four-fibre action`  
`-> derived kernel`  
`-> derived nonsplitting residue`.

The certificate later identifies those derived objects with the classical names `GL(2,3)`, `PGL(2,3)≅S4` and central `C2`. The classical identification is a theorem about the model, not model membership data.

This is exactly the semantic internalization Q10 left open.

## 10. Tool reuse

Existing Enterprise tools cover the reusable method layer:

- `T7_FINITE_SYMMETRY_EQUIVARIANCE`: automorphism, orbit, kernel and section/canonicality audit;
- `T9_HOLONOMY_COCOYCLE_GLUING`: reuse of the Q12 residue/induced-holonomy semantics;
- `T2_BLOCK_FINITE_CERTIFICATE`: exact finite counter/deletion certificates.

No new global tool family is proposed. The 8-point `HiddenBalance3` witness is a task-local result.

## 11. Deterministic checker

Checker:

`research_checks/P000_PHILOSOPHY_FIRST_HIDDEN_KERNEL_MODEL_SIGNATURE_CHECK_20260830.py`

Finite certificate:

`research_artifacts/P000_PHILOSOPHY_FIRST_HIDDEN_KERNEL_MODEL_SIGNATURE/P000_Q15_HIDDEN_KERNEL_MODEL_SIGNATURE_CERTIFICATE_V1.json`

The checker verifies, using only the Python standard library:

- 8 Hidden states and exactly 8 balance triples;
- pair codegrees `24×1 + 4×0`;
- four derived antipodal fibres;
- exact `8!` automorphism census `|Aut|=48`;
- equality of that automorphism permutation set with the 48 `GL(2,3)` certificate actions;
- full carrier image of order 24 and kernel order 2;
- 24 quotient `(3,2,4)` generator pairs;
- all 96 lifted pairs having `(AB)^4=z`;
- same-signature split model `|Aut|=384`, kernel 16, section exists;
- same-signature P4 no-lift model `|Aut|=4`, carrier image 2;
- all three field-deletion audits;
- one-balance-tuple deletion drops `|Aut|` and carrier image to 6;
- Q12 untwisted induced-holonomy readout `H_ind=R=z`.

Local execution in this research turn:

`PASS / MINIMAL_NONSPLIT_HIDDEN_KERNEL_SIGNATURE_FOUND`.

## 12. Driver recommendation

Accept at the exact declared finite relational strength:

`P000_MINIMAL_TYPED_HIDDEN_BALANCE_PLUS_CARRIER_BRIDGE_INTERNALIZES_A_NONSPLIT_HIDDEN_KERNEL_MODEL`.

The useful doctrine is:

`A NONSPLIT HIDDEN KERNEL MAY BE CALLED NATIVE ONLY AFTER BOTH THE HIDDEN COUPLING AND ITS CARRIER BRIDGE ARE PRIMITIVE-SEMANTIC, WHILE THE KERNEL, QUOTIENT, GROUP EXTENSION AND RESIDUE ARE DERIVED FROM AUTOMORPHISMS.`

No Foundation, Working Truth or bare-P000 group identification should be promoted from this single finite witness.

## Boundary / non-claims

- No claim that `F3^2`, `GL(2,3)`, `S4` or central `C2` is a universal P000 ontology.
- No claim of absolute one-symbol/minimum-arity definability.
- No claim that every nonsplit extension can be internalized by a ternary Hidden relation.
- No noncentral/nonabelian Q12 holonomy law is inferred.
- No classical group/cohomology novelty claim is made.
- No canonical promotion authority is requested; Driver review is required.
