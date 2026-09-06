# #1162 — integer/critical-half carrier classification and function-level L-flows

Status: `RESEARCH_NOTE / DURABLE FRONTIER / NOT PROMOTED`
Researcher-ID: `EM-DIRECT-B62D`
At: `2026-09-06T17:45:00+08:00`
Source journal: `awdawmip/chatgpt-global-knowledge:journal/enterprise-math/2026-09-06/20260906T174500+0800-critical-half-carrier-generating-flows.md`
Progress-Event-ID: `critical-half-carrier-generating-flows-20260906`

## Two-carrier parity principle

For integer p>=2 and Dirichlet character χ mod q:

- parity matched (`χ(-1)=(-1)^p`): the finite-perfect carrier is `A^-1`. Since `T_{1,N}(α)=π^2csc^2(πα)` for every finite N,

`L(p,χ)=(-1)^(p-2)/[2q^p(p-1)!]Σ_aχ(a)∂_α^(p-2)T_{1,N}(a/q)`

exactly for every N.

- parity mismatched (`χ(-1)=(-1)^(p-1)`): among all half-integer base orders `σ=j+1/2`, the unique order maximizing single-scale cancellation of low lattice corrections is `σ=1/2`; the optimal carrier is `A^-1/2` and gives the finite flow `R_{χ,p,N}`.

Thus `A^-1` is the finite-perfect matched carrier and `A^-1/2` the unique optimal mismatch flowing carrier.

## Critical spectral meaning

In one dimension `s=1/2` is exactly the trace-class threshold for Laplacian inverse powers. Principal character observes the constant critical mode and its z=1 pole; nonprincipal/centered observers quotient it out. This supplies a spectral explanation for the principal odd-zeta correction penalty.

## Superconvergence three-way law

Let `c_{1/2,r}=[x^(2r)](x/sin x)`.

Odd nonprincipal χ, p=2n:

`R_{χ,2n,N}=L(2n,χ)-c_{1/2,n}(π/(qN))^(2n)L(0,χ)+O(N^(-2n-2))`.

Even nonprincipal χ, p=2n+1:

`R_{χ,2n+1,N}=L(2n+1,χ)+(2n+1)c_{1/2,n+1}(π/(qN))^(2n+2)L(-1,χ)+O(N^(-2n-4))`.

Principal even χ, p=2n+1: the z=1 Pochhammer zero is resurrected by the L(1) pole, producing `O(N^(-(p-1)))` rather than the even-nonprincipal `O(N^(-(p+1)))`. The principal pole costs exactly two powers.

## Odd-zeta generating flow

For |x|<1/2,

`H_N(x)=T_{1/2,N}(1/2+x)-T_{1/2,N}(1/2)`

`      =2Σ_{n>=1}(2^(2n+1)-1)R_{n,N}x^(2n)`.

Continuum:

`H_∞(x)=-ψ(1/2+x)-ψ(1/2-x)+2ψ(1/2)`

`      =2Σ_{n>=1}(2^(2n+1)-1)ζ(2n+1)x^(2n)`.

N=1:

`H_1(x)=π(sec πx-1)`.

Exact positive error:

`H_∞(x)-H_N(x)=2∫_0^∞[cosh(xt)-1]/[sinh(t/2)(e^(Nt)+1)]dt>0`

for real `0<|x|<1/2`. Hence all odd-zeta coefficients flow monotonically together from the Euler/beta endpoint to the zeta fixed point.

## Even-beta generating flow

For |y|<1,

`B_N(y)=1/8[T_{1/2,N}(1/4-y/4)-T_{1/2,N}(1/4+y/4)]`

`      =Σ_{n>=1}R_{χ4,2n,N}y^(2n-1)`.

Continuum:

`B_∞(y)=Σ_{n>=1}β(2n)y^(2n-1)`.

Exact positive error:

`B_∞(y)-B_N(y)=∫_0^∞sinh(yt)/[cosh t(e^(4Nt)+1)]dt>0` for `0<y<1`.

At N=1 the coefficients are `L(2n,χ8)`, parity-matched cyclotomic closed values.

## General character critical generating function

If `χ(-1)=(-1)^a`, define

`G_{χ,N}(y)=1/(2q)Σ_{b=1}^{q-1}χ(b)T_{1/2,N}((b-y)/q)`.

Then

`G_{χ,N}(y)=Σ_{d>=0,d≡a mod2}R_{χ,d+1,N}y^d`.

For nonprincipal χ,

`G_{χ,∞}(y)=Σ_{d>=0,d≡a mod2}L(d+1,χ)y^d`.

Integral form:

`G_{χ,N}(y)=∫_0^∞F_χ(t)tanh(qNt/2)C_a(yt)dt`, with `C_0=cosh`, `C_1=sinh` (subtract the principal L(1) constant divergence before using the even-principal generating function).

## Literature boundary

Cotangent/polygamma special-value formulas and beta/zeta generating functions are classical. The current candidate structure is the finite-polygon integer/critical-half carrier classification, optimality of the half-order mismatch carrier, and the positive-error refinement flows at function level. Historical novelty is not asserted.

## Next

1. Prove precise admissibility/branch statements for complex-valued characters.
2. Extract convexity and majorization inequalities from the positive function-level kernels.
3. Classify real primitive characters with sign-positive `F_χ` by exact character-polynomial root location.
