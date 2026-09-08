# X6 determinant-5 exact minimum: golden-ratio discriminant gluing beats the Gaussian pair

Status: `RESEARCH_NOTE / DURABLE FRONTIER / NONCANONICAL / NOT_FOUNDATION / NOT_WORKING_TRUTH`
Date: `2026-09-08`
Scope: `Enterprise Math / P000 X6 / one-step prime anisotropy / natural-number geometry`
Parents:
- `research_notes/x6_p3_exact_minimum_a2_common_depth_20260908.md`
- `research_notes/x6_prime_similarity_closure_gaussian_eisenstein_characters_20260908.md`
- `research_notes/x6_index_p_branch_smith_quadric_split_20260908.md`
EM source snapshot before write: `awdawmip/enterprise-math@d8ccb5ad6c774e1ac36406260973c9a29fe58f44`

## 0. Result and the conceptual reversal

For every integer full-rank transport

`A in M_6(Z)`

with

`|det A|=5`,

let

`G=A^T A`

and

`Delta_6(A)=6 tr(G^2)-tr(G)^2`.

Then

`boxed: Delta_6(A)>=48`.

The bound is sharp.

This immediately overturns the most obvious one-step candidate. Because `5=1^2+2^2`, a Gaussian pair block gives an exact determinant-5 conformal two-axis event with Gram spectrum

`(5,5,1,1,1,1)`

and defect

`128`.

But the true one-step minimum is only

`48`.

Therefore for the first odd Gaussian-split prime:

`ONE-STEP MINIMUM ANISOTROPY != SHORTEST EXACT p^3 CLOSURE BRANCH FAMILY`.

The branch that is locally roundest is not the Gaussian branch that makes the three-event global closure simplest.

This is an exact theorem under the declared X6 integer-coordinate/quadratic-readout model. It is not a claim that `Delta_6` is the unique physical cost.

## 1. Defect decomposition

As in the p=3 theorem, write

`d_i=g_ii`,

`D=sum_(i<j)(d_i-d_j)^2`,

`M=sum_(i<j)g_ij^2`.

Then

`Delta_6=D+12M`.

Since

`det G=(det A)^2=25`,

we need an integral positive-definite Gram determinant 25.

To prove `Delta_6>=48`, suppose for contradiction that

`Delta_6<48`.

Then

`M<=3`.

Moreover every nonzero off-diagonal entry is necessarily `+/-1`; an entry of absolute value at least 2 would contribute at least `12*4=48` by itself.

Thus the lower-bound problem reduces to integral diagonal data plus a graph with at most three unit off-diagonal edges.

## 2. Case M=0

Then G is diagonal and its positive integer diagonal entries have product 25.

The most balanced nontrivial factorization is

`(5,5,1,1,1,1)`.

Its diagonal defect is

`D=8(5-1)^2=128`.

Hence no diagonal Gram has defect below 48.

## 3. Case M=1

After permutation,

`G=[[a,epsilon],[epsilon,b]] direct_sum diag(c_1,c_2,c_3,c_4)`,

with `epsilon=+/-1`, so

`(ab-1) product c_i=25`.

The positive divisor

`x=ab-1`

is one of `1,5,25`.

For each x, the exact most-balanced diagonal choice is finite:

| `x` | best `(a,b;c_1,c_2,c_3,c_4)` up to permutation | minimum D |
| --- | --- | ---: |
| 1 | `(1,2;1,1,5,5)` | 117 |
| 5 | `(2,3;1,1,1,5)` | 77 |
| 25 | `(2,13;1,1,1,1)` | 701 |

All have

`D+12>48`.

So `M=1` cannot beat 48.

## 4. Case M=2: two disjoint edges

If the two unit off-diagonal entries are disjoint, after permutation

`det G=(ab-1)(cd-1)ef=25`.

Let

`x=ab-1`, `y=cd-1`.

The only positive divisor patterns have x,y in `{1,5,25}` with `xy|25`.

Exact balancing gives the following minimum diagonal defects:

| `(x,y)` up to order | minimizing diagonal type | minimum D |
| --- | --- | ---: |
| `(1,1)` | `(1,2;1,2;5,5)` | 104 |
| `(1,5)` | `(1,2;2,3;1,5)` | 68 |
| `(1,25)` | `(1,2;2,13;1,1)` | 680 |
| `(5,5)` | `(2,3;2,3;1,1)` | 24 |

Thus the exact minimum in the disjoint-edge sector is

`D=24`, `M=2`,

which gives

`Delta_6=24+24=48`.

This is already the prospective equality type.

## 5. Case M=2: a length-two path

If the two unit off-diagonals share a vertex, the nontrivial 3x3 block has determinant

`T=abc-a-c`.

Hence

`T d e f=25`

and `T` is one of `1,5,25`.

Solving these finite divisor equations and minimizing D gives:

| T | one minimizing diagonal type | minimum D |
| --- | --- | ---: |
| 1 | `(2,1,3;1,5,5)` | 101 |
| 5 | `(1,3,3;1,1,5)` | 80 |
| 25 | `(2,5,3;1,1,1)` | 77 |

All are far above the `D<24` required for `Delta_6<48` with `M=2`.

Therefore the only scalar equality candidate in the M=2 sector is the two-disjoint-edge type from Section 4.

## 6. Case M=3: exact sparse-graph exclusion

If `M=3` and `Delta_6<48`, then

`D<12`.

For six positive integer diagonals this forces all diagonals to take only two consecutive values:

`a` and `a+1`,

with

`D=k(6-k)`

when exactly k coordinates take the higher value. Thus `D` can only be `0,5,8,9` below 12.

The three unit off-diagonal entries form one of the five unlabeled three-edge graph types:

1. three disjoint edges;
2. a two-edge path plus one disjoint edge;
3. a four-vertex path;
4. a three-leaf star;
5. a triangle.

Their component determinants are obtained from the exact formulas

`edge(x,y)=xy-1`,

`P3(x,y,z)=xyz-x-z`,

`P4(x,y,z,w)=xyzw-xy-xw-zw+1`,

`star(y;x,z,w)=xyzw-xz-xw-zw`,

`triangle(x,y,z)=xyz-x-y-z+2 epsilon`,

where `epsilon=+/-1` is the cycle-sign product.

The remaining vertices contribute singleton diagonal factors.

### 6.1 Minimum diagonal a>=3

For a positive-definite matrix, determinant is strictly increasing in any diagonal entry because the corresponding principal cofactor is positive.

So it is enough to put all diagonals equal to 3. Across the five graph types the smallest determinant is the negative-cycle triangle case:

`16 * 3^3 = 432`.

Hence determinant 25 is impossible for all `a>=3`.

### 6.2 a=2

The finite component formulas give:

- k=0: possible positive-definite determinants `{16,20,24,27,32}`;
- k=1: `{24,30,32,36,40,42,44,45,48,56}`;
- k>=2: determinant at least 36.

None equals 25.

### 6.3 a=1

The same exact formulas give:

- k=0 or 1: no positive-definite three-edge matrix;
- k=2: determinant set `{1}`;
- k=3: `{1,2,4}`;
- k=4: `{2,3,4,5,8}`;
- k=5: `{4,6,8,9,10,12,16}`;
- k=6: `{16,20,24,27,32}`.

Again 25 never occurs.

Thus no M=3 integral positive-definite Gram matrix of determinant 25 can satisfy `Delta_6<48`.

## 7. M>=4

If `M>=4`, then

`Delta_6=D+12M>=48`.

Combining Sections 2–7 proves

`boxed: Delta_6(A)>=48 for |det A|=5`.

## 8. Exact equality construction

Define

`C_5 =`

`[[-1, 0,-1, 1],`

` [ 1, 0,-1, 0],`

` [ 0,-1, 1, 1],`

` [ 0, 1, 0, 1]]`.

Then

`det C_5=5`.

Its Gram matrix is

`C_5^T C_5 =`

`[[2, 0, 0,-1],`

` [0, 2,-1, 0],`

` [0,-1, 3, 0],`

` [-1,0, 0, 3]]`.

After a column permutation this is

`K_5 direct_sum K_5`,

where

`K_5=[[2,-1],[-1,3]]`

has determinant 5.

Set

`A=C_5 direct_sum I_2`.

Then

`|det A|=5`.

The full Gram diagonal multiset is

`(2,2,3,3,1,1)`

and there are exactly two unit off-diagonal entries. Hence

`D=24`, `M=2`,

so

`Delta_6=24+24=48`.

The lower bound is attained.

## 9. Exact golden-ratio singular spectrum

The eigenvalues of

`K_5=[[2,-1],[-1,3]]`

are the roots of

`lambda^2-5 lambda+5=0`,

namely

`lambda_+=(5+sqrt(5))/2`,

`lambda_-=(5-sqrt(5))/2`.

Each occurs twice in the four-dimensional active block; two further eigenvalues are 1.

Their ratio is

`lambda_+/lambda_-=(3+sqrt(5))/2=phi^2`,

where

`phi=(1+sqrt(5))/2`.

Therefore the ratio of the two active singular scales is exactly

`boxed: sigma_+/sigma_-=phi`.

So the true determinant-5 minimum carries a repeated golden-ratio anisotropy rather than a conformal pair-plane scale.

This is an exact spectral fact, not an aesthetic choice.

## 10. Branch normal and p-adic type

Modulo 5, the active four-dimensional image has projective normal

`v=(1,1,2,2)`.

In full X6 take

`v=(1,1,2,2,0,0)`.

Then

`q(v)=1+1+4+4=10=0 (mod5)`.

Thus the minimizer lies on the isotropic projective quadric, and the branch/Smith theorem gives

`SNF(G)=(1,1,1,1,5,5)`.

So p=5, like p=3, minimizes in the two-p Smith stratum rather than the concentrated p^2 stratum.

This is evidence for, but not yet a proof of, the conjecture that one-step minimum anisotropy favors isotropic-normal branches for all primes.

## 11. Discriminant-5 gluing rather than a coordinate Gaussian plane

Each rank-2 Gram block K5 has determinant 5. Such a block cannot by itself be the Gram of a full-rank index-integer map `Z^2->Z^2`, because that would require an integer determinant whose square is 5.

But two copies have determinant

`5*5=25`,

and their direct sum is integrally realizable as the index-5 four-dimensional block C5.

Thus the p=5 minimum uses a genuine **discriminant gluing** phenomenon:

`TWO NON-INTEGRAL-AS-STANDALONE DISC-5 METRIC PLANES`

`-> ONE INTEGRAL INDEX-5 RANK-4 TRANSPORT`.

This mechanism is different from the Gaussian pair plane even though 5 is a sum of two squares.

The arithmetic branch is therefore not determined by the existence of a lower-rank exact norm representation alone.

## 12. Local optimum versus global closure

For p=5 there are now two exact but different geometric roles.

### Local one-step optimum

The C5 construction has

`Delta_6=48`

and golden-ratio active singular ratio phi.

### Shortest exact strict-isotropy closure

Because `5=1^2+2^2`, a Gaussian pair block

`B_5=[[1,-2],[2,1]]`

satisfies

`B_5^T B_5=5 I_2`.

Three disjoint pair blocks close at index

`5^3`

to

`5 I_6`.

But one such event has defect

`8(5-1)^2=128`.

Therefore:

`boxed: LOCALLY ROUNDEST BRANCH != FASTEST EXACT-CLOSURE BRANCH}`.

The natural-number geometry must distinguish a local cost observer from a future-operation/closure observer. Selecting one branch only because it minimizes the current scalar defect is not operation-safe for multiplication.

This is a direct application of the T6/BRC rule that current-readout optimality does not imply future-operation equivalence.

## 13. Comparison p=2,3,5

The first three prime cases now have exact one-step minima:

| p | `delta_min(p)` | one exact minimizing geometry | strict closure exponent |
| ---: | ---: | --- | ---: |
| 2 | 8 | rank-2 Hadamard/conformal pair | 3 |
| 3 | 32 | rank-3 A2 differences + common depth | 6 |
| 5 | 48 | rank-4 double discriminant-5 gluing | 3 |

No simple monotone formula in p is yet claimed.

More importantly, the support/repair rank changes:

`2 -> 2-axis`,

`3 -> 3-axis`,

`5 -> 4-axis`

for the displayed exact minimizers.

This is a strong hint that prime geometry may be controlled by the smallest rank in which an adequately balanced discriminant-p metric object embeds integrally, rather than by one universal pair-plane template.

That conjecture is open.

## 14. BRC / observer-safety audit

`T0_BRC`: `REUSE_APPLIED`.

The local minimizer branch and the Gaussian closure branch are retained as different provenance objects even though both represent arithmetic p=5.

`T6_OPERATION_SAFE_QUOTIENT`: `REUSE_APPLIED`.

The map

`branch -> current scalar Delta_6`

is not safe for future strict-isotropy closure optimization: the local minimum loses to the higher-current-cost Gaussian branch on closure horizon.

`T7_FINITE_SYMMETRY_EQUIVARIANCE`: `REUSE_APPLIED`.

The displayed C5 block is one representative. No unique support/orientation is declared canonical under S6.

`T8_RELATION_OBSERVABLE_SPECTRUM`: `COMPOSE_APPLIED`.

Arithmetic 5 carries multiple useful geometric subrelations depending on the observer/future operation.

No new top-level tool family is proposed.

## 15. Status ledger

Exact proved here:

- `min_{|det A|=5} Delta_6(A)=48`;
- explicit rank-4 equality construction C5;
- equality Gram has two discriminant-5 blocks `K5` plus two unit directions;
- active singular-value ratio is exactly the golden ratio;
- the minimizer lies on the isotropic branch quadric with Smith type `(1^4,5,5)`;
- the Gaussian pair candidate has defect 128 and is therefore not one-step optimal;
- local minimum anisotropy and shortest strict p^3 closure choose different p=5 branch families.

Still open:

- full minimizer orbit classification for p=5;
- a uniform theorem that minimizers lie on the isotropic projective quadric;
- exact p=7 minimum and whether its optimal support/repair rank continues the 2,3,4 pattern;
- an invariant predicting minimal repair rank from p without exhaustive Gram classification;
- whether the golden-ratio p=5 spectrum has a reusable cross-project role beyond this exact lattice optimization.

## 16. Next exact target

The next prime is p=7.

Because 7 is Gaussian-inert, strict isotropy first closes at `7^6`, but the p=3 case already showed that inertness does not force a high one-step scalar defect.

The next test is to determine

`delta_min(7)`

and the minimal support/repair rank of its exact minimizer.

The main structural question is now:

> Does the sequence of minimum one-step prime geometries reveal a rank/discriminant ladder independent of the separate strict-closure character `chi_-4`?
