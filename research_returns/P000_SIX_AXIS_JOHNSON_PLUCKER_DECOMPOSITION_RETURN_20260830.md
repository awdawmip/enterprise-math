# P000 six-axis Johnson–Plücker decomposition return

Status: `SUCCESS / STRUCTURAL_CALCULUS_SURVIVES`

- Task: `RS-P000-SIX-AXIS-JOHNSON-PLUCKER-DECOMPOSITION`
- Publication: `TP2-88B098FBEE7FEAF82669`
- Researcher: `EM-P000JP1-B4E7C2`
- Claim: `chatgpt-p000jp1-20260830-b4e7c2`
- Execution branch: `research/p000-six-axis-johnson-plucker-em-p000jp1-b4e7c2`
- Frozen taskbook: `research_tasks/P000_SIX_AXIS_JOHNSON_PLUCKER_DECOMPOSITION_20260830.md`
- Exact checker: `research_checks/P000_SIX_AXIS_JOHNSON_PLUCKER_DECOMPOSITION_CHECK_20260830.py`

Hard target disposition:

`P000_SIX_AXIS_JOHNSON_PLUCKER_DECOMPOSITION_AND_ARITHMETIC_INVARIANTS_EXACTLY_CLASSIFIED_AT_DERIVED_CARRIER_LEVEL`

No statement below changes bare P000 dimension, identifies `Lambda^2(R^4)` with native ontology, or promotes carrier `S4`, complement, Hodge star, or Pfaffian data to the full native P000 rotation group.

## 0. Executive result

The route survives, but in a sharper form than the naive `six edge labels = exterior bivectors` slogan.

Five conclusions control the return.

1. The frozen **unsigned carrier edge-permutation module** on
   `AB,AC,AD,BC,BD,CD` has exact Johnson decomposition
   `1 + 3 + 2`, with spectrum `4^1,0^3,(-2)^2` and rational primitive projectors
   `J/6`, `(I-C)/2`, `(I+C)/2-J/6`.
2. The natural oriented `Lambda^2` action of the same permutation of four carrier letters is **not the same representation** as the frozen unsigned six-axis action. A transposition has character `2` in the unsigned edge module but character `0` in the natural exterior module. Thus the coordinate bijection to bivectors is a useful derived facade, not an equivariant identification.
3. The Plücker/Pfaffian quadratic
   `Q=x_AB x_CD-x_AC x_BD+x_AD x_BC`
   is a sign-relative invariant for the natural exterior action, but is **not invariant under the frozen unsigned carrier S4**. In one unsigned carrier orbit it can change value, `gcd(Q,m)`, and `v_p(Q)`.
4. There is nevertheless a genuinely new exact arithmetic residue tied to the Johnson spectral calculus: the rational `1+3+2` decomposition fails to split the full integer lattice integrally by index exactly `24`. The obstruction is
   `rho(x)=(x1-x6 mod 2, x2-x5 mod 2, x3-x4 mod 2, sum_i x_i mod 3)`,
   with quotient `(Z/2)^3 x Z/3 ~= Z/2 x Z/2 x Z/6`.
5. The K4 stars are exactly graphic-matroid cocircuits, the four triangles are circuits, and complement exchanges each star with its opposite triangle. This is an exact incidence transport reformulation of the frozen Gen12 star data, not a new geometric existence theorem.

Accordingly the task terminates in `STRUCTURAL_CALCULUS_SURVIVES`: the Johnson projectors, representation-separation certificate, and index-24 integral splitting residue are exact reusable quantities. The naive claim that `Q` itself is an unsigned-carrier arithmetic invariant is refuted.

## 1. Frozen six-axis actions: two representations must be separated

Use

`E1=AB, E2=AC, E3=AD, E4=BC, E5=BD, E6=CD`.

The frozen unsigned carrier generators are

- `a_xi=(E1 E2 E3)(E4 E6 E5)`;
- `b_xi=(E2 E4)(E3 E5)`, with `E1,E6` fixed.

They satisfy exactly

`a_xi^3=b_xi^2=(a_xi b_xi)^4=I`

and generate an order-24 permutation group, faithfully realizing carrier `S4` on the six 2-subsets.

Now encode the same six coordinate labels by the ordered exterior basis

`e_A∧e_B, e_A∧e_C, e_A∧e_D, e_B∧e_C, e_B∧e_D, e_C∧e_D`.

The natural exterior action is signed whenever a permuted wedge must be reordered. In particular:

- under `a=(BCD)`, the first triple cycles positively while the second triple acquires orientation signs on two legs;
- under `b=(AB)`, `e_A∧e_B` changes sign, the AC/BC and AD/BD pairs swap, and CD is fixed.

This signed exterior action again generates an order-24 group and satisfies the same abstract generator relations, but the two six-dimensional representations are not isomorphic. A minimal character witness is:

| carrier class | unsigned edge module | natural `Lambda^2` module |
|---|---:|---:|
| transposition | 2 | 0 |
| double transposition | 2 | -2 |

The unsigned edge module decomposes as `1 + 3 + 2`; the natural exterior module decomposes as two 3-dimensional irreducibles. Therefore:

`LABEL_BIJECTION != S4_EQUIVARIANT_MODULE_IDENTIFICATION`.

This distinction is essential for every claim about Hodge star or `Q`.

## 2. Johnson / association-scheme exact layer

With adjacency defined only by “the two carrier 2-subsets share exactly one endpoint”, the Johnson adjacency matrix in the frozen order is

```text
A_J =
[0 1 1 1 1 0]
[1 0 1 1 0 1]
[1 1 0 0 1 1]
[1 1 0 0 1 1]
[1 0 1 1 0 1]
[0 1 1 1 1 0].
```

Let `J` be the all-ones matrix, `I` the identity, and let complement be

`C=(E1 E6)(E2 E5)(E3 E4)`.

Then exactly

`A_J = J-I-C`, `C^2=I`.

The spectrum and multiplicities are

`4^1, 0^3, (-2)^2`,

with minimal polynomial

`t(t+2)(t-4)`.

Over characteristic zero, or any coefficient ring in which 6 is invertible, the rational primitive projectors are

`P_4 = J/6`,

`P_0 = (I-C)/2`,

`P_-2 = (I+C)/2-J/6`.

The checker verifies exactly:

- `P_i^2=P_i`;
- `P_iP_j=0` for `i!=j`;
- `P_4+P_0+P_-2=I`;
- ranks `1,3,2`;
- `A_J P_4=4P_4`, `A_JP_0=0`, `A_JP_-2=-2P_-2`;
- all three commute with the frozen unsigned carrier `S4`.

Thus the six-dimensional unsigned permutation module has the exact multiplicity-free decomposition

`6 = 1 + 3 + 2`.

The complement involution commutes with the entire unsigned carrier `S4`, but it is not an element of that order-24 group. Adjoining it produces an order-48 group. This is combinatorial automorphism data only.

Complement parity and the Johnson sectors align as follows:

- `C=-1` is exactly the 3-dimensional `0`-eigenspace;
- `C=+1` is the direct sum of the 1-dimensional `4`-sector and 2-dimensional `-2` sector.

## 3. K4 circuit / cocircuit layer

In the K4 graphic matroid, the frozen stars

- `J_A={E1,E2,E3}`;
- `J_B={E1,E4,E5}`;
- `J_C={E2,E4,E6}`;
- `J_D={E3,E5,E6}`

are the four vertex bonds, hence cocircuits.

The four 3-cycles are

- `ABC={E1,E2,E4}`;
- `ABD={E1,E3,E5}`;
- `ACD={E2,E3,E6}`;
- `BCD={E4,E5,E6}`,

and are circuits.

With the standard oriented K4 incidence matrix, its rank is exactly 3 and the signed triangle vectors lie in the cycle kernel. This is the `T3_TYPED_INCIDENCE_CIRCUIT` reuse point; no replacement circuit calculus was created.

The frozen carrier transport is recovered exactly:

- `a_xi(J_A)=J_A`;
- `a_xi(J_B)=J_C`;
- `a_xi(J_C)=J_D`;
- `a_xi(J_D)=J_B`;
- `b_xi(J_A)=J_B`, `b_xi(J_B)=J_A`;
- `b_xi` fixes `J_C,J_D` as sets.

Complement has a useful dual statement:

- `C(J_A)=BCD`;
- `C(J_B)=ACD`;
- `C(J_C)=ABD`;
- `C(J_D)=ABC`.

Thus complement exchanges each vertex cocircuit with its opposite triangle circuit. This is incidence duality in the six-label calculus, not a Full-Cell slice existence result.

## 4. Exterior, Hodge, and Pfaffian layer

Choose orientation `A<B<C<D`. In the ordered bivector basis, Hodge star is

`*E1= E6`,
`*E2=-E5`,
`*E3= E4`,
`*E4= E3`,
`*E5=-E2`,
`*E6= E1`.

Its matrix `H` satisfies

`H^2=I`, `det(H)=-1`, rank `6`.

The `+/-` Hodge sectors are each dimension 3. Reversing the underlying 4-label orientation changes the Hodge operator sign and exchanges the signed interpretation of these sectors. This orientation dependence is precisely why Hodge star cannot be silently imported into the unsigned carrier module.

For the natural exterior action `W_pi`,

`W_pi^T H W_pi = sgn(pi) H`.

Equivalently the Pfaffian/Plücker quadratic

`Q(x)=x1 x6-x2 x5+x3 x4`

obeys

`Q(W_pi x)=sgn(pi)Q(x)`.

Hence `Q` is preserved by even carrier permutations and changes sign under odd carrier permutations in the natural exterior representation.

The unsigned Johnson complement `C` and Hodge `H` share the same three complementary edge pairs, but are not equal. `C` has no orientation signs. They commute, and `C` preserves `Q`, but this support-level coincidence is not an equivariant identification of the two operators.

The polarization of `Q` has Gram matrix `H` (up to the conventional factor 2). Consequences:

- over `Z`, `H` is unimodular;
- over `R`, signature is `(3,3)`;
- over fields of characteristic not 2, the form is split hyperbolic of rank 6;
- in characteristic 2, the polynomial becomes `x1x6+x2x5+x3x4`; its polarization is alternating and nondegenerate, so the rank-6 split structure survives but the sign-relative formulation collapses;
- the rational Johnson projectors themselves require inversion of 2 and 3, so characteristics 2 and 3 are non-semisimple/merged cases and must not be read through the characteristic-zero projector formulas.

No equation `Q=0` was imposed.

## 5. Arithmetic layer

### 5.1 Exact unsigned-carrier orbit law for Q

Define the three complementary products

`t1=x1x6`, `t2=x2x5`, `t3=x3x4`, and `S=t1+t2+t3`.

Then `Q=S-2t2`.

The frozen unsigned carrier `S4` permutes the three complementary pairs, hence the complete `Q`-value set along one unsigned carrier orbit is

`{S-2t1, S-2t2, S-2t3}`

with multiplicities inherited from coincidences among the `t_i`.

Therefore `Q` is not an unsigned-carrier invariant.

Minimal witness:

`x=(1,0,0,0,0,1)` has `Q(x)=1`, while `Q(a_xi x)=-1`.

Even sign-insensitive arithmetic can change:

- for `x=(2,1,0,0,1,1)`, the unsigned orbit has `Q` values `{-1,1,3}`, so `gcd(|Q|,3)` changes;
- for `x=(3,1,0,0,1,1)`, the unsigned orbit has `Q` values `{-2,2,4}`, so `v_2(Q)` changes from 1 to 2.

Thus neither `gcd(Q,m)` nor `v_p(Q)` is a well-defined invariant of the frozen unsigned carrier orbit unless one first passes to an explicitly declared oriented exterior lift or replaces `Q` by its full unsigned orbit data.

A safe derived observable is therefore the unordered triple

`Q_orb(x)=sort(S-2t1,S-2t2,S-2t3)`.

### 5.2 Carrier-invariant quadratic forms

The unsigned carrier action has exactly three orbits on unordered coordinate pairs:

1. six diagonal terms;
2. twelve adjacent-edge cross terms;
3. three complementary-edge cross terms.

Equivalently, because the Johnson module is multiplicity-free, its symmetric commutant is 3-dimensional and spanned by `I,A_J,C`.

So every unsigned-carrier invariant symmetric quadratic form is a linear combination of these three exact forms. The signed Pfaffian Gram matrix `H` is not in that commutant.

The complement quadratic

`R_C=t1+t2+t3 = (1/2)x^T Cx`

is carrier-invariant where 2 is invertible, but it is already encoded by the Johnson complement operator and is not an independent fourth symmetry invariant.

### 5.3 Complement sectors and Q

Write complementary-pair coordinates

`u_i=(x_i+x_{i^c})/2`, `v_i=(x_i-x_{i^c})/2`.

Then the C-even and C-odd parts separate:

`Q=(u1^2-u2^2+u3^2)-(v1^2-v2^2+v3^2)`.

There are no C-even/C-odd cross terms. However the internal sign pattern `(+,-,+)` is orientation-dependent and not invariant under the frozen unsigned `S4`; therefore this formula is a decomposition identity, not an unsigned-carrier invariantization of Q.

### 5.4 New integral spectral-splitting residue: index 24

Let `L=Z^6` be the integer six-axis lattice. Let

- `L_1 = L ∩ im(P_4)`;
- `L_3 = L ∩ im(P_0)`;
- `L_2 = L ∩ im(P_-2)`.

Explicitly,

`L_1=Z(1,1,1,1,1,1)`;

`L_3=Z(E1-E6)+Z(E2-E5)+Z(E3-E4)`;

`L_2={(a,b,c,c,b,a): a+b+c=0}`.

The direct sum

`L_split=L_1⊕L_3⊕L_2`

is not all of `Z^6`. A basis determinant is exactly 24. A Smith computation gives invariant factors

`1,1,1,2,2,6`,

so

`L/L_split ~= Z/2 x Z/2 x Z/6 ~= (Z/2)^3 x Z/3`.

A canonical residue map exhibiting the quotient is

`rho(x)=(`
` x1-x6 mod 2,`
` x2-x5 mod 2,`
` x3-x4 mod 2,`
` sum_i x_i mod 3 )`.

It is surjective and

`ker(rho)=L_split`.

Equivalently:

`P_4x, P_0x, P_-2x are all integral <=> rho(x)=0`.

This is the strongest genuinely new arithmetic output of the task. It measures the denominator obstruction to splitting an integer six-axis state into the three canonical rational Johnson sectors. It is factor-blind, exact, and derived entirely from the six-axis carrier calculus.

The vanishing condition `rho=0` is invariant under the frozen carrier `S4` and complement. The three mod-2 components themselves are permuted by carrier symmetry; the mod-3 total-sum component is fixed.

### 5.5 Factor-blind finite census

The checker enumerates Cartesian state boxes directly; generation never factors coordinates or selects states using prime factors.

For `{0,1}^6`:

- states: `64`;
- `Q` distribution: `-1:9, 0:33, 1:19, 2:3`;
- distinct unsigned `Q_orb` patterns: `4`;
- `rho=0`: `2` states;
- states whose `Q` varies along unsigned carrier orbit: `36`.

For `{-1,0,1}^6`:

- states: `729`;
- `Q` distribution: `-3:8, -2:60, -1:174, 0:245, 1:174, 2:60, 3:8`;
- distinct unsigned `Q_orb` patterns: `10`;
- `rho=0`: `47`;
- states whose `Q` varies along unsigned carrier orbit: `588`.

For `{-2,-1,0,1,2}^6`:

- states: `15625`;
- `Q` distribution:
  `-12:8, -10:48, -9:24, -8:204, -7:120, -6:568, -5:408, -4:1230, -3:848, -2:1920, -1:1278, 0:2313, 1:1278, 2:1920, 3:848, 4:1230, 5:408, 6:568, 7:120, 8:204, 9:24, 10:48, 12:8`;
- distinct unsigned `Q_orb` patterns: `84`;
- `rho=0`: `733`;
- states whose `Q` varies along unsigned carrier orbit: `14736`.

These counts are certificates of the declared finite families only; no asymptotic or algorithmic speedup is inferred.

## 6. Gen12 regression / consumable residue table

| object | `a_xi` | `b_xi` | complement `C` | status for Gen12 |
|---|---|---|---|---|
| Johnson `P_4,P_0,P_-2` | commute | commute | commute | safe carrier-derived projectors |
| four stars | `A` fixed; `B->C->D->B` | `A<->B`, `C,D` fixed | stars -> opposite triangles | incidence transport only |
| unsigned carrier group | order-3 generator | order-2 generator | central outer combinatorial involution | axis-label level only |
| natural exterior action | signed order-3 lift | signed order-2 lift | separate operator | derived oriented facade |
| Pfaffian `Q` under natural exterior | preserved | sign flip | preserved | orientation-relative classifier only |
| Pfaffian `Q` under frozen unsigned action | generally changes | generally changes | preserved | **not** a carrier invariant |
| unsigned `Q_orb` | invariant | invariant | invariant | safe orbit-valued residue |
| `rho=0` integral-splitting condition | invariant | invariant | invariant | safe arithmetic obstruction |

No nontrivial Cell kernel, central extension, or Full-Cell residue is proved here. If Gen12 consumes any item, it must remain typed as an axis-label/carrier-derived classifier unless separately lifted by the Gen12 model.

## 7. Deterministic certificate and tool reuse

The exact checker uses only Python standard-library integer/rational arithmetic. It verifies:

- frozen six labels and Johnson adjacency identity `A=J-I-C`;
- exact spectrum dimensions and minimal-polynomial annihilation;
- all three rational projectors and their orthogonality/idempotence;
- frozen carrier generator relations and group order 24;
- complement commutation and order-48 extension;
- K4 star/circuit incidence statements;
- natural signed exterior action and its representation-character separation from the unsigned module;
- Hodge matrix and exact transformation law for Q;
- explicit Q/gcd/valuation counterexamples;
- three unsigned quadratic coefficient orbits;
- determinant-24 integral splitting lattice and the residue criterion;
- all three finite censuses.

Reuse resolution:

- `T7_FINITE_SYMMETRY_EQUIVARIANCE`: `REUSE_APPLIED` for finite group generation, orbit, commutation and equivariance logic;
- `T3_TYPED_INCIDENCE_CIRCUIT`: `REUSE_APPLIED` for K4 circuit/cocircuit typing and incidence-kernel interpretation;
- this checker is a task-local deterministic certificate, not a new general-purpose tool family.

## 8. Proved statements

`PROVED-1` — The frozen unsigned six-axis carrier module is the J(4,2) edge module with exact `1+3+2` rational decomposition.

`PROVED-2` — `C=(E1 E6)(E2 E5)(E3 E4)` is a central combinatorial involution commuting with carrier S4, outside that S4; adjoining it gives order 48.

`PROVED-3` — The four frozen K4 stars are cocircuits, the four triangles are circuits, and complement exchanges each star with its opposite triangle.

`PROVED-4` — The natural `Lambda^2` representation associated with the same four carrier labels is not the frozen unsigned six-axis representation.

`PROVED-5` — In the natural exterior representation, `Q` transforms by the sign character.

`PROVED-6` — Under the frozen unsigned carrier S4, `Q`, `gcd(Q,m)` and `v_p(Q)` are not invariants in general; the exact unsigned Q-orbit is `{S-2t1,S-2t2,S-2t3}`.

`PROVED-7` — Every unsigned-carrier invariant symmetric quadratic form lies in the 3-dimensional span of `I,A_J,C`.

`PROVED-8` — The rational Johnson sectors do not integrally split `Z^6`; their integer direct sum has index exactly 24.

`PROVED-9` — The index-24 obstruction is exactly the residue `rho` with quotient `(Z/2)^3 x Z/3`; all three rational projectors are simultaneously integral iff `rho=0`.

`PROVED-10` — The declared factor-blind finite censuses reproduce the exact distributions and counterexample frequencies frozen in the checker.

## 9. Counterexamples / killed interpretations

The following candidate interpretations are closed negatively.

1. `Lambda^2(R^4)` is not an equivariant identification of the frozen unsigned carrier six-axis module; it is only a coordinate/derived representation facade unless one changes the action to the signed exterior action.
2. `Q` is not a scalar invariant of frozen unsigned carrier S4.
3. `gcd(Q,m)` and `v_p(Q)` are not rescued by ignoring the sign of Q; explicit same-orbit counterexamples change them.
4. Hodge star is not the Johnson complement involution; it requires orientation signs.
5. None of Johnson complement, Hodge star, exterior S4, or the index-24 residue is thereby a native P000 rotation or Full-Cell theorem.

## 10. New reusable quantities

The task returns four reusable derived quantities/certificates.

1. `P_4,P_0,P_-2`: exact rational Johnson spectral projectors on the frozen six-axis carrier module.
2. `Q_orb(x)=sort(S-2t1,S-2t2,S-2t3)`: a safe unsigned-carrier orbit-valued replacement for the non-invariant Pfaffian scalar.
3. `rho(x) in (Z/2)^3 x Z/3`: the exact integral spectral-splitting obstruction, especially the invariant predicate `rho(x)=0`.
4. the representation-separation certificate `chi_unsigned((12))=2 != 0=chi_exterior((12))`, preventing future conflation of the unsigned edge and signed exterior modules.

The project-level novelty is not the classical existence of Johnson schemes, exterior powers, Hodge star or Pfaffians. It is the exact compatibility/no-compatibility boundary with the already frozen P000 six-axis carrier action, together with the index-24 arithmetic residue produced by that boundary.

## 11. Open questions — not automatically published

The following remain legitimate but are not successor tasks created by this return:

- whether the sibling tropical/valuated-matroid task can use `Q_orb` or `rho` as a valuation-stable input;
- whether a declared Gen12 Full-Cell lift carries any of the rational Johnson sectors or integral residue functorially at the enriched level;
- whether the index-24 lattice obstruction has a stronger canonical formulation over localized coefficient rings or mod-p reduction;
- whether an oriented carrier datum exists elsewhere in the project that legitimately upgrades the signed exterior representation from a facade to a typed derived state object.

Those questions require independent scheduling/authority. This return itself is terminal at the declared derived-carrier scope.
