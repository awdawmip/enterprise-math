# FQ010 — Cardinality Readout Classification

Researcher-ID: `EM-FQ010-CA2555`

## 1. Separate the relation from its scalar readout

The relation

`R_type={(x,y):tau(x)=tau(y)}`

is already fixed at relation strength. FQ010 now classifies only the further step

`R_type -> Q_K:=|R_type|`.

Finite cardinality is an exact, isomorphism-invariant readout of the finite relation carrier. That makes `Q_K` a mathematically canonical **available** N2 readout once the choice to count relation-pairs has been made. It does not make cardinality the unique scalar forced by N0.

## 2. Exact cardinality formula

Write the occupied type fibers as

`U_c=tau^{-1}(c)`, with `|U_c|=n_c`.

Then

`R_type = disjoint_union_c (U_c x U_c)`.

The union is disjoint because one ordered pair cannot simultaneously have two distinct common component types. Therefore

`|R_type| = sum_c |U_c x U_c| = sum_c n_c^2`.

Hence

`Q_K=sum_c n_c^2`.

No metric, length, norm or current scalar formula is used in this derivation.

## 3. Is cardinality uniquely selected by minimal valuation axioms?

No.

Consider finite equivalence relations as relational structures. Every such relation is a disjoint union of complete equivalence blocks `E_n` of sizes `n`.

Let `V` be a valuation satisfying:

1. isomorphism invariance;
2. additivity under disjoint union of equivalence-relation structures;
3. unit normalization `V(E_1)=1`.

Then `V` is determined by an arbitrary function

`g:N_{>0}->A`, with `g(1)=1`,

via

`V(disjoint_union_i E_{n_i})=sum_i g(n_i)`.

The conditions above do not determine `g(n)` for `n>1`.

Distinct surviving examples include:

- `g(n)=n^2`, giving relation-pair cardinality `|R_type|`;
- `g(n)=n`, giving total token count;
- `g(n)=1`, giving occupied component count.

All are isomorphism-invariant, disjoint-union additive and unit-normalized.

Therefore:

`ISOMORPHISM_INVARIANCE + STRUCTURAL_DISJOINT_UNION_ADDITIVITY + UNIT_NORMALIZATION`

**does not uniquely select relation cardinality.**

## 4. What does uniquely select ordinary cardinality?

Two stronger packages can do so, but both add information beyond bare relation canonicity.

### A. Pair-atom counting convention

Treat the underlying finite set of ordered relation-pairs as the valuation carrier and impose:

- additivity over disjoint unions of finite pair-sets;
- every singleton ordered pair has value `1`.

Then ordinary finite cardinality is uniquely obtained.

This is mathematically standard, but it is precisely a choice to resolve the relation into ordered-pair observation atoms. It is a readout convention, not a theorem that every semantic scale must use those atoms.

### B. Block valuation plus quadratic axis calibration

For an isomorphism-invariant block-additive valuation, impose

`V(E_n)=n^2`

for every one-block relation. Then necessarily

`V(R_type)=sum_c n_c^2=|R_type|`.

Equivalently, quadratic replication of a one-block state plus unit normalization selects the same `g(n)=n^2`.

These conditions are extra scalar/semantic conditions. In the FQ008 interface, axis-square calibration plus transverse independence supplies an equivalent scalar characterization on the sector domain.

## 5. Competing scalars of the same relation

The same canonical relation supports multiple exact, presentation-independent scalar readouts, for example:

- `|U| = sum_c n_c`, recoverable from the diagonal;
- number of equivalence classes / occupied component count;
- largest block size;
- number of off-diagonal same-type ordered pairs `|R_type|-|U|`;
- same-type unordered-pair count `( |R_type|-|U| )/2`;
- `sum_c h(n_c)` for other parameter-free integer functions `h`.

Thus the R065 scalar-underdetermination boundary survives intact.

## 6. Semantic classification

The strongest justified typing is:

- `R_type`: `N0_DEFINABLE_DERIVED`;
- `|R_type|` as ordinary finite cardinality: exact `N2_READOUT_COLLAPSE`;
- selection of relation cardinality as the **preferred** line-scale readout: not N0-forced;
- identification `|R_type| := squared native line scale`: separate semantic declaration/calibration required.

Therefore uniqueness of cardinality as a finite-set valuation must not be confused with uniqueness of cardinality as the semantic valuation of the relation object.

## 7. Result

`CARDINALITY_READOUT_TYPED_SEPARATELY_FROM_RELATION = PASS`.

`BARE_RELATION_STRUCTURE_UNIQUELY_SELECTS_CARDINALITY = FALSE`.

`Q_K_IS_EXACT_AND_CANONICAL_ONCE_PAIR_CARDINALITY_READOUT_IS_SELECTED = TRUE`.

This is the precise boundary needed for the final FQ010 admission decision.
