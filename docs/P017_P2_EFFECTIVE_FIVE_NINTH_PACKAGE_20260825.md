# P017 — P2 Five-Ninth Effectivity-Oriented Parameter Package

Status: `PROVED_WIP PARAMETER SPECIALIZATION + EXACT RATIONAL MAIN-TERM CERTIFICATE / NOT CANONICAL / PRIOR-ART SPECIALIZATION`

Date: `2026-08-25`

Owner branch: `research/p017-p2-chen-carry-bridge-20260823`

Depends on Iwaniec–Laborde (1981), *P2 in short intervals*, especially Lemmas 1, 2, 4, 6 and the unsimplified general `W_1` bound; and on the P017 Chen-carry bridge checkpoint.

Historical boundary: this does **not** claim a new asymptotic P2 theorem. The purpose is to choose a parameter package with large fixed power slack and a simple exact linear-sieve zone, suitable for later explicit-constant engineering.

## 1. Parameters

Fix

\[
\theta=\frac{4999}{10000},\qquad
D=X^{5/9},\qquad
a=4,
\]

and freeze the high-prime cutoff at the square-root edge by taking

\[
c=\frac{18}{5},\qquad b=\frac{13}{5}.
\]

Then

\[
b+c+1=\frac{36}{5}=\frac{a}{5/9},
\]

so the Lemma-1 relation

\[
b+c+1=a\frac{\log X}{\log D}
\]

holds exactly. The induced cut points are

\[
z=D^{1/a}=X^{5/36},
\]

\[
D^{b/a}=X^{13/36},
\]

and

\[
w=D^{c/a}=X^{1/2}.
\]

The basic domain is strict:

\[
1<b<c<a.
\]

The Selberg high-prime tail is therefore only the very thin band

\[
X^{4999/10000}\le p<X^{1/2}.
\]

## 2. Large fixed bilinear power margin

The Iwaniec–Laborde bilinear analysis permits, before arbitrarily small epsilon/delta losses, total level exponent

\[
2\theta-\frac5{14}.
\]

Our package has exact power gap

\[
2\theta-\frac5{14}-\frac59
=\boxed{\frac{27437}{315000}}
\approx0.0871016.
\]

This is over thirty times the bilinear power slack of the earlier `D=X^(16/25)` rational package.

## 3. Lemma-6 geometry has fixed slack

The Lemma-6 quantity

\[
D_1=(y^3/X)^{1/2}X^{-2\varepsilon}
\]

has base exponent `(3 theta-1)/2`. Since

\[
2\frac5{36}-\frac{3\theta-1}{2}
=\boxed{\frac{5027}{180000}}>0,
\]

we have strict room for `D_1<z^2` even before the favorable `X^{-2 epsilon}` factor.

The remaining band inequalities are also strict:

\[
\frac{13}{36}<\theta<\frac12<\frac32\theta.
\]

In particular `w/y=X^(1/10000)`, so the two-dimensional Selberg tail occupies only a root-boundary sliver.

## 4. Exact linear-sieve zone

For `a=4` every `F`-argument appearing in the four negative integrals of the unsimplified general `W_1` formula lies in the classical exact zone `1<=s<=3`. Hence

\[
F(s)=\frac{2e^\gamma}{s}
\]

throughout those integrals, and

\[
4f(4)=2e^\gamma\log3.
\]

Thus no continuation bound for `F` is required in this package.

Normalize the four negative integrals by `C_0=2e^gamma`, writing them as `J_1,...,J_4`.

## 5. Fully rational upper certificates for the four integrals

### 5.1 First integral

Direct integration gives

\[
J_1=\frac14\log\frac{39}{7}.
\]

The positive Taylor partial sum for `exp(43/25)` through degree six already exceeds `39/7`. Therefore

\[
\log\frac{39}{7}<\frac{43}{25},
\]

and

\[
\boxed{J_1<\frac{43}{100}}.
\]

### 5.2 Double integral

Exact elementary integration gives

\[
20J_2
=\log\left(
\frac{5^{20}13^{13}7^7}{3^{21}11^{22}}
\right).
\]

The positive Taylor partial sum for `exp(17/5)` through degree six exceeds the displayed exact rational. Hence

\[
\boxed{J_2<\frac{17}{100}}.
\]

### 5.3 Third integral

Exact integration gives

\[
J_3
=\frac9{10}\log\frac95
+\frac{11}{10}\log\frac{11}{15}
=\frac1{10}\log\left[
\left(\frac95\right)^9
\left(\frac{11}{15}\right)^{11}
\right].
\]

The degree-five positive Taylor partial sum for `exp(19/10)` exceeds the exact rational inside the logarithm. Thus

\[
\boxed{J_3<\frac{19}{100}}.
\]

### 5.4 Fourth integral

For an upper bound we may enlarge the upper endpoint from `theta=4999/10000` to `1/2`. Exact integration then gives

\[
J_4<\frac1{10}\log\left[
\left(\frac{18}{13}\right)^9\frac27
\right].
\]

The degree-five positive Taylor partial sum for `exp(17/10)` exceeds this exact rational, hence

\[
\boxed{J_4<\frac{17}{100}}.
\]

Therefore

\[
\boxed{J_1+J_2+J_3+J_4<\frac{24}{25}}.
\]

## 6. Coarse but exact positive `W_1` coefficient

The atanh series at `z=1/2` gives

\[
\log3
=2\left(\frac12+\frac{(1/2)^3}{3}+\frac{(1/2)^5}{5}+\cdots\right)
>\frac{263}{240}>\frac{109}{100}.
\]

Here

\[
\Delta=2c-b-1=\frac{18}{5},
\qquad
\frac{2a}{\Delta}=\frac{20}{9}.
\]

Since `a=4`, the general `W_1` coefficient simplifies exactly to

\[
2\log3-\frac{20}{9}(J_1+J_2+J_3+J_4).
\]

Consequently

\[
C_1
>2\frac{109}{100}
-\frac{20}{9}\frac{24}{25}
=\boxed{\frac7{150}}
\approx0.0466667.
\]

The true coefficient is materially larger; this coarse rational bound is chosen for auditability.

## 7. Lemma-6 tail is negligible in this package

Let `d=5/9`. The generalized Lemma-6 coefficient of `y/log D` is

\[
C_2(\theta)
=\frac{16(cd-a\theta)^2}
{a\Delta(3\theta-1)^2}.
\]

Here

\[
cd-a\theta
=2-4\frac{4999}{10000}
=\frac1{2500},
\]

so

\[
\boxed{
C_2=\frac{160}{224730081}
\approx7.11965\times10^{-7}.
}
\]

Hence the certified coarse asymptotic margin is

\[
\boxed{
C_1-C_2
>\frac{524362189}{11236504050}
\approx0.04666595.
}
\]

This leaves orders of magnitude more Selberg-tail room than the preceding rational package.

## 8. Why this package is better for effectivization

It deliberately avoids maximizing the level. Compared with `D=X^(16/25)`, it trades some ideal main-term strength for:

- a bilinear exponent slack of about `0.0871` instead of about `0.00266`;
- an exact `F(s)=2e^gamma/s` zone throughout the `W_1` integrals;
- a high-prime Selberg tail confined to `X^theta<=p<X^(1/2)`;
- an explicit rational main-term reserve exceeding `0.0466`.

These features are tailored to the next task: replacing all asymptotic `O`, `<<`, smoothing, bilinear and Mertens/prime-sum errors by explicit numerical constants.

## 9. P017 interface and remaining frontier

The exact P017 transfer remains

\[
(H_m-H_{2m})-\frac{K}{m}=r_K(m)-r_K(2m).
\]

Thus an explicit treatment of the classical short-interval floor remainder transports to the P017 binary carry without inventing a new distribution theorem.

The next load-bearing question is no longer positivity. It is to extract an explicit power-saving exponent and constant from Lemma 4 and combine it with explicit linear-sieve/Mertens/end-effect terms. The numerical target is to force the analytic threshold below the existing finite consecutive-square verification range.
