# X6 determinant-13 exact minimum: full-rank ternary self-gluing after the six-axis budget saturates

Status: `RESEARCH_NOTE / DURABLE FRONTIER / NONCANONICAL / NOT_FOUNDATION / NOT_WORKING_TRUTH`
Date: `2026-09-08`
Scope: `Enterprise Math / P000 X6 / one-step prime anisotropy / post-saturation regime`
Parents:
- `research_notes/x6_p11_exact_minimum_full_rank_phase_pairing_20260908.md`
- `research_notes/x6_prime_discriminant_pairing_gluing_principle_20260908.md`
Exact finite certificate:
- `research_notes/certificates/x6_p13_sparse_gram_exact_certificate_20260908.py@836ae34e628f36073e7269f40c2a7b02fd2aa2ae`
EM source snapshot before theorem write: `awdawmip/enterprise-math@836ae34e628f36073e7269f40c2a7b02fd2aa2ae`

## 0. Theorem

For every integer full-rank transport

`A in M_6(Z)`

with

`|det A|=13`,

let

`G=A^T A`

and

`Delta_6(A)=6 tr(G^2)-tr(G)^2`.

Then

`boxed: Delta_6(A)>=56`.

The bound is sharp.

Therefore

`boxed: min_{|det A|=13} Delta_6(A)=56`.

This is the first prime after the displayed p=2,3,5,7,11 support-rank ladder has reached all six axes. The minimum does not increase. Instead the full-rank geometry reorganizes into two identical determinant-13 ternary blocks and the defect drops from the p=7,p=11 value 68 to 56.

Thus prime size is not a monotone proxy for one-step geometric anisotropy.

## 1. Exact lower-bound window

Suppose

`Delta_6<56`.

Writing

`Delta_6=D+12M`,

we have

`M<=4`.

Every off-diagonal entry is therefore in `{0,+/-1,+/-2}`, with at most one absolute-2 entry.

As in the p=7,p=11 certificates, the diagonal range is at most 4.

If every diagonal is at least 3, write

`G=3I+E+R`

with R diagonal nonnegative. The p=7 exact base certificate already verifies

`det(3I+E)>=216`

for the larger family `M<=5`, hence in particular for `M<=4`.

Since

`13^2=169<216`,

a determinant-169 Gram below 56 must have minimum diagonal 1 or 2.

The resulting finite window is strictly smaller than the p=7/p=11 window.

## 2. Exact certificate

The p=13 companion certificate reuses the exact Bareiss enumeration primitives and checks

`215,558`

symmetric integer matrices in the analytically reduced `Delta_6<56` window.

It finds

`boxed: zero determinant-169 matrices with Delta_6<56`.

Therefore every determinant-13 X6 integer transport has

`Delta_6>=56`.

No discriminant-form exclusion is needed below the bound because the scalar Gram window itself is empty.

## 3. Exact equality construction

Take

`A_13=`

`[[1,0,0,0,-1,-1],`

` [0,1,1,-1,0,0],`

` [1,0,0,0,1,0],`

` [0,1,-1,0,0,0],`

` [0,0,1,1,0,1],`

` [0,0,0,1,1,-1]]`.

Then

`|det A_13|=13`.

Its Gram matrix is

`G_13=`

`[[2,0,0,0,0,-1],`

` [0,2,0,-1,0,0],`

` [0,0,3,0,0,1],`

` [0,-1,0,3,1,0],`

` [0,0,0,1,3,0],`

` [-1,0,1,0,0,3]]`.

The diagonal multiset is

`(2,2,3,3,3,3)`

and there are four unit off-diagonal entries. Hence

`D=8`, `M=4`,

so

`Delta_6=8+48=56`.

The lower bound is attained.

## 4. Equality geometry is H13 direct-sum H13

The support graph has two disconnected three-vertex paths. After coordinate/sign switches each component has Gram

`H_13=[[2,-1,0],[-1,3,-1],[0,-1,3]]`.

Its determinant is

`det H_13=13`.

Therefore

`G_13 ~= H_13 direct_sum H_13`

under signed coordinate permutation.

The characteristic polynomial of each ternary block is

`lambda^3-8 lambda^2+19 lambda-13`.

The full six-dimensional equality state is thus a doubled ternary metric shape rather than a pair-plane Gaussian similarity.

## 5. Discriminant phase and why self-gluing is allowed

The adjugate is

`adj(H_13)=[[8,3,1],[3,6,2],[1,2,5]]`.

Every displayed diagonal generator coefficient `8,6,5` is a quadratic nonresidue modulo 13, so the determinant-13 discriminant phase is the nonsquare class.

Two identical H13 blocks require a nonzero solution of

`a x^2+a y^2=0 (mod13)`,

equivalently

`x^2+y^2=0 (mod13)`.

Because

`13==1 (mod4)`,

`-1` is a square modulo 13; for example `5^2=25=-1 (mod13)`.

Hence the two same-phase ternary blocks possess an order-13 isotropic glue and can combine into an integral unimodular overlattice. The explicit A13 realizes that gluing inside the standard X6 lattice.

This is the same abstract self-gluing character as p=5, but acting on rank-3 rather than rank-2 determinant-p blocks.

## 6. The first six prime minima

The exact one-step minima now read

| p | exact `delta_min(p)` | displayed determinant-p block ranks | strict closure exponent |
| ---: | ---: | --- | ---: |
| 2 | 8 | `1+1` | 3 |
| 3 | 32 | `2+1` | 6 |
| 5 | 48 | `2+2` | 3 |
| 7 | 68 | `3+2` | 6 |
| 11 | 68 | `4+2` | 6 |
| 13 | 56 | `3+3` | 3 |

The sequence

`8,32,48,68,68,56`

is already enough to rule out a naive monotone “larger prime -> larger one-step anisotropy” model.

The block-rank organization is also not monotone after the six-axis budget saturates: p=13 reorganizes the full rank as `3+3` rather than extending the previous `4+2` pattern.

## 7. Saturation boundary

The sparse-window proof used a prime-independent fact:

for `Delta_6<68`, if every diagonal is at least 3, then

`det G>=216`.

This handles p=7 and p=11 because

`7^2=49<216`,

`11^2=121<216`.

The stronger p=13 bound 56 still lies in the same diagonal-reduction regime because

`13^2=169<216`.

But the next prime satisfies

`17^2=289>216`.

Therefore p=17 is a genuine method boundary: a low-defect determinant-289 Gram may live entirely in the diagonal-at-least-3 region, so the previous exact sparse-window reduction is no longer sufficient.

This is a structural reason to stop prime-by-prime reuse of the old certificate and build a more general variational method.

## 8. Binary/ternary quadratic-form interpretation

The determinant-p block-pair picture now contains both classical binary and ternary positive integral forms.

For a binary block

`[[a,b],[b,c]]`

the associated quadratic form has discriminant

`-4p`.

The p=13 equality instead uses ternary determinant-13 forms. Thus the correct classification surface cannot be only the binary class group of discriminant `-4p`; it must allow a rank-varying family of positive determinant-p lattices with discriminant phase.

This motivates a rank-graded block library:

`rank -> metric cost -> determinant p -> discriminant phase -> gluing compatibility`.

The one-step X6 minimum is then a constrained gluing problem under total rank at most 6.

## 9. Consequence for the original natural-number question

The developing geometry has moved far beyond assigning a radius to n.

For p=13:

- arithmetic identity remains exactly 13;
- determinant-forced mean linear scale is `13^(1/6)`;
- local minimum geometry is a doubled ternary discriminant-13 relation;
- strict closure exponent is still 3 because `13==1 mod4`;
- the local minimum is not a Gaussian pair representation despite the same split character.

So even within one congruence class, the prime's geometric fiber reorganizes substantially.

This reinforces the typed thesis:

`NATURAL NUMBER != UNIQUE POINT`,

`PRIME GEOMETRY = ARITHMETIC IDENTITY + MULTIPLE OBSERVER-DEPENDENT RELATIONS + REPAIR/GLUE STATE`.

## 10. Tool / method audit

`T0_BRC`: `REUSE_APPLIED` — local block shape, discriminant phase, gluing and strict-closure character remain separate typed coordinates.

`T6_OPERATION_SAFE_QUOTIENT`: `REUSE_APPLIED` — no scalar observer is promoted to the full prime state.

`T9_HOLONOMY_COCOYCLE_GLUING`: `COMPOSE_APPLIED` — self-gluing of the two ternary phases is exact.

The p=13 certificate composes the existing exact sparse-Gram enumeration primitives and remains `RESULT_ONLY`.

## 11. Status ledger

Exact proved:

- `min_{|det A|=13} Delta_6(A)=56`;
- exact no-candidate certificate below 56;
- explicit determinant-13 equality matrix;
- equality Gram is two identical determinant-13 ternary blocks;
- the blocks carry the same nonsquare discriminant phase and self-glue because `-1` is a square mod13;
- p=13 marks the last prime for which `p^2<216`, after which the old low-window proof mechanism no longer automatically applies.

Still open:

- equality-orbit classification at p=13;
- a general determinant-p block variational theorem;
- whether the exact minimum is always achieved by a two-block determinant-p decomposition;
- how the rank-graded determinant-p forms relate to classical genus/spinor-genus data;
- p=17 behavior in the new high-diagonal regime.

## 12. Next frontier

Freeze the next task as:

**Determinant-p block-pair variational calculus before p=17.**

For each rank `r=1,2,3,4,5` as needed:

1. classify or bound positive integral Gram forms `H` with `det H=p`;
2. retain `(tr H, tr H^2, discriminant phase, rank)`;
3. for compatible pairs `(H,K)` with total rank `<=6`, compute the exact padded X6 cost

`Delta_X6(H,K)=6[tr(H^2)+tr(K^2)+6-r-s]`

`-[tr H+tr K+6-r-s]^2`;

4. require exact discriminant-phase gluing compatibility;
5. compare the lower envelope to the six proved primes;
6. only then use p=17 as a falsification test.

This is now the smallest route likely to turn the prime atlas into a reusable law rather than a list of exceptional matrices.
