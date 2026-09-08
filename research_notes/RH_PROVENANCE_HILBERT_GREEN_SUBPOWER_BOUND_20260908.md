# RH provenance-Hilbert Green bound and the remaining coherent-observer gap

Status: `RESEARCH FRONTIER / EXACT OPERATOR-NORM BOUND + RH-EQUIVALENT OBSERVER REDUCTION / NOT A PROOF OF RH`
Date: `2026-09-08`
Project: `Enterprise Math / 进取数论`
Scope: `ordered prime provenance / X6 block resolvent / Hilbert norm / Möbius / RH observer gap`

## 0. Purpose and typing guard

The preceding block-resolvent identity localized prime discreteness as

`R_pi-R_0=-G_pi S_X6`,

with

`G_pi=(I-K_pi^6)^(-1)`

and

`S_X6=Q_5(K_pi)(K_pi-K_0)R_0`.

This note determines whether growth of the positive full-block Green operator can itself be a fixed-power RH obstruction.

P000 is unchanged. Prime paths are arithmetic provenance fibers, not spatial axes.

---

## 1. Toy nilpotent shift calibration

Let `S_N` be the N by N lower unilateral shift with ones on the first subdiagonal. Then

`(I+S_N)^(-1)=I-S_N+S_N^2-...+(-1)^(N-1)S_N^(N-1)`.

The exact spectral norm is

`||(I+S_N)^(-1)||_2 = 1/[2 sin(pi/(4N+2))]`

and therefore

`||(I+S_N)^(-1)||_2 ~ 2N/pi`.

Thus a positive nilpotent operator may have all eigenvalues zero while its resolvent grows linearly with depth through nonnormal/pseudospectral boundary effects.

Freeze:

`NILPOTENT != UNIFORMLY_SMALL_RESOLVENT`.

However, polynomial growth in a critical depth `N~log x/loglog x` is only `x^o(1)`.

---

## 2. Weighted ordered-prime creation operator on provenance Hilbert space

Use the orthonormal basis of finite ordered-prime provenance paths. A path ending at prime upper bound a has children obtained by appending one smaller allowed prime p.

Define the critical creation operator C by

`C e_v = sum_(p in Child(v)) p^(-1/2) e_(v,p)`.

Every child has a unique parent. Hence child sets of different parents are disjoint and

`C^* C e_v = [sum_(p in Child(v))1/p] e_v`.

Therefore exactly

`||C||_2^2 = sup_v sum_(p in Child(v))1/p`.

The backward Volterra operator K used in the rough recurrence is the adjoint presentation of the same weighted tree transition on the finite provenance Hilbert space, so

`||K||_2=||C||_2`.

---

## 3. Critical prime-window bound

Take

`y=(log x)^2`.

Every allowed child prime lies in `(y,x]`, so

`||K||_2^2 <= lambda(x,y):=sum_(y<p<=x)1/p`.

Mertens' prime harmonic theorem gives

`lambda(x,y)=loglog x-loglog y+O(1)`

and hence

`lambda(x,y)=(1+o(1))loglog x`.

The ordered provenance depth is bounded by the log budget:

`M<=log x/log y ~ log x/(2loglog x)`.

Thus K is nilpotent of index at most `M+1` on the truncated state space.

---

## 4. Full Möbius resolvent is subpower in provenance l2

The exact finite inverse is

`(I+K)^(-1)=sum_(r=0)^M (-K)^r`.

Therefore

`||(I+K)^(-1)||_2`
`<= (M+1) max(1,lambda^(M/2))`.

Since

`M/2 ~ log x/(4loglog x)`

and

`log lambda = logloglog x+O(1)`,

we obtain

`log ||(I+K)^(-1)||_2`
`<= (1/4+o(1)) log x * logloglog x/loglog x`.

Hence

`||(I+K)^(-1)||_2 = x^o(1)`.

Freeze:

`CRITICAL_ORDERED_PRIME_MOBIUS_RESOLVENT_HAS_SUBPOWER_PROVENANCE_L2_NORM`.

This estimate uses no RH cancellation.

---

## 5. X6 full-block Green is also subpower

With

`G_6=(I-K^6)^(-1)=sum_(q=0)^D K^(6q)`,

where `D=floor(M/6)`,

`||G_6||_2 <= (D+1) max(1,lambda^(3D))`.

Because `3D<=M/2`, the same bound gives

`||G_6||_2=x^o(1)`.

The local residual projector satisfies

`||Q_5(K)||_2`
`<=sum_(r=0)^5 ||K||_2^r`
`<=6 max(1,lambda^(5/2))`
`=(log x)^o(1)`.

Thus neither the complete-block Green nor the fixed-width residual X6 projector produces a fixed power loss in this Hilbert norm.

Freeze:

`X6_BLOCK_GREEN_OPERATOR_NORM_IS_NOT_THE_RH_HALF_POWER_BOTTLENECK`.

---

## 6. Why this does not prove RH: the coherent observer

Define

`A(x)=sum_(n<=x) mu(n)/sqrt(n)`.

By partial summation,

`RH iff A(x)=O_eps(x^eps)`.

Indeed:

- `M(t)=O_eps(t^(1/2+eps))` implies
  `A(x)=M(x)/sqrt x + (1/2)int_1^x M(t)t^(-3/2)dt = O_eps(x^eps)`;
- conversely `A(t)=O_eps(t^eps)` implies
  `M(x)=sqrt x A(x) - (1/2)int_1^x A(t)t^(-1/2)dt = O_eps(x^(1/2+eps))`.

Now regard

`a_n=mu(n)/sqrt(n)`

as the arithmetic Cell coefficient vector. Its ordinary Hilbert norm is

`||a||_2^2=sum_(n<=x)mu(n)^2/n`
`=(6/pi^2+o(1))log x`.

But

`A(x)=<a,1_[1,x]>`,

and

`||1_[1,x]||_2=sqrt x`.

Generic Cauchy-Schwarz therefore yields only

`|A(x)| <= (1+o(1))sqrt[(6/pi^2)x log x]`.

RH requires a gain of essentially `x^(1/2)` over this generic observer norm.

Freeze:

`PROVENANCE_HILBERT_NORM_CONTROL != COHERENT_MOBIUS_OBSERVER_CONTROL`.

This is the exact ordered-prime/X6 realization of the earlier generic observer half-derivative loss.

---

## 7. Consequence for the localized source

Because

`R_pi-R_0=-G_pi S_X6`

and `||G_pi||_2=x^o(1)` in the declared critical provenance norm, further work on the bare Green operator norm cannot supply the missing half power.

The new target must directly control the coherent observer projection

`<J_x, G_pi S_X6>`

or, by adjoint transfer,

`<G_pi^* J_x, S_X6>`.

A successful estimate must use arithmetic structure of the local signed source and/or the back-propagated observer. Merely showing

`||S_X6||_2=O(1)`

or

`||G_pi||_2=x^o(1)`

is insufficient.

Provisional frontier:

`X6_LOCAL_SOURCE_TO_COHERENT_OBSERVER_ORTHOGONALITY`.

---

## 8. Pair-BRC interpretation

Squaring a coherent scalar observer produces a pair kernel. Thus the required source/observer orthogonality is the one-copy form of the established Pair-BRC collision-coherence condition.

The next useful norm bridge should therefore compare

`|<J_x,G_pi S_X6>|^2`

against a diagonal/collision energy of `S_X6` or its propagated image, rather than against its positive L1 mass.

This is consistent with the established boundary:

`POSITIVE CAPACITY SMALL != SIGNED ANALYTIC CRITICALITY SMALL`.

No claim here proves RH.
