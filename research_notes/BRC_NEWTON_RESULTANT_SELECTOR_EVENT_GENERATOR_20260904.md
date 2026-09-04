# BRC exact resultant selector-event generator

Date: 2026-09-04
Mode: TASK_RESEARCH
Status: research candidate; no Foundation promotion in this note
Parent: one-parameter selector event theorem and exact chamber compiler line

## 1. Goal

The one-parameter selector event theorem says that a polynomial whose real zero set contains all degree-drop, multiple-root, and endpoint-crossing parameters is enough to partition the parameter line into selector-constant intervals.

The remaining manual step is constructing that event polynomial from the family itself.

This note gives an exact universal construction for polynomial coefficient families over one rational parameter.

Resultants and discriminants are classical prior art.  No generic elimination-theory novelty is claimed.

## 2. Polynomial family

Let

\[
P_t(x)=\sum_{j=0}^{d}a_j(t)x^j,
\qquad
a_j(t)\in\mathbb Q[t],
\]

with nominal degree `d>=1` and nonzero leading coefficient polynomial `a_d(t)`.

Fix a rational selector probe `r`.

Let

\[
P_x=\frac{\partial P_t}{\partial x}.
\]

## 3. Resultant event factor

Define

\[
\boxed{
R_P(t)=\operatorname{Res}_x(P_t,P_x).
}
\]

For every specialization `t=t0`, the nominal Sylvester resultant vanishes whenever:

1. the specialization loses nominal degree;
2. the specialized polynomial has a multiple finite root.

Thus `R_P` simultaneously covers the leading-degree event and the discriminant event.

When the nominal leading coefficient is nonzero at `t0`, the familiar relation is

\[
\operatorname{Disc}_x(P_t)
=
(-1)^{d(d-1)/2}
\frac{R_P(t)}{a_d(t)}.
\]

The resultant form is preferable for the event compiler because it avoids polynomial division by `a_d(t)` and continues to vanish at degree drops.

## 4. Smallest-real generated event polynomial

For a fixed rational declared root/probe `r`, define

\[
\boxed{
E_{\rm real}(t)
=
R_P(t)\,P_t(r).
}
\]

Every smallest-real selector transition is contained in

\[
Z_{\mathbb R}(E_{\rm real}).
\]

The two factors cover:

- topology/order changes of the root set (`R_P=0`);
- a real root crossing the declared probe (`P_t(r)=0`).

Hence selector/root-rank is constant on every connected interval where `E_real` is nonzero.

## 5. Smallest-positive generated event polynomial

For `r>0`, define

\[
\boxed{
E_+(t)
=
R_P(t)\,P_t(r)\,P_t(0).
}
\]

The extra `P_t(0)` factor detects roots crossing zero, which changes positive/non-positive status even when no root crosses the declared `r`.

Every smallest-positive selector transition lies in the real zero set of `E_+`.

## 6. Generic repeated-factor boundary

If

\[
R_P(t)\equiv0
\]

as a polynomial in `t`, then `P_t` and `P_x` have a common factor over the rational function field `Q(t)`.  The family is generically non-squarefree in `x`.

In that case the event generator does not yield a finite exceptional set.  One must first pass to an appropriate generic squarefree competing-root carrier or otherwise separate the persistent repeated factor.

Therefore the executable one-parameter event pipeline assumes

\[
\boxed{R_P\not\equiv0.}
\]

## 7. Exact Sylvester implementation

No external CAS is required for the research implementation.

Represent every `a_j(t)` as a finite rational polynomial in `t`.  Build the standard Sylvester matrix of `P_t` and `P_x`, whose entries lie in `Q[t]`.

Its size is

\[
2d-1.
\]

The checker evaluates its determinant by subset dynamic programming over column assignments.  This is exponential in nominal degree and is **reference-grade**, not a runtime complexity claim.

The output is an exact polynomial in `Q[t]`.

## 8. Degree-drop witness

Take

\[
P_t(x)=t x^2+x+1.
\]

The quadratic discriminant is

\[
1-4t.
\]

The exact resultant is

\[
\boxed{
R_P(t)=t(4t-1).
}
\]

Thus:

- `t=1/4` is the ordinary double-root event;
- `t=0` is a nominal degree-drop event, even though the specialized linear polynomial has a simple finite root.

This demonstrates why `Res(P,P_x)` is the correct single event factor rather than the discriminant alone.

## 9. Low-degree exact recoveries

### Quadratic witness

For

\[
P_t(x)=x^2+t x+1,
\]

\[
\boxed{R_P(t)=4-t^2.}
\]

Multiplying by `P_t(-1)=2-t` or `P_t(1)=t+2` gives the smallest-real or smallest-positive event polynomial.  After squarefree reduction the real event roots are exactly `-2,2`.

### Depressed cubic

For

\[
P_t(x)=x^3-3x+t,
\]

\[
\boxed{R_P(t)=27(t^2-4).}
\]

The generated smallest-real event at `r=-2` again has real roots `-2,2` after squarefree reduction.

### One-real cubic

For

\[
P_t(x)=x^3+x+t,
\]

\[
\boxed{R_P(t)=4+27t^2.}
\]

This resultant has no real zero.  For smallest-positive selection at `r=1`, the only real generated events come from

\[
P_t(1)=t+2,
\qquad
P_t(0)=t,
\]

hence exactly `-2,0`.

## 10. Degree-five product witness

Let

\[
F(x)=(x^2+1)(x^2-x-1),
\qquad
P_t(x)=F(x)(x-t).
\]

The fixed factor `F` is squarefree.  By the product discriminant/resultant law,

\[
R_P(t)
=C\,F(t)^2
\]

for a nonzero rational constant `C`.

Therefore

\[
\boxed{
R_P(t)
=C(t^2+1)^2(t^2-t-1)^2.
}
\]

For smallest-positive selection at `r=1`,

\[
P_t(1)\propto(t-1),
\qquad
P_t(0)\propto t.
\]

Thus the generated event polynomial has real zeros

\[
\frac{1-\sqrt5}{2},\quad0,\quad1,\quad\frac{1+\sqrt5}{2},
\]

exactly matching the hand-supplied event polynomial used by the chamber compiler.

## 11. Exact event pipeline

For a generically squarefree one-parameter family the complete research pipeline is now

\[
\boxed{
P_t(x)
\xrightarrow{\operatorname{Res}(P,P_x)}
E(t)
\xrightarrow{\text{Sturm isolation}}
\text{event cells}
\xrightarrow{\text{one pointwise selector sample/cell}}
\text{exact chamber labels}.
}
\]

No root formula, floating discriminant evaluation, or numerical continuation is required.

## 12. Hard boundaries

- RESULTANT_EVENT_SET is a boundary superset, not the minimal selector boundary.
- The implementation is one-parameter and reference-grade; it is not a high-degree fast resultant engine.
- `R_P identically zero` requires generic squarefree preprocessing and is outside the direct compiler.
- A generated event polynomial does not by itself define selector behavior exactly on event roots.
- Multi-parameter connected-component computation remains a separate semi-algebraic geometry problem.
- No complete Puiseux solver, generic multi-generator algebraic field, signed branch interference, or infinite-state claim is made.
