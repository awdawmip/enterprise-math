# P017 — `a=4`, `d=11/20` effectivity-optimized P2 packet

Status: `PROVED_WIP PARAMETER GEOMETRY + CLOSED-FORM POSITIVE MAIN TERM + EXPLICIT POWER EXPONENT / NOT CANONICAL / IMPLIED CONSTANT OPEN`

Date: `2026-08-24`

Owner branch: `research/p017-p2-chen-carry-bridge-20260823`

This packet refines the preceding `d=4/7` closed-form packet.  The high-prime weight still terminates exactly at the square-root visibility boundary, but the sieve level is pulled inward to gain a larger power saving in Iwaniec–Laborde Lemma 4 while retaining an elementary positive main term.

## 1. Exact parameters

Take

\[
\boxed{
\theta=\frac{49}{100},\qquad
D=x^{11/20},\qquad
a=4,
}
\]

and impose the square-root high endpoint

\[
D^{c/a}=x^{1/2}.
\]

This forces

\[
\boxed{c=\frac{40}{11}.}
\]

Lemma 1 requires

\[
b+c+1=\frac ad=\frac{80}{11},
\]

so

\[
\boxed{b=\frac{29}{11}.}
\]

Thus

\[
1<b<c<a,
\qquad
\frac37<\theta<\frac12.
\]

## 2. Weight windows

The lower and upper prime-weight breakpoints are

\[
D^{b/a}
=x^{(11/20)(29/44)}
=x^{29/80},
\]

and

\[
D^{c/a}=x^{1/2}.
\]

Therefore

\[
\boxed{
x^{29/80}<y=x^{49/100}<x^{1/2}.}
\]

The upper weight again stops exactly at the root horizon.

## 3. Fixed epsilon and Lemma-4 level room

Choose

\[
\boxed{\varepsilon=\frac1{28}.}
\]

The published Lemma-4 hypotheses permit total product exponent

\[
2\theta-\frac5{14}-2\varepsilon
=\frac{193}{350}
=\frac{386}{700}.
\]

The chosen level is

\[
d=\frac{11}{20}=\frac{385}{700}.
\]

Hence the exact product-level slack is

\[
\boxed{\frac1{700}.}
\]

A concrete exponent split is

\[
M\asymp x^{159/350},
\qquad
N\asymp x^{67/700}.
\]

Indeed

\[
\frac{159}{350}=\theta-\varepsilon,
\]

while

\[
\theta-\frac5{14}-\varepsilon
=\frac{17}{175}=\frac{68}{700},
\]

so the `N` block also has strict `1/700` exponent room.

The proof of Lemma 4 permits every power saving `eta<epsilon/6`; therefore a convenient strict choice is

\[
\boxed{\eta=\frac1{180}<\frac1{168}=\frac{\varepsilon}{6}.}
\]

Thus the exponent part of the bilinear estimate may be frozen as

\[
\boxed{R(\mathcal A,M,N)\ll yx^{-1/180},}
\]

with the multiplicative implied constant still to be tracked explicitly.

## 4. Lemma-6 geometry

Here

\[
z=D^{1/a}=x^{11/80},
\qquad z^2=x^{11/40}.
\]

The auxiliary Lemma-6 level has exponent

\[
\frac{3\theta-1}{2}-2\varepsilon
=\frac{229}{1400}.
\]

The high endpoint is

\[
w=D^{c/a}=x^{1/2}.
\]

Hence

\[
\boxed{
D_1=x^{229/1400}
<z^2=x^{11/40}
<y=x^{49/100}
<w=x^{1/2}
<y^{3/2}=x^{147/200}.
}
\]

All order conditions are strict.

## 5. Closed-form p.53 main term

For these parameters all `F`-arguments in the general first p.53 inequality lie in `(0,3]`. Therefore

\[
F(s)=\frac{2e^\gamma}{s}
\]

throughout the four negative integrals and

\[
f(4)=\frac{2e^\gamma\log3}{4}.
\]

Let `C=2e^gamma` and denote the p.53 brace by `B`. Elementary integration gives

\[
\boxed{
\frac BC
=-\log392+\frac2{11}\log224+\frac{10}{11}\log3+\log55.
}
\]

Equivalently

\[
\boxed{
\frac BC
=\frac1{11}\log R_0,
}
\]

where

\[
R_0
=\frac{3^{10}224^2 55^{11}}{392^{11}}
=\frac{822625431538522412109375}{669346043402278412484608}.
\]

The exact integer comparison

\[
5\cdot822625431538522412109375
>
6\cdot669346043402278412484608
\]

shows

\[
\boxed{R_0>\frac65.}
\]

For `u>0`,

\[
\log(1+u)=\int_0^u\frac{dt}{1+t}>\frac{u}{1+u}.
\]

Taking `u=1/5` gives

\[
\log(6/5)>\frac16.
\]

Consequently

\[
\boxed{\frac BC>\frac1{66}.}
\]

## 6. High-prime tail and rigorous net margin

Because `dc/a=1/2`, the normalized Lemma-6 high-tail ratio is unchanged:

\[
\boxed{R=\frac4{47}.}
\]

After the standard `e^{-gamma}` normalization, `C=2e^gamma` contributes a factor `2`, so the net asymptotic coefficient satisfies

\[
S
=2\frac BC-\left(\frac4{47}\right)^2
>\frac1{33}-\frac{16}{2209}.
\]

Therefore

\[
\boxed{
S>\frac{1681}{72897}>0.023.
}
\]

Numerically the exact closed-form coefficient is about `0.03024777`; the rational lower bound above is the theorem-level certificate and does not depend on numerical quadrature.

## 7. Why this packet is preferred for effectivity

Compared with the earlier `d=4/7` closed-form packet:

- the root endpoint `w=x^(1/2)` is preserved exactly;
- the main-term lower margin drops but remains comfortably positive (`>0.023`);
- the allowed fixed epsilon rises to `1/28`;
- a safe Lemma-4 saving rises from roughly `1/300` to
  \[
  \boxed{1/180},
  \]
  a factor `5/3` improvement in the power exponent.

Thus this is currently the preferred generic packet for tracking an effective threshold.

## 8. Current boundary

Closed at `PROVED_WIP` scope:

- exact parameter geometry;
- strict Lemma-4 and Lemma-6 exponent conditions;
- closed-form positive main term with rational margin `>1681/72897`;
- explicit admissible Lemma-4 power exponent `eta=1/180`;
- exact P017 odd-carry transfer from the parent bridge.

Open:

- the multiplicative constant in the Lemma-4 bound;
- constants in the linear-sieve decomposition and its `O((log MN)^2)` block count;
- constants in Lemma 6 / Poisson / van der Corput / Mertens error terms;
- the resulting concrete threshold `x_0` and overlap with a finite square-basin verification range.

The next high-value question is no longer parameter optimization.  It is whether the special square-endpoint phase can replace the generic Lemma-4 constant chase by a substantially stronger bound.
