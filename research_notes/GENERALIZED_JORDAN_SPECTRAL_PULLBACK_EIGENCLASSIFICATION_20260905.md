# Generalized Jordan functions classify multiplicative eigencoordinates of primitive spectral pullback

Status: `FREE_RESEARCH / EXACT ARITHMETIC-SEMIGROUP THEOREM-CANDIDATE / NOT_FOUNDATION`
Date: `2026-09-05`
Researcher: `EM-FREE-W59A / FREE_AXIOM_DISCOVERY`
Issue: `#1159`
Depends on:
- primitive denominator pullback semigroup `A_n`;
- Möbius incidence algebra.

## 1. Pullback eigenfunctional equation

For the primitive pullback fiber

\[
\mathcal F_n(d)=\{dg:g\mid n,\ (d,n/g)=1\},
\]

define the dual pullback action on arithmetic functions by

\[
(\mathcal A_n^*f)(d)
:=\sum_{e\in\mathcal F_n(d)}f(e).
\]

The operators satisfy

\[
\mathcal A_m^*\mathcal A_n^*=\mathcal A_{mn}^*.
\]

We ask for arithmetic functions which are simultaneous eigenfunctions of every pullback.

## 2. Completely multiplicative eigencharacters

Let `chi` be any completely multiplicative function into a commutative coefficient ring/field, and define its generalized Jordan transform

\[
\boxed{J_\chi:=\mu*\chi.}
\tag{GJE-1}

Prime-locally, if `lambda_p:=chi(p)`, then

\[
\boxed{
J_\chi(p^a)
=\lambda_p^{a-1}(\lambda_p-1),
\qquad a\ge1.
}
\tag{GJE-2}

The function `J_chi` is multiplicative.

## 3. Exact pullback eigenlaw

For one prime `p`:

### p absent from d

The fiber is `{d,pd}`.  Multiplicativity and (GJE-2) give

\[
J_\chi(d)+J_\chi(pd)
=J_\chi(d)[1+(\lambda_p-1)]
=\lambda_pJ_\chi(d).
\]

### p already present in d

The fiber is `{pd}` and

\[
J_\chi(pd)=\lambda_pJ_\chi(d).
\]

Thus

\[
\boxed{\mathcal A_p^*J_\chi=\chi(p)J_\chi.}
\tag{GJE-3}

By commutative semigroup composition,

\[
\boxed{
\mathcal A_n^*J_\chi
=\chi(n)J_\chi
}
\tag{GJE-4}

for every `n`.

Therefore generalized Jordan functions are simultaneous eigencoordinates of primitive phase pullback.

## 4. Converse classification in the multiplicative class

Let `f` be multiplicative with `f(1)=1`, and suppose for every prime `p`

\[
\mathcal A_p^*f=\lambda_p f.
\]

At `d=1`,

\[
f(1)+f(p)=\lambda_p f(1),
\]

so

\[
f(p)=\lambda_p-1.
\]

At `d=p^a`, `a>=1`, the p-present rule gives

\[
f(p^{a+1})=\lambda_p f(p^a).
\]

Hence

\[
\boxed{
f(p^a)=\lambda_p^{a-1}(\lambda_p-1).}
\tag{GJE-5}

Define the completely multiplicative function `chi` by `chi(p)=lambda_p`.  Multiplicativity of `f` and (GJE-5) force

\[
\boxed{f=\mu*\chi=J_\chi.}
\tag{GJE-6}

Thus normalized multiplicative simultaneous eigenfunctions are exactly generalized Jordan transforms of completely multiplicative eigencharacters.

## 5. Ordinary Jordan totients

Take

\[
\chi_k(n)=n^k.
\]

Then

\[
J_{\chi_k}(n)=J_k(n),
\]

the ordinary Jordan totient, and (GJE-4) becomes

\[
\boxed{\mathcal A_n^*J_k=n^kJ_k.}
\]

This recovers the previously derived Jordan eigencoordinate theorem and shows it is one member of the complete multiplicative eigenfamily.

## 6. Dirichlet-series quotient

Whenever the relevant Dirichlet series converge absolutely,

\[
\sum_{n\ge1}\frac{J_\chi(n)}{n^s}
=\left(\sum_{n\ge1}\frac{\mu(n)}{n^s}\right)
\left(\sum_{n\ge1}\frac{\chi(n)}{n^s}\right).
\]

Therefore

\[
\boxed{
\mathcal D(J_\chi)(s)
=\frac{L_\chi(s)}{\zeta(s)},
}
\tag{GJE-7}

where `L_chi` denotes the Dirichlet series of the completely multiplicative weight `chi`.

For `chi_k(n)=n^k`,

\[
\boxed{
\sum_{n\ge1}\frac{J_k(n)}{n^s}
=\frac{\zeta(s-k)}{\zeta(s)}.
}
\tag{GJE-8}

This explains the shifted zeta ratios which appeared earlier in primitive reciprocal spectral-moment Dirichlet series.

## 7. Analytic Jordan family and von Mangoldt as first derivative

Take the analytic eigencharacter

\[
\chi_z(n)=n^z
\]

and write

\[
J_z(n):=(\mu*\chi_z)(n)
=n^z\prod_{p\mid n}(1-p^{-z}).
\tag{GJE-9}

The pullback eigenlaw is

\[
\boxed{
\sum_{e\in\mathcal F_n(d)}J_z(e)
=n^zJ_z(d).
}
\tag{GJE-10}

For `d>1`, `J_0(d)=0`.  Differentiate (GJE-10) at `z=0`:

\[
\sum_{e\in\mathcal F_n(d)}J_0'(e)
=J_0'(d).
\]

But prime-locally

\[
\boxed{
J_0'(d)=\Lambda(d).
}
\tag{GJE-11}

Indeed for `d=p^a`, the derivative is `log p`, while if `d` contains at least two distinct primes the product has a zero of order at least two.

Thus the previously observed endpoint prime-mass conservation

\[
\sum_{e\in\mathcal F_n(d)}\Lambda(e)=\Lambda(d)
\]

is the first derivative at the zero-eigencharacter point of the generalized Jordan pullback eigenlaw.

## 8. Higher derivatives resolve higher prime-support interactions

Let

\[
\omega(d)=|\{p:p\mid d\}|.
\]

From (GJE-9), near `z=0`,

\[
J_z(d)
=z^{\omega(d)}
\prod_{p\mid d}\log p
+O(z^{\omega(d)+1}).
\]

Therefore

\[
\boxed{
J_0^{(r)}(d)=0
\quad\text{for }r<\omega(d),
}
\tag{GJE-12}

while the first nonzero derivative is

\[
\boxed{
J_0^{(\omega(d))}(d)
=\omega(d)!\prod_{p\mid d}\log p.
}
\tag{GJE-13}

Thus the analytic Jordan family carries a hierarchy of prime-support interaction orders.

- first derivative sees exactly prime-power support and is von Mangoldt;
- second and higher derivatives begin to see genuinely mixed-prime denominators;
- a denominator with `r` distinct primes is invisible to all derivatives below order `r`.

## 9. Why endpoint mass misses mixed branches

The primitive endpoint integer mass is

\[
P_d=\exp(\Lambda(d))
\]

as a later log readout.  It therefore keeps only the first derivative channel (GJE-11).

If `omega(d)>=2`,

\[
\Lambda(d)=0,
\qquad
P_d=1,
\]

even though the higher derivative (GJE-13) is nonzero.

So the endpoint-mass neutrality of mixed primitive factors is not accidental cancellation.  It is a structural truncation to the first prime-support response of the generalized Jordan eigenfamily.

## 10. Triangular derivative transport

Differentiate (GJE-10) `r` times at zero:

\[
\boxed{
\sum_{e\in\mathcal F_n(d)}J_0^{(r)}(e)
=\sum_{a=0}^{r}
\binom ra(\log n)^{r-a}J_0^{(a)}(d).
}
\tag{GJE-14}

The first derivative reduces to exact Lambda conservation because `J_0(d)=0` for `d>1`.  Higher derivatives mix lower prime-support orders triangularly with scale-depth log provenance.

The logarithms here are derived analytic coordinates; the underlying finite branch/pullback algebra is already exact before this readout.

## 11. Interpretation

The pullback arithmetic admits a full common spectral family:

```text
completely multiplicative eigencharacter chi
    -> generalized Jordan eigencoordinate mu * chi
    -> pullback eigenvalue chi(n)
```

Specializations:

```text
chi(n)=n                 -> Euler phi
chi(n)=n^k               -> Jordan J_k
analytic derivative at k=0 -> von Mangoldt Lambda
higher derivatives at 0  -> higher prime-support interaction hierarchy
```

Thus Euler/Jordan multiplicity scaling and endpoint prime-mass conservation are different jets of one semigroup eigenfamily rather than unrelated arithmetic coincidences.

Freeze:

`MULTIPLICATIVE_PULLBACK_EIGENFUNCTIONS = GENERALIZED_JORDAN mu*chi`.

`JORDAN_J_k = POWER_EIGENCHARACTER n^k`.

`VON_MANGOLDT = FIRST z-DERIVATIVE OF J_z AT z=0`.

`MIXED_PRIME_SUPPORT = HIGHER J_z JET ORDER`.
