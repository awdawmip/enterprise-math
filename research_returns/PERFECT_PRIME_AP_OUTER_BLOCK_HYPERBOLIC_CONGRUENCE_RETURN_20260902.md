# Perfect Prime AP outer block-hyperbolic congruence invariant — Research Return

Researcher-ID: `EM-PPTAPOBHC1-C58329`
Task: `RS-PERFECT-PRIME-AP-OUTER-BLOCK-HYPERBOLIC-CONGRUENCE`
Publication: `TP2-E2EE65A96658AD50D37C`
Claim: `CLM-43687A005470DE71A6DF`
Execution record: `ER-F7285D4C9DB27860AEF4`
Result: `RR-19DB7617DE41BD10CCF7`

## Terminal verdict

`NEGATIVE_BOUNDARY / EXACT_STATIC_SIMULTANEOUS_BLOCK_OBSTRUCTION / UNSTRUCTURED_ADAPTIVE_BLOCK_EXISTENCE_EQUIVALENT_TO_NONSINGULARITY / PARENT_NONVANISHING_OPEN`

This return does **not** prove or refute

`det S_m(t) != 0` for every `m>=2`, `0<t<=1`.

It closes two tempting but insufficient readings of the new block-hyperbolic route.

1. A **single t-independent congruence with one fixed 1x1/2x2 block partition** cannot work uniformly: an exact `m=4` three-parameter certificate rules it out already at `t=1/3,2/3,1`.
2. If the phrase "there exists a 1x1/2x2 block LDL decomposition" is allowed to choose pivots adaptively with no extra structure, then for real symmetric matrices that existence is **equivalent to nonsingularity itself**. It therefore cannot be the independent invariant needed to prove the Perfect Prime determinant theorem without circularity.

The surviving block route is consequently much narrower: it must construct an explicit, genuinely structured `t`-dependent congruence or pivot rule whose block determinants are controlled by an independent formula. Merely invoking symmetric-indefinite pivoting does not advance the parent theorem.

## 1. Frozen input

Use the accepted outer matrix unchanged. Put `n=m-1`, `b=m^2`,
`y_j=mj`, `w_j=(-1)^j binom(n,j)`, and

`lambda_(j,s)(t)=(-1)^s binom(n,s)t^s c_s(y_j)`

with

`c_s(y)=n! / prod_(r=1)^m (y+b s+r)`.

For `1<=r,q<=n`,

`C_j(t)[r,q]
 = sum_s lambda_(j,s) z_(j,s)^(r+q)
   -(sum_s lambda_(j,s)z_(j,s)^r)
    (sum_s lambda_(j,s)z_(j,s)^q)/Dcal_j(t)`

where `z_(j,s)=y_j+b s` and `Dcal_j=sum_s lambda_(j,s)>0`.

The frozen outer matrix is

`S_m(t)=sum_(j=0)^n w_j C_j(t)`

in the quotient monomial basis `X,...,X^n`, and the accepted reduction gives

`tau_m(t) != 0 <=> det S_m(t) != 0`

for `0<t<=1`.

The predecessor negative boundary is also frozen: at `m=15,t=4/5` the canonical scalar LDL pivots exchange signs at positions 12 and 13 while the full determinant remains nonzero and the inertia remains `7+/7-`.

## 2. Exact theorem: unrestricted adaptive 1x1/2x2 block LDL is equivalent to nonsingularity

### Theorem

Let `A` be a finite real symmetric matrix. Then the following are equivalent.

- `A` is nonsingular.
- After a permutation of coordinates and repeated symmetric Schur-complement elimination, `A` admits a block LDL congruence whose diagonal pivot blocks all have size `1` or `2` and are nonsingular.

### Proof

The reverse implication is immediate: a congruence by an invertible elimination matrix preserves rank, and a block diagonal matrix with nonsingular diagonal blocks is nonsingular.

For the forward implication, induct on the dimension.

If some diagonal entry `a_ii` is nonzero, permute it to the first coordinate and use the nonsingular `1x1` principal pivot `[a_ii]`. The symmetric Schur complement is again nonsingular because

`det A = a_ii * det(Schur)`.

If every diagonal entry is zero, nonsingularity implies that some off-diagonal entry `a_ij` is nonzero. Permute `i,j` to the first two coordinates. Their principal block is

`[[0,a_ij],[a_ij,0]]`

with determinant `-a_ij^2 != 0`. Eliminate this nonsingular `2x2` block. Again

`det A = det(block) * det(Schur)`

so the remaining symmetric Schur complement is nonsingular. Apply the induction hypothesis.

Thus an adaptive `1x1/2x2` pivot sequence exists for **every** nonsingular real symmetric matrix, in every odd or even dimension.

### Consequence for this task

For the frozen `S_m(t)`, the assertion

`there exists some adaptive nonsingular 1x1/2x2 block LDL`

is exactly equivalent to

`det S_m(t) != 0`.

So this existential block statement is not a sharper invariant. A valid block proof must prescribe additional structure and prove the required block determinants nonzero without first assuming the parent target.

This also handles the task's size-parity issue at the abstract level: no odd/even exception rescues the unrestricted existential formulation.

## 3. Exact obstruction to a fixed t-independent simultaneous block congruence

A genuinely stronger possibility would be a single basis, independent of `t`, in which the whole family `S_m(t)` splits into blocks of dimension at most two.

This already fails at `m=4`, where `S_4(t)` is `3x3`.

Set

`A=S_4(1/3)`,
`B=S_4(2/3)`,
`C=S_4(1)`.

The exact checker gives

`det A > 0`, `det B > 0`, `det C > 0`.

Assume for contradiction that one fixed `P in GL_3(R)` and one fixed partition `1+2` simultaneously block-diagonalize all three forms by congruence:

`P^T A P`, `P^T B P`, `P^T C P`.

(The fully diagonal `1+1+1` case is stronger and is included.)

Let `U` be the one-dimensional block in the original coordinates and `W` its two-dimensional complement. Since `A` is nonsingular and `U,W` are `A`-orthogonal, `A` is nondegenerate on each block. Define

`T_B=A^(-1)B`,
`T_C=A^(-1)C`.

For `u in U`, `w in W`,

`A(T_B u,w)=B(u,w)=0`.

Hence `T_B U subset U`; similarly `T_C U subset U`. Therefore `U` is a common real eigenline of `T_B` and `T_C`.

Now form the exact commutator

`K=[T_B,T_C]=T_B T_C-T_C T_B`.

The checker proves exactly

`rank K = 2`, `det K = 0`.

Thus `ker K` is one-dimensional. A primitive integer generator `v` of this kernel has coordinate bit lengths

`[345,340,334]`

and canonical comma-separated-vector hash

`sha256:3ba80ec7b3a9d849a9bc977b546dfd72900fb220c5d90081a660be542e0cca43`.

The checker verifies

`K v = 0`

but also

`(T_B v) wedge v != 0`;

indeed all three wedge coordinates are nonzero, with signs

`[+,-,-]`.

Therefore the unique commutator-kernel line is not an eigenline of `T_B`. No common eigenline exists. This contradicts the necessary condition for a fixed simultaneous `1+2` congruence decomposition.

Hence:

`NO_FIXED_T_INDEPENDENT_SIMULTANEOUS_1x1_2x2_BLOCK_CONGRUENCE_FOR_S_4(t)`.

Because the target theorem is universal in `m`, this single exact `m=4` obstruction is sufficient to rule out any proposed all-`m` theorem of that static-basis form.

## 4. The most obvious adjacent 2x2 repair also inherits the accepted crossing

There is an even simpler warning against merely pairing canonical scalar pivots.

In the canonical ordering, grouping coordinates as adjacent pairs
`(1,2),(3,4),...` makes every even prefix determinant the product of the preceding `2x2` block determinants whenever the elimination is defined.

But the accepted predecessor certificate proves for `m=15` that

`Delta_(15,12)(3/4)>0`,
`Delta_(15,12)(4/5)<0`,
`Delta_(15,12)(1)>0`.

By continuity, `Delta_(15,12)` vanishes at least once in `(3/4,4/5)` and at least once in `(4/5,1)`.

Therefore the canonical adjacent-pair block schedule cannot provide nonsingular blocks throughout the admissible interval: at a zero of the `12x12` prefix determinant, the product of its first six `2x2` block determinants cannot remain nonzero.

So the paired-pivot exchange does **not** mean that simply gluing neighboring canonical pivots into fixed pairs repairs the proof.

## 5. Regression against the accepted m=15 witness

The paired exact checker reconstructs the predecessor witness from the frozen formula, not from stored determinant values.

At `m=15,t=4/5`, the leading-principal-minor signs are

`[-,-,+,+,-,-,+,+,-,-,+,-,-,-]`.

The rejected old pattern is

`[-,-,+,+,-,-,+,+,-,-,+,+,-,-]`.

The sole mismatch is still `k=12`. The one-by-one LDL pivot signs are

`[-,+,-,+,-,+,-,+,-,+,-,-,+,+]`

with exactly `7` positive and `7` negative pivots. The `Delta_12` signs at
`t=3/4,4/5,1` remain `+,-,+`.

Thus the new obstruction preserves the accepted paired-pivot phenomenon exactly and does not silently restore the failed scalar flag.

## 6. Endpoint and parity boundary

The admissible interval is `0<t<=1`. The exact static obstruction uses `t=1` as one of its three matrices and two interior rational parameters, so it is not an artifact of approaching the excluded singular endpoint `t=0`.

At the first endpoint the accepted expansion remains

`S_m(t)=t S_m^(1)+O(t^2)`

with nondegenerate quotient crossing form `S_m^(1)`. Nothing in this return changes the forced order `ord_(t=0) det S_m(t)=m-1`.

For matrix-size parity:

- the adaptive-existence equivalence holds in every dimension;
- the static simultaneous-basis obstruction occurs already in quotient dimension `3` (`m=4`);
- the even-dimensional `m=15` regression shows the adjacent pivot-pair exchange but is used only as a regression/route warning, not as an all-`m` theorem.

## 7. Exact residue left open

This task does **not** prove that every conceivable structured `t`-dependent block congruence fails.

What survives is precisely the noncircular version:

> Find an explicit `t`-dependent congruence, permutation law, or hyperbolic-pair construction determined from the closed formulas for `S_m(t)`, and prove independently that every resulting `1x1/2x2` pivot block has nonzero determinant for all `m>=2`, `0<t<=1`.

The word "independently" is load-bearing. A rule whose next pivot is certified only because the remaining Schur complement is assumed nonsingular is just the theorem in Section 2 and is circular.

If no such structured rule is found, the separate residual Bernstein/Mobius interface remains the genuinely different fallback route already preserved by the Driver. It is not bundled into this return.

## 8. Tool reuse and verification

Tool-routing audit:

- `coverage_verdict = NOT_APPLICABLE` for the curated Enterprise Toolbox: no registered LDL/Schur/symmetric-congruence family matched this exact task contract.
- `matched_tool_or_method_ids = []`.
- Current Method Inventory likewise contains no Schur/LDL/inertia method at the required semantic strength.
- Executable-source lookup returned no relevant current reusable implementation.
- `reuse_resolution_state = REUSE_APPLIED` at the task-local level: the predecessor's exact `fractions.Fraction` construction of `S_m(t)` and exact determinant arithmetic were reused unchanged rather than re-derived through a new general-purpose package.
- `hard_boundary_checked`: finite computation certifies only the stated `m=4` static obstruction and reproduces the `m=15` regression; the adaptive-block equivalence is proved symbolically above.

Paired checker:

`research_checks/PERFECT_PRIME_AP_OUTER_BLOCK_HYPERBOLIC_CONGRUENCE_CHECK_20260902.py`.

Paired certificate:

`research_artifacts/PERFECT_PRIME_AP_OUTER_BLOCK_HYPERBOLIC_CONGRUENCE/static_block_obstruction_certificate_20260902.json`.

`method_harvest = RESULT_ONLY`.

No Working Truth, Foundation authority, L4/canonical promotion, novelty claim, or parent-objective closure is requested.

Recommended Driver disposition:

`ACCEPT EXACT_NEGATIVE_BOUNDARY; close the fixed t-independent simultaneous <=2 block congruence route and reject unstructured adaptive block-LDL existence as an independent invariant; preserve det S_m(t)!=0 as open; any further block successor must name a genuinely structured t-dependent invariant with independently controlled pivot determinants, otherwise route to the already separate residual Bernstein/Mobius interface.`
