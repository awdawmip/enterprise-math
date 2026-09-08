# X6 determinant-3 exact minimum: A2 differences plus common-depth repair

Status: `RESEARCH_NOTE / DURABLE FRONTIER / NONCANONICAL / NOT_FOUNDATION / NOT_WORKING_TRUTH`
Date: `2026-09-08`
Scope: `Enterprise Math / P000 X6 / one-step prime anisotropy`
Parent: `research_notes/x6_index_p_branch_smith_quadric_split_20260908.md`
EM source snapshot before write: `awdawmip/enterprise-math@d39b1e96ef01b851c1f9ae46eb58c0c036d65d9b`

## 0. Result

For every integer full-rank transport

`A in M_6(Z)`

with

`|det A|=3`,

define

`G=A^T A`

and

`Delta_6(A)=6 tr(G^2)-tr(G)^2`.

Then

`boxed: Delta_6(A) >= 32`.

The bound is sharp.

One exact minimizer is

`A=B_3 direct_sum I_3`,

where

`B_3=[[1,0,1],[-1,1,1],[0,-1,1]]`.

Its three nontrivial columns are

`e_1-e_2`,

`e_2-e_3`,

`(1,1,1)`.

Thus the first Gaussian-inert prime does not realize its optimum by a pair-conformal block. Its exact minimum is realized by a three-axis object consisting of two A2-type differences plus the common-depth direction.

This is an exact theorem under the declared X6 integer-coordinate/quadratic-readout model. It does not promote this particular minimizer to a unique physical primitive.

## 1. Exact defect decomposition

Write

`d_i=g_ii`

and

`M=sum_(i<j) g_ij^2`.

Since G is an integral positive-definite Gram matrix,

`d_i in Z_(>0)`

and

`M in Z_(>=0)`.

Expanding gives

`Delta_6`

`= sum_(i<j)(d_i-d_j)^2 + 12 sum_(i<j) g_ij^2`.

Set

`D=sum_(i<j)(d_i-d_j)^2`.

Hence

`Delta_6=D+12M`.

Also

`det G=(det A)^2=9`.

## 2. Lower bound: M=0

If `M=0`, G is diagonal and its positive integer diagonal entries have product 9.

Up to permutation the only factorizations are

`(9,1,1,1,1,1)`

or

`(3,3,1,1,1,1)`.

The smaller diagonal defect is attained by the second pattern:

`D=32`.

Therefore no diagonal Gram matrix has `Delta_6<32`.

## 3. Lower bound: M=1

If `M=1`, exactly one off-diagonal entry is `+/-1`; all others vanish.

After permutation,

`G=[[a,epsilon],[epsilon,b]] direct_sum diag(c_1,c_2,c_3,c_4)`,

with `epsilon=+/-1`.

Thus

`(ab-1) product_r c_r = 9`.

The positive divisor `ab-1` is one of `1,3,9`.

### 3.1 Block determinant 1

Then `ab=2`, so `{a,b}={1,2}` and the remaining four positive integers have product 9.

The most balanced possibility is `(1,1,3,3)`. Its diagonal multiset is

`(1,2,1,1,3,3)`

and already

`D=29`.

Hence

`Delta_6>=29+12=41`.

All other product-9 distributions are less balanced and have larger D.

### 3.2 Block determinant 3

Then `ab=4`. The minimum diagonal spread occurs at

`a=b=2`,

while the four singleton diagonals have product 3 and therefore are

`(3,1,1,1)`.

This gives

`D=20`

and

`Delta_6=20+12=32`.

The alternative factor pair `{1,4}` gives a larger defect.

### 3.3 Block determinant 9

Then `ab=10`, while all four singleton diagonals equal 1. The closest factor pair is `{2,5}`, which already gives a diagonal defect greater than 32 before the off-diagonal contribution is added.

Therefore the M=1 sector has minimum exactly 32.

## 4. Lower bound: M=2

If `Delta_6<32` and `M=2`, then necessarily

`D<8`.

For six positive integers, a pairwise square-difference total below 8 forces their multiset to be either

- all equal (`D=0`), or
- five equal to `a` and one equal to `a+1`, or conversely (`D=5`).

The two unit off-diagonal entries form either two disjoint graph edges or a length-two path.

### 4.1 All diagonals equal

If every diagonal equals a, the two-edge determinant is:

- disjoint edges: `a^2(a^2-1)^2`;
- a three-vertex path: `a^4(a^2-2)`.

For `a=1` the matrix is not positive definite in the relevant edge component; for `a>=2` the determinant is at least 32. It cannot equal 9.

### 4.2 Five a and one a+1, with a>=2

All diagonal entries are at least 2. For either two-edge graph type, increasing a positive diagonal entry of a positive-definite matrix strictly increases the determinant because the corresponding principal cofactor is positive.

The all-2 comparison matrices already have determinant 36 (two disjoint edges) or 32 (a path). Therefore determinant 9 is impossible.

### 4.3 The only low-diagonal boundary cases

For diagonals `(2,1,1,1,1,1)`, positive definiteness forbids a unit off-diagonal edge between two diagonal-1 vertices. Both edges would therefore have to pass through the unique diagonal-2 vertex, but the resulting `3x3` block has determinant 0.

For diagonals `(2,2,2,2,2,1)`, direct two-edge component determinants give only

`8,12,16,18`

depending on whether the diagonal-1 vertex is isolated, an endpoint, or belongs to a disjoint edge. None equals 9.

Thus no `M=2` positive-definite integral Gram matrix of determinant 9 has `Delta_6<32`.

## 5. M>=3

If `M>=3`, then

`Delta_6=D+12M >=36`.

Combining all cases proves

`boxed: Delta_6(A)>=32 for |det A|=3`.

## 6. Sharp explicit construction

Take

`B_3 = [[1,0,1],[-1,1,1],[0,-1,1]]`.

Its determinant is

`det B_3=3`.

Its Gram matrix is

`B_3^T B_3 = [[2,-1,0],[-1,2,0],[0,0,3]]`.

Hence for

`A=B_3 direct_sum I_3`,

we have

`|det A|=3`

and full Gram

`G = [[2,-1,0],[-1,2,0],[0,0,3]] direct_sum I_3`.

The diagonal multiset is

`(2,2,3,1,1,1)`

and there is one unit off-diagonal entry, so

`D=20`, `M=1`.

Therefore

`Delta_6=20+12=32`.

The lower bound is sharp.

## 7. The minimizer is A2 differences plus common depth

The three nontrivial columns are exactly

`c_1=e_1-e_2`,

`c_2=e_2-e_3`,

`c_3=(1,1,1)`.

The first two span the standard A2 difference plane inside the selected three-axis coordinate block. The third is the common-depth direction of that triple.

They satisfy

`c_1 dot c_2=-1`,

`c_1 dot c_3=0`,

`c_2 dot c_3=0`.

So the common-depth repair is orthogonal at the declared quadratic observer to the two relative difference directions.

The image of `B_3` is precisely

`{x in Z^3 : x_1+x_2+x_3 ==0 (mod 3)}`.

Thus the determinant-3 minimum is carried by the triple-sum index-3 relation rather than a two-axis Gaussian norm block.

This is a direct bridge to the already-admitted X6 distinction between relative coordinates and common-depth repair. It does not identify the three-axis block with a new primitive spatial direction.

## 8. Branch/Smith type

Modulo 3, the projective branch normal is

`v=(1,1,1,0,0,0)`.

It is isotropic for the six-square form because

`q(v)=1+1+1=0 (mod 3)`.

Therefore the exact branch-Smith theorem from the parent note gives

`SNF(G)=(1,1,1,1,3,3)`.

This is the two-p metric Smith stratum, as expected for a minimum that spreads rather than concentrates the p-adic defect.

## 9. Same singular spectrum, different integer geometry

The nontrivial `3x3` Gram block has eigenvalues

`3,3,1`.

Therefore the full X6 singular values of the minimizer are

`sqrt(3), sqrt(3), 1,1,1,1`.

This is exactly the singular-value pattern one would obtain from a hypothetical pair-conformal determinant-3 event with Gram

`diag(3,3,1,1,1,1)`.

But such an integral pair-conformal realization does not exist because 3 is not a sum of two squares; equivalently `3==3 (mod4)` is Gaussian-inert.

So:

`boxed: SAME SINGULAR SPECTRUM != SAME INTEGER GEOMETRY}`.

The one-step scalar anisotropy and singular values do not encode the eigenlattice orientation/projective branch needed for later arithmetic closure.

This is a direct BRC information-loss witness:

- the spectrum correctly reads the amount of anisotropy;
- it erases the arithmetic orientation that distinguishes a Gaussian pair plane from the A2/common-depth triple block;
- that erased orientation is precisely material to the known p^3 versus p^6 closure-period distinction.

Therefore future prime multiplication must retain at least branch/eigenlattice/transport data beyond the singular spectrum.

## 10. Equality candidates and integral realizability

At scalar Gram level, several determinant-9 positive-definite integral matrices can have `Delta_6=32`. Not all are Gram matrices of index-3 sublattices of the standard X6 lattice.

For example the diagonal candidate

`diag(3,3,1,1,1,1)`

would require, after four unit columns consume four coordinate axes, two orthogonal integer vectors of squared norm 3 in the remaining `Z^2`; this is impossible because 3 is not a sum of two squares.

Another scalar candidate contains two orthogonal `A2` Gram blocks

`[[2,1],[1,2]] direct_sum [[2,1],[1,2]] direct_sum I_2`.

After the two unit columns are removed, an integral realization would require two mutually orthogonal A2 pairs in `Z^4`. Put the first pair by signed coordinate symmetry into

`u=e_1+e_2`, `v=e_2+e_3`.

A norm-squared-2 integer vector w orthogonal to both would satisfy

`w_1+w_2=0`, `w_2+w_3=0`.

If any of `w_1,w_2,w_3` is nonzero, all three are nonzero and `||w||^2>=3`; if all vanish, only the fourth coordinate remains and norm squared 2 is impossible. Hence no such second A2 pair exists.

The realized sharp type is therefore the mixed

`A2 difference block + common-depth norm-3 direction + three unit axes`

exhibited above.

No full classification of all integral A representatives modulo left/right signed symmetries is claimed here.

## 11. Comparison with p=2

The p=2 minimum has

`Delta_6,min(2)=8`

and a pair-supported Hadamard/conformal event with singular values

`sqrt(2),sqrt(2),1,1,1,1`.

The p=3 minimum has

`Delta_6,min(3)=32`

and the same two-loaded-singular-value pattern with p substituted:

`sqrt(3),sqrt(3),1,1,1,1`,

but its exact integer realization requires a three-axis A2/common-depth block.

Thus the scalar spectrum does not by itself predict the global closure exponent:

- p=2 closes isotropically after three minimal pair events at index 8;
- p=3 has no `3^3` strict closure and first strict closure is `3^6`.

The repair state that distinguishes these futures is arithmetic/geometric orientation, not only spectral magnitude.

## 12. Consequence for natural-number representation

This strengthens the developing typed model:

`INTEGER n = EXACT COUNT/INDEX + FORCED SCALE n^(1/6) + GEOMETRIC FIBER + REPAIR STATE`.

For prime 3, the exact one-step optimum already requires a joint relation involving three native coordinates and the common-depth coordinate. A unique radial scale or singular-value list cannot reconstruct that relation.

Therefore even before composite multiplication is considered, a prime itself may carry indispensable relational geometry beyond its scalar magnitude.

## 13. BRC / observer audit

`T0_BRC`: `REUSE_APPLIED`.

Retain the branch normal, integral columns and common-depth provenance rather than only the final singular spectrum.

`T6_OPERATION_SAFE_QUOTIENT`: `REUSE_APPLIED`.

The projection

`A -> singular values -> Delta_6`

is explicitly certified unsafe for future prime-closure questions by the p=3 witness.

`T7_FINITE_SYMMETRY_EQUIVARIANCE`: `REUSE_APPLIED`.

The displayed triple is one representative; axis permutations produce equivalent support triples. No canonical triple is selected globally.

`T8_RELATION_OBSERVABLE_SPECTRUM`: `COMPOSE_APPLIED`.

The triple-sum branch is retained as a relation object distinct from its spectrum.

No new tool family is proposed.

## 14. Status ledger

Exact proved in this note:

- `min_{|det A|=3} Delta_6(A)=32`;
- explicit determinant-3 minimizer `B_3 direct_sum I_3`;
- its branch is the triple-sum relation `x_1+x_2+x_3=0 mod3`;
- its branch normal is isotropic and Gram Smith type is `(1^4,3,3)`;
- its singular values are `sqrt3,sqrt3,1,1,1,1`;
- the optimal integer geometry uses A2 differences plus common-depth repair;
- singular spectrum/Delta does not preserve the integer geometry needed to distinguish p=3 from a hypothetical Gaussian pair event.

Not promoted / still open:

- uniqueness of the minimizer orbit under the full admissible integer symmetry action;
- a general formula for `delta_min(p)`;
- whether all odd primes admit a two-loaded singular spectrum at the exact one-step minimum;
- whether the optimal support size is governed by representation of p by native lower-rank norm forms;
- the p=5 exact minimizer and whether Gaussian pair support is globally optimal there.

## 15. Next exact target

The next smallest unit is p=5.

Because 5 is Gaussian-split, the pair block

`[[1,-2],[2,1]]`

already gives an index-5 candidate with Gram

`diag(5,5,1,1,1,1)`.

Its defect is

`Delta_6=8(5-1)^2=128`.

The next question is not whether p=5 has a pair-conformal candidate—it does—but whether some higher-support integer branch has `Delta_6<128`.

A proof either way will decide whether one-step minimum anisotropy and strict p^3 closure use the same geometric branch family for the first Gaussian-split odd prime.
