# RH / Dickman parity resolvent / critical-depth prime-source analysis

Status: `RESEARCH FRONTIER / EXACT IDENTITIES + PRIOR-ART SYNTHESIS + EMPIRICAL SPECTRAL PILOT / NOT A PROOF OF RH`
Date: `2026-09-06`
Project: `Enterprise Math / 进取数论`
Scope: `RH / Möbius / Dickman-Buchstab / friable integers / BRC / X6 fixed-width growing-depth provenance`

## 0. Typing guard

P000 is unchanged. Arithmetic factor labels, prime packets, Mellin variables, and smoothness depth are provenance/relation coordinates, not additional native X6 spatial axes. The six native axes remain the six primitive spatial directions.

BRC discipline remains:

`PROVENANCE > MULTIPLICITY > BOOLEAN SUPPORT`.

Positive path multiplicity, positive entropy, and signed Möbius cancellation are distinct. No positive BRC multiplicity is to be interpreted as signed cancellation without an explicit observer theorem.

---

## 1. Base parity kernel at z=-1: all asymptotic powers vanish

Tenenbaum--Weingartner's generalized Buchstab kernel `omega_z(u)` admits, for `1/2<=|z|<=2`, an all-orders expansion of the form

`omega_z(u)=e^(-gamma z) sum_{0<=k<=K} b_k(z) u^(z-1-k)/Gamma(z-k) + O_K(u^(Re z-2-K)).`

At the parity point `z=-1`, every reciprocal gamma coefficient vanishes:

`1/Gamma(-1-k)=0` for all `k>=0`.

Therefore

`omega_-1(u)=O_A(u^-A)` for every fixed `A>0`.

In the present Enterprise lineage this is the already identified exact identity

`omega_-1(u)=rho'(u)=-rho(u-1)/u`,

where `rho` is Dickman's function.

Freeze:

`CONTINUUM_ROUGH_PARITY_IS_NOT_THE_RH_BOTTLENECK`.

The signed continuum rough layer has super-polynomial decay in the depth variable u.

---

## 2. Exact positive Dickman parity resolvent

The dense-divisor spectral denominator is

`Mhat_z(s)=int_1^infinity omega_z(u)/(u+1)^(s+1) du`

(initially in its convergence region, then by continuation in the cited theory).

The normalized response has the form

`qhat_z(s)/Gamma(z)=Gamma(s+1-z)/[Gamma(s+1)(1+Mhat_z(s))]`.

At `z=-1`, the gamma ratio is `s+1`, hence

`R_-1(s)=(s+1)/(1+Mhat_-1(s)).`

Use `omega_-1(u)=rho'(u)` and integrate by parts. One obtains exactly

`1+Mhat_-1(s)=(s+1) int_0^infinity rho(u)(u+1)^(-s-2) du`.

The apparent zero at `s=-1` is therefore removable, and

`R_-1(s) = [int_0^infinity rho(u)(u+1)^(-s-2) du]^-1.`

With `u=e^t-1`,

`R_-1(s)^-1 = int_0^infinity rho(e^t-1)e^{-(s+1)t}dt.`

Thus a signed parity response is converted into the reciprocal of the Laplace transform of a purely positive Dickman Cell density.

Candidate project name:

`DICKMAN_LOG_LAPLACE_PARITY_RESOLVENT`.

If U has density `e^-gamma rho(u)du` and `Y=log(1+U)`, then on `Re s=-2`, the normalized denominator is the characteristic function of Y. This is an arithmetic/spectral statement only, not a physical force identification.

### Empirical spectral pilot

A conversation-local high-accuracy method-of-steps / quadrature experiment found a stable first visible nontrivial zero near

`s_* ~= -1.99646752084011 +/- 6.25979879844824 i`.

This is empirical only. No rigorous rightmost-zero claim is made. The near `Re s=-2` location suggests an approximately `v^-2` first parity mode after the removable degeneracy, but this must not be promoted without certification.

---

## 3. Hildebrand critical depth and saddle-depth duality

Hildebrand's classical smooth-number criterion places the RH transition at

`y=(log x)^(2+o(1))`.

Write

`y=(log x)^kappa`, `L=log x`, `ell=log L`, `u=L/(kappa ell)`.

The smooth-number saddle is

`beta=1-xi(u)/log y`,

where `e^{xi(u)}=1+u xi(u)` and

`xi(u)=log u+log log u+O(loglog u/log u)`.

Substitution gives

`beta = 1-1/kappa + (log kappa)/(kappa ell) + O(log ell/ell^2)`.

Hence the asymptotic saddle-depth duality

`u ~ (1-beta) log x/loglog x`.

At the critical line `beta=1/2`,

`u_RH ~ (1/2) log x/loglog x`.

This independently matches the previously derived Enterprise fixed-label transport complexity scale `Omega(log x/loglog x)`.

Freeze:

`RH_CRITICAL_ARITHMETIC_DEPTH ~ log X/loglog X`.

The earlier exact X6 terminalization at `y=x^(1/7)` has fixed `u=7`; its saddle tends to 1 as x grows and therefore remains globally subcritical for RH. It is a finite certificate, not an RH-depth mechanism.

---

## 4. Dickman density itself reaches square-root scale at critical depth

At

`y=(log x)^2`, `u~log x/(2loglog x)`,

Dickman's standard asymptotic

`log rho(u)=-u(log u+loglog u-1+o(1))`

gives

`rho(u)=x^(-1/2+o(1)).`

Since

`rho'(u)=-rho(u-1)/u`

and `rho(u-1)/rho(u)~u log u` at this scale,

`|rho'(u)|=x^(-1/2+o(1)).`

Thus the continuum rough parity kernel naturally lands at square-root scale precisely at the Hildebrand critical depth. The `1/2` exponent is not inserted by hand in this continuum model.

However, Hildebrand's equivalence shows that transferring this continuous carrier to actual discrete smooth-number counts at the same depth is already RH-strength. Therefore any Enterprise proof must use genuinely signed/provenance structure beyond positive smooth-count stability.

---

## 5. Exact prime-discrete source channel from Gorodetsky's correction factor

Gorodetsky decomposes the smooth-number correction as `G=G1 G2`, with

`log G1(s,y)=sum_{n<=y} Lambda(n)/(n^s log n)`
`-[log(zeta(s)(s-1))+loglog y+gamma+I((1-s)log y)].`

Differentiate in the Stieltjes sense with respect to y. The derivative of the continuous bracket is exactly `y^-s dy/log y`. Hence

`d_y log G1(s,y)= y^-s/log y * d(psi(y)-y)`.

Equivalently, for `y0<y`,

`log G1(s,y)-log G1(s,y0)`
`=int_{y0}^y t^-s/log t dE(t)`,

where `E(t)=psi(t)-t`.

This is an exact source injection formula. Prime-location discrepancy and prime-power provenance are separate channels.

### Positive-propagation no-go

For real `s=beta`, an atomic positive perturbation of the prime discrepancy at `t0` produces response

`t0^-beta/log t0 >0`.

At `beta=1/2` this is the square-root weight `t0^-1/2/log t0`.

Therefore a positive Green operator cannot manufacture RH cancellation from an arbitrary external prime-error source. Any successful mechanism must exploit the fact that the source itself is generated by prime provenance.

Freeze:

`POSITIVE_PROPAGATION_CANNOT_CREATE_RH_CANCELLATION_FROM_ARBITRARY_PRIME_ERROR`.

---

## 6. Squarefree/Möbius prime-only correction and critical rank one

For the Möbius Euler product, define

`Z_-(s,y)=prod_{p<=y}(1-p^-s)`

and the continuous prime-density carrier

`Z_-^cont(s,y)=exp(int_2^y log(1-t^-s)/log t dt)`.

Because

`sum_{p<=y}f(p)=int_2^y f(t)/log t dtheta(t)`,

we have the exact prime-only identity

`log[Z_-(s,y)/Z_-^cont(s,y)]`
`=int_2^y log(1-t^-s)/log t d(theta(t)-t).`

No non-squarefree prime-power counting channel is required in this representation.

Expand

`log(1-t^-s)=-t^-s-sum_{k>=2}t^(-ks)/k.`

At `Re s=1/2`, the `k=1` term is the unique channel capable of carrying power-scale critical growth. Under the classical PNT zero-free-region error, the `k>=2` discrepancy channels are convergent/stable after partial summation.

Thus the earlier Mellin/Newton `critical rank = 1` reappears at the exact prime-provenance source level:

`MOBIUS_PRIME_DISCRETE_CRITICAL_RANK = 1`.

The sole critical linear source is

`J_1/2(y)=int_2^y t^-1/2/log t d(theta(t)-t).`

Controlling this source by simply assuming square-root prime discrepancy is tautological; the project must seek a provenance constraint that acts before or within this source.

---

## 7. Prime-power bias is not the Möbius orientation bottleneck

Gorodetsky notes that an auxiliary function `alpha_y` coincides with the y-smooth indicator on squarefree integers and removes the `G2` proper-prime-power bias. Since Möbius already lives on squarefree Cells, `G2` must not be mistaken for the core Möbius obstruction.

Freeze:

`PRIME_POWER_BIAS_G2 != MOBIUS_ORIENTATION_BOTTLENECK`.

The relevant obstruction remains the prime-location channel `G1`, equivalently the prime-only theta-discrepancy representation above.

---

## 8. Selberg 1<->2 provenance is exact but zero-transparent

Let

`F(s)=-zeta'(s)/zeta(s)=sum Lambda(n)n^-s`.

Then

`-F'(s)+F(s)^2=zeta''(s)/zeta(s)`.

The coefficient side is

`Lambda(n)log n + (Lambda*Lambda)(n)`,

an exact arithmetic relation between a one-prime channel and a two-prime convolution channel. This is the canonical classical analogue of a `1 <-> 2` factor-provenance triad.

But `zeta''/zeta` retains poles at zeta zeros. Therefore the identity constrains the prime source but does not suppress off-critical zero modes.

Freeze:

`SELBERG_1_TO_2_TRIAD_IS_ZERO_TRANSPARENT`.

This further rules out fixed-order arithmetic-triad closure as an RH mechanism.

---

## 9. Oscillating friable averages: signed parity has genuine extra stability

De la Bretèche--Tenenbaum (2023) treat oscillating multiplicative functions with Dirichlet series close to negative powers of zeta. Their Corollary 1.4 specializes to the Möbius case `f=mu`, with positive majorant `f^dagger=1`, and gives a uniform bound of the shape

`|M(x,y;mu)|/Psi(x,y)`
`<< exp(-c0 u/(log_2 u)^2)/(log y)^2 + 1/L_r(y)`

for `u>2` (with `1<r<3/2`, and parameters as in the theorem).

Thus the signed smooth-sector parity is unconditionally much better mixed than a generic positive smooth count. This is genuine signed structure and should be reused before inventing a new parity mechanism.

At `y=(log x)^2`, the smooth support itself already satisfies the simple Rankin bound

`Psi(x,y)<=x^(1/2) prod_{p<=y}(1-p^-1/2)^-1`
`=x^(1/2+o(1)).`

Hence

`sum_{n<=x, P+(n)<=(log x)^2} mu(n)=O_epsilon(x^(1/2+epsilon))`

unconditionally, even before using signed cancellation.

Freeze:

`CRITICAL_SMOOTH_CORE_ALREADY_HAS_SQRT_SUPPORT_SIZE`.

Therefore RH difficulty lies in the nonsmooth provenance carrying at least one prime `>(log x)^2` and its reconnection to the critical smooth core.

---

## 10. BRC block compression and the missing shuffle entropy

The Dickman main exponent is

`-log rho(u)~u log u`.

If depth u is split into D equal blocks of size `h=u/D` and each block is compressed to a scalar before composition, multiplying local factors of size approximately `exp(-h log h)` only produces

`exp(-u log h)`,

missing the exponent `u log D`.

BRC retains an exact combinatorial carrier for this missing cross-block information:

`B_shuffle = u!/(h!)^D` for integer `u=Dh`.

Stirling gives

`log B_shuffle = u log D + O(D log h)`.

Thus at the level of leading combinatorial entropy,

`u log u = D(h log h)+u log D+O(u)`.

This is the same multinomial structure already encoded by `B_fact=Omega!/prod e_i!`.

Important boundary:

`SHUFFLE_MULTIPLICITY_RESTORES_GEOMETRIC_INFORMATION != SIGNED_ARITHMETIC_CANCELLATION`.

The point is architectural: scalar layer compression deletes cross-layer provenance at exactly the exponent scale needed by the global Dickman carrier. A growing-depth BRC operator must retain the shuffle/provenance fiber until an operation-safe arithmetic observer is applied.

---

## 11. Four-way critical-depth convergence

The scale `log x/loglog x` now appears independently in:

1. Hildebrand's smooth-number RH transition, with `u_RH~(1/2)log x/loglog x`;
2. the previously proved fixed-label transport obstruction `K(x)=Omega(log x/loglog x)`;
3. the number of fixed-log contractions needed to accumulate a power-scale effect;
4. the maximal squarefree prime-factor complexity `max_{n<=x} omega(n)~log x/loglog x` (primorial scale).

This strengthens the project interpretation:

`X6 WIDTH IS FIXED; RH-CRITICAL PROVENANCE DEPTH GROWS`.

It does not alter P000 dimension.

---

## 12. New smallest unit

Do not continue by:

- scalar positive propagation of an arbitrary `psi-y` source;
- fixed-depth X6 terminalization;
- fixed-order Selberg/triadic convolution identities;
- prime-power bias analysis as if it were Möbius parity;
- counting BRC shuffles as independent signed samples.

The surviving technical target is:

**Construct a fixed-width / growing-depth, provenance-preserving error propagator for the prime-only critical source `J_1/2`, in which cross-layer shuffle information is retained, and prove a signed/collision bound that is stronger than simply assuming square-root control of `theta(t)-t`.**

A useful exact starting point is the prime-only source identity in Section 6 together with the rough/smooth factor decomposition at `y=(log x)^2`. Any claimed contraction must be audited against Hildebrand's RH equivalence and against the nonzero first variation of the source map.

No RH proof is claimed.