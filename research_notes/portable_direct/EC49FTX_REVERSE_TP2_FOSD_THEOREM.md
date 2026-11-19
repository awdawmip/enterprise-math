# EC49FTX — Strict reverse-TP2 continuous fiber with full mixed stochastic order

Date: 2026-11-19. **AUTHOR_PROVED / EXACT_FRACTION_VERIFIED / PARENT_DEPENDENT / NOT_REVIEWED**.

## Frozen source, type and question

This work takes the native BRC16943 input fixed at commit fc0f038e7bfd12c886b4d37f900bfb770c0f61ab. Its native Bellman parent is EC49FTH [PR #2774](https://github.com/awdawmip/enterprise-math/pull/2774) @999bf1069403306b3813e0e390dae4435d7b4b8c, and the immediate price-prior observer parent is EC49FTW [PR #2807](https://github.com/awdawmip/enterprise-math/pull/2807) @50b012f33f4e48f0f1357e6f0a164f10cd725414. Native optimality is inherited author evidence, NOT_REVIEWED. This is an **external price-prior observer** problem, not a fresh native Bellman run or a claim about P000 heartbeat dynamics.

Question: Is TP2 of the *continuous* conditional fiber necessary for full stochastic monotonicity of the mixed clipped optimizer? **No**, even with the original box, its exact clipped fiber and a globally positive polynomial prior.

## Constructed prior and exact theorem

On the external price rectangle a in [3/4,49/64], b in [7/16,57/128] define the affine forms

    M_*(a,b) = 525a/8 - 231b/4 - 9/8,
    Z_*(a,b) = 35a/32 - b/16 - 5/96,

and the positive unnormalized joint price density

    h(a,b) = 1 - M_*(a,b)*Z_*(a,b)/1000.

These forms extend the nonclipped inverse chart as affine functions over the box. In the clipped region Z_* is **not** the true optimized Z, which remains U=3/4, and no clipped event is reclassified.

**Theorem.** For this h and inherited high-gap m-domain I=(1469/64,187/8), all pairs m<m' in I satisfy

    Law(Z | M=m) <=_st Law(Z | M=m').

At the same time the continuous kernel is everywhere strictly reverse-TP2: its mixed log derivative in (m,z) is negative.

## Exact positivity and reverse TP2

All box corners (and hence the full rectangle, by affine extrema) satisfy 0<M_*<=12213/512<24 and 0<Z_*<=4657/6144<1. Hence h>976/1000, so normalization is finite and strictly positive; that normalizer cancels from conditional distributions.

On the **nonclipped** parent branch,

    a(m,z)=(47-m)/945+(44/45)z,
    b(m,z)=1/27-m/54+(10/9)z,
    K(m,z)=(16/945)*(1-m*z/1000),
    L(m)=(8m+173)/480, U=3/4.

Consequently

    partial_m partial_z log K = -(1/1000)/(1-m*z/1000)^2 < 0,

so K is strictly reverse-TP2 throughout the continuous fiber.

## The normalized continuous fiber nevertheless shifts right

Put t=187/8-m in (0,27/64). Then L=U-t/60 and L'(m)=1/60. For L(m)<z<U, the conditional **continuous-component** upper-tail probability is

    H_m(z)=(U-z)/(U-L) * N/D,
    N=1-m*(z+U)/2000,
    D=1-m*(L+U)/2000.

At a fixed threshold z,

    partial_m log H_m(z)
      =1/t-(z+U)/(2000*N)+((L+U)+m/60)/(2000*D).

Here N,D>976/1000, z,U<=1, and 1/t>64/27. The final summand is positive, so

    partial_m log H_m(z)
       > 64/27-1/976 = 62437/26352 > 0.

If a moving lower endpoint crosses z, the continuous upper-tail becomes 1, preserving this order. The normalized continuous distributions therefore increase in first-order stochastic order even though their likelihood-ratio kernels have the opposite TP2 sign.

## The actual clipped top atom also increases

The original clipping geometry gives

    b_c(m)=(47-m)/54,
    x(m)=(740-m)/945,
    B(m)=(1/54)*integral_[x(m),49/64] h(a,b_c(m)) da,
    A(m)=integral_[L(m),U] K(m,z) dz.

Exact rational integration, using the same h in both regions, produces

    A(t)= t*(943170+907*t-8*t^2)/3402000000,
    B(t)= (441-64*t)*(750801415275+606886272*t-462848*t^2)
          /2496508125511680000.

A(t), B(t)>0 for 0<t<27/64. A direct exact derivative gives

    B'(t)*A(t)-B(t)*A'(t)
       = -P(t)/4246560321495367680000000000,

    P(t)=156143408271305245875+300310805691601425*t
        -7230168422976708*t^2+354330391570944*t^3
        +142745649152*t^4.

For 0<=t<=27/64, the constant, linear, cubic and quartic terms are nonnegative. Thus

    P(t) >=156143408271305245875
          -7230168422976708*(27/64)^2
         =159889532371621484270967/1024 >0.

Therefore d(B/A)/dt<0, and because dt/dm=-1, r(m)=B(m)/A(m) is strictly increasing. The full mixed CDF for z<U is

    F_m(z)=F_m^(continuous)(z)/(1+r(m)).

Both factors are nonincreasing with m; at U each CDF is exactly 1. This proves the theorem across the whole high-gap interval, with the actual clipping atom instead of an assigned mass.

## Reproducibility, evidence scope and remaining problem

The standalone standard-library Fraction verifier EC49FTX_REVERSE_TP2_FOSD_VERIFY.py checks: polynomial mass integrals against the original h at six distinct rational t nodes (more than needed for cubic-polynomial identity); the complete exact derivative polynomial coefficients; positive global bounds; and 12 illustrative mixed-CDF comparisons. The proof over all real m in I is supplied by the explicit identities and uniform inequalities, not extrapolation from sample points. Local execution of the verifier completed successfully with exit status 0. The accompanying JSON certificate records the actual calculated values.

This answers a distinct open follow-up from EC49FTR–FTW: continuous TP2 is a powerful sufficient hypothesis, but not necessary once the upward-moving truncation boundary dominates reverse likelihood-ratio movement. The next question is the sharp epsilon-domain in the family h_epsilon=1-epsilon*M_*Z_* and the onset of conditional-order failure as epsilon grows.

**Scope:** external price-prior postprocessing; parent native Bellman evidence is AUTHOR_PROVED/NOT_REVIEWED; no new native BRC execution, CLAIM, Result, Review, Activity association, canonical main merge or physical-world inference is asserted.
