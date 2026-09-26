# Fixed actual H4/sign/swap alphabet is dense on the retained real carrier

Status: ROOT-PROPOSED / SHARED AUTHOR SYMBOLIC CROSS-CHECK / UNREVIEWED / NOT ADMITTED.

Researcher: `EM-DIRECT-C6438C`; activity: `RA-CAAAC604CB513AEA8BBC1DFC`.
Registration Source: `f0e5fb6f478a5a380ab5a7533d2585f7f43ee3bf`.
Frozen actual primitive source: `0852cad130c1d877174d235687cf60c19f318c58`.

Root proposed the overlapping four-coordinate reflection construction. This note verifies the actual primitive identities, supplies a four-conjugate generator extraction, and proves the closure statement directly. It does not invoke an unverified universal quantum-gate theorem. No new ordinary reference propagation, trigonometric numerical evaluation, primitive-precision increase, or density benchmark was executed.

## 1. Statement and its implementation boundary

Let `D>=5`. On the real `D`-coordinate carrier, take the actual frozen native H4 on any selected four coordinates, together with native coordinate sign changes and swaps. Each is the identity on unselected coordinates. Let `G` be the group of their finite words and let `G_plus` be its determinant-positive subgroup.

**Theorem.** The operator-norm closure of `G_plus` is `SO(D)`. The closure of `G` is `O(D)`. In particular, this applies to the existing **61-dimensional** retained carrier, without adding coordinates or changing any primitive coefficient.

All actual finite words remain exactly dyadic and exactly orthogonal. Their length, and consequently their common denominator exponent and integer storage cost, may grow. No primitive uses a more accurate angle or replaces its existing coefficient by an adjustable one.

This is a density/existence theorem. It does not yet provide an implemented word compiler, a useful word-length bound, a completed full-column approximation certificate, or an executed all-input small-TV Shor simulator. Section 8 specifies the remaining effective obligations.

## 2. The primitive identity is available in the actual source

The frozen `stage78/shor_benchmark.py::native_quartet` obtains the exact signed columns from the equal C12 construction and verifies the Walsh sign table. `stage80/fixed_phase.py::primitives` reads those columns and also certifies native sign and swap operations, including their controlled direct sums. The actual H4 is

```text
H = (1/2) [ 1  1  1  1
            1 -1  1 -1
            1  1 -1 -1
            1 -1 -1  1 ].
```

The same file's `apply_word` applies this returned primitive to any named four distinct internal coordinates and leaves the others intact. Its `neg` and `swap` cases use the returned native sign and swap. These interfaces, rather than an independently entered desired matrix, are the source of the proposed word alphabet.

For a fixed `D`, even a smaller finite generating alphabet suffices: H4 on coordinates `1,2,3,4`, the adjacent coordinate swaps, and one single-coordinate sign change. Permutation conjugation supplies H4 on any four-coordinate set and sign changes at every coordinate. This gives `D+1` generator letters, all involutions; for `D=61`, it is a 62-letter fixed alphabet. Indexed H4/sign/swap operations are an equivalent convenient presentation.

There is no spectator reset or residual projection in this statement. The 61 coordinates are the existing internal logical/retained modes; their common metric normalization is inherited from the certified primitive interface.

## 3. The required four-coordinate reflection is an exact native word

Use local coordinate labels `1,2,3,4` and put

`w=(e1+e2+e3+e4)/2`, `H_w=I-2ww^T`.

On these four coordinates,

```text
H_w = (1/2) [ 1 -1 -1 -1
             -1  1 -1 -1
             -1 -1  1 -1
             -1 -1 -1  1 ].
```

Let `D4=diag(1,-1,-1,-1)` on the selected block and let `P23` swap its local coordinates two and three. Direct multiplication of the actual displayed Walsh sign table gives

`H_w = D4 P23 H D4`.

Thus one exact native realization, in execution order, is:

1. flip local coordinates two, three, and four;
2. apply the actual H4;
3. swap local coordinates two and three;
4. flip local coordinates two, three, and four again.

Every unselected coordinate is unchanged. This is a left/right signed-permutation transformation of H4, **not** a signed-permutation conjugation of H4. Indeed `H^2=I` and `trace(H)=0`, so H4 has two negative and two positive eigenvalues and determinant `+1`; `H_w` is a reflection and has determinant `-1`. Conjugacy would preserve these invariants and is impossible.

There is also a shorter-to-check two-H4 identity. Since `H e1=w`, `H^T=H`, and `H^2=I`,

`H_w = H diag(-1,1,1,1) H`.

It uses two actual H4 calls and one native sign change. Either identity gives an exact finite word; no claim of primitive-count optimality is needed.

For `D>=5`, put

`v=(e1+e2+e3+e5)/2`.

The coordinate swap `S45` sends `w` to `v`, so

`H_v=S45 H_w S45`.

Therefore both reflections, and their product, are actual finite words in the same fixed alphabet. In dimension 61 this construction initially acts on five coordinates and is the identity on the other 56.

## 4. Their product supplies an irrational planar rotation

Both vectors have unit norm and

`rho=w^T v=3/4`, `sigma=sqrt(1-rho^2)=sqrt(7)/4`.

The product `R=H_w H_v` has determinant `+1`, fixes `span(w,v)^perp`, and is a rotation on `span(w,v)`. In the orthonormal basis `w, (v-rho w)/sigma`, its two-dimensional matrix is

```text
[ 2rho^2-1    2rho sigma
 -2rho sigma  2rho^2-1 ].
```

Hence its angle magnitude `theta` satisfies

`cos(theta)=2rho^2-1=1/8`, `0<theta<pi`.

This angle is not a rational multiple of pi. Otherwise `zeta=exp(i theta)` would be a root of unity, so `zeta+zeta^(-1)=2cos(theta)=1/4` would be an algebraic integer. A rational algebraic integer is an integer: putting a reduced rational into a monic integral polynomial forces its denominator to divide its numerator. Since `1/4` is not an integer, this is a contradiction.

Thus the powers of `R` are dense in the entire circle of rotations on this plane. For completeness, an infinite subgroup of the circle has arbitrarily small nonzero angle increments by compactness/pigeonhole. Multiples of such an increment approach any prescribed angle to within that increment, so its closure is the entire circle. Irrationality makes the subgroup generated by `theta` infinite.

Define the real skew matrix

`A=w v^T-v w^T`.

On the same orthonormal plane its matrix is `[[0,sigma],[-sigma,0]]`, so `R=exp((theta/sigma) A)`. The circle-density result therefore implies

`exp(t A) in closure(G_plus)` for every real `t`.

The angle, square root, and exponential appear only in this proof of the closure. The implemented word `R` has the exact fixed dyadic coefficients obtained from its native factors; no irrational coefficient is passed to a primitive.

## 5. Four sign conjugates isolate one coordinate-plane generator

Let `Hplus=closure(G_plus)`. It is a closed subgroup of `SO(D)`. Conjugating it by any signed permutation in `G` preserves it, even when that signed permutation has determinant `-1`: conjugation preserves determinant, and it sends each actual determinant-positive word to another such word.

Consider the set

`L={X real skew: exp(tX) in Hplus for all real t}`.

It is closed under real scalar multiplication. It is also closed under addition, by the finite-matrix product formula

`exp(t(X+Y)) = lim_(n -> infinity) [exp(tX/n) exp(tY/n)]^n`.

A direct finite-dimensional justification is enough here: the one-step difference between `exp(tX/n)exp(tY/n)` and `exp(t(X+Y)/n)` is `O(n^-2)` by their convergent matrix power series. Their factors are orthogonal for real skew matrices, so the telescoped `n`-step norm difference is `O(n^-1)`. Each approximant lies in `Hplus`, and it is closed. Thus no unproved matrix-Lie subgroup theorem is required for this use of the product formula. The classical primary reference for its general operator extension is [Trotter, *On the product of semi-groups of operators* (1959)](https://doi.org/10.1090/S0002-9939-1959-0108732-6); the finite-matrix argument needed here has just been given explicitly.

Section 4 gives `A in L`. Conjugation therefore puts `S A S^(-1)` in `L` for every native signed permutation `S`.

Let `F4` and `F5` denote the single-coordinate sign changes at coordinates four and five. Write

`E_ij=e_i e_j^T-e_j e_i^T`.

The coefficient of `E_45` in `A` is `w_4 v_5-v_4 w_5=1/4`. The exact sign-character projection is

`E_45 = A - F4 A F4 - F5 A F5 + F4 F5 A F5 F4`.

To verify it, conjugation by `F4` multiplies a skew coefficient by minus one exactly when one of its indices is four; `F5` has the analogous action. The four-term combination kills every pair except `(4,5)`, whose coefficient is multiplied by four. This proves the displayed identity coefficient by coefficient. A full average over all `2^D` sign patterns is unnecessary.

All four terms and their negatives are in the real linear space `L`, so `E_45 in L`. Coordinate permutations then give

`E_ij in L` for every `i<j`.

These matrices form a basis of `so(D)`. Consequently every real skew matrix belongs to `L`, and in particular `Hplus` contains every coordinate-plane rotation `exp(t E_ij)`.

The linear combinations here are a proof about limits of products of exact words. They are not native gates that add generator matrices or take a physical weighted mixture. The finite words approximating the flows are formed by concatenation, inverse words, sign/permutation conjugation, and the product-formula construction only.

## 6. From coordinate rotations to SO(61), with determinant bookkeeping

Every matrix in `SO(D)` is a product of coordinate-plane rotations. One elementary proof is real Givens elimination: coordinate rotations successively remove the below-diagonal entries of its columns. An orthogonal triangular matrix is diagonal with entries `+1` or `-1`; determinant `+1` makes the number of minus signs even. Each pair of minus signs is a rotation by pi in that coordinate plane. Reversing the elimination gives the desired factorization.

Section 5 puts every such rotation, and therefore every such finite product, in `Hplus`. The reverse inclusion is already `Hplus subset SO(D)`. Hence

`closure(G_plus)=SO(D)`.

The full alphabet also contains a single-coordinate reflection, so its closure contains both `SO(D)` and the other component obtained by multiplying it by that reflection. Thus

`closure(G)=O(D)`.

The odd dimension `D=61` creates no determinant obstruction. Each `H_w` and `H_v` has determinant `-1` on the full carrier, their product has determinant `+1`, and all approximating rotation words can stay in `G_plus`. Conjugating these words by determinant-negative signed permutations still yields determinant-positive words. The argument does not silently replace a reflection by a rotation.

## 7. Why this does not inherit the fixed K33 obstruction

The fixed K33 obstruction relied on a **fixed finite family** of retained phase products. For high-odd work components, all members of that family were invertible in both branches, giving one positive width-independent minimum branch singular value. Its repeated strict contraction drove mass away from the ideal peak set.

The present alphabet is finite, but the permitted word family has unbounded length and is infinite. Density allows these words to approach target rotations arbitrarily closely. The finite-family positive minimum used for K33 need not remain bounded away from zero across longer and longer words. Thus the K33 proof does not exclude this new approximation policy.

For any one finite Shor width and any desired positive error allowance, density gives finite words approximating each required ideal principal-plane phase direct-sum the identity on all other 59 modes. With a suitable finite per-occurrence error allocation, the standard operator-norm telescoping argument would give the corresponding finite circuit error bound. This is an existence consequence; it is not an implemented, certified selection procedure or an efficiency bound.

The distinction is exact: primitive H4/sign/swap coefficients remain fixed; only word selection and length vary. Full-word matrix denominators and integer sizes can increase as ordinary consequences of composing fixed exact primitives. This does not retune the 32-bit target parameters or 64-bit unit-vector constants of an old gate.

## 8. What an effective compiler and strong-TV implementation still require

The next implementation needs concrete, replayable work beyond density:

1. **A target specification and error budget.** The desired phase is its exact algebraic/borrowed ideal definition, with a certificate capable of deciding a strict error bound. Merely reusing one unchanged 32-bit interval cannot by itself certify arbitrarily smaller errors once that interval's uncertainty dominates. Refining a target proof or using an exact algebraic comparison is a separate observer obligation; it must not be disguised as a more accurate primitive or as a new untracked numerical reference.
2. **A terminating word-selection procedure.** Density proves some word exists. An exhaustive enumeration could become a computable baseline if a sound target-error verifier eventually accepts strict approximations, but that verifier and termination contract must be implemented. This note supplies no useful asymptotic word-length or search-cost bound.
3. **Actual full-column execution.** Each proposed word must replay the certified H4/sign/swap primitives on all 61 basis columns, preserve the other modes, verify its inverse, and bind its source and word sequence. Agreement only on `e0,e1` is insufficient for later residual-bearing inputs.
4. **A full-operator approximation certificate.** An exact entrywise/Frobenius certificate can upper-bound operator norm if it covers every column and uses certified target information. Orthogonality of the actual word is exact, but does not alone certify proximity to the intended phase. Independently rounding matrix entries is not an acceptable word construction.
5. **Controlled composition and the global budget.** The existing controlled native catalog can lift a validated word as a direct sum; the word's complete-carrier error is retained by this lift. Each gate occurrence must receive and satisfy its budget so their sum is within the requested terminal TV allowance. Retry-transcript budgets, computational costs, and incomplete outputs remain separate contracts.

These are concrete mathematical and implementation obligations, not a request to freeze a larger environment restriction into a taskbook. The density theorem makes the route viable at the level of existence, while the future compiler must turn that existence into actual native words and checkable error bounds.

The present unit changes no published K33 algorithm, demonstrates no practical small-TV run, and claims no independent admission, universal efficient classical factoring, or physical sampling result.

Global-Knowledge-Sync: main@441ebef / GLOBAL_KNOWLEDGE_V1
