# X6 determinant-11 exact minimum: the low-defect window empties before the first full-rank phase-paired lift

Status: `RESEARCH_NOTE / DURABLE FRONTIER / NONCANONICAL / NOT_FOUNDATION / NOT_WORKING_TRUTH`
Date: `2026-09-08`
Scope: `Enterprise Math / P000 X6 / one-step prime anisotropy / discriminant phase pairing`
Parents:
- `research_notes/x6_p7_exact_minimum_discriminant_obstruction_20260908.md`
- `research_notes/x6_prime_discriminant_pairing_gluing_principle_20260908.md`
Exact finite certificate:
- `research_notes/certificates/x6_p11_sparse_gram_exact_certificate_20260908.py@ae401a4d8dca4c176cea091be8eefd6bf05c4bef`
EM source snapshot before theorem write: `awdawmip/enterprise-math@ae401a4d8dca4c176cea091be8eefd6bf05c4bef`

## 0. Theorem

For every integer full-rank transport

`A in M_6(Z)`

with

`|det A|=11`,

let

`G=A^T A`

and

`Delta_6(A)=6 tr(G^2)-tr(G)^2`.

Then

`boxed: Delta_6(A)>=68`.

The bound is sharp.

Unlike p=7, no lower scalar Gram candidate needs a discriminant-form obstruction: the entire exact integral Gram window below 68 is already empty at determinant

`det G=11^2=121`.

An explicit determinant-11 transport reaches 68.

Therefore

`boxed: min_{|det A|=11} Delta_6(A)=68`.

## 1. The low-Delta window is prime-independent

The decomposition

`Delta_6=D+12M`

with

`D=sum_(i<j)(g_ii-g_jj)^2`,

`M=sum_(i<j)g_ij^2`

is independent of the target determinant.

If

`Delta_6<68`,

then exactly as in the p=7 theorem:

- `M<=5`;
- all off-diagonal entries lie in `{0,+/-1,+/-2}` with at most one absolute-2 entry;
- the diagonal range is at most 4;
- if every diagonal is at least 3, the exact admissible-E scan gives `det(3I+E)>=216` and diagonal monotonicity pushes every larger diagonal matrix still higher.

Since

`121<216`,

a determinant-121 candidate below the bound must again have minimum diagonal 1 or 2.

Thus the p=7 exact sparse window can be reused unchanged.

## 2. Exact integer certificate

The companion certificate composes the p=7 finite-enumeration primitives and checks the same

`1,150,826`

symmetric integer matrices in the analytically reduced window.

It uses exact fraction-free Bareiss determinants and finds

`boxed: zero determinant-121 matrices with Delta_6<68`.

This is stronger than a failure to find an X6 lift: there is no abstract symmetric integral Gram candidate at all below the bound.

Hence every determinant-11 integer transport satisfies

`Delta_6>=68`.

## 3. Exact equality construction

Take

`A_11=`

`[[-1,-1, 0, 0, 0, 1],`

` [ 1, 0, 0,-1, 0, 1],`

` [ 0, 1, 0, 0, 0, 1],`

` [ 0, 0,-1, 0, 1, 0],`

` [ 0, 0, 1, 1, 1, 0],`

` [ 0, 0, 1,-1, 0,-1]]`.

Then

`|det A_11|=11`.

Its Gram matrix is

`G_11=`

`[[2,1,0,-1,0,0],`

` [1,2,0,0,0,0],`

` [0,0,3,0,0,-1],`

` [-1,0,0,3,1,0],`

` [0,0,0,1,2,0],`

` [0,0,-1,0,0,4]]`.

The diagonal multiset is

`(2,2,3,3,2,4)`.

There are four unit off-diagonal entries, so

`D=20`, `M=4`.

Therefore

`Delta_6=20+48=68`.

The lower bound is attained.

## 4. Equality construction splits into determinant-11 blocks of ranks 4 and 2

The support graph of G11 has two connected components.

After a coordinate permutation,

`G_11 = H_{11,4} direct_sum K_{11,2}`,

where

`H_{11,4}=`

`[[2,-1,0,1],`

` [-1,3,1,0],`

` [0,1,2,0],`

` [1,0,0,2]]`,

and

`K_{11,2}=[[3,-1],[-1,4]]`.

Both have determinant 11.

Thus the displayed equality geometry uses all six coordinates nontrivially and is a full-rank pairing of two determinant-11 discriminant blocks.

No theorem is claimed that every p=11 minimizer has full active support; this statement concerns the explicit equality representative.

## 5. Complementary discriminant phases

For the binary block,

`adj(K_{11,2})=[[4,1],[1,3]]`.

A discriminant generator has coefficient

`4`,

a quadratic residue modulo 11.

For the rank-4 block,

`adj(H_{11,4})`

has a diagonal coefficient

`10=-1 (mod11)`,

which is a nonresidue because `11==3 mod4`.

The gluing equation can therefore be written

`10 x^2+4 y^2=0 (mod11)`,

or

`-x^2+4y^2=0`.

It has nonzero solutions

`x=+/-2y`.

So the equality construction again uses **opposite discriminant phases** rather than same-phase self-gluing.

The local phase law survives after the active rank reaches all six coordinate directions.

## 6. First five prime minima and the displayed repair-rank ladder

We now have exact one-step minima for

`p=2,3,5,7,11`:

| p | exact `delta_min(p)` | displayed determinant-p block ranks | strict closure exponent |
| ---: | ---: | --- | ---: |
| 2 | 8 | `1+1` | 3 |
| 3 | 32 | `2+1` | 6 |
| 5 | 48 | `2+2` | 3 |
| 7 | 68 | `3+2` | 6 |
| 11 | 68 | `4+2` | 6 |

The total nontrivial ranks of the displayed minimizers are therefore

`2,3,4,5,6`.

This is an exact observation about the exhibited equality constructions, but **not yet** a theorem that the minimum possible support rank follows this ladder or that it continues for larger primes.

The fact that p=11 reaches the full six-axis budget makes the next prime qualitatively different: no larger support rank is available. Any further improvement must come from changing form shape/phase inside full X6 rather than activating a new spatial coordinate.

## 7. p=7 and p=11 share the same minimum for different reasons

Both have

`delta_min=68`,

but the lower-bound mechanisms differ.

### p=7

An abstract scalar Gram with defect 56 exists, but its same-phase discriminant form cannot lift to an index-7 X6 sublattice. The arithmetic repair coordinate raises the admissible minimum to 68.

### p=11

No integral Gram matrix of determinant 121 exists anywhere in the scalar window below 68. No later discriminant obstruction is needed.

Thus equality of the final scalar minima does not imply equality of the obstruction mechanism.

Again:

`SAME FINAL DELTA != SAME NATIVE CAUSE`.

## 8. Binary quadratic-form connection inside the p=11 equality state

The rank-2 block

`K_{11,2}=[[3,-1],[-1,4]]`

corresponds to the positive binary quadratic form

`3x^2-2xy+4y^2`

with classical discriminant

`(-2)^2-4*3*4=-44=-4*11`.

More generally, every determinant-p symmetric binary Gram

`[[a,b],[b,c]]`

corresponds to

`a x^2+2bxy+c y^2`

of discriminant

`-4p`.

Therefore the binary block layer of the prime-geometry problem naturally sits inside the classical class/genus theory of positive binary quadratic forms of discriminant `-4p`.

The discriminant-phase square class used in the gluing law is the p-primary finite-lattice datum that survives into this representation.

This observation does not by itself solve the higher-rank minimization, but it identifies a mature arithmetic classification surface for the rank-2 part of the proposed block-pair variational calculus.

## 9. Consequence for the natural-number geometry program

The first five primes now show that a prime's geometric fiber cannot be summarized by any one of:

- scalar radius `p^(1/6)`;
- local anisotropy minimum `delta_min(p)`;
- strict closure exponent `tau_X6(p)`;
- support rank;
- discriminant phase;
- binary split/inert status.

Each is an observer of a richer integral relation/transport carrier.

The most stable emerging representation is

`PRIME p -> FAMILY OF INTEGRAL METRIC BLOCKS + DISCRIMINANT PHASE + GLUE RELATION + X6 EMBEDDING + FUTURE CLOSURE STATE`.

This is exactly the kind of typed geometric fiber anticipated by the original “2 does not land on one natural point” intuition.

## 10. Tool / method audit

`T0_BRC`: `REUSE_APPLIED` — p=7 and p=11 retain different obstruction provenance despite the same scalar minimum.

`T6_OPERATION_SAFE_QUOTIENT`: `REUSE_APPLIED` — Delta alone is again insufficient for mechanism classification and future closure.

`T9_HOLONOMY_COCOYCLE_GLUING`: `COMPOSE_APPLIED` — complementary discriminant phases provide the exact finite gluing law.

The companion certificate composes the p=7 result-specific finite-enumeration code; it is `RESULT_ONLY`, not a new global tool family.

## 11. Status ledger

Exact proved:

- `min_{|det A|=11} Delta_6(A)=68`;
- no abstract integral Gram determinant121 has `Delta_6<68`;
- explicit equality matrix A11;
- equality Gram decomposes into determinant-11 rank4 and rank2 blocks with complementary discriminant phases;
- the displayed equality construction activates all six coordinates;
- the rank2 block is a positive binary quadratic form of discriminant `-44`.

Still open:

- equality-orbit classification at p=11;
- whether the displayed 2,3,4,5,6 active-rank ladder is intrinsic or representative-dependent;
- a block-pair variational theorem reproducing all five prime minima without sparse prime-specific enumeration;
- p=13 exact minimum, now in a full-rank-saturated regime;
- whether class/genus data of discriminant `-4p` predict when a low-cost binary block can participate in the global minimizer.

## 12. Next frontier

The next structurally meaningful step is **not** simply to repeat the p=11 sparse certificate at p=13.

Construct the block-pair variational layer explicitly:

1. rank-1 determinant-p blocks;
2. reduced binary determinant-p forms / discriminant `-4p` classes;
3. low-trace ternary/quaternary determinant-p forms only when needed;
4. discriminant phase square class;
5. exact X6 Delta cost after padding;
6. compatibility/gluing constraint;
7. compare its predicted envelope against known exact minima p=2,3,5,7,11.

If that envelope matches all five, then p=13 becomes a real falsification test of a general law rather than another isolated computation.
