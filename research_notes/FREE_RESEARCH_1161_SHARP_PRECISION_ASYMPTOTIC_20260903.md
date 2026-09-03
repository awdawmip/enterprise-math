# Free Research #1161 — sharp precision asymptotic from the internal rotation phase

Status: `FREE_RESEARCH_RESULT / SHARP ASYMPTOTIC / NOT WORKING_TRUTH / NOT FOUNDATION`
Date: `2026-09-03`
Researcher: `EM-FREE-G61R8`
Parent issue: `#1161`
Dependencies:
- `Pi_*=Theta_AGM=tau`;
- finite Böttcher tail certificate;
- defect-mass scaling and AGM scale tail.

## 1. Exact phase normalization

For the standard self-dual Gauss–Legendre seed, the internal completion has been proved to satisfy

\[
\Pi_*=\Theta_{\rm AGM}=\tau.
\]

The finite Böttcher phase is

\[
\Theta_n=2^{-n}\ln\frac4{s_n},
\]

where

\[
s_n=U_n/H_n.
\]

The finite tail certificate is

\[
0<\Theta_n-\tau
\le
2^{-n}\frac{s_{n+1}}{1-s_{n+1}/2}.
\]

Therefore

\[
0<2^n(\Theta_n-\tau)
\le
\frac{s_{n+1}}{1-s_{n+1}/2}
\longrightarrow0.
\]

But

\[
2^n\Theta_n=\ln(4/s_n).
\]

Hence

\[
\ln\frac4{s_n}
=\tau2^n+o(1).
\]

Exponentiating gives the sharp shape asymptotic

\[
\boxed{
s_n\sim4e^{-\tau2^n}.}
\]

Thus the exact double-exponential rate is controlled by the same internal rotation-completion phase `tau` that equals the endogenous GL completion.

## 2. Budget tail is asymptotic to the current defect mass

Recall

\[
\delta_n=P_nH_n^2s_n^2,
\qquad
P_n=2^n,
\]

and

\[
\frac{\delta_{n+1}}{\delta_n}=\frac{s_{n+1}}2\longrightarrow0.
\]

Therefore

\[
A_n-A_\infty
=\sum_{k\ge n}\delta_k
\]

is dominated by its first term:

\[
\boxed{
\frac{A_n-A_\infty}{\delta_n}\longrightarrow1.
}
\]

Equivalently,

\[
\frac{A_n-A_\infty}{P_ns_n^2}
\longrightarrow H_\infty^2.
\]

## 3. Scale tail is negligible relative to `P_n s_n^2`

The chord-loss variable satisfies

\[
H_{n+1}=H_n(1-\ell_n),
\]

with

\[
\ell_n=\frac{1-r_n}{2}
=\frac{s_{n+1}}{1+s_{n+1}}
=O(s_n^2).
\]

The later losses contract superquadratically, so

\[
H_n-H_\infty=O(s_n^2).
\]

Hence

\[
H_n^2-H_\infty^2=O(s_n^2).
\]

Since `P_n=2^n -> infinity`, this gives

\[
\boxed{
\frac{H_n^2-H_\infty^2}{P_ns_n^2}\longrightarrow0.
}
\]

## 4. Sharp error coefficient

Let

\[
R_n=H_n^2/A_n,
\qquad
E_n=\Pi_*-R_n.
\]

Write

\[
H_*=H_\infty,
\qquad
A_*=A_\infty.
\]

Then exactly

\[
E_n
=
\frac{H_*^2(A_n-A_*)-A_*(H_n^2-H_*^2)}{A_*A_n}.
\]

Divide by `P_n s_n^2`.

The first numerator term tends to

\[
H_*^2\cdot H_*^2=H_*^4,
\]

while the scale-tail term tends to zero by Section 3. The denominator tends to `A_*^2`. Therefore

\[
\boxed{
\frac{\Pi_*-R_n}{P_ns_n^2}
\longrightarrow
\frac{H_*^4}{A_*^2}
=\Pi_*^2
=\tau^2.
}
\]

Thus

\[
\boxed{
\Pi_*-R_n
\sim\tau^2P_ns_n^2.
}
\]

## 5. Closed error asymptotic

Substitute

\[
P_n=2^n
\]

and

\[
s_n\sim4e^{-\tau2^n}.
\]

Then

\[
\boxed{
\Pi_*-R_n
\sim
16\tau^2\,2^n e^{-2\tau2^n}.
}
\]

Taking logarithms,

\[
\boxed{
-\ln(\Pi_*-R_n)
=
2\tau2^n
-n\ln2
-\ln(16\tau^2)
+o(1).
}
\]

For decimal precision,

\[
\boxed{
-\log_{10}(\Pi_*-R_n)
=
\frac{2\tau}{\ln10}2^n
-n\log_{10}2
-\log_{10}(16\tau^2)
+o(1).
}
\]

Thus digit doubling is quantitatively controlled by the same `tau` phase that arises independently from the #1159 finite rotation/Wallis completion.

## 6. Interpretation

There are now three equivalent appearances of `tau` in #1161:

1. **global normalization:** `Pi_*=tau`;
2. **Böttcher/rotation phase:** `Theta_AGM=tau`;
3. **precision exponent:** the leading exponent in the GL error is `2 tau 2^n`.

This makes the rotation/chord interpretation operational: the completion phase is not only the limiting scalar but also the exponential rate controlling how fast the finite chord defect is renormalized away.

## 7. Scope

Freeze at free-research-result strength:

`S_N ~ 4 EXP(-TAU 2^N) = PROVED`.

`(PI_STAR-R_N)/(P_N S_N^2) -> TAU^2 = PROVED`.

`PI_STAR-R_N ~ 16 TAU^2 2^N EXP(-2 TAU 2^N) = PROVED`.

`TAU=CLASSICAL_PI = SEPARATE IDENTIFICATION LAYER`.
