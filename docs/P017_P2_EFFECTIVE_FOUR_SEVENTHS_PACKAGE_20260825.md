# P017 — P2 Four-Sevenths Effectivity-Oriented Parameter Package

Status: `PROVED_WIP PARAMETER SPECIALIZATION + EXACT RATIONAL MAIN-TERM CERTIFICATE / NOT CANONICAL / PRIOR-ART SPECIALIZATION`

Date: `2026-08-25`

Owner branch: `research/p017-p2-chen-carry-bridge-20260823`

Purpose: compare an effectivity-oriented level `D=X^(4/7)` against the five-ninth package while preserving a large fixed bilinear power margin and an exact linear-sieve zone.

## 1. Parameters

Fix

\[
\theta=\frac{4999}{10000},\qquad D=X^{4/7},\qquad a=4,
\]

and take

\[
b=\frac52,\qquad c=\frac72.
\]

Then

\[
b+c+1=7=\frac{a}{4/7},
\]

so the Iwaniec–Laborde Lemma-1 relation holds exactly. The cut points are

\[
z=D^{1/a}=X^{1/7},
\]

\[
D^{b/a}=X^{5/14},
\]

and

\[
w=D^{c/a}=X^{1/2}.
\]

Thus `1<b<c<a` and the high Selberg tail again occupies only

\[
X^{4999/10000}\le p<X^{1/2}.
\]

## 2. Fixed analytic power margins

The bilinear level gap is

\[
2\theta-\frac5{14}-\frac47
=\boxed{\frac{2493}{35000}}
\approx0.0712286.
\]

The Lemma-6 `D_1<z^2` gap is

\[
\frac27-\frac{3\theta-1}{2}
=\boxed{\frac{5021}{140000}}
\approx0.0358643.
\]

The remaining band inequalities are strict:

\[
\frac5{14}<\theta<\frac12<\frac32\theta.
\]

Hence this package gives up only a modest amount of bilinear exponent room compared with `D=X^(5/9)` while moving the main linear-sieve term substantially upward.

## 3. Exact linear-sieve zone

Again `a=4`, so every `F`-argument in the general `W_1` integrals lies in the exact zone where

\[
F(s)=\frac{2e^\gamma}{s}
\]

and

\[
4f(4)=2e^\gamma\log3.
\]

Normalize the four negative integrals by `C_0=2e^gamma`, obtaining `J_1,...,J_4`.

## 4. Rational integral certificates

Direct elementary integration gives formulas that can be certified using only positive Taylor partial sums for the exponential.

### 4.1 First integral

\[
J_1=\frac14\log5.
\]

Since the degree-six positive Taylor partial sum for `exp(41/25)` exceeds `5`,

\[
\boxed{J_1<\frac{41}{100}}.
\]

### 4.2 Double integral

The exact logarithmic form satisfies

\[
8J_2=\log\left(\frac{8^8 3^7 5^5 7}{63^8}\right).
\]

The degree-six positive Taylor partial sum for `exp(6/5)` exceeds this exact rational, hence

\[
\boxed{J_2<\frac{15}{100}}.
\]

### 4.3 Third integral

Exact integration yields

\[
8J_3=\log\left(\frac{3^9 7^7}{16^8}\right).
\]

The degree-six positive Taylor partial sum for `exp(34/25)` exceeds this ratio, therefore

\[
\boxed{J_3<\frac{17}{100}}.
\]

### 4.4 Fourth integral

With the exact upper endpoint `theta/d`,

\[
8J_4
=\log\left(
\frac{5007\,34993^7}{2^{24}5^{39}3}
\right).
\]

The degree-six positive Taylor partial sum for `exp(32/25)` exceeds this exact rational. Hence

\[
\boxed{J_4<\frac{16}{100}}.
\]

Combining,

\[
\boxed{J_1+J_2+J_3+J_4<\frac{89}{100}}.
\]

## 5. Coarse exact `W_1` coefficient

Use the same elementary lower bound

\[
\log3>\frac{109}{100}.
\]

Here

\[
\Delta=2c-b-1=\frac72,
\qquad
\frac{2a}{\Delta}=\frac{16}{7}.
\]

Thus the general `W_1` coefficient satisfies

\[
C_1
>2\frac{109}{100}-\frac{16}{7}\frac{89}{100}
=\boxed{\frac{51}{350}}
\approx0.145714286.
\]

## 6. Lemma-6 tail remains microscopic

For `d=4/7`,

\[
cd-a\theta
=2-4\frac{4999}{10000}
=\frac1{2500}.
\]

The generalized Lemma-6 coefficient is

\[
C_2
=\frac{16(cd-a\theta)^2}{a\Delta(3\theta-1)^2}
=\boxed{\frac{128}{174790063}}
\approx7.32307\times10^{-7}.
\]

Therefore

\[
\boxed{
C_1-C_2
>\frac{181923437}{1248500450}
\approx0.145713553.
}
\]

This certified reserve is about three times the coarse reserve of the five-ninth package.

## 7. Comparison with the five-ninth package

`D=X^(5/9)`:

- bilinear power gap `27437/315000 ~= 0.08710`;
- certified net main coefficient `>0.04666595`.

`D=X^(4/7)`:

- bilinear power gap `2493/35000 ~= 0.07123`;
- certified net main coefficient `>0.14571355`.

Thus four-sevenths sacrifices about 18% of the available exponent slack but gains more than a factor three in certified main-term reserve.

Which package produces the lower **explicit numerical threshold** depends on the effective power-saving exponent and constants in Lemma 4; that dependence must be extracted from the proof rather than guessed from the raw level gap.

## 8. P017 interface

The exact carry transfer remains

\[
(H_m-H_{2m})-\frac{K}{m}=r_K(m)-r_K(2m).
\]

The next frontier is therefore to make the Lemma-4 bilinear saving explicit and compare the resulting finite-X error budget for the five-ninth and four-sevenths packages.
