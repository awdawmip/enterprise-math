# X6 determinant-19 exact minimum: the same-phase false optimum returns at p=19

Status: `RESEARCH_NOTE / DURABLE FRONTIER / NONCANONICAL / NOT_FOUNDATION / NOT_WORKING_TRUTH`
Date: `2026-09-08`
Scope: `Enterprise Math / P000 X6 / one-step prime anisotropy / discriminant gluing`
Parents:
- `research_notes/x6_p17_exact_minimum_new_diagonal_layer_20260908.md`
- `research_notes/x6_p7_exact_minimum_discriminant_obstruction_20260908.md`
- `research_notes/x6_prime_discriminant_pairing_gluing_principle_20260908.md`
Exact finite certificate:
- `research_notes/certificates/x6_p19_sparse_gram_exact_certificate_20260908.cpp@77c68325d2154a1e8fb0c47d40c63bfeb0e567ad`
EM source snapshot before theorem write: `awdawmip/enterprise-math@77c68325d2154a1e8fb0c47d40c63bfeb0e567ad`

## 0. Theorem

For every integer full-rank transport

`A in M_6(Z)`

with

`|det A|=19`,

let

`G=A^T A`

and

`Delta_6(A)=6 tr(G^2)-tr(G)^2`.

Then

`boxed: Delta_6(A)>=77`.

The bound is sharp. Therefore

`boxed: min_{|det A|=19} Delta_6(A)=77`.

The proof repeats the p=7 phenomenon at a higher diagonal layer: a scalar integral Gram type with lower defect 72 exists, but it consists of two identical determinant-19 discriminant phases and cannot lift to an index-19 sublattice of the standard X6 lattice.

This repetition turns discriminant phase from an isolated explanatory device into a recurring exact admissibility obstruction.

## 1. Low-defect forcing

Write

`Delta_6=D+12M`,

where

`D=sum_(i<j)(g_ii-g_jj)^2`,

`M=sum_(i<j)g_ij^2`.

Assume

`Delta_6<77`.

Then

`M<=6`.

The diagonal range is at most 4: the least possible D for six integer diagonals containing values separated by 5 is exactly 77.

If every diagonal is at least 5, write

`G=5I+E+R`,

with E zero-diagonal and R diagonal nonnegative.

The defect bound gives `tr(E^2)=2M<=12`. If E had a negative eigenvalue `-r`, trace zero and Cauchy on the other five eigenvalues give

`12 >= tr(E^2) >= r^2+r^2/5 = 6r^2/5`,

so `r^2<=10`. Hence `5I+E` is positive definite.

The exact certificate enumerates every allowed E and finds

`min det(5I+E)=10800`.

Since

`10800>19^2=361`,

no determinant-361 candidate below the bound can have minimum diagonal at least 5.

Thus the complete scalar search reduces to minimum diagonal `1,2,3,4`, range at most4, and `M<=6`.

## 2. Exact finite scalar-Gram certificate

The result-specific exact C++ certificate uses fraction-free Bareiss determinants and no floating point.

It checks exactly

`5,926,168`

symmetric integer matrices in the analytically reduced window.

Exactly

`64`

have determinant 361 below the proposed bound.

Every one of those 64 candidates has

`Delta_6=72`

and, up to coordinate permutation and tree-sign switches, the same type

`G_false = H_19 direct_sum H_19`,

with

`H_19=[[2,0,-1],[0,3,-1],[-1,-1,4]]`,

`det H_19=19`.

The sorted full diagonal is `(2,2,3,3,4,4)`, there are four unit off-diagonal edges, and the support graph is two disconnected three-vertex paths, each having endpoint diagonals 2 and3 and center diagonal4.

Thus the entire abstract scalar window below77 collapses to one tempting false optimum.

## 3. The Delta=72 false optimum has the wrong glue phase

The adjugate of H19 is

`adj(H_19)=[[11,1,3],[1,7,2],[3,2,6]]`.

The displayed diagonal discriminant coefficients 11,7,6 are all quadratic residues modulo19, so H19 carries the square discriminant phase.

Two copies of the same phase can admit an order-19 isotropic glue only if

`x^2+y^2=0 (mod19)`

has a nonzero solution.

But

`19==3 (mod4)`,

so `-1` is not a quadratic residue modulo19.

Therefore

`H_19 direct_sum H_19`

has no order-19 isotropic subgroup in its discriminant group and no integral unimodular overlattice of index19.

If it were `A^T A` for an integer matrix A of determinant19, the standard lattice `Z^6` would give exactly such an overlattice. Contradiction.

Hence every abstract Gram candidate below77 is nonliftable to the actual X6 transport carrier.

## 4. Exact equality construction

Take

`A_19=`

`[[ 1,-1,-1, 0, 0, 1],`

` [ 1, 0, 0, 0, 1,-1],`

` [ 1, 1, 0, 0,-1, 0],`

` [ 0,-1, 1,-1, 0, 0],`

` [ 0, 0,-1,-1,-1,-1],`

` [ 0, 0, 0,-1, 0, 1]]`.

Then exactly

`det A_19=19`.

Its Gram matrix is

`G_19=`

`[[3,0,-1,0,0,0],`

` [0,3,0,1,-1,-1],`

` [-1,0,3,0,1,0],`

` [0,1,0,3,1,0],`

` [0,-1,1,1,3,0],`

` [0,-1,0,0,0,4]]`.

Its diagonal multiset is `(3,3,3,3,3,4)` and it has six unit off-diagonal entries, so

`D=5`, `M=6`.

Therefore

`Delta_6=5+72=77`.

The lower bound is attained.

## 5. p=7 and p=19 exhibit the same exact obstruction schema

The two primes share a structural pattern:

### p=7

- abstract low scalar candidate: `H7 direct_sum H7`;
- defect 56;
- same discriminant phase;
- self-glue requires `x^2+y^2=0 mod7`;
- impossible because `chi_-4(7)=-1`;
- true X6 minimum rises to68.

### p=19

- abstract low scalar candidate: `H19 direct_sum H19`;
- defect72;
- same discriminant phase;
- self-glue requires `x^2+y^2=0 mod19`;
- impossible because `chi_-4(19)=-1`;
- true X6 minimum rises to77.

Thus the mod-4 character enters one-step optimization not by determining the scalar Gram cost itself, but by deciding whether a same-phase paired scalar optimum is an admissible native X6 state.

This is a different typed role from the earlier strict-isotropy closure exponent `tau_X6(p)`, even though the same character appears.

## 6. Exact prime-minimum atlas through p=19

The current exact atlas is

| p | `delta_min(p)` | strict closure exponent |
| ---: | ---: | ---: |
| 2 | 8 | 3 |
| 3 | 32 | 6 |
| 5 | 48 | 3 |
| 7 | 68 | 6 |
| 11 | 68 | 6 |
| 13 | 56 | 3 |
| 17 | 72 | 3 |
| 19 | 77 | 6 |

So

`delta_min = 8,32,48,68,68,56,72,77`

on the first eight primes.

The one-step sequence remains nonmonotone and is not determined by the strict-closure character alone.

## 7. Stronger BRC/admissibility principle

The p=19 theorem reinforces the hierarchy

`ABSTRACT INTEGRAL GRAM`

`-> DISCRIMINANT FORM + GLUE POSSIBILITY`

`-> ACTUAL INDEX-p X6 TRANSPORT`.

A scalar Gram can satisfy every local metric desideratum and still fail the native lift because its discriminant phases cannot cancel.

Therefore the discriminant form is not optional metadata. It is an **admissibility coordinate**.

The following compressions are globally unsafe for prime multiplication research:

- determinant only;
- singular spectrum only;
- scalar Delta only;
- abstract Gram without ambient-lift data.

## 8. Consequence for the general variational program

The exact p=19 scalar false optimum is itself a pair of low-rank determinant-p blocks. This supports a block-form lower-envelope viewpoint, but the p=17 equality Gram warned that the actual admissible minimizer need not visibly split in the coordinate basis.

A general theory should therefore optimize over **integral lattice genera/classes and overlattice gluings**, with direct-sum block pairs as a tractable chart, rather than assuming every minimizer is literally block diagonal.

The relevant state should retain at least

`(rank, determinant, trace, trace-square, discriminant form, ambient embedding/glue class)`.

## 9. Tool / method audit

`T0_BRC`: `REUSE_APPLIED` — scalar false optimum and native admissible optimum are kept distinct.

`T6_OPERATION_SAFE_QUOTIENT`: `REUSE_APPLIED` — full abstract Gram still does not descend safely to native feasibility without discriminant/overlattice state.

`T9_HOLONOMY_COCOYCLE_GLUING`: `COMPOSE_APPLIED` — same-phase discriminant obstruction supplies the exact lift failure.

The C++ finite certificate is `RESULT_ONLY`.

## 10. Status ledger

Exact proved:

- `min_{|det A|=19} Delta_6(A)=77`;
- exact low-window enumeration of 5,926,168 scalar candidates;
- exactly64 determinant361 candidates below77, all one H19+H19 type at Delta72;
- H19 phase is square and same-phase self-gluing is impossible modulo19;
- explicit determinant19 equality transport at Delta77;
- the p=7 same-phase false-optimum obstruction recurs at p=19.

Still open:

- equality-orbit classification at p=19;
- a theorem predicting when the scalar optimum is same-phase doubled and therefore killed by `chi_-4=-1`;
- a general genus/class variational law recovering the exact atlas without prime-specific sparse scans;
- the next split/inert primes as independent falsification tests only after such a law is formulated.

## 11. Next frontier

Stop blind enumeration here unless needed to falsify a proposed law.

The next research object should be a **prime X6 lattice energy with gluing admissibility**:

1. minimize `Delta_6` over determinant-p integral lattices/Gram classes;
2. retain their discriminant forms;
3. impose existence of an index-p embedding into the standard unimodular X6 lattice;
4. separate current metric minimum from future strict-closure optimization;
5. derive congruence/genus/spinor-genus signatures visible in the eight-prime exact atlas.

This is now a genuine generalization problem rather than a lack of examples.
