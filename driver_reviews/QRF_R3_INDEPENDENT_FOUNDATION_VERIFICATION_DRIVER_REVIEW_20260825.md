# Driver Review — QRF-R3 Independent Foundation Verification

Status: `DRIVER_ACCEPTED_WITH_TYPING_NARROWING / MINIMAL_C2_ORIENTATION_TORSOR VERIFIED / NO_NATIVE_DIAGONAL_QUOTIENT / NOT_FOUNDATION_ADMITTED`

Date: `2026-08-25`

Driver-ID: `EM-DVR-R63A21 / CONTROL_PLANE`

Task:
`RS-QRF-R3-INDEPENDENT-FOUNDATION-VERIFICATION`

Taskbook source:
`41a1bbdf23831f9ad2af160df4a6bd5603f22547`

Owner branch/head:
`research/qrf-r3-independent-foundation-verification@90ec9f9bbcf88ab996842cba7bb65f6fe26b745d`

Researcher-ID:
`EM-QRF3-BEEA43`

Primary report:
`research_outputs/QRF_R3_INDEPENDENT_FOUNDATION_VERIFICATION_20260822.md`

## 1. Driver verdict

The mathematical core of

`VERIFY_R3_MINIMAL_C2_REFOUNDATION`

is accepted, but only with a mandatory typing narrowing.

The pre-orientation substrate must consist of the unlabeled elementary triangle incidence plus translation structure / unoriented boundary translation classes. A positively directed generator triple may **not** be treated as independently pre-given input, because such a triple already chooses the orientation sheet and makes the extra `C2` datum redundant.

Under the corrected typing:

- one orientation element `o in Or(T)` is necessary and sufficient to select the positive orientation sheet;
- directed positive boundary classes are outputs after choosing `o`;
- axis names remain gauge labels only;
- the min-zero atlas is a carrier normal-form decoder, not a native diagonal quotient.

## 2. Exact orientation obstruction

For an unlabeled elementary triangle `T`, cyclic orderings modulo cyclic rotation form exactly two classes.

`Aut(T) ~= S3` acts on these two classes with kernel `A3`; odd permutations exchange them. Therefore

`Or(T) ~= S3/A3 ~= C2`

as a two-sheet torsor for the quotient action.

No element of `Or(T)` is fixed by the full `S3`, so bare triangle incidence cannot canonically select one orientation sheet.

The distinguished origin and the additive translation law do not remove this obstruction: an orientation-reversing carrier automorphism can fix the origin and exchange two primitive boundary directions.

Thus a chiral choice is genuinely missing from the unlabeled pre-orientation substrate.

## 3. Sufficiency and minimality of one torsor element

Choose one orientation element

`o in Or(T)`.

It cyclically orients all three boundary edges at once. Their translation classes form a cyclically ordered three-element positive-direction set. Changing the starting vertex only cyclically relabels this set; no base vertex or base edge is needed.

Nonnegative iteration gives the three positive ray families.

A serialization as `E1,E2,E3` requires only gauge labeling. Coordinate-free addresses may instead be functions on the cyclic direction set, so no absolute first axis is ontically required.

The opposite orientation sheet reverses all three directed boundary classes, up to gauge permutation.

Therefore one orientation torsor element carries exactly the missing binary chirality and no additional metric, embedding, or base-edge datum is needed.

## 4. Mandatory typing narrowing

The taskbook phrase that the carrier “may have three directed generators” is potentially ambiguous.

The report correctly exposes the theorem-critical distinction:

- if `e1,e2,e3` are merely names for the **post-orientation** directed boundary classes generated from `o`, the C2 datum is necessary and sufficient;
- if a positively directed triple is already admitted in the **pre-orientation** frozen substrate, that triple itself selects the sheet and the additional orientation bit is redundant.

Hence the accepted primitive is not

`PRE-DIRECTED_TRIPLE + C2_BIT`.

It is

`UNLABELED_TRIANGLE_TRANSLATION_SUBSTRATE + ORIENTATION_TORSOR_ELEMENT`.

A naked Boolean `0/1` is also insufficient without a presentation-level identification with the two sheets. The intrinsic datum is the selected element `o in Or(T)`.

## 5. Min-zero decoder theorem

Let the oriented boundary translation classes be `d0,d1,d2`, with

`d0+d1+d2=0`,

and any two consecutive classes generating the rank-two carrier lattice.

For the coefficient presentation map

`Phi: Z^3 -> L`,
`Phi(a,b,c)=a d0+b d1+c d2`,

one has exactly

`ker(Phi)=Z(1,1,1)`.

For any integer representative `z`, define

`N(z)=z-min(z)(1,1,1)`.

Then `N(z)` is nonnegative, has minimum zero, represents the same carrier displacement, and is the unique such representative.

The proof is exact:

if two min-zero representatives encode the same displacement, their difference is `k(1,1,1)`; comparing minima forces `k=0`.

The decoder commutes with coordinate permutations, so no hidden first-axis convention is introduced by normalization.

## 6. Native diagonal-quotient firewall

The diagonal kernel is accepted only at the carrier-presentation layer.

The native address set is the min-zero slice

`A_E={(a,b,c) in N_0^3 : min(a,b,c)=0}`

with ordinary literal equality.

If `a in A_E` and `k>0`, then `min(a+k1)=k>0`; if `k<0`, at least one zero coordinate becomes negative. Therefore no nonzero common diagonal shift maps one valid native address to another valid native address.

Thus:

`CARRIER_KERNEL_Z(1,1,1) != NATIVE_DIAGONAL_QUOTIENT`.

The result does not authorize path-fiber collapse, native operation invariance under diagonal shifts, metric angle structure, or global absolute axis labels.

## 7. Executable pressure evidence

The executable regression correctly verifies:

- exactly two cyclic orientation classes;
- the `S3` action factors through parity, with no full-S3 fixed sheet;
- cyclic representatives choose no base edge;
- the opposite sheet reverses all directed edges;
- 1,331 bounded integer carrier representatives normalize correctly;
- bounded min-zero uniqueness;
- normalization commutes with all coordinate permutations;
- every nonzero diagonal shift exits the native min-zero slice;
- global generator reversal gives the complement normal form.

These checks are regression evidence; the no-section, kernel, and uniqueness statements are supplied by the exact proofs.

## 8. Scope / Foundation boundary

Accepted:

`QRF_R3_ORIENTATION_TORSOR_OBSTRUCTION = VERIFIED`

`QRF_R3_ONE_TORSOR_ELEMENT_SUFFICES = VERIFIED`

`QRF_R3_MIN_ZERO_DECODER = VERIFIED`

`QRF_R3_NATIVE_DIAGONAL_QUOTIENT_LEAK = false`

`QRF_R3_PRE_DIRECTED_TRIPLE_ALLOWED = false`

Not accepted:

- a detached canonical Boolean without orientation-torsor typing;
- an independently pre-given positive directed generator triple plus another orientation bit;
- metric/Euclidean orientation;
- native diagonal equivalence;
- path/provenance fiber collapse;
- automatic Foundation promotion.

## 9. Closure

`DRIVER_REVIEW = ACCEPT_WITH_TYPING_NARROWING`

`VERIFY_R3_MINIMAL_C2_REFOUNDATION = ACCEPTED_AT_CORRECTED_TYPE_SCOPE`

`FOUNDATION_ADMITTED = false`

`SUCCESSOR_AUTOMATICALLY_OPENED = false`

This closes independent verification of QRF-R3 at the corrected pre-orientation substrate scope.