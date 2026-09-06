# Research frontier — #1162 Basel discrete rotation spectrum: first-order mother determinant

Status: RESEARCH_FRONTIER / NOT_PROMOTED
Date: 2026-09-06
Scope: #1162

## Native operator

For `0<alpha<1`, define the positive first-order rotation operator on Fourier mode k by

`D_{N,alpha} e_k = (N/pi) sin(pi(k+alpha)/N) e_k`.

Then the normalized chord Laplacian is exactly `A_{N,alpha}=D_{N,alpha}^2`. Hence the former `A^{-1}` versus `A^{-1/2}` carrier split is the native integer-power split `D^{-2}` versus `D^{-1}`.

## First-order determinant

Define `Xi_{N,alpha}(z)=det(I+z D_{N,alpha}^{-1})`, `delta_N(z)=(N/pi) asin(pi z/N)`, and

`P_N(alpha)=prod_{k=0}^{N-1} tan(pi(k+alpha)/(2N))`.

Exact identities:

1. `Xi(z)Xi(-z)=Psi_{N,alpha}(-z^2)`.
2. `Xi(z)/Xi(-z)=P_N(alpha+delta_N(z))/P_N(alpha-delta_N(z))`.
3. `Xi_{qN,alpha}(z)=prod_{r=0}^{q-1}Xi_{N,(alpha+r)/q}(z/q)`.
4. `P_{qN}(alpha)=prod_{r=0}^{q-1}P_N((alpha+r)/q)`.

Thus even inverse powers are the even part of one first-order determinant and odd inverse powers are the odd part.

## BRC criticality

For `Tr D^{-m}`, q-refinement has q positive branches, each weight `q^{-m}`, total branch mass `q^{1-m}`. Therefore `m=1` is the unique critical inverse power and all `m>=2` are subcritical.

The scale operator `K_m=m+N d/dN` labels endpoint corrections by `m-2r`; the anomalous bulk branch always has label 1. Thus even m never hits the critical label 1, while odd m necessarily does.

For fixed finite depth L, uniform q-adic digits with `alpha_{j+1}=(alpha_j+r_{j+1})/q` give the exact martingale

`M_j^(s)=q^{j(1-2s)} T_{s,q^{L-j}N}(alpha_j)`.

At `s=1/2`, no scale renormalization is needed.

## Critical cocycle

`T_{1/2,N}(alpha)=2 log N+C(alpha)+o(1)`, where

`C(alpha)=-psi(alpha)-psi(1-alpha)-2 log(pi/2)`

and

`(1/q) sum_{r=0}^{q-1} C((alpha+r)/q)=C(alpha)+2 log q`.

This is the additive Jordan cocycle underlying the half-integer logarithmic resonance.

## Orientation-resolved Gamma branches

Let

`S_N(alpha)=prod sin(pi(k+alpha)/(2N))`,
`C_N(alpha)=prod cos(pi(k+alpha)/(2N))`.

Then `P_N=S_N/C_N`, `S_N C_N=2^{1-2N} sin(pi alpha)`, and exact q-refinement products hold separately for S_N and C_N.

Continuum limits:

`(2^{N-1/2}/sqrt(pi))(2N/pi)^{1/2-alpha} S_N(alpha) -> 1/Gamma(alpha)`,

`(2^{N-1/2}/sqrt(pi))(2N/pi)^{alpha-1/2} C_N(alpha) -> 1/Gamma(1-alpha)`.

Consequently Euler reflection and Gauss multiplication are continuum fixed-point identities of the orientation-resolved branch products (classical identities; this note records the rotation-spectrum derivation/synthesis, not historical novelty).

## Signed BRC complexity witness

For fundamental discriminant `D=7413`, the weighted theta values are rigorously certified to have signs

`t=1:+`, `3.5:-`, `5:+`, `20:-`, `60:+`.

Each was computed from 800 terms with an explicit absolute Gaussian tail smaller than the displayed sign margin. Self-reciprocity gives at least nine nodal sign sectors: `J_7413>=9`.

## Status / next

These are research-frontier derivations and a finite certified witness, not Working Truth/Foundation promotion. Next: combine the Gamma orientation branch with prime-holonomy Euler-factor operators into a minimal completed-L local-factor carrier; separately continue the open primitive-quadratic `CM => LCM?` question.