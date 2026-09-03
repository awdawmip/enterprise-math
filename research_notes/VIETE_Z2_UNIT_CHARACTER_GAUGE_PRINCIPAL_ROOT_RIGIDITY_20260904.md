# Viète compatible character towers: Z2-unit gauge and rigidity of the principal positive-longitudinal root

Status: `FREE_RESEARCH / EXACT CHARACTER-TOWER CLASSIFICATION + PRINCIPAL-SECTION RIGIDITY / NOT_FOUNDATION`
Date: `2026-09-04`
Researcher: `EM-FREE-7D3C9A / FREE_AXIOM_DISCOVERY`
Issue: `#1158`

## 1. Why the finite gate tower is not yet the Viète radical tower

The winding-memory construction can determine the connected finite state tower

\[
C_3\leftarrow C_6\leftarrow C_{12}\leftarrow C_{24}\leftarrow\cdots.
\]

But a finite cyclic state group does not by itself choose one distinguished primitive one-dimensional character.

Different primitive characters assign different algebraic phases to the same finite gate state and therefore different half-traces.

Thus one must distinguish:

`STATE COVER TOWER`

from

`CHARACTER NORMALIZATION / ROOT TOWER`.

This note classifies the remaining character freedom exactly.

## 2. Reduce to the 2-primary character chain

The Viète half-angle mechanism after the coarse three-ray factor lives in the 2-primary character component.

For `m>=1`, let

\[
U_m=\mu_{2^m}
\]

be the cyclic group of algebraic character values of exact 2-power order.

A compatible primitive character-root tower is a sequence

\[
(u_1,u_2,u_3,\ldots)
\]

such that

\[
\boxed{
\operatorname{ord}(u_m)=2^m,
\qquad
u_{m+1}^2=u_m.
}
\]

The first term is forced:

\[
u_1=-1.
\]

At the next level one chooses one of the two quarter roots.

## 3. Finite-depth classification by odd residue classes

Fix one compatible reference primitive generator system

\[
\zeta_m\in\mu_{2^m},
\qquad
\zeta_{m+1}^2=\zeta_m.
\]

Every primitive element of `mu_{2^m}` is

\[
\zeta_m^{a_m}
\]

for a unique odd residue

\[
a_m\in(\mathbf Z/2^m\mathbf Z)^\times.
\]

A depth-`m` compatible tower is determined by its final primitive element, because repeated squaring determines every coarser level.

Therefore the number of depth-`m` compatible primitive towers is

\[
\boxed{
\varphi(2^m)=2^{m-1}.
}
\]

Equivalently, they are parametrized by the odd residue classes modulo `2^m`.

## 4. Infinite compatible towers form a Z2-unit torsor

Compatibility of exponents means

\[
a_{m+1}\equiv a_m\pmod{2^m}.
\]

Hence an infinite compatible exponent system is exactly an inverse-limit unit

\[
a=(a_m)_m\in\varprojlim_m(\mathbf Z/2^m\mathbf Z)^\times.
\]

The inverse limit is the 2-adic unit group:

\[
\boxed{
\varprojlim_m(\mathbf Z/2^m\mathbf Z)^\times
=\mathbf Z_2^\times.
}
\]

Thus, after choosing one reference tower, the set of all compatible primitive character towers is a torsor under

\[
\boxed{\mathbf Z_2^\times.}
\]

No one reference tower is selected by the abstract finite cyclic state groups alone.

This is standard cyclotomic/profinite mathematics; no historical novelty is claimed.

## 5. Inversion is only one small part of the character gauge

Turn-sense inversion acts by

\[
u_m\mapsto u_m^{-1}.
\]

In exponent coordinates this is

\[
a\mapsto-a.
\]

Thus chirality reversal identifies only the pair

\[
a,\quad-a
\]

inside the much larger unit group `Z_2^x`.

At finite depth `m>=2`, the `2^{m-1}` primitive characters therefore form

\[
2^{m-2}
\]

inversion pairs.

So the statement “there are only two character choices, clockwise and counterclockwise” is false before the principal-root constraint is imposed.

## 6. Root ambiguity at one refinement step

Suppose one compatible primitive value `u_m` has been selected.

Its two primitive square roots at the next level are

\[
w,\qquad-w.
\]

They differ by the `H` half-turn/deck operation, not by sweep inversion `S` in general.

Therefore each new binary character refinement carries a genuine root-sign choice.

Making arbitrary choices at infinitely many levels generates the full `Z_2^x` family above.

## 7. Positive-longitudinal principal root removes the H ambiguity uniquely

Use the Enterprise algebraic longitudinal half-trace

\[
c(w)=\frac{w+w^{-1}}2.
\]

The sibling root-selection theorem proves:

- if the parent is non-antipodal, exactly one of `w,-w` has positive longitudinal coordinate;
- that member is the normalized equal-resultant root;
- at the half-turn parent both quarter roots have zero longitudinal coordinate and must both be retained.

Thus, once one quarter-root chirality branch has been chosen, every later root is uniquely forced by

\[
\boxed{c>0.}
\]

There is no further binary choice along that branch.

## 8. Only two infinite principal towers survive

At the half-turn level

\[
u_1=-1,
\]

the two quarter roots are

\[
J,\qquad-J=J^{-1}.
\]

Choose `J`. The positive-longitudinal theorem uniquely determines all later roots:

\[
J\to u_3^+\to u_4^+\to\cdots.
\]

Choose `-J` instead. The same rule gives the inverse tower

\[
-J\to (u_3^+)^{-1}\to(u_4^+)^{-1}\to\cdots.
\]

Therefore the enormous `Z_2^x` character gauge collapses under the principal-root rule to exactly two towers, exchanged by `S`:

\[
\boxed{
\mathcal T_{\rm principal}=\{\mathcal T_+,\mathcal T_-\},
\qquad
\mathcal T_-=S(\mathcal T_+).
}
\]

No additional deep root choices remain.

## 9. Scalar Viète quotient is unique

The scalar Viète factor is inversion-even:

\[
c(u^{-1})=c(u).
\]

Hence the two principal chirality towers have identical longitudinal factors at every level.

After quotienting by `S`, the scalar tower is unique:

\[
\boxed{
\mathcal T_{\rm scalar}
=
\mathcal T_{\rm principal}/S.
}
\]

This is the unique plus-radical Viète chain.

Thus the full selection sequence is

```text
connected finite gate-state tower
    -> huge compatible primitive-character gauge Z_2^x
    -> choose quarter-root chirality torsor
    -> principal positive-longitudinal root at every deeper level
    -> exactly two inverse oriented towers
    -> S-even scalar quotient
    -> unique Viète nested-radical tower
```

## 10. State precision and character precision are different resources

The winding-memory/profinite state tower is determined by finite quotient structure:

\[
G_m=C_{3\cdot2^m}.
\]

Its coherent state address lives in

\[
C_3\times\mathbf Z_2.
\]

The `Z_2^x` freedom found here belongs instead to **which primitive character system is used to read that state tower**.

Therefore:

\[
\boxed{
\mathbf Z_2\text{ state precision}
\neq
\mathbf Z_2^\times\text{ character gauge}.
}
\]

This distinction prevents a second common type collapse.

## 11. Galois interpretation at finite depth

At finite depth the primitive `2^m`-th character values form one Galois orbit under

\[
(\mathbf Z/2^m\mathbf Z)^\times.
\]

The choice of exponent `a_m` is therefore also a cyclotomic embedding/character choice.

The principal positive-longitudinal rule is not a statement that the other primitive characters cease to exist. It selects one identity-centered refinement branch relevant to the Viète precision observer.

Hence

`CHARACTER_GAUGE_MULTIPLICITY != NATIVE_PATH_MULTIPLICITY`.

The other algebraic embeddings must not be counted as additional Cell trajectories unless a separate bridge says so.

## 12. Relation to algebraic degree growth

The earlier #1158 degree theorem shows that deeper ideal slope/readout fields grow exponentially in degree.

The present theorem explains one source of that structure: finite primitive characters have an expanding unit/Galois orbit, while the principal-root rule selects one compatible real branch from that orbit.

The exponential algebraic field complexity therefore coexists with a very small process prescription:

- one quarter-root chirality choice;
- then deterministic principal-root refinement.

This is another concrete separation between description complexity of the algebraic readout and state-update complexity of the finite precision process.

## 13. Current native boundary

At G1 character strength, the principal-root rule completely removes the `Z_2^x` normalization ambiguity up to chirality, and scalar Viète is unique.

At G0 native strength, the unresolved issue is not character algebra. It is whether actual Cell/process semantics supplies:

1. the connected winding/deck precision tower as an effective state augmentation;
2. a bridge from positive native sector orientation to the positive-longitudinal algebraic root chart.

Once those are given, no further character-normalization freedom remains for the scalar Viète mechanism.
