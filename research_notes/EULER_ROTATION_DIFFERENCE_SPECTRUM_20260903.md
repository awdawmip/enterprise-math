# Euler rotation characters as finite-difference eigenmodes: a spectral meaning of precision pi

Status: `FREE_RESEARCH / EXACT FINITE SPECTRAL IDENTITIES / NOT FOUNDATION`  
Date: `2026-09-03`  
Researcher: `EM-FREE-F6D046 / FREE_AXIOM_DISCOVERY`  
Author/program signature: `YUAN X / Enterprise Math`

## 1. Setup

Normalize one complete oriented phase turn to length `1`. Let

\[
\chi:\mathbf R/\mathbf Z\to U(1)
\]

be the completed fundamental rotation character. In the dyadic root tower put

\[
h_m=\frac1{2^{m+1}},
\qquad
U_m=\chi(h_m),
\]

and choose the oriented quarter-turn unit

\[
J=U_1,
\qquad
J^2=-1.
\]

Define the reversal-even and normalized reversal-odd coordinates

\[
c_m=\frac{U_m+U_m^{-1}}2,
\]

\[
s_m=\frac{U_m-U_m^{-1}}{2J}.
\]

The finite rotation readout derived in the Cell-gate refinement line is

\[
\Pi_m=2^m s_m.
\]

No numerical value of pi is used in these finite definitions.

## 2. Antisymmetric difference operator

For any function on the phase circle define the centered first difference at scale
`h` by

\[
(\nabla_h^{\rm skew}f)(t)
=
\frac{f(t+h)-f(t-h)}{2h}.
\]

Because `chi` is multiplicative,

\[
\chi(t\pm h_m)=\chi(t)U_m^{\pm1}.
\]

Therefore

\[
\begin{aligned}
(\nabla_{h_m}^{\rm skew}\chi)(t)
&=
\chi(t)\frac{U_m-U_m^{-1}}{2h_m}\\
&=
J\frac{s_m}{h_m}\chi(t).
\end{aligned}
\]

Since `h_m^-1=2^(m+1)` and `Pi_m=2^m s_m`,

\[
\boxed{
\nabla_{h_m}^{\rm skew}\chi
=
2J\Pi_m\chi.
}
\]

Thus `chi` is an exact eigencharacter of the finite skew-difference operator, and

\[
\boxed{
\Pi_m
=
\frac12\left|\text{finite skew-generator eigenvalue at scale }h_m\right|.
}
\]

This is the finite form of

\[
\pi=\frac12|\chi'(0)|.
\]

## 3. Positive discrete Laplacian

Define the positive centered second difference

\[
(\Delta_h^+ f)(t)
=
\frac{2f(t)-f(t+h)-f(t-h)}{h^2}.
\]

On the fundamental character,

\[
\Delta_{h_m}^+\chi
=
\Lambda_m\chi,
\]

with exact eigenvalue

\[
\boxed{
\Lambda_m
=
\frac{2(1-c_m)}{h_m^2}.
}
\]

The dyadic square-root identity implies

\[
s_{m+1}^2=\frac{1-c_m}{2}.
\]

Hence

\[
\begin{aligned}
4\Pi_{m+1}^2
&=
4\cdot2^{2m+2}s_{m+1}^2\\
&=
2^{2m+3}(1-c_m)\\
&=
\frac{2(1-c_m)}{h_m^2}.
\end{aligned}
\]

Therefore

\[
\boxed{
\Lambda_m=4\Pi_{m+1}^2.
}
\]

Equivalently,

\[
\boxed{
\Pi_{m+1}=\frac12\sqrt{\Lambda_m}.
}
\]

So the next Viète precision value is exactly one half of the fundamental positive
Laplacian frequency at the current phase resolution.

## 4. Exact relation between first- and second-difference spectra

Using

\[
s_m^2=(1-c_m)(1+c_m),
\]

we obtain

\[
\left(2\Pi_m\right)^2
=
\frac{s_m^2}{h_m^2}
=
\frac{1+c_m}{2}\Lambda_m.
\]

Thus

\[
\boxed{
4\Pi_m^2
=
\frac{1+c_m}{2}\Lambda_m.
}
\]

As refinement forces `c_m -> 1`, the skew and positive-Laplacian frequencies become
asymptotically compatible:

\[
(2\pi_{\rm rot})^2
=
\lim_m\Lambda_m.
\]

Under the standard Archimedean character this is

\[
\lim_m\Lambda_m=4\pi^2.
\]

## 5. Purely finite interpretation

At each finite level there is no derivative and no continuous Fourier series. There
is only:

1. a finite cyclic phase state;
2. a forward/backward translation pair;
3. one character of that finite cyclic translation;
4. its exact first- and second-difference eigenvalues.

The scalar `Pi_m` is determined from those finite operators. The classical constant
appears only after the phase-metric completion.

This supports the following typing:

\[
\boxed{
\pi
=
\text{completed fundamental rotation-generator scale},
}
\]

not merely

\[
\pi
=
\text{circumference divided by diameter}.
\]

## 6. Bridge to the Basel branch

The identity

\[
\Lambda_m=4\Pi_{m+1}^2
\]

makes the Basel problem a natural next spectral test. For a finite cyclic phase
operator, higher characters give a full list of discrete Laplacian eigenvalues.
The questions for the independent Basel branch are then:

- whether an exact finite trace/Green-function identity can be written purely from
  these phase eigenvalues;
- whether the inverse-eigenvalue sum has a finite rational form;
- whether the completion to `pi^2/6` can be obtained without putting a continuous
  circle Laplacian into the native input.

This note does not prove the Basel identity. It supplies the operator whose
fundamental eigenvalue is already controlled by the same precision-pi tower.

## 7. Orientation gauge

Reverse the cyclic orientation. Then

\[
U_m\longmapsto U_m^{-1},
\qquad
J\longmapsto J^{-1}=-J.
\]

Consequently,

\[
c_m\longmapsto c_m,
\qquad
s_m\longmapsto s_m,
\qquad
\Pi_m\longmapsto\Pi_m,
\qquad
\Lambda_m\longmapsto\Lambda_m.
\]

The complex oriented eigenvalue `2J Pi_m` changes sign/conjugates, but its scalar
magnitude and the positive Laplacian spectrum are invariant.

Therefore a single root `i` requires an orientation frame, while the scalar
precision-pi hierarchy descends to the unoriented rotation geometry.

## 8. Candidate statement

`AC-EM-FREE-F6D046-EULER-DIFFERENCE-SPECTRUM-V1`:

> On the dyadically refined rotation phase carrier, the fundamental character is
> an exact eigenmode of the centered skew difference with eigenvalue `2 J Pi_m`.
> It is also an eigenmode of the positive centered Laplacian with eigenvalue
> `Lambda_m=4 Pi_(m+1)^2`. Hence the Viète precision hierarchy is simultaneously a
> sequence of finite rotation-generator eigenvalues and a sequence of fundamental
> discrete Laplacian frequencies. These scalar frequencies are invariant under
> orientation reversal even though the chosen quarter-turn unit `J` is not.

Status:

`FINITE_DIFFERENCE_IDENTITIES_EXACT`.

`ORIENTATION_INVARIANCE_EXACT`.

`ARCHIMEDEAN_LIMIT_TYPED_DERIVED`.

`BASEL_FULL_SPECTRAL_TRACE_OPEN`.
