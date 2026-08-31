# R063 Stage 2 — Native Path Multiplicative Lift / No-Go Classification

Status: `CHOICE-FREE FROZEN-SEMANTIC LIFT NO-GO / RELATION-VALUED SURVIVOR`

## 1. What is being classified

Fix frozen R061 native path fibers

`Path_E(a,b)=Sh_{a,b}(X_i,X_j)`

with cardinality

`|Path_E(a,b)|=binom(a+b,a)`.

After an ordered sector orientation is explicitly fixed, Stage 2 has the exact target trace product

`r star_i s`.

The question is whether the frozen path semantics itself induces a canonical single-valued operation

`Path_E(r) x Path_E(s) -> Path_E(r star_i s)`.

The conclusion is **no without additional path-process semantics**. This does not say that arbitrary set-theoretic functions are impossible.

## 2. Mandatory multiplicity theorem

Take

`A=B=2`, `r=s=(1,1)`.

Then

`r star_i s=(0,2)`.

Frozen native path multiplicities are

`|Path_E(1,1)|=binom(2,1)=2`,

`|Path_E(0,2)|=binom(2,0)=1`.

Therefore

`|Path_E(r star_i s)| = 1 != 2*2 = |Path_E(r)| |Path_E(s)|`.

So

`NATIVE_PATH_MULTIPLICITY_IS_NOT_MULTIPLICATIVE_UNDER_ROOT_PRODUCT`.

This is the smallest exact counterexample in the exhaustive Stage 2 order.

The same witness also separates operations:

- fixed-signed-target Gaussian provenance preimages: `4`;
- source native path pairs: `4`;
- multiplicative target native paths: `1`;
- frozen additive-concatenation target `T_{2,2}` native paths: `binom(4,2)=6`.

The equality `4=4` between the first two layers is accidental and is not an identification of carriers.

## 3. Non-coincidence witness

For

`A=B=5`, `r=s=(2,1)`,

`r star_i s=(3,4)`.

Then

- fixed-signed-target provenance preimage count = `4`;
- source native path-pair count = `3*3=9`;
- target native path multiplicity = `binom(7,3)=35`.

Thus `4`, `9`, and `35` are pairwise distinct. This removes the possibility that the `2 x 2` equality of two upstream counts reflects a hidden multiplicity law.

## 4. Stronger no-go inside the frozen path-operation closure

The frozen R061 operations available on path representatives are:

- typed word concatenation;
- interleaving/shuffle of positive component letters;
- adjacent component-preserving commutations;
- trace projection;
- typed incidence/translation already frozen by R061.

Every construction generated from concatenation, interleaving and adjacent commutation preserves the **total positive component letter counts**. Starting from traces `(a,b)` and `(c,d)`, such a construction remains in trace

`(a+c,b+d)`.

But Gaussian/root multiplication requires, before unit normalization,

`(ac-bd, ad+bc)`,

and after the Stage 2 orientation normalization generally a different nonnegative pair.

At `r=s=(1,1)`, all direct concatenations and all interleavings have trace `(2,2)`, while the multiplicative target trace is `(0,2)`.

Therefore:

> No path multiplication can be generated from the frozen R061 path operations alone and project to the Stage 2 multiplicative trace product in general.

To change `(a+c,b+d)` into the multiplicative target requires at least one new operation such as letter substitution, signed/negative contribution, cancellation, unit rotation, target-word selection, rank/unrank selection, or another transducer. By the native-semantics gate, that is additional `N1` process/choice semantics, not a consequence already present in the frozen path fiber.

This is the precise sense of the Stage 2 choice-free path-lift no-go.

## 5. Required candidate audit

### Direct word concatenation

Rejected as multiplicative lift. It implements frozen additive trace composition, not root multiplication. Minimal discriminator: `2 x 2` gives `(2,2)` instead of `(0,2)`.

### Shuffle / interleaving

Rejected for the same reason. Interleaving changes word order but not total component counts, so it cannot repair the trace mismatch.

### Cartesian/tensor source paths followed by deterministic target readout

A set-theoretic map can always be manufactured once a target path selector is added. For `5 x 5`, there are `9` source path pairs and `35` target paths, so trace compatibility alone permits many functions. The frozen trace/path data do not select one of them. Lexicographic-first, rank reduction, block-word choice, or any similar rule is extra selection semantics.

### Gaussian substitution / transducer

The raw component formula contains the signed term `ac-bd`. Implementing it at word level requires negative letters/cancellation or an equivalent unit-rotation/transducer state. Those operations are absent from the frozen positive-axis path language. Such a lift can be researched only as an explicitly enriched carrier.

### Provenance-labelled path product

Permitted as a richer future construction, but forgetting provenance/process state still needs a target-path relation or selector. It is not the same object as the native R061 path fiber.

### Relation-valued lift

This survives exactly after an oriented target trace is fixed. Define

`M_rel(p,q)=Path_E(r star_i s)`

for every `p in Path_E(r)`, `q in Path_E(s)`.

Equivalently, each source pair is related to the entire target native path fiber. This is typed, choice-free at the path-representative level, and compatible with target trace projection. It deliberately forgets source path order and is **not** a single-valued multiplication.

Because the target trace product is associative, the induced target-support relation is associative at the trace/support level. It does not create a canonical representative.

## 6. Orientation-free obstruction is even earlier

Before an ordered sector orientation is fixed, a single-valued path lift would have to project to a single-valued ordered trace product. Section `R063_STAGE2_TRACE_PRODUCT_CLASSIFICATION.md` proves that no component-swap-equivariant ordered trace product exists at `A=B=2`. Therefore an orientation-free canonical path lift is impossible already at trace projection.

## 7. Exact final statement

`NATIVE_PATH_MULTIPLICITY_IS_NOT_MULTIPLICATIVE_UNDER_ROOT_PRODUCT = PROVED`.

`DIRECT_CONCATENATION_MULTIPLICATIVE_LIFT = FALSE`.

`SHUFFLE_INTERLEAVING_MULTIPLICATIVE_LIFT = FALSE`.

`FROZEN_R061_OPERATION_CLOSURE_CANONICAL_MULTIPLICATIVE_PATH_LIFT = NO_GO`.

`SINGLE_VALUED_LIFT_WITH_ADDED_SELECTOR_OR_TRANSDUCER = POSSIBLE_IN_PRINCIPLE_BUT_ADDITIONAL_SEMANTICS`.

`CHOICE_FREE_RELATION_VALUED_TARGET_FIBRE_LIFT = EXACT_AFTER_ORIENTATION`.

No Stage 3 construction is opened here.
