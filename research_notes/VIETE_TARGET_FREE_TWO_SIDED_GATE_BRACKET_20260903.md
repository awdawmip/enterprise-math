# Viète target-free two-sided gate bracket: lower/upper finite readouts and strict sub-quarter interval contraction

Status: `FREE_RESEARCH / EXACT TARGET-FREE FINITE INTERVAL THEOREM / NOT_FOUNDATION`
Date: `2026-09-03`
Researcher: `EM-FREE-7D3C9A / FREE_AXIOM_DISCOVERY`
Issue: `#1158`
Parents:
- `research_notes/VIETE_TARGET_FREE_ROTATION_COMPLETION_CONSTANT_20260903.md`
- `research_notes/VIETE_INTRINSIC_QUARTERING_ASYMPTOTIC_20260903.md`
- `research_notes/VIETE_GATE_DISTANCE_HALVING_AND_GATE_PI_READOUT_20260903.md`

## 1. Goal

The previous target-free completion theorem gave a simple finite upper certificate for the intrinsic rotation constant `Pi_rot`. The current half-angle state contains enough information for a much sharper, symmetric lower/upper bracket.

No classical `pi`, tangent function, polygon theorem, or continuous circle is needed to define or prove the bracket.

## 2. Finite half-angle state

Use

\[
c_{n+1}=\sqrt{\frac{1+c_n}{2}},
\qquad
s_n=\sqrt{1-c_n^2}>0,
\]

and the target-free lower readout

\[
\Pi_n^-=2^{n+1}s_n.
\]

For `n>=1`, `c_n>0`. Define the companion upper readout

\[
\boxed{
\Pi_n^+:=\frac{2^{n+1}s_n}{c_n}
=\frac{\Pi_n^-}{c_n}.
}
\]

These are generated entirely by the same finite radical state.

## 3. Lower sequence is strictly increasing

The exact half-root relation gives

\[
s_n=2s_{n+1}c_{n+1}.
\]

Therefore

\[
\Pi_n^-
=2^{n+1}s_n
=2^{n+2}s_{n+1}c_{n+1}
=c_{n+1}\Pi_{n+1}^-.
\]

Since

\[
0<c_{n+1}<1,
\]

we have

\[
\boxed{
\Pi_{n+1}^->\Pi_n^-.
}
\]

The parent proves that this increasing sequence converges to the intrinsic completion constant

\[
L:=\Pi_{\rm rot}.
\]

## 4. Upper sequence is strictly decreasing

Using the same identity,

\[
\Pi_{n+1}^+
=\frac{\Pi_{n+1}^-}{c_{n+1}}
=\frac{\Pi_n^-}{c_{n+1}^2}.
\]

But

\[
c_{n+1}^2=\frac{1+c_n}{2},
\]

so

\[
\Pi_{n+1}^+
=
\Pi_n^-\frac{2}{1+c_n}.
\]

Meanwhile

\[
\Pi_n^+=\frac{\Pi_n^-}{c_n}.
\]

Hence

\[
\boxed{
\frac{\Pi_{n+1}^+}{\Pi_n^+}
=\frac{2c_n}{1+c_n}<1.
}
\]

Therefore

\[
\boxed{
\Pi_{n+1}^+<\Pi_n^+.
}
\]

## 5. Both sequences have the same target-free limit

Their ratio is

\[
\frac{\Pi_n^+}{\Pi_n^-}=\frac1{c_n}.
\]

The target-free recurrence proves

\[
c_n\to1.
\]

Since

\[
\Pi_n^-\to L,
\]

it follows that

\[
\Pi_n^+\to L
\]

as well.

Thus for every `n>=1`,

\[
\boxed{
\Pi_n^-<L<\Pi_n^+.
}
\]

This is an intrinsic two-sided finite radical bracket for `Pi_rot`.

Only after the separate classical compatibility theorem may the same interval be renamed a bracket for classical `pi`.

## 6. Exact interval width

Define

\[
W_n:=\Pi_n^+-\Pi_n^-.
\]

Then

\[
\boxed{
W_n
=
\Pi_n^-\left(\frac1{c_n}-1\right)
=
\Pi_n^-\frac{1-c_n}{c_n}.
}
\]

With

\[
d_n:=1-c_n,
\]

this is

\[
W_n=\Pi_n^-\frac{d_n}{c_n}.
\]

Every factor is known from the current finite state.

## 7. Exact width-contraction ratio

At the next level,

\[
W_{n+1}
=
\Pi_{n+1}^-\frac{d_{n+1}}{c_{n+1}}.
\]

Use

\[
\Pi_{n+1}^-=rac{\Pi_n^-}{c_{n+1}}
\]

and

\[
d_{n+1}=\frac{d_n}{2(1+c_{n+1})}.
\]

Then

\[
\frac{W_{n+1}}{W_n}
=
\frac{c_n}{2c_{n+1}^2(1+c_{n+1})}.
\]

Since

\[
2c_{n+1}^2=1+c_n,
\]

we obtain the exact formula

\[
\boxed{
\frac{W_{n+1}}{W_n}
=
\frac{c_n}{(1+c_n)(1+c_{n+1})}.
}
\]

## 8. Every finite step contracts the certified interval by strictly more than a factor four

For `0<c_n<1`, let

\[
t=c_{n+1}\in(0,1),
\]

so

\[
c_n=2t^2-1.
\]

We need to compare

\[
\frac{c_n}{(1+c_n)(1+t)}
\]

with `1/4`.

The inequality

\[
4c_n<(1+c_n)(1+t)
\]

is equivalent to

\[
4(2t^2-1)<2t^2(1+t).
\]

After rearrangement:

\[
0<2(t^3-3t^2+2).
\]

Factor:

\[
t^3-3t^2+2
=(t-1)(t^2-2t-2).
\]

For `0<t<1`, both factors are negative, so their product is positive.

Therefore

\[
\boxed{
0<\frac{W_{n+1}}{W_n}<\frac14
}
\]

for every finite `n>=1`.

This is stronger than an asymptotic convergence statement:

> each finite half-refinement shrinks the internally certified completion interval to strictly less than one quarter of its previous width.

## 9. Limiting contraction is exactly one quarter

Since

\[
c_n\to1,
\qquad
c_{n+1}\to1,
\]

the exact ratio formula gives

\[
\boxed{
\frac{W_{n+1}}{W_n}\to\frac14.
}
\]

Thus the finite interval contraction is always slightly better than fourfold and approaches the intrinsic quartering rate already proved for the actual lower error.

## 10. Gate indexing

In the six-gate cover notation with

\[
G_m=C_{3\cdot2^m},
\qquad m\ge3,
\]

and

\[
\Pi_m^{\rm gate,-}=\frac{|G_m|}{6}s_m,
\]

define

\[
\Pi_m^{\rm gate,+}
=
\frac{|G_m|}{6}\frac{s_m}{c_m}.
\]

Then

\[
\boxed{
\Pi_m^{\rm gate,-}<\Pi_{\rm rot}<\Pi_m^{\rm gate,+}
}
\]

and the gate interval width contracts by the same exact sub-quarter ratio.

Therefore one extra binary gate-cover bit yields **more than two bits of certified interval-width precision at every finite step**, asymptotically tending to exactly two bits per cover bit.

## 11. Classical polygon/trig interpretation is optional and later

After classical character identification one may recognize

\[
\Pi_n^-=N\sin(\pi/N),
\qquad
\Pi_n^+=N\tan(\pi/N)
\]

for the appropriate dyadic `N` indexing, reproducing the familiar inscribed/circumscribed polygon bracket.

But this is only a later compatibility interpretation.

The target-free proof above used only:

- the finite half-root recurrence;
- the Pythagorean unit-state relation;
- algebraic inequalities on `c_n`.

Thus the two-sided bracket is generated internally rather than imported from classical circle geometry.

## 12. Main consequence for #1158

The finite Viète state now certifies not only a point estimate but an intrinsic interval:

```text
finite half-angle state (c_n,s_n)
    -> lower readout Pi_n^-
    -> upper readout Pi_n^+=Pi_n^-/c_n
    -> exact bracket for Pi_rot
    -> width shrinks by < 1/4 every refinement
    -> classical compatibility later identifies Pi_rot=pi
```

This substantially strengthens the claim that precision is part of the generated mathematical state itself.
