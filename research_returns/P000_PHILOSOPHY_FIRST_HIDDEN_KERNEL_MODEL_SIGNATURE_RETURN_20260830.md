# P000 Philosophy-First Q15 - Hidden-Kernel Native Signature Return

Status: `FROZEN RESEARCH RETURN / DRIVER REVIEW REQUIRED`

Researcher-ID: `EM-P000-F9683F`
Task-ID: `RS-P000-PHILOSOPHY-FIRST-HIDDEN-KERNEL-MODEL-SIGNATURE`
Publication-ID: `TP2-712F3EA72A8A0CBA7446`
Claim-ID: `chatgpt-phq15-20260830-1947-132355`
Execution-Record-ID: `ER-238DA8040F3D84D6D280`
Execution branch: `research/p000-phil-q15-hidden-kernel-model-signature-em-p000-f9683f`
Execution base: `6c346f37f2a6a61e984bfd7b249a29c6e22598df`

Hard target: `P000_HIDDEN_KERNEL_NONSPLIT_MODEL_SIGNATURE_MINIMALITY_CLASSIFIED`

Terminal class: `MINIMAL_NONSPLIT_HIDDEN_KERNEL_SIGNATURE_FOUND`

## 1. Result

Q15 has a positive exact finite answer. Extend the Driver-accepted Q10 signature by only:

- one opaque sort `HiddenPhase`;
- one internal ternary relation `HiddenBalance3`;
- one typed bridge `HiddenAxisInc` from `HiddenPhase` to the existing Q10 `AxisType`.

For the nonsplit witness, `HiddenPhase` has 8 opaque points. A certificate labels them by the nonzero vectors of `F_3^2`, and `HiddenBalance3` contains the 8 unordered triples of distinct certificate vectors whose sum is zero. The coordinates are only a checker presentation. They are not primitive fields.

For distinct hidden points, pair codegree in `HiddenBalance3` is either 1 or 0. Exactly 4 pairs have codegree 0 and the other 24 pairs have codegree 1. The 4 zero-codegree pairs are therefore definable inside the primitive ternary relation. `HiddenAxisInc` maps the two members of each such pair to the same Q10 carrier-star triple, giving a typed bridge to the existing carrier.

Exact enumeration gives

`Aut_prim(M_NS) = Aut(HiddenBalance3) ~= GL(2,3)`

with order 48. Its action on the 4 derived carrier fibres has image of order 24 and kernel of order 2:

`rho_M : Aut_prim(M_NS) -> C_M ~= S4`,
`ker(rho_M) = {1,z} ~= C2`.

The nonidentity `z` swaps the two members of every derived fibre simultaneously. The sign involution, `C2`, `GL(2,3)`, the quotient map and the extension are not primitive.

Across all 24 carrier `(3,2,4)` generating pairs and all 96 lifted pairs, the checker finds

`(AB)^4 = z != 1`.

A homomorphic section would send `(ab)^4=1` to identity, which contradicts this census. Thus `rho_M` is surjective, has nontrivial kernel, and is nonsplit.

## 2. Primitive witness and derivation

The Q10 core stays unchanged: `NativeCell`, `AxisType`, `CarrierStar3`, `CellAxisInc`, `NativeAdj`, and the retained framed/PF-10 shell.

The only new relation roles are:

1. `HiddenBalance3 subset binom(HiddenPhase,3)`: an internal latent compatibility relation.
2. `HiddenAxisInc subset HiddenPhase x AxisType`: a cross-sort bridge whose neighbourhood at each hidden point is one Q10 carrier-star triple.

For the 8-point witness, the certificate labels are

`u=(1,0)`, `v=(0,1)`, `p=(1,1)`, `q=(1,2)` and their negatives.

The 8 balance triples are:

- `{v+,u+,p-}`
- `{v+,p+,q-}`
- `{v+,q+,u-}`
- `{v-,u+,q-}`
- `{v-,p+,u-}`
- `{v-,q+,p-}`
- `{u+,p+,q+}`
- `{u-,q-,p-}`

The opposite pairing is not supplied. It is derived as the unique pair-codegree-zero relation.

Every invertible linear map in the certificate preserves the 8 triples, yielding 48 automorphisms. Conversely, an automorphism is fixed by the image of any ordered non-antipodal pair; there are exactly `8*6=48` such ordered pairs. Hence there are at most 48 automorphisms. The exhaustive `8!` census independently confirms exactly 48 and verifies that its permutation set equals the 48 certificate `GL(2,3)` actions.

The four codegree-zero pairs are mapped by `HiddenAxisInc` to the four Q10 carrier stars. The induced star action contains all 24 permutations and its kernel is exactly `{1,z}`.

## 3. Same-signature regressions

The extended signature still contains all three logical regimes.

### Split

Use the same 8 hidden points and two-over-one carrier bridge, but interpret `HiddenBalance3` coarsely as all triples lying over three distinct carrier fibres. Then

`|Aut_prim|=384`,
`|ker rho|=16`,
`|im rho|=24`.

The group is the split wreath-type `C2^4 semidirect S4`, and an explicit homomorphic section exists.

### No lift

Keep the exact 8-triple hidden witness and bridge, but use the Q10 `P4` NativeAdj on the four one-per-star Cells. Then

`|Aut_prim|=4`,
`|im rho|=2<24`.

So no lift exists.

### Surjective nonsplit

Use the exact 8-triple hidden witness, bridge, and the Q10 K4 base. Then

`|Aut_prim|=48`,
`|ker rho|=2`,
`|im rho|=24`,
`SECTION_EXISTS=FALSE`.

Thus split, no-lift and surjective-nonsplit all occur inside the same signature.

## 4. Deletion audit

Delete `HiddenBalance3` but keep the two-over-one bridge. The hidden states above each carrier star flip independently:

`Aut = C2^4 semidirect S4`, order 384, kernel order 16.

A section returns. Therefore an intra-Hidden coupling relation is necessary.

Delete `HiddenAxisInc` but keep the exact hidden ternary structure over the Q10 K4 base. Hidden automorphisms and carrier automorphisms decouple:

`Aut = GL(2,3) x S4`, order 1152.

The pure carrier factor gives a section. Therefore a cross-sort bridge is necessary.

Delete `HiddenPhase`. The model returns to the Q10 Gen12 split base, whose carrier readout is an isomorphism.

The 8 balance triples form one orbit under the 48-element primitive automorphism group. Deleting one balance tuple drops the automorphism group and carrier image to order 6, so the full 8-tuple packet is irredundant for this full-surjectivity witness.

This proves deletion minimality and relation-role minimality under typed semantic discipline: one internal Hidden coupling role and one Hidden-to-carrier bridge role are both necessary, and the construction uses exactly one relation of each role. No absolute one-symbol minimality is claimed against artificial arity fusion.

## 5. Circularity test

The primitive signature does not contain:

- an opposite/sign involution;
- a four-element projective quotient sort;
- `C2`;
- `GL(2,3)` or a group multiplication table;
- a quotient homomorphism;
- a section/nonsection bit;
- a cocycle or obstruction label;
- `(AB)^4`;
- Q12 residue or holonomy.

All of these are derived after primitive automorphism enumeration. The `F_3^2` coordinates occur only in the deterministic certificate, so relabelling the 8-point relation by any isomorphism changes no primitive model data.

Therefore the nonsplit extension is not inserted by hand.

## 6. Q12 derived observable

Q12 accepted the untwisted induced-connection law `H_ind=R`.

Here the extension itself is now derived from `Aut_prim(M_NS)` and `rho_M`, and the unique nonidentity kernel element `z` is derived. The exact lift census gives

`R=(AB)^4=z`

for every `(3,2,4)` lifted pair. Applying the already-accepted Q12 construction to the actual eight-edge `(ab)^4` loop gives

`H_ind=R=z`.

Neither residue nor holonomy is primitive in Q15. If an independent kernel-valued twist is later added, Q12/T9 remains controlling with `H=R*D`; Q15 does not pre-fix `D`.

## 7. Tool reuse and exact checker

Reused methods:

- `T7_FINITE_SYMMETRY_EQUIVARIANCE`
- `T9_HOLONOMY_COCOYCLE_GLUING`
- `T2_BLOCK_FINITE_CERTIFICATE`

No new global tool family is proposed.

Checker:

`research_checks/P000_PHILOSOPHY_FIRST_HIDDEN_KERNEL_MODEL_SIGNATURE_CHECK_20260830.py`

Finite certificate:

`research_artifacts/P000_PHILOSOPHY_FIRST_HIDDEN_KERNEL_MODEL_SIGNATURE/P000_Q15_HIDDEN_KERNEL_MODEL_SIGNATURE_CERTIFICATE_V1.json`

The checker uses only the Python standard library and verifies:

- 8 hidden points, 8 balance triples;
- pair codegrees `24x1 + 4x0`;
- 4 derived opposite fibres;
- exact `8!` automorphism census, order 48;
- equality with the 48 `GL(2,3)` certificate actions;
- carrier image 24 and kernel 2;
- 24 quotient `(3,2,4)` generator pairs;
- all 96 lifted pairs satisfy `(AB)^4=z`;
- split regression: order 384, kernel 16, section exists;
- no-lift regression: order 4, carrier image 2;
- all field deletions above;
- one tuple deletion gives automorphism/image order 6;
- Q12 untwisted readout `H_ind=R=z`.

Local execution in this research turn:

`PASS / MINIMAL_NONSPLIT_HIDDEN_KERNEL_SIGNATURE_FOUND`.

## 8. Driver recommendation and boundary

Recommended exact finite conclusion:

`P000_MINIMAL_TYPED_HIDDEN_BALANCE_PLUS_CARRIER_BRIDGE_INTERNALIZES_A_NONSPLIT_HIDDEN_KERNEL_MODEL`.

No Foundation, Working Truth or bare-P000 group identification is requested.

Non-claims:

- no universal claim that `F_3^2`, `GL(2,3)`, `S4` or central `C2` is P000 ontology;
- no absolute minimum-arity or one-symbol definability claim;
- no claim that every nonsplit extension admits this ternary construction;
- no noncentral/nonabelian Q12 law;
- no classical group/cohomology novelty claim.

Driver review is required.
