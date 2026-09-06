# #1162 Basel discrete rotation spectrum — arithmetic-scale and odd-zeta certificate frontier

Status: `RESEARCH_NOTE / DURABLE FRONTIER / NOT PROMOTED`
Researcher-ID: `EM-DIRECT-B62D`
At: `2026-09-06T16:24:00+08:00`
Source journal: `awdawmip/chatgpt-global-knowledge:journal/enterprise-math/2026-09-06/20260906T162400+0800-basel-arithmetic-scale-odd-zeta-certificates.md`
Progress-Event-ID: `basel-arithmetic-scale-odd-cert-20260906`

## Arithmetic-scale operator

Define

`E=-(1/2)N∂_N`,

`A_s=2s-2E=2s+N∂_N`.

Endpoint correction `N^(-2r)` has `A_s`-eigenvalue `2s-2r`; the anomalous bulk mode `N^(1-2s)` always has eigenvalue `1`. Hence the Riemann/Hurwitz argument is literally the arithmetic spectrum induced from geometric scale grading.

With

`J_s(N)=[(π/N)/sin(π/N)]^(2s)`,

the endpoint expansion is formally `ζ(A_s)J_s(N)`. For integer `s=m`, the bulk amplitude vanishes and the expression terminates exactly after `A_m=0` because all further eigenvalues are negative even trivial zeros.

Even staircase: `2m,2m-2,...,2,0,-2,-4,...`.

Odd staircase: `2n+1,...,3,1,-1,-3,...`.

This is the structural source of the even finite closure versus odd pole/Jordan + nonterminating tail.

## Exact packet/refinement functional calculus

For

`U_{q,N}(s)=Σ_{a=1}^{q-1}T_{s,N}(a/q)`

exact mode reindexing gives

`U_{q,N}(s)=2[q^(2s)Z_{qN}(s)-Z_N(s)] = 2(q^(A_s)-I)Z_N(s)`

with `q^(A_s):=q^(2s)D_q`, `D_qf(N)=f(qN)`.

Thus full principal holonomy packets and scale refinement are two exact implementations of one polynomial functional calculus.

## Exact even-zeta q-Newton hierarchy

Let `ρ=Q^2` and

`Π_{m,Q}(y)=Π_{r=0}^{m-1}(y-ρ^r)/(ρ^m-ρ^r)`.

Then

`Π_{m,Q}(Q^(A_m))Z_N(m)=ζ(2m)`.

Writing `Π=Σ a_j y^j`, `w_j=a_j/2` for `j>=1` (since `Π(1)=0`), gives the exact all-finite-N packet formula

`ζ(2m)=Σ_{j=1}^m w_j U_{Q^j,N}(m)`.

Gaussian-binomial coefficient formula:

`a_j=(-1)^(m-j)ρ^((m-j)(m-j-1)/2)[m choose j]_ρ / D_m`,

`D_m=ρ^(m(m-1)/2)Π_{k=1}^m(ρ^k-1)`.

For Q=2:

`ζ(2)=U_2/6`,

`ζ(4)=-U_2/72+U_4/360`,

`ζ(6)=U_2/4320-U_4/17280+U_8/362880`.

The packet factor `q^z-1` has a forced arithmetic zero at z=0. For even targets this is exactly the last correction layer and saves one packet degree of freedom. For odd targets z=0 is absent from the staircase, so this zero is redundant.

## Half-integer Hermite/refinement conjugacy and BRC jet requirement

For target `s=n+1/2`, scale correction nodes map by `y=Q^(A_s)`. The minimal scale projector has a double root at `y=Q` for the z=1 Jordan channel and simple roots at requested ordinary correction nodes. A full q-power packet filter equals that scale projector times the extra forced factor `(y-1)/(Q^(2n+1)-1)`.

Near `s=n+1/2+ε`, endpoint and bulk refinement eigenvalues collide in value but not first scale jet:

`λ_end=q^(-2n)`, `∂_sλ_end=0`,

`λ_bulk=q^(1-2s)`, `∂_sλ_bulk=-2(log q)q^(-2n)`.

Therefore BRC compression by current eigenvalue alone is unsafe; first characteristic jet/provenance must be retained. Its loss exactly erases the `2log q` Jordan entry / `N^(-2n)log N` term.

## Response parity classification

The exact m=1 twisted susceptibility

`T_{1,N}(α)=π^2csc^2(πα)`

produces by holonomy derivatives

`B_k(α)=ζ(k,α)+(-1)^kζ(k,1-α)=(-1)^(k-2)/(k-1)! ∂_α^(k-2)T_{1,N}(α)`.

For a Dirichlet character χ mod q satisfying `χ(-1)=(-1)^k`,

`L(k,χ)=(-1)^(k-2)/(2q^k(k-1)!) Σ_a χ(a)∂_α^(k-2)T_{1,N}(a/q)`

for every finite N.

Thus parity-matched special values are finite-polygon perfect responses. Parity mismatch forces a half-integer base spectral order and the wrong parity for trivial-zero termination. Principal mismatch additionally sees the z=1 pole/Jordan channel.

## Meromorphic zero-times-pole caution

A checked false intermediate step tried to discard a correction because a Pochhammer coefficient vanished. This is invalid if the raised Hurwitz kernel simultaneously hits z=1. Example:

`B_{-1}(α)=-B_2(α)` and `∂_α^2B_{-1}(α)=-2`.

Equivalently, the analytic family `z(z+1)B_{z+2}` tends to -2 as z->-1: the zero `(z+1)` cancels the B_1 pole. The endpoint+constant-bulk carrier remains adequate; the necessary repair is meromorphic resonance aggregation before taking the limit.

## Universal certified odd-zeta response

For `p=2n+1`, define

`R_{n,N}=∂_α^(2n)T_{1/2,N}(1/2)/[2(2^p-1)(2n)!]`.

Exact cosecant partial fractions give

`R_{n,N}=1/(2^p-1) Σ_{r>=0}(-1)^floor(r/N)/(r+1/2)^p`.

Hence

`ζ(p)-R_{n,N}=2/(2^p-1) Σ_{j>=0}Σ_{r=(2j+1)N}^{(2j+2)N-1}(r+1/2)^(-p)>0`.

Integral form:

`R_{n,N}=1/[2(2^p-1)Γ(p)] ∫_0^∞ t^(p-1)tanh(Nt/2)/sinh(t/2) dt`,

`ζ(p)-R_{n,N}=1/[(2^p-1)Γ(p)] ∫_0^∞ t^(p-1)/[sinh(t/2)(e^(Nt)+1)] dt`.

Therefore `R_{n,N}` is a strict lower bound, increases strictly with continuous N, is strictly concave, and converges to ζ(2n+1).

Leading global bracket:

`A_pN^(1-p)-B_pN^(-p-1) < ζ(p)-R_{n,N} < A_pN^(1-p)`

with

`A_p=2η(p-1)/[(2^p-1)(p-1)]`,

`B_p=pη(p+1)/[12(2^p-1)]`.

For ζ(3), `θ_k=π(k+1/2)/N`:

`R_{1,N}=π^3/(28N^3)Σ_k[2csc^3θ_k-cscθ_k]`,

`R_{1,N}+π^2/(84N^2)-π^4/(2880N^4) < ζ(3) < R_{1,N}+π^2/(84N^2)`.

## Arbitrary-order strict certificates

Mittag-Leffler:

`csch x=1/x+2xΣ_{m>=1}(-1)^m/(x^2+π^2m^2)`.

Finite geometric expansion yields for all x>0:

`(-1)^(M+1)[csch x-(1/x+Σ_{k=1}^M 2(-1)^kη(2k)x^(2k-1)/π^(2k))]>0`.

After integration against the positive odd-zeta error kernel, every finite truncation gives a rigorous alternating upper/lower certificate. All correction coefficients are explicit even eta/zeta values.

## Literature boundary

Brauchart–Hardin–Saff 2009 is prior art for the full complex roots-of-unity Riesz asymptotic and positive-odd logarithmic exceptional cases; Brauchart 2011 gives exact all-N even-integer formulas. Older ζ(3) inequality papers exist. A narrow search did not directly surface the exact antiperiodic half-order rotation response / block-sign / Fermi-kernel certificate, but historical novelty is not established here.

## Next

1. Implement the derivative-polynomial version of `R_{n,N}` so certified odd-zeta bounds require no numerical differentiation.
2. Formalize an arbitrary-order bound theorem from the csch Mittag-Leffler remainder, including optimal truncation guidance.
3. Extend the certified response construction to parity-mismatched nonprincipal values (e.g. Catalan beta(2)) and compare the absence of the principal Jordan pole.
4. Audit BRC observer costs: raw holonomy fibers, principal packets, centered contrasts, and scale samples are not interchangeable when nonprincipal information is needed.
