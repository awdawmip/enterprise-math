# #1162 Basel discrete rotation spectrum — holonomy observer/shell projector frontier

Status: `RESEARCH_NOTE / DURABLE FRONTIER / NOT PROMOTED`
Researcher-ID: `EM-DIRECT-B62D`
At: `2026-09-06T16:10:00+08:00`
Source journal: `awdawmip/chatgpt-global-knowledge:journal/enterprise-math/2026-09-06/20260906T161000+0800-basel-holonomy-observer-shell-projectors-r2.md`
Progress-Event-ID: `basel-holonomy-observer-shell-20260906-r2`

## 1. Anomaly-free odd-zeta holonomy contrast

For the general half-integer family `s=n+1/2`, the anomalous bulk/Jordan branch is independent of holonomy. The rational twists `α=1/2` and `α=1/3` obey

`B_z(1/2)=2(2^z-1)ζ(z)`

`B_z(1/3)=(3^z-1)ζ(z)`

for the symmetric bilateral Hurwitz kernel `B_z` (analytic continuation understood).

Set

`D_n=3^(2n+1)-2^(2n+2)+1`

and

`H_{n,N}=[T_{n+1/2,N}(1/3)-T_{n+1/2,N}(1/2)]/D_n`.

Then the holonomy-constant bulk term cancels. At the resonant correction `z=1`, the pole residues also cancel, so the Jordan/log mode disappears. The leading continuum value is still `ζ(2n+1)`. Hence `H_{n,N}` has only the ordinary even refinement corrections `N^(-2r)` and admits standard (non-confluent) scale projection.

This is an explicit BRC observer result: passing to a fiber contrast factors through the quotient by the constant branch and removes the nilpotent half-integer extension. Compared with the untwisted principal observable, one refinement level is saved.

### ζ(3) instance

Define

`C_N=[T_{3/2,N}(1/3)-T_{3/2,N}(1/2)]/12`.

Then

`C_N=ζ(3)+(π^2/(24N^2))log(27/16)-17π^4/(51840N^4)+O(N^-6)`.

Therefore

`(4C_{2N}-C_N)/3=ζ(3)+17π^4/(207360N^4)+O(N^-6)`.

The displayed constants were high-precision checked; the accelerated error times `N^4` converges to `17π^4/207360`.

## 2. Exact integer refinement-shell polynomial

For integer `m>=1`, define the half-total nontrivial q-holonomy shell

`Σ_{m,q,N}=(1/2)Σ_{a=1}^{q-1}T_{m,N}(a/q)`.

Exact mode grouping gives

`Σ_{m,q,N}=q^(2m)Z_{qN}(m)-Z_N(m)`.

Since the integer untwisted half trace is an exact finite polynomial in `N^-2`, writing `x=q^2` makes `Σ_m(x;N)` a degree-m polynomial with `Σ_m(1;N)=0` and

`[x^m]Σ_m(x;N)=ζ(2m)`.

Thus even zeta is exactly the top coefficient of the refinement-shell response polynomial.

For arbitrary distinct integers `q_1,...,q_m >=2`, `x_j=q_j^2`, Lagrange leading-coefficient extraction gives, for every N,

`ζ(2m)=Σ_j Σ_{m,q_j,N}/[(x_j-1) Π_{l!=j}(x_j-x_l)]`.

Equivalently with the full shell packet `V_{q,N}=Σ_{a=1}^{q-1}T_{m,N}(a/q)=2Σ_{m,q,N}`,

`ζ(2m)=Σ_j V_{q_j,N}/[2(x_j-1)Π_{l!=j}(x_j-x_l)]`.

For `m=2`, `q_1=2`, `q_2=3` this reduces to the exact all-N identity

`ζ(4)=-(1/30)T_{2,N}(1/2)+(1/40)T_{2,N}(1/3)`.

At `N=1`, it immediately yields `ζ(4)=π^4/90`. The general formula was checked for `m=2,3,4` and multiple N to high precision.

Interpretation: `m=1` is uniquely contamination-free because the shell polynomial is only

`Σ_1(x)=ζ(2)(x-1)`.

## Status / prior-art caution

Finite cosecant even-power sums being polynomials and their zeta/Bernoulli coefficients are classical. Do not claim historical novelty for polynomiality itself. Current project value is the refinement-shell top-coefficient interpretation and its placement alongside the scale/Jordan/BRC observer framework.

## Next

1. Prove a unified interpolation duality theorem: scale-node interpolation in refinement eigenvalue versus holonomy-shell interpolation in `x=q^2`.
2. Seek rigorous remainder/sign bounds for the centered ζ(3) estimator.
3. Test whether a finite set of rational-holonomy packets can impose Hermite zeros at the resonant arithmetic point `z=1`, providing single-scale high-order odd-zeta reconstruction.
