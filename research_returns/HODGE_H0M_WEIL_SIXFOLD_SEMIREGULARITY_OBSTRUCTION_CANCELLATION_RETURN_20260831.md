# HODGE H0M — Weil Sixfold Open-Frontier Return

Researcher-ID: `EM-DIRECT-7B2F9A`
Task-ID: `RS-HODGE-H0M-WEIL-SIXFOLD-SEMIREGULARITY-OBSTRUCTION-CANCELLATION`
Publication: `TP2-4D8C1A7E2B609F35C614`
Claim: `chatgpt-hodgeh0m-20260831-1317-7b2f9a`
Execution branch: `research/hodge-h0m-weil-sixfold-obstruction-cancellation-em-direct-7b2f9a`
Date: `2026-08-31`

## Verdict

Primary classification:

`EXACT_HARD_BLOCK_WITH_MISSING_OBJECT_AND_UNBLOCK_CONDITION`.

Hard target:

`OPEN_WEIL_SIXFOLD_ENTERPRISE_ALGEBRAICITY_MECHANISM_CLASSIFIED_WITHOUT_TARGET_LEAKAGE = SATISFIED_AT_NEGATIVE_HARD_BLOCK_STRENGTH`.

Prerequisite A:

`OPEN_WEIL_SIXFOLD_EXACT_RATIONAL_HODGE_CARRIER_AND_FRONTIER_MODEL_ESTABLISHED = PASS`.

No algebraic codimension-three representative of a nonzero target Weil class is constructed. No non-algebraicity claim and no Hodge-conjecture claim is made. H1 is not opened.

## Literature gate

Primary sources were rechecked through 2026-08-31.

- Markman, arXiv:2502.03415: sixfold Weil classes are algebraic on the discriminant `-1` / split locus.
- Markman, arXiv:2509.23403: split-Weil/secant-sheaf source mechanism and deformation framework.
- Mostaed, arXiv:2603.20268: sixfold Hodge-Weil classes remain outside existing algebraicity mechanisms at the studied frontier points, with CM isolation, missing `K`-secant structure and uncontrolled discriminant among the explicit obstacles.
- arXiv:2607.18341 concerns abelian fourfolds, not an all-discriminant sixfold theorem.

No later primary result was found closing all discriminant classes for polarized abelian sixfolds of Weil type.

Literature classification:

`CURRENTLY_OPEN_FRONTIER_AT_DECLARED_SCOPE`.

## Exact target model

Take `K=Q(i)`, homology `U=K^6`, lattice `Lambda=Z[i]^6`, and Hermitian form

`h=diag(1,1,1,-1,-1,-3)`.

It has signature `(3,3)` and discriminant class `[-3]` in `Q^*/Nm(K^*)`.

The split sixfold class is `[-1]`; their ratio is `3`. If `3` were a norm from `Q(i)`, clearing denominators would give coprime integers

`x^2+y^2=3z^2`.

Modulo `3`, this forces `x,y` divisible by `3`, and then `z` divisible by `3`, contradiction. Thus `3` is not a norm and `[-3] != [-1]`.

Define

`E(x,y)=(1/2)Tr_{K/Q}(i h(x,y))`.

It is integral on `Z[i]^6`. Let `J0` be multiplication by `i` on the first three coordinates and by `-i` on the last three. Then `E(x,J0 x)>0` for nonzero `x`, giving a nonempty `U(3,3)/(U(3)xU(3))` period component. The frontier target is a very-general member `A_gen` of this fixed `[-3]` component, chosen before cycle search and outside additional rational Hodge/special solved loci.

Let `V=H^1(A_gen,Q)=Hom_Q(U,Q)`. Then `dim_K V=6`, and

`W_K(A_gen)=wedge_K^6 V`

has `dim_Q W_K=2`. After complexification,

`W_K,C = wedge^6 V_sigma direct-sum wedge^6 V_sigma_bar`.

Weil signature `(3,3)` gives three `(1,0)` and three `(0,1)` directions in each embedding block, so both determinant lines are pure of type `(3,3)`.

For the very-general target `NS_Q=Q[E]`; hence divisor-generated degree-six classes form `Q[E^3]`, lying in the `(3,3)` exterior-count block `wedge^3 V_sigma tensor wedge^3 V_sigma_bar`, while `W_K` lies in the `(6,0)` and `(0,6)` embedding-count blocks. Therefore

`W_K(A_gen) intersect Q[E^3] = 0`.

The exceptional Weil target is not a divisor product under another name.

## Split-source defect and transport no-go

A split six-dimensional `K`-Hermitian space with a three-dimensional totally isotropic `K`-subspace is a sum of three hyperbolic planes and has determinant class `[-1]`. Since the target has class `[-3]`, the maximal split/isotropic source datum required by the known split `K`-secant presentation is absent.

For any six-dimensional `K`-Hermitian rational similitude

`h' = c g^* h g`, with `c in Q^*`,

one has

`det(h') = c^6 Nm(det g) det(h)`.

Both extra factors are norms in `Q^*/Nm(K^*)`, since `c^6=Nm(c^3)`. Thus the discriminant class is invariant.

Consequently the standard `K`-compatible route cannot move the split source object from `[-1]` to `[-3]` by:

- deformation inside the polarized Weil-type component structure;
- `K`-linear polarized isogeny/similitude;
- unitary Hecke transport;
- duality from the self-inverse split class;
- a Fourier-Mukai/Orlov transport only insofar as it is required to induce the relevant `K`-compatible Hermitian-similitude identification of the target Weil carrier.

This does not rule out every algebraic correspondence. A genuinely new codimension-three correspondence not induced by those `K`-compatible transports remains open.

## Exact obstruction-cancellation hard block

Standard Ext/deformation/semiregularity theory is available source mathematics. It is not the missing innovation.

The missing object is exactly:

`E on the target [-3] component with exceptional_projection(ch_3(E)) != 0 in W_K(A_gen)`,

or an algebraic family/correspondence producing such a class.

Until such an `E` exists, `Ext^1(E,E)`, `Ext^2(E,E)`, semiregularity channels and any proposed finite obstruction-cancellation process are not instantiated target-side data. Standard semiregularity cannot manufacture the initial object or cross the discriminant wall.

Therefore:

`STANDARD_SEMIREGULARITY = SOURCE_INHERITED`;

`ENTERPRISE_OBSTRUCTION_CANCELLATION = NOT_INSTANTIATED`.

No R2/R3 attribution is claimed.

## Class-first status

- divisor products: rejected by the direct-summand separation above;
- known split secant-sheaf characteristic classes: rejected as frontier generators;
- new target-side sheaf/complex: open but not constructed;
- genuinely new algebraic correspondence: open but not constructed.

Exact unresolved frontier:

`CONSTRUCT_A_TARGET_SIDE_ALGEBRAIC_OR_DERIVED_SOURCE_OBJECT_ON_THE_NON_SPLIT_COMPONENT_WITH_NONZERO_EXCEPTIONAL_WEIL_CH3_PROJECTION_OR_A_GENUINELY_NEW_CORRESPONDENCE_PRODUCING_SUCH_A_CLASS`.

Absolute-Hodge, Mumford-Tate and Hodge-type status are not treated as algebraicity.

## Checker and frozen evidence

Checker:

`research_checks/HODGE_H0M_WEIL_SIXFOLD_SEMIREGULARITY_OBSTRUCTION_CANCELLATION_CHECK_20260831.py`

Git blob SHA-1: `af17c502b23abc2ad35fadd2136993bf9282d6e4`
SHA-256: `a750d5aaef6257d5352b6569587875449838496e6df56c9246df4451d37f5313`

Frozen run:

`HODGE_H0M_CHECKS=13`
`HODGE_H0M_FAILURES=0`
`HODGE_H0M_WEIL_SIXFOLD_SEMIREGULARITY_OBSTRUCTION_CANCELLATION_CHECK: PASS`

Artifact digests:

- literature ledger: blob `322485bcb41788eb4ba3c98a225b866e8ca82196`, sha256 `a452a2f4f4ccf81e684fc558f49c9b8b4d09782b5309ff7ca9b79f899f6b81ba`
- model spec: blob `604ad638570d7fbbb90cade22b5d514af1d4673b`, sha256 `19e732fd2ba1c5419a1d255c71e9abfc189cf8e70ddadbd43b3856b772b0f1ad`
- discriminant defect: blob `ce7a3679850101e11b8dc431a52431ecf21d5e9a`, sha256 `0e8ef0b31767b86b32c9ef8556a20fa0c3c5c742bb30cc954b2d53b528f85629`
- transport registry: blob `6726445ac86c08a99d28cd702b3f5973fa17bc38`, sha256 `e1c14b4ddffae3bf4dd87ad6385f8d361465c4e9b7a4ef68bd0ce0e64cbf4246`
- obstruction registry: blob `caf0a6aa9be3cc2b4c61e1cefbbf10c490d64726`, sha256 `2dd7fc9a1e5c040dc8dcb85dcee804c488b20da6e06e4d7dd60f6e0e6b8f51ae`
- class-first registry: blob `414df0b8c11b9e64f468b40302d35cf29ccdca2f`, sha256 `c95121fd81020bf5f8609cb36a5814fc411ce05d4ecbb591c72ecc06596fd536`

## Recommendation

Driver-review this result as a negative hard-block classification. Do not reopen the split transport route without new mathematics that changes the discriminant compatibility. If the Hodge-special line continues, the next task should be narrower: direct target-side source-object existence/classification on the non-split component, or a separately falsifiable new algebraic-correspondence route. Do not promote to H1 from this result.

Freeze boundary reached.
