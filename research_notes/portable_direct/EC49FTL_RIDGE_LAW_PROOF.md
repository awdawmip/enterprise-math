# EC49FTL — Exact clipped ridge distribution and expected value of q140 price optimization

**Status:** AUTHOR_PROVED / EXACT_RATIONAL_FRACTION_CHECK_PASSED / CONDITIONAL_ON_EC49FTH_BELLMAN / NOT_REVIEWED.  
**Date:** 2026-11-19. **Frozen scientific pin:** awdawmip/enterprise-math@fc0f038e7bfd12c886b4d37f900bfb770c0f61ab.  
**Parents:** EC49FTH PR #2774@999bf1069403306b3813e0e390dae4435d7b4b8c and EC49FTK PR #2776@c8a24ab9f007c8d6348f45c60e9806c2fbfe238e.

## Question and observer scope

In the native BRC16943 price experiment, choose the q32 discount a and q34 discount b independently uniformly in the rectangle A=[3/4,49/64], B=[7/16,57/128], then optimize the q140 discount z over [11/16,3/4] to maximize the normalized exact exchange gap G(a,b,z)=D-S. Determine the full probability law of z*(a,b), its moments, the mean/variance of the achieved optimized gap and the improvement over a fixed z=3/4.

These probability statements refer only to the stated **uniform external price design**. They are not distributions of P000 Cells, paths, original states, physical query outcomes, or BRC branch multiplicities. All 141 named profiles and 228 physical original-index observations remain exactly those of the pinned parent. No observer quotient or science repin is performed.

## Inherited exact native Bellman premise

The EC49FTH parent author-proved exact unrestricted Bellman values on the complete closed box:
D=min(329-36a-68b-141z, 334-141a-62b-45z, 326-141a-47b-43z);
S=332-141a-8b-105z.
The EC49FTK deduction establishes the unique maximizing discount
z*=min(3/4,T(a,b)), T(a,b)=(105a-6b-5)/96.
Its optimized gap M=max_z G is
M=(525a-462b-9)/8 for a≤a_c(b) and M=47-54b for a≥a_c(b),
where a_c(b)=(77+6b)/105. Equalities agree on the switching boundary.

The following theorems are unconditional analytic consequences **of those explicit affine parent formulas**. Their native Bellman interpretation inherits the parents' AUTHOR_PROVED/NOT_REVIEWED status.

## Theorem 1 — complete mixed probability law of the clipped optimizer

Let u=64(a-3/4), v=128(b-7/16). By uniformity, u and v are independent Uniform[0,1]. Exactly,

T=569/768+(35u-v)/2048.

Set X=35u-v, x_c=56/3, X*=min(X,x_c), and Z*=569/768+X*/2048. Because x_c is strictly between 0 and 34, the complete CDF of X* is

F(x)=0 for x<-1;
F(x)=(x+1)^2/70 for -1≤x≤0;
F(x)=(x+1/2)/35 for 0≤x<56/3;
F(x)=1 for x≥56/3.

Equivalently the absolutely continuous part has density
f(x)=(x+1)/35 on (-1,0) and f(x)=1/35 on (0,56/3), with an atom of exactly 19/42 at x=56/3. Thus the optimizer is genuinely interior with probability 23/42 and is clipped to z=3/4 with probability 19/42. The continuous z-support begins at 4549/6144; in z coordinates multiply the x-density by 2048 and substitute x=2048(z-569/768).

Moreover at fixed b:
P(z*=3/4 | b)=(217-384b)/105 for all b∈B.

**Proof.** The difference of two independent uniforms U[0,35] and U[0,1] has convolution density (x+1)/35 on [-1,0], 1/35 on [0,34], and (35-x)/35 on [34,35]. Clipping at x_c=56/3 collapses its right tail into a single atom. Direct integration up to x_c gives F(x_c-)=23/42; the remaining mass is 19/42. For the conditional formula, z*=3/4 precisely when a≥a_c(b); divide A_1-a_c(b) by the a-interval width 1/64.

## Theorem 2 — exact moments of the optimizer and of the optimized exchange gap

Under the same independent uniform price design,

E[Z*]=964373/1290240,
Var(Z*)=654049/69363302400;

E[M]=494813/21504,
Var(M)=60097/1204224.

These are exact rational fractions. The optimized-gap variance is expressed in squared normalized-cost units; Var(Z*) is in squared dimensionless discount units.

**Proof.** For k=1,2 calculate
E[(Z*)^k] = 1/area × ∫_{b0}^{b1} [∫_{a0}^{a_c(b)} T(a,b)^k da + (a1-a_c(b))(3/4)^k] db,
and
E[M^k] = 1/area × ∫_{b0}^{b1} [∫_{a0}^{a_c(b)} ((525a-462b-9)/8)^k da + (a1-a_c(b))(47-54b)^k] db,
with area=(1/64)(1/128)=1/8192. All integrands and limits are rational polynomials. The attached pure-stdlib Fraction checker evaluates both k=1 and k=2 exactly, independently of the convolution calculation, and checks the resulting variance by subtracting squared first moments. It also recomputes the optimizer moments from the mixed CDF independently.

## Theorem 3 — exact benefit of optimizing z rather than using the top face

At fixed z=3/4, the mean exchange gap over A×B is
E[G(a,b,3/4)]=154009/6720.

Consequently the exact mean incremental improvement from optimizing z is
E[M-G(a,b,3/4)]=3307/35840 > 0.

In fact this has the geometric identity
E[M-G(a,b,3/4)]=36·Vol(Dmid)/(area),
where Vol(Dmid)=3307/10569646080 is the full three-dimensional Dmid optimal-cell volume established by EC49FTK. Also, compared to drawing z uniformly over its full interval (EC49FTK's mean 1317531013/61931520), the mean value gained by optimizing it for each (a,b) is 107530427/61931520.

**Proof.** When a≥a_c(b) the unique constrained optimizer is z=3/4 and the gain is zero. When a<a_c(b), the top face lies on Dmid, whose gap slope in z is -36, so the gain is exactly 36(3/4-T(a,b)). Thus the average over the price rectangle equals 36/area times the three-dimensional volume below the top face and above T, i.e. Dmid. Substituting the previously proved exact phase volume establishes the formula. The fixed-top expectation follows by directly integrating the two affine top-face expressions on either side of a_c(b).

## Exact verification and boundaries

Included: EC49FTL_RIDGE_LAW_VERIFY.py (pure standard-library Fraction polynomial integrator and a separate distribution-moment calculation); EC49FTL_RIDGE_LAW_CERT.json; EC49FTL_RUN_LOG.txt with exact observed execution. Every reported fraction has a corresponding assertion in the verifier. This proof uses the parent's actual affine native Bellman result and does not redo original 228-query Bellman enumeration, the 141-profile decision-tree replay, independent raw94 parsing, or a formal proof assistant run. Independent project mathematical review remains pending.

**Next scientific question:** derive the sharp law of the optimized gap M itself (not just its first two moments), including its piecewise-polynomial CDF and boundary singularities; separately test whether the clipped ridge structure survives the next genuinely native Bellman region z<11/16. Do not extrapolate current parent optima across unverified box faces.
