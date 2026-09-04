# Dyadic annihilation hierarchy for target-free completion certificates

Status: `FREE_RESEARCH / GENERALIZATION OF WSR-T11/T12 / NOT_FOUNDATION`
Date: `2026-09-04`
Researcher: `EM-FREE-W59A / FREE_AXIOM_DISCOVERY`
Issue: `#1159`
Depends on:
- the internal completion law `(S,C,tau)`;
- the exact first-mode radius identity `T_q = 2q S(tau/(2q))`;
- the already verified target-free sign certificate `tau < 4`.

## 0. Main result

WSR-T11/T12 are the first member of an arbitrary-order dyadic extrapolation hierarchy.
For each level `m>=1` there is a finite rational combination of

`T_q, T_(2q), ..., T_(2^m q)`

which is a strict lower bound for `tau` and whose certified error is order

`q^(-2m-2)`.

For dyadic `q`, every endpoint is constructible from integers, rational arithmetic, and nested square roots only.

## 1. Base completion observable

Let

\[
T_q=q\sqrt{a_q}.
\]

Using the internal phase quantization of the first Dirichlet mode,

\[
\boxed{
T_q=2q\,S\left(\frac{\tau}{2q}\right).
}
\]

Set

\[
y=\frac{\tau}{2q}.
\]

Then

\[
\frac{T_q}{\tau}
=\frac{S(y)}y
=\sum_{n=0}^{\infty}\frac{(-1)^n y^{2n}}{(2n+1)!}.
\tag{DAH-1}
\]

## 2. Recursive dyadic annihilation

Define

\[
E_0(q):=T_q,
\]

and recursively for `m>=1`,

\[
\boxed{
E_m(q)
:=
\frac{4^m E_{m-1}(2q)-E_{m-1}(q)}{4^m-1}.
}
\tag{DAH-2}
\]

Thus

\[
E_1(q)=\frac{4T_{2q}-T_q}{3},
\]

which is exactly the old WSR-T11/T12 quantity `R_q`.

The next level is

\[
\boxed{
E_2(q)
=
\frac{T_q-20T_{2q}+64T_{4q}}{45}.
}
\]

The third level is

\[
\boxed{
E_3(q)
=
\frac{-T_q+84T_{2q}-1344T_{4q}+4096T_{8q}}{2835}.
}
\]

## 3. Refinement-operator interpretation

Let the dyadic refinement operator act by

\[
(\mathcal E f)(q)=f(2q).
\]

Then

\[
\boxed{
\mathcal A_m
=
\prod_{r=1}^{m}
\frac{4^r\mathcal E-I}{4^r-1},
\qquad
E_m=\mathcal A_m T.
}
\tag{DAH-3}
\]

For an even-power error mode

\[
g_n(q)=q^{-2n},
\]

one has

\[
\mathcal E g_n=4^{-n}g_n.
\]

Hence the exact response of the level-`m` filter is

\[
\boxed{
\lambda_{m,n}
=
\prod_{r=1}^{m}
\frac{4^{r-n}-1}{4^r-1}.
}
\tag{DAH-4}
\]

Consequently

\[
\lambda_{m,0}=1,
\]

and

\[
\boxed{
\lambda_{m,n}=0
\qquad(1\le n\le m).
}
\tag{DAH-5}
\]

Thus the filter annihilates exactly the first `m` even-power discretization modes.

This is a reusable precision/refinement operator, not a sine-specific coincidence.

## 4. Exact filtered power-series coefficients

Applying the filter termwise to (DAH-1),

\[
\boxed{
\frac{E_m(q)}\tau
=
\sum_{n=0}^{\infty}
\frac{(-1)^n\lambda_{m,n}y^{2n}}{(2n+1)!}.
}
\tag{DAH-6}
\]

For every `n>=m+1`, all factors `1-4^(r-n)` are positive, so

\[
\operatorname{sgn}(\lambda_{m,n})=(-1)^m.
\]

The first surviving response simplifies exactly:

\[
\boxed{
\lambda_{m,m+1}
=
(-1)^m 4^{-m(m+1)/2}.
}
\tag{DAH-7}
\]

Proof: rewrite each numerator as

\[
1-4^{r-m-1}
=
\frac{4^{m+1-r}-1}{4^{m+1-r}},
\]

then the numerator product `prod_(s=1)^m (4^s-1)` cancels the denominator product, leaving

\[
4^{-1-2-\cdots-m}.
\]

## 5. Alternating one-sided error survives every level

For `n>=m+1`, let

\[
\mu_{m,n}:=|\lambda_{m,n}|.
\]

The ratio of consecutive filter responses telescopes:

\[
\boxed{
\frac{\mu_{m,n+1}}{\mu_{m,n}}
=
\frac{1-4^{-n}}{1-4^{-(n-m)}}
<\frac43.
}
\tag{DAH-8}
\]

Indeed the intermediate factors cancel:

\[
\prod_{r=1}^{m}
\frac{1-4^{r-n-1}}{1-4^{r-n}}
=
\prod_{t=n-m}^{n-1}
\frac{1-4^{-(t+1)}}{1-4^{-t}}.
\]

For `q>=2`, the already verified `tau<4` gives

\[
0<y=\frac\tau{2q}<1.
\]

The magnitude ratio of consecutive surviving terms in (DAH-6) is therefore bounded by

\[
\frac43\,
\frac{y^2}{(2n+2)(2n+3)}<1.
\]

So after the `m` annihilated terms, the remainder is strictly alternating with decreasing magnitude.

Because the first surviving sign is always negative,

\[
\boxed{E_m(q)<\tau.}
\tag{DAH-9}
\]

More precisely,

\[
0<\tau-E_m(q)
\le
\tau\,
4^{-m(m+1)/2}
\frac{y^{2m+2}}{(2m+3)!}.
\]

Substituting `y=tau/(2q)` gives the exact internal bound

\[
\boxed{
0<\tau-E_m(q)
\le
\frac{\tau^{2m+3}}
{2^{(m+1)(m+2)}(2m+3)!\,q^{2m+2}}.
}
\tag{DAH-10}
\]

This is the arbitrary-order extension of WSR-T12.

## 6. Fully target-free rational width using only `tau<4`

Using the finite rational sign certificate `tau<4`, (DAH-10) gives

\[
\boxed{
E_m(q)<\tau<
E_m(q)
+
\frac{4^{2m+3}}
{2^{(m+1)(m+2)}(2m+3)!\,q^{2m+2}}.
}
\tag{DAH-11}
\]

The first levels are:

### `m=1` — quartic

\[
\boxed{
E_1(q)<\tau<E_1(q)+\frac{2}{15q^4}.
}
\]

This is exactly WSR-T12.

### `m=2` — sextic

\[
\boxed{
E_2(q)<\tau<E_2(q)+\frac{1}{1260q^6}.
}
\tag{DAH-12}
\]

### `m=3` — octic

\[
\boxed{
E_3(q)<\tau<E_3(q)+\frac{1}{1451520q^8}.
}
\tag{DAH-13}
\]

### `m=4` — tenth order

\[
\boxed{
E_4(q)<\tau<E_4(q)+\frac{1}{10218700800q^{10}}.
}
\tag{DAH-14}
\]

So the former fourth-order certificate is only the first rung of a systematic hierarchy.

## 7. Dyadic nested-radical constructibility

For dyadic `q`, the first-mode eigenvalues obey the exact inverse-decimation recursion

\[
a_{2q}=2-\sqrt{4-a_q},
\qquad a_2=2.
\]

Therefore every

\[
T_{2^j q}=2^j q\sqrt{a_{2^j q}}
\]

is built from integers, rational arithmetic, and nested square roots only.

Since every `E_m(q)` is a rational linear combination of finitely many such values,

\[
\boxed{
\text{dyadic }E_m(q)
\text{ is an algebraic, target-free lower certificate for }\tau.
}
\]

No trigonometric evaluation and no prior numerical value of `tau` or `pi` is required by the finite endpoint construction.

## 8. Fixed-base superfast hierarchy

Taking the smallest dyadic base `q=2`, (DAH-11) yields

\[
0<\tau-E_m(2)
<
\frac{2^{2-m^2-m}}{(2m+3)!}.
\tag{DAH-15}
\]

The first widths are:

```text
m=1: 1/120
m=2: 1/80640
m=3: 1/371589120
m=4: 1/10463949619200
m=5: 1/1671553167969484800
```

Thus increasing extrapolation depth gives a factor `2^(-m^2)` on top of factorial decay.

This is a certified arbitrary-precision route whose finite data remain in the dyadic nested-radical tower.

## 9. Optional sharper rational enclosure for tau

The coarse `tau<4` is convenient but not close to optimal. The same internal power series gives a much tighter purely rational enclosure without naming classical `pi`.

For every `0<x<4`, the magnitudes

\[
\frac{x^{2j+1}}{(2j+1)!}
\]

are strictly decreasing for `j>=1`, because

\[
\frac{x^2}{(2j+2)(2j+3)}
<\frac{16}{20}<1.
\]

At

\[
x_-=\frac{333}{106},
\]

the alternating partial sum through `j=7` is exactly

\[
\boxed{
P_7(x_-)
=
\frac{354434436851029003616983682290476507}
{4298926914316678785690142642056200192000}
>0.
}
\]

Since the next term is positive, the alternating remainder gives

\[
S(x_-)>P_7(x_-)>0.
\]

At

\[
x_+=\frac{355}{113},
\]

the alternating partial sum through `j=8` is exactly

\[
\boxed{
P_8(x_+)
=-
\frac{4271215760395527771482336170544960726645}
{17480292242231875961634561740127795897286361088}
<0.
}
\]

Since the next term is negative,

\[
S(x_+)<P_8(x_+)<0.
\]

Using `tau>=2`, the internal antiperiodicity

\[
S(\tau+y)=-S(y)
\qquad(0<y<\tau),
\]

and `x_-<x_+<4<=2tau`, these signs force

\[
\boxed{
\frac{333}{106}<\tau<\frac{355}{113}.
}
\tag{DAH-16}
\]

This enclosure is entirely rational and target-free; its numerical closeness to the classical constant is a later compatibility observation.

Replacing `4` by `355/113` in (DAH-10) gives a substantially tighter rational width:

\[
\boxed{
0<\tau-E_m(q)
<
\frac{(355/113)^{2m+3}}
{2^{(m+1)(m+2)}(2m+3)!\,q^{2m+2}}.
}
\tag{DAH-17}
\]

## 10. Tool-harvest interpretation

This hierarchy belongs under `T5_PRECISION_REFINEMENT`, not as a new top-level tool family.

Reusable operator:

```text
DYADIC_ANNIHILATION_FILTER(m)
input: a refinement-indexed observable f(q)
operator: prod_{r=1}^m (4^r E - I)/(4^r-1)
annihilates: q^-2, q^-4, ..., q^(-2m)
```

Sine/Dirichlet specialization adds the one-sided certificate because the surviving power-series coefficients alternate with controlled magnitude.

Freeze:

`T12 = LEVEL_1_OF_DYADIC_ANNIHILATION_HIERARCHY`.

`LEVEL_m -> ORDER_(2m+2)_TARGET_FREE_BRACKET`.

`DYADIC_CARRIER -> RATIONAL + NESTED_SQRT_ENDPOINTS`.
