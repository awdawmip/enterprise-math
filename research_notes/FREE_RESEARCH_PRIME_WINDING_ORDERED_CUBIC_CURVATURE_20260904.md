# Free Research — Ordered Cubic Curvature of the Prime-Winding Quotient Cloud

Status: `FREE_RESEARCH_FRONTIER / EXACT_DEGREE_THREE_POLARIZATION_CLOSED / ORDERED_PROVENANCE_NECESSARY / NATIVE_RATE_OPEN / NOT_WORKING_TRUTH / NOT_FOUNDATION / EXTERNAL_NOVELTY_UNVERIFIED`
Date: `2026-09-04`
Parent: `FREE_RESEARCH_PI_PRIME_GEOMETRY_FRONTIER_V5_20260904.md`

## 1. Executive advance

The V5 mother question asked whether the weighted quotient-cloud variance can be dominated by a positive degree-three provenance energy.

The answer is stronger than a one-sided comparison:

\[
\boxed{
\text{the quotient-cloud variance is exactly the antisymmetric square norm of an ordered cubic history tensor.}
}
\]

The equality holds for every finite action family and every real field.  No asymptotic input, prime-number theorem, or analytic completion is used.

The crucial restriction is that the three-history packet must retain its ordered first intermediate vertex until after polarization.  Full product-label recoalescence erases precisely the component carrying the variance.

---

## 2. Setup

For an action label `a>=1`, let

\[
q_a(n)=\left\lfloor\frac na\right\rfloor,
\qquad
\delta_a f(n)=f(n)+f(q_a(n)).
\]

The quotient actions commute and compose:

\[
q_bq_a=q_{ab}.
\]

Let `S` be a finite action set, let `u_a>=0`, and write

\[
U=\sum_{a\in S}u_a>0.
\]

For fixed `n`, set

\[
x_a=f(q_a(n)),
\qquad
\bar x=U^{-1}\sum_a u_ax_a.
\]

The weighted quotient-cloud variance is

\[
\Gamma_S(f;n)
:=\sum_a u_a|x_a-\bar x|^2
=\frac1{2U}\sum_{a,b}u_au_b|x_a-x_b|^2.
\tag{2.1}
\]

For the prime-winding specialization,

\[
S=S_Y=\{a\le Y:a\text{ is a prime power}\},
\qquad
u_a=\frac{\Lambda(a)}a.
\]

---

## OCC-T01 — Common-suffix curvature cancellation

For ordered labels `a,b` and a common closing label `c`, define

\[
\boxed{
\Omega_{a,b\mid c}(f;n)
:=\delta_{bc}f(q_a(n))-\delta_{ac}f(q_b(n)).
}
\tag{3.1}
\]

Both signless edges terminate at the same recoalesced endpoint:

\[
q_{bc}(q_a(n))=q_{abc}(n)=q_{ac}(q_b(n)).
\]

Therefore that endpoint cancels exactly and

\[
\boxed{
\Omega_{a,b\mid c}(f;n)=f(q_a(n))-f(q_b(n))=x_a-x_b.
}
\tag{3.2}
\]

Consequences:

\[
\Omega_{b,a\mid c}=-\Omega_{a,b\mid c},
\tag{3.3}
\]

\[
\Omega_{a,b\mid c}+\Omega_{b,d\mid c}+\Omega_{d,a\mid c}=0,
\tag{3.4}
\]

and the curvature is independent of the common suffix label:

\[
\boxed{
\Omega_{a,b\mid c}=\Omega_{a,b\mid d}
}
\tag{3.5}
\]

for all `c,d`.

Thus the quotient-cloud difference is an exact ordered-history cocycle represented at degree three.

---

## OCC-T02 — Exact cubic polarization of the cloud variance

Define the positive ordered cubic curvature energy

\[
\mathcal C_{3,S}(f;n)
:=\sum_{a,b,c\in S}
 u_au_bu_c\,|\Omega_{a,b\mid c}(f;n)|^2.
\tag{4.1}
\]

Using OCC-T01,

\[
\mathcal C_{3,S}(f;n)
=U\sum_{a,b}u_au_b|x_a-x_b|^2.
\]

Combining this with (2.1) gives the exact identity

\[
\boxed{
\mathcal C_{3,S}(f;n)=2U^2\Gamma_S(f;n).
}
\tag{4.2}
\]

Equivalently,

\[
\boxed{
\Gamma_S(f;n)
=\frac1{2U^2}
\sum_{a,b,c\in S}
 u_au_bu_c
\left|
\delta_{bc}f(q_a(n))-\delta_{ac}f(q_b(n))
\right|^2.
}
\tag{4.3}
\]

This closes the V5 comparison target with equality rather than merely

\[
\Gamma\le C\mathcal P_3.
\]

The identity is uniform in `n`, in the cutoff, and in the positive weights.  In particular it is valid at `Y=sqrt(n)`.  Some closing triples may reach the absorbing state `0`; this does not affect the identity because the common endpoint cancels before squaring.

---

## OCC-T03 — Hodge polarization of the transported edge tensor

Define the ordered transported signless-edge tensor

\[
A_f(a,b,c;n)
:=\delta_{bc}f(q_a(n))
=x_a+f(q_{abc}(n)).
\tag{5.1}
\]

Let the transposition `tau` exchange `a` and `b`, and let

\[
A_f^-:=\frac12(A_f-\tau A_f).
\]

The common endpoint is symmetric under `a<->b`, hence

\[
\boxed{
A_f^-(a,b,c;n)=\frac{x_a-x_b}{2}.
}
\tag{5.2}
\]

With the weighted tensor norm

\[
\|A\|_u^2
:=\sum_{a,b,c}u_au_bu_c|A(a,b,c)|^2,
\]

one obtains

\[
\boxed{
\Gamma_S(f;n)=\frac{2}{U^2}\|A_f^-\|_u^2.
}
\tag{5.3}
\]

Because the swap is unitary for the symmetric product weights,

\[
\|A_f\|_u^2=\|A_f^+\|_u^2+\|A_f^-\|_u^2.
\]

Therefore

\[
\boxed{
\Gamma_S(f;n)
\le\frac{2}{U^2}
\sum_{a,b,c}u_au_bu_c
|\delta_{bc}f(q_a(n))|^2.
}
\tag{5.4}
\]

This is the requested positive unpolarized degree-three domination.  The sharper statement is that only the antisymmetric ordered-provenance sector contributes to the variance.

---

## OCC-T04 — Arithmetic degree-three support

For the prime-power weights

\[
u_a=\frac{\Lambda_Y(a)}a,
\]

ordered triples group by their full product `m=abc` with coefficient

\[
\boxed{
\sum_{abc=m}u_au_bu_c
=\frac{(\Lambda_Y*\Lambda_Y*\Lambda_Y)(m)}m.
}
\tag{6.1}
\]

The positive provenance hierarchy satisfies

\[
\Lambda_3=\mu*\log^3
=D^2\Lambda+3\Lambda*(D\Lambda)+\Lambda*\Lambda*\Lambda.
\tag{6.2}
\]

Thus (4.3) is supported exactly on the fully split cubic collision sector

\[
\Lambda*\Lambda*\Lambda
\]

of the positive degree-three packet.  The other two sectors encode one-history self marks and two-history collision/self-mark combinations.

The word “supported” is important: the scalar coefficient (6.1) alone is not sufficient to reconstruct the curvature, because the square must be formed before ordered histories are collapsed to their product.

---

## OCC-T05 — Ordered provenance is necessary

The two histories

\[
a\to bc,
\qquad
b\to ac
\]

have the same start and the same total label `abc`, but their first intermediate states are `q_a(n)` and `q_b(n)`.

Product-label recoalescence retains only

\[
(n,abc,q_{abc}(n)).
\]

It therefore erases the value

\[
f(q_a(n))-f(q_b(n)).
\]

The existing formal counterexample with the histories `2 then 9` and `9 then 2` proves that the product key cannot recover the ordered transport key or even a concrete transported observable.  OCC-T01 identifies the quotient-cloud curvature with exactly this lost ordered component.

Hence:

\[
\boxed{
\text{FULL PRODUCT RECOALESCENCE BEFORE POLARIZATION}
\Longrightarrow
\text{VARIANCE INFORMATION LOSS}.
}
\tag{7.1}
\]

This is not merely a limitation of one proof.  It is an information-theoretic no-go inherited from `NO_RESURRECTION`.

---

## OCC-T06 — Factorial provenance and the `S_3` standard sector

Fix three labels `a,b,c` and let

\[
z=f(q_{abc}(n)).
\]

For each of the six ordered histories `sigma in S_3`, define the direct closing-edge readout

\[
H_\sigma=f(q_{\sigma(1)}(n))+z.
\tag{8.1}
\]

The six values occur in three equal pairs:

\[
x_a+z,\ x_a+z;
\qquad
x_b+z,\ x_b+z;
\qquad
x_c+z,\ x_c+z.
\]

The alternating/sign representation vanishes because exchanging the last two labels changes no readout.  The trivial representation is the common mean.  The entire nontrivial content therefore lies in the two-dimensional standard representation.

Writing

\[
\bar H=z+\frac{x_a+x_b+x_c}{3},
\]

its exact local energy is

\[
\boxed{
\sum_{\sigma\in S_3}|H_\sigma-\bar H|^2
=\frac23\left(
|x_a-x_b|^2+|x_b-x_c|^2+|x_c-x_a|^2
\right).
}
\tag{8.2}
\]

Averaging over `a,b,c` with weights `u_au_bu_c` gives

\[
\boxed{
\sum_{a,b,c}u_au_bu_c
\sum_{\sigma\in S_3}|H_\sigma-\bar H|^2
=4U^2\Gamma_S(f;n).
}
\tag{8.3}
\]

Thus the same six-history provenance fiber that supplies the current `3!` completion factor also possesses a canonical representation-theoretic split:

- trivial sector: fully recoalesced/common amplitude;
- standard sector: quotient-cloud fluctuation energy;
- sign sector: zero for endpoint-symmetric closing-edge readouts.

This is a structural alignment, not yet a theorem identifying the full `tau` completion with the trivial projector of this particular readout.

---

## OCC-T07 — All-degree cylindrical lift

Let `C=c_1...c_{r-2}` be the product of any common suffix word.  Define

\[
\Omega^{(r)}_{a,b\mid c_1,\ldots,c_{r-2}}
:=\delta_{bC}f(q_a)-\delta_{aC}f(q_b).
\]

The common endpoint again cancels, so

\[
\Omega^{(r)}_{a,b\mid c_1,\ldots,c_{r-2}}
=x_a-x_b.
\]

Consequently, for product weights,

\[
\boxed{
\sum_{a,b,c_1,\ldots,c_{r-2}}
 u_au_b\prod_j u_{c_j}
|\Omega^{(r)}|^2
=2U^{r-1}\Gamma_S(f;n).
}
\tag{9.1}
\]

The variance therefore has exact representatives in every provenance degree `r>=2`.

This produces a useful no-go:

> increasing provenance degree by appending a common suffix does not itself contract the fluctuation; the curvature is cylindrically stable.

A native quantitative remainder theorem must therefore control the magnitude of the transported signless-edge tensor, or introduce a mixing operation acting on the first/intermediate label.  Degree elevation alone is insufficient.

---

## 10. Formal and computational status

Lean file:

- `EnterpriseMath/Relation/OrderedQuotientCurvature.lean`.

It formalizes:

1. common-endpoint cancellation;
2. suffix invariance;
3. antisymmetry;
4. the cocycle identity;
5. the exact finite weighted cubic-energy lift;
6. the normalized equality with quotient-cloud variance.

Exact checker:

- `scripts/check_free_research_ordered_cubic_curvature.py`.

It verifies the pointwise identities, weighted polarization, Hodge antisymmetric projection, all-degree lift through degree five, the grouped cubic collision coefficient, and the exact decomposition of `Lambda_3` using only integers and `Fraction`.

The Lean status is not declared green until the branch workflow completes successfully.

---

## 11. Updated next mother question

The V5 existence/comparison question is closed.  The next genuinely discriminating target is now:

> Can the full transported cubic edge norm
> \[
> \sum_{a,b,c\le Y}\frac{\Lambda(a)\Lambda(b)\Lambda(c)}{abc}
> |\delta_{bc}r(q_a(n))|^2
> \]
> be bounded by a scalar or matrix-valued degree-three return law at a strength that decays after division by `U_Y^2`?

Equivalently, one needs a native estimate on the antisymmetric standard-representation component before product recoalescence.

A second route is to construct a provenance-mixing operator on the six `S_3` histories and prove a spectral gap on its standard sector.  This would connect the original `3!` history fiber directly to a quantitative prime-distribution remainder mechanism.

No Riemann-hypothesis-scale conclusion follows at this stage.
