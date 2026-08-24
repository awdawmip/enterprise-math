# P017 — Closed-form `a=4` Iwaniec–Laborde P2 packet

Status: `PROVED_WIP PARAMETER COMPATIBILITY + CLOSED-FORM POSITIVE MAIN TERM / NOT CANONICAL / EFFECTIVE REMAINDER CONSTANTS OPEN`

Date: `2026-08-24`

Owner branch: `research/p017-p2-chen-carry-bridge-20260823`

This packet supersedes the `a=5` packet as the preferred explicitification route. It stays strictly inside the original Iwaniec–Laborde hypothesis `3/7 < theta < 1/2`, reaches the natural square-root high-prime boundary exactly, leaves fixed room in Lemma 4, and reduces the entire p.53 main integral to elementary logarithms.

## 1. Exact packet

Take

\[
\boxed{
\theta=\frac{49}{100},\qquad
D=x^{4/7},\qquad
a=4,
}
\]

and

\[
\boxed{
b=\frac52,\qquad c=\frac72.}
\]

For later remainder bookkeeping fix

\[
\boxed{\varepsilon=\frac1{50}.}
\]

The Section-3 interval assumption is strict:

\[
\frac37<\frac{49}{100}<\frac12.
\]

Lemma 1's weight relation is exact:

\[
b+c+1
=\frac52+\frac72+1
=7
=\frac{a}{d},
\qquad d=\frac47.
\]

## 2. Weight windows

The two prime-weight breakpoints become

\[
D^{b/a}
=x^{(4/7)(5/8)}
=x^{5/14},
\]

and

\[
D^{c/a}
=x^{(4/7)(7/8)}
=x^{1/2}.
\]

Hence

\[
\boxed{
D^{b/a}=x^{5/14}
<y=x^{49/100}
<D^{c/a}=x^{1/2}.
}
\]

The high-prime weight therefore terminates exactly at the square-root visibility horizon.

## 3. Lemma-4 room

With the displayed epsilon losses, the product level available from Lemma 4 is

\[
2\theta-\frac5{14}-2\varepsilon
=
\frac{102}{175}.
\]

The chosen level is

\[
d=\frac47=\frac{100}{175}.
\]

Thus

\[
\boxed{
\left(2\theta-\frac5{14}-2\varepsilon\right)-d
=rac2{175}>0.
}
\]

A concrete exponent split is

\[
M\asymp x^{47/100},
\qquad
N\asymp x^{\,4/7-47/100},
\]

which is strictly inside the individual Lemma-4 bounds.

## 4. Lemma-6 room

Here

\[
z=D^{1/a}=x^{1/7},
\qquad z^2=x^{2/7}.
\]

The Lemma-6 auxiliary level has exponent

\[
\frac{3\theta-1}{2}-2\varepsilon
=rac{39}{200}.
\]

Also

\[
w=D^{c/a}=x^{1/2}.
\]

Therefore the full order chain is strict:

\[
\boxed{
D_1=x^{39/200}
<z^2=x^{2/7}
<y=x^{49/100}
<w=x^{1/2}
<y^{3/2}=x^{147/200}.
}
\]

Thus the 1981 Selberg-tail geometry has fixed exponent room as well.

## 5. Why the p.53 integral becomes elementary

For `a=4,b=5/2,c=7/2`, every argument of `F` in the general first inequality on p.53 lies in `(0,3]`:

- in `I1`, `4(1-t)` ranges from 3 down to `3/2`;
- in the double integral `I2`, `(1-t)/s` is at most 3;
- in `I3`, `(1-t)/t` ranges from 3 downward;
- in `I4`, `4(1-t)` is below `3/2`.

Hence throughout all four integrals

\[
F(u)=\frac{2e^\gamma}{u}
\]

exactly. Moreover

\[
f(4)=\frac{2e^\gamma\log3}{4}
\]

exactly.

Put `C=2e^gamma` and write the p.53 brace as

\[
B=(2c-b-1)f(4)-(c-b)I_1-I_2-I_3-I_4.
\]

Direct elementary integration gives

\[
\frac{I_1}{C}=\frac14\log5,
\]

\[
\frac{I_2+I_3}{C}
=-\log2+\frac58\log5,
\]

and

\[
\frac{I_4}{C}
=-\log2-\frac{23}{8}\log5
+\frac{21}{8}\log7
+\frac18\log19.
\]

The positive term is

\[
\frac{(2c-b-1)f(4)}{C}
=\frac78\log3.
\]

Combining and cancelling yields the closed form

\[
\boxed{
\frac{B}{C}
=
\frac18
\left(
7\log3+16\log10-21\log7-\log19
\right)
}
\]

or equivalently

\[
\boxed{
\frac{B}{C}
=
\frac18\log
\left(
\frac{3^7 10^{16}}{19\,7^{21}}
\right).
}
\]

## 6. High-prime tail

For this packet

\[
\frac{dc}{a}=\frac12,
\]

so the normalized Lemma-6 tail ratio is

\[
R
=
\frac{4(dc/a-\theta)}{3\theta-1}
=
\frac4{47}.
\]

After the standard `e^{-gamma}` normalization, `C=2e^gamma` cancels and the net asymptotic coefficient is therefore exactly

\[
\boxed{
S
=
\frac14\log
\left(
\frac{3^7 10^{16}}{19\,7^{21}}
\right)
-rac{16}{2209}.
}
\]

## 7. Pure integer/log proof of positivity

An exact integer comparison gives

\[
3^7 10^{16}>38\,7^{21},
\]

hence

\[
\frac{3^7 10^{16}}{19\,7^{21}}>2.
\]

Also

\[
\log2=\int_1^2\frac{dt}{t}>\frac12.
\]

Therefore

\[
S
>\frac14\log2-\frac{16}{2209}
>\frac18-\frac{16}{2209}
=\boxed{\frac{2081}{17672}}>0.1177.
\]

Thus the positive main-term gate is closed with a fully elementary fixed margin; no numerical quadrature, Laborde constants `B_1,B_2`, or delayed-sieve numerical solution is needed.

## 8. Square-basin embedding

Set

\[
x_K=K^2+2K=(K+1)^2-1.
\]

Because `theta=49/100<1/2`, the terminal interval

\[
(x_K-x_K^{49/100},x_K]
\]

lies inside

\[
(K^2,(K+1)^2)
\]

for all sufficiently large `K` (and the elementary exponent comparison is far from critical).

Consequently, an effective version of Lemmas 2, 4 and 6 for this fixed packet would provide an effective P2-in-every-consecutive-square-basin theorem beyond its explicit threshold.

This is not a new asymptotic theorem: the 1981 paper already proves the stronger sufficiently-large-x exponent `0.45`. The point of the present packet is its unusually simple and wide **effective-constant margin**.

## 9. P017 interface and remaining frontier

The exact P017 transfer remains

\[
O_m(K)-\frac Km=r_K(m)-r_K(2m).
\]

Thus the generic analytic remainder technology transfers to the binary carry without introducing a new distribution conjecture. The route has now closed:

- pointwise/combinatorial P2 weight architecture: classical Iwaniec–Laborde input;
- strict legal parameter geometry: proved for this packet;
- main-term positivity: proved in closed form with margin `>2081/17672`;
- high-prime cutoff: exactly the square-root horizon.

The only unresolved analytic gate is **effectivity**:

1. explicit constants in the linear-sieve error `E` of Lemma 2;
2. explicit constant and power saving in Lemma 4's bilinear remainder;
3. explicit constants in Lemma 6's Selberg/Poisson remainder and the Mertens inputs;
4. comparison of the resulting `x_0` with an explicit finite verification range.

If the generic threshold is too high, P017's low-height square-root coupling is then the only project-specific place where new cancellation is worth seeking.
