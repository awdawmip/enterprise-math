# R004 precision genesis — Supplement 19: module cut compiler and dual-matroid instruction bases

Status: `PROVED_WIP + EXECUTABLE_CHECKED + PRIOR_ART_SPECIALIZATION + MODULE_CUT_CLOSED_FORM`  
Parent: `R004_PRECISION_GENESIS_QUANTUM_MACRO_CLOSURE_SUPPLEMENT_18.en.md`  
Owner branch: `research/r004-precision-genesis-closure-20260810`

Supplement 18 gave the first arithmetic closed-form obstruction compiler. This supplement gives a linear/module analogue in which the complete carrier-cut clutter is a representable matroid circuit family, and all minimal Carrier Bases are obtained without hypergraph dualization.

## 1. Finite p-power module world

Let

`R=Z/p^K Z`, `X=R^d`,

and let the current observation be

`O_A(x)=A x in R^r`

for an `r x d` integer matrix read modulo `p^K`.

Assume every column `A_i` is primitive mod `p`: at least one entry of that column is nonzero modulo `p`. For each coordinate `i`, declare the future generator `Z_i` that resets coordinate `i` to zero.

## 2. R004-COMP-T35 — retained-reset quotient

For retained reset set `S`, define

`q_S(x)=(Ax,x|_S)`.

This is exactly the coarsest future-safe quotient.

Sufficiency is immediate: equal `Ax` and equal retained coordinates give equal observations after every composition of retained resets.

Necessity follows from

`Ax-A(Z_i x)=A_i x_i`.

Because `A_i` has a unit entry, multiplication `x_i -> A_i x_i` is injective in `R`; hence current and one-reset observations recover each retained coordinate exactly.

Thus

`Compile_S(P0)=ker q_S`, where `P0=ker A`.

With all resets retained, the carrier is discrete.

## 3. R004-COMP-T36 — hidden injectivity is controlled mod p

Let `H` be the deleted/hidden coordinate set. The retained quotient is discrete iff the restricted map

`A_H:R^H -> R^r`

is injective.

This occurs iff the reduced columns

`bar A_H=A_H mod p`

are linearly independent over `F_p`.

Elementary proof. If `bar A_H` is independent and `A_H v=0` for nonzero `v`, divide `v` by the largest common power `p^t`; the resulting vector has a unit coordinate, and reducing the equation modulo `p` gives a nonzero kernel vector of `bar A_H`, contradiction. Conversely, if `bar A_H c=0` for nonzero `c mod p`, lift `c` and multiply by `p^(K-1)` to obtain a nonzero kernel vector of `A_H` in `R^H`.

So the entire p-power carrier obstruction is already visible in the residue-field column dependence pattern.

## 4. R004-COMP-T37 — carrier cuts are matroid circuits

Let `M(A mod p)` be the column matroid represented over `F_p`.

A hidden set `H` is carrier-breaking iff it is dependent in this matroid. Therefore the inclusion-minimal carrier cuts are exactly

`C_car = Circuits(M(A mod p))`.

This specializes Supplement 16's abstract deletion-cut clutter to a standard algebraic object.

## 5. R004-COMP-T38 — minimal Carrier Bases are dual-matroid bases

A retained reset set `S` preserves the discrete carrier iff it intersects every circuit of `M`, equivalently iff its complement `E\S` contains no circuit and is therefore independent.

`S` is inclusion-minimal iff `E\S` is maximal independent, i.e. a basis of `M`.

Hence

`B_C = {E\B : B in Bases(M)} = Bases(M*)`.

All minimal Carrier Bases therefore have the same cardinality

`|S| = d-rank(A mod p)`.

This is a stronger result than generic cut dualization: one Gaussian-elimination column basis immediately gives one minimum instruction set, and enumerating all column bases enumerates all minimal Carrier Bases.

## 6. Relation to representation codimension

Earlier relation-rank compilation used `Gamma=K(d-r)` to count exact p-adic digit freedoms removed by a rank-`r` relation carrier.

Here the same rank defect appears at the **instruction** level:

`instruction_nullity = d-rank(A mod p)`.

The two quantities should not be conflated: `Gamma` counts p-adic state digits, while the new nullity counts primitive coordinate-reset instructions needed to recover the exact carrier from the current linear observation. But they are controlled by the same residue-field rank defect.

## 7. Examples

- Full-rank observation `A=I_d`: no circuits, no reset instructions are carrier-required.
- One-row equal nonzero columns: all pairs are circuits; every minimal reset basis has size `d-1`.
- Triangle representation over `F_2`, columns `(1,0),(1,1),(0,1)`: the unique circuit is all three columns; any one reset is a minimal Carrier Basis.

## 8. Exact validation

Independent exact checks covered **2,247** p-power matrix systems across `p=2,3`, `K=1,2`, `d=2,3`, and one/two observation rows, with every column primitive modulo `p`.

- all **13,320** retained-reset quotient cases matched `ker(Ax,x|_S)`;
- all **2,247** compiler-derived minimal carrier-cut families matched the circuits of `A mod p`;
- all **2,247** inclusion-minimal compiler Carrier Basis families matched complements of column bases.

No violations were found.

Executable reference: `src/enterprise_math/precision_module_cut_compiler.py`; regressions: `tests/test_precision_module_cut_compiler.py`.

No fresh full-repository CI or canonical-main status is claimed.

## 9. Prior-art boundary

Matroid circuits as minimal dependent sets, representable/vector matroids, dual matroids, complements of bases, finite-field linear algebra, and local-ring/Nakayama-style reduction modulo the maximal ideal are established mathematics.

R004 claims only the compiler bridge:

`p-power linear observation + coordinate resets -> residue-field column matroid -> circuits as carrier cuts -> dual bases as minimal carrier instructions`.

Historical novelty remains `NOVELTY_UNVERIFIED`.

## 10. Architectural consequence

The algebraic cut atlas now contains two genuinely different dependency geometries:

- integer weighted binary observation -> minimal non-dissociated supports;
- p-power linear module observation -> representable-matroid circuits.

The generic obstruction clutter is therefore not one fixed combinatorial species; the typed observation/action algebra determines which dependency geometry compiles the cuts.

## 11. Next frontier

The next useful target is a richer module/relation case where the full language does not necessarily make the carrier discrete. The aim is to derive cut edges for preserving a specified quotient exponent profile or A3 relation rank, rather than only exact-state recovery.
