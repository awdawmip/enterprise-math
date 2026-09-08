# RH commuting prime-shift critical operator

Status: `RESEARCH FRONTIER / EXACT FINITE OPERATOR FACTORIZATION + CRITICAL-RANK-1 REDUCTION / NOT RH`
Date: `2026-09-08`
Project: `Enterprise Math / 进取数论`
Scope: `rough parity / positive histogram / dilation operators / prime powers / continuous prime density / discrete prime source`

## 0. Input from the preceding criterion

The note

`RH_CRITICAL_ROUGH_ARITY_POSITIVE_HISTOGRAM_GAUGE_20260908.md`

reduced the first-cosine RH criterion, up to a subpolynomial finite-Euler gauge, to the parity output of a completely positive histogram counting the number of squarefree prime factors exceeding

`y=(log N)^2`.

The present note takes the exact positive prime-insertion circuit behind that histogram and factors it at the operator level.

The result gives another exact occurrence of `CRITICAL RANK = 1`: repeated-prime/prime-power channels are subpolynomially well-conditioned at the square-root norm, and the only power-critical channel is the primitive-prime dilation sum.

---

## 1. Scale-dilation algebra

Fix an ambient scale N. Let `X_N` be functions f on `[1,N]`, extended by zero below 1. For a>=1 define

`(D_a f)(T)=f(T/a)`.

Then

`D_a D_b=D_(ab)=D_b D_a`.

Thus all dilation operators commute.

Use the square-root triangular norm

`||f||_(1/2,N)=sup_(1<=T<=N)|f(T)|/sqrt(T)`.

Then exactly

`||D_a||<=a^-1/2`.

For the first-cosine seed

`f_0(T)=w(1/T)`, `w(x)=cos(pi x/2)`

(with f_0=0 for T<1), expansion of products of dilation operators reproduces the corresponding arithmetic cosine flow.

For example,

`prod_(p<=y)(I+D_p) f_0`

is the positive squarefree y-smooth flow, while

`prod_(p>y)(I-D_p) f_0`

is the rough Möbius/parity flow.

---

## 2. Exact finite logarithm of the rough squarefree operator

On the restricted space `X_N`, each `D_p` is nilpotent: `D_p^m=0` once `p^m>N`.

Therefore the logarithm series is finite as an operator on this space:

`log(I-D_p)=-sum_(k>=1)D_(p^k)/k`.

Define

`P_k(y,N)=sum_(y<p<=N^(1/k))D_(p^k)`.

Because all dilation operators commute,

`M_(y,N):=prod_(y<p<=N)(I-D_p)`

satisfies the exact identity

`M_(y,N)=exp[-sum_(k>=1)P_k(y,N)/k]`.

Split

`P_1=sum_(y<p<=N)D_p`

and

`A_>=2=sum_(k>=2)P_k/k`.

Then exactly

`M_(y,N)=exp(-P_1) exp(-A_>=2)`.

Freeze:

`ROUGH_PARITY_OPERATOR = PRIMITIVE_PRIME_EXPONENTIAL * REPEATED_PRIME_REPAIR`.

No analytic continuation is used.

---

## 3. The repeated-prime repair is subpolynomially conditioned at the RH scale

By the dilation norm,

`||A_>=2||`
`<=sum_(k>=2)(1/k)sum_(y<p<=N^(1/k))p^(-k/2)`.

The k=2 term is

`(1/2)sum_(y<p<=sqrt(N))1/p`
`=(1/2)[loglog sqrt(N)-loglog y]+O(1)`

by Mertens' theorem for primes.

For k>=3,

`sum_(k>=3)(1/k)sum_(p>y)p^(-k/2)`
`=O(sum_(p>y)p^-3/2)=O(1)`

(and in fact tends to zero with y).

Hence

`||A_>=2||`
`<= (1/2)log[(log N)/(2 log y)]+O(1)`.

Both the stable factor and its inverse obey

`||exp(+-A_>=2)||<=exp(||A_>=2||)`.

At

`y=(log N)^2`, `log y=2loglog N`,

we obtain

`||exp(+-A_>=2)||`
`<= (log N/loglog N)^(1/2+o(1))`
`=N^o(1)`.

Thus all repeated-prime / prime-power repair channels are stable in the exact square-root observer norm.

Freeze:

`PRIME_POWER_AND_REPEAT_CHANNELS_ARE_SQRT_NORM_STABLE`.

This is the finite operator analogue of the earlier Mellin/Newton observation that channels k>=2 are analytically stable to the right of the critical half-line.

---

## 4. Primitive-prime channel is the only critical operator

Up to the subpolynomially invertible stable factor,

`M_(y,N)`

is therefore equivalent, for the declared square-root triangular observer, to

`exp(-P_1)`,

where

`P_1=sum_(y<p<=N)D_p`.

The exponential expansion is

`exp(-P_1)`
`=sum_(j>=0)(-1)^j P_1^j/j!`.

It is a Poissonized BRC path sum over ordered primitive-prime insertion paths; repeated prime labels are allowed in this exponential, and the stable factor `exp(-A_>=2)` exactly repairs this to the squarefree/distinct-prime Euler product.

Thus the critical arithmetic information resides in one primitive-prime insertion operator rather than in a hierarchy of independent prime-power channels.

Freeze:

`FINITE_SCALE_MOBIUS_PRIME_SHIFT_CRITICAL_RANK = 1`.

---

## 5. Exact commuting discrete/continuum factorization

Define the continuous prime-density dilation operator

`L_(y,N)=int_y^N D_t dt/log t`.

Define the primitive-prime discrepancy operator

`E_(y,N)=P_1(y,N)-L_(y,N)`.

Every D_t commutes with every D_a. Hence

`[P_1,L]=0`, `[L,E]=0`.

Therefore exactly

`exp(-P_1)=exp(-L)exp(-E)`.

No time ordering, Dyson series, commutator correction, or noncommutative Green expansion is present.

Freeze:

`PRIME_DISCRETE_ERROR_IS_A_SINGLE_COMMUTING_EXPONENTIAL_SOURCE`.

This is compatible with, but sharper in this operator coordinate system than, earlier delay-Green formulations: those formulations resolve source injection in a recursive depth coordinate, whereas here the full multiplicative dilation algebra is simultaneously commuting.

---

## 6. Full critical rough-parity flow

Let

`B_y=prod_(p<=y)(I+D_p)`

be the positive squarefree small-prime base operator.

Then the scale flow of

`eta_y(n)=mu(n)^2(-1)^(r_y(n))`

is exactly

`S_(eta_y)=B_y M_(y,N) f_0`

on all T<=N.

Thus

`S_(eta_y)`
`=B_y exp(-A_>=2) exp(-L) exp(-E) f_0`.

The small-prime positive base has square-root norm operator bound

`||B_y||<=prod_(p<=y)(1+p^-1/2)`
`=exp(O(sqrt(y)/log y))`.

At `y=(log N)^2`, this is also `N^o(1)`.

The repeated-prime repair and small-prime base therefore cost no fixed power at the RH cutoff.

The continuum factor `exp(-L)` is the operator version of the continuous prime-density/Buchstab--Dickman model. The previously established continuum rough parity at critical depth has square-root scale; convolution with the small positive base and stable repeated-prime factor changes this by only `N^o(1)` in the declared norm.

Hence the sole unresolved power-scale issue is the action of

`exp(-E_(y,N))`.

---

## 7. Mellin/Fourier symbol of the remaining source

In log-scale coordinates, after the critical `T^(1/2)` normalization, D_p is a translation weighted by `p^-1/2`. Its Fourier/Mellin multiplier is `p^(-1/2-it)`.

Therefore the symbol of E at critical weight is

`E_hat(t)`
`=sum_(y<p<=N)p^(-1/2-it)`
` -int_y^N u^(-1/2-it)du/log u`.

This is exactly the primitive-prime discrete-versus-continuous discrepancy on the critical half-line.

All higher Euler channels have already been placed in the subpolynomial stable factor.

Thus the current smallest unresolved analytic unit is not a generic high-dimensional BRC cancellation problem. It is the effect, on one specific continuum critical state, of the single commuting multiplier

`exp[-E_hat(t)]`.

A whole-space operator-norm estimate by total variation is far too large and would throw away prime cancellation. An L2/average-frequency estimate alone is also insufficient for the pointwise all-scale RH observer without a mechanism recovering the generic half-derivative loss identified earlier.

---

## 8. Current frontier

The critical rough-parity problem now has the finite exact architecture

`POSITIVE SMALL-PRIME BASE`

`x SUBPOLYNOMIAL REPEATED-PRIME REPAIR`

`x CONTINUUM DICKMAN PARITY EVOLUTION`

`x ONE COMMUTING PRIMITIVE-PRIME DISCREPANCY EXPONENTIAL`.

Only the last factor is not already controlled at `N^o(1)` relative cost.

This gives a sharper research target:

Can one prove a provenance-preserving bound for

`exp(-E_(y,N))`

**on the specific continuum critical state**, not in a generic positive operator norm, that is `N^o(1)` in the triangular square-root observer?

Any proposed bound must be audited against the Mellin symbol above: controlling it by a supremum on the whole critical line is liable to be RH-equivalent; controlling only average frequency risks losing the half derivative needed for point evaluation.

This is the next admissible bottleneck.
