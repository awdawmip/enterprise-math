# Gregory–Machin continuation: rational complementary turns, Pell near-half-turns, and the sharp two-factor completion infimum

Status: `FREE_RESEARCH / EXACT_RATIONAL_COMPLEMENT_THEOREM + PELL_FINITE_RESOLUTION_CHAIN + ANALYTIC_COST_INFIMUM / NOT_FOUNDATION`
Date: `2026-09-04`
Researcher: `EM-FREE-B2817C / FREE_AXIOM_DISCOVERY`
Issue: `#1160`
Checker: `research_notes/experiments/gregory_machin_rational_pell_halfturn_check_20260904.py`
Depends on: exact rational-turn group, relative-turn theorem, finite Farey refinement, fixed-compute completion-cost theorem.

## 1. Frontier

The preceding #1160 return proves a complete positive two-reciprocal split theorem for a primitive rational residual and blindly recovers the six-term `mu≈1.489121359...` identity.  Its explicit next frontier is to stop restricting the completion alphabet to integer reciprocal turns `[D+i]` and allow every primitive positive rational-slope turn

\[
V_{a,b}:=[b+ai],
\qquad 0<a<b,
\qquad \gcd(a,b)=1.
\]

This does **not** enlarge the native rational-turn group: these classes were already present in

\[
\mathcal T_{\mathbf Q}=\mathbf Q(i)^\times/\mathbf Q_{>0}^\times.
\]

What changes is only the preferred analytic completion alphabet.

Freeze:

`RATIONAL_GENERATOR_EXTENSION = COMPLETION_ALPHABET_EXTENSION`,

not

`NEW_NATIVE_TURN_CARRIER`.

The two-coordinate carrier remains a rotation certificate/readout and is not asserted to replace the P000 six-dimensional spatial substrate.

---

## 2. Exact complementary-turn involution

For an integer direction

\[
v=(b,a),\qquad 0<a<b,
\]

define its diagonal complement

\[
\boxed{C(v)=(b+a,b-a)}.
\]

Then raw Gaussian multiplication gives

\[
\begin{aligned}
(b+ai)\big((b+a)+(b-a)i\big)
&=b(b+a)-a(b-a)\\
&\qquad +\big(b(b-a)+a(b+a)\big)i\\
&=(a^2+b^2)(1+i).
\end{aligned}
\]

Therefore exactly in the positive-scale quotient,

\[
\boxed{[v][C(v)]=\tau},
\qquad \tau=[1+i].
\]

Also

\[
C(C(b,a))=(2b,2a),
\]

so after positive scale quotient

\[
\boxed{C^2=\mathrm{id}}.
\]

Thus every primitive rational direction produces an exact two-factor decomposition of the diagonal turn before any real angle is introduced.

After classical completion only,

\[
\boxed{
\frac\pi4
=\arctan\frac ab
+\arctan\frac{b-a}{b+a}.
}
\]

---

## 3. The exact rational half-diagonal turn is missing

A literal half-diagonal turn would be a class `h` with

\[
h^2=\tau.
\]

There are two equivalent native obstructions.

### 3.1 `C8` torsion obstruction

The already-proved valuation decomposition has a torsion coordinate

\[
C_8,
\]

with diagonal target `tau` in odd class `1 mod 8`.  A square has even torsion coordinate.  Hence

\[
2x\equiv1\pmod8
\]

has no solution.

Therefore

\[
\boxed{\tau\text{ has no square root in }\mathcal T_{\mathbf Q}.}
\]

### 3.2 Integer-direction obstruction

For `v=(b,a)`, equality of the two complementary projective directions would require

\[
[v]=[C(v)].
\]

Their determinant is

\[
\boxed{
Q(b,a):=\det(v,C(v))
=b^2-2ab-a^2.
}
\]

Thus an exact equality would require

\[
Q(b,a)=0.
\]

Dividing by `b^2` gives

\[
1-2(a/b)-(a/b)^2=0,
\]

whose positive root is

\[
\sqrt2-1,
\]

not rational.  Hence no nonzero integer direction realizes the missing half-turn.

This gives a finite arithmetic defect coordinate for the unavailable square root:

\[
\boxed{Q(v)=\det(v,C(v)).}
\]

---

## 4. Minimal nonzero defect is Pell/unimodular

Because `Q(v)` is an integer and zero is impossible, the smallest possible nonzero defect is

\[
\boxed{|Q(v)|=1.}
\]

But `Q(v)` is exactly the determinant of the complementary pair.  Therefore

\[
|Q(v)|=1
\]

means that `v` and `C(v)` are unimodular/Farey neighbors.

The near-half-turn problem has therefore reduced without real angle to the Pell-type equations

\[
\boxed{b^2-2ab-a^2=\pm1.}
\]

This is the integer minimum-resolution substitute for the unavailable equation `Q=0`.

No novelty is claimed for Pell equations or continued fractions.  The #1160 result is their forced appearance as the minimum determinant defect of the rational complementary-turn involution.

---

## 5. Complement-mediant Pell refinement chain

Start from

\[
v_0=(2,1)
\]

and recursively set

\[
\boxed{v_{n+1}=v_n+C(v_n)}.
\]

If

\[
v_n=(b_n,a_n),
\]

then

\[
\boxed{
(b_{n+1},a_{n+1})=(2b_n+a_n,b_n).
}
\]

This is not an arbitrary recurrence: `v_n+C(v_n)` is exactly the Farey mediant direction of the two complementary rays.

A second exact identity is

\[
C(v_{n+1})=2v_n+C(v_n).
\]

The determinant defect flips sign:

\[
\begin{aligned}
Q(v_{n+1})
&=(2b+a)^2-2(2b+a)b-b^2\\
&=-(b^2-2ab-a^2)\\
&=-Q(v_n).
\end{aligned}
\]

Since

\[
Q(v_0)=-1,
\]

one gets

\[
\boxed{Q(v_n)=(-1)^{n+1}.}
\]

Thus every stage remains a minimum-defect unimodular complementary pair.

The first states are

\[
\boxed{
(2,1),
(5,2),
(12,5),
(29,12),
(70,29),
(169,70),
(408,169),
(985,408),\ldots
}
\]

and their complementary partners begin

\[
(3,1),(7,3),(17,7),(41,17),(99,41),\ldots.
\]

---

## 6. Exact finite-resolution bracket for the missing half-turn

Put

\[
x=\frac ab,
\qquad
T(x)=\frac{1-x}{1+x}
=\frac{b-a}{b+a}.
\]

The complement map on slopes is the rational involution `T`.

Direct subtraction gives

\[
\boxed{
T(x)-x
=\frac{Q(b,a)}{b(b+a)}.
}
\]

Hence on the Pell chain,

\[
\boxed{
|T(x_n)-x_n|
=\frac1{b_n(b_n+a_n)}.
}
\]

The unique positive fixed point of `T` is determined only after solving

\[
x=T(x),
\]

namely

\[
x_*^2+2x_*-1=0,
\qquad
x_*=\sqrt2-1.
\]

Because `T` is decreasing, `x_n` and `T(x_n)` lie on opposite sides of its fixed point.  Therefore the exact rational interval with endpoints

\[
\frac{a_n}{b_n},
\qquad
\frac{b_n-a_n}{b_n+a_n}
\]

contains the unavailable balanced state, and its width is exactly

\[
\boxed{
\frac1{b_n(b_n+a_n)}.
}
\]

Since `b_{n+1}>2b_n`, these finite rational brackets shrink to zero.

This is a finite-resolution readout before any `arctan` is introduced:

\[
\boxed{
\text{missing rational half-turn}
\rightsquigarrow
\text{nested unimodular complementary brackets}.
}
\]

---

## 7. Exact approximation law

Let

\[
r=\sqrt2-1.
\]

Because

\[
Q(b,a)
=b^2\big(1-2(a/b)-(a/b)^2\big),
\]

and

\[
1-2x-x^2=-(x-r)(x+1+\sqrt2),
\]

the Pell states satisfy the exact error identity

\[
\boxed{
\frac{a_n}{b_n}-r
=-\frac{Q(v_n)}{b_n^2\left(a_n/b_n+1+\sqrt2\right)}.
}
\]

Consequently

\[
\left|\frac{a_n}{b_n}-r\right|
\sim \frac1{2\sqrt2\,b_n^2}.
\]

Thus one unit of determinant defect produces a quadratic-in-height slope error.

---

## 8. Generalized analytic completion cost

Only now attach the classical power-series readout.  For a primitive rational generator

\[
V_{a,b}=[b+ai],
\]

with `0<a<b`, define

\[
\Theta(V_{a,b})=\arctan(a/b).
\]

Its finite expansion is

\[
A_N(a,b)
=\sum_{j=0}^{N}
\frac{(-1)^j a^{2j+1}}{(2j+1)b^{2j+1}},
\]

and the standard alternating/integral remainder decays geometrically at rate

\[
(a/b)^{2N+3}.
\]

Therefore the fixed-compute theorem from the integer-reciprocal case extends simply by replacing denominator `D` by the ratio

\[
\rho=\frac ba.
\]

For a two-factor complementary diagonal decomposition define the generalized Lehmer cost

\[
\boxed{
\mu_{\rm gen}(x)
=\frac1{\log_{10}(1/x)}
+\frac1{\log_{10}(1/T(x))},
\qquad 0<x<1.
}
\]

This is a completion-layer resource coordinate, not a native angle.

---

## 9. Sharp global two-factor cost infimum

Set

\[
t=\ln(1/x),
\qquad
s=\ln(1/T(x)).
\]

A direct algebraic calculation gives

\[
\sinh t
=\frac{1-x^2}{2x},
\qquad
\sinh s
=\frac{2x}{1-x^2},
\]

hence

\[
\boxed{\sinh t\,\sinh s=1.}
\]

We need one elementary convexity lemma.

Define

\[
h(u)=\ln\sinh(e^u).
\]

Then

\[
h''(u)
=\frac{e^u\big(\sinh(e^u)\cosh(e^u)-e^u\big)}{\sinh^2(e^u)}>0
\]

because `sinh z cosh z > z` for `z>0`.

Therefore `h` is strictly convex.  Applying Jensen at `u=ln t` and `v=ln s` gives

\[
0
=\frac{h(\ln t)+h(\ln s)}2
\ge h\!\left(\ln\sqrt{ts}\right)
=\ln\sinh\sqrt{ts}.
\]

Thus

\[
\sqrt{ts}\le\operatorname{arsinh}(1)
=\ln(1+\sqrt2).
\]

Finally

\[
\frac1t+\frac1s
\ge\frac2{\sqrt{ts}}
\ge\frac2{\ln(1+\sqrt2)}.
\]

Multiplying by `ln 10` yields the sharp bound

\[
\boxed{
\mu_{\rm gen}(x)
\ge
\frac{2}{\log_{10}(1+\sqrt2)}
=:\mu_*.
}
\]

Numerically,

\[
\boxed{\mu_*\approx5.224992277747915.}
\]

Equality requires simultaneously `t=s`, equivalently

\[
x=T(x)=\sqrt2-1.
\]

Since this value is irrational, no primitive rational generator attains equality.

Therefore:

\[
\boxed{
\inf_{x\in\mathbf Q\cap(0,1)}\mu_{\rm gen}(x)
=\frac{2}{\log_{10}(1+\sqrt2)},
\quad\text{but the infimum is not attained.}
}
\]

The Pell complementary chain constructed above approaches the missing minimizer from finite integer data.

---

## 10. Quartic completion-cost convergence along the Pell chain

Write the natural-log cost

\[
G(x)=\frac1{\ln(1/x)}+
\frac1{\ln((1+x)/(1-x))}.
\]

At

\[
r=\sqrt2-1,
\qquad
\rho=\ln(1+\sqrt2),
\]

one has

\[
G'(r)=0
\]

and a direct differentiation gives

\[
\boxed{
G''(r)
=\frac{4-\sqrt2\,\rho}{r^2\rho^3}>0.
}
\]

The exact Pell error from Section 7 is `Theta(b_n^{-2})`.  Taylor expansion at the strict minimizer therefore yields

\[
\boxed{
\mu_{\rm gen}(x_n)-\mu_*
=\Theta(b_n^{-4}).
}
\]

More precisely,

\[
\boxed{
\mu_{\rm gen}(x_n)-\mu_*
\sim
\frac{\ln 10}{16}
\frac{4-\sqrt2\,\rho}{r^2\rho^3}
\frac1{b_n^4}.
}
\]

The asymptotic coefficient is approximately

\[
3.3733381167.
\]

Thus the minimum determinant defect is second-order in slope resolution and fourth-order in the analytic fixed-compute cost defect.

---

## 11. Relation to the existing Farey calculus

The Pell chain does not introduce a new global tool or a new primitive rotation law.

The exact step

\[
v_{n+1}=v_n+C(v_n)
\]

is the mediant operation already present in the #1160 Farey refinement theorem.  The new specialization is that the two endpoints are linked by the diagonal-complement involution, so the mediant refinement preserves the smallest possible nonzero determinant defect and flips its orientation sign.

Likewise, circuit/same-endpoint surgery remains covered by the existing `T3 Typed Incidence Circuit` family; this note does not claim a new circuit calculus.

Reuse classification:

- Farey mediant refinement: `REUSE_APPLIED`;
- relative-turn/complement certificate: `REUSE_APPLIED`;
- T3 circuit machinery: `NOT_NEEDED_FOR_THIS_TWO_FACTOR_THEOREM`;
- Pell/continued-fraction arithmetic: classical prior art, no novelty claim.

---

## 12. Semantic and optimization boundary

Allowing general primitive rational-slope atoms changes the **completion alphabet**.  Exact endpoint equality alone does not select a unique analytic cost because the same rational-turn element can admit different exact factorizations.

Freeze:

\[
\boxed{
\texttt{EXACT_ENDPOINT_GROUP}
\ne
\texttt{COMPLETION_COST_ALPHABET}.
}
\]

Therefore the integer-reciprocal record `mu≈1.489121359...` and a future generalized-rational record may be compared only after the allowed atom alphabet and normalization rules are declared.

The present theorem solves the complete **positive complementary two-factor** problem in the generalized alphabet and provides its sharp unattained cost infimum.  It does not assert global optimality among arbitrary signed multi-factor rational circuits.

---

## 13. Next frontier

The remaining nontrivial question is now sharply typed:

> In a declared primitive rational-slope alphabet, can a signed valuation circuit have generalized fixed-compute cost below the best integer-reciprocal circuit, and what finite height/norm normalization prevents mere representation changes from masquerading as algorithmic improvement?

A correct continuation must therefore keep three layers separate:

1. exact `C8 + Gaussian valuation` endpoint feasibility;
2. finite winding/lift certificate;
3. alphabet-relative analytic Pareto cost.

The Pell chain supplies the canonical two-factor calibration/negative control for that generalized search.
