# Gregory–Machin continuation: a parameter-free generalized Lehmer / input-height Pareto bound

Status: `FREE_RESEARCH / EXACT_RESOURCE_INEQUALITY + GENERALIZED_ALPHABET_REPAIR / NOT_FOUNDATION`
Date: `2026-09-04`
Researcher: `EM-FREE-B2817C / FREE_AXIOM_DISCOVERY`
Issue: `#1160`
Depends on: unrestricted rational-alphabet Lehmer no-go, Gaussian `C8 + free valuation` endpoint decomposition.

## 1. Purpose

The unrestricted primitive rational-slope alphabet makes Lehmer measure alone degenerate:

\[
\inf\mu=0,
\]

while the integer coordinates of the atoms diverge.  A correct repair should not immediately invent an arbitrary scalar penalty `mu + lambda B`.

This note derives a parameter-free two-resource inequality that every generalized Machin formula must satisfy.

---

## 2. Generalized alphabet and resources

Let an exact signed endpoint formula use `s` **distinct** primitive positive rational-slope atoms

\[
V_j=[b_j+a_j i],
\qquad
0<a_j<b_j,
\qquad
\gcd(a_j,b_j)=1.
\]

Integer coefficients and signs are allowed; they do not enter the classical Lehmer denominator-only exponent coordinate.

Define

\[
\rho_j=\frac{b_j}{a_j}>1
\]

and the generalized Lehmer measure

\[
\boxed{
\mu=\sum_{j=1}^{s}\frac1{\log_{10}\rho_j}.
}
\]

Define the parameter-free logarithmic coordinate-height resource

\[
\boxed{
B_{\log}=\sum_{j=1}^{s}\log_2 b_j.
}
\]

This is a lower proxy for any ordinary binary encoding of the denominator coordinates.  Using actual integer bit lengths only increases the resource coordinate.

---

## 3. Universal two-resource inequality

Since

\[
1<\rho_j=\frac{b_j}{a_j}\le b_j,
\]

we have

\[
\ln\rho_j\le\ln b_j
\]

and therefore

\[
\frac1{\ln\rho_j}\ge\frac1{\ln b_j}.
\]

Hence

\[
\mu
=\ln10\sum_j\frac1{\ln\rho_j}
\ge
\ln10\sum_j\frac1{\ln b_j}.
\]

By Cauchy–Schwarz / Titu's lemma,

\[
\left(\sum_j\frac1{\ln b_j}\right)
\left(\sum_j\ln b_j\right)
\ge s^2.
\]

Since

\[
B_{\log}
=\frac1{\ln2}\sum_j\ln b_j,
\]

we obtain:

### Theorem 3.1 — generalized Lehmer / log-height Pareto bound

\[
\boxed{
\mu B_{\log}
\ge
s^2\frac{\ln10}{\ln2}
=s^2\log_2 10.
}
\]

This inequality is independent of the endpoint coefficients, a numerical value of `pi`, and any user-chosen tradeoff parameter.

---

## 4. Exact diagonal formulas require at least two strict-slope atoms

Could `s=1` occur?  Suppose one strict positive rational-slope atom `V=[b+ai]`, `0<a<b`, satisfied

\[
V^c=\tau
\]

for some nonzero integer `c`.

In the already-proved decomposition

\[
\mathcal T_{\mathbf Q}
\cong
C_8\oplus\bigoplus_{p\equiv1(4)}\mathbf Z,
\]

the endpoint equation forces every free split-prime coordinate of `V` to vanish.  Thus `V` is torsion-only.  But the rational torsion directions have only axis/diagonal slopes (`0`, `1`, infinity and their signs), not a strict slope `0<a/b<1`.

Therefore

\[
\boxed{s\ge2}
\]

for every convergent strict-slope generalized Machin endpoint formula.

Combining this with Theorem 3.1 gives the universal bound

\[
\boxed{
\mu B_{\log}
\ge4\log_2 10
\approx13.2877123795.
}
\]

With distinct strict-slope atoms the formal equality conditions of the elementary inequalities cannot all occur simultaneously, so the practical inequality is strict; the displayed non-strict form is the stable universal bound.

---

## 5. Actual bit encodings inherit the bound

Let

\[
B_{\rm bits}
=\sum_j\left\lceil\log_2(b_j+1)\right\rceil.
\]

Then

\[
B_{\rm bits}\ge B_{\log},
\]

so automatically

\[
\boxed{
\mu B_{\rm bits}
\ge s^2\log_2 10
\ge4\log_2 10.
}
\]

The same remains true if one uses the larger full atom-coordinate encoding that also stores every numerator `a_j`.

Thus the generalized-alphabet no-go does **not** imply unbounded improvement at fixed input size.

---

## 6. Fixed input budget consequence

For any declared binary coordinate budget

\[
B_{\rm bits}\le B,
\]

one has

\[
\boxed{
\mu
\ge
\frac{s^2\log_2 10}{B}
\ge
\frac{4\log_2 10}{B}.
}
\]

So every finite bit budget restores a positive lower bound to the completion exponent problem.

This is a genuine Pareto statement rather than a scalarization:

\[
\boxed{
(\mu,\;B_{\rm bits})
}
\]

should be retained as two typed coordinates unless an operational arithmetic-cost theorem justifies combining them.

---

## 7. Relation to the first-crossing adversarial family

The exact first-crossing family from the predecessor note satisfies

\[
\mu_q<\frac2{\log_{10}q}
\to0,
\]

but its residual atom norm has bit length

\[
\Theta(q\log q).
\]

Therefore it moves toward smaller `mu` only by moving rapidly outward in the input-height coordinate.  It does not contradict the Pareto inequality; it is the adversarial witness showing why both coordinates are needed.

Moreover, the previous fixed-compute exponent

\[
\Gamma=\frac{2\ln10}{\mu}
\]

satisfies along that family

\[
\Gamma=\Theta(\ln q),
\]

whereas residual atom description size is `Theta(q log q)`.  Thus the apparent term-count exponent grows only logarithmically relative to the exploding atom description.

---

## 8. Scope and next frontier

This is a lower-bound calibration, not a complete bit-operation model.  It does not charge for:

- coefficient bit length;
- high-precision multiplication/division;
- argument construction and reduction;
- winding certificates;
- reuse of common atom constants across repeated evaluations.

Those resources should be added only when their operational semantics are fixed.

The next finite research problem is now well-posed:

> For a bounded primitive rational-atom coordinate budget, compute the exact endpoint-feasible Pareto frontier in `(mu, B_bits, support, coefficient size, winding)` and determine which extra resource coordinates materially change the frontier.

The present theorem supplies a parameter-free global lower envelope against which any such census can be checked.
