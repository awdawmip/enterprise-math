# RH continuum Dickman-Gamma counterterm and critical boundary layer

Status: `RESEARCH FRONTIER / EXACT CONTINUUM THEOREM + ASYMPTOTIC PROFILE + DISCRETE TRANSFER GAP / NOT A PROOF OF RH`
Date: `2026-09-07`
Project: `Enterprise Math / 进取数论`
Scope: `RH / Möbius / generalized Dickman carrier / rough-divisor BRC / hyperbola counterterm`
Parent frontier:

- `RH_HYPERBOLA_COUNTERTERM_TOWER_20260907.md`
- `RH_DICKMAN_PARITY_RESOLVENT_CRITICAL_DEPTH_20260906.md`

## 0. Purpose and typing guard

The parent note found the highest-logarithmic fixed-order counterterm tower

`-A_X t exp(-L_Xt).`

The present note constructs the exact continuum rough-divisor carrier that produces this tower and identifies the missing Gamma correction.

The generalized Dickman equation, its Laplace transform, and Gamma asymptotics belong to classical analysis/probabilistic number theory. The project contribution here is the typed composition with the rough/small Alladi-Duhamel carrier and the identification of the critical boundary-layer counterterm. No generic novelty claim is made before a dedicated literature audit.

P000 is unchanged. The variable `u=log X/log Y` is arithmetic residual depth, not a spatial axis.

---

## 1. Continuous squarefree rough-divisor partition

After the prime-density substitution

`p=Y^x,`

we have

`dp/(p log p)=dx/x.`

Thus the natural continuous carrier for a squarefree rough divisor with prime-log coordinates `x_i>=1` and product budget `prod p_i<=Y^u` is

`R_t(u)`
`= sum_(m>=0) (-t)^m/m!`
`  int_(x_i>=1, x_1+...+x_m<=u)`
`  dx_1...dx_m/(x_1...x_m).`

The `m=0` term is `1`. For each finite `u`, only `m<=floor(u)` occurs, so the expression is finite.

This is the continuum analogue of

`M_rough(V;t)`
`=sum_(a<=V,P^-(a)>Y)mu(a)t^omega(a).`

The coordinates remain labeled/provenance coordinates until the symmetric integral is taken. The factor `1/m!` removes ordering only after all m branches have been retained.

---

## 2. Exact Laplace transform

Let

`g(x)=1_(x>=1)/x`

and let `g^(*m)` denote additive convolution. Then

`R_t(u)`
`=1+sum_(m>=1)(-t)^m/m!`
`  int_0^u g^(*m)(v)dv.`

Put

`E_1(s)=int_1^infinity e^(-sx)dx/x.`

For `Re s>0`, convolution and the cumulative integral give exactly

`Laplace[R_t](s)`
`= (1/s)sum_(m>=0)(-t E_1(s))^m/m!`
`= exp(-tE_1(s))/s.`

Hence

`boxed(Laplace[R_t](s)=e^(-tE_1(s))/s).`

This transform is an exact continuum BRC composition law: independent rough-log branches exponentiate before the product-budget observer is inverted.

---

## 3. Exact generalized Dickman delay equation

Differentiate

`s Laplace[R_t](s)=exp(-tE_1(s)).`

Since

`E_1'(s)=-e^(-s)/s,`

we obtain

`Laplace[R_t](s)+s d/ds Laplace[R_t](s)`
`=t e^(-s)Laplace[R_t](s).`

Using

`Laplace[uR_t'(u)]`
`=-(Laplace[R_t]+s d/ds Laplace[R_t]),`

inverse Laplace transformation yields

`u R_t'(u)=-t R_t(u-1)` for `u>1`,

with

`R_t(u)=1` for `0<=u<=1`.

Thus `R_t` is the generalized Dickman carrier with parameter `t`.

At `t=1`,

`R_1(u)=rho(u),`

the ordinary Dickman function.

This connects the present squarefree rough-divisor partition directly to the Dickman parity branch already used in the parent frontier.

---

## 4. Gamma-corrected large-depth asymptotic

As `s->0` in the right half-plane,

`E_1(s)=-gamma-log s+O(s).`

Therefore

`Laplace[R_t](s)`
`=e^(gamma t)s^(t-1)(1+O_t(s)).`

For fixed `t` with `0<Re t<1`, Laplace inversion gives

`R_t(u)`
`~ C_D(t) u^(-t),`

where

`C_D(t)=e^(gamma t)/Gamma(1-t).`

The Gamma factor is essential. Its logarithm is

`log C_D(t)`
`=gamma t-log Gamma(1-t)`
`=-sum_(n>=2) zeta(n)t^n/n`

near `t=0`.

Hence

`C_D(t)=1+O(t^2)`

and there is no linear correction to the highest-logarithmic tower found previously.

At `t=1`,

`1/Gamma(1-t)=1/Gamma(0)=0.`

Thus the algebraic `u^-t` coefficient vanishes. The ordinary Dickman branch then decays faster than every fixed power, consistently with the parent result that the continuum parity channel has no surviving algebraic asymptotic coefficients.

Freeze:

`CONTINUUM_PARITY_SUPERDECAY = GAMMA_ZERO_AT_t=1`.

This is a continuum identity, not a statement about the discrete Mertens function.

---

## 5. Continuous one-small-prime insertion channel

Fix a weight exponent `beta>0`. A small prime `q<=Y` consumes the logarithmic budget

`r_q=log q/log Y.`

Conditioning on that prime changes the available rough depth from `u` to `u-r_q`.

The prime-density continuum version of the zeroth suffix source `A_0=-S_(beta,Y)` therefore has coupling defect

`C_lin(X,Y;t)`
`= -int_2^Y q^(beta-1)/log q`
`    [R_t(u-log q/log Y)-R_t(u)]dq.`

Use the Gamma-corrected asymptotic. Uniformly for `0<=log q/log Y<=1` and fixed `0<Re t<1`,

`R_t(u-r)-R_t(u)`
`~ C_D(t)t r u^(-t-1).`

Since

`int_2^Y q^(beta-1)dq`
`~Y^beta/beta,`

we obtain

`C_lin(X,Y;t)`
`~ -A_X t C_D(t)u^(-t),`

where

`A_X=Y^beta/(beta log X)`

and

`u=log X/log Y.`

Equivalently,

`boxed(C_lin ~ -[Y^beta/(beta log X)]`
`              t [e^(gamma t)/Gamma(1-t)]`
`              (log Y/log X)^t).`

This is the Gamma-refined continuum counterterm.

---

## 6. Recovery of the fixed-order tower

Write

`L_X=log u=log(log X/log Y).`

Then

`u^(-t)=e^(-L_Xt).`

Because `C_D(t)=1+O(t^2)`, the highest power of `L_X` in the coefficient of `t^m` is

`(-1)^m A_X L_X^(m-1)/(m-1)!`,

exactly the tower derived from the discrete hyperbola-shell geometry.

The lower powers of `L_X` are organized by the Gamma factor

`exp(-sum_(n>=2)zeta(n)t^n/n).`

Thus the previous formal tower was not an unrelated exponential guess. It is the leading-log projection of the exact generalized Dickman carrier.

Freeze:

`HYPERBOLA_COUNTERTERM_TOWER = LEADING_LOG_OF_DICKMAN_GAMMA_PROFILE`.

---

## 7. Critical boundary-layer scaling

Assume the balance

`Y=(log X)^kappa,`

`kappa beta=1.`

Then

`A_X->1/beta`

and

`u=log X/(kappa loglog X)->infinity.`

Let

`t=tau/log u`

with `tau` in a fixed compact set. Since

`C_D(t)=1+O(1/(log u)^2)`

and

`u^(-t)=e^(-tau),`

we obtain the exact continuum scaling profile

`log u * C_lin(X,Y;tau/log u)`
`-> -(tau/beta)e^(-tau).`

For the RH specialization `kappa=2`, `beta=1/2`,

`log u * C_lin`
`-> -2tau e^(-tau).`

This proves, inside the continuum model, that the product-budget defect is concentrated in a boundary layer of width

`1/log u ~ 1/loglog X.`

The profile vanishes both at `tau=0` and as `tau->infinity`, with maximal magnitude at `tau=1`.

---

## 8. Two different cancellations at t=1 and t=0

The same Gamma-Dickman profile clarifies two endpoints.

### `t=0`

The rough phase is identically `1`, so covariance centering removes the constant mode. The derivative at zero remains nonzero because the boundary layer has slope `-A_X`.

### `t=1`

The Gamma coefficient vanishes. The continuum rough partition is the Dickman function and has super-polynomial depth decay.

Thus:

- cancellation at `t=0` is ordinary covariance centering;
- cancellation at `t=1` is a Gamma zero / Dickman superdecay;
- neither implies control of the discrete prime-intensity remainder or of a growing Alladi jet family.

---

## 9. What the continuum theorem does not solve

The exact continuum carrier removes an ambiguity in the project architecture, but several discrete gaps remain.

1. The actual discrete rough sum is not equal to `R_t(u)` at the Hildebrand critical depth without a transfer theorem.
2. The full suffix Alladi polynomial contains higher small-prime jets; Section 5 treats the leading one-small-prime insertion channel.
3. The prime-density replacement erases the one-point source discrepancy `J_(1/2)(Y)`.
4. A fixed-t continuum asymptotic does not imply uniform control for complex `t` or Taylor order growing with `X`.
5. At `t=1`, the continuum Gamma zero may be spoiled by discrete source errors; proving otherwise at square-root scale is RH-strength.

Freeze:

`CONTINUUM_GAMMA_ZERO != DISCRETE_RH_CANCELLATION`.

`DICKMAN_COUNTERTERM_REMOVAL != PRIME_INTENSITY_CONTROL`.

---

## 10. New smallest research unit

The deterministic rough/small product-budget carrier is now explicit:

`B_D(X,Y;t)`
`= -[Y^beta/(beta log X)]`
`  t [e^(gamma t)/Gamma(1-t)]`
`  (log Y/log X)^t.`

The next task is to insert this carrier into the exact discrete Abel identity

`C_X(t)`
`= (1/X)sum_U`
`  [M_rough(floor(X/U);t)-1]`
`  [A^suf_U(t-1)-G_X(t-1)]`

and define a discrete-minus-continuum residual with all repair coordinates retained.

The first admissible theorem would establish a nontrivial uniform bound for

`C_X(t)-B_D(X,Y;t)`

on the boundary-layer window

`|t|<=c/log u,`

separating explicitly:

- the prime-intensity source;
- the higher suffix-jet contribution;
- floor-quotient error;
- the high-arity tail;
- the discrete rough-sum error.

A successful bound here would remove the entire universal product-budget layer. It would still leave the deeper RH-critical provenance problem of depth `log X/loglog X`.

No RH proof is claimed.
