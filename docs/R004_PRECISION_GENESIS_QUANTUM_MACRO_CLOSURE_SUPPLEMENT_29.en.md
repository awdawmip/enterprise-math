# R004 precision genesis — Supplement 29: canonical multi-target dependency/synergy decomposition

Status: `PROVED_WIP + EXECUTABLE_REFERENCE + MULTI-TARGET MODULE DECOMPOSITION`  
Parent: `R004_PRECISION_GENESIS_QUANTUM_MACRO_CLOSURE_SUPPLEMENT_28.en.md`  
Owner branch: `research/r004-precision-genesis-closure-20260810`

Supplement 28 showed that ordinary pairwise inclusion-exclusion fails because observation may know cross-target combinations. This supplement gives a parenthesization-independent decomposition for any finite target family.

## 1. Target presentation relation module

Let `W_1,...,W_m` be target row modules. Define the sum map

`pi_W : direct_sum_i W_i -> sum_i W_i`,

`pi_W((w_i))=sum_i w_i`.

Its kernel

`R_W=ker pi_W`

is the complete target-dependency module. It contains all linear relations among target components, not only pairwise intersections.

The exact sequence

`0 -> R_W -> direct_sum_i W_i -> sum_i W_i -> 0`

gives

`mu(R_W)=sum_i mu(W_i)-mu(sum_i W_i)`.

## 2. Observed relation module

Let

`U_i=U cap W_i`.

The observed component sum has presentation

`pi_U : direct_sum_i U_i -> sum_i U_i`.

Define

`R_U=ker pi_U`.

Since every U_i is contained in W_i, the direct-sum inclusion sends any observed relation to a target relation, so

`R_U subseteq R_W`.

The quotient

`R_W/R_U`

is therefore the target-dependency structure that individual defect accounting would double-count but that is not already accounted for inside the individually observed pieces.

## 3. Multi-target observation synergy

Define

`S_U(W_1,...,W_m)`
` = (U cap sum_i W_i) / (sum_i (U cap W_i))`.

This measures cross-target combinations known by U that cannot be assembled from target components individually known by U.

It is the multi-target generalization of Supplement 28's distributivity-defect quotient.

## 4. Canonical joint-defect formula

For each target let

`delta_i=delta(U,W_i)=mu(W_i)-mu(U cap W_i)`.

Then

`delta(U,sum_i W_i)`
` = sum_i delta_i`
`   - mu(R_W/R_U)`
`   - mu(S_U(W_1,...,W_m))`.

Proof. Expand the mass of the target sum by the exact sequence defining R_W and the mass of `sum_i U_i` by R_U, then use

`mu(U cap sum W_i)=mu(sum U_i)+mu(S_U)`.

No distributive-lattice or Möbius assumption is used.

## 5. Two canonical rebates

The sum of individual defects can overcount joint defect for exactly two module-valued reasons.

### Dependency rebate

`R_W/R_U` records dependencies among target modules not already present among their separately observed parts.

### Synergy rebate

`S_U` records combinations seen jointly by the observation but invisible in every individual observed target part.

Therefore

`delta(U,sum_i W_i) <= sum_i delta(U,W_i)`.

The difference is not an opaque scalar: it is the exponent mass of two explicit finite p-group objects.

## 6. Examples

### Pure target dependency

Over `F_2^2`, take U=0 and targets

`W1=<e1>`, `W2=<e2>`, `W3=<e1+e2>`.

Each individual defect has mass 1, but the three targets span only two dimensions. Here

`mu(R_W/R_U)=1`, `mu(S_U)=0`,

so joint defect is `3-1=2`.

### Pure observation synergy

Over `F_2^3`, take

`U=<e1+e2>`,

and independent targets

`W1=<e1>`, `W2=<e2>`, `W3=<e3>`.

There is no target dependency, but `mu(S_U)=1`; three individual defects sum to 3 while joint defect is 2.

These two mechanisms are structurally different even when they produce the same scalar rebate.

## 7. Why this replaces Möbius bookkeeping

For three or more submodules, ordinary inclusion-exclusion over intersections is not canonical in a non-distributive subgroup lattice. The presentation-kernel module R_W captures all target dependencies at once, while S_U captures all observation-side join synergy at once.

The formula is independent of target ordering or parenthesization.

## 8. Validation

Independent exact checks covered **7,200** random systems over small 2- and 3-power ambient modules with two, three and four target modules. In every case:

- `R_U` mass did not exceed `R_W` mass;
- the dependency and synergy rebates were nonnegative;
- the canonical decomposition exactly reproduced the direct joint target defect.

In 3,362 cases the total rebate was strictly positive.

These are finite exact WIP checks, not fresh full-repository CI or canonical-main claims.

## 9. Architecture consequence

Multi-target precision accounting should carry **dependency presentations and relative embeddings**, not only individual target profiles or pairwise overlaps. This is another instance of the Representation Compiler rule that scalar summaries are acceptable outputs but not complete compositional state.

The next frontier is to move this decomposition beyond linear row modules. At A4 MAY level, multi-target support unions have a set-theoretic union law, but richer witness identities can contain cross-target correlations analogous to R_W. The compiler needs a typed notion of dependency presentation appropriate to the declared witness algebra, not a forced linearization.
