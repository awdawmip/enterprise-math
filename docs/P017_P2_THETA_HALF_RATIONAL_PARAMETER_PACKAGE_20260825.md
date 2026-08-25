# P017 — P2 Near-Half Rational Iwaniec–Laborde Parameter Package

Status: `PROVED_WIP PARAMETER SPECIALIZATION + EXACT RATIONAL MAIN-TERM CERTIFICATE / NOT CANONICAL / PRIOR-ART SPECIALIZATION`

Date: `2026-08-25`

Owner branch: `research/p017-p2-chen-carry-bridge-20260823`

Depends on:

- Iwaniec–Laborde (1981), *P2 in short intervals*, especially Lemmas 1, 2, 4, 6 and the unsimplified general `W_1` bound on p. 53;
- `docs/P017_P2_CHEN_CARRY_BRIDGE_20260823.md`;
- `docs/P017_P2_CHEN_CARRY_BRIDGE_CHECKPOINT_20260825.md`.

Historical boundary: this does **not** claim a new asymptotic P2 theorem. Iwaniec–Laborde already prove the stronger exponent `theta=0.45`. The project value here is a clean rational specialization near the consecutive-square scale, with large algebraic margins suitable for later effectivization and P017 remainder transport.

## 1. Clean rational parameter choice

Avoid the endpoint convention `theta=1/2` by fixing

\[
\theta=\frac{4999}{10000}.
\]

Choose

\[
a=\frac{24}{5},\qquad b=\frac52,\qquad c=4.
\]

Then

\[
b+c+1=\frac{15}{2}.
\]

Lemma 1 requires

\[
b+c+1=a\frac{\log X}{\log D},
\]

so set

\[
\boxed{D=X^{16/25}}.
\]

Writing `D=y^(1+alpha)` with `y=X^theta`,

\[
1+\alpha=\frac{16/25}{4999/10000}=\frac{6400}{4999},
\qquad
\alpha=\frac{1401}{4999}.
\]

The natural weighted-sieve cut points become

\[
z=D^{1/a}=X^{2/15},
\]

\[
D^{b/a}=X^{1/3},
\]

and

\[
w=D^{c/a}=X^{8/15}.
\]

The basic weight-domain hypothesis is satisfied exactly:

\[
1<b<c<a.
\]

No `b>=3` assumption is needed because we use the general integral lower bound for `W_1`; the later `b>=3` restriction in the 1981 paper is only for its further simplification through precomputed Laborde constants.

## 2. Bilinear level has a strict power margin

The Iwaniec–Laborde remainder analysis with exponent pair `(1/14,11/14)` permits, after choosing the small loss parameter sufficiently small, total bilinear level up to the power

\[
X^{2\theta-5/14-o(1)}.
\]

For our fixed `theta`,

\[
2\theta-\frac5{14}-\frac{16}{25}
=\boxed{\frac{93}{35000}}>0.
\]

Thus `D=X^(16/25)` lies strictly inside the bilinear range. The margin is small but fixed; all auxiliary epsilon/delta losses can be chosen below it in the asymptotic argument.

## 3. Lemma 6 Selberg-tail geometry also has a strict margin

Lemma 6 uses

\[
D_1=(y^3/X)^{1/2}X^{-2\varepsilon}
\]

and requires

\[
D_1\le z^2<y<w<y^{3/2}.
\]

Ignoring the favorable `X^(-2 epsilon)` factor, the exponent of `D_1` is

\[
\frac{3\theta-1}{2}.
\]

Since

\[
\frac4{15}-\frac{3\theta-1}{2}
=\boxed{\frac{1009}{60000}}>0,
\]

we have a strict margin for `D_1<z^2`.

The remaining inequalities are even wider:

\[
\theta-\frac13=\frac{4997}{30000}>0,
\]

\[
\frac8{15}-\theta=\frac{1003}{30000}>0,
\]

and

\[
\frac32\theta-\frac8{15}=\frac{12991}{60000}>0.
\]

Therefore

\[
X^{1/3}<y<X^{8/15}<y^{3/2}.
\]

This fixes the failure of the naive `a=6`, maximal-level extrapolation at `theta=1/2`, where `z^2` was too shallow for Lemma 6.

## 4. Direct general `W_1` bound, not the `b>=3` simplification

Let

\[
C_0=2e^\gamma.
\]

Use the standard dimension-one linear-sieve bounds

\[
1\le F(s)\le \frac{C_0}{\min(s,3)}
\]

on the argument range needed below, and the delay identity

\[
a f(a)=4f(4)+\int_4^a F(t-1)\,dt.
\]

Since

\[
4f(4)=C_0\log 3
\]

and `a-4=4/5`, we get

\[
\boxed{a f(a)\ge C_0\log3+\frac45}.
\]

In the general p. 53 formula for `W_1`, normalize the four negative integrals by `C_0` and call them `J_1,...,J_4`. For the present rational parameters, elementary splitting at the points where the argument of `F` crosses `3` gives the following rigorous bounds.

### 4.1 First integral

Exactly,

\[
J_1
=\frac12\log\frac95
+\frac5{16}\log\frac{125}{69}.
\]

The Taylor lower bounds for the exponential give

\[
\log\frac95<\frac35,
\qquad
\log\frac{125}{69}<\frac{76}{125}.
\]

Hence

\[
\boxed{J_1<\frac{49}{100}}.
\]

### 4.2 Double integral

Put

\[
H=\frac{b+1}{a}=\frac{35}{48},
\qquad
s_0=\frac1a=\frac5{24},
\qquad
s_1=\frac{b+1}{2a}=\frac{35}{96}.
\]

Using

\[
\frac1{\min(u,3)}\le \frac1u+\frac13,
\]

write `J_2 <= A+B`.

For the first part, since `t+s<=H<1`,

\[
t(1-t)\ge s(1-s),
\]

so

\[
A\le \frac{35}{48}\log\frac74
+\frac{61}{48}\log\frac{61}{76}.
\]

The elementary estimates

\[
\log\frac74<\frac{14}{25},
\]

and

\[
\log(1-u)\le -u-\frac{u^2}{2}-\frac{u^3}{3}
\quad(0<u<1),
\]

with `u=15/76`, imply

\[
A<\frac{13}{100}.
\]

For the second part, use for `x>=1`

\[
\log x\le \frac{x-x^{-1}}2.
\]

It gives

\[
B\le \frac16\left(\frac32+\log\frac25\right)
=\frac14-\frac16\log\frac52.
\]

The positive atanh series with `z=3/7` gives

\[
\log\frac52
=2\left(z+\frac{z^3}{3}+\cdots\right)
>\frac{312}{343}>\frac9{10},
\]

hence

\[
B<\frac1{10}.
\]

Therefore

\[
\boxed{J_2<\frac{23}{100}}.
\]

### 4.3 Third integral

Splitting at `t=1/4` gives the exact expression

\[
J_3=
\frac7{36}
+\frac23\log\frac56
+\frac{35}{48}\log\frac{35}{24}
+\frac{61}{48}\log\frac{61}{72}.
\]

Use

\[
\log(1-u)\le-u-\frac{u^2}{2}
\]

for the two negative logarithms and

\[
\log(1+v)\le v-\frac{v^2}{2}+\frac{v^3}{3}
\]

with `v=11/24`. This yields exactly

\[
J_3<\frac{96947}{663552}<\boxed{\frac3{20}}.
\]

### 4.4 Fourth integral

At `theta=1/2` the upper endpoint is largest, so using that larger endpoint gives a valid upper bound for our slightly smaller theta. The integral reduces to

\[
J_4\le
\frac16\log\frac{5103}{1472}.
\]

The first five positive terms of the exponential series show

\[
e^{63/50}>\frac{5103}{1472},
\]

so

\[
\boxed{J_4<\frac{21}{100}}.
\]

Combining,

\[
\boxed{
J_1+J_2+J_3+J_4<\frac{27}{25}.
}
\]

## 5. A rational positive lower bound for `W_1`

Let

\[
\Delta=2c-b-1=\frac92.
\]

The coefficient of `y/log D` in the direct general lower bound for `W_1` is at least

\[
e^{-\gamma}\frac{a}{\Delta}
\left[
\frac{\Delta}{a}\left(C_0\log3+\frac45\right)
-C_0\frac{27}{25}
\right].
\]

Since `C_0=2e^gamma`, `log 3>1`, and the standard bound `e^(-gamma)>1/2`,

\[
W_1\text{-coefficient}
>
2+\frac25
-\frac{2a}{\Delta}\frac{27}{25}.
\]

Here

\[
\frac{2a}{\Delta}=\frac{32}{15},
\]

so

\[
\boxed{
W_1\text{-coefficient}>\frac{12}{125}=0.096.
}
\]

This deliberately uses very coarse bounds; the true numerical coefficient is much larger.

## 6. Lemma 6 upper-tail coefficient

Let

\[
d=\frac{\log D}{\log X}=\frac{16}{25}.
\]

Substituting

\[
z=D^{1/a},\qquad w=D^{c/a},\qquad y=X^\theta
\]

into Lemma 6 gives the asymptotic coefficient of `y/log D`

\[
C_2(\theta)
=
\frac{16(cd-a\theta)^2}
{a\Delta(3\theta-1)^2}.
\]

For

\[
\theta=\frac{4999}{10000},
\]

we have

\[
cd-a\theta=\frac{1003}{6250}
\]

and therefore

\[
\boxed{
C_2
=\frac{257538304}{3370951215}
\approx0.0763993.
}
\]

Consequently the coarse certified main-term margin is

\[
\boxed{
\frac{12}{125}-C_2
=\frac{1651825316}{84273780375}
>0.0196.
}
\]

The original asymptotic formulas contain arbitrarily small `epsilon` losses. Since the margin above is fixed and positive, choose those losses sufficiently small. Thus this rational parameter package is safely positive in the asymptotic Iwaniec–Laborde framework.

## 7. Consequence and exact boundary

For sufficiently large `X`, the Iwaniec–Laborde weighted sieve with this parameter package detects a `P_2` in an interval of length `X^(4999/10000)`.

A consecutive-square basin has length asymptotic to `2 X^(1/2)`, so for sufficiently large square basins it contains such a shorter subinterval. Hence this package alone supplies a clean rational re-proof of an asymptotic statement already strictly weaker than the 1981 theorem `theta=0.45`.

It is therefore **not** a novelty claim and not the target endpoint.

Its value is that all load-bearing exponent inequalities now have fixed rational slack and the main term has a fixed rational positive margin. This sharply separates the remaining project problem:

> effectivize the `O`, `<<`, smoothing, linear-sieve `E`, bilinear remainder, Selberg-tail, Mertens/prime-sum and squarefull terms sufficiently to compute an explicit threshold, then compare that threshold with finite square-basin verification.

## 8. P017 interface retained

On the full square basin, P017 still gives the exact identity

\[
(H_m-H_{2m})-\frac{K}{m}
=r_K(m)-r_K(2m).
\]

Thus any explicit treatment of the classical floor remainder can be transported to the binary-carry observable without a new distribution theorem. Whether the square endpoint coupling reduces the explicit constants remains the active P017-specific question.
