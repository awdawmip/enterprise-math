# X6 prime discriminant pairing: why locally balanced determinant-p blocks must carry a glue phase

Status: `RESEARCH_NOTE / DURABLE FRONTIER / NONCANONICAL / NOT_FOUNDATION / NOT_WORKING_TRUTH`
Date: `2026-09-08`
Scope: `Enterprise Math / P000 X6 / prime-index lattice gluing / BRC repair state`
Parents:
- `research_notes/x6_p3_exact_minimum_a2_common_depth_20260908.md`
- `research_notes/x6_p5_exact_minimum_golden_discriminant_gluing_20260908.md`
- `research_notes/x6_index_p_branch_smith_quadric_split_20260908.md`
EM source snapshot before write: `awdawmip/enterprise-math@04361f94b24c9afb3e9d27c04ad90ac12fd700fd`

## 0. Purpose

The exact p=3 and p=5 minima expose a common feature that is invisible if one records only the singular spectrum.

Their active Gram structures can be decomposed into two positive-definite integral blocks of determinant p whose direct sum has determinant `p^2`. The direct sum becomes the Gram of an index-p sublattice of a standard integer lattice only because the two determinant-p discriminant forms carry compatible, cancelling glue phases.

This note isolates that exact mechanism.

It also records a p=7 exact upper-bound construction, found after exhaustive traversal of all `|P^5(F_7)|=19608` projective index-7 branches with one deterministic LLL-reduced basis per branch:

`delta_min(7) <= 68`.

The p=7 value 68 is **not** promoted to an exact minimum here, because one LLL basis per branch is not an exhaustive search over all unimodular basis changes. The construction itself is exact and is used only as a gluing example.

## 1. Determinant-p block discriminant form

Let H be an integral positive-definite `r x r` Gram matrix with

`det H=p`

for an odd prime p.

The discriminant group

`D_H=H^{-1} Z^r / Z^r`

has order p and is therefore cyclic.

Choose a generator `g`. The induced rational bilinear form on the discriminant group has the form

`b_H(g,g)=a/p (mod Z)`

for some nonzero

`a in F_p^*`.

Changing the generator by `g -> u g` multiplies a by `u^2`. Thus the square class

`[a] in F_p^*/(F_p^*)^2`

is an invariant of the determinant-p discriminant form.

Call this the **discriminant phase square class** of H.

It is a downstream arithmetic/lattice observer, not a new P000 primitive.

## 2. Exact two-block gluing criterion

Let H and K be determinant-p integral positive-definite blocks with discriminant coefficients a and b in chosen generators.

The direct sum lattice has discriminant group

`D_H direct_sum D_K ~= F_p^2`

with bilinear form

`(x,y) -> (a x^2+b y^2)/p (mod Z)`.

An integral overlattice of index p corresponds to an order-p isotropic subgroup of this discriminant group.

A nonzero vector `(x,y)` is isotropic iff

`a x^2+b y^2 ==0 (mod p)`.

Because a,b are nonzero, an isotropic vector must have both coordinates nonzero. Dividing gives

`(x/y)^2 == -b/a (mod p)`.

Therefore:

`boxed: H direct_sum K admits an index-p integral unimodular gluing`

`iff -b/a is a quadratic residue mod p.`

Equivalently the two one-dimensional discriminant forms are negatives of each other up to square rescaling.

After such a gluing, the determinant drops from `p^2` to 1 because an index-p overlattice divides the determinant by `p^2`.

Strength boundary: the resulting positive-definite unimodular overlattice need not be identified with the standard coordinate lattice solely from this abstract criterion in arbitrary rank. An actual X6 coordinate realization requires an explicit isometry/embedding or a separate low-rank classification. The p=3,5,7 examples below have explicit integer matrices, so that extra issue is resolved there.

## 3. p=3: A2 block plus common-depth scalar are opposite phases

The exact p=3 minimizer has active Gram

`H_A2 direct_sum [3]`,

where

`H_A2=[[2,-1],[-1,2]]`, `det H_A2=3`.

Its inverse is

`H_A2^(-1)=(1/3)[[2,1],[1,2]]`.

A discriminant generator therefore has coefficient

`a=2=-1 (mod3)`.

The scalar block `[3]` has discriminant coefficient

`b=1`.

The isotropy equation is

`2x^2+y^2=0 (mod3)`,

which has the nonzero solutions `y=+/-x`.

Thus the A2 relative-difference lattice and the common-depth scalar direction have exactly opposite discriminant phases and glue to the standard index-3 active `Z^3` geometry exhibited by B3.

This gives a precise lattice-gluing meaning to the p=3 “A2 + common depth repair” language.

## 4. p=5: two identical binary blocks can glue because -1 is a square

The p=5 exact minimum uses two copies of

`K5=[[2,-1],[-1,3]]`, `det K5=5`.

Its inverse is

`K5^(-1)=(1/5)[[3,1],[1,2]]`.

A generator has coefficient

`a=3 (mod5)`.

For two identical copies the gluing equation becomes

`3x^2+3y^2=0`

or

`x^2+y^2=0 (mod5)`.

Because

`2^2=-1 (mod5)`,

there is an isotropic order-5 subgroup. The two discriminant-5 metric planes can therefore glue to the explicit rank-4 index-5 integer block C5.

This is the exact arithmetic reason two copies of a determinant-5 block that cannot individually be full-rank integer coordinate transports can nevertheless combine into an integral index-5 rank-4 transport.

## 5. Why the same binary self-gluing fails at p=7

Consider the low-trace binary determinant-7 block

`K7=[[2,1],[1,4]]`, `det K7=7`.

Its inverse is

`K7^(-1)=(1/7)[[4,-1],[-1,2]]`.

A generator has coefficient

`a=4`, a square modulo 7.

Two identical K7 blocks would require

`x^2+y^2=0 (mod7)`.

But `-1` is not a square modulo 7.

Therefore two identical binary determinant-7 blocks **cannot** cancel their discriminant phases to form an integral unimodular gluing.

This is a local gluing obstruction separate from, but arithmetically resonant with, the earlier global theorem that p=7 cannot have strict p^3 X6 isotropy.

The two statements must remain typed separately.

## 6. Exact p=7 upper-bound construction: binary + ternary opposite phases

An exact determinant-7 X6 transport is

`A7=`

`[[ 0,-1,-1, 0, 0,-1],`

` [ 1, 0, 0, 0, 0, 0],`

` [ 0, 1, 0,-1, 0,-1],`

` [ 0, 0, 1, 0, 0,-1],`

` [ 0, 0, 0,-1, 1, 1],`

` [ 0, 0, 0, 1, 1, 0]]`.

It has

`|det A7|=7`.

Its Gram matrix is

`G7=`

`[[1,0,0,0,0,0],`

` [0,2,1,-1,0,0],`

` [0,1,2,0,0,0],`

` [0,-1,0,3,0,0],`

` [0,0,0,0,2,1],`

` [0,0,0,0,1,4]]`.

Thus

`G7 = [1] direct_sum H7_3 direct_sum K7`,

where

`H7_3=[[2,1,-1],[1,2,0],[-1,0,3]]`, `det H7_3=7`,

and K7 is the binary block above.

The diagonal defect is 32 and there are three unit off-diagonal entries, hence

`Delta_6(A7)=32+36=68`.

Therefore

`boxed: delta_min(7)<=68`.

No lower-bound equality is claimed here.

## 7. p=7 ternary block supplies the missing discriminant phase

The adjugates are

`adj(K7)=[[4,-1],[-1,2]]`,

`adj(H7_3)=[[6,-3,2],[-3,5,-1],[2,-1,3]]`.

Choose discriminant generators corresponding to the first dual coordinate in each block. Their coefficients are

`a_K=4`,

`a_H=6=-1 (mod7)`.

The gluing equation is

`4x^2+6y^2=0 (mod7)`,

or

`4x^2-y^2=0`.

It has solutions

`y=+/-2x`.

So the binary determinant-7 block and the ternary determinant-7 block have exactly the compatible opposite phase required for integral gluing.

This explains the exact rank-5 construction structurally:

`DET-7 BINARY PHASE + COMPLEMENTARY DET-7 TERNARY PHASE`

`-> INDEX-7 RANK-5 INTEGER GLUING`.

## 8. The emerging discriminant-p pairing hierarchy

The first exact/candidate active geometries can now be retyped as pairs of determinant-p discriminant blocks:

| p | determinant-p block ranks in displayed construction | status |
| ---: | --- | --- |
| 2 | `1+1` | exact global minimum |
| 3 | `2+1` | exact global minimum |
| 5 | `2+2` | exact global minimum |
| 7 | `3+2` | exact construction / upper bound 68 only |

The sum of block ranks is the active repair rank in these representatives.

The table is **not** yet a theorem that repair rank grows monotonically with p. Split primes can have low-rank Gaussian structures, and different determinant-p forms can carry different discriminant phases.

The stronger durable hypothesis is instead:

> One-step prime geometry is controlled by a search over determinant-p metric blocks **together with their discriminant phases and gluing compatibility**, not by determinant, singular values, support rank, or prime congruence alone.

## 9. BRC significance

The discriminant phase is exactly a repair coordinate that disappears under several tempting compressions:

- determinant p alone does not retain it;
- block eigenvalues alone do not retain it;
- scalar anisotropy Delta does not retain it;
- support rank alone does not retain it.

Yet the phase decides whether two locally valid metric blocks can be combined into an integral index-p geometry.

Therefore:

`CURRENT METRIC QUALITY != GLUING COMPATIBILITY`,

`SAME DETERMINANT != SAME DISCRIMINANT PHASE`,

`SPECTRAL EQUIVALENCE != INTEGRAL COMPOSITION EQUIVALENCE`.

This is a direct BRC / operation-safe quotient witness.

## 10. Relation to chi_-4

For two identical determinant-p blocks with the same discriminant phase, self-gluing requires

`x^2+y^2=0 (mod p)`.

For odd p this is possible exactly when

`chi_-4(p)=+1`.

Thus the mod-4 character reappears here as a **self-gluing character**.

But if two blocks have different phase classes, an inert prime may still glue after pairing complementary forms, as p=3 and p=7 explicitly demonstrate.

So:

`chi_-4=-1` forbids SAME-PHASE SELF-GLUING`,

not all determinant-p gluing.

This distinction is essential.

## 11. Tool / observer audit

`T0_BRC`: `REUSE_APPLIED` — discriminant phase retained as composition-relevant provenance.

`T6_OPERATION_SAFE_QUOTIENT`: `REUSE_APPLIED` — determinant/spectrum/Delta/support-only quotients are unsafe for gluing questions.

`T7_FINITE_SYMMETRY_EQUIVARIANCE`: `REUSE_APPLIED` — displayed blocks are representatives, not canonical axis choices.

`T9_HOLONOMY_COCOYCLE_GLUING`: `COMPOSE_APPLIED` — the discriminant-phase matching condition is an exact finite gluing obstruction/repair law. No global physical holonomy interpretation is claimed.

No new top-level tool family is proposed.

## 12. Status ledger

Exact theorem in this note:

- two determinant-p cyclic discriminant blocks admit an index-p integral unimodular gluing iff their one-dimensional discriminant forms contain a nonzero isotropic pair, equivalently iff `-b/a` is a square modulo p;
- p=3 A2 and scalar-3 blocks have complementary phases;
- p=5 two K5 blocks self-glue because -1 is a square mod5;
- two identical K7 blocks cannot self-glue because -1 is not a square mod7;
- K7 and the displayed H7_3 block have complementary phases and glue in the explicit index-7 rank-5 construction;
- explicit p=7 construction has `Delta_6=68`, hence `delta_min(7)<=68`.

Not proved:

- `delta_min(7)=68`;
- that every global minimizer decomposes orthogonally into exactly two determinant-p blocks;
- a formula for the minimum active repair rank;
- that discriminant phase alone determines the optimal one-step geometry.

## 13. Next frontier

Two routes are now sharply separated:

1. **Exact p=7 lower bound:** certify or refute `delta_min(7)=68` by exhaustive sparse-Gram analysis under `Delta<68` or a stronger structural inequality.
2. **General discriminant-block calculus:** classify low-rank positive integral determinant-p forms by `(rank, trace/shape cost, discriminant phase)` and solve the minimum-cost compatible-pair gluing problem inside total rank at most 6.

The second route is likely the more reusable explanation if it succeeds; the first supplies the next hard finite theorem test.
