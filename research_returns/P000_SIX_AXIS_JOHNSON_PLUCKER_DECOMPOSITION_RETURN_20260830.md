# P000 six-axis Johnson–Plücker decomposition return

Status: `SUCCESS / STRUCTURAL_CALCULUS_SURVIVES`

- Task: `RS-P000-SIX-AXIS-JOHNSON-PLUCKER-DECOMPOSITION`
- Publication: `TP2-88B098FBEE7FEAF82669`
- Researcher: `EM-P000JP1-B4E7C2`
- Claim: `chatgpt-p000jp1-20260830-b4e7c2`
- Exact checker: `research_checks/P000_SIX_AXIS_JOHNSON_PLUCKER_DECOMPOSITION_CHECK_20260830.py`

Hard target disposition:

`P000_SIX_AXIS_JOHNSON_PLUCKER_DECOMPOSITION_AND_ARITHMETIC_INVARIANTS_EXACTLY_CLASSIFIED_AT_DERIVED_CARRIER_LEVEL`

All conclusions stay at the declared carrier/derived-calculus level. They do not reduce native P000 dimension and do not promote carrier `S4`, complement, Hodge star, or `Lambda^2(R^4)` to the full native rotation group.

## 1. Johnson exact layer

Freeze `E1=AB,E2=AC,E3=AD,E4=BC,E5=BD,E6=CD`. With adjacency defined by sharing exactly one carrier endpoint, the Johnson matrix is

```text
A_J =
[0 1 1 1 1 0]
[1 0 1 1 0 1]
[1 1 0 0 1 1]
[1 1 0 0 1 1]
[1 0 1 1 0 1]
[0 1 1 1 1 0].
```

For complement `C=(E1 E6)(E2 E5)(E3 E4)`,

`A_J=J-I-C`, `C^2=I`.

The exact spectrum is `4^1,0^3,(-2)^2`, with minimal polynomial `t(t+2)(t-4)`. Over coefficients in which 6 is invertible, the primitive rational projectors are

`P4=J/6`,
`P0=(I-C)/2`,
`Pm2=(I+C)/2-J/6`.

They are pairwise orthogonal idempotents, sum to `I`, have ranks `1,3,2`, and commute with the frozen unsigned carrier action. Hence the six-edge permutation module has exact `1+3+2` decomposition.

The unsigned carrier generators
`a_xi=(E1 E2 E3)(E4 E6 E5)` and
`b_xi=(E2 E4)(E3 E5)`
satisfy `a_xi^3=b_xi^2=(a_xi b_xi)^4=I` and generate order 24. `C` commutes with this group, is not inside it, and adjoining `C` gives order 48. This is combinatorial carrier symmetry only.

## 2. K4 circuit/cocircuit layer

The four frozen stars

`J_A={E1,E2,E3}`,
`J_B={E1,E4,E5}`,
`J_C={E2,E4,E6}`,
`J_D={E3,E5,E6}`

are the four vertex bonds/cocircuits of `K4`.

The four 3-cycles/circuits are

`ABC={E1,E2,E4}`,
`ABD={E1,E3,E5}`,
`ACD={E2,E3,E6}`,
`BCD={E4,E5,E6}`.

The standard oriented K4 incidence matrix has rank 3 and the signed triangle vectors lie in its cycle kernel. The frozen star transport is recovered exactly:
`a_xi` fixes `J_A` and cycles `J_B->J_C->J_D->J_B`;
`b_xi` swaps `J_A,J_B` and fixes `J_C,J_D` as sets.
Complement sends each star to the opposite triangle.

This is a `T3_TYPED_INCIDENCE_CIRCUIT` reuse result, not a new geometric existence theorem.

## 3. Exterior/Hodge/Pfaffian boundary

Use the ordered exterior basis
`e_A∧e_B,e_A∧e_C,e_A∧e_D,e_B∧e_C,e_B∧e_D,e_C∧e_D`.

The natural `Lambda^2` action is signed when a wedge must be reordered. It is not the frozen unsigned edge-permutation representation. A minimal character separation is:

- transposition: unsigned character `2`, exterior character `0`;
- double transposition: unsigned character `2`, exterior character `-2`.

Thus

`LABEL_BIJECTION != S4_EQUIVARIANT_MODULE_IDENTIFICATION`.

For orientation `A<B<C<D`, Hodge star is

`*E1=E6`,
`*E2=-E5`,
`*E3=E4`,
`*E4=E3`,
`*E5=-E2`,
`*E6=E1`.

Its matrix `H` satisfies `H^2=I`, `det(H)=-1`, rank 6. The candidate Pfaffian/Plücker quadratic

`Q=x1*x6-x2*x5+x3*x4`

satisfies, for the natural exterior action `W_pi`,

`Q(W_pi x)=sgn(pi) Q(x)`.

Therefore `Q` is a sign-relative invariant only after an oriented exterior action is declared. Johnson complement and Hodge star share the same three complementary edge pairs but are not the same operator.

## 4. Q is not an unsigned-carrier invariant

Set

`t1=x1*x6`, `t2=x2*x5`, `t3=x3*x4`, `S=t1+t2+t3`.

Then `Q=S-2*t2`, while the frozen unsigned carrier group permutes `t1,t2,t3`. Hence the complete unsigned-orbit value set is

`{S-2*t1,S-2*t2,S-2*t3}`.

Explicit same-orbit counterexamples:

- `x=(1,0,0,0,0,1)`: `Q=1`, but after `a_xi`, `Q=-1`;
- `x=(2,1,0,0,1,1)`: orbit values `{-1,1,3}`, so `gcd(|Q|,3)` changes;
- `x=(3,1,0,0,1,1)`: orbit values `{-2,2,4}`, so `v_2(Q)` changes.

Thus `Q`, `gcd(Q,m)`, and `v_p(Q)` are not scalar invariants of the frozen unsigned carrier orbit. A safe replacement is the orbit-valued observable

`Q_orb(x)=sort(S-2*t1,S-2*t2,S-2*t3)`.

The unsigned action has exactly three orbits on unordered quadratic coordinate pairs: diagonal (6), adjacent (12), and complementary (3). Consequently every unsigned-carrier invariant symmetric quadratic form lies in the three-dimensional span of `I,A_J,C`; the signed Pfaffian form is not in that commutant.

## 5. New arithmetic residue: integral splitting index 24

Let `L=Z^6` and let `L1,L3,L2` be the integer points in the rational Johnson sectors `im(P4),im(P0),im(Pm2)`.

Explicitly,

`L1=Z*(1,1,1,1,1,1)`,

`L3=Z*(E1-E6)+Z*(E2-E5)+Z*(E3-E4)`,

`L2={(a,b,c,c,b,a):a+b+c=0}`.

Their direct sum `Lsplit=L1⊕L3⊕L2` has determinant/index exactly `24`. Smith invariant factors are

`1,1,1,2,2,6`,

so

`L/Lsplit ~= Z/2 x Z/2 x Z/6 ~= (Z/2)^3 x Z/3`.

A canonical residue map is

`rho(x)=((x1-x6) mod 2,(x2-x5) mod 2,(x3-x4) mod 2,(sum_i x_i) mod 3)`.

It is surjective and

`ker(rho)=Lsplit`.

Equivalently,

`P4*x`, `P0*x`, and `Pm2*x` are all integral iff `rho(x)=0`.

This index-24 denominator obstruction is the strongest new arithmetic output of the task: factor-blind, exact, and tied directly to the canonical Johnson spectral decomposition. The vanishing predicate `rho=0` is invariant under the frozen carrier `S4` and complement.

## 6. Exact factor-blind census

The checker enumerates Cartesian boxes without factoring during state generation.

For `{0,1}^6`:
- total 64;
- Q distribution `{-1:9,0:33,1:19,2:3}`;
- 4 distinct `Q_orb` patterns;
- `rho=0`: 2 states;
- Q varies inside unsigned carrier orbit: 36 states.

For `{-1,0,1}^6`:
- total 729;
- Q distribution `{-3:8,-2:60,-1:174,0:245,1:174,2:60,3:8}`;
- 10 distinct `Q_orb` patterns;
- `rho=0`: 47;
- Q varies inside unsigned carrier orbit: 588.

For `{-2,-1,0,1,2}^6`:
- total 15625;
- 84 distinct `Q_orb` patterns;
- `rho=0`: 733;
- Q varies inside unsigned carrier orbit: 14736.

These are finite certificates only; no factorization speedup or asymptotic claim follows.

## 7. Tool reuse and terminal classification

- `T7_FINITE_SYMMETRY_EQUIVARIANCE`: `REUSE_APPLIED` for group order, orbit, commutation, and equivariance checks.
- `T3_TYPED_INCIDENCE_CIRCUIT`: `REUSE_APPLIED` for K4 circuit/cocircuit typing.
- The task checker is a task-local deterministic certificate, not a new global tool family.

Terminal proved boundary:

1. Johnson `1+3+2` projectors survive exactly.
2. K4 circuit/cocircuit transport survives exactly.
3. Natural exterior and frozen unsigned carrier representations must remain separated.
4. Scalar Pfaffian Q as an unsigned-carrier invariant is refuted.
5. `Q_orb` is a safe orbit-valued replacement.
6. The integer Johnson splitting obstruction `rho` gives quotient `(Z/2)^3 x Z/3` of index 24 and is genuinely new project-level derived arithmetic data.

Open questions about tropical consumption, Full-Cell lifting, or oriented carrier structure are not automatically published as successor tasks.
