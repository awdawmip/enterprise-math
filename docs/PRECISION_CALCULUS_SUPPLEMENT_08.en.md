# P018 — Finite-Precision Proof Calculus: Supplement 08

Status: `ACTIVE RESEARCH NOTE`  
Scope: P006/P018 signed precision extensions, section-dependent carry, coboundary changes, and non-strictifiable structural obstructions  
Depends on: P006, P008, P018-T63–T67  
Discipline: group extensions, short exact sequences, 2-cocycles, coboundaries, and extension classes are established mathematics. The research target here is to determine how these mature objects enter the finite-precision foundation of Enterprise Math exactly, not to rename them and claim priority.

## 1. Why the passage from `N` to `Z` must be checked explicitly

Supplement 07 proves on natural-number states that

\[
\Phi_m(n)=(n//m,n\bmod m)
\]

rewrites natural-number addition as a twisted monoid consisting of coarse state, detail, and carry.

The standard group-cohomological interpretation of carry, however, naturally lives between signed integers and a cyclic quotient group. Without separating these two levels one can easily conflate two different statements:

1. coarse/detail decomposition on `N` forms a commutative monoid with carry;
2. the residue quotient on `Z` forms a genuine group extension whose section defect is classified by a 2-cocycle.

P006 already proves that signed extension is not obtained by merely attaching a minus sign to the natural-number root: the usual-order root and the signed-magnitude root are different structures. The same discipline is required here. We must state which signed quotient semantics are being used.

This supplement studies only **integer Euclidean decomposition / residue quotient**. It does not modify either root semantics already separated by P006.

---

## 2. P018-T68 — Signed Euclidean precision decomposition

Status: `PROVED / ESTABLISHED`

Fix an integer `m>=1`. For every

\[
z\in\mathbb Z
\]

there exist unique

\[
q_m(z)\in\mathbb Z,
\qquad
\rho_m(z)\in\{0,1,\ldots,m-1\}
\]

such that

\[
\boxed{z=mq_m(z)+\rho_m(z).}
\]

Here `q_m` is the Euclidean/floor quotient paired with a nonnegative canonical remainder, not truncation toward zero.

Thus the coarse/detail coordinates of finite precision extend across negative states without ambiguity once the quotient convention is made part of the state definition.

This matches the P006 design discipline: **signed state must explicitly choose its order and quotient semantics; a programming language's default integer division must not silently decide the mathematics.**

---

## 3. P018-T69 — The same carry exactly controls signed additive defect

Status: `PROVED`

For `x,y in Z`, write

\[
x=mq_x+r_x,
\qquad
y=mq_y+r_y,
\qquad0\le r_x,r_y<m.
\]

Define the standard carry as before:

\[
\kappa_m(r_x,r_y)
=\left\lfloor\frac{r_x+r_y}{m}\right\rfloor
\in\{0,1\}.
\]

Then

\[
\boxed{
q_m(x+y)=q_m(x)+q_m(y)+\kappa_m(r_x,r_y)
}
\]

and

\[
\boxed{
\rho_m(x+y)=(r_x+r_y)\bmod m.
}
\]

### Proof

Add the two Euclidean decompositions:

\[
x+y=m(q_x+q_y)+(r_x+r_y).
\]

A second unique Euclidean decomposition of `r_x+r_y` gives the two formulas. ∎

Thus the carry defect of Supplement 07 is not a boundary effect caused by restricting to natural numbers. Under the correct signed Euclidean quotient, it extends unchanged to `Z`.

---

## 4. P018-T70 — Coarse/detail/carry on `Z` forms a genuine twisted group

Status: `PROVED`

Let

\[
D_m=\{0,1,\ldots,m-1\}
\]

with modular addition, identifying it with the standard representatives of the cyclic group `Z/mZ`.

Define

\[
\Phi_m^{\mathbb Z}(z)=(q_m(z),\rho_m(z)).
\]

On `Z x D_m` define

\[
(a,u)\boxplus(b,v)
=
\bigl(a+b+\kappa_m(u,v),(u+v)\bmod m\bigr).
\]

Then

\[
\boxed{
(\mathbb Z,+)
\cong
(\mathbb Z\times D_m,\boxplus)
}
\]

as groups.

The identity is `(0,0)`. Inverses can be written explicitly:

\[
\boxed{-(a,0)=(-a,0),}
\]

while for `0<u<m`,

\[
\boxed{-(a,u)=(-a-1,m-u).}
\]

Indeed,

\[
u+(m-u)=m
\]

produces exactly one carry, which cancels the additional `-1` in the coarse coordinate.

This gives a signed unification of carry and borrow: **crossing zero or a digit boundary needs no hidden continuous remainder; the correction is part of the inverse structure of the same extension algebra.**

---

## 5. P018-T71 — Carry is the section defect of the standard residue extension

Status: `PROVED / ESTABLISHED EXTENSION-THEORY INSTANCE`

Consider the short exact sequence

\[
\boxed{
0
\longrightarrow\mathbb Z
\xrightarrow{\times m}
\mathbb Z
\xrightarrow{\rho}
\mathbb Z/m\mathbb Z
\longrightarrow0.
}
\]

Choose the standard section

\[
s:\mathbb Z/m\mathbb Z\to\mathbb Z,
\qquad
s([u])=u,
\qquad0\le u<m.
\]

The section is generally not a group homomorphism. Its failure to preserve addition is

\[
s(u)+s(v)-s(u+v)=m\kappa_m(u,v).
\]

Hence

\[
\boxed{
\kappa_m(u,v)
=\frac{s(u)+s(v)-s(u+v)}{m}.
}
\]

The quotient is an exact integer because the numerator belongs to the kernel `mZ`.

Thus the cohomological meaning of carry is not merely a renaming of elementary carrying. Once a detail representative section is chosen, the section cannot strictly preserve the group operation; carry is the exact kernel coordinate of that failure.

Daniel C. Isaksen, *A Cohomological Viewpoint on Elementary School Arithmetic* (American Mathematical Monthly, 2002, DOI `10.1080/00029890.2002.11919915`) explicitly discusses carrying, group extensions, and cocycles. This established connection is not an Enterprise Math invention.

---

## 6. P018-T72 — Changing the section changes carry only by a coboundary

Status: `PROVED / PRIOR-ART COHOMOLOGY PATTERN`

Keep the same residue quotient but replace the standard section `s` by another section `s'`.

Every such section can be written

\[
s'(u)=s(u)+m h(u),
\]

for some

\[
h:\mathbb Z/m\mathbb Z\to\mathbb Z.
\]

Let its corresponding defect be

\[
\kappa'_m(u,v)
=\frac{s'(u)+s'(v)-s'(u+v)}{m}.
\]

Substitution gives

\[
\boxed{
\kappa'_m(u,v)
=\kappa_m(u,v)
+h(u)+h(v)-h(u+v).
}
\]

Thus a different representative system changes the local carry table, but the change is exactly a coboundary.

### Direct consequence for representation switches

This strengthens the representation-switch discipline of Supplement 07:

> **A local defect may depend on representation. What deserves promotion toward the foundation may instead be the equivalence or cohomology class that survives all legitimate representation changes.**

Future precision-defect research should therefore distinguish:

1. coordinate-dependent defect;
2. change-of-section law;
3. representation-invariant obstruction.

This distinction can serve as a general filter for deciding which quantities are worthy of foundational status.

---

## 7. P018-T73 — For `m>1`, the carry obstruction cannot be globally strictified away

Status: `PROVED / ESTABLISHED GROUP-THEORETIC CONSEQUENCE`

For `m>1`, the short exact sequence

\[
0\to\mathbb Z\xrightarrow{\times m}\mathbb Z\to\mathbb Z/m\mathbb Z\to0
\]

**does not split**.

### Elementary proof

If the extension split, there would exist a group-homomorphic section

\[
s:\mathbb Z/m\mathbb Z\to\mathbb Z
\]

whose composition with the quotient is the identity.

Then `s(1)` would be an element of order `m` in `Z`. But the additive group `Z` is torsion-free: no nonzero element has finite order.

Contradiction. ∎

Therefore there is no section whose cocycle is identically zero on all inputs.

Equivalently,

\[
\boxed{
\text{carry may be re-coordinatized, but for }m>1\text{ it cannot be eliminated globally.}
}
\]

This is stronger than saying that one chosen projection is not a homomorphism. That failure might have been blamed on poor coordinates. T73 shows that, in the signed group extension, **no smarter choice of representatives can strictify the entire defect away.**

This yields the strongest candidate foundational principle of the present stage:

> Some finite-precision defects should be understood as structural obstructions rather than computational errors. A defect is eligible for deletion from the foundation only after the corresponding extension/class is shown to be trivializable.

---

## 8. The boundary between P006 and P018 is now sharper

P006 already distinguishes:

- odd-power `orderRootOdd`;
- `magnitudeRoot`;
- `signedMagnitudeCollapse`.

The `q_m / rho_m` introduced here form **another independent signed scale decomposition**. They do not select a root semantics and do not revise any existing P006 result.

There are therefore at least two signed-state questions that must not be conflated:

1. **root semantics**: should negative-number roots follow the usual integer order or signed magnitude?
2. **precision quotient semantics**: how should a negative state decompose into a coarse integer plus a canonical nonnegative residue?

The two can be composed, but neither replaces the other.

This preserves the P006 route while giving P018 a genuine group-extension host.

---

## 9. A third candidate layer for the foundational logic

Supplement 07 gave:

- Layer 0: order-adjoint core;
- Layer 1: defect-enriched operation core.

This supplement suggests a still-unfrozen Layer 2:

### Layer 2 — Defect equivalence / obstruction layer

Do not treat a particular coordinate table `D_f` as the final invariant. Record instead

\[
\boxed{
\text{defect}
+\text{change-of-representation law}
+\text{obstruction class}.
}
\]

The core questions become:

- Which defects can be removed by a legitimate representation change?
- Which can change representatives but cannot be eliminated?
- Which nontrivial extension/class data constitute irreducible information about the finite-precision structure itself?

For additive carry, T72–T73 provide a complete prototype.

This is more robust than promoting the word “cocycle” itself to a new primitive, because it preserves the distinction between representation-dependent quantities and structural invariants.

---

## 10. From carry obstruction to general precision obstruction

A more disciplined workflow can now be proposed for an arbitrary operation defect in a precision system.

Given a precision system and operation `f`:

### Step A — Define the defect

\[
D_f=\pi f-f\pi.
\]

### Step B — Identify legitimate representation changes

Specify which coordinate, section, or representative changes preserve the semantics of the original problem.

### Step C — Derive the defect transformation law

Determine whether

\[
D_f\mapsto D'_f
\]

is governed by a coboundary, conjugacy, gauge transformation, or another mature structure.

### Step D — Find the obstruction

Ask whether some legitimate representation can make

\[
D'_f=0.
\]

If yes, the original defect is closer to a coordinate artifact. If no, search for the invariant that obstructs strictification.

### Step E — Only then consider foundational promotion

Only structures stable across representations, or structures whose entire representation-change law can be controlled exactly, should be considered candidates for the foundational logic.

This is a stronger anti-drift rule than adding every attractive formula to the base layer.

---

## 11. New connection to the P017 global-certificate route

The signed shells, carries, and Möbius terms in P017 often depend on a chosen decomposition.

T72 suggests that a local term changing under a different decomposition need not mean the proof structure has changed. A better question may be:

> Do different P017 decompositions, anchors, or precision axes obey a change-of-section-like transformation law so that the total certificate belongs to one equivalence class?

If so, a global certificate need not require every local decomposition to agree. It would be enough to prove:

1. legitimate re-representations add only controlled boundary/coboundary terms;
2. the final obstruction / total certificate is invariant;
3. the Legendre existence target imposes a definite sign or nonvanishing condition on that invariant.

This route is currently `OPEN`, but is structurally stronger than requiring termwise positivity.

---

## 12. New connection to P012 geometry

P012 geometry should use the same filter.

When a lattice lift, coset coordinate, or embedding changes and a local distance formula changes with it, distinguish:

- whether the geometry itself changed;
- whether only its coordinate expression changed;
- whether a gauge/coboundary-like equivalence relation exists;
- which shortest-path or quotient-fiber quantities remain representation-invariant.

Thus P012 keeps primitive graph metric as its most stable baseline while allowing derived geometries to move upward only after passing a representation-invariance test.

---

## 13. Next open questions

### P018-Q69 — Lean formalization of signed carry

Formalize T68–T70 using the current canonical integer Euclidean division/modulo operations in mathlib, with special care over negative-number conventions.

### P018-Q70 — Finite formalization of section change / coboundary

There is no need to import a full group-cohomology library first. Prove T72 directly for finite residue representatives.

### P018-Q71 — Formalize the nonsplitting obstruction

Formalize that for `m>1` there is no additive section `Z/mZ -> Z`, and connect this to the impossibility of making carry globally zero.

### P018-Q72 — Multi-precision extension tower

For `d|e|f`, study the nested subgroups

\[
f\mathbb Z\subseteq e\mathbb Z\subseteq d\mathbb Z\subseteq\mathbb Z
\]

and determine how the corresponding extension classes compose, connecting the result with T67 staged-carry coherence.

### P018-Q73 — Abstract precision obstruction

Find a structure weak enough to cover integer precision but strong enough to speak about strictification obstruction. Do not assume in advance that a full abelian category or derived functor is necessary.

---

## 14. Current conclusion

Supplement 07 shows that carry is operation-defect and cocycle data.

Supplement 08 moves one layer deeper:

\[
\boxed{
\text{a concrete carry table is not the final object.}
}
\]

The more stable hierarchy is

\[
\boxed{
\text{section defect}
\longrightarrow
\text{coboundary change law}
\longrightarrow
\text{nonsplitting obstruction / extension class}.
}
\]

The candidate foundational evolution is therefore

\[
\boxed{
\text{order adjunction}
\to
\text{typed precision projection}
\to
\text{exact defect}
\to
\text{coherence}
\to
\text{defect equivalence / obstruction}
\to
\text{proof certificate and time dynamics}.
}
\]

The most important new rule is:

> **First ask whether a defect can be strictified by a legitimate re-representation; only then decide whether it belongs to the foundation.**

For signed additive carry with `m>1`, the answer is already negative: representatives may change, but the obstruction cannot be removed globally.