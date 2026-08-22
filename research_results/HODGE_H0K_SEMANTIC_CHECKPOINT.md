# HODGE H0K Semantic Checkpoint

Status: `FROZEN / RESEARCH COMPLETE / H1 BLOCKED`
Task: `RS-HODGE-H0K-FERMAT-CUBIC-RATIONAL-HODGE-CARRIER-INTERACTION-TRANSFER`
Taskbook source: `35af8150cc4e7d6a50c26b82a2d0c17a4de784fe`
Researcher-ID: `EM-HODGE-H0K-5A71D2`
Owner branch: `research/hodge-h0k-fermat-rational-hodge-interaction`

## Final disposition

`H0K_CLASS_FIRST_LIFT_SOURCE_COMPLETE_NO_ENTERPRISE_INCREMENT`

Hard prerequisite A:

`FERMAT_CUBIC_EXACT_RATIONAL_HODGE_INPUT_CARRIER_ESTABLISHED_WITHOUT_CYCLE_GENERATOR = PASS`

Primary hard target B:

`SOURCE_DERIVED_INTERACTION_PROCESS_ADDS_ROBUST_ATTRIBUTED_LEVERAGE_ON_EXACT_RATIONAL_HODGE_INPUT = NOT_ESTABLISHED`

Stronger target C:

`FERMAT_CUBIC_CLASS_FIRST_ENTERPRISE_R3_PRESEED = NOT_ESTABLISHED`

`H1_ADMISSIBLE=false`.

## A. Exact rational Hodge carrier was frozen before cycle search

For the Fermat cubic fourfold

`X_F : x0^3+...+x5^3=0`,

the Jacobian ring is

`C[x0,...,x5]/(x0^2,...,x5^2)`.

Griffiths degree accounting gives primitive pieces from degrees `0,3,6`, hence dimensions `1,20,1`.

A primitive diagonal character has all six entries in `{1,2}`. If `k` entries equal `2`, the character-sum condition forces `k in {0,3,6}`, and `|alpha|=2+k/3`. Thus `(2,2)` is exactly `k=3`, giving `C(6,3)=20` one-dimensional complex eigenlines.

Galois conjugation `zeta_3 -> zeta_3^2` sends a 3-subset `S` to its complement. The 20 middle eigenlines therefore form ten 2-element orbits.

For each orbit, the rational group-algebra idempotent

`e_[alpha] = e_alpha + e_2alpha`

has coefficient `2/243` when `chi_alpha(g)=1` and `-1/243` otherwise, so `e_[alpha] in Q[G]`. Its image in `H^4_prim(X_F,Q)` is a genuine two-dimensional rational Hodge block. Adding the ambient `Q*h^2` line yields an exact 21-dimensional rational Hodge carrier.

No plane, Chow basis, known spanning theorem, or algebraic-cycle representative was used in this carrier construction.

## B. Full plane grammar was generated only after the carrier gate

All 15 perfect matchings of the six coordinates were generated. For each matching, all `3^3=27` phase triples were generated using

`x_i = -zeta_3^r x_j`.

Direct substitution into the Fermat equation verifies every plane. Pairing and phase data are recoverable from the restricted coordinate proportionality classes, so the 405 descriptors are exact and distinct.

## C. Exact full plane-cycle class map

For two generated planes:

- self-intersection is `3`, from `c2(N_{P/X})=3`;
- meeting in a line gives `-1` by excess intersection;
- meeting transversely in one point gives `1`;
- disjoint gives `0`.

For one fixed pairing orbit, the 27x27 intersection kernel depends only on phase Hamming distance and has Fourier eigenvalue `9` exactly for the trivial mode and the eight all-nonzero character modes, and `0` for modes with one or two zero coordinates.

For each rational Hodge block choose the lexicographically first compatible pairing and define

`U = F_t + F_-t`

and

`V = (F_t-F_-t)/(zeta_3-zeta_3^2)`.

These are integral plane combinations with coefficients:

- `U`: `2` when `t.r=0`, otherwise `-1`;
- `V`: `0,-1,+1` when `t.r=0,1,2`.

Together with `h^2=(1/9) sum_r [L_r]`, they form an orthogonal 21-dimensional rational cycle-class basis with Gram diagonal

`3, 486,162, ..., 486,162`.

The formula-complete 405x21 class matrix is regenerated deterministically, has rank `21`, and all `164025` pairwise plane intersection entries are exactly reconstructed from it.

Therefore:

`FERMAT_PLANE_CYCLE_CLASS_MATRIX = EXACT`.

## D. Exact arbitrary class-first lift

For an arbitrary input `alpha in V_Hdg,Q`, decompose it by the rational projectors. For each two-dimensional block:

`a=(alpha.U)/486`,
`b=(alpha.V)/162`,

and output

`Z_B(alpha)=a U_cycle + b V_cycle`.

The ambient coefficient is lifted by the 27-plane orbit average. Summing all blocks gives a rational plane cycle satisfying

`cl_Q(Z(alpha))=alpha`

for every input in the frozen 21-dimensional carrier, including negative and denominator-bearing combinations.

The cycle basis is selected globally and lexicographically after the complete grammar freeze, never after target inspection.

## E. Interaction-process transfer

The Hodge-side local interaction is source-derived:

`m(t,r)=zeta_3^(-tr)`.

In the rational basis `1,zeta_3`, multiplication is

`(a,b)*(c,d)=(ac-bd, ad+bc-bd)`,

which is visibly not the R063 Gaussian law. No R063 `C4` table or root target semantics is imported.

Across three coordinate pairs, the local process reconstructs the plane-to-character Fourier coefficient multiplicatively. It compresses 216 global per-pairing cyclotomic coefficients to a six-entry local table plus tensor composition, so it has real abstract `COMPOSITIONAL_FACTORING / DEPENDENCY_REDUCTION` against `B_raw^Fermat`.

However, `B_std^Fermat` already owns exactly this tensor-product character DFT, cyclotomic arithmetic, rational group-algebra projector, Galois descent, block decomposition, and exact linear inversion. K1/K2/K3/K4 are therefore all `SOURCE_INHERITED_LEVERAGE` under the H0D0 attribution addendum.

## F. Route boundary

The recurring Hodge-input ambiguity is closed on this benchmark: the rational Hodge carrier is exact and cycle-independent.

The algebraicity/lifting problem is also source-complete on the declared Fermat cubic carrier: the full rational Hodge carrier admits an exact plane class-first lift.

What H0K does **not** establish is an Enterprise-specific proof differential. The transferred finite interaction process is an exact repackaging of ordinary character/DFT/Galois/intersection linear algebra available to the fair classical source.

Do not rerun H0K with more phases, a larger plane subset, or a different target basis. A successor must change the Enterprise mechanism itself.

## Checker

`168173/168173 PASS`

Semantic core SHA-256: `32d795d72ad07391a7cd486b3f7f83605dba0462d8a4c5557a805afc85a9c218`

Checker script SHA-256: `c4385f780e311de2bcab7f837e0315d5ddb12966032eb82908a9be6a64784a88`

Checker output SHA-256: `be3a279723ec850899b744f08e735d838e1c345242c40347f92218cc4ad0911c`

`CI_NOT_REQUIRED_FOR_RESEARCH`

No Hodge proof is claimed. No H1 stage is opened.
