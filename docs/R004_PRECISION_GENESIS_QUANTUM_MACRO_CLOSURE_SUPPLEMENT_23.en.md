# R004 precision genesis — Supplement 23: typed defect certificate composition

Status: `PROVED_WIP + EXECUTABLE_REFERENCE + P023/A4_COMPOSITION_BRIDGE`  
Parent: `R004_PRECISION_GENESIS_QUANTUM_MACRO_CLOSURE_SUPPLEMENT_22.en.md`  
Owner branch: `research/r004-precision-genesis-closure-20260810`

Supplements 20–22 established several exact defect representations: p-adic modules for linear targets, A3 exterior/guard specializations, and A4 support correspondences for arbitrary nonlinear MAY semantics. This supplement asks how such certificates compose through successive representation changes without reopening fine state.

The answer is deliberately typed. There is no universal scalar defect addition law. Each certificate class has its own strong composition law and a sound erasure path to weaker semantics. A4 MAY correspondence is the total conservative fallback.

## 1. Universal MAY support composition

Let

`X --q1--> Q1 --r--> Q2`

and let `t:X->T` be any target. Suppose the first stage has retained only the exact support relation

`R1 = R_(q1,t) subseteq Q1 x T`.

Let `r^op subseteq Q2 x Q1` be the reverse graph of r. Then

`R_(r o q1,t) = r^op ; R1`.

Proof. `(b,y)` lies in the right-hand side iff there is `a in Q1` with `r(a)=b` and a fine x with `q1(x)=a`, `t(x)=y`; this is exactly the definition of target y appearing in the fiber of the composite collapse.

Thus a MAY support certificate can always be transported through further source coarsening without reopening X.

For a future target relation `S subseteq T x U`, post-composition is equally exact:

`R_(q1,t) ; S`.

Hence arbitrary source coarsening and future MAY evolution live in ordinary relation composition.

## 2. Strong certificate families and erasures

The current compiler has several stronger certificate types.

### Functional certificate

A descended function `f:Q->T` composes as a function when the next typed step is functional. Its MAY erasure is its graph.

Further source coarsening need not preserve functionality. When singleton fibers fail, the certificate safely demotes to its support relation.

### Homogeneous group/module defect

A translation-homogeneous target carries a variation subgroup/module plus the maps that explain its action on fibers. Nested homogeneous collapses admit group/module extension laws. Its MAY erasure is the corresponding coset-support relation.

### Weighted/COUNT relation certificate

A relation matrix over a declared semiring composes by semiring matrix multiplication. If a verified semiring homomorphism to Boolean support is available, erasure commutes with composition.

For natural-number witness counts, `n -> (n != 0)` is such a map, so

`support(A B)=support(A) support(B)`

where the right side is Boolean relational composition.

### MAY support certificate

Ordinary relation composition is always defined. It is therefore the total fallback when stronger closure gates fail.

## 3. Nested linear target defects form a short exact sequence

Work over `R=Z/p^K`. Let a finer linear observation have row module

`V=Row(A1)`

and a further coarsening have

`U=Row(A2) subseteq V`.

Let target row module be

`W=Row(B)`.

The two Structural Target defects are

`D2=(U+W)/U`

for the coarser world and

`D1=(V+W)/V`

for the finer world.

The map

`D2 -> D1`, `x+U |-> x+V`

is a natural surjection. Its kernel is

`((U+W) cap V)/U`.

Using the modular law because `U subseteq V`,

`(U+W) cap V = U + (W cap V)`.

Therefore

`ker ~= (W cap V)/(W cap U)`.

Define the incremental defect

`I_(2/1)=(W cap V)/(W cap U)`.

Then

`0 -> I_(2/1) -> D2 -> D1 -> 0`

is exact.

This is the exact composition law for nested linear target loss.

## 4. Exponent mass is chain-additive

Taking p-power cardinalities in the short exact sequence gives

`|D2|=|I_(2/1)| |D1|`.

Thus the integer exponent mass satisfies

`mu(D2)=mu(I_(2/1))+mu(D1)`.

Along any nested chain of linear collapses, incremental exponent masses telescope. The total scalar repair mass is path independent once the endpoints and target are fixed.

This does **not** make the defect mass a matroid/polymatroid rank. Supplement 20 already gave submodularity and supermodularity failures away from a single nested chain. Chain additivity is strictly weaker than a global lattice-rank law.

## 5. Exponent profiles do not compose without extension data

The short exact sequence determines cardinality, but the exponent profile of the middle module is not determined by the profiles of the submodule and quotient.

Inside the same ambient target group

`T=Z/4 x Z/2`,

let

`H1=< (2,0) > ~= Z/2`.

Two larger defect groups are possible:

`H2a=< (1,0) > ~= Z/4`,

and

`H2b=< (2,0),(0,1) > ~= Z/2 x Z/2`.

In both chains,

`profile(H1)=(1)`

and

`profile(H2/H1)=(1)`.

But the total profiles are respectively

`(2)` and `(1,1)`.

Therefore an exact composable structured certificate must retain an actual module/group presentation and morphisms, or equivalent extension data. Rank, total mass and invariant-factor profile are complexity summaries, not complete composition state.

## 6. No automatic upward lift

Every sound erasure used by the compiler is one-way unless an explicit reconstruction certificate is supplied.

Three minimal boundaries already exist.

1. **MAY does not determine COUNT.** A single support edge with witness count 1 and the same edge with count 2 have identical Boolean support.
2. **Coset support does not determine action transport.** Supplement 22's `Z/6 -> Z/2` example has identical full `Z/3` support on both coarse fibers but opposite target derivatives for the same kernel translation.
3. **Profile does not determine structured defect.** The extension example above has identical stage profiles but different total modules; Supplement 21 additionally showed identical A3 relation exponent profiles with different projective directions.

Hence a compiler may automatically **demote** along a verified forgetful map, but it must never infer a stronger certificate from a weaker one merely because some stronger realization exists.

## 7. Typed partial composition table

The current fail-closed table is:

| Certificate kind | Strong composition when gate passes | Safe fallback |
|---|---|---|
| function | function composition / constant-on-new-fibers | MAY graph/support |
| p-adic module defect | short exact sequence with explicit module maps | coset/MAY support |
| homogeneous group defect | subgroup extension with derivative homogeneity | coset/MAY support |
| semiring-weighted relation | semiring matrix composition | MAY via declared Boolean factor |
| MAY correspondence | relation composition | itself |

The table is partial at the strong level but total at MAY level.

This is the intended meaning of a **typed defect certificate calculus**: not one universal defect algebra, but a family of exact algebras connected by explicit erasure morphisms.

## 8. Validation

Independent exact checks include:

- 12,526 nested finite set-partition / binary-target cases on carriers up to five states: `R_(r o q,t)=r^op;R_(q,t)` exactly;
- 6,561 pairs of 2x2 natural-number witness matrices with entries 0,1,2: Boolean support of count-semiring product exactly equaled relational composition of Boolean supports;
- 1,171 nested cyclic-group quotient / homomorphic-target cases: target supports were exact variation-subgroup cosets and sequential MAY support matched the composite collapse;
- 4,000 random nested p-power row-module systems: the linear defect short-exact-sequence cardinality identity held exactly;
- additional small subgroup-chain checks confirmed telescoping exponent-mass additivity.

These are finite exact WIP checks, not fresh full-repository CI or canonical-main claims.

## 9. Ownership and next frontier

Generic future-safe quotient descent remains P023. Generic relation/correspondence composition remains A4. Semiring-weighted relation composition and finite-group/module exact sequences are prior mathematics. R004's addition is the typed compiler dispatch/composition contract and the explicit no-upward-lift boundary.

The next frontier is **certificate minimization under composition**: given a multi-stage future program, determine the weakest certificate type and smallest retained generator surface that can be transported through the whole program without reopening fine state. This combines the obstruction-cut basis of Supplements 16–19 with the typed composition laws here.
