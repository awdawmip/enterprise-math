# Free Research — Target-Free Wallis-to-Cauchy Completion

Status: `FREE_RESEARCH_FRONTIER / ANCHOR_EXPOSED / NOT_WORKING_TRUTH / NOT_FOUNDATION`
Date: `2026-09-04`
Parent: `FREE_RESEARCH_PI_PRIME_PROJECTIVE_RADIUS_C3_BRIDGE_20260904.md`
Dependency: #1159 exact rational `wallisPartial` and internal `wallisLimit`.

## 1. Goal

The projective-radius/C3 bridge reduced its remaining analytic normalization to

\[
\texttt{wallisLimit}
\stackrel{?}{=}
\int_0^\infty\frac{dx}{1+x^2}.
\]

The important requirement is to prove this without using a classical circle integral or a pre-known value of `pi`.

This note gives that proof by squeezing the Cauchy integral with the **same exact rational Wallis products** already formalized in #1159.

---

## WCI-T01 — Algebraic integral family

For `m>=0`, define

\[
\boxed{
I_m
:=\int_0^\infty
\left(\frac{x}{\sqrt{1+x^2}}\right)^m
\frac{dx}{1+x^2}.
}
\]

Equivalently,

\[
I_m
=\int_0^\infty
\frac{x^m}{(1+x^2)^{m/2+1}}\,dx.
\]

The base values are

\[
\boxed{
I_0=\int_0^\infty\frac{dx}{1+x^2},
\qquad
I_1=1.
}
\]

The second identity follows from

\[
\frac{d}{dx}(1+x^2)^{-1/2}
=-\frac{x}{(1+x^2)^{3/2}}.
\]

No trigonometric substitution is needed.

---

## WCI-T02 — Exact Wallis recurrence by integration by parts

For `m>=2`, differentiate

\[
F_m(x):=x^{m-1}(1+x^2)^{-m/2}.
\]

Then

\[
F_m'(x)
=(m-1)x^{m-2}(1+x^2)^{-m/2}
-mx^m(1+x^2)^{-m/2-1}.
\]

The boundary values of `F_m` at `0` and `infinity` vanish. Hence integration gives

\[
\boxed{
I_m=\frac{m-1}{m}I_{m-2}.
}
\]

Therefore, with

\[
A_n:=\prod_{k=1}^n\frac{2k-1}{2k},
\qquad
B_n:=\prod_{k=1}^n\frac{2k}{2k+1},
\]

we have

\[
\boxed{
I_{2n}=A_n I_0,
\qquad
I_{2n+1}=B_n.
}
\]

---

## WCI-T03 — Monotonicity gives the exact Wallis squeeze

For every `x>0`,

\[
0<\frac{x}{\sqrt{1+x^2}}<1.
\]

Thus

\[
\boxed{I_{m+1}<I_m.}
\]

In particular,

\[
I_{2n+1}<I_{2n}<I_{2n-1}.
\]

Using WCI-T02:

\[
B_n<A_n I_0<B_{n-1}.
\]

Divide by positive `A_n`:

\[
\frac{B_n}{A_n}
<I_0
<\frac{B_{n-1}}{A_n}.
\]

But

\[
\frac{B_n}{A_n}
=\prod_{k=1}^n
\frac{(2k)^2}{(2k-1)(2k+1)}
=\texttt{wallisPartial}(n)
=:W_n,
\]

and

\[
\frac{B_{n-1}}{A_n}
=W_n\frac{2n+1}{2n}.
\]

Hence for every `n>=1`,

\[
\boxed{
W_n
<I_0
<W_n\frac{2n+1}{2n}.
}
\]

This is a target-free finite squeeze. The relative upper gap is exactly `1/(2n)`.

---

## WCI-T04 — The Cauchy completion is the internal Wallis limit

Current #1159 Lean proves

\[
W_n\longrightarrow\texttt{wallisLimit}
\]

without primitive `pi` input.

Also

\[
\frac{2n+1}{2n}\longrightarrow1.
\]

Therefore the upper sequence in WCI-T03 has the same limit as `W_n`. By squeezing the constant `I_0`,

\[
\boxed{
I_0=\texttt{wallisLimit}.
}
\]

That is,

\[
\boxed{
\texttt{wallisLimit}
=\int_0^\infty\frac{dx}{1+x^2}.
}
\]

This theorem introduces the integral only as a **derived completion readout** and proves that it equals the already-internal rational Wallis completion. It does not use circumference, a circle spectrum, arctangent normalization, or the numerical value of `pi`.

---

## WCI-T05 — Internal tau normalization

The #1159/#1161 research packet uses the pi-like completion

\[
\tau=2\,\texttt{wallisLimit}.
\]

Combining WCI-T04 gives internally

\[
\boxed{
\tau
=2\int_0^\infty\frac{dx}{1+x^2}.
}
\]

Crucially, the direction of derivation is now

\[
\text{finite rational Wallis spectrum}
\to
\texttt{wallisLimit}
\to
\text{Cauchy integral readout},
\]

not `classical pi integral -> identify Wallis limit`.

---

## WCI-T06 — Close the projective-radius normalization

The projective-radius bridge proved, for `R_cell=1/sqrt(3)`,

\[
\mathcal O_3
=\frac{2R_{\rm cell}}3
\int_0^\infty\frac{du}{1+u^2}.
\]

WCI-T05 now gives

\[
\boxed{
\mathcal O_3
=\frac{\tau R_{\rm cell}}3
}
\]

**without importing a classical circle integral or arctangent value.**

Thus the `C3` orientation-series normalization is internally derived from the same target-free Wallis completion already present in #1159.

The prime Euler product at `s=1` still uses the standard Dirichlet analytic passage from the multiplicative character to its conditional Euler product, but the geometric normalization of its value no longer depends on external `pi` geometry.

---

## 7. Formalization target

This bridge is unusually well suited for Lean because the rational Wallis side is already green. A minimal formal route is:

1. define `cauchyWallisIntegral m` as an improper interval integral;
2. prove `I_1=1`;
3. prove the two-step recurrence by integration by parts;
4. prove strict decrease from the pointwise factor `x/sqrt(1+x^2)<1`;
5. identify `B_n/A_n` with existing `wallisPartial n`;
6. derive the finite squeeze;
7. use existing `wallisPartialReal_tendsto` to prove `I_0=wallisLimit`.

This should be stacked after #1172 rather than added to current `main` until the dependency lands.

---

## Current classification

- algebraic integral recurrence: `PROVED / ANALYTIC BUT TARGET-FREE`.
- Cauchy integral finite Wallis squeeze: `PROVED / TARGET-FREE`.
- `I_0=wallisLimit`: `PROVED GIVEN CURRENT #1159 LIMIT THEOREM`.
- `tau=2 I_0`: `INTERNAL COMPLETION CONSEQUENCE`.
- `O3=tau R_cell/3`: `NOW INTERNAL WALLIS/PROJECTIVE COMPLETION; NO CLASSICAL CIRCLE INPUT NEEDED`.
- Dirichlet prime Euler product at `s=1`: `ANALYTIC MULTIPLICATIVE COMPLETION STILL REQUIRED`.
