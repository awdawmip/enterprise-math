# P025 Supplement 37 — Radius-Dependent Smith Tower of Certificate Obstructions

Status: `ACTIVE RESEARCH NOTE / NONCANONICAL`  
Owner generation: `program/p025-certificate-index-stage34`  
Depends on: P025 Supplements 35–36  
Hard block: `NONE`

## 1. Group order is still too coarse along the radius tower

Supplement 36 defines, once full certificate rank is visible,

\[
\mathcal D_R
=
\operatorname{Sat}(C)/C_R
\]

and the terminal intrinsic quotient

\[
\mathcal D_\infty
=
\operatorname{Sat}(C)/C.
\]

Their orders give

\[
|\mathcal D_R|
=
\delta_H J_H(R).
\]

But Stage 35 shows that equal orders do not classify multidimensional congruence structure. Therefore each radius should retain the full Smith signature of `D_R` whenever the certificate rank is complete.

## 2. P025-D24 — Smith defect state at radius `R`

Let the labelled generators of `C_R` have rational rank `d`, equal to the full certificate rank. Define determinantal divisors

\[
\Delta_i(R)
\]

and invariant factors

\[
\boxed{
s_i(R)=\Delta_i(R)/\Delta_{i-1}(R),
\qquad i=1,\ldots,d.
}
\]

Then

\[
\boxed{
\mathcal D_R
\cong
\bigoplus_{i=1}^d\mathbb Z/s_i(R)\mathbb Z.
}
\]

The terminal signature

\[
(s_1(\infty),\ldots,s_d(\infty))
\]

is the intrinsic certificate-defect signature from Stage 35.

## 3. Exact arithmetic multi-certificate example: `3+7=10`

For

\[
3+7=10
\]

the block-value relation lattice has the standard rank-two basis

\[
g_1=(1,0,1),
\qquad
 g_2=(0,1,1).
\]

Declare two labelled certificates

\[
\boxed{
H(u,v,w)=(2u,2v).
}
\]

The complete certificate image is

\[
C=2\mathbb Z^2.
\]

Hence the terminal defect group is

\[
\boxed{
\mathcal D_\infty
\cong
\mathbb Z/2\oplus\mathbb Z/2,
}
\]

with Smith signature

\[
\boxed{(2,2)}
\]

and order four.

### Radius one

The radius-one relation states generate the index-two relation sublattice with coordinate generators

\[
(1,1),
\qquad
(1,-1).
\]

Applying `H` gives certificate generators

\[
(2,2),
\qquad
(2,-2).
\]

Their determinantal divisors are

\[
\Delta_1=2,
\qquad
\Delta_2=8,
\]

so

\[
\boxed{
\mathcal D_1
\cong
\mathbb Z/2\oplus\mathbb Z/4.
}
\]

Thus

\[
|\mathcal D_1|=8,
\qquad
J_H(1)=8/4=2.
\]

### Radius two

The relation lattice is fully generated, so

\[
C_2=C
\]

and

\[
\boxed{
\mathcal D_2
=
\mathcal D_\infty
\cong
\mathbb Z/2\oplus\mathbb Z/2.
}
\]

The exact Smith tower is therefore

\[
\boxed{
(2,4)
\longrightarrow
(2,2).
}
\]

This is a real arithmetic relation in which increasing access changes the finite congruence **type**, not only its cardinality.

## 4. The extension is again not a direct-sum bookkeeping rule

For the same example,

\[
C/C_1
\]

has order two, while

\[
\mathcal D_\infty
\cong
\mathbb Z/2\oplus\mathbb Z/2.
\]

If access and intrinsic defects simply formed a direct sum, the radius-one group would be

\[
(\mathbb Z/2)^3.
\]

Instead

\[
\boxed{
\mathcal D_1
\cong
\mathbb Z/2\oplus\mathbb Z/4.
}
\]

so the access kernel is absorbed into a longer `2`-power cyclic factor. This is the multidimensional version of the scalar `4+11=15` nonsplitting example.

## 5. Early terminal stabilization: `3+4=7`

For the raw scalar Wronskian of

\[
3+4=7,
\]

the terminal defect signature is

\[
(4).
\]

Radius one already generates the complete Wronskian image, so the Smith tower is terminal immediately:

\[
\boxed{(4)}.
\]

But the relation lattice itself is still rank-deficient at radius one and completes only at radius two.

Thus even the **full finite congruence type** of a declared certificate can stabilize before relation-state rank does.

## 6. Pure access tower: `1+22=23`

Here the terminal raw Wronskian image is saturated, with signature

\[
(1).
\]

The finite tower is

\[
\boxed{
(2)
\longrightarrow
(1),
}
\]

at radii two and four. The obstruction is entirely access-induced.

## 7. Prime-local view

For each prime `ell`, the sequence

\[
\bigl(v_\ell(s_1(R)),\ldots,v_\ell(s_d(R))\bigr)
\]

gives the `ell`-primary certificate-obstruction state at radius `R`.

In the `3+7=10` example, the `2`-primary state changes from

\[
(1,2)
\]

to

\[
(1,1).
\]

This is more informative than saying merely that the total index falls from eight to four.

## 8. Architectural meaning

The certificate precision hierarchy now has four layers:

\[
\boxed{
\text{rational rank}
\to
\text{finite obstruction order}
\to
\text{Smith obstruction type}
\to
\text{labelled quotient map}.
}
\]

Stage 35 already warns that the Smith type still does not determine the labelled embedding/kernel required for arbitrary fixed-coordinate target membership. Therefore the Smith signature is an exact abstract-group state, not automatically the final P023-minimal labelled state.

## 9. Prior-art / ownership boundary

All Smith/invariant-factor mathematics is prior art. The project-side pressure-test result is the radius-indexed use of those invariants as finite certificate precision states and the strict separation from the richer relation state.

## 10. Executable assets

Added:

- `src/enterprise_math/certificate_defect_tower.py`;
- `tests/test_certificate_defect_tower.py`.

The tower stores strict changes of the finite Smith signature through certificate completion.

## 11. Next frontier

No hard block exists. Continue with:

1. the **labelled quotient map** needed for exact target membership, not only abstract group type;
2. canonical congruence normal forms for certificate targets;
3. task-relative coarsening when only selected target classes are queried;
4. Foundation backflow of the rank / index / Smith / labelled-kernel ladder.
