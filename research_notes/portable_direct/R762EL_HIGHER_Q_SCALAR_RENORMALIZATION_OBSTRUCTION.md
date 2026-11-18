# R762EL — Why the q=3 scalar-affine BRC renormalization cannot extend to q>=9

**Date:** 2026-11-18. **Parent task:** `RS-X6-TRIADIC-CLOSURE-DYNAMICS`. **Researcher provenance:** `EM-X6-3050F6`; continuation of R762EK. **Status:** `AUTHOR_PROVED / NOT_REVIEWED`.

## Theorem (all higher powers of three, all positive periods)

Let `q=3^a` with `a>=2`, `G_q=(Z/qZ)^3`, `R_q=Z[G_q]`, and let

[
P_q=1+X+Z+XY+YZ+XYZ,qquad S_q=sum_{gin G_q}g.
]

For **every** pair of positive integers `n,L`, there exist **no** complex scalars `A,B` for which

[
oxed{P_q^{n+L}=A P_q^n+B S_q 	ext{ in } mathbb C[G_q].}
]

In particular, the exact `q=3` identity in R762EK, `P_3^{n+6}=3^6P_3^n+7·3^5·6^n S_3`, does not extend verbatim to higher `3`-power moduli using any positive period, any scalar multiplier, or any uniform-per-endpoint additive correction.

## Exact proof

Choose a primitive q-th root of unity `ζ=e^(2πi/q)`, and put `ω=ζ^(q/3)=e^(2πi/3)`. Since `q>=9`, the two nontrivial characters

[
chi_1:(X,Y,Z)mapsto(zeta,1,1),qquad
chi_2:(X,Y,Z)mapsto(omega,1,1)
]

are well defined on the same `G_q`. For either character, all six positive branches collapse *after evaluation* to

[
chi(P_q)=3(1+chi(X)).
]

Both eigenvalues are nonzero, and `χ_1(S_q)=χ_2(S_q)=0` because the characters are nontrivial. If the proposed identity held, evaluating at `χ_1` and `χ_2` and cancelling the nonzero `χ(P_q)^n` would require

[
A=[3(1+zeta)]^L=[3(1+omega)]^L.
]

But `|1+ω|=1`, whereas

[
|1+zeta|=2cos(pi/q)>1
]

for `q>=9` (indeed `0<π/q<=π/9<π/3`). Their positive L-th powers have different complex absolute values. This contradiction proves the theorem.

## Stronger corollary: the minimal recurrence order grows with q

Let `μ_q(T)` be the monic minimal polynomial over Q of the exact rational operator `m_(P_q):Q[G_q]->Q[G_q]`. For **every** q=3^a, a>=1,

\[
\boxed{T\big((T-3)^q-3^q\big)\mid\mu_q(T),\quad\deg\mu_q\ge q+1.}
\]

**Proof.** For each `t=0,...,q-1` the character `(X,Y,Z)=(ζ^t,1,1)` has eigenvalue `λ_t=3(1+ζ^t)`; these q eigenvalues are pairwise distinct and are precisely the q roots of `(T-3)^q-3^q`. Separately, the character `(X,Y,Z)=(ω,1,ω²)`, with `ω=ζ^(q/3)`, has eigenvalue `1+ω+ω²+ω+ω²+1=0`. The zero root is not among the `λ_t`, because q is odd and no q-th root is −1. Every eigenvalue is a root of `μ_q`, and group algebra multiplication is diagonalizable over C, proving the stated exact divisor and degree bound.

In particular, a single recurrence with fixed order independent of q cannot annihilate the full family of terminal coefficient sequences; increasing q forces a growing exact rational spectral state. This explains why a higher-q repair must carry additional spectral classes, rather than only rescale the q=3 recurrence.

## Interpretation and next viable direction

The q=3 proof works because every nonzero *nontrivial* eigenvalue is exactly 3 times a sixth root of unity. Starting at q=9, even the one-coordinate specializations `χ(X)=ζ` and `χ(X)=ω` already carry distinct nontrivial spectral magnitudes. A higher-q exact recurrence therefore needs an operator-valued or multi-spectral-class state rather than one scalar multiplier plus uniform S correction. This is a rigorous obstruction to **one specified renormalization ansatz**, not to the full three-coordinate all-horizon content conjecture.

A productive next test is to compute the integral minimal-polynomial/primary submodule decomposition of `m_{P_q}` for q=9 and seek a short *multi-component* recurrence with exact 3-adic nondivisibility witnesses.

**Scope / frozen input discipline:** Positive six-branch terminal BRC endpoint in `R_q`; P000 six-axis signed native state and task source pins are unchanged. No native `TRIADIC_CLOSURE_E` Cell/Link/Port event license or signed-state compression claim follows. The argument is exact complex-character algebra; no floating test, approximation, or independent review is claimed.
