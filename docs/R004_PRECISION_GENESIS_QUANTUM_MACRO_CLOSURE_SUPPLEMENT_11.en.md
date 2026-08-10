# R004 precision genesis — Supplement 11: fraction-free linear-lift compiler and the A3 exterior bridge

Status: `PROVED_WIP + EXECUTABLE_CHECKED + A3_BRIDGE + PRIOR_ART_SPECIALIZATION`  
Parent: `R004_PRECISION_GENESIS_QUANTUM_MACRO_CLOSURE_SUPPLEMENT_10.en.md`  
Owner branch: `research/r004-precision-genesis-closure-20260810`

Supplement 10 used an additive-congruence gate to convert some future kernels into quotient modules. That gate is intentionally strict. This supplement proves that failure of the modular congruence gate does **not** yet imply that a fully general relation/witness state is required.

A noncongruent finite partition can still be the restriction of an ordinary integer/rational linear quotient after lifting the finite carrier into `Z^d`. R004 now detects this case with fraction-free determinants.

## 1. Finite future partition in an integer lift

Let

`X subset Z^d`

be a finite declared carrier and let `E` be the future-safe partition induced by the declared future language.

Collect all differences of states that already lie in the same future class:

`D_E={x-y : x E y}`.

Let

`V_E=span_Q(D_E)`.

Every linear coordinate constant on each `E`-class must annihilate `V_E`.

The first compiler question is therefore not whether `E` is a congruence of the original finite modular carrier, but whether `E` is the restriction to `X` of cosets of the rational subspace `V_E`.

## 2. R004-COMP-T08 — linear-lift span criterion

The partition `E` is exactly the restriction of the coset relation modulo `V_E` if and only if no pair from different `E`-classes has difference in `V_E`:

`x not E y -> x-y notin V_E`.

The forward direction is immediate. Conversely, all same-class differences lie in `V_E` by construction, while the displayed condition excludes every inter-class difference. Hence

`x E y iff x-y in V_E`

on the finite carrier `X`.

This is a finite linear-algebra criterion, not a new abstract quotient theorem.

The branch tests membership using only exact integer rank: `v in V_E` iff appending `v` does not increase the integer matrix rank over `Q`.

## 3. Fraction-free determinant token for arbitrary codimension

Let the rank of `V_E` be `k<d` and choose any `k` independent integer intra-class differences as rows of a matrix `B`.

For every `(k+1)`-element column subset `J`, define

`Phi_B(x)_J = det([B_J ; x_J])`.

All coordinates are integers. Determinants are computed by Bareiss-style fraction-free elimination in the executable layer.

Because determinant is linear in the final row,

`Phi_B(x)-Phi_B(y)=Phi_B(x-y)`.

All `(k+1)x(k+1)` minors vanish exactly when appending `x-y` does not increase the row rank of `B`. Therefore

`Phi_B(x)=Phi_B(y)`

if and only if

`x-y in span_Q(B)=V_E`.

Combining this with R004-COMP-T08 gives:

`E = ker(Phi_B)|_X`.

Thus every finite future partition passing the linear-lift span gate receives a completely integer determinant relation token without rational nullspace coordinates.

The specific determinant tuple depends on the chosen integer basis of `V_E`, but its equality kernel on `X` does not. R004 treats the kernel/future partition as the semantic object and the determinant tuple as one exact coordinate representation.

Exterior powers, alternating maps, minors and determinants are established linear algebra. Mathlib has canonical exterior-algebra/exterior-power and determinant APIs; R004 does not claim these constructions as novel.

## 4. Codimension one: automatic scalar relation recovery

If

`rank(V_E)=d-1`,

the annihilator is one-dimensional. A primitive integer normal

`c_E in Z^d`

is unique up to sign.

Choose `d-1` independent intra-class differences. The signed cofactors of their `(d-1) x d` matrix give an integer normal; divide by the gcd of its coordinates and choose a fixed sign convention.

Then the partition is exactly the fibers of

`x -> c_E . x`

if and only if all inter-class differences have nonzero dot product with `c_E`.

This is the codimension-one specialization of the determinant compiler: there is only one `d x d` minor, and it is the scalar linear coordinate up to the fixed normalization.

## 5. The coupled-AND counterexample is simpler than a general witness state

Supplement 08 used the two-bit state `(Z/2)^2`, XOR dynamics and coupled observable

`O(x_1,x_2)=x_1 x_2`.

The diagonal action language

`{(0,0),(1,1)}`

has safe partition

`{{00},{01,10},{11}}`.

Its modular congruence gate fails, but the integer-lift compiler recovers the primitive normal

`(1,1)`.

Hence the safe classes are exactly the fibers of the ordinary integer total

`x_1+x_2`.

The cross action language

`{(0,1),(1,0)}`

has safe partition

`{{00,11},{01},{10}}`.

Again the modular congruence gate fails, but the integer-lift compiler recovers

`(1,-1)`.

Hence the safe classes are exactly the fibers of

`x_1-x_2`.

This corrects an earlier provisional interpretation: noncongruence on the modular carrier is not sufficient evidence that a general A4 witness state is required. An integer lift may expose a much smaller relation coordinate.

## 6. A3 weighted relation field is the rank-one determinant compiler

Now take the existing A3 capacity vector

`m=(m_i)`

and block-total state

`c=(c_i)`.

A3 defines

`Z_ij=m_j c_i-m_i c_j`.

Apply the determinant compiler with one intra-class/basis direction `m`. For a column pair `(i,j)`:

`D_ij(c)=det([[m_i,m_j],[c_i,c_j]])`

`=m_i c_j-m_j c_i`.

Therefore

`Z_ij=-D_ij`.

So the canonical A3 weighted relation field is exactly, up to sign convention, the **rank-one exterior/determinant token** for quotienting the total-state vector by common shifts along the capacity direction.

This is an exact reduction identity, not an analogy.

The existing A3 primitive field-preserving shift `m/gcd(m)` is precisely the primitive integer generator of this rank-one kernel. The existing A3 relation dimension `n-1` is exactly the codimension of a one-dimensional forgotten span in ambient dimension `n`.

## 7. A3 closure is the exterior integrability identity

A3 requires antisymmetry and the weighted closure law

`m_k Z_ij + m_i Z_jk + m_j Z_ki = 0`.

Substituting `Z_ij=m_jc_i-m_ic_j` makes every triple defect cancel identically.

In exterior language this is the coordinate form of

`m wedge (m wedge c)=0`.

Thus the A3 three-block closure is not an unrelated extra pattern: it is exactly the redundancy/integrability identity forced by a decomposable rank-one exterior relation field.

The branch adds an executable bridge that checks:

- A3 upper-triangular relation coordinates are the negatives of determinant-token coordinates;
- every weighted closure defect is zero;
- A3 relation dimension equals the rank-one quotient codimension;
- primitive capacity shifts preserve both the A3 field and the determinant token.

R004 does not modify A3 ownership or claim exterior algebra as new. The bridge is a cross-owner structural identification.

## 8. Validation

New executable assets:

- `precision_integer_linear_lift_compiler.py`;
- `precision_a3_exterior_bridge.py`;
- matching tests.

Independent verification additionally compared the fraction-free integer rank/determinant routines against exact SymPy rank/determinant on tens of thousands of random small integer matrices with no mismatch.

For **329** primitive linear forms across finite 2D/3D/4D boxes, whenever the induced same-class span had codimension one, the compiler recovered the correct primitive normal up to the fixed sign convention.

Committed regressions include:

- automatic recovery of `(1,1)` and `(1,-1)` for the coupled-AND partitions;
- a 3D codimension-one example with primitive normal `(1,-2,1)`;
- an arbitrary-codimension line quotient in `Z^3` compiled by determinant minors;
- fail-closed partitions whose intra-class span cannot separate inter-class states;
- direct A3 exterior identity and weighted closure checks.

No fresh full-repository CI or Lean status is claimed.

## 9. Revised fail-closed compiler ladder

The current compiler should now attempt structured representations in the following order when applicable:

1. direct p-adic translation trie on one axis;
2. product of axis compilers under full product observation;
3. proved modular linear relation factorization;
4. additive-congruence quotient module and invariant exponent profile;
5. **integer-lift rational-linear span gate and determinant relation token**;
6. rank-one positive-capacity specialization reduces exactly to A3 weighted relation field;
7. only after these gates fail should a genuinely more general A3/A4 relation/witness representation be required.

This ordering matters. It prevents the compiler from escalating to a richer state type merely because the original modular coordinates were the wrong carrier for a simple integer relation.

## 10. Next frontier

After this supplement, the next hard case is not every noncongruent partition. It is a future-safe partition that simultaneously fails:

- product factorization;
- additive congruence/module extraction;
- rational-linear lift/coset representation.

For such a partition, the project should ask whether A3's richer weighted relation structures, A4 finite witness/correspondence structures, or another verified bridge provide the weakest non-opaque state.

That frontier should be pursued under the actual A3/A4 owners. R004's role is now to supply the compiler gates, reduction identities, and counterexamples that show exactly when each simpler representation fails.
