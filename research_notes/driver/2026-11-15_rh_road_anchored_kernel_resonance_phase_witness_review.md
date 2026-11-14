# RH composite-road: anchored double-frequency kernel and explicit phase witness

Status: DRIVER MATHEMATICAL CROSSCHECK / PROVED WITHIN STATED DEFINITIONS; NOT A NATIVE RESULT, NOT TASK COMPLETION, NOT AN RH PROOF.
Date: 2026-11-15.
Scope: Classical Fourier/geometric-sum auxiliary model in the immutable RH-ROAD-KERNEL-20260909 and RH-ROAD-TAIL-20260909 taskbooks, not an Enterprise-native geometry transfer theorem.
Scientific source and origin: EM-FREE-C4A91D, RA-C4A91D-RH-HANDOFF-20260909; handoff `research_handoffs/COMPOSITE_ROAD_RH_20260909/START_HERE.md`; original scientific source pinned at `9d7c4c6eafc5479a6795a128fc0288fc893bed3c`. This note is a later driver's independently derived, scoped crosscheck, not a replacement of the original author or an independent Native review of an immutable Result. No live CLAIM is asserted.

## Exact statement and proof

Write `h_N(theta)=sum_{n=1}^N exp(i*n*theta)`, and define the raw anchored kernel `K(theta,phi)=sum_{N>=1} h_N(theta)*conj(h_N(phi))/N^2`. Angles are real modulo `2*pi`. This statement makes no claim about the arithmetic Ramanujan coefficients or the full-road energy.

For `z=exp(i*theta)!=1` and `w=exp(-i*phi)!=1`, the finite geometric sum is
`h_N(theta)=z(1-z^N)/(1-z)`, `conj(h_N(phi))=w(1-w^N)/(1-w)`. Consequently, with `Li_2(u)=sum_{N>=1}u^N/N^2` for `|u|<=1`,
```
K(theta,phi) = zw/((1-z)(1-w)) *
               (zeta(2)-Li_2(z)-Li_2(w)+Li_2(zw)).
```
All four series converge absolutely. The estimate `|h_N(theta)|<=min(N,2/|1-z|)` proves convergence without any appeal to analytic continuation or an unverified zero-free region. For the truncation `K_M=sum_{N=1}^M ...`, the explicit tail bound for every integer `M>=1` is
```
|K-K_M| <= 4 / (M * |1-z| * |1-w|).
```
This follows from `sum_{N>M} N^-2<=1/M`. The bound is uniform in `theta-phi` (including exact resonance) on any region with `|1-z|>=delta>0` and `|1-w|>=delta>0`; hence no spurious `1/|theta-phi|` denominator is required. It is *not* uniform as either frequency approaches zero. Conjugating and exchanging the two frequencies gives `K(phi,theta)=conj(K(theta,phi))`, and `K(theta,theta)>=0`.

For `t in [0,2*pi]` representing the positive angular distance from 0, the classical absolutely convergent cosine Fourier series yields `sum_{N>=1}(1-cos(N*t))/N^2 = pi*t/2-t^2/4`. Thus
```
K(t,t) = (pi*t-t^2/2)/(4*sin(t/2)^2)   (0<t<2*pi),
K(t,t) = pi/t - 1/2 + O(t)             (t -> 0+).
```
The apparent singularity at `theta=phi` away from zero is removable; the actual positive diagonal diverges as the frequency approaches zero.

The *raw unregularized* series is not defined on the zero-frequency axes: `K_M(0,0)=M`. For `phi!=0 (mod 2*pi)`, letting `w=exp(-i*phi)`,
```
K_M(0,phi) = w/(1-w) * (H_M - sum_{N=1}^M w^N/N).
```
The second sum converges by Dirichlet's test while `H_M=log M+O(1)`; the nonzero coefficient `w/(1-w)` gives logarithmic divergence. The symmetrical assertion applies to `K_M(theta,0)`. Any claimed all-frequency kernel must therefore state an explicit subtraction, regularization, or domain restriction.

## Exact rational-frequency phase-loss witness

Take two distinct nonzero Fourier frequencies `theta=pi` and `phi=pi/2`. Since `h_N(pi)=-1` for odd `N` and zero for even `N`, while `h_N(pi/2)=i,-1+i,-1,0` according to `N mod 4=1,2,3,0`, one gets
```
K(pi,pi/2) = i * sum_{k>=0}(4*k+1)^-2
             + sum_{k>=0}(4*k+3)^-2.
```
In particular `A:=Re K(pi,pi/2)=sum_{k>=0}(4*k+3)^-2>0` (indeed `A>=1/9`).

Use identical per-mode powers but opposite relative phases:
```
F_N(+) = h_N(pi) + h_N(pi/2),
F_N(-) = h_N(pi) - h_N(pi/2).
E(+/-) = sum_{N>=1} |F_N(+/-)|^2/N^2.
```
The coefficient vectors `(1,+1)` and `(1,-1)` both have mode powers `(1,1)`, yet
```
E(+) - E(-) = 4*Re K(pi,pi/2)
            = 4*sum_{k>=0}(4*k+3)^-2
            >= 4/9 > 0.
```
The same strict inequality already holds at every finite cutoff `M>=3`: `E_M(+)-E_M(-)=4*sum_{4k+3<=M}(4k+3)^-2`. This is a rigorous fixed-origin, same-powers/different-energy witness. It refutes only the proposed *power-only replacement of the anchored observation*, not the full arithmetic route, the Nyman criterion, nor RH itself.

## Interface / remaining obligations

1. These elementary Fourier identities provide a phase-preserving kernel, a quantitative fixed-frequency cutoff, a zero-frequency obstruction, and an exact non-diagonal witness. They do not constitute completion of the RH-ROAD-KERNEL task because its coupling/Schur interface and entire source-admission/review obligations are separately specified.
2. The RH-ROAD-TAIL task also requires arithmetic `a`, `M(a)` and all-shell bounds for `sum_{N>=M(a)} B_(a,N)^2/N^2`; none follows from the fixed-frequency bound `4/[M|1-z||1-w|]`. The latter loses uniformity for rational frequencies whose denominator grows. No unconditional `D_a=O(a)` result is claimed.
3. The historical source is not to be erased or reattributed; the original audit/kernel dependencies and any live owner/claim are governed by current canonical control, not by this note.
