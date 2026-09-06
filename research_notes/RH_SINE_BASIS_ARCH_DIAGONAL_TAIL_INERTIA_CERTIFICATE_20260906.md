# RH sine-basis archimedean diagonal-tail / inertia certificate

Status: `TASK_RESEARCH / EXACT FINITE-BASIS TAIL THEOREM + EXPLICIT NUMERICAL BUDGETS / NOT YET INTERVAL MATRIX CERTIFIED / NOT AN RH PROOF`
Date: `2026-09-06`
Researcher-ID: `EM-DIRECT-7C1A42`
Scope: `RH / Weil square-shell / branch-sine Galerkin / archimedean frequency tail / threshold inertia`

## 0. Purpose

The current `log2 -> log3` program has isolated and rigorously bounded the regular **cross** tail. The remaining numerical obstruction was the finite-cutoff evaluation of the archimedean diagonal blocks `A_2,D_2`.

For the support-exact Dirichlet sine basis there is an additional structural gain: each basis transform decays like `tau^-2`, so the omitted archimedean Gram tail decays like `log(T)/T^3`, much faster than a generic non-endpoint-vanishing Galerkin basis.

This note proves an explicit tail bound and an inertia-stability rule. It does not certify the finite integral on `[0,T]`; that is now the smallest remaining numerical unit.

## 1. Basis and exact Fourier decay

On an interval `[a,a+ell]`, let

`phi_k(x)=sqrt(2/ell) sin(k pi (x-a)/ell)`,

`alpha_k=k pi/ell`.

Under

`phi_hat_k(tau)=integral phi_k(x) exp(-i tau x) dx`,

one has exactly

`phi_hat_k(tau)`
`= sqrt(2/ell) exp(-i tau a)`
`  * alpha_k [1-(-1)^k exp(-i tau ell)]/(alpha_k^2-tau^2)`.

Hence, for `tau>T>alpha_k`,

`|phi_hat_k(tau)|^2`
`<= 8 alpha_k^2/[ell (tau^2-alpha_k^2)^2]`
`<= 8 alpha_k^2`
`   /[ell (1-(alpha_k/T)^2)^2 tau^4]`.

The extra `tau^-2` decay of the transform is the endpoint-vanishing advantage of this basis.

## 2. Elementary high-frequency bound for the archimedean multiplier

Put

`h(t)=Re psi(1/4+i t/2)-log pi`.

For `a=1/4`, `u=t/2`, the trigamma series gives

`h'(t)=u sum_(k>=0) (k+a)/[(k+a)^2+u^2]^2 >0`.

Thus `h` is increasing for positive `t`.

To obtain a simple upper derivative bound, set

`g_u(x)=(x+1/4)/[(x+1/4)^2+u^2]^2`.

This function is unimodal, so

`sum_(k>=0) g_u(k)`
`<= integral_0^infinity g_u(x) dx + max_(s>0) s/(s^2+u^2)^2`
`= 1/[2(u^2+1/16)] + 9/[16 sqrt(3) u^3]`.

Therefore

`h'(t)`
`<= 1/t + 9/[4 sqrt(3) t^2]`
`< 1/t + 13/(10 t^2)`.

A completely elementary positivity check at `t=7` is available from the convergent digamma series

`Re psi(a+i u)`
`= -gamma + sum_(k>=0) [1/(k+1) - (k+a)/((k+a)^2+u^2)]`.

At `a=1/4,u=7/2`, every term from `k=17` onward is negative. The first 17 terms sum exactly to

`81205020322416109955475984183157520590194283`
`/43857492434975295978699700118650648770475920`

which is greater than `1.8515` and less than `1.852`.

For `k>=17`, the magnitude of a negative tail term is at most `3/(4k^2)`, so the complete negative tail has magnitude less than `3/64`.

Using the elementary rigorous bounds

`gamma<0.6`, `log pi<1.2`,

we get

`h(7) > 1.8515 - 0.6 - 3/64 - 1.2 > 0`.

For an upper bound, `-gamma<0`, the post-16 tail is negative, and `log pi>1`, so

`h(7)<1.852-1<0.852`.

Integrating the derivative bound from 7 and using `log7>1.9` yields, for every `t>=7`,

`0 < h(t) < log t`.

This is all that is required for the tail certificate below.

## 3. Positive-semidefinite archimedean tail

For a real finite basis with transforms collected into the vector `F(t)`, the omitted archimedean matrix above cutoff `T` is

`Delta_arch(T)`
`= (1/pi) integral_T^infinity h(t) F(t)^* F(t) dt`.

For `T>=7`, Section 2 gives `h(t)>0`, so

`boxed: Delta_arch(T) >= 0}`

in Loewner order.

This statement is basis-independent. The quantitative `T^-3` estimate below uses the sine basis.

## 4. Explicit two-branch operator bound

Consider two reflected branches of equal length `ell`, with sine modes `k=1,...,N` on each branch. Let

`alpha_k=k pi/ell`

and choose

`T > max(7,alpha_N)`.

Since a positive-semidefinite matrix has operator norm at most its trace,

`||Delta_arch(T)|| <= Tr Delta_arch(T)`.

Using `h(t)<log t` and the Fourier bound from Section 1,

`Tr Delta_arch(T)`
`<= [16/(pi ell)]`
` * sum_(k=1)^N alpha_k^2/[1-(alpha_k/T)^2]^2`
` * integral_T^infinity (log t)/t^4 dt`.

The remaining integral is exact:

`integral_T^infinity (log t)/t^4 dt`
`= (3 log T + 1)/(9 T^3)`.

Therefore define

`boxed: B(ell,N,T)}`
`:= [16/(pi ell)] * (3 log T+1)/(9T^3)`
`   * sum_(k=1)^N alpha_k^2/[1-(alpha_k/T)^2]^2`.

Then

`boxed: 0 <= Delta_arch(T) <= B(ell,N,T) I}`.

This is an explicit cutoff-to-infinity Loewner certificate for the declared finite sine subspace.

## 5. First-step `N=8` budgets

For the old two branches,

`ell_old=log2`, `N=8`.

For the shell two branches,

`ell_shell=log(3/2)`, `N=8`.

At `T=2000`, direct high-precision evaluation of the closed formula gives

`boxed: B_A(2000) < 1.018379e-5}`,

`boxed: B_D(2000) < 5.092069e-5}`.

Representative larger-cutoff shell budgets are

- `B_D(5000) < 3.632e-6`;
- `B_D(10000) < 4.894e-7`;
- `B_D(50000) < 4.576e-9`;
- `B_D(100000) < 6.075e-10`;
- `B_D(200000) < 8.038e-11`.

The old-block budgets are smaller; for example

`B_A(200000) < 1.609e-11`.

All these values come from the explicit monotone formula above and are not spectral extrapolations.

## 6. Threshold-block one-sided inertia stability

Let `A_T,D_T` be the archimedean-frequency-truncated diagonal blocks with every non-archimedean finite term already included, and let the cross block `B` be held fixed at its declared cutoff-free or separately certified value.

Define

`H_eta,T = [[eta^2 A_T,B],[B^*,D_T]]`.

The cutoff-free finite-basis threshold matrix is

`H_eta,infinity = H_eta,T + E_T`,

where

`E_T = diag(eta^2 Delta_A(T), Delta_D(T)) >=0`.

Moreover

`||E_T|| <= beta_eta(T)`

with

`beta_eta(T)=max(eta^2 B_A(T), B_D(T))`.

Therefore

`n_-(H_eta,infinity) <= n_-(H_eta,T)`.

If `H_eta,T` has exactly `q` negative eigenvalues and its largest negative eigenvalue satisfies

`lambda_q(H_eta,T) < -beta_eta(T)`,

then every one of those `q` eigenvalues remains negative after adding `E_T`, while nonnegative eigenvalues cannot become negative under a positive-semidefinite perturbation. Hence

`boxed: n_-(H_eta,infinity)=q}`.

This is stronger than a symmetric Weyl perturbation rule because the high-frequency diagonal tail has a known sign.

## 7. Consequence for the corrected `prime+Cauchy` reference block

The floating `N=8` diagnostic found for

`B_ref=B_prime+B_Cauchy`

the following closest negative eigenvalues at `T=2000`:

- `eta=0.9`: about `-1.22e-4`;
- `eta=0.99`: about `-9.64e-4`;
- `eta=0.999`: about `-1.49e-4`.

All are farther below zero than

`B_D(2000)<5.093e-5`.

Therefore the **high-frequency diagonal tail itself cannot change the reference-block negative-inertia count** if an interval construction of the finite `[0,2000]` matrix confirms these gaps with sufficient margin.

This turns the current reference-block task into a finite validated-numerics problem:

`INTERVAL MATRIX ON [0,2000] -> LDL*/INERTIA -> APPLY EXPLICIT PSD TAIL`.

No integration to infinity is required.

## 8. Staged route for the full cross

The floating full-cross negative gaps suggest a useful certification schedule:

- at `eta=0.9`, the closest negative is about `-1.94e-4`; `T=2000` has a diagonal tail below `5.1e-5`;
- at `eta=0.99`, the closest negative is about `-1.05e-5`; `T=5000` has a shell tail below `3.64e-6`;
- at `eta=0.999`, the closest negative is only about `-4.3e-10`; a diagonal cutoff near `T=200000` gives a shell tail below `8.04e-11`.

For the last threshold, if the degree-50 regular-arch cross approximation from the companion note is used, its separate norm tail is below `1.622e-10`. The combined analytic uncertainty is then below roughly `2.43e-10` before finite-range quadrature/rounding error.

This makes `eta=0.999` difficult but no longer absurdly out of scale: its floating negative gap is larger than the two already-proved analytic tails combined. A true certificate still requires interval construction of the retained finite matrix.

## 9. Relation to the 2026 finite Guinand-Weil tail theorem

Akiva Groskin's 2026 finite Guinand-Weil work proves a stronger Cauchy-Stieltjes/total-positivity description of the omitted archimedean tail in the Connes-van Suijlekom frequency Galerkin coordinates and gives a general finite-cutoff certification budget.

The present theorem does **not** import that matrix formula into a different basis. Instead it uses only the same underlying high-frequency positivity and derives a new elementary basis-specific bound from the exact Fourier transforms of the branch-sine functions.

Thus

`CvS TAIL MATRIX FORMULA != DIRECTLY REUSED IN BRANCH-SINE BASIS`,

while

`ARCH HIGH-FREQUENCY POSITIVITY + EXACT SINE FOURIER DECAY -> NEW BASIS-SPECIFIC T^-3 CERTIFICATE`.

## 10. Current smallest unresolved unit

For the `N=8` first step, implement validated interval evaluation of the **finite** archimedean integrals on `[0,T]` for the sine basis, starting with the `prime+Cauchy` reference block at `T=2000`.

The proof obligation is now finite:

1. interval-enclose every `A_T,D_T` entry;
2. interval-enclose or analytically evaluate the retained cross entries;
3. interval-LDL* certify the negative inertia and the largest negative gap;
4. append the explicit positive tail `B_A,B_D` from this note;
5. only then promote the finite-basis reference inertia from floating diagnostic to certified result.

## 11. Hard boundaries

- `FINITE-BASIS CUTOFF-FREE INERTIA != INFINITE-OPERATOR INERTIA`.
- The theorem controls only the frequency tail beyond `T`; interval error on `[0,T]` remains separate.
- The reference-block floating gaps are not themselves proof data.
- A positive diagonal tail may remove negative eigenvalues; the explicit negative-gap test is mandatory.
- The `T^-3` rate depends on the endpoint-vanishing sine basis and should not be silently transferred to other Galerkin bases.
- No statement at `eta=1` and no RH proof is claimed.
