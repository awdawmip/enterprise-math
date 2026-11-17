# IPQ — finite-phase monotonicity and quantitative mesh certificate (2026-11-17)

Task: RS-EMW59A-1159-IPQ-EULER; publication TP2-92EA595599F5DC6254F9.
Scope: author-side derivation / numerical preflight, NOT independent Driver review or formal acceptance.
Frozen sources: original W59A state-machine handoff (2026-09-09), `WALLIS_SINE_INTERNAL_PHASE_QUANTIZATION_EULER_PRODUCT_20260904.md` at `9e6e9abe813aa17a7eff1ee8278e2f0e9f73312c`, and finite-core note at `269b1cafac209e42d6770b0aae4a4d8d0a981f8a`.
Semantics: algebraic finite Dirichlet carrier plus separately declared internal power-series completion. No classical pi/circle spectrum is a proof premise; any decimal is a compatibility diagnostic.

## Definitions and exact dependencies

Define the entire power series
S(x)=sum_{j>=0} (-1)^j x^(2j+1)/(2j+1)!, C(x)=sum_{j>=0} (-1)^j x^(2j)/(2j)!.
From termwise differentiation: S'=C, C'=-S, S(0)=0,C(0)=1, S'(0)=1; addition/doubling and S²+C²=1 follow from uniqueness for the corresponding linear ODE (or direct power-series convolution).
Existence of a smallest strictly positive root tau of S: S(x)>0 near 0 by derivative 1; S(4)<-268/405<0 from the finite alternating-series upper bound (the remainder after x^9/9! is negative and alternating magnitudes decrease from that point). Continuity gives at least one positive root, and no positive roots sufficiently close to 0, so a first exists. Thus S>0 on (0,tau). Doubling gives C(tau/2)=0 and S(tau/2)=1; then C(tau)=-1. Consequently C'=-S<0 on (0,tau), so C strictly decreases from 1 to -1. Since S''=-S<=0 and S(0)=0, S(tau/2)=1, on [0,tau/2]:
2y/tau <= S(y) <= y. Also tau>=2.

For M>=2 let D_0(u)=1, D_1(u)=2-u, D_{n+2}(u)=(2-u)D_{n+1}(u)-D_n(u). From sine addition and this recurrence:
D_n(2-2C(theta))S(theta)=S((n+1)theta), n>=0.
Therefore for 1<=k<M, u_{k,M}=2-2C(k tau/M) are M-1 distinct, strictly ordered roots in (0,4) of D_{M-1}; degree M-1 proves completeness. Double-angle gives
rho_{k,M}:=M sqrt(u_{k,M})=2M S(k tau/(2M)).
As in the source, 2k<=rho_{k,M}<=k tau. D_{M-1}(0)=M gives the exact finite spectral factorization.

## New quantitative refinement theorem (finite mesh)

**Theorem.** For every integer k>=1 and M>=k+1, the mode radius rho_{k,M} increases strictly with M and satisfies

  0 < k tau - rho_{k,M} <= k^3 tau^3/(24 M^2),

  0 <= 1/rho_{k,M}^2 - 1/(k^2 tau^2) <= tau^2/(48 M^2).

In particular, for each fixed k, rho_{k,M} increases to k tau with a certified O(M^-2) bound.

**Proof.** Put a=k tau>0 and y=a/(2M), so 0<y<tau/2. As S''=-S<0 on (0,tau), S is strictly concave there, with S(0)=0. Hence S(y)/y strictly decreases with y, and rho_{k,M}=a[S(y)/y] strictly increases with M.

The integral Taylor identity from S''=-S is
  y-S(y)= integral_0^y (y-t) S(t) dt.
On [0,tau/2], 0<=S(t)<=t, so
  0<=y-S(y)<= integral_0^y (y-t)t dt = y^3/6.
Multiplication by 2M proves the first explicit bound; the strict lower inequality holds for y>0 because S(t)>0 for t in (0,y).
For the inverse-square gap, use rho<=a, rho>=2k and a^2-rho^2=(a-rho)(a+rho)<=2a(a-rho). Thus
  1/rho^2-1/a^2 <= [2a*k^3*tau^3/(24M^2)]/[(2k)^2*(k tau)^2] = tau^2/(48 M^2).
All inequalities are internal consequences of the declared S,C analytic completion. QED.

**Finite-head corollary.** For 1<=K<M and |x|<=R with R>=0, let
  H_{M,K}(x)=prod_{k=1}^K(1-x^2/rho_{k,M}^2)
  P_K(x)=prod_{k=1}^K(1-x^2/(k^2 tau^2)).
A telescoping difference of products, and each factor's absolute bound 1+R²/(4k²), yield
  sup_{|x|<=R}|H_{M,K}(x)-P_K(x)|
      <= exp(R²/2) * K R² tau²/(48 M²).
We used sum_{k>=1} 1/k² <=2, proved without an infinite zeta value via 1/k²<=1/[k(k-1)] for k>=2.
Combining the original direct log-free tail certificate, for K>=1, 2K>=R, M>K+1,
  sup_{|x|<=R}|F_M(x)-P_K(x)|
      <= exp(R²/2)[R²/(4K)+K R² tau²/(48M²)].
Let M tend to infinity at fixed K and use the independently preserved compact convergence F_M=>S(x)/x. Then the original internal Euler product and its locally uniform tail certificate follow. This corollary supplements rather than replaces the sharper direct finite coefficient O(M^-2) error for F_M.

## Exact algebra / analytic dependency graph

A. Integer continuant recurrence -> degree M-1, D_{M-1}(0)=M, exact determinant F_M.
B. Power-series differentiation + addition + sign certificate S(4)<0 -> existence/positivity tau, C monotonicity, doubling endpoints.
C. A+B -> recurrence identity -> distinct complete finite roots -> quantized radii.
D. B+C -> 2k lower bound; strict concavity + integral Taylor -> increasing radii + quantitative O(M^-2) gap.
E. C+D -> finite factorization + direct tail (original W59A proof) + finite-head bound above.
F. Finite coefficient compact convergence (existing verified core) + E -> uniform internal Euler product.
G. Product evaluated at tau/2 + finite rational Wallis carrier -> tau=2 W_infty.
Classical sine/cosine/pi naming is downstream compatibility only.

## Reproducibility / coverage

`IPQ_QUANT_MESH_PREFLIGHT_20261117.py` evaluates S,C from their power series, obtains tau as the root in (3,4) using the internal series, and checks recurrence residuals, positivity, mesh monotonicity and both inequalities on M=2,3,4,5,8,16,32 (63 pairs), at 70-digit precision. Exploratory numerical agreement is not an independent proof nor formal acceptance. The analytical proof above is primary.
Unfinished review: independent author-disjoint audit of the complete seven-lemma graph and optional Lean extraction. No new CLAIM, reviewer authority, or Foundation promotion follows from this note.
