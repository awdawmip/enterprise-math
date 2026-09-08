# X6 Gram common-depth quotient: bounded anisotropy becomes finitely many determinant curves

Status: `RESEARCH_NOTE / DURABLE FRONTIER / NONCANONICAL / NOT_FOUNDATION / NOT_WORKING_TRUTH`
Date: `2026-09-08`
Scope: `Enterprise Math / P000 X6 / natural-number metric geometry / prime-index variational reduction`
Parents:
- `research_notes/x6_p19_exact_minimum_same_phase_false_optimum_20260908.md`
- `research_notes/x6_p13_exact_minimum_saturated_ternary_self_gluing_20260908.md`
- `definitions/ENTERPRISE_X6_NATIVE_SPATIAL_CELL_TORSOR_20260905.md`
EM source snapshot before write: `awdawmip/enterprise-math@37e9fc9e87f192e898a32bbfac69943c2f1c6897`

## 0. Main theorem package

The prime-by-prime exact atlas reveals an invariant that makes a genuine general reduction possible.

For a symmetric integral `6x6` Gram matrix G, define

`C(G)=6G-tr(G) I_6`.

Then:

1. `C(G)` is an exact integer traceless **centered metric-shape coordinate**;
2. `C(G+cI)=C(G)` for every integer c;
3. `C(G1)=C(G2)` iff `G2=G1+cI` for some integer c;
4. the anisotropy is exactly

`Delta_6(G)=tr(C(G)^2)/6`;

5. for a fixed shape C, every integral Gram representative is one common-scale translate

`G_k=G_C+kI`;

6. the arithmetic index condition becomes the one-variable determinant equation

`det(G_C+kI)=n^2`;

7. therefore a fixed anisotropy budget contains only finitely many centered integer shapes, and all possible integer/index events under that budget lie on a finite family of degree-six determinant-square curves.

This is the metric analogue of the already-admitted X6 `relative coordinate + common-depth repair` decomposition. It does not identify metric common depth with spatial common depth; they are typed analogous quotient structures.

## 1. Exact centered shape lattice

Let `Sym_6(Z)` be the additive group of symmetric integral `6x6` matrices.

For G in this group, set

`C=6G-tr(G)I`.

Then C satisfies:

- `C=C^T`;
- `tr C=0`;
- every off-diagonal entry of C is divisible by 6;
- all six diagonal entries of C are congruent modulo 6.

Define

`Shape_6(Z)`

as the subgroup of symmetric integral matrices satisfying exactly those four conditions.

The map

`CENTER_6: Sym_6(Z) -> Shape_6(Z)`,

`G -> 6G-tr(G)I`

is a group homomorphism.

Its kernel is exactly

`Z I_6`.

Indeed, `C(G)=0` gives `6G=tr(G)I`, so all off-diagonals vanish and all diagonals are equal integers.

Conversely every integer scalar matrix lies in the kernel.

The image conditions above are also sufficient. Given C in `Shape_6(Z)`, choose the unique

`t_0 in {0,1,2,3,4,5}`

with

`t_0 == -C_11 (mod6)`.

Then

`G_C=(C+t_0 I)/6`

is an integral symmetric matrix and

`tr G_C=t_0`, `C(G_C)=C`.

Hence there is an exact short sequence

`0 -> Z I_6 -> Sym_6(Z) -> Shape_6(Z) -> 0`.

## 2. Lossless repair coordinate

The centered shape C alone deliberately forgets one integer common-scale direction.

The canonical section above gives the lossless reconstruction

`G = G_C + k I`, `k in Z`.

Equivalently one may retain the trace

`tr G=t_0+6k`.

Thus:

`FULL INTEGRAL GRAM <-> CENTERED SHAPE C + INTEGER METRIC COMMON DEPTH k`.

This is directly analogous in form to the P000 X6 coordinate decomposition

`full signed spatial state <-> relative state + common depth`,

but the objects must remain typed separately:

- spatial common depth is a coordinate displacement repair;
- metric common depth is a scalar Gram/length-square repair.

No new spatial axis is introduced in either case.

## 3. Delta is exactly the shape norm

Let

`t=tr G`.

Then

`C=6G-tI`.

A direct expansion gives

`tr(C^2)`

`=36 tr(G^2)-12 t trG+6t^2`

`=36 tr(G^2)-6t^2`

`=6[6 tr(G^2)-t^2]`.

Therefore

`boxed: Delta_6(G)=tr(C^2)/6`.

In particular

`boxed: Delta_6(G+cI)=Delta_6(G)}`.

So Delta is not a generic size measure. It is exactly the squared Frobenius norm of the metric state after removing its common scalar scale.

This explains why the exact prime-minimum sequence need not increase with p: increasing the common metric depth is free to this observer.

## 4. Centered form of the column-frame energy

If `G=A^T A` for an integer transport A with columns `a_1,...,a_6`, then

`tr G=sum_i ||a_i||^2`,

`tr(G^2)=sum_i ||a_i||^4 + 2 sum_(i<j)(a_i dot a_j)^2`.

Hence

`Delta_6(A)`

`=6 sum_i ||a_i||^4`

` +12 sum_(i<j)(a_i dot a_j)^2`

` -(sum_i ||a_i||^2)^2`.

Equivalently

`Delta_6=6 ||G-(trG/6)I||_F^2`.

Thus the one-step prime problem is an exact integral **nearly-tight frame / nearly-isotropic basis problem at fixed covolume**, with the important additional condition that the basis is the actual native transport frame rather than an arbitrary unframed lattice quotient.

Arbitrary `GL_6(Z)` right-basis changes do not preserve Delta and may not be silently quotiented. The safe finite symmetry is the declared signed-axis/permutation action that preserves the current observer.

## 5. Determinant polynomial of one shape

Fix a centered shape C and its canonical integral section `G_C`.

All integral lifts are

`G_k=G_C+kI`.

Define the monic degree-six integer polynomial

`P_C(k)=det(G_C+kI)`.

Changing the section only translates the variable k, so the determinant-curve class is intrinsic to the centered shape.

For a full-rank integer transport A of arithmetic index n,

`det(A^T A)=n^2`.

Therefore every index-n realization of shape C must satisfy

`boxed: P_C(k)=n^2`.

For a prime event this becomes

`boxed: y^2=P_C(k), y=p prime}`.

This is a necessary scalar-Gram condition. Native X6 admissibility can impose the further discriminant/gluing/lift restrictions already proved at p=7 and p=19.

## 6. Bounded-anisotropy finite-shape theorem

Fix a finite defect budget B.

If

`Delta_6(G)<=B`,

then

`tr(C(G)^2)<=6B`.

Since C is an integer matrix, there are only finitely many possible C.

Therefore:

`boxed: FIXED DELTA BUDGET -> FINITELY MANY CENTERED INTEGER METRIC SHAPES}`.

The common metric depth k may be unbounded, so this does **not** imply finitely many Gram matrices or finitely many arithmetic indices.

Instead all possible indices lie on a finite union of determinant-square equations

`y^2=P_C(k)`.

This turns the infinite prime-index minimization problem at bounded defect into a finite list of arithmetic curves plus native lift conditions.

This is the first non-prime-specific reduction produced by the current natural-number geometry route.

## 7. Generic and degenerate determinant curves

Because G_C is real symmetric,

`P_C(k)=product_i (k+lambda_i)`,

where `lambda_i` are its real eigenvalues.

Hence P_C has repeated roots exactly when the shape representative has repeated eigenvalues.

### Generic shape

If P_C is squarefree of degree six, then

`y^2=P_C(k)`

is a genus-two hyperelliptic curve after smooth projective completion. Classical finiteness theorems imply only finitely many rational points, hence finitely many integer prime hits, on that one fixed shape.

### Degenerate/repeated-spectrum shape

If P_C has repeated factors, the curve has lower geometric genus and can support qualitatively different arithmetic behavior.

The extreme case relevant here is a doubled rank-three block:

`G_C=H direct_sum H`.

Then

`P_C(k)=det(H+kI)^2`

is already a perfect square polynomial, so the square condition reduces to

`p=|det(H+kI)|`.

Thus repeated-block shapes are natural candidates for **recurrent low-defect prime families**.

Prime values of the resulting cubic polynomial are a separate arithmetic problem; no infinitude is claimed.

## 8. The p=13 shape predicts p=41 before a new search

The exact p=13 minimizer has

`G_13=H_13 direct_sum H_13`,

`H_13=[[2,-1,0],[-1,3,-1],[0,-1,3]]`,

and

`Delta_6=56`.

The shape shift law gives

`G(k)=(H_13+kI) direct_sum (H_13+kI)`

with the same Delta for every integer k.

Its determinant is

`det G(k)=q(k)^2`,

where

`q(k)=det(H_13+kI)`

`=k^3+8k^2+19k+13`.

The first values are

`q(0)=13`,

`q(1)=41`,

`q(2)=91`,

`q(3)=169`,

`q(4)=281`.

Therefore the centered-shape theory predicts an abstract determinant-41 Gram at exactly the same defect 56 before any p=41 optimization is run.

An explicit integer lift exists:

`A_41=`

`[[ 1,-1, 1,-1, 0, 0],`

` [ 1, 0,-1, 0, 1,-1],`

` [ 1, 0, 0, 1,-1, 1],`

` [ 0,-1,-1, 0,-1, 0],`

` [ 0,-1, 0, 0, 1, 1],`

` [ 0,-1, 1, 1, 0,-1]]`.

It satisfies

`|det A_41|=41`,

`A_41^T A_41=(H_13+I) direct_sum (H_13+I)`,

and therefore

`Delta_6(A_41)=56`.

A separate exact low-window certificate proves no determinant-41 transport has smaller Delta; that theorem is persisted separately.

This is the first exact recurrence of one centered metric shape at two distinct primes.

## 9. Discriminant phase is still required on a determinant curve

The determinant-square curve only controls abstract Gram scale.

For a doubled block `H_k direct_sum H_k` of prime determinant p, same-phase self-gluing into a standard index-p X6 transport requires

`x^2+y^2=0 (mod p)`

when the two discriminant phases are equal.

Thus even when the determinant polynomial hits a prime, `chi_-4(p)` can still decide native liftability.

This is exactly what killed the lower abstract optima at p=7 and p=19.

The p=13 -> p=41 recurrence succeeds because both primes are `1 mod4` and the explicit lifts exist.

Hence the correct shape-curve state is

`CENTERED SHAPE + COMMON DEPTH + DETERMINANT VALUE + DISCRIMINANT/LIFT STATE`,

not the polynomial value alone.

## 10. BRC / operation-safe scope

`T0_BRC`: `REUSE_APPLIED`.

- centered metric shape and common depth are retained as separate typed coordinates;
- native lift/discriminant state remains above the scalar determinant curve.

`T6_OPERATION_SAFE_QUOTIENT`: `REUSE_APPLIED`.

The quotient

`G -> C(G)`

is exact for current one-step anisotropy because Delta factors through C. It is **not** globally operation-safe for multiplication of transports:

`G(A B)=B^T G(A) B`

and cannot in general be reconstructed from C(A),C(B) alone.

Therefore full transport A/provenance must remain available when future multiplication is in scope.

`T9_HOLONOMY_COCOYCLE_GLUING`: `COMPOSE_APPLIED`.

Discriminant/lift state is retained as the repair above the centered-shape determinant curve.

No new top-level tool family is proposed yet. The shape quotient is a research mechanism pending broader verification.

## 11. Strongest current interpretation

The natural-number geometry now has a nested exact decomposition:

`ARITHMETIC INDEX n`

`-> FORCED MEAN SCALE n^(1/6)`

`+ CENTERED INTEGER METRIC SHAPE C`

`+ INTEGER METRIC COMMON DEPTH k`

`+ DISCRIMINANT / AMBIENT-LIFT REPAIR`

`+ FULL TRANSPORT / FUTURE-COMPOSITION PROVENANCE`.

The ordinary number line collapses almost all of these layers into one scalar coordinate.

This is a precise mathematical reason that arithmetic 2, or any prime p, need not correspond to one unique “natural point”.

## 12. Next frontier

The next general task is now sharply defined:

1. enumerate centered shape classes C by increasing `Delta=tr(C^2)/6`, modulo only observer-preserving signed/permutation symmetry;
2. attach the determinant polynomial `P_C(k)`;
3. factor its repeated-spectrum/curve type;
4. solve or bound prime-square hits;
5. apply discriminant/ambient-lift admissibility;
6. compare the resulting lower envelope with the exact atlas through p=19 and the new recurrence p=41.

This is a finite-shape arithmetic-curve program rather than blind enumeration over primes.
