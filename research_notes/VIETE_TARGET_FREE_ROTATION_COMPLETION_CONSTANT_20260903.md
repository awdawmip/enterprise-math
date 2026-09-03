# Viète target-free completion: intrinsic rotation constant, finite radical brackets, and later identification with classical pi

Status: `FREE_RESEARCH / EXACT TARGET-FREE CONVERGENCE + FINITE BRACKET / CLASSICAL IDENTIFICATION SEPARATED / NOT_FOUNDATION`
Date: `2026-09-03`
Researcher: `EM-FREE-7D3C9A / FREE_AXIOM_DISCOVERY`
Issue: `#1158`
Parent: `research_notes/VIETE_SEGMENT_BISECTOR_ROTATION_PRECISION_20260903.md`

## 1. Why another convergence proof is needed

The earlier Viète note proved the exact finite recursion without using the target value of `pi`, then identified the finite readout with

\[
2^{n+1}\sin(\pi/2^{n+1})
\]

at the classical completion layer and used the small-angle limit to obtain convergence to `pi`.

That is sufficient for classical compatibility, but the causal separation can be made stronger:

> prove that the target-free algebraic sequence itself has a finite completion constant and a finite computable bracket before any use of trigonometry or the target value `pi`.

Only after that intrinsic constant is constructed should classical analysis identify it with classical `pi`.

## 2. Target-free recurrence

Use the exact post-quarter-turn scalar recurrence

\[
c_0=0,
\qquad
c_{n+1}=\sqrt{\frac{1+c_n}{2}},
\]

with the principal positive root.

Let

\[
s_n=\sqrt{1-c_n^2}>0
\]

and define

\[
\Pi_n=2^{n+1}s_n.
\]

The predecessor proves, entirely algebraically,

\[
\Pi_n=c_{n+1}\Pi_{n+1}
\]

and hence

\[
\Pi_{n+1}>\Pi_n.
\]

No target constant is used in these definitions.

## 3. Longitudinal defect contracts geometrically

Define

\[
d_n:=1-c_n.
\]

Rationalize the half-angle update:

\[
1-c_{n+1}
=
\frac{1-c_{n+1}^2}{1+c_{n+1}}
=
\frac{(1-c_n)/2}{1+c_{n+1}}.
\]

Therefore

\[
\boxed{
d_{n+1}=\frac{d_n}{2(1+c_{n+1})}.}
\]

Since `c_{n+1}>=0`,

\[
\boxed{0<d_{n+1}\le\frac12 d_n.}
\]

Thus

\[
d_n\le2^{-n}d_0=2^{-n}
\]

and, more importantly, every tail is summable:

\[
\sum_{j=m}^{\infty}d_j\le2d_m.
\]

This already proves

\[
c_n\to1
\]

without trigonometry.

## 4. Multiplicative increments of Pi_n

From

\[
\Pi_n=c_{n+1}\Pi_{n+1},
\]

one has

\[
\boxed{
\frac{\Pi_{n+1}}{\Pi_n}
=\frac1{c_{n+1}}
=\frac1{1-d_{n+1}}.
}
\]

For `0<=x<=1/2`,

\[
\frac1{1-x}\le1+2x.
\]

For `n>=1`, all tail defects `d_{n+1},d_{n+2},...` lie below `1/2`, so for `m>n`,

\[
\frac{\Pi_m}{\Pi_n}
\le
\prod_{j=n+1}^{m}(1+2d_j).
\]

## 5. Finite product bound without exp/log

For nonnegative numbers `a_j` with total sum `S<1`,

\[
\prod_j(1+a_j)\le\frac1{1-S}.
\]

Reason: expand the finite product into elementary symmetric sums. The degree-`k` symmetric sum is at most `S^k`, so the whole product is at most

\[
1+S+S^2+\cdots=\frac1{1-S}.
\]

Use

\[
a_j=2d_j.
\]

The geometric defect bound gives

\[
S_n:=\sum_{j=n+1}^{\infty}2d_j
\le4d_{n+1}.
\]

For `n>=1`,

\[
d_{n+1}\le d_2\le\frac12d_1<\frac14,
\]

so

\[
4d_{n+1}<1.
\]

Hence

\[
\boxed{
\frac{\Pi_m}{\Pi_n}
\le
\frac1{1-4d_{n+1}}
}
\]

for every `m>n>=1`.

## 6. Intrinsic completion constant exists before classical pi

The sequence `Pi_n` is strictly increasing and, by the previous bound, bounded above for every fixed `n>=1`.

Therefore the finite limit exists:

\[
\boxed{
\Pi_{\mathrm{rot}}
:=
\lim_{n\to\infty}\Pi_n
<\infty.
}
\]

This is an **intrinsic rotation-refinement completion constant** defined by the target-free nested-radical mechanism itself.

No numerical value of classical `pi`, no circumference, no sine/cosine function, and no continuous circle is required to define or prove existence of `Pi_rot`.

Freeze:

`PI_ROT_DEFINED_BY_TARGET_FREE_REFINEMENT_LIMIT`.

`CLASSICAL_PI_NOT_USED_TO_DEFINE_PI_ROT`.

## 7. Finite target-free bracket

Passing `m->infinity` in the finite product bound gives, for every `n>=1`,

\[
\boxed{
\Pi_n
\le
\Pi_{\mathrm{rot}}
\le
\frac{\Pi_n}{1-4d_{n+1}}.
}
\]

Equivalently,

\[
\boxed{
0
\le
\Pi_{\mathrm{rot}}-\Pi_n
\le
\Pi_n\frac{4d_{n+1}}{1-4d_{n+1}}.
}
\]

Every quantity on the right is generated from the current finite radical state. Thus the mechanism certifies its own completion precision without consulting the target value it will later be shown to recover.

This bound is not asymptotically sharp; its role is to prove target-free completion and provide a simple explicit finite certificate.

## 8. Infinite product is now a consequence of the intrinsic constant

The exact finite identity from the predecessor is

\[
P_n=\prod_{k=1}^{n}c_k=\frac{2}{\Pi_n}.
\]

Because

\[
\Pi_n\to\Pi_{\mathrm{rot}}>0,
\]

it follows that

\[
\boxed{
\prod_{k=1}^{\infty}c_k
=\frac{2}{\Pi_{\mathrm{rot}}}.
}
\]

So the Viète product is first a theorem about the intrinsic completion constant of the rotation-refinement system.

## 9. Classical compatibility is a later identification theorem

Only after `Pi_rot` has been constructed independently add the classical rotation-character calibration

\[
(c_n,s_n)
=
\left(
\cos\frac{\pi}{2^{n+1}},
\sin\frac{\pi}{2^{n+1}}
\right).
\]

Then

\[
\Pi_n
=
2^{n+1}\sin\frac{\pi}{2^{n+1}}.
\]

Classical analysis gives

\[
\Pi_n\to\pi.
\]

Limits are unique, hence

\[
\boxed{
\Pi_{\mathrm{rot}}=\pi.
}
\]

The logical direction is now explicit:

```text
target-free finite refinement
    -> monotone finite readouts
    -> target-free finite completion constant Pi_rot
    -> finite radical self-brackets for Pi_rot
    -> classical compatibility theorem
    -> Pi_rot = classical pi
```

This is stronger than defining the sequence from known trigonometric values and observing convergence.

## 10. Reinterpretation of Viète's product

The classical statement

\[
\frac2\pi
=
\frac{\sqrt2}{2}
\frac{\sqrt{2+\sqrt2}}2
\frac{\sqrt{2+\sqrt{2+\sqrt2}}}2\cdots
\]

can now be typed as two theorems:

1. **Enterprise-internal completion theorem**

\[
\frac2{\Pi_{\mathrm{rot}}}
=
\prod_{k=1}^{\infty}c_k,
\]

where `Pi_rot` is generated and bounded without the target classical constant;

2. **classical compatibility theorem**

\[
\Pi_{\mathrm{rot}}=\pi.
\]

This separation removes target leakage from the generative mechanism.

## 11. Precision meaning

At finite depth the pair

\[
\left(
\Pi_n,
\frac{\Pi_n}{1-4d_{n+1}}
\right)
\]

is an intrinsic precision interval for `Pi_rot`.

After classical identification the same pair is a valid interval for classical `pi`, but its construction did not require `pi` as an input.

Therefore finite precision is part of the generated state:

- `Pi_n` is the current lower readout;
- `d_{n+1}` is an internally generated unresolved-orientation defect;
- together they certify a finite completion interval.

This is closer to the project ontology “precision is part of the number itself” than an externally attached decimal error estimate.

## 12. Boundary

This theorem still lives at the algebraic orientation-readout/completion layer. It does not prove that current G0 Cell dynamics uniquely generates the normalized-bisector law.

What it does prove is that once the finite refinement law is declared, **neither convergence nor finite precision certification needs classical pi or a continuous circle**.

The remaining native question is therefore about the source of the refinement law, not about the existence or calibration of its completion constant.
