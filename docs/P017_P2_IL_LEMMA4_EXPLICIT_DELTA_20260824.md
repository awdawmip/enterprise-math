# P017 — Explicit power saving extracted from Iwaniec–Laborde Lemma 4

Status: `PROVED_WIP PARAMETER EXTRACTION / NOT CANONICAL / IMPLIED CONSTANT STILL NONEXPLICIT`

Date: `2026-08-24`

Owner branch: `research/p017-p2-chen-carry-bridge-20260823`

## 1. Statement being sharpened

Iwaniec–Laborde 1981, Lemma 4 states that, for fixed `epsilon>0`,

\[
M\le yx^{-\varepsilon},\qquad
N\le yx^{-5/14-\varepsilon},
\]

one has

\[
R(\mathcal A,M,N)\ll_{\varepsilon}yx^{-\delta}
\]

for some `delta=delta(epsilon)>0`.

The proof itself makes the dependence elementary. To avoid a clash of letters, call the desired power saving `eta` below.

## 2. Conditions appearing in the proof

After Fourier truncation and Cauchy–Schwarz, the proof reduces to a collection of sufficient conditions. The relevant ones are:

\[
(A_1)\qquad MN\le yx^{1-\eta},
\]

\[
(A_2)\qquad M<yx^{-6\eta},
\]

\[
(A_3)\qquad MN^2<x,
\]

plus a branch `(A_4)` which, if it holds, already yields an admissible estimate. When `(A_4)` fails, the refined exponent-pair argument gives the sufficient condition

\[
N\le yx^{-5/14-4\eta}
\]

after inserting the exponent pair

\[
(\kappa,\lambda)=\left(\frac1{14},\frac{11}{14}\right).
\]

The primary proof also shows that the remaining constants depend only on the fixed smoothing/epsilon parameters.

## 3. Consequence under the published Lemma-4 hypotheses

Assume the paper's Section-3 range

\[
\frac37<\theta<\frac12,
\qquad y=x^\theta,
\]

and the Lemma-4 input

\[
M\le yx^{-\varepsilon},
\qquad
N\le yx^{-5/14-\varepsilon}.
\]

Then every

\[
0<\eta<\frac{\varepsilon}{6}
\]

satisfies the proof conditions for sufficiently large `x`:

- `(A_2)` follows immediately because `6 eta < epsilon`;
- the final exponent-pair condition follows because `4 eta < epsilon`;
- `(A_3)` follows from
  \[
  MN^2\le y^3x^{-10/14-3\varepsilon}
  <x^{3/2-5/7}<x;
  \]
- `(A_1)` is much weaker in this theta range, since
  \[
  MN\le y^2x^{-5/14-2\varepsilon}
  \]
  and `theta<1/2` leaves more than enough room below `yx^(1-eta)`.

Thus one may sharpen the existential exponent statement to

\[
\boxed{
R(\mathcal A,M,N)\ll_{\varepsilon,\eta}yx^{-\eta}
\quad\text{for every }0<\eta<\varepsilon/6.
}
\]

The implied constant is **not** made explicit here. This is an exponent extraction from the existing proof, not a new exponential-sum theorem.

## 4. Application to the preferred effective packet

For the strengthened closed-form packet

\[
\theta=\frac{49}{100},\qquad
D=x^{11/20},\qquad
a=4,
\]

choose

\[
\varepsilon=\frac1{28}.
\]

The total product-level allowance is

\[
2\theta-\frac5{14}-2\varepsilon
=\frac{193}{350}
=\frac{386}{700},
\]

whereas

\[
\frac{11}{20}=\frac{385}{700}.
\]

Hence the product level has exact slack

\[
\boxed{1/700}.
\]

A concrete split is

\[
M\asymp x^{159/350},
\qquad
N\asymp x^{67/700},
\]

while the individual upper bounds are

\[
\theta-\varepsilon=\frac{159}{350},
\]

and

\[
\theta-\frac5{14}-\varepsilon=\frac{17}{175}=\frac{68}{700}.
\]

Thus the `N` block has an additional `1/700` exponent room.

Since every `eta<1/168` is allowed, a convenient strict value is

\[
\boxed{\eta=\frac1{180}}.
\]

Therefore the bilinear remainder has the explicit **power exponent**

\[
\boxed{
R(\mathcal A,M,N)\ll yx^{-1/180}
}
\]

for this fixed packet, with an as-yet untracked absolute implied constant depending on the fixed smooth cutoff.

## 5. What remains nonexplicit

This closes the exponent-saving ambiguity but not the effective threshold. The remaining work inside Lemma 4 is to track:

1. constants in repeated integration by parts / Poisson truncation;
2. constants in Lemma 5's special mean-value estimate;
3. constants in the exponent-pair `(1/14,11/14)` application and partial summation;
4. the `O((log MN)^2)` number of bilinear blocks inherited from the linear-sieve decomposition.

The key routing change is therefore:

`unknown delta(epsilon)` is no longer a blocker;

`explicit multiplicative constant for the fixed eta=1/180 bound` is the live blocker.
