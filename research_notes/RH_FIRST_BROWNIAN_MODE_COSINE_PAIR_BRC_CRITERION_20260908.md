# RH first Brownian mode / cosine Pair-BRC rank-one criterion

Status: `RESEARCH FRONTIER / EXACT RH-EQUIVALENT SINGLE-MODE REFORMULATION / NOT A PROOF OF RH`
Date: `2026-09-08`
Project: `Enterprise Math / 进取数论`
Scope: `Mertens cumulative Gram / top Brownian eigenmode / cosine smoothing / Mellin zero-free kernel / Pair-BRC collision coherence`

## 0. Prior-art boundary

General Möbius/Mellin test-function criteria are classical in spirit: if a scaled test function has a Mellin transform that does not vanish in a target strip, sufficiently strong decay of the corresponding Möbius-weighted sum analytically continues `1/zeta`. Möbius/Müntz transformation literature contains this general principle. Recent Möbius Laplace/Fourier criteria provide further nearby examples.

The project-specific point of this note is the identification of a particularly simple zero-free Mellin test function with the **first eigenvector of the q=1 cumulative Brownian Gram**, and the resulting one-mode Pair-BRC collision-coherence packaging. No historical novelty is claimed for the generic Mellin principle.

---

## 1. q=1 Brownian eigenmode

The q=1 cumulative Gram is, after reversing integer order,

`C_N(i,j)=min(i,j)`.

Its first normalized eigenvector is

`v_1(j)=sqrt(4/(2N+1)) sin(j theta_1)`,

where

`theta_1=pi/(2N+1)`.

Returning to the original integer order gives the raw first-mode Möbius coefficient

`B_N=sum_{n<=N}mu(n) cos((n-1/2)theta_1)`.

The normalized spectral coefficient is

`c_1=sqrt(4/(2N+1)) B_N`.

The eigenvalue is

`lambda_1=1/[4 sin^2(theta_1/2)] ~ 4N^2/pi^2`.

---

## 2. Scale-invariant cosine weight differs only by O(1)

Define

`w(x)=cos(pi x/2)`, `0<=x<=1`,

and

`S_w(N)=sum_{n<=N}mu(n)w(n/N)`.

For every `1<=n<=N`,

`|(n-1/2)/(2N+1)-n/(2N)|`
`=(N+n)/[2N(2N+1)]`
`<=1/(2N+1)`.

Since cosine is 1-Lipschitz with respect to its angle,

`|B_N-S_w(N)|<=pi N/(2N+1)<pi/2`.

Therefore the first exact finite Brownian mode and the scale-invariant cosine-smoothed Möbius sum are equivalent at every power scale:

`B_N=S_w(N)+O(1)`.

---

## 3. Mellin transform of the cosine weight is zero-free for Re(s)>0

Let

`W(s)=int_0^1 x^(s-1) cos(a x) dx`,

with `a=pi/2`.

For `Re(s)>0`, integrate by parts:

`W(s)=a/s * J(s)`,

where

`J(s)=int_0^1 x^s sin(a x) dx`.

A second integration by parts gives

`J(s)=[1-a W(s+2)]/(s+1)`

because `sin(a)=1` and `cos(a)=0`.

Hence the exact recurrence

`W(s)=a/[s(s+1)] * [1-a W(s+2)]`.

If `sigma=Re(s)>0`, then because `cos(ax)>=0` on `[0,1]`,

`|W(s+2)|`
`<=int_0^1 x^(sigma+1)cos(ax)dx`
`<int_0^1 x^(sigma+1)dx`
`=1/(sigma+2)`
`<1/2`
`<1/a=2/pi`.

Therefore

`|a W(s+2)|<1`

and the bracket `1-aW(s+2)` cannot vanish. Since neither s nor s+1 vanishes in `Re(s)>0`,

`W(s) != 0 for every Re(s)>0`.

Freeze:

`COSINE_TOP_MODE_MELLIN_TRANSFORM_ZERO_FREE_ON_Re(s)>0`.

---

## 4. Exact Mellin identity for the scaled Möbius sum

For `Re(s)>1`, absolute convergence permits

`int_1^infinity S_w(X)X^(-s-1)dX`
`=sum_n mu(n) int_n^infinity w(n/X)X^(-s-1)dX`.

Set `u=n/X`. Then

`int_n^infinity w(n/X)X^(-s-1)dX`
`=n^-s int_0^1 w(u)u^(s-1)du`
`=n^-s W(s)`.

Thus exactly

`int_1^infinity S_w(X)X^(-s-1)dX`
`=W(s)/zeta(s)`.

---

## 5. Single cosine mode is RH-equivalent

### RH -> cosine square-root bound

Under RH,

`M(x)=O_eps(x^(1/2+eps))`.

Partial summation, using `w(1)=0` and bounded derivative, gives

`S_w(X)=O_eps(X^(1/2+eps))`.

### cosine square-root bound -> RH

Assume for every eps>0,

`S_w(X)=O_eps(X^(1/2+eps))`.

Then for every `sigma>1/2`, choosing eps below `sigma-1/2`, the Mellin integral

`int_1^infinity S_w(X)X^(-s-1)dX`

converges absolutely and locally uniformly in `Re(s)>1/2`.

Hence `W(s)/zeta(s)` is holomorphic in that half-plane. Since `W(s)` has no zeros there (indeed none in `Re(s)>0`), `1/zeta(s)` is holomorphic in `Re(s)>1/2`. By zeta symmetry, RH follows.

Therefore

`RH <=> S_w(N)=O_eps(N^(1/2+eps))`.

Since `B_N=S_w(N)+O(1)`, also

`RH <=> B_N=O_eps(N^(1/2+eps))`.

In normalized Brownian coordinates,

`RH <=> c_1=N^o(1)`.

Because `lambda_1~4N^2/pi^2`, equivalently

`RH <=> lambda_1 |c_1|^2 <= N^(2+o(1))`.

Freeze:

`FIRST_BROWNIAN_GRAM_EIGENMODE_ALONE_IS_RH_STRENGTH`.

This is a reformulation, not a proof.

---

## 6. Consequence for the previous sqrt(N)-low-mode criterion

The full q=1 spectral criterion had shown that all modes above `sqrt N` are automatically RH-scale safe and that controlling the first `sqrt N` weighted modes is equivalent to the natural q=1 Gram bound.

The present result is logically sharper for RH equivalence:

**one does not need to control all first `sqrt N` modes; the very first Brownian mode already carries an RH-equivalent scalar condition.**

The other low modes may remain useful for quantitative energy decompositions or intermediate zero-free estimates, but they are analytically redundant for an equivalence statement.

Freeze distinction:

`FULL_q1_GRAM_RH_EQUIVALENT`

and

`TOP_q1_EIGENMODE_RH_EQUIVALENT`

are both true; the latter is the smaller carrier.

---

## 7. Finite positive Pair-BRC packaging

Because `w(x)>=0` on `[0,1]`, define the positive squarefree weight

`U_N(n)=mu(n)^2 w(n/N)`, `n<=N`.

For prime-support distance

`r=|S_m triangle S_n|`, define

`H_N^(w)(z)=sum_{m,n<=N}U_N(m)U_N(n) z^r`.

Then exactly

`H_N^(w)(1)=A_N^2`,

`H_N^(w)(0)=V_N`,

`H_N^(w)(-1)=S_w(N)^2`,

where

`A_N=sum_n U_N(n)`,

`V_N=sum_n U_N(n)^2`.

Squarefree density and partial summation give

`A_N ~ (6/pi^2)N int_0^1 cos(pi x/2)dx`
`=12/pi^3 * N`,

and

`V_N ~ (6/pi^2)N int_0^1 cos^2(pi x/2)dx`
`=3/pi^2 * N`.

Thus

`sqrt(V_N) ~ sqrt(3)/pi * sqrt(N)`

is exactly the square-root collision/RMS scale.

Therefore

`RH <=> H_N^(w)(-1) <= N^o(1) H_N^(w)(0)`.

This is a finite compact-support analogue of the Riesz Pair-BRC collision-coherence criterion.

The effective positive Cell count is

`N_eff=A_N^2/V_N ~ (48/pi^4)N`.

---

## 8. Rank-one convergence across three observer systems

Current Enterprise RH work has independently exposed one-dimensional critical obstructions in three different representations:

1. multiplicative Mellin/Newton/Euler analysis: only the primitive power-sum channel `P_1(s)` is critical;
2. rough/Dickman Green analysis: one algebraic dominant source charge survives unless orthogonalized;
3. additive cumulative Brownian Gram: the first positive eigenmode alone already supports an RH-equivalent criterion.

These are not proven to be the same operator or the same state. They are different transforms of the arithmetic problem.

Safe project observation:

`CRITICAL_OBSTRUCTION_APPEARS_RANK_ONE_IN_MULTIPLE_NONIDENTICAL_OBSERVER_DECOMPOSITIONS`.

Do not promote this observation to a unification theorem without an explicit intertwining map.

---

## 9. Current limitation

The first mode is extremely low frequency: its phase changes only by order one across the entire interval `[1,N]`. Existing Davenport/short-interval cancellation gives logarithmic savings here, not the required square-root cancellation.

Thus the single-mode compression simplifies the target but does not make it easier by known methods. Any proof of its natural collision scale is already a proof of RH.

---

## 10. Next question

The natural next Enterprise question is not to search for additional additive modes. It is to ask whether the first-mode cosine weight admits a provenance-preserving **multiplicative/BRC intertwiner** whose output is simpler than the original Möbius sum without introducing a hidden RH-strength inverse.

Candidate audit targets:

- exact divisor/Möbius transforms of the cosine weight;
- Mellin convolution factorizations with zero-free factors;
- whether Alladi ordered-prime coordinates can represent the first-mode weighted sum with a positive high-depth tail;
- whether any such representation is merely a known Nyman--Beurling/Riesz/Müntz reformulation.
