# X6 index-p branch Smith split and finite-quadric observer

Status: `RESEARCH_NOTE / DURABLE FRONTIER / NONCANONICAL / NOT_FOUNDATION / NOT_WORKING_TRUTH`
Date: `2026-09-08`
Scope: `Enterprise Math / P000 X6 / prime index geometry`
Parent: `research_notes/x6_prime_similarity_closure_gaussian_eisenstein_characters_20260908.md`
EM source snapshot before write: `awdawmip/enterprise-math@3e95d66f171d4ec6ffbb6e37ed956a40eafc573e`

## 0. Purpose

The previous note classified the first **global strict-isotropy closure power** of a prime, but it deliberately left the harder one-step problem

`min_{|det A|=p} Delta_6(A)`

open.

This note derives an exact branch-level structural split that does not require solving that optimization.

Every index-p sublattice branch of `Z^6` has a projective normal

`[v] in P^5(F_p)`.

The value

`q(v)=v_1^2+...+v_6^2 (mod p)`

separates two exact p-adic metric types:

- anisotropic normal `q(v)!=0`: the p^2 metric defect is concentrated in one Smith direction;
- isotropic normal `q(v)=0`: the p^2 metric defect splits into two p-valued Smith directions.

This gives a canonical first stratification of the one-step index-p search space before any Euclidean/Enterprise anisotropy minimization is attempted.

## 1. Index-p branch normal

Let

`A in M_6(Z)`, `|det A|=p`

with p prime.

Modulo p, A has rank 5. Its column image

`W=im(A mod p)`

is therefore a hyperplane in `F_p^6`.

Choose a nonzero projective normal v such that

`W=v^perp={x:v dot x=0}`.

The projective class `[v]` is exactly the index-p sublattice branch in

`P^5(F_p)`.

Scaling v by a nonzero scalar changes q(v) by a square, so the condition

`q(v)=0`

is projectively well-defined.

## 2. Gram rank modulo p

Let

`G=A^T A`.

For x in `F_p^6`,

`Gx=0`

iff

`Ay dot Ax=0`

for every y, i.e. iff

`Ax in W intersect W^perp`.

Because `W=v^perp`,

`W^perp=span(v)`.

There are two cases.

### Case A: q(v)!=0

Then v is not in v^perp, so

`W intersect W^perp=0`.

Therefore

`ker(G mod p)=ker(A mod p)`

has dimension 1, and

`rank_Fp(G mod p)=5`.

### Case B: q(v)=0

Then v lies in v^perp, so

`W intersect W^perp=span(v)`

has dimension 1.

The preimage of this one-dimensional radical under A adds one dimension beyond `ker A`, hence

`dim ker(G mod p)=2`,

`rank_Fp(G mod p)=4`.

Thus:

`boxed: q(v)!=0 <=> rank(G mod p)=5`,

`boxed: q(v)=0 <=> rank(G mod p)=4`.

## 3. Exact Smith-type dichotomy for the Gram matrix

Since

`det G=(det A)^2=p^2`,

all nontrivial Smith invariant factors of G are powers of p whose exponents sum to 2.

The number of invariant factors divisible by p equals the nullity of `G mod p`.

Therefore:

### Anisotropic-normal branch

Nullity 1 forces

`SNF(G)=(1,1,1,1,1,p^2)`.

### Isotropic-normal branch

Nullity 2 forces

`SNF(G)=(1,1,1,1,p,p)`.

Hence the branch quadric condition has a direct p-adic metric meaning:

`q(v)!=0 -> ONE p^2 METRIC DIRECTION`,

`q(v)=0 -> TWO p METRIC DIRECTIONS`.

This is basis-invariant Smith data, unlike a chosen diagonalization or scalar anisotropy observer.

## 4. Relation to the binary minimum-defect theorem

For p=2,

`q(v)=sum_i v_i^2=sum_i v_i (mod 2)`.

So nonzero isotropic projective normals are exactly the even-Hamming-weight vectors:

- weight 2: 15 branches;
- weight 4: 15 branches;
- weight 6: 1 branch.

Total isotropic index-2 branches:

`31`.

The previous exact minimization selected only the 15 weight-2 branches as `Delta_6=8` minimizers.

Therefore:

`ISOTROPIC PROJECTIVE NORMAL != GLOBAL MINIMUM Delta_6`.

The quadric/Smith split is a necessary structural stratification, not a complete optimization result.

This is an important anti-overclaim boundary for general p.

## 5. Odd-prime count of isotropic projective branches

For odd p, the standard six-square form has the exact zero count

`N0 = p^5 + (p-1) chi_-4(p) p^2`,

where `chi_-4(p)` is the quadratic character of -1.

This is the standard even-dimensional finite-field quadratic-form count, obtainable by a one-line quadratic Gauss-sum evaluation.

Removing the zero vector and quotienting by the `p-1` nonzero scalars gives the number of isotropic projective branches:

`I_6(p)=(N0-1)/(p-1)`

`      =(p^5-1)/(p-1)+chi_-4(p)p^2`

`      =p^4+p^3+(1+chi_-4(p))p^2+p+1`.

Therefore:

### Gaussian-split prime p==1 mod4

`I_6(p)=p^4+p^3+2p^2+p+1`

`      =(p^2+1)(p^2+p+1)`.

### Gaussian-inert prime p==3 mod4

`I_6(p)=p^4+p^3+p+1`

`      =(p+1)(p^3+1)`.

The full index-p branch count remains

`P_6(p)=|P^5(F_p)|=p^5+p^4+p^3+p^2+p+1`.

Thus the isotropic-normal fraction is asymptotically of order `1/p`.

## 6. The same character controls two different exact phenomena

The previous note proved that for odd p:

`chi_-4(p)=+1`

iff strict global p^3 similarity closure exists.

The present note shows that the same character also changes the exact cardinality of the local isotropic branch quadric by

`2 p^2`

between the split and inert cases.

But the two statements are not equivalent:

- even an inert prime has many isotropic one-step branch normals;
- what it lacks is a three-dimensional totally isotropic subspace large enough to support `A^T A=pI_6`.

So the hierarchy is:

`ISOTROPIC VECTOR EXISTS` — true for all odd p in six dimensions;

`MAXIMAL 3D TOTALLY ISOTROPIC SUBSPACE EXISTS` — iff `chi_-4(p)=+1`;

`STRICT p^3 X6 SIMILARITY EXISTS` — iff `chi_-4(p)=+1`.

This distinguishes local p-adic branch balancing from global similarity closure.

## 7. Pair-conformal split-prime branches are a tiny subrelation

For odd `p==1 mod4`, the preceding Gaussian-pair note exhibited

`30`

pair-supported exact conformal branches: 15 support pairs times the two roots of `-1` modulo p.

These lie inside the much larger isotropic projective quadric of size

`I_6(p)=p^4+p^3+2p^2+p+1`.

For example p=5 gives

`I_6(5)=806`,

while only 30 are pair-supported Gaussian branches.

Therefore the p^3 Gaussian closure mechanism is a highly structured low-dimensional subrelation of the full isotropic branch population.

One-step `Delta_6` minimizers for p>2 must not be assumed to lie in that 30-branch subrelation without a separate proof.

## 8. New BRC carrier hierarchy for one prime event

For an index-p event retain separately:

1. arithmetic prime p;
2. full projective branch `[v] in P^5(F_p)`;
3. quadric bit `q(v)=0` or not;
4. Gram Smith type `(1^4,p,p)` or `(1^5,p^2)`;
5. actual integral transport A;
6. Gram G;
7. scalar anisotropy `Delta_6`;
8. when available, Gaussian pair-support/phase data;
9. future closure schedule provenance.

The implications are one-way unless separately proved:

`PAIR-CONFORMAL -> q(v)=0 -> TWO-p SMITH TYPE`.

Neither converse is automatic.

This is exactly the sort of observer/provenance distinction required by the Joint Relation Observer Preservation contract.

## 9. Consequence for the one-step minimization program

The hard optimization

`min_{|det A|=p} Delta_6(A)`

should now be stratified, not attacked as one undifferentiated search.

Compute separately:

`delta_iso(p)=min Delta_6(A) over q(v)=0 branches`,

`delta_aniso(p)=min Delta_6(A) over q(v)!=0 branches`.

Then

`delta_min(p)=min(delta_iso(p),delta_aniso(p))`.

This preserves the exact p-adic branch type and allows a genuine theorem to state whether minimum real/component anisotropy prefers the two-p Smith distribution.

For p=2 the exact answer is known:

`delta_min(2)=8`

and minimizers lie in the isotropic-normal stratum, but not every isotropic branch minimizes.

For odd p no general inequality `delta_iso(p)<delta_aniso(p)` is claimed yet.

## 10. Connection to finite quadratic geometry

The isotropic branch locus is a projective quadric in `P^5(F_p)`.

Its type changes with `chi_-4(p)`:

- split/hyperbolic type when `p==1 mod4`;
- nonsplit/elliptic type when `p==3 mod4`.

This gives a finite-geometric carrier for the same arithmetic character already seen in strict closure period.

The project should therefore treat `P^5(F_p)` not as a flat list of `1+p+...+p^5` branches but as a typed branch space containing an intrinsic quadric and its complement.

This may be more useful for bounded branch selectors than raw enumeration.

## 11. Status ledger

Exact proved under the declared model:

- every index-p branch is a projective hyperplane normal `[v]`;
- `q(v)=0` iff `rank(G mod p)=4`, otherwise rank 5;
- isotropic normal iff `SNF(G)=(1^4,p,p)`;
- anisotropic normal iff `SNF(G)=(1^5,p^2)`;
- for p=2 there are 31 isotropic branches, of which the 15 weight-2 branches are the known minimum-Delta orbit;
- for odd p the isotropic branch count is `p^4+p^3+(1+chi_-4(p))p^2+p+1`;
- the split/inert branch-count difference is exactly `2p^2`;
- pair-supported Gaussian branches are a strict subrelation of the isotropic quadric for odd split p.

Still open:

- prove whether one-step `Delta_6` minimizers always lie on the isotropic quadric;
- exact `delta_iso(p)` and `delta_aniso(p)`;
- S6-orbit refinement inside the quadric, which is much finer than the p=2 Hamming-weight classification;
- a bounded selector preserving enough quadric/phase data for repeated multiplication.

## 12. Smallest next unit

The next high-value theorem target is:

> Find a branch-type lower bound for `Delta_6` in terms of the Smith/quadric stratum, strong enough either to prove `delta_iso(p)<delta_aniso(p)` for an infinite prime class or produce an explicit counterexample.

A finite exact search for p=3,5,7 should be used only as a conjecture generator unless accompanied by a complete bound/certificate.
