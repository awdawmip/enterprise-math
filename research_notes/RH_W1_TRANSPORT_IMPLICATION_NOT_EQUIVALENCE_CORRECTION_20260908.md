# Second correction: Möbius W1 transport is RH-equivalent with the full epsilon family

Status: `CORRECTION OF CORRECTION / EXACT`
Date: `2026-09-08`
Project: `Enterprise Math / 进取数论`
Scope: `RH / Möbius transport / earthmover W1 / Mellin continuation`

## 0. Retraction of the previous version

The first version of this file claimed that

`int_X^(2X)|M(t)|dt <<_eps X^(3/2+eps)`

was only an RH consequence and not an RH equivalence. That conclusion was based solely on the generic 1-Lipschitz spike inequality for M and ignored the arithmetic Mellin identity

`1/zeta(s)=s int_1^infinity M(x)x^(-s-1)dx`.

That omission was decisive. The previous version is retracted.

The spike argument remains correct as a **generic pointwise conversion**: an L1 bound at one scale only forces a `3/4`-type pointwise exponent for an arbitrary 1-Lipschitz sequence. But the Möbius cumulative function has additional global analytic structure, and the family of W1 bounds at all scales with arbitrary epsilon gives absolute Mellin convergence in every half-plane `Re(s)>1/2`.

Freeze:

`GENERIC_LIPSCHITZ_CONSEQUENCE != ARITHMETIC_MELLIN_CONSEQUENCE`.

---

## 1. Exact one-dimensional cut-flux identity

Let positive Möbius Cells and negative Möbius Cells carry unit masses. On the integer line, the net signed flux across the cut at location t is the cumulative charge

`M(t)=sum_{n<=t}mu(n)`.

Every transport plan has absolute cost at least the L1 norm of this cut flux, and the monotone same-rank transport attains equality. Thus, with standard finite-boundary bookkeeping,

`W1_Mobius = int |M(t)|dt`.

Freeze:

`1D_MONOTONE_MOBIUS_TRANSPORT_COST = L1_CUMULATIVE_MERTENS_FLUX`.

---

## 2. RH implies the dyadic W1 bound

RH is equivalent to

`M(t)=O_eps(t^(1/2+eps))`

for every eps>0. Hence

`int_X^(2X)|M(t)|dt <<_eps X^(3/2+eps)`.

---

## 3. The dyadic W1 epsilon-family implies RH

Assume that for every eps>0,

`int_X^(2X)|M(t)|dt <<_eps X^(3/2+eps)`

uniformly for large dyadic X.

Fix `sigma>1/2`. Choose

`0<eps<sigma-1/2`.

On a dyadic interval `[X,2X]`,

`int_X^(2X)|M(t)|t^(-sigma-1)dt`
`<=X^(-sigma-1) int_X^(2X)|M(t)|dt`
`<< X^(1/2-sigma+eps)`.

The exponent is strictly negative. Summing over dyadic X shows

`int_1^infinity |M(t)|t^(-sigma-1)dt < infinity`.

The convergence is locally uniform on compact subsets of `Re(s)>1/2` after choosing eps below the distance to the boundary. Therefore

`F(s)=s int_1^infinity M(t)t^(-s-1)dt`

is holomorphic in `Re(s)>1/2`.

For `Re(s)>1`, classical partial summation gives

`F(s)=sum mu(n)n^-s=1/zeta(s)`.

By analytic continuation, `1/zeta(s)` is holomorphic in `Re(s)>1/2`. Hence zeta has no zero there. The functional equation and zero symmetry give RH.

Therefore

`RH <=> for every eps>0, dyadic W1(X)<<_eps X^(3/2+eps)`.

Freeze:

`MOBIUS_W1_EPSILON_FAMILY = RH_EQUIVALENT`.

---

## 4. Why the spike argument did not contradict this

M is 1-Lipschitz, so a local spike of height H forces L1 area `>>H^2`. Therefore the W1 estimate at a **single scale**, viewed only as a metric inequality, yields at best

`H<<X^(3/4+o(1))`.

This does not contradict the RH equivalence because the Mellin argument uses:

1. the W1 estimate on every large dyadic scale;
2. arbitrary epsilon slack;
3. the exact Möbius Dirichlet/Mellin identity.

A generic Lipschitz sequence does not possess item 3.

Thus there are two valid implication mechanisms:

- metric/local: `W1 -> 3/4` by spike control;
- arithmetic/global: `W1 epsilon-family -> RH` by Mellin continuation.

The second is stronger only because it uses Möbius-specific global analytic structure.

---

## 5. Correct transport hierarchy

Do not order W1 and Winfinity merely by their generic norm strength when discussing RH equivalence.

For arbitrary transport states,

`W1` is weaker than `Winfinity`.

For the special Möbius cumulative state, however, the all-scale epsilon-family

`W1(X)<<_eps X^(3/2+eps)`

already forces RH through Mellin continuation.

The same warning applies to higher Lp flux moments: generic moment-to-sup inequalities and arithmetic RH-equivalence can have different logical strength.

---

## 6. Audit rule

Any future claim that a positive averaged Mertens quantity is weaker than RH must be checked not only by local spike constructions but also against

`1/zeta(s)=s int_1^infinity M(x)x^(-s-1)dx`.

If the proposed all-scale bound makes this integral absolutely convergent for every `Re(s)>1/2`, then it is already RH-strength even if a purely metric pointwise conversion appears weaker.
