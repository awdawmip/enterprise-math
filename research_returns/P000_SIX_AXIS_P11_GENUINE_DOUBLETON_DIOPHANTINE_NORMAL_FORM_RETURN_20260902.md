# P000 six-axis genuine P11 doubleton Diophantine normal form — Return

- Task: `RS-P000-SIX-AXIS-P11-GENUINE-DOUBLETON-DIOPHANTINE-NORMAL-FORM`
- Publication: `TP2-5774A7C199FB50588943`
- Parent accepted Result: `RR-16ADB5F4DE72A332B509`
- Researcher: `EM-P000P11D1-4C8E72`
- Claim: `chatgpt-p000p11d1-20260902-1013-4c8e72`
- Execution branch: `research/p000-six-axis-p11-genuine-doubleton-diophantine-em-p000p11d1-4c8e72`
- Execution branch base: `bde59957ed4e9ac3e5cf14c9a222d1c3eefd5a4c`
- Result: `RR-952CD6287F68219D7782`
- Execution record: `ER-D76E045E3B49878A7F95`

## Terminal verdict

`DIOPHANTINE_NORMAL_FORMS_COMPLETE_WITH_NONRATIONAL_PARAMETER_COMPONENTS`

The frozen six-square/parity membership test can be replaced by an exact primitive **rank-one integer normal form**.  Every genuine C1 doubleton is represented canonically by three primitive rank-one factor skeletons and six scale coordinates satisfying three linear row equations, strict order inequalities and one homogeneous cubic collision equation.  C2 is not a second independent arithmetic species: it is the exact involutive image of C1 under global root negation plus reversal of the sorted `H` rows.

After quotienting common root scaling, a fixed factor skeleton is a projective cubic slice.  At least one actual primitive nonzero-root C1 solution lies on a fixed skeleton whose slice is birational to a squarefree quartic double cover of `P^1`, hence is a genus-one, non-rational component.  Therefore a globally complete description cannot consist only of rational/conic/Pell-style parameter components.  The correct terminal form is a complete skeleton/cubic normal form with a certified genus-one component.

No higher mixed moment, native orientation, Pfaffian slot, dimension reduction, factorization claim, Full-Cell dynamics, Working Truth, Foundation authority or canonical promotion is used.

---

## 1. Frozen input restatement

Let

`H=(h0<h1<h2)`, `T=(t0<t1<t2)`

and

`A=h1-h0`, `B=h2-h1`, `C=t1-t0`, `D=t2-t1`.

For an edge `(h,t)`, frozen pairability is

`Pair(h,t) <=> h^2-4t=d^2 >= 0` with `d ≡ h (mod 2)`.

Equivalently there is a unique unordered integer root pair `{r,s}` with

`r+s=h`, `rs=t`.

The genuine C1 edge set is

`(0,0),(0,1),(1,0),(1,2),(2,1),(2,2)`

and C1 collision is `A*C=B*D`.

The genuine C2 edge set is

`(0,1),(0,2),(1,0),(1,2),(2,0),(2,1)`

and C2 collision is `A*D=B*C`.

---

## 2. Rank-one equal-product lemma

### Lemma 2.1 — canonical column factorization

Take two pairable edges with the same product `t` and different sums.  Recover and sort their root pairs

`top=(a,b)` with `a<=b`, and `bottom=(c,d)` with `c<=d`.

Because `ab=cd`, the integer matrix

`M = [[a,c],[d,b]]`

has determinant zero.  The two sums are different, so `M` is not the zero matrix.  Hence it has rank one over `Q`.  Let `(p,q)` be the primitive integer generator of its row line, normalized by

`gcd(|p|,|q|)=1`

and the first nonzero entry of `(p,q)` positive.  Then there are unique integers `(u,v)` such that

`M = [[u*p,u*q],[v*p,v*q]]`.

Thus the two sorted root pairs are exactly

`top=(u*p, v*q)`,

`bottom=(u*q, v*p)`.

Conversely these formulas always give equal products, because both products equal `u*v*p*q`.

This is just primitive rank-one factorization of an integer `2 x 2` matrix.  It includes all sign patterns and all zero-product boundaries: no division by a root is required.

### Root-swap effect

Before sorting, each of the six pairable edges admits the finite swap of its two local roots.  These are presentation symmetries only; they do not change `(h,t)`.  Sorting every recovered pair removes all six swaps canonically before the rank-one factorization is taken.  Therefore the normal form is unique, not merely unique after making arbitrary root-order choices.

---

## 3. Complete C1 normal form

Apply Lemma 2.1 to the three equal-product columns of C1:

- column `t0`, joining rows `h0 -> h1`, with primitive skeleton `(p0,q0)` and scales `(u0,v0)`;
- column `t1`, joining rows `h0 -> h2`, with primitive skeleton `(p1,q1)` and scales `(u1,v1)`;
- column `t2`, joining rows `h1 -> h2`, with primitive skeleton `(p2,q2)` and scales `(u2,v2)`.

The six edge root pairs are then

`(h0,t0): (u0*p0, v0*q0)`

`(h1,t0): (u0*q0, v0*p0)`

`(h0,t1): (u1*p1, v1*q1)`

`(h2,t1): (u1*q1, v1*p1)`

`(h1,t2): (u2*p2, v2*q2)`

`(h2,t2): (u2*q2, v2*p2)`

with each displayed pair already in its canonical sorted order.

### Theorem 3.1 — C1 equivalence

A datum `(H,T)` is a genuine C1 doubleton if and only if there exist canonical primitive skeletons `(pj,qj)` and integer scales `(uj,vj)` satisfying all of the following.

**Row compatibility**

`u0*p0+v0*q0 = u1*p1+v1*q1 = h0`,

`u0*q0+v0*p0 = u2*p2+v2*q2 = h1`,

`u1*q1+v1*p1 = u2*q2+v2*p2 = h2`.

**Products**

`t0=u0*v0*p0*q0`,

`t1=u1*v1*p1*q1`,

`t2=u2*v2*p2*q2`.

**Strict sorted gaps**

`A=(q0-p0)*(u0-v0)>0`,

`B=(q2-p2)*(u2-v2)>0`,

`A+B=(q1-p1)*(u1-v1)`,

`C=t1-t0>0`,

`D=t2-t1>0`.

**C1 collision**

`A*C=B*D`.

**Sorted-root chamber inequalities**

For each column, the two reconstructed top/bottom pairs obey their canonical nondecreasing inequalities, e.g. `uj*pj <= vj*qj` on the top edge and `uj*qj <= vj*pj` on the bottom edge.

### Proof

Necessity: genuine C1 supplies exactly the six pairable edges.  Recover their unique unordered roots, sort them, and apply Lemma 2.1 independently to the three equal-product columns.  The three row equations are exactly the requirement that the two C1 edges in each row have the same sum `hi`.  The product formulas are tautological.  Taking differences of the two sums in columns `t0,t2,t1` gives the displayed formulas for `A,B,A+B`; the frozen collision equation gives `A*C=B*D`.

Sufficiency: start from the displayed integer data.  Each column formula produces two integer root pairs with equal product, so all six frozen C1 edges are pairable.  The row equations identify their sums with a single strictly sorted `H`; the product equations identify their products with a single strictly sorted `T`.  Finally `A*C=B*D` is exactly the frozen C1 combinatorial collision criterion.  Hence both C1 packets are pairable and the datum is a genuine C1 doubleton.

Thus the six discriminant-square/parity predicates have been eliminated from the classification and replaced by an exact integer rank-one normal form.

---

## 4. Primitive normalization and uniqueness

Because `gcd(|pj|,|qj|)=1`, the gcd of the four roots occurring in column `j` is exactly `gcd(|uj|,|vj|)`.  Therefore the common gcd of all twelve recovered edge roots is

`m = gcd(|u0|,|v0|,|u1|,|v1|,|u2|,|v2|)`.

Scaling every recovered root by `m` multiplies every `uj,vj` by `m` and leaves every primitive skeleton `(pj,qj)` fixed.  Consequently

`H -> m H`, `T -> m^2 T`.

Every genuine C1 datum therefore has a unique positive primitive representative obtained by dividing all `uj,vj` by `m`; primitive means exactly `m=1`.  Canonical sorting plus the primitive sign normalization of each `(pj,qj)` makes this representative unique.  There is no remaining infinite normalization ambiguity.

This proves the requested existence/uniqueness modulo common root scaling and the declared finite pre-sorting root swaps.

---

## 5. Signs and zero-root boundaries

The normal form handles signs without case deletion.

For column `j`,

`t_j = u_j v_j p_j q_j`.

Hence the sign of `t_j` is exactly the sign of that product.  If `t_j<0`, both local pairs in that column have one positive and one negative root.  If `t_j>0`, each local pair has roots of the same sign.  If `t_j=0`, at least one of `u_j,v_j,p_j,q_j` is zero and every edge in that equal-product column has a zero root.  Since `t0<t1<t2`, at most one column can be a zero column.

The signs of the `h_i` are not separately constrained by pairability: they are the signed row sums given in Theorem 3.1.  Strict order is encoded exactly by `A>0,B>0` rather than by deleting negative, even or composite roots.

Thus negative roots, zero roots, even roots and roots with small prime factors are part of the same normal form; none are discarded as a preprocessing convention.

---

## 6. C2 is the C1 involutive image

### Theorem 6.1

Define

`I(H,T)=((-h2,-h1,-h0), T)`.

On recovered local roots this is obtained by negating every root and reversing the sorted `H` row order.  Since pairability depends on `h^2-4t`, it is preserved.  The C1 six-edge pattern maps exactly to the C2 six-edge pattern.

The `H` gaps are exchanged: `A' = B`, `B' = A`, while `C,D` are unchanged.  Therefore

`A*C=B*D`

maps to

`A'*D=B'*C`.

So `I` is an involutive bijection between genuine C1 and genuine C2 doubletons, preserving common root gcd and therefore primitive status.

This completely classifies C2 from C1; a second unrelated parameter grammar is unnecessary.

The retained B=6 witnesses are exchanged by this involution:

C1: `H=(-1,1,4)`, `T=(-30,-12,0)`;

C2: `H=(-4,-1,1)`, `T=(-30,-12,0)`.

For the C1 witness the canonical column parameters are

`(p0,q0,u0,v0)=(6,5,-1,1)`,

`(p1,q1,u1,v1)=(2,1,-2,3)`,

`(p2,q2,u2,v2)=(4,1,0,1)`,

so the known B=6 family is recovered internally by multiplying all six `u/v` scales by a common `m`, not inserted as exceptional data.

---

## 7. Fixed skeletons are cubic arithmetic components

Fix the three primitive skeletons

`S=((p0,q0),(p1,q1),(p2,q2))`.

The three row-compatibility equations are homogeneous linear equations in

`U=(u0,v0,u1,v1,u2,v2)`.

Thus they define a rational linear space `L_S`.  Common root scaling acts by scalar multiplication on `U`, so primitive scaling quotient is the integral part of the projectivization `P(L_S)`.

The gaps `A,B` are linear in `U`, whereas each `t_j=u_j v_j p_j q_j` is quadratic.  Hence

`A*(t1-t0)-B*(t2-t1)=0`

is a homogeneous cubic on `L_S`.

Therefore the exact global primitive solution set is a disjoint canonical union over primitive signed factor skeletons of integral points in projective cubic slices, intersected with the explicit sorted-root and strict-order chambers.  Degenerate skeletons are included automatically; if the row-equation rank drops, one obtains the corresponding higher-dimensional linear-space cubic slice rather than a failed parameterization.

This is the complete normal-form classification promised by the task.  What remains to determine is whether every such cubic slice is rational.  The answer is no.

---

## 8. Exact genus-one obstruction

Consider the primitive genuine C1 datum

`H=(-7,11,13)`, `T=(10,12,30)`.

Its six sorted root pairs are

`(-5,-2), (-4,-3), (1,10), (5,6), (1,12), (3,10)`

on the C1 edges, and its canonical skeleton/scales are

`(p0,q0,u0,v0)=(5,-1,-1,2)`,

`(p1,q1,u1,v1)=(4,-1,-1,3)`,

`(p2,q2,u2,v2)=(5,3,1,2)`.

So fix

`S=((5,-1),(4,-1),(5,3))`.

Solving the three row equations gives

`v0=(-55*u0+45*u1+16*u2)/13`,

`v1=(-120*u0+97*u1+16*u2)/13`,

`v2=(-96*u0+75*u1+5*u2)/13`.

Substitution into the C1 collision gives, up to the nonzero scalar `10/169`, the homogeneous cubic

`G = 11220*u0^3 -45405*u0^2*u1 -33552*u0^2*u2`

`    +49515*u0*u1^2 +55200*u0*u1*u2 -96*u0*u2^2`

`    -16296*u1^3 -22667*u1^2*u2 +163*u1*u2^2 +120*u2^3`.

The primitive witness is `(-1:-1:1)`, equivalently `(1:1:-1)` projectively.

On the affine chart `u0=1`, write `x=u1/u0`, `y=u2/u0` and take the pencil of lines through `P=(1,-1)`:

`y=-1+s*(x-1)`.

After removing the known factor `(x-1)`, the residual quadratic in `x` has coefficients

`A(s)=120*s^3+163*s^2-22667*s-16296`,

`B(s)=-240*s^3-619*s^2+54874*s+55886`,

`C(s)=120*s^3+456*s^2-33000*s-44556`.

Its discriminant is

`Delta(s)=466489*s^4-2689724*s^3+8699424*s^2-57498680*s+218906692`.

Exact Euclidean gcd gives

`gcd_Q(Delta, Delta')=1`.

Hence the line-pencil model is birational to the squarefree quartic double cover

`w^2=Delta(s)`.

A double cover of `P^1` branched at four distinct points has genus one by the classical Riemann-Hurwitz formula.  Equivalently, the corresponding smooth projective cubic has genus `(3-1)(3-2)/2=1`.  Geometric genus is birationally invariant, whereas `P^1` has genus zero; therefore this component is not rational.

Classical references used only for this final genus interpretation:

- Stacks Project, Tag `0BYD`, plane-curve genus formula: https://stacks.math.columbia.edu/tag/0BYD
- Stacks Project, Tag `0C1D`, Riemann-Hurwitz: https://stacks.math.columbia.edu/tag/0C1D
- Stacks Project, Tag `0CE2`, birational invariance of geometric genus: https://stacks.math.columbia.edu/tag/0CE2
- Stacks Project, Tag `0C6U`, characterization of `P^1`/genus zero: https://stacks.math.columbia.edu/tag/0C6U

The rank-one specialization, the displayed skeleton, the cubic and the quartic are task-specific derivations.  The genus theory itself is prior mathematics.

### Parametrization conclusion

This genus-one slice is the required exact non-rational arithmetic component.  Therefore the terminal result is **not** `FINITE_PRIMITIVE_C1_C2_PARAMETER_FAMILIES_COMPLETE`; a complete normal form necessarily permits non-rational cubic components.

The claim is deliberately algebraic: this obstructs a rational parametrization of the component in the standard birational/dominant sense.  It does not claim that no ad hoc algorithm can enumerate individual rational or integral points on an elliptic curve.

---

## 9. Simultaneous C1+C2 sublocus

Assume the strict gaps `A,B,C,D` are positive and both collision equations hold:

`A*C=B*D`,

`A*D=B*C`.

Dividing the two equalities gives `C/D=D/C`, hence `C=D`; substituting back gives `A=B`.

Conversely `A=B` and `C=D` imply both collision equations.  Therefore

**simultaneous combinatorial C1+C2 iff `H` and `T` are both strict three-term arithmetic progressions.**

This is a specialization of the separate collision families, not a new scaling species.

To be **simultaneously genuine**, a genuine C1 point on this AP specialization must additionally make the two C2-only corners pairable:

`(h0,t2)` and `(h2,t0)`.

The four shared C1/C2 edges are already pairable, so these two extra corners are the exact additional arithmetic conditions.  Thus the simultaneous genuine locus is an intersection specialization of the same rank-one normal form; it carries no new common-scaling rule.

The bounded regression below found no simultaneously genuine point in the declared root box.  That finite absence is recorded only as regression evidence and is **not** promoted to a global impossibility theorem.

---

## 10. Bounded full-integer regression

The finite regression domain was declared before the formal census:

`all recovered local integer roots r with -20 <= r <= 20`.

No parity class, even integer, composite, or small-prime factor was removed.  The domain contains `861` unordered root pairs.

Exact task-local checker output:

`PASS P000_P11_GENUINE_DOUBLETON_DIOPHANTINE_NORMAL_FORM root_box_R=20 unordered_root_pairs=861 factor_checks=3644 C1=83 C2=83 primitive_C1=78 gcd_profile=1:78,2:4,3:1 zero_column_C1=66 primitive_zero_C1=61 AP_C1=3 simultaneous_genuine_box=0 counterexample_height=9 obstruction_skeleton=(5,-1)|(4,-1)|(5,3) cubic_identity_checks=125 quartic_degree=4 quartic_squarefree=1`

Consequences inside this declared box:

- genuine C1 doubletons: `83`;
- genuine C2 doubletons: `83`, exactly paired with C1 by Theorem 6.1;
- primitive in each class: `78`;
- C1 root-gcd profile: `m=1:78`, `m=2:4`, `m=3:1`;
- C1 zero-product-column points: `66`, of which `61` are primitive;
- C1 AP collision points: `3`;
- simultaneously genuine C1+C2 points: `0` (regression only).

Observed C1 `T` sign patterns, preserving the full integer population:

`--0:32`, `-0+:22`, `0++:12`, `--+:8`, `---:7`, `+++:2`.

Observed C1 `H` sign patterns:

`--+:33`, `-++:26`, `+++:19`, `---:4`, `0++:1`.

These counts are not used as proof of the symbolic classification.

---

## 11. Required falsifier: B=6 is not the whole primitive world

The tempting simplification

> every genuine doubleton is a common scale of the B=6 seed

is false.

A primitive C1 counterexample already occurs at root height `9`:

`H=(-7,-3,2)`, `T=(-18,-8,0)`.

Its six C1 edge root pairs are

`(-9,2), (-8,1), (-6,3), (-3,0), (-2,4), (0,2)`.

Their common gcd is `1`, so this point is primitive.  It is not the B=6 witness and therefore cannot be a nontrivial common scaling of that primitive witness.

This counterexample is exact, not statistical.

---

## 12. Tool-reuse and novelty classification

A bounded lookup of `enterprise_toolbox_registry.json` found no accepted enterprise tool for `Diophantine`, `pairability`, or this P11 root normal form.  The parent task-local exact pairability/root-reconstruction logic was reused rather than reimplemented as a new global mechanism.  No global tool promotion is proposed.

Classical machinery:

- primitive rank-one factorization of integer `2 x 2` determinant-zero matrices;
- projective/affine cubic slices and line pencils;
- Riemann-Hurwitz, genus one, and birational invariance.

Task-specific contribution:

- identifying the three C1 equal-product columns as canonical rank-one matrices;
- proving the exact C1 normal form and primitive-gcd law;
- proving the C1/C2 involution;
- reducing each fixed skeleton to a cubic arithmetic slice;
- isolating the explicit primitive skeleton `((5,-1),(4,-1),(5,3))` and deriving its exact genus-one quartic obstruction;
- full-integer `[-20,20]` regression and the height-9 non-B6 primitive falsifier.

---

## 13. Hard-target disposition

Hard target:

`P000_P11_GENUINE_DOUBLETON_DIOPHANTINE_NORMAL_FORM_EXACTLY_CLASSIFIED_OR_FINITE_PARAMETRIZATION_OBSTRUCTED`

Disposition:

`DIOPHANTINE_NORMAL_FORMS_COMPLETE_WITH_NONRATIONAL_PARAMETER_COMPONENTS`.

The integer solution set is exactly classified by canonical primitive factor skeletons plus projective cubic slices.  A certified fixed skeleton has a genus-one non-rational component, so the rational-family branch of the task is closed at the correct obstruction strength.

No downstream task decision is made from the researcher lane.  Driver review is required.
