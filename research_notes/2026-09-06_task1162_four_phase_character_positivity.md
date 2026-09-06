# TASK #1162 — four strict positivity phases for quadratic-character rotation kernels

Status: `RESEARCH_FRONTIER / THEOREM PACKAGE CANDIDATE / NOT PROMOTED`
Researcher-ID: `EM-DIRECT-B62D`
At: `2026-09-06T21:23:00+08:00`

## Kernel

For a positive fundamental discriminant D with real primitive even quadratic character chi_D, define

`F_D(t)=sum_{n>=1} chi_D(n)e^{-nt}` and the normalized rotation/Laplace kernel `h_D(z)= [F_D(sqrt z)/sqrt z]/[-L(-1,chi_D)]`.

The BRC observer ladder is genuinely strict.

## Phase 1 — LCM / infinitely divisible

Witness: `D=5`.

`h_5(z)=5*sinh(sqrt z/2)*sinh(sqrt z)/(sqrt z*sinh(5sqrt z/2))`.

Its logarithmic derivative has inverse-Laplace heat density

`K_5(t)=sum_{n>=1} exp(-4pi^2 n^2 t/25) - sum_{n>=1} exp(-pi^2 n^2 t) - sum_{n>=1} exp(-4pi^2 n^2 t)`.

A direct integer injection proves K_5(t)>0: map the second right-hand family n to left k=5n, and map the first family by n=2m -> k=5m-1, n=2m+1 -> k=5m+2. Images are disjoint and each mapped left Gaussian weight is >= (strictly > for the first family) its source. Hence -log h_5 is Bernstein and h_5 is LCM.

## Phase 2 — CM but not LCM

Witness: `D=365`.

The weighted theta is rigorously positive on the whole positive axis (interval/modular certificate in `research_notes/2026-09-06_task1162_cm_not_lcm_d365.md`), so h_365 is completely monotone. But the character polynomial has a certified root rho whose z=(-Log rho)^2 lies in Re z>0, so h_365 has a right-half-plane zero and cannot equal exp(-phi) with phi Bernstein. Thus CM does not imply LCM in this family.

A convenient necessary LCM root-wedge condition follows: for every character-polynomial root rho with 0<|rho|<1,

`-log|rho| <= dist(arg rho, 2pi Z)`.

Violation puts z=(-Log rho)^2 in the open right half-plane. D=365 violates it with `0.03858947479... > 0.03615453022...`.

## Phase 3 — positive kernel but not CM

Witness: `D=53`.

The character polynomial admits an exact positivity decomposition on 0<x<1, so F_53(t)>0 for all t>0 and the associated finite-rotation mismatch flow is one-sided/monotone. However the weighted theta is rigorously negative near the self-dual point (approximately -0.1107477...), so the normalized g_53 is not completely monotone.

## Phase 4 — signed

Witness: `D=173`.

The character polynomial is already negative at the exact rational point x=4/5, so F_173(t) changes sign and no global positive-kernel compression is valid.

## Strict hierarchy

`LCM  subsetneq  CM  subsetneq  kernel-positive  subsetneq  signed/unrestricted`,

with explicit witnesses `D=5,365,53,173`.

## General zero/pole heat criterion

For a normalized meromorphic kernel h of order <1 with zeros {-b_j}, poles {-a_k}, all in the open left half-plane and summable reciprocals, the genus-0 product gives

`-d/dz log h(z) = sum_k 1/(z+a_k) - sum_j 1/(z+b_j)`.

Hence

`-d/dz log h(z) = int_0^infty e^{-zt} K(t) dt`,

`K(t)=sum_k e^{-a_k t}-sum_j e^{-b_j t}`.

Therefore h is LCM iff K(t)>=0 for all t>0. In the character family this is a pole-heat versus zero-heat dominance condition. Right-half-plane zeros are an immediate obstruction before this comparison is even available.

## BRC consequence

The positive theta/measure observer is not safe for future logarithmic or infinite-divisibility operations: it deletes complex zero provenance. D=365 is an explicit information-loss witness. Finite moment/cumulant jets are also insufficient: the first 20 cumulants at z=0 are positive for D=365 even though global LCM fails.

## Literature boundary

Hyperbolic infinitely-divisible laws are classical (Pitman–Yor, 2003), and current work also studies Thorin positivity for Dirichlet L-functions themselves. No historical novelty claim is made for the general Bernstein/zero-free principles. The project candidate is the strict four-phase classification inside this finite-rotation quadratic-character kernel family and the D=365 certified phase separation.
