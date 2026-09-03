# Free Research #1161 — Böttcher rotation phase of the AGM shape RG

Status: `FREE_RESEARCH_RESULT / DERIVED LOG PHASE / NOT WORKING_TRUTH / NOT FOUNDATION`
Date: `2026-09-03`
Researcher: `EM-FREE-G61R8`
Parent issue: `#1161`

## 1. Shape dynamics

Use the normalized AGM cone shape

\[
s_n=U_n/H_n,
\qquad
r_n=V_n/H_n,
\qquad
r_n^2+s_n^2=1,
\]

with exact update

\[
\boxed{
s_{n+1}=\frac{s_n^2}{(1+r_n)^2}.
}
\]

The fixed direction is `s=0`, and the map is superattracting of order two:

\[
s_{n+1}\sim s_n^2/4.
\]

## 2. An endogenous logarithmic phase

Define the finite derived log readout

\[
\boxed{
\Theta_n:=2^{-n}\ln\frac4{s_n}.
}
\]

`LN` is a derived readout here, not primitive native state.

Using the exact shape recursion,

\[
\begin{aligned}
\Theta_{n+1}-\Theta_n
&=
2^{-n}\ln\frac{1+r_n}{2}.
\end{aligned}
\]

Since `0<r_n<1` at every finite nonfixed step,

\[
\boxed{
\Theta_{n+1}<\Theta_n.
}
\]

The sequence is positive and therefore converges. Define

\[
\boxed{
\Theta_{\rm AGM}:=\lim_{n\to\infty}\Theta_n.
}
\]

This constant is defined entirely from the AGM shape orbit. No classical pi value, circumference, elliptic integral, or external period is part of the definition.

## 3. Chord-loss form of the phase decrement

The #1161/#1158 bisector-square bridge identified

\[
\ell_n=\frac{1-r_n}{2}=S_n^2
\]

as the squared transverse coordinate of the finite Viète bisector.

Since

\[
\frac{1+r_n}{2}=1-\ell_n,
\]

one has

\[
\boxed{
\Theta_n-\Theta_{n+1}
=2^{-n}\bigl[-\ln(1-\ell_n)\bigr].
}
\]

Thus the rotation-phase correction is the dyadically weighted log of the same chord-loss scalar that controls the AGM scale contraction.

## 4. Finite tail certificate

For `0<=ell<1`,

\[
-\ln(1-\ell)\le\frac{\ell}{1-\ell}.
\]

But the AGM shape law gives exactly

\[
\frac{\ell_n}{1-\ell_n}=s_{n+1}.
\]

Therefore

\[
0<\Theta_n-\Theta_{\rm AGM}
\le
\sum_{k=n}^\infty 2^{-k}s_{k+1}.
\]

Because `s_{k+1}<s_k^2` and `0<s_k<1`, for `j>=0`

\[
s_{n+1+j}\le s_{n+1}^{2^j}\le s_{n+1}^{j+1}.
\]

Hence the geometric majorant yields

\[
\boxed{
0<\Theta_n-\Theta_{\rm AGM}
\le
2^{-n}\frac{s_{n+1}}{1-s_{n+1}/2}.
}
\]

This is a current-state finite error certificate for the endogenous phase.

## 5. Normalized Böttcher coordinate

Define

\[
\psi(s):=e^{-\Theta(s)},
\]

where `Theta(s)` is obtained by starting the same shape recursion at `s` and taking the limit above.

If `f(s)` denotes one AGM shape update, then shifting the orbit by one step gives

\[
\boxed{
\Theta(f(s))=2\Theta(s),
}
\]

hence

\[
\boxed{
\psi(f(s))=\psi(s)^2.
}
\]

The tail estimate shows that as `s->0+`,

\[
\Theta(s)=\ln(4/s)+o(1),
\]

so

\[
\boxed{
\psi(s)\sim s/4.
}
\]

Thus `psi` is precisely the normalized Böttcher coordinate of the superattracting AGM shape RG.

This gives an intrinsic dynamical meaning to `precision doubling`: in the `psi` coordinate one refinement step is literal squaring.

## 6. Three internal completion constants

There are now three separately defined internal constants in the current research packet:

1. budget/readout completion
   \[
   \Pi_*=H_\infty^2/A_\infty;
   \]
2. AGM shape/Böttcher rotation phase
   \[
   \Theta_{\rm AGM};
   \]
3. independent #1159 determinant/Wallis boundary-completion phase
   \[
   \tau.
   \]

Finite numerical/certified experiments are consistent with all three having the familiar value later called pi, but definitionally they are distinct until bridge theorems are supplied.

The global closure problem can therefore be split into

\[
\boxed{
\Pi_*\stackrel{?}=\Theta_{\rm AGM}
}
\]

and

\[
\boxed{
\Theta_{\rm AGM}\stackrel{?}=\tau.
}
\]

This decomposition prevents the local AGM mechanism, the AGM dynamical phase, and the independent rotation-spectrum normalization from being conflated.

## 7. Relation to the self-dual response bridge

The separate #1161 self-dual defect/response invariant gives

\[
\Pi_*
=
\frac{M^2}{\sum_{n\ge0}2^n b_n(a_n-b_n)}.
\]

Therefore the first bridge can equivalently be written

\[
\boxed{
\Theta_{\rm AGM}
\sum_{n\ge0}2^n b_n(a_n-b_n)=M^2.
}
\]

If the second bridge `Theta_AGM=tau` is also proved, this becomes the internal `tau` response normalization isolated previously.

## 8. Scope boundary

Freeze only at free-research-result strength:

`AGM_SHAPE_BOTTCHER_PHASE = DEFINED_AND_FINITE_CERTIFIED`.

`BOTTCHER_SQUARING psi(f(s))=psi(s)^2 = PROVED`.

`THETA_AGM_FINITE_TAIL_BOUND = PROVED`.

`PI_STAR_EQUALS_THETA_AGM = OPEN`.

`THETA_AGM_EQUALS_TAU = OPEN`.

`CLASSICAL_PI_IDENTIFICATION = ANALYTIC_COMPLETION`.
