# #1162 — parity-mismatch Dirichlet finite-rotation flow

Status: `RESEARCH_NOTE / DURABLE FRONTIER / NOT PROMOTED`
Researcher-ID: `EM-DIRECT-B62D`
At: `2026-09-06T17:15:00+08:00`
Source journal: `awdawmip/chatgpt-global-knowledge:journal/enterprise-math/2026-09-06/20260906T171500+0800-parity-mismatch-dirichlet-rotation-flow.md`
Progress-Event-ID: `parity-mismatch-dirichlet-rotation-flow-20260906`

## Exact finite-rotation flow

Let χ be a Dirichlet character modulo q and let integer p>=2 satisfy parity mismatch

`χ(-1)=(-1)^(p-1)`.

Define

`R_{χ,p,N}=(-1)^(p-1)/[2q^p(p-1)!] Σ_{a=1}^{q-1}χ(a)∂_α^(p-1)T_{1/2,N}(α)|_{α=a/q}`.

Cosecant partial fractions give exactly

`R_{χ,p,N}=Σ_{m>=1}χ(m)(-1)^floor((m-1)/(qN))/m^p`.

Let

`F_χ(t)=Σ_{m>=1}χ(m)e^(-mt)=[Σ_{a=1}^qχ(a)e^(-at)]/[1-e^(-qt)]`.

Then

`R_{χ,p,N}=1/Γ(p)∫_0^∞ t^(p-1)F_χ(t)tanh(qNt/2)dt`,

`L(p,χ)-R_{χ,p,N}=2/Γ(p)∫_0^∞ t^(p-1)F_χ(t)/(e^(qNt)+1)dt`.

A sufficient exact condition for a monotone lower flow is `F_χ(t)>=0` for all t>0. For real χ this is the finite polynomial positivity problem

`A_χ(x)=Σ_{a=1}^qχ(a)x^a >=0` for `0<x<1`.

Uniform certified error without sign assumptions:

`|L(p,χ)-R_{χ,p,N}| < 2η(p-1)/[(p-1)(qN)^(p-1)]`.

For nonprincipal χ, if

`M_χ=max_{1<=r<=q}|Σ_{a=1}^rχ(a)|`,

then Abel summation gives

`|L(p,χ)-R_{χ,p,N}| <= 2M_χη(p)/(qN)^p`.

## Finite cyclotomic orbit

Define

`χ~_N(n)=χ(n)(-1)^floor((n-1)/(qN))`.

It is periodic modulo `2qN` and satisfies

`χ~_N(2qN-n)=(-1)^pχ~_N(n)`.

Thus every finite N value is parity-matched and has the exact finite reflection formula

`R_{χ,p,N}=(-1)^(p-1)π/[(2qN)^p(p-1)!] Σ_{a=1}^{qN-1}χ(a)[d^(p-1)/dx^(p-1)cot(πx)]_{x=a/(2qN)}`.

For algebraic χ, `R_{χ,p,N}/π^p` lies in the relevant cyclotomic field. Hence a parity-mismatched hard L-value is approached through a refinement orbit of explicit parity-matched cyclotomic π^p values.

## Nonprincipal correction tower

For nonprincipal χ,

`F_χ(t)~Σ_{m>=0}(-1)^mL(-m,χ)t^m/m!`.

Therefore

`L(p,χ)-R_{χ,p,N} ~ 2/Γ(p) Σ_{m>=0} (-1)^mL(-m,χ)Γ(p+m)η(p+m)/[m!(qN)^(p+m)]`.

Parity mismatch forces every surviving `p+m` to be even.

For primitive χ and a surviving m,

`L(-m,χ)=2q^m m!τ(χ)/(2πi)^(m+1) L(m+1,barχ)`.

Thus every correction factors as

`Gauss phase × L(m+1,barχ) × η(p+m)`,

with both positive special values parity-matched.

## Example χ5, p=3

For the quadratic even character mod 5,

`A_χ5(x)=x-x^2-x^3+x^4=x(1-x)(1-x^2)>0`.

Hence `R_{χ5,3,N}` increases strictly from below to `L(3,χ5)`. Using `L(0,χ5)=0`, `L(-1,χ5)=-2/5`, `L(-3,χ5)=2`,

`L(3,χ5)-R_{χ5,3,N}=7π^4/(187500N^4)-31π^6/(11812500N^6)+...`.

Absence of a principal z=1 pole together with the even-character trivial zero improves the first correction by two powers relative to the ζ(3) principal flow.

## Universal nonperturbative scale

For primitive χ,

`F_χ(t)=1/τ(barχ) Σ_{a mod q}barχ(a)/(e^(t-2πia/q)-1)`.

The nearest complex-t singularity is at distance `2π/q`. Since the finite-rotation Laplace variable is `u=qNt`, the normalized nearest singularity is universally at `|u|=2πN`. Consequently the optimally truncated correction tower has nonperturbative scale `exp(-2πN)` up to algebraic factors; when parity removes every other term the half-index optimum is `~πN`.

## Catalan strict all-order subfamily

For `G=β(2)`,

`G-G_N=∫_0^∞ t/[cosh t(e^(4Nt)+1)]dt`.

The global Mittag-Leffler expansion

`sech x=(4/π)Σ_{m>=0}(-1)^m(2m+1)/[(2m+1)^2+(2x/π)^2]`

gives arbitrary-order strict alternating certificates:

`G-G_N=Σ_{j>=0}(-1)^jβ(2j+1)Γ(2j+2)η(2j+2)/[4^(j+1)π^(2j+1)N^(2j+2)]`

with each finite truncation a one-sided bound. Optimal index `~πN`; certified width `~exp(-2πN)`.

## Literature boundary

Bradley (Ramanujan J. 2002 / arXiv:math/0505078) is prior art for acceleration formulas for periodic-coefficient Dirichlet series, including odd zeta, Dirichlet L and Lerch values via hyperbolic partial fractions. Bharadwaj–Pathak (JNT 2022) is prior art on special values/arithmetic of periodic-coefficient Dirichlet series. General periodic-series acceleration and cyclotomic special-value facts are therefore not claimed new.

Current narrower candidates: finite-polygon half-order response realization; exact periodic block-sign/Fermi cutoff flow; BRC observer interpretation; easy×easy correction factorization; strict monotone/certificate subfamilies.

## Next

1. Classify real primitive χ for which `A_χ(x)` has fixed sign on `(0,1)` and hence yields monotone one-sided flows.
2. Build arbitrary-order absolute remainder bounds for sign-changing characters from the Gauss-pole decomposition.
3. Introduce the general response arithmetic-scale operator `A_p=p+N∂_N` and connect the entire correction tower to `L(A_p,χ)`.
