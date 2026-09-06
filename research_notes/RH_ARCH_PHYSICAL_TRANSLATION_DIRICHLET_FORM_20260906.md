# RH cutoff-free physical-space archimedean translation Dirichlet form

Status: `TASK_RESEARCH / EXACT OPERATOR IDENTITY + CUTOFF-FREE FINITE-SUPPORT REDUCTION / NOT AN RH PROOF`
Date: `2026-09-06`
Researcher-ID: `EM-DIRECT-7C1A42`
Scope: `RH / Weil archimedean term / physical log coordinate / translation Dirichlet form / square-shell finite certification`

## 0. Main result

The archimedean Mellin multiplier

`h_inf(t)=Re psi(1/4+i t/2)-log pi`

admits an exact Levy/Dirichlet-form representation in physical logarithmic coordinates.

Define

`w(r)=exp(-r/2)/(1-exp(-2r))`, `r>0`,

and

`h0=h_inf(0)=psi(1/4)-log pi`
`=-gamma-pi/2-3 log2-log pi`.

Then

`boxed: h_inf(t)=h0+2 integral_0^infinity w(r)(1-cos(tr)) dr}`.

Consequently, for admissible compactly supported `f,g` for which the expressions are defined,

`boxed: Q_arch(f,g)`
`= h0 <f,g>`
`+ integral_0^infinity w(r)`
`  <T_r f-f, T_r g-g> dr`,

where `T_r` is translation on the additive logarithmic line.

This removes the infinite-frequency digamma quadrature from the finite-support square-shell computation entirely.

## 1. Derivation from the digamma integral

For `Re z>0`,

`psi(z)=-gamma+integral_0^infinity`
`[exp(-s)-exp(-z s)]/(1-exp(-s)) ds`.

Set

`z=1/4+i t/2`

and take real parts:

`h_inf(t)`
`=-gamma-log pi`
`+ integral_0^infinity`
`[exp(-s)-exp(-s/4) cos(ts/2)]/(1-exp(-s)) ds`.

With `s=2r`,

`h_inf(t)`
`=-gamma-log pi`
`+2 integral_0^infinity`
`[exp(-2r)-exp(-r/2)cos(tr)]/(1-exp(-2r)) dr`.

Subtract the same identity at `t=0`. The constant part cancels and gives

`h_inf(t)-h_inf(0)`
`=2 integral_0^infinity`
`exp(-r/2)/(1-exp(-2r)) * (1-cos(tr)) dr`.

The special value

`psi(1/4)=-gamma-pi/2-3log2`

gives the displayed exact `h0`.

## 2. Plancherel converts the multiplier to translation energy

Use

`f_hat(t)=integral_R f(x) exp(-itx) dx`

and

`<f,g>=(1/(2pi)) integral f_hat(t) conjugate(g_hat(t)) dt`.

For translation,

`(T_r f)^hat(t)=exp(i t r) f_hat(t)`

up to the harmless opposite sign convention if `T_r` is defined in the other direction. Hence

`<T_r f-f,T_r g-g>`
`=(1/(2pi)) integral`
`|exp(i t r)-1|^2 f_hat(t) conjugate(g_hat(t)) dt`
`=(1/pi) integral`
`(1-cos(tr)) f_hat(t) conjugate(g_hat(t)) dt`.

Insert Section 1 into

`Q_arch(f,g)=(1/(2pi)) integral h_inf(t)`
`f_hat(t) conjugate(g_hat(t)) dt`

and interchange the positive/absolutely convergent integrals on the declared compact-support form domain. This gives

`Q_arch(f,g)=h0<f,g>+integral_0^infinity w(r)`
`<T_r f-f,T_r g-g> dr`.

For `f=g`, the nonconstant part is manifestly nonnegative:

`Q_arch(f,f)=h0||f||^2+integral_0^infinity w(r)||T_r f-f||^2 dr`.

## 3. Matrix form for any finite orthonormal basis

Let `phi_1,...,phi_m` be an orthonormal finite family and define the translation-overlap matrix

`R(r)_(ij)=<phi_i,T_r phi_j>`.

Then the archimedean Gram matrix is

`boxed: A_arch`
`= h0 I + integral_0^infinity w(r)`
`  [2I-R(r)-R(r)^*] dr`.

The integrand matrix is positive semidefinite for every `r`, because

`2I-R-R^*`

is the Gram matrix of the vectors `T_r phi_j-phi_j`.

This is a basis-independent exact identity.

## 4. Exact finite-support cutoff

Assume every basis function is supported in one common interval of diameter `Rmax`.

For `r>Rmax`, the original and translated supports are disjoint, so

`R(r)=0`.

Therefore

`A_arch`
`= h0 I`
`+ integral_0^Rmax w(r)[2I-R(r)-R(r)^*] dr`
`+ 2 I integral_Rmax^infinity w(r) dr`.

The remaining scalar tail is elementary. Put

`q=exp(-Rmax/2)`.

Since

`w(r)=exp(-r/2)/(1-exp(-2r))`,

the substitution `z=exp(-r/2)` gives

`integral_Rmax^infinity w(r) dr`
`= 2 integral_0^q dz/(1-z^4)`
`= atanh(q)+atan(q)`.

Hence

`boxed: A_arch`
`= h0 I`
`+ integral_0^Rmax w(r)[2I-R(r)-R(r)^*] dr`
`+ 2[atanh(exp(-Rmax/2))+atan(exp(-Rmax/2))] I`.

The improper frequency integral is gone. Only a finite physical-translation integral remains.

## 5. Specialization to the complete `H_log3` N=8 branch-sine section

For the four labelled intervals

`[-log2,0]`, `[0,log2]`, `[-log3,-log2]`, `[log2,log3]`,

all basis functions lie in

`[-log3,log3]`.

Thus

`Rmax=2 log3`.

The exact scalar exterior tail is

`2[atanh(1/3)+atan(1/3)] I`,

because

`exp(-(2log3)/2)=1/3`.

So the complete archimedean 32x32 finite-section matrix is reduced to

`h0 I`
`+ integral_0^(2log3) w(r)[2I-R(r)-R(r)^T] dr`
`+2[atanh(1/3)+atan(1/3)]I`.

No frequency cutoff `T` and no numerical digamma evaluation remain.

## 6. Exact translation overlaps for the branch-sine basis

For

`phi_i(x)=sqrt(2/ell_i) sin(alpha_i(x-a_i))`

on `[a_i,b_i]`, and similarly `phi_j`, the overlap

`R_ij(r)=integral phi_i(x) phi_j(x+r) dx`

is taken over

`[max(a_i,a_j-r), min(b_i,b_j-r)]`.

When this interval is nonempty, product-to-sum gives an elementary antiderivative:

`sin(alpha_i x+p_i) sin(alpha_j x+q_j(r))`
`=1/2 cos((alpha_i-alpha_j)x+p_i-q_j(r))`
` -1/2 cos((alpha_i+alpha_j)x+p_i+q_j(r))`.

Therefore every `R_ij(r)` is a piecewise elementary combination of

`r`, `sin(c r+d)`, `cos(c r+d)`

on a finite partition whose breakpoints are endpoint differences of the support intervals.

For the four `log2/log3` branches the nonnegative breakpoints are exactly among

`0`, `log(3/2)`, `log2`, `log3`, `log4`, `log6`, `log9`.

Thus validated evaluation of the full arch matrix reduces to finitely many one-dimensional elementary-function interval integrals.

## 7. Regularity at the apparent `r=0` singularity

Although

`w(r)=1/(2r)+O(1)`

as `r->0+`, the matrix factor

`2I-R(r)-R(r)^*`

vanishes at `r=0`.

For the zero-extended Dirichlet sine basis, each basis function lies in `H^1(R)`. Translation strong differentiability implies

`||T_r phi-phi||_2=O(r)`,

so the quadratic matrix factor is `O(r^2)` and the product with `w(r)` is `O(r)`.

Hence the physical integral has a removable endpoint singularity and is well suited to finite validated quadrature after the local expansion is encoded.

## 8. Floating cross-check against the former frequency integral

A direct floating implementation of the exact physical formula was compared with the previous positive-frequency digamma quadrature at cutoff `T=2500` on the `N=8` 32-dimensional branch-sine section.

The operator-norm difference was approximately

`3.4e-6`,

consistent with the independently derived frequency-tail scale at that cutoff.

The physical formula itself showed rapid Gauss-rule stabilization: changing the finite-r integral quadrature order over the exact breakpoint partition altered the resulting matrix only around ordinary double-precision roundoff in the tested orders.

This is a diagnostic cross-check, not an interval certificate.

## 9. New cutoff-free finite-section diagnostic

Using the physical arch matrix together with the exact finite prime-power and two pole channels, the floating `N=8` full `H_log3` Gram matrix had

`lambda_min ~= 7.1e-13 >0`.

Equivalently, the full threshold block at

`eta=1`

had zero negative eigenvalues in ordinary floating arithmetic.

The corresponding largest normalized-response singular value was numerically only about `5.7e-11` below one.

This is precisely the regime where floating arithmetic must **not** be interpreted as proof. The value is recorded only to identify the required validation scale.

At the lower diagnostic thresholds the physical-space calculation reproduced the prior strict floating counts:

- `eta=0.9`: 8 negative directions;
- `eta=0.99`: 6;
- `eta=0.999`: 5.

## 10. Why this is a substantial certification improvement

Before this identity, the diagonal blocks required either

- integration of the digamma multiplier to a large frequency cutoff plus a tail theorem, or
- an imported cutoff-free implementation in another Galerkin coordinate system.

Now the branch-sine basis has its own cutoff-free representation:

`DIGAMMA INFINITE FREQUENCY INTEGRAL`
`-> FINITE PHYSICAL TRANSLATION INTEGRAL + EXACT SCALAR TAIL`.

The only remaining numerical special functions are elementary constants/functions (`gamma`, `log`, `atan`, `atanh`, `exp`, `sin`, `cos`), all amenable to standard ball/interval arithmetic.

This also preserves the BRC branch support exactly: the translation-overlap matrix retains which old/shell branch pair is interacting at each displacement.

## 11. Smallest unresolved unit

Build an actual interval/ball implementation of Section 4 for the `N=8` four-branch sine basis:

1. partition `r in [0,2log3]` at all support endpoint differences;
2. use the exact product-to-sum formula for each `R_ij(r)`;
3. treat `r=0` with its removable local expansion;
4. interval-integrate the finite elementary kernel;
5. add the exact scalar tail and the finite prime/pole matrices;
6. perform interval `LDL*` inertia certification at `eta=0.9,0.99,0.999,1`.

At `eta=1`, the floating margin is around `10^-12` in the threshold matrix, so a real proof will require substantially more than ordinary double precision.

## 12. Hard boundaries

- `CUTOFF-FREE FINITE MATRIX != INFINITE-DIMENSIONAL WEIL POSITIVITY`.
- The physical formula does not eliminate the Galerkin-complement proof obligation.
- The `eta=1` positive floating eigenvalue is not an interval certificate.
- The translation integral must be validated; ordinary Gauss convergence is only diagnostic evidence.
- No RH proof is claimed.
