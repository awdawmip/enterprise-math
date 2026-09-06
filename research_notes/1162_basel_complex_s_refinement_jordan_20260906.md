# #1162 Basel discrete rotation spectrum — complex-s refinement/Jordan frontier

Status: `RESEARCH_NOTE / DURABLE FRONTIER / NOT PROMOTED`
Researcher-ID: `EM-DIRECT-B62D`
At: `2026-09-06T16:09:00+08:00`
Source journal: `awdawmip/chatgpt-global-knowledge:journal/enterprise-math/2026-09-06/20260906T160900+0800-basel-complex-s-jordan-brc.md`
Progress-Event-ID: `basel-complex-s-jordan-brc-20260906`

## Scope and BRC carrier

Question: extend #1162 from integer inverse moments to general complex `s` and classify refinement corrections.

BRC applicability: branch/provenance and observer discipline applied. Carrier keeps labeled endpoint branches, bulk branch, exact refinement eigenvalues, signed/complex amplitudes, and holonomy fiber identity. Positive weighted/mass BRC is not adequate because pole cancellation and complex/signed amplitudes are essential.

Population/branches:
- endpoint branch `E_r`, `r>=0`;
- bulk branch `B_s`;
- at half-integer resonance, the colliding pair is retained as a two-dimensional Jordan fiber rather than collapsed by equal scale.

Future operation: integer refinement `N -> qN`.
Observer: total spectral sum, plus centered/character holonomy observers when stated.

## Exact refinement law

For

`T_{s,N}(α)=(π/N)^(2s) Σ_{k=0}^{N-1} csc^(2s)(π(k+α)/N)`

and

`(R_q^(s)f)(α)=q^(-2s) Σ_{r=0}^{q-1} f((α+r)/q)`,

one has exactly

`T_{s,qN}=R_q^(s)T_{s,N}`.

The symmetric bilateral Hurwitz endpoint branch of order `2s-2r` has refinement eigenvalue `q^(-2r)`. The holonomy-constant function has eigenvalue `q^(1-2s)`.

## Untwisted complex-s asymptotic

Let

`Z_N(s)=1/2 (π/N)^(2s) Σ_{k=1}^{N-1} csc^(2s)(πk/N)`

and define

`c_{s,r}=[x^(2r)](x/sin x)^(2s)`.

The large-N meromorphic asymptotic is

`Z_N(s) ~ Σ_{r>=0} c_{s,r}(π/N)^(2r) ζ(2s-2r) + K(s)N^(1-2s)`

with

`K(s)=π^(2s-1/2)/2 * Γ(1/2-s)/Γ(1-s)`

`     =π^(2s-1/2)/2 * Γ(s)/Γ(s+1/2) * tan(πs)`.

The underlying complex-Riesz/cosecant asymptotic, including logarithmic exceptional cases, is prior art (Brauchart–Hardin–Saff 2009). The structural interpretation below is the current research frontier.

## RG spectral classification

Use scale generator `E=-(1/2)N∂_N`.

- `E N^(-2r)=r N^(-2r)`;
- `E N^(1-2s)=(s-1/2)N^(1-2s)`.

Thus the correction characteristic spectrum is `{0,1,2,...}` plus `s-1/2`.

### Integer `s=m`

`K(m)=0` because `tan(πm)=0`. The bulk eigenmode is dark rather than resonant. The endpoint analytic continuation tail beyond the finite integer range is killed by the trivial zeros of ζ; exact finite closure was established independently by residue identities.

### Half-integer `s=n+1/2`

The bulk eigenvalue equals the endpoint eigenvalue `q^(-2n)`. Define

`F_1(α)=FP_{z=1}[ζ(z,α)+ζ(z,1-α)]=-ψ(α)-ψ(1-α)`.

Taking the finite part of the Kubert distribution relation gives exactly

`q^(-1) Σ_{r=0}^{q-1} F_1((α+r)/q)=F_1(α)+2 log q`.

Hence on `{1,F_1}` the refinement is the universal Jordan block

`J_{n,q}=q^(-2n) [[1,2 log q],[0,1]]`.

Equivalently, the repeated Euler-Cauchy characteristic root forces `N^(-2n)log N`.

The exact log amplitude is

`c_{n+1/2,n}=Res_0 csc^(2n+1)x=binom(2n,n)/4^n`.

Therefore

`Coeff[N^(-2n)log N] Z_N(n+1/2)=binom(2n,n)/4^n * π^(2n)`.

Example:

`Z_N(3/2)=ζ(3)+(π^2/(2N^2))log N+(π^2/N^2)[γ/2-1/12+(1/2)log(2/π)]+O(N^-4)`.

This expansion was independently high-precision checked.

## Confluent odd-zeta projector

Let `D_qf(N)=f(qN)` and `λ_r=q^(-2r)`. For `M>=n`,

`P_res=((D_q-λ_nI)^2/(1-λ_n)^2) Π_{1<=r<=M,r!=n} ((D_q-λ_rI)/(1-λ_r))`

annihilates the Jordan pair and the first `M` ordinary correction modes:

`P_res Z_N(n+1/2)=ζ(2n+1)+O(N^(-2M-2))`.

For `n=1,q=2,M=1`:

`(16/9)Z_{4N}(3/2)-(8/9)Z_{2N}(3/2)+(1/9)Z_N(3/2)`

`= ζ(3)-17π^4/(23040N^4)+O(N^-6)`.

## Rank-one holonomy anomaly

For twisted complex-s sums, the bulk term is independent of `α`; it lies entirely in the constant holonomy sector. Therefore any zero-mean holonomy contrast removes it. In particular, for a nonprincipal even Dirichlet character `χ mod Q`,

`M_{s,N,Q}^χ=(1/(2Q^(2s))) Σ_{a mod Q} χ(a)T_{s,N}(a/Q)`

has

`M_{s,N,Q}^χ ~ Σ_{r>=0} c_{s,r}(π/(QN))^(2r)L(2s-2r,χ)`

with no `N^(1-2s)` mode.

At `s=n+1/2`, nonprincipal `L(1,χ)` is finite, so there is no logarithmic resonance. For a principal character `χ0 mod Q`, the log coefficient is

`[binom(2n,n)/4^n] * Res_{z=1}L(z,χ0) * (π/(QN))^(2n)`

and `Res_{z=1}L(z,χ0)=φ(Q)/Q`.

Hence the half-integer log is a principal/constant-holonomy anomaly and its amplitude detects the arithmetic pole at `z=1`.

## Prior-art boundary

Brauchart–Hardin–Saff, *The Riesz energy of the Nth roots of unity: an asymptotic expansion for large N*, Bull. Lond. Math. Soc. 41 (2009), 621–633, DOI `10.1112/blms/bdp034`, already contains the complete complex-parameter roots-of-unity Riesz asymptotic and the positive-odd exceptional logarithmic cases. Do not claim those asymptotics/log terms as new.

Current candidate synthesis/theorem package to investigate further:
1. BRC typed refinement eigenbranch organization;
2. universal half-integer Jordan cell and Euler-generator repeated-root interpretation;
3. confluent finite-scale projector for odd zeta;
4. rank-one constant-holonomy anomaly and disappearance under nonprincipal/centered observers;
5. pole-at-one -> finite-size-log transmutation formula.

## Next

1. Prove centered holonomy quotient semisimplicity as an exact operator statement.
2. Seek rigorous remainder/sign control for the confluent ζ(3), ζ(5), ... projectors.
3. Test whether higher-order arithmetic poles generate higher Jordan/log powers under analogous refinement towers.
