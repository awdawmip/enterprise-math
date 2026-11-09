# PREFIX-651-R6 — 三槽位偏度、峰度的三阶单侧外推

Date: 2026-11-10 (Asia/Shanghai). Role: independent TASK_RESEARCH.
Status: AUTHOR_PROVED / EXACT_RATIONAL_IMPLICATION_CHECKED / UNREVIEWED / NOT_ADMITTED.
Frozen scientific pin: f42f2906d77f24085c123f3ccfe9667d41caa96d.
Mother objective: certify the global maximum of the sampling-stop variance in the frozen signed two-informative-direction BRC first-stop statistical observer.

## Domain and inherited inputs

Retain the signed 189-layer observer of PREFIX-645–650. Let Y(p,z) denote the Poissonized first-stop maximum; T_q denotes its corresponding marked discrete sampling count. Put a=E[Y], b=Var(Y), c=κ₃(Y), d=κ₄(Y), t=1/q, B=b−at. Define
  g₁(t)=(c−3bt+at²)/B^(3/2), g₂(t)=(d−6ct+7bt²−at³)/B².
For R={|p−1/6|≤2^(−29), |z−19/128|≤2^(−29)}, PREFIX-649/650 supplies strict envelopes
  108<a<110, 335<b<338, −1266<c<−1153, 14638<d<86111.
For t∈[0,1/12], B>325 and √B>18. At t=0 both functions extend analytically, with limits γ₁,∞=c/b^(3/2), γ₂,∞=d/b².

## Theorem 651.1: signed third derivatives

On all R×[0,1/12], one has
  −3/10 < g₁'''(t) < 0 < g₂'''(t) < 11/10.

Proof: Three differentiations of the exact cumulant transforms yield
  g₁'''(t)=−3a²(a²t²+3abt−35ac+66b²)/(8B^(9/2)),
  g₂'''(t)=6a(4a²d+11ab²t−6a²ct−18abc+13b³)/B⁵.
Both sign-corrected numerators have strictly positive summands, using a,b,d>0, c<0 and t≥0. Applying the inherited strict envelopes and B>325, √B>18 gives exact rational bounds
  |g₁'''| < [3·110²(110²/12² + 3·110·338/12 +35·110·1266+66·338²)]/[8·325⁴·18]
           = 54117127669/192786750000 < 3/10;
  0<g₂''' < [6·110(4·110²·86111 +11·110·338²/12+6·110²·1266/12
                  +18·110·338·1266+13·338³)]/325⁵
           = 730778040872/725181640625 < 11/10.
These strict inequalities prove Theorem 651.1.

## Theorem 651.2: three-slot one-sided cubic extrapolation

For q≥12 such that q,2q,4q are all model-admissible sampling parameters, write γᵢ(q)=gᵢ(1/q) and
  Rᵢ(q)=γᵢ(q)/3−2γᵢ(2q)+8γᵢ(4q)/3.
Then uniformly on R:
  γ₁,∞ − 1/(160q³) < R₁(q) < γ₁,∞,
  γ₂,∞ < R₂(q) < γ₂,∞ + 11/(480q³).
For the integer slots q=12,24,48:
  γ₁,∞−1/276480 < γ₁(12)/3−2γ₁(24)+8γ₁(48)/3 < γ₁,∞,
  γ₂,∞ < γ₂(12)/3−2γ₂(24)+8γ₂(48)/3 < γ₂,∞+11/829440.

Proof: Let h=1/q. Quadratic Lagrange interpolation at nodes h,h/2,h/4 evaluated at zero has weights 1/3,−2,8/3; it cancels monomials of degrees one and two. The order-three interpolation remainder yields for some ξ∈(0,h):
  g(0)−R(g) = g'''(ξ)/6 · (−h)(−h/2)(−h/4)
            = −g'''(ξ)h³/48.
Consequently R(g)−g(0)=g'''(ξ)h³/48. Apply Theorem 651.1 to determine both signs and bounds. At q=12 the stated fractions follow from exact rational arithmetic. QED.

## Verification, relation to P000 and continuation

The companion Python standard-library Fraction certificate checks the exact rational third-derivative majorants, polynomial differentiation identities at rational witnesses, Lagrange coefficients and the q=12 error fractions. Observed: ALL_CHECKS_PASS 43. The universal derivative identities and interpolation-remainder proof are written above; numerical checks are supplementary.

Inputs are the published cumulative evidence from PREFIX-645@f11c0345bf89321aba48d90671c244bdec25d416, PREFIX-648@6b53f51abe70ac29a591fa9fcd29c1308f6c98e2, PREFIX-649@cb21c9452f5bc094493cd92bfa37be99ab988782, PREFIX-650@7b796596aad06919954529220566561096aaf27a. No 189-layer survivor-state or 96-port native dynamics run was repeated. The (p,z) coordinates are statistical observer readouts, not a native two-dimensional spatial plane. P000 and frozen scientific inputs are unchanged. The 48-slot value is a rigorously permissible comparison within the stated parameter domain; no physical 48-slot execution is asserted.

Next executable science: evaluate γ₁(48),γ₂(48) from the pinned 189-layer moments to obtain an exact three-slot worked case and inspect the observed error within the certified interval; independently improve local moment/score derivative bounds to enlarge R. The parent global two-parameter variance-extremum problem remains open.
