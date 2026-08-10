# R004 precision genesis — Supplement 09: relation-rank compiler and representation exponent codimension

Status: `PROVED_WIP + EXECUTABLE_CHECKED + A3_CONSUMER + FOUNDATION_FEEDBACK_CANDIDATE`  
Parent: `R004_PRECISION_GENESIS_QUANTUM_MACRO_CLOSURE_SUPPLEMENT_08.en.md`  
Owner branch: `research/r004-precision-genesis-closure-20260810`

Supplement 08 located the true product-compiler boundary: joint action correlation is harmless under componentwise dynamics and full product observation, while cross-axis observable/dynamical coupling can require a joint state.

This supplement solves a large structured subclass of such coupling. If the coupled future factors through an integer linear relation state, the relation coordinate can be proved sufficient and compiled directly.

## 1. Linear relation state

Fix prime `p`, cap `K`, ambient dimension `d`, and state

`x in (Z/p^K Z)^d`.

Let `A` be an integer `r x d` matrix and define the relation vector

`R_A(x)=A x mod p^K`.

The future actions are componentwise translations `x -> x+a`.

Linearity gives

`R_A(x+a)=R_A(x)+R_A(a)`.

Assume the declared observable depends only on the relation vector, specifically the full vector of capped relation valuations

`O_A(x)=(q_K(R_A(x)_1),...,q_K(R_A(x)_r))`.

Then every future observable after a joint action depends on the original state only through `R_A(x)`.

Hence the literal product-state future signature factors as

`Sigma_X = Sigma_R o R_A`.

This is a direct P023 factorization certificate: the relation coordinate is legal here because sufficiency is proved, not assumed.

## 2. Surjective relation rank

Suppose `A mod p` has full row rank `r`.

Then some `r x r` minor has determinant not divisible by `p`. That determinant is a unit modulo `p^K`, so the corresponding square submatrix is invertible over `Z/p^K Z`. Consequently

`R_A : (Z/p^K Z)^d -> (Z/p^K Z)^r`

is surjective.

This gives an exact finite meaning to **relation rank** in the present compiler: every relation-state tuple is genuinely reachable from some ambient state.

Matrix rank and invertible-unit-minor algebra are prior mathematics. R004 uses the condition only to certify exact class counts.

## 3. R004-COMP-T06 — relation-language reduction

Let `W` be any nonempty finite joint translation language on the ambient state. Map it through the relation matrix:

`R_A(W)={R_A(a): a in W}`.

The relation future signature is the full vector of capped valuations under these induced relation translations.

By Supplement 08's product factorization, correlations among the `r` induced relation actions may be discarded after projecting to the individual relation axes, because the observable exposes the complete relation-observation vector.

Therefore the compiler is:

1. compute `z=R_A(x)`;
2. compute the induced relation action set `R_A(W)`;
3. project that set onto each relation coordinate;
4. compile every relation coordinate with the one-axis p-adic trie compiler;
5. return the tuple of relation-axis trie tokens.

If `A mod p` has full row rank, this tuple is the coarsest future-safe state on the original ambient product.

The class count is exactly the product of the relation-axis trie class counts.

## 4. Rank-one example: difference is enough

For two axes choose

`A=[1,-1]`.

Then

`R_A(x_1,x_2)=x_1-x_2 mod p^K`.

A joint translation `(a_1,a_2)` induces only

`a_1-a_2`.

If the future observable sees only the capped valuation of that difference, every pair of ambient states with the same compiled difference-relation token is future-equivalent, even if their individual coordinates differ completely.

This gives a precise sufficient case in which a relation coordinate genuinely replaces the product state.

It is structurally adjacent to A3 relation-state language, but R004 does not claim the generic relation concept as its own.

## 5. Full-translation state-count theorem

Take the complete ambient translation language

`W=(Z/p^K Z)^d`.

If `A` has full row rank `r`, surjectivity implies the induced relation translations fill all of

`(Z/p^K Z)^r`.

Every relation coordinate therefore reaches the universal-translation endpoint of Supplement 06/07 and must retain its exact residue modulo `p^K`.

The minimum future-safe class count is therefore

`C_relation = p^(K r)`.

The exact ambient state space contains

`C_ambient = p^(K d)`

states.

No normalized compression ratio is needed.

## 6. Representation exponent codimension

Because both class counts are exact powers of the same prime, define the integer

`Gamma = K(d-r)`.

Then

`p^(K d) = p^Gamma * p^(K r)`.

`Gamma` counts the exact number of ambient p-adic digit freedoms proved irrelevant to the declared future language.

R004 calls this the **representation exponent codimension** for the present relation-compiler family.

It is not a logarithmic approximation. The exponent is already part of the exact prime-power state counts.

Examples:

- `d=2,r=1,K=3`: `64` ambient states -> `8` safe relation classes, `Gamma=3`;
- `d=3,r=2,K=4`: `p^12` ambient states -> `p^8` relation classes, `Gamma=4`;
- `r=d`: `Gamma=0`, so no exponent-level reduction is certified by relation rank alone.

## 7. What rank does and does not mean

This theorem does **not** identify relation rank with physical spatial dimension.

It says something narrower and more operational:

> under an explicitly declared relation-factored future language, `r` independent relation coordinates are sufficient, and the remaining `d-r` ambient coordinate directions are future-invisible at the exact state level.

That is a representation theorem, not an ontology theorem.

It also does not imply every coupled observable admits a low-rank linear relation factorization. Supplement 08 already provides a coupled Boolean example whose safe partition changes with joint action correlation; a structured relation normal form must be proved case by case or by a genuine upstream mother theorem.

## 8. Validation and oracle correction

Executable assets:

- `precision_relation_language_compiler.py` — single linear relation coordinate;
- `precision_relation_rank_compiler.py` — full-row-rank relation matrices;
- matching tests.

During independent cross-checking, an initial validation oracle was found to deduplicate joint actions after mapping them to identical induced relation actions and then compare the compiler only with that deduplicated signature. Deduplication is mathematically safe for kernel equality, but that oracle was not independent enough.

The implementation was corrected: compiler construction may still deduplicate induced actions, while regression comparison now keeps the **literal original joint-action signature**, including duplicate induced coordinates.

After the correction, independent enumeration checked **1,313** bounded partition cases across multiple primes, caps, ambient dimensions, relation ranks, full-row-rank matrices and action subsets with no mismatch.

This correction is part of the evidence trail; the earlier weaker oracle is not counted as independent validation.

## 9. Architecture consequence

R004's representation compiler now has three exact structured regimes:

1. **one prime axis:** arbitrary translation language -> p-adic trie state;
2. **independent/full-vector product:** arbitrary correlated joint translations -> product of marginal trie states;
3. **linear coupled future:** relation matrix -> induced relation language -> relation-rank trie state.

The third regime gives an explicit entry point for A3 consumption:

`ambient state -> proved sufficient relation state -> operation-conditioned minimal repair`.

The next hard question is no longer whether relation coordinates can ever be sufficient. They can.

The hard question is:

> **For coupled futures that do not arrive with a declared relation matrix, can Enterprise Math discover or certify the minimum sufficient relation/witness state automatically?**

That question belongs at the P023/A3/A4/Foundation boundary rather than being silently solved inside R004.
