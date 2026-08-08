# P018 — Finite-Precision Proof Calculus, Supplement 01

Status: `ACTIVE RESEARCH NOTE`  
Scope: scale degree, graded transport, homogeneous nonlinear precision defects  
Depends on: `docs/PRECISION_CALCULUS.en.md`  
Discipline: graded algebra is established mathematics; this note studies its interaction with finite many-to-one precision projection.

## 1. Why precision needs a degree

Stage 1 treated ordinary numerical/root states as scale-degree-one quantities.  If precision changes by a ratio

\[
r=e/d,
\]

then the canonical transported coarse state is

\[
a\mapsto ra.
\]

But not every mathematical quantity scales that way.

- a state or root state has scale degree `1`;
- a product of two degree-one states has scale degree `2`;
- a `p`-th power has scale degree `p`;
- a product of a degree-`q` and degree-`s` quantity has degree `q+s`.

Therefore a single projection rule `//r` is not type-correct for every quantity.  A degree-`q` quantity must be transported by `r^q` and projected by integer division by `r^q`.

This is ordinary graded thinking applied to the precision coordinate.  Graded rings and the rule that multiplication adds degree are established mathematics; P018 does not claim that idea as new.

## 2. P018-T13 — Degree-q precision fiber

Status: `PROVED`

For a nonnegative scale degree `q`, define

\[
\tau^{(q)}_{d\to e}(a)=r^q a,
\qquad
\pi^{(q)}_{e\to d}(x)=x\operatorname{//}r^q,
\]

and

\[
\delta^{(q)}_{e:d}(x)=x\bmod r^q.
\]

Then every degree-`q` fine quantity has the unique decomposition

\[
\boxed{
x
=r^q\pi^{(q)}_{e\to d}(x)
+
\delta^{(q)}_{e:d}(x),
\qquad
0\le\delta^{(q)}_{e:d}(x)<r^q.
}
\]

For `q=1`, this is P018-T01.  For `q=p`, it is the correct output projection used by the stage-1 collapse/refinement recovery map.

The degree is therefore part of the mathematical type of a scale-dependent quantity: the same fine integer can project to different coarse integers depending on its scale degree.

## 3. P018-T14 — Graded transport laws

Status: `PROVED / ESTABLISHED GRADED PATTERN`

For equal-degree quantities,

\[
\boxed{
\tau^{(q)}(a+b)
=
\tau^{(q)}(a)+\tau^{(q)}(b).
}
\]

For quantities of degrees `q` and `s`,

\[
\boxed{
\tau^{(q+s)}(ab)
=
\tau^{(q)}(a)\tau^{(s)}(b).
}
\]

Proofs are immediate from powers of `r`.

This exact transport law is not the difficult part.  The interesting structure appears after applying the many-to-one coarse projection: floor projection need not preserve nonlinear multiplication, so a finite defect/carry is created.

## 4. P018-T15 — Degree-q transported Möbius shell

Status: `PROVED`

For an integer-valued quantity `A(c)` of scale degree `q`, define

\[
\boxed{
\widehat A_q(d)
=
\sum_{c\mid d}
\mu(d/c)
\left(\frac dc\right)^q A(c).
}
\]

Then

\[
\boxed{
A(d)
=
\sum_{c\mid d}
\left(\frac dc\right)^q
\widehat A_q(c).
}
\]

The proof is the same divisor-poset Möbius inversion as P018-T07, with the scale transport replaced by degree-`q` transport.

### Homogeneous bulk annihilation

If

\[
A(c)=c^q A(1),
\]

then for every `d>1`,

\[
\boxed{
\widehat A_q(d)=0.
}
\]

Thus the stage-1 shell is only the degree-one member of a graded shell family.  A pure homogeneous scale law of the correct degree is invisible to every nontrivial shell; only failure of exact homogeneous transport remains.

## 5. Homogeneous monomials

Let

\[
M(x_1,\ldots,x_m)
=
\prod_{i=1}^m x_i^{\alpha_i},
\]

where each input has scale degree one and

\[
q=\sum_i\alpha_i>0.
\]

Write each fine input as

\[
x_i=ra_i+u_i,
\qquad
0\le u_i<r.
\]

The exact transported coarse monomial is

\[
r^q M(a_1,\ldots,a_m).
\]

The fine monomial is generally larger because the details `u_i` interact nonlinearly.

## 6. P018-T16 — Monomial precision-defect bound

Status: `PROVED`

Define the recovered coarse monomial

\[
\mathcal R_M
=
\left\lfloor
\frac{M(x_1,\ldots,x_m)}{r^q}
\right\rfloor
\]

and its **precision naturality defect**

\[
D_M
=
\mathcal R_M-M(a_1,\ldots,a_m).
\]

Then

\[
\boxed{D_M\ge0.}
\]

Moreover,

\[
\boxed{
D_M
\le
M(a_1+1,\ldots,a_m+1)
-
M(a_1,\ldots,a_m)
-1.
}
\]

Proof: since

\[
ra_i\le x_i<r(a_i+1),
\]

homogeneity gives

\[
r^qM(a)
\le
M(x)
<
r^qM(a+\mathbf 1).
\]

Divide by `r^q` with integer floor projection. ∎

Finally, there is a unique output detail `rho` with

\[
\boxed{
M(x)
=
r^q\bigl(M(a)+D_M\bigr)+\rho,
\qquad
0\le\rho<r^q.
}
\]

The defect `D_M` is therefore not an approximation error.  It is the exact number of coarse degree-`q` cells crossed by nonlinear interaction of fine details.

## 7. P018-T17 — Multiplication precision carry

Status: `PROVED`

For two degree-one states

\[
x=rA+u,
\qquad
y=rB+v,
\]

multiplication has degree two.  The degree-two coarse recovery is

\[
\left\lfloor\frac{xy}{r^2}\right\rfloor
=AB+C_\times,
\]

where

\[
\boxed{
C_\times
=
\left\lfloor
\frac{rAv+rBu+uv}{r^2}
\right\rfloor.
}
\]

The carry satisfies the sharp cell bound

\[
\boxed{
0\le C_\times\le A+B.
}
\]

Indeed, T16 specializes to

\[
(A+1)(B+1)-AB-1=A+B.
\]

There is also a unique product detail

\[
0\le\rho_\times<r^2
\]

such that

\[
\boxed{
xy=r^2(AB+C_\times)+\rho_\times.
}
\]

This is the multiplicative analogue of the binary addition carry from P018-T04, but it is no longer binary because a nonlinear degree-two output may cross several coarse product cells.

## 8. P018-T18 — Power precision carry

Status: `PROVED`

For

\[
x=rk+u,
\qquad0\le u<r,
\]

the map `x -> x^p` has degree `p`.  Define

\[
C_p^{\mathrm{prec}}
=
\left\lfloor\frac{x^p}{r^p}\right\rfloor-k^p.
\]

Then

\[
\boxed{
0\le C_p^{\mathrm{prec}}
\le
(k+1)^p-k^p-1.
}
\]

So the exact same basin-width expression that controls perfect-power collapse also controls the precision carry of the ordinary `p`-th-power map.

This is not accidental: a coarse perfect-power basin is exactly the range of degree-`p` coarse cells that can be reached by varying the degree-one detail inside a single root fiber.

## 9. P018-T19 — Monomial refinement recovery is monotone

Status: `PROVED`

Let

\[
d\mid e\mid f
\]

and let a collection of degree-one fine states at precision `f` project compatibly to precision `e` and `d`.

For a homogeneous monomial `M` of total degree `q`, define its recovery at base precision `d` from an intermediate precision `e` by

\[
\mathcal R_{M;e\to d}
=
\pi^{(q)}_{e\to d}
\bigl(M(x_e)\bigr).
\]

Then

\[
\boxed{
\mathcal R_{M;e\to d}
\le
\mathcal R_{M;f\to d}.
}
\]

Proof: each component satisfies

\[
x_f=sx_e+u_i\ge sx_e,
\qquad s=f/e.
\]

Therefore homogeneity and nonnegative exponents give

\[
M(x_f)\ge s^qM(x_e).
\]

Degree-`q` projection to `d` preserves the inequality. ∎

Thus stage-1 monotone collapse recovery is part of a more general rule: **nonnegative homogeneous monomials recover coarse structure monotonically as finite input precision increases.**

## 10. P018-T20 — Collapse defect is root power carry

Status: `PROVED`

Stage 1 defined

\[
S_{p,d}(n)=R_p(nd^p)
\]

and the collapse/refinement defect

\[
\chi_{p;e:d}(n)
=
\left\lfloor
\frac{S_{p,e}(n)^p}{(e/d)^p}
\right\rfloor
-
S_{p,d}(n)^p.
\]

P018-T09 gives

\[
S_{p,e}(n)
=rS_{p,d}(n)+\eta,
\qquad0\le\eta<r.
\]

Substituting this into P018-T18 shows immediately that

\[
\boxed{
\chi_{p;e:d}(n)
=
C_p^{\mathrm{prec}}
\bigl(S_{p,e}(n);d,e\bigr).
}
\]

In words:

> the apparent noncommutation between collapse and precision refinement is exactly the ordinary degree-`p` precision carry produced when the root-detail fiber is passed through the `p`-th-power map.

This removes one special-purpose object from the theory.  Stage-1 collapse recovery is now a direct instance of the graded nonlinear precision-defect calculus.

## 11. Structural interpretation

Stage 2 separates two maps that should not be confused.

### Exact refinement transport

\[
\tau^{(q)}_{d\to e}(a)=r^qa
\]

is algebraically exact and respects the grading.

### Many-to-one coarse projection

\[
\pi^{(q)}_{e\to d}(x)=x//r^q
\]

forgets the bounded degree-`q` detail.

Linear equal-degree addition behaves exactly under both operations except for the already known addition carry generated by input details.  Nonlinear homogeneous maps produce a larger but still finite naturality defect whose size is controlled by the image width of one coarse input cell.

This suggests a general P018 program:

\[
\boxed{
\text{exact graded transport}
+
\text{many-to-one projection}
+
\text{bounded naturality defect}.
}
\]

The defect, rather than an external error estimate, is the internal finite object that measures how much nonlinear structure becomes visible when precision increases.

## 12. Counterexample / boundary: projection is not a graded homomorphism

It is tempting to infer from exact graded transport that the coarse floor projection also preserves multiplication:

\[
\pi^{(2)}(xy)
\stackrel{?}{=}
\pi^{(1)}(x)\pi^{(1)}(y).
\]

This is false whenever `C_x` is nonzero.

For example, with ratio `r=10`,

\[
x=y=19,
\]

we have

\[
\pi^{(1)}(19)=1,
\qquad
\pi^{(2)}(19^2)=361//100=3.
\]

The multiplication precision carry is `2`.

Therefore the correct graded structure belongs to **transport**; projection is many-to-one and has a controlled finite defect.

## 13. Prior-art boundary

Graded rings/algebras and the principle that homogeneous multiplication adds degree are established mathematics.  P018 uses that language rather than claiming a new grading concept.

The project-specific stage-2 question is whether the scale degree attached to finite precision states gives a useful calculus in which:

- the appropriate coarse projection depends on degree;
- homogeneous bulk is removed by degree-aware transported Möbius shells;
- nonlinear operations create exact finite cell-crossing defects;
- those defects are monotone under compatible refinement;
- root/collapse precision dynamics become instances of one generic homogeneous map law.

Historical novelty of this combination remains `NOVELTY_UNVERIFIED`.

## 14. Stage-2 status

- P018-T13 degree-q precision fiber: `PROVED`
- P018-T14 graded transport laws: `PROVED`
- P018-T15 degree-q transported shell + homogeneous bulk annihilation: `PROVED`
- P018-T16 monomial precision-defect bound: `PROVED`
- P018-T17 multiplication precision carry: `PROVED`
- P018-T18 power precision carry: `PROVED`
- P018-T19 monomial recovery monotonicity: `PROVED`
- P018-T20 collapse defect = root power carry: `PROVED`
- arbitrary homogeneous polynomial defect calculus: `OPEN`
- general operation/predicate naturality formalism: `OPEN`
- exact P017 reinterpretation: `OPEN`

Executable checks live in `src/enterprise_math/graded_precision.py` and `tests/test_graded_precision.py`.
