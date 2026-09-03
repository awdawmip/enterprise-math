# Viète–Wallis internal completion equality: Pi_rot = tau = 2 W_infinity before classical pi is named

Status: `FREE_RESEARCH / EXACT CROSS-FAMILY INTERNAL COMPLETION THEOREM / NOT_FOUNDATION`
Date: `2026-09-03`
Researcher: `EM-FREE-7D3C9A / FREE_AXIOM_DISCOVERY`
Issue: `#1158`
Cross-family source: `#1159` free-research result comment `5525992157`
Depends on:
- `research_notes/VIETE_TARGET_FREE_ROTATION_COMPLETION_CONSTANT_20260903.md`
- `research_notes/VIETE_INTRINSIC_QUARTERING_ASYMPTOTIC_20260903.md`

## 1. Two independently defined internal constants

#1158 defines, without classical `pi`, the finite radical sequence

\[
c_0=0,
\qquad
c_{n+1}=\sqrt{\frac{1+c_n}{2}},
\]

\[
s_n=\sqrt{1-c_n^2}>0,
\qquad
\Pi_n=2^{n+1}s_n,
\]

and proves the intrinsic completion

\[
\boxed{\Pi_{\rm rot}=\lim_{n\to\infty}\Pi_n.}
\]

Independently, #1159 defines the power-series rotation law

\[
S(x)=\sum_{j=0}^{\infty}\frac{(-1)^j x^{2j+1}}{(2j+1)!}
\]

from its finite determinant limit and lets `tau` be the first positive zero of `S`.

The same #1159 result proves internally:

\[
S(\tau/2)=1
\]

and for the exact rational Wallis partial products

\[
W_N=\prod_{r=1}^N\frac{(2r)^2}{(2r-1)(2r+1)},
\]

\[
\boxed{W_\infty=\tau/2.}
\]

No classical circumference value is used to define either `Pi_rot` or `tau`.

## 2. Internal cosine companion

Define

\[
C(x):=S'(x)
=\sum_{j=0}^{\infty}\frac{(-1)^j x^{2j}}{(2j)!}.
\]

The power-series laws used in #1159 give

\[
\boxed{S(x)^2+C(x)^2=1,}
\]

\[
\boxed{S(2x)=2S(x)C(x),}
\]

\[
\boxed{C(2x)=C(x)^2-S(x)^2=2C(x)^2-1.}
\]

These are internal analytic identities of the power-series completion. They are not introduced by naming `S` and `C` as classical trigonometric functions.

## 3. Quarter-turn seed at tau/2

#1159 proves

\[
S(\tau/2)=1.
\]

Using

\[
S^2+C^2=1,
\]

we get

\[
\boxed{C(\tau/2)=0.}
\]

Thus the internal power-series state at half of the first boundary-completion phase is exactly

\[
\boxed{(C(\tau/2),S(\tau/2))=(0,1),}
\]

which is the #1158 quarter-turn scalar seed `(c_0,s_0)`.

## 4. Positivity on the dyadic interval

Because `tau` is the first positive zero of `S` and `S'(0)=1`,

\[
S(x)>0
\]

for

\[
0<x<\tau.
\]

We also need

\[
C(x)>0
\]

for

\[
0<x<\tau/2.
\]

Suppose instead that some

\[
a\in(0,\tau/2)
\]

satisfies

\[
C(a)=0.
\]

Then `S(a)>0` and `S(a)^2+C(a)^2=1`, so

\[
S(a)=1.
\]

The doubling law gives

\[
S(2a)=2S(a)C(a)=0.
\]

But

\[
0<2a<\tau,
\]

contradicting the definition of `tau` as the first positive zero.

Therefore

\[
\boxed{C(x)>0\quad\text{for }0<x<\tau/2.}
\]

This positivity fixes the same identity-near branch used by the finite shortest-root / normalized equal-resultant #1158 refinement.

## 5. The #1158 nested-radical states are exactly dyadic samples of the #1159 internal rotation law

Define

\[
\widehat c_n
:=
C\left(\frac{\tau}{2^{n+1}}\right),
\]

\[
\widehat s_n
:=
S\left(\frac{\tau}{2^{n+1}}\right).
\]

At `n=0`, Section 3 gives

\[
(\widehat c_0,\widehat s_0)=(0,1)=(c_0,s_0).
\]

Now let

\[
x=\frac{\tau}{2^{n+2}}.
\]

Then

\[
2x=\frac{\tau}{2^{n+1}}.
\]

The doubling identity gives

\[
C(2x)=2C(x)^2-1.
\]

Hence

\[
C(x)^2
=
\frac{1+C(2x)}2.
\]

Since `C(x)>0`,

\[
\boxed{
\widehat c_{n+1}
=
\sqrt{\frac{1+\widehat c_n}{2}}.
}
\]

Likewise `S(x)>0` and `S^2+C^2=1`, so

\[
\widehat s_{n+1}
=
\sqrt{1-\widehat c_{n+1}^2}.
\]

Therefore the hatted sequence satisfies exactly the same initial state and deterministic positive half-root recurrence as the #1158 sequence.

By uniqueness of the recurrence:

\[
\boxed{
(c_n,s_n)
=
\left(
C\left(\frac{\tau}{2^{n+1}}\right),
S\left(\frac{\tau}{2^{n+1}}\right)
\right).
}
\]

This equality is internal to the two project-defined completion systems and does not use the name/classical value of `pi`.

## 6. Equality Pi_rot = tau

Using the exact state identification,

\[
\Pi_n
=
2^{n+1}
S\left(\frac{\tau}{2^{n+1}}\right).
\]

Set

\[
x_n=\frac{\tau}{2^{n+1}}.
\]

Then

\[
\Pi_n
=
\tau\frac{S(x_n)}{x_n}.
\]

From the defining power series,

\[
\frac{S(x)}x
=
1-\frac{x^2}{3!}+\frac{x^4}{5!}-\cdots
\longrightarrow1
\]

as `x->0`.

Therefore

\[
\Pi_n\longrightarrow\tau.
\]

But #1158 independently proves

\[
\Pi_n\longrightarrow\Pi_{\rm rot}.
\]

Uniqueness of limits gives the exact internal bridge

\[
\boxed{
\Pi_{\rm rot}=\tau.
}
\]

No classical `pi` is used in this equality proof.

## 7. Viète–Wallis equality before classical identification

#1159 proves

\[
W_\infty=\tau/2.
\]

Combining with

\[
\Pi_{\rm rot}=\tau
\]

gives

\[
\boxed{
\Pi_{\rm rot}=2W_\infty.
}
\]

Equivalently,

\[
\boxed{
\frac2{\Pi_{\rm rot}}
=
\frac1{W_\infty}.
}
\]

Since #1158 also proves

\[
\prod_{n=1}^{\infty}c_n
=
\frac2{\Pi_{\rm rot}},
\]

we obtain the direct internal infinite-product bridge

\[
\boxed{
\prod_{n=1}^{\infty}c_n
=
\frac1{W_\infty}
=
\prod_{r=1}^{\infty}\left(1-\frac1{4r^2}\right).
}
\]

The first product is the Viète half-root product; the second is the inverse Wallis product. Their equality is established through the common internal completion constant, not by first naming both as functions of classical `pi`.

## 8. Cross-family interpretation

The common internal structure is now:

```text
#1158 finite binary rotation refinement
    -> nested radical states
    -> intrinsic completion Pi_rot

#1159 finite determinant / parity spectrum
    -> power-series rotation law S
    -> first boundary phase tau
    -> Wallis limit W_inf=tau/2

internal half-phase/doubling bridge
    -> Pi_rot=tau
```

Thus Viète and Wallis are no longer merely numerically consistent or classically equivalent. They share the same project-internal boundary-completion constant before classical naming.

## 9. Relation to #1161 AGM

#1161 already proves that its local AGM cone update factors through the same #1158 normalized equal-resultant root, but its global completion equality with `tau` remains a separate open normalization identity

\[
A_\infty\tau=H_\infty^2.
\]

The theorem here does not close that AGM bridge. It does, however, reduce the internal target:

\[
\boxed{
\text{AGM completion} = \Pi_{\rm rot}
\iff
\text{AGM completion} = \tau.
}
\]

So #1158 and #1159 now provide one already-unified internal target for #1161.

## 10. Classical compatibility is strictly later

After this internal equality is established, a separate classical compatibility theorem may identify

\[
\tau=\pi.
\]

Then automatically

\[
\Pi_{\rm rot}=\pi,
\qquad
W_\infty=\pi/2.
\]

But none of these classical names were needed to prove

\[
\Pi_{\rm rot}=\tau=2W_\infty.
\]

## 11. Main consequence for #1158

The target-free completion constant produced by the Viète gate-refinement mechanism is not an isolated formula-specific artifact.

It is exactly the same internal rotation boundary-completion phase independently reconstructed by the Wallis finite spectral/determinant route.

Freeze at free-research-result strength:

`VIETE_INTERNAL_COMPLETION = WALLIS_INTERNAL_ROTATION_PHASE`.

`PI_ROT = TAU = 2 W_INFINITY`.

`CLASSICAL_PI_IDENTIFICATION = LATER COMPATIBILITY LAYER`.
