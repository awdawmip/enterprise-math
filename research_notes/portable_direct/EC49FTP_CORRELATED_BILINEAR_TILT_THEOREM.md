# EC49FTP supplement — correlated bilinear-tilt price priors retain conditional stochastic order

Status: **AUTHOR_PROVED / NUMERIC_DIAGNOSTIC / PARENT_DEPENDENT / NOT_REVIEWED**. Date: 2026-11-19. Retains original frozen native BRC16943 input `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`; this is only external price-prior postprocessing of EC49FTO and the EC49FTP curvature theorem. All price/transform definitions and clipping support are as in the main EC49FTP proof.

## A further theorem: correlated prices

Let a,b range over A=[3/4,49/64], B=[7/16,57/128] with a **correlated joint density**

`hκ(a,b)=Cκ f(a)g(b)exp(κab)`, κ≥0,

where Cκ>0 is the joint normalization. Assume positive C² f,g, f nondecreasing, log f''≤H, log g''≤−G with H,G≥0, and define α=44/45, β=10/9, dmax=7/960. If

`βG/54 ≥ αH/945 + κ(α/54+β/945)`

and

`(H+(945/54)κ)*dmax²/2 < 1`,

then the complete mixed conditional optimizer law obeys

`Z|M=m ≤_st Z|M=m'` for all m<m' in the interior M support, including the rightmost atom at Z=3/4.

This is an actual dependent-prior extension; no claim of product independence is used.

### Proof: continuous branch

The nonclipped joint density kernel is Kκ(m,z)=(16/945)hκ(a(m,z),b(m,z)). Its cross partial is

`∂m∂z log Kκ = -α(log f)''/945 - β(log g)''/54 - κ(β/945+α/54)`.

The first assumed inequality makes this nonnegative on the full rectangle. Therefore the continuous fiber kernel is TP2. Moving rightward fiber endpoints preserve conditional first-order stochastic order, exactly as in the independent-prior proof.

### Proof: atom ratio

For m∈(m2,m3), x=(740-m)/945, y=(47-m)/54, d=Ahi−x, T=3/4−L2(m); x'=-1/945, y'=-1/54, d'=1/945, T'=-1/60. As before the ratio of joint-M clipped atom mass and continuous mass factors into (945/864)Nκ/Qκ, but now

`Nκ=∫_0^d exp(ℓf(x+s)−ℓf(x)+κ y s) ds`,

`Qκ=∫_0^T exp(ℓf(x−αt)−ℓf(x)+ℓg(y−βt)−ℓg(y)−κ(αy+βx)t+καβt²) dt`.

For Eκ(s) the numerator integrand, f nondecreasing and κ,y≥0 imply Eκ(s)≤Eκ(d), while

`945 (Nκ)' = Eκ(d) -∫_0^d Eκ(s)[ℓf'(x+s)−ℓf'(x)+(945/54)κs] ds`

`≥ Eκ(d){1−[H+(945/54)κ]d²/2}>0.`

The logarithmic m-derivative of Qκ's integrand at fixed t is bounded above by

`t[αH/945−βG/54+κ(α/54+β/945)]≤0.`

As T shrinks strictly, Qκ decreases strictly; the clipping atom probability B/(B+I) increases strictly for m>m2. At m2 this atom enters at the maximal feasible Z, so combining with the continuous TP2 comparison proves the global mixed order. QED.

## A strictly log-convex **and dependent** example

Set f(a)=1+(a−3/4)², g(b)=b, κ=1; normalize hκ over A×B. The price variables are genuinely dependent because the mixed log-density derivative ∂a∂b log hκ=1≠0.

Take H=2, G=16384/3249. The exact correlated TP2 margin is

`βG/54−αH/945−(α/54+β/945)=11385908/138163725>0.`

The atom numerator growth condition reads

`[H+(945/54)κ]*(7/960)²/2=637/1228800<1.`

The f marginal **factor** remains strictly log-convex. The normalized *actual marginal of a* need not retain that curvature property under correlation; this theorem asserts the non-product joint density and the strictly log-convex factor, not a standalone claim about either normalized correlated marginal. The conditional stochastic order follows analytically for every m.

## Diagnostics and limits

Author-only numerical regression on this exact correlated hκ passed **9108** ordered conditional-CDF comparisons: 24 interior rational m-levels, 33 thresholds, SciPy adaptive quadrature with float64. The largest observed `F_{later}(z)−F_{earlier}(z)` was 0.0. This numeric evidence does **not** prove the continuum theorem: the two analytic inequalities and derivative calculation do.

No native Bellman rerun, formal reviewer, accepted Result, Source CLAIM or Activity is inferred. Next: find sharp necessity conditions for TP2 + a top atom under arbitrary joint priors, or construct a dependent prior that breaks the order while the continuous kernel remains TP2 because the atom compatibility fails.
