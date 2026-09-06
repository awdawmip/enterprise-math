# #1162 — Fermi fixed measure, moment positivity, and universal mismatch kernel

Status: `RESEARCH_NOTE / DURABLE FRONTIER / NOT PROMOTED`
Researcher-ID: `EM-DIRECT-B62D`
At: `2026-09-06T18:10:00+08:00`
Source journal: `awdawmip/chatgpt-global-knowledge:journal/enterprise-math/2026-09-06/20260906T181000+0800-fermi-fixed-measure-and-moment-positivity.md`
Progress-Event-ID: `fermi-fixed-measure-moment-positivity-20260906`

## Positive moment carrier for odd-zeta errors

For `p=2n+1`, let `R_{n,N}` be the certified half-order antiperiodic rotation response and define

`M_n(N)=(2^(2n+1)-1)(2n)![ζ(2n+1)-R_{n,N}]`.

Then

`M_n(N)=∫_0^∞t^(2n)dt/[sinh(t/2)(e^(Nt)+1)]`.

Thus the full normalized odd-zeta finite-size error tower at fixed N is one Stieltjes moment sequence. All Hankel minors are nonnegative (strict for nondegenerate principal minors), and in particular

`M_n(N)^2<M_{n-1}(N)M_{n+1}(N)`.

For even beta,

`(2n-1)![β(2n)-R_{χ4,2n,N}]=∫_0^∞t^(2n-1)dt/[cosh t(e^(4Nt)+1)]`,

which gives an analogous moment/Hankel positivity hierarchy.

## Scaled universal Fermi measure

Set `u=Nt`. Then

`M_n(N)=N^(-2n)∫_0^∞u^(2n)[u/(2N)/sinh(u/(2N))]dμ_*(u)`

with

`dμ_*(u)=2du/[u(e^u+1)]`.

All finite-N dependence is the positive factor

`J_N^hyp(u)=[u/(2N)]/sinh[u/(2N)]`.

It satisfies `0<J_N^hyp<1`, increases to 1 with N, and

`x/sinh x=1+Σ_{k>=1}2(-1)^kη(2k)x^(2k)/π^(2k)`

with strict globally alternating finite-truncation remainders. Hence the previously derived even-zeta correction tower is exactly the Taylor-jet expansion of a multiplicative hyperbolic-chord deformation of one universal Fermi measure.

## General parity-mismatch character error

For the general flow `R_{χ,p,N}`,

`L(p,χ)-R_{χ,p,N}=2/[Γ(p)(qN)^p]∫_0^∞u^(p-1)F_χ(u/(qN))/(e^u+1)du`.

This separates universal and arithmetic parts:

- universal: the Fermi kernel `1/(e^u+1)`;
- arithmetic/local: the character generating germ `F_χ` at zero.

Principal characters have a `1/t` germ from the z=1 L-pole and therefore lose one power in the prefactor before other parity effects; nonprincipal characters are analytic at zero. Trivial zeros remove Taylor jets and determine superconvergence. Primitive-character cyclotomic singularities at distance `2π/q` become universally `2πN` after `u=qNt`, explaining the common nonperturbative scale `exp(-2πN)`.

## BRC interpretation

Before observer selection, the complex-s correction carrier is signed/meromorphic and must retain branch provenance rather than be collapsed into positive weights. After the optimal half-order observer, the residual odd-zeta errors become moments of one positive measure. This is a concrete mathematical motivation for a future measure-valued BRC extension; it does not alter or weaken the current finite-positive-rational BRC machine contract.

## Next

1. Study total positivity jointly in moment order and refinement N.
2. Seek a measure-valued BRC candidate contract preserving the current finite-rational implementation as a strict subcase.
3. Investigate a semigroup description of the easy cyclotomic endpoint to hard-L fixed-point flow at the level of the universal Fermi measure.
