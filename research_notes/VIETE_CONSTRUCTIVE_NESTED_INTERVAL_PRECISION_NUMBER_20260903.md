# Viète constructive precision-number: nested finite radical intervals define Pi_rot before classical pi

Status: `FREE_RESEARCH / EXACT NESTED-INTERVAL CONSTRUCTION + FINITE BIT CERTIFICATE / NOT_FOUNDATION`
Date: `2026-09-03`
Researcher: `EM-FREE-7D3C9A / FREE_AXIOM_DISCOVERY`
Issue: `#1158`
Parent: `research_notes/VIETE_TARGET_FREE_TWO_SIDED_GATE_BRACKET_20260903.md`

## 1. Precision interval from one finite radical state

For `n>=1`, define the two target-free finite readouts

\[
L_n:=\Pi_n^-=2^{n+1}s_n,
\]

\[
U_n:=\Pi_n^+=\frac{2^{n+1}s_n}{c_n}.
\]

The parent proves

\[
L_n<L_{n+1},
\qquad
U_{n+1}<U_n,
\]

and both sequences have the same finite limit.

Define the finite precision interval

\[
\boxed{I_n=[L_n,U_n].}
\]

Then

\[
\boxed{I_{n+1}\subset I_n.}
\]

No target real constant is used to construct any endpoint.

## 2. First interval

From

\[
c_1=s_1=\frac{\sqrt2}{2},
\]

one gets

\[
L_1=4\frac{\sqrt2}{2}=2\sqrt2,
\]

and

\[
U_1=\frac{2\sqrt2}{\sqrt2/2}=4.
\]

Therefore

\[
\boxed{I_1=[2\sqrt2,4].}
\]

Its exact width is

\[
\boxed{W_1=4-2\sqrt2<2.}
\]

This initial interval is generated entirely from the first nontrivial nested-root state.

## 3. Strict sub-quarter interval contraction

The parent proves the exact width recurrence

\[
\frac{W_{n+1}}{W_n}
=
\frac{c_n}{(1+c_n)(1+c_{n+1})}
<\frac14.
\]

Therefore by induction

\[
\boxed{
W_n
<
\frac{W_1}{4^{n-1}}
<
\frac{2}{4^{n-1}}
=
2^{3-2n}.
}
\]

Hence

\[
W_n\to0
\]

with an explicit finite target-free rate.

## 4. Unique nested-interval number

The intervals are nonempty, closed, nested, and have diameters tending to zero. Therefore the nested-interval theorem gives exactly one real number in their intersection:

\[
\boxed{
\bigcap_{n=1}^{\infty}I_n
=\{\Pi_*\}.
}
\]

This can be used as an intrinsic definition:

\[
\boxed{
\Pi_* := \text{the unique real number contained in every finite Viète precision interval }I_n.
}
\]

The monotone-limit construction in the parent immediately shows

\[
\Pi_*=\Pi_{\rm rot}.
\]

Thus `Pi_rot` may be defined equivalently either as:

- the target-free monotone limit of the lower readouts; or
- the unique point selected by the nested finite radical intervals.

The interval formulation makes the precision content explicit at every finite stage.

## 5. Binary absolute-precision certificate

Fix a requested absolute precision width

\[
2^{-b},
\qquad b\in\mathbb N_0.
\]

The simple bound

\[
W_n<2^{3-2n}
\]

shows that

\[
3-2n\le-b
\]

is sufficient. Therefore

\[
\boxed{
n\ge\left\lceil\frac{b+3}{2}\right\rceil}
\]

implies

\[
\boxed{W_n<2^{-b}.}
\]

So a finite nested-radical state at depth roughly `b/2` certifies `b` bits of **interval-width absolute precision** for the intrinsically generated number.

This is a worst-case finite guarantee; the exact width recurrence is sharper.

## 6. Precision is stored by the state, not compared to a target

At depth `n`, the mathematical datum

\[
(c_n,s_n,L_n,U_n)
\]

already carries:

- current lower estimate `L_n`;
- current upper estimate `U_n`;
- exact certified uncertainty width `W_n`;
- an exact next-state rule that reduces the width by more than a factor four.

No external decimal approximation of the final number is required to say how precise the state is.

Thus the state itself realizes a precision-number semantics:

\[
\boxed{
\text{FINITE NUMBER STATE}=(\text{readout interval},\text{refinement law},\text{certified width}).
}
\]

## 7. Six-gate cover indexing

For the gate tower

\[
G_m=C_{3\cdot2^m},
\qquad m\ge3,
\]

the corresponding interval is

\[
I_m^{\rm gate}
=
\left[
\frac{|G_m|}{6}s_m,
\frac{|G_m|}{6}\frac{s_m}{c_m}
\right].
\]

One extra binary cover level produces a strictly sub-quarter interval-width contraction.

Therefore:

\[
\boxed{
1\text{ bit of gate-state resolution}
\Longrightarrow
>2\text{ bits of certified interval-width gain at every finite step, asymptotically }2.
}
\]

The `>2` statement refers to finite width ratio `<1/4`; the asymptotic information gain tends to exactly two bits because the ratio tends to `1/4`.

## 8. Classical identification is not part of the definition

Only after `Pi_*` has been defined by the nested target-free intervals does the classical compatibility layer prove

\[
\boxed{\Pi_*=\pi.}
\]

Thus a logically clean formulation is:

1. construct a unique real constant from finite discrete/algebraic rotation refinement;
2. equip every finite stage with an intrinsic certified interval;
3. prove independently that the resulting constant agrees with classical `pi`.

This avoids defining precision by measuring error against a value already assumed known.

## 9. Relation to classical polygon bounds

After classical identification one recognizes the lower and upper endpoints as the usual inscribed/circumscribed dyadic polygon semiperimeter readouts.

That historical compatibility is welcome but not used in the internal construction.

The nested-interval theorem is therefore an exact refoundation of the same convergence phenomenon from the finite radical state itself.

## 10. Boundary

This result is exact at the G1 finite orientation/refinement layer. It does not prove that G0 Cell dynamics uniquely realizes the binary cycle-cover refinement.

But once that finite refinement layer is admitted, the precision-number object is fully target-free and internally certified.
