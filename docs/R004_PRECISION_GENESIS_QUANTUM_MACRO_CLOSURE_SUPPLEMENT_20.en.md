# R004 precision genesis — Supplement 20: p-adic structural target cuts

Status: `PROVED_WIP + EXECUTABLE_REFERENCE + STRUCTURE-PRESERVATION SPECIALIZATION + PRIOR_ART_BOUNDED`  
Parent: `R004_PRECISION_GENESIS_QUANTUM_MACRO_CLOSURE_SUPPLEMENT_19.en.md`  
Owner branch: `research/r004-precision-genesis-closure-20260810`

Supplements 16–19 compiled generator cuts for preserving the exact full carrier and then found arithmetic and matroid closed forms. This supplement changes the target: the retained future language need not reconstruct exact state. It must preserve a declared **linear target quotient**.

The main object is no longer an ordinary residue-field rank defect. Over `Z/p^K`, target preservation is controlled by a missing row-submodule quotient. The residue-field matroid of Supplement 19 reappears only at `K=1` or in the exact-state specialization.

## 1. Setup

Let

`R = Z/p^K Z`, `X=R^d`.

The current observation is

`O_A(x)=A x`,

and the target structure that must remain reconstructible is

`T_B(x)=B x`.

Primitive future instructions are coordinate resets `Z_i` that set coordinate `i` to zero. If the retained reset set is `S` and `H=E\S` is hidden, the exact future-safe carrier candidate is

`q_S(x)=(A x, x|_S)`.

Two states have the same `q_S` state iff their difference is supported on `H` and lies in `ker A_H`.

Therefore `B x` factors through `q_S` iff

`ker A_H subseteq ker B_H`.

This is the exact target-preservation criterion.

## 2. Row-submodule dual criterion

Use the standard perfect dot pairing on the finite module `R^H`. For every matrix `M`, `Row(M)` annihilates `ker M`. Smith diagonalization over an integer lift gives the same cardinality to `Row(M)` and the full annihilator of `ker M`, so

`Row(M) = Ann(ker M)`.

Hence

`ker A_H subseteq ker B_H`

iff

`Row(B_H) subseteq Row(A_H)`.

Thus preservation of the target quotient is not merely a rank condition: it is exact **row-submodule inclusion**.

## 3. Missing-target module

Define

`D_H = (Row(A_H)+Row(B_H)) / Row(A_H)`.

Then

`target safe on H  <=>  D_H = 0`.

The module `D_H` is a finite abelian p-group. It is therefore a typed missing-structure object, not only a Boolean failure flag.

Define the integer structural repair mass

`Delta(H)=log_p |D_H|`.

No real logarithm is required computationally: `|D_H|` is a p-power and `Delta(H)` is obtained by exact repeated division by `p`.

If `H subseteq J`, coordinate restriction `R^J -> R^H` maps `Row(A_J)` onto `Row(A_H)` and the stacked row module onto the smaller stacked row module. Hence it induces a surjection

`D_J ->> D_H`.

Consequently

`Delta(H) <= Delta(J)`.

Hiding more coordinates cannot reduce the amount of target structure missing from the coarse world.

## 4. Smith exponent-mass compiler

Let `M` be any matrix over `R`. Choose canonical integer representatives and an integer Smith normal form with diagonal entries `d_i`. Put

`v_i=min(nu_p(d_i),K)`, treating `d_i=0` as `v_i=K`.

Then

`mu_K(M)=log_p |Row_R(M)| = sum_i (K-v_i)`.

Therefore the target defect has the closed form

`Delta(H)=mu_K([A_H;B_H]) - mu_K(A_H)`.

This gives a scalable exact backend based on Smith invariants. The committed reference implementation deliberately uses finite row-module enumeration instead, so the semantic oracle remains independent and transparent; a future optimized backend can replace enumeration without changing the theorem interface.

## 5. Field specialization: relative circuits

At `K=1`, write

`C=[A;B]`.

Then `H` is target-breaking iff

`rank C_H > rank A_H`.

An inclusion-minimal target-breaking set `H` is exactly a set that is

- a circuit of the column matroid `M(A)`, and
- independent in the column matroid `M(C)`.

Proof sketch. Minimality means every proper subset has equal A- and C-rank. If H is unsafe, some A-dependence is removed by the added B coordinates. Taking an A-circuit inside a smallest such dependence gives a proper unsafe subset unless the circuit is all of H; its proper subsets are A-independent and hence also C-independent, while H itself becomes C-independent because B resolves the unique A-circuit dependence.

For the exact-state target `B=I`, the stacked column matroid is free, so every circuit of `M(A)` is relative. This recovers Supplement 19.

## 6. Relative cuts need not form a matroid

The exact-state Module Cut Compiler had the especially strong form

`cuts = circuits(M(A mod p))`,

so minimal carrier instructions were dual-matroid bases.

That does **not** extend to a general target B.

Over `F_2`, take

`A=(0,1,1,1)`,

`B=(0,0,0,1)`.

The minimal target cuts are

`{1,3}` and `{2,3}`.

They violate circuit elimination: after eliminating the common element `3`, there is no cut contained in `{1,2}`. Equivalently, the target-safe hidden-set family violates matroid augmentation.

Thus the relative target-cut clutter is generally a genuine hypergraph obstruction family, not the circuit family of another ordinary matroid.

## 7. Higher-p-adic information invisible mod p

Residue-field rank can miss target structure.

Over `Z/4`, let

`A=(1,1)`, `B=(0,2)`.

Modulo 2, stacking B does not increase rank. But `z=(1,3)` satisfies

`A z=0 mod 4`,

while

`B z=2 mod 4`.

So target B is not recoverable from A.

More generally, over `Z/p^K`, take

`A=(1,1)`, `B=(0,p^t)`, `1<=t<K`.

The only minimal hidden cut is the two-coordinate set and

`D_H ~= Z/p^(K-t) Z`,

so

`Delta(H)=K-t`.

All these examples have the same residue-field B row (zero), yet their missing target depth ranges through `1,...,K-1`. Ordinary mod-p matroid data therefore cannot encode the full structural repair precision.

## 8. Defect mass is monotone but not a polymatroid rank

`Delta(H)` is monotone under hidden-set inclusion by the quotient-surjection theorem above.

However exact primitive-column examples over `Z/4` show that `Delta` can fail submodularity, and other primitive-column examples show that it can fail supermodularity. Hence the scalar defect mass is not, in general, an ordinary matroid or polymatroid rank function.

The typed primitive is the missing-target p-group `D_H`; `Delta(H)` is only its integer exponent mass.

This also connects directly to the earlier quotient exponent-profile compiler: the invariant-factor exponent word of `D_H` is an exact typed repair profile for the structure lost by hiding H.

## 9. Compiler architecture consequence

The cut atlas now has three levels.

1. **Exact-state module reset**: mod-p column matroid circuits; minimal instructions are dual-matroid bases.
2. **Field target quotient**: relative circuit clutter between `M([A;B])` and `M(A)`; generally not itself matroidal.
3. **p-adic target quotient**: minimal supports where the missing row-submodule quotient `D_H` is nonzero; each cut carries a finite p-group repair object and exponent mass.

Thus `preserve exact state` and `preserve declared structure` are mathematically different compiler problems. The latter can require precision hidden above the residue field.

## 10. Validation

Independent exact checks for this supplement include:

- 1,024 exhaustive `Z/4`, two-coordinate one-row A/B retained-set cases: kernel-inclusion target safety exactly matched row-submodule inclusion;
- 4,800 additional small p-power multirow cases: target safety exactly matched `Delta(H)=0`;
- 793 finite-field one-row systems over `F_2` and `F_3`: minimal compiler cuts exactly matched the relative-circuit formula;
- 900 random small p-power matrices: direct row-module exponent mass exactly matched the Smith-invariant formula;
- explicit primitive-column examples verify that `Delta` can fail both submodularity and supermodularity.

These are finite exact WIP checks, not a fresh full-repository CI or canonical-main claim.

## 11. Prior-art boundary and next frontier

Smith normal form, finite abelian p-groups, matroid circuits/duality, modules over local/valuation rings, and matroids over rings/valuation rings are prior mathematics. R004 does not claim those theories.

The project-local addition under test is the compiler bridge:

`declared target quotient -> hidden-coordinate row-submodule defect -> structural cut clutter -> p-group repair profile`.

The next frontier is to replace the reference row enumeration by exact Smith/profile extraction and then test whether A3 determinant/exterior targets and guard-image lattices can be expressed as instances of the same `target object + defect module` interface without forcing nonlinear semantics into a linear module model.
