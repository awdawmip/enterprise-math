# #1162 — certified odd-zeta rotation algorithm and beta endpoint

Status: `RESEARCH_NOTE / DURABLE FRONTIER / NOT PROMOTED`
Researcher-ID: `EM-DIRECT-B62D`
At: `2026-09-06T16:45:00+08:00`
Source journal: `awdawmip/chatgpt-global-knowledge:journal/enterprise-math/2026-09-06/20260906T164500+0800-odd-zeta-certified-rotation-algorithm.md`
Progress-Event-ID: `odd-zeta-certified-rotation-algorithm-20260906`

## Certified odd-zeta rotation response

Let `p=2n+1` and

`R_{n,N}=∂_α^(2n)T_{1/2,N}(1/2)/[2(2^p-1)(2n)!]`.

Using the cosecant partial-fraction expansion one obtains exactly

`R_{n,N}=1/(2^p-1) Σ_{r>=0} (-1)^floor(r/N)/(r+1/2)^p`.

Hence

`ζ(p)-R_{n,N}=2/(2^p-1) Σ_{j>=0} Σ_{r=(2j+1)N}^{(2j+2)N-1}(r+1/2)^(-p)>0`.

Integral form:

`R_{n,N}=1/[2(2^p-1)Γ(p)] ∫_0^∞ t^(p-1)tanh(Nt/2)/sinh(t/2) dt`,

`ζ(p)-R_{n,N}=1/[(2^p-1)Γ(p)] ∫_0^∞ t^(p-1)/[sinh(t/2)(e^(Nt)+1)] dt`.

Consequences: `R_{n,N}` is a strict lower bound for every finite N, increases strictly with continuous N, is strictly concave, and converges to `ζ(2n+1)`.

## Finite trigonometric implementation

Define integer polynomials `P_n(u)` by

`d^(2n)/dx^(2n) csc x = csc x * P_n(csc^2 x)`.

Recurrence:

`P_0=1`,

`P_{n+1}(u)=4u^2(u-1)P_n''(u)+(10u^2-8u)P_n'(u)+(2u-1)P_n(u)`.

First values:

`P_1=2u-1`,

`P_2=24u^2-20u+1`,

`P_3=720u^3-840u^2+182u-1`.

With `θ_k=π(k+1/2)/N`,

`R_{n,N}=(π/N)^p/[2(2^p-1)(2n)!] Σ_{k=0}^{N-1} csc(θ_k)P_n(csc^2 θ_k)`.

For `ζ(3)`:

`R_{1,N}=π^3/(28N^3) Σ_k [2csc^3 θ_k-csc θ_k]`.

## Rigorous brackets

Let `E_{n,N}=ζ(p)-R_{n,N}`. A global first bracket is

`A_pN^(1-p)-B_pN^(-p-1) < E_{n,N} < A_pN^(1-p)`

where

`A_p=2η(p-1)/[(2^p-1)(p-1)]`,

`B_p=pη(p+1)/[12(2^p-1)]`.

For `ζ(3)`:

`R_{1,N}+π^2/(84N^2)-π^4/(2880N^4) < ζ(3) < R_{1,N}+π^2/(84N^2)`.

Mittag-Leffler for csch gives the stronger all-order certificate:

`csch x=1/x+2xΣ_{m>=1}(-1)^m/(x^2+π^2m^2)`.

Finite denominator expansion yields, for every `M>=0` and `x>0`, strict alternating one-sided remainders. Integration against the positive Fermi kernel gives an arbitrary-order alternating sequence of rigorous upper/lower bounds for `ζ(2n+1)`.

For k>=1 the positive correction coefficients are

`A_{n,k}=2^(2-2k)η(2k)Γ(2n+2k)η(2n+2k)/[(2^p-1)Γ(2n+1)π^(2k)]`.

Successive term ratio:

`T_{k+1}/T_k=[(2n+2k)(2n+2k+1)/(4π^2N^2)] [η(2k+2)/η(2k)] [η(2n+2k+2)/η(2n+2k)]`.

Thus optimal truncation has `k_opt~πN`; the resulting certified interval width is exponentially small, of order `exp(-2πN)` up to algebraic factors. For `ζ(3)`, `N=10`, the minimum term occurs at k=31 and the adjacent rigorous bracket width is approximately `1.8450878151e-27`.

## N=1 beta endpoint

At N=1,

`R_{n,1}=2^p/(2^p-1) β(p)`

or equivalently

`R_{n,1}=|E_{2n}|π^p/[2(2^p-1)(2n)!]`.

Hence

`2^p/(2^p-1)β(p)=R_{n,1}<R_{n,2}<...<ζ(p)`.

For `ζ(3)`, `R_{1,1}=π^3/28=(8/7)β(3)`.

This provides a monotone finite-rotation flow from a parity-matched closed beta value to the principal odd zeta value.

## Catalan mismatch analogue

For `G=β(2)`, an analogous half-order one-response construction yields

`G_N=Σ_{r>=0}(-1)^floor(r/N)[(4r+1)^(-2)-(4r+3)^(-2)]`,

`G_N=∫_0^∞ t tanh(2Nt)/(2cosh t) dt`,

`G-G_N=∫_0^∞ t/[cosh t(e^(4Nt)+1)] dt>0`.

Thus `G_N↑G`. Its first corrections are

`G-G_N=π^2/(192N^2)-7π^4/(61440N^4)+...`.

At N=1,

`G_1=L(2,χ_8)=π^2/(8sqrt(2))`.

## Status / prior-art caution

The complex roots-of-unity Riesz asymptotics and odd logarithmic exceptional cases are prior art (Brauchart–Hardin–Saff 2009). Older ζ(3) inequality literature also exists. The exact antiperiodic half-order rotation response, periodic-block lower series, Fermi-kernel positive error, all-order strict certificate construction, and beta-to-zeta monotone-flow interpretation remain research candidates here; historical novelty is not asserted.

## Next

1. Derive the general periodic-character/parity-mismatch `L(k,χ)` finite-rotation cutoff kernel.
2. Seek a unified proof that the finite-rotation kernel is positive/monotone for broad real characters, identifying exact sign conditions.
3. Compare arithmetic cost of optimal certified bounds with Apéry/central-binomial series.
