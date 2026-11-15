# BRC N=4 S23: uniform rational Chernoff optimizer proxy and eighth-order error certificate

Date: 2026-11-04. Status: AUTHOR_ANALYTIC_PROOF / EXACT_RATIONAL_AUDIT_EXECUTED / UNREVIEWED / NOT_ADMITTED.

## Precise scientific domain and scope

Frozen source: awdawmip/enterprise-math@43ec6098b1330ae86d0a7863be336c5d97f6ef34. This is the two-state source-tagged S23 hypothesis-testing experiment, with 0<s<=1, 0<h<=1/42, v=2h<=1/21, k=s/(2-s). The full-source trial T has respective laws (s(1/2+h),1-s,s(1/2-h)) and (s(1/2-h),1-s,s(1/2+h)). The scalar B trial observes Bernoulli success probabilities s(1/2+h), s(1/2-h). Their stipulated costs are c_T=2-s, c_B=1. Only the declared two-state, independent-sampling Chernoff task is compared; source provenance remains available in T, while B is an explicit projection.

Let C_B be the EXACTLY OPTIMIZED Bernoulli Chernoff information. At exponent t=(1+delta)/2, the B Chernoff coefficient equals

    Z(delta)=X exp(alpha delta)+Y exp(-gamma delta),

with X=(s/2)sqrt(1-v²), Y=((2-s)/2)sqrt(1-k²v²), alpha=atanh(v), gamma=atanh(kv).

Define the rational optimizer proxy delta_0=(1-k)v/6 and C_hat=-log Z(delta_0). No numeric optimization is needed to select delta_0.

## Theorem (uniform, all-real legal parameters)

For every real s in (0,1], h in (0,1/42], the unique Chernoff optimizer delta_* obeys

    delta_0(1-v²) <= delta_* <= delta_0/(1-v²)².

At s=1, delta_*=0. For 0<s<1, delta_*>0. In particular, the optimizer is interior and satisfies

    0 <= delta_* <= 3087/387200 < 1/125.

The rational proxy has the exact uniform eighth-order information-loss bound

    0 <= C_B-C_hat
       <= (1-k²)² v⁸(2-v²)²/[288(1-v²)⁶]
       <= 776161/2089818390528000000
       < 4/10¹³.

Consequently C_hat agrees with the optimized C_B through order h⁶, uniformly in s, with a quantified O(h⁸) remainder. Put

    C_T=-log(1-s+s sqrt(1-v²)),
    F=C_T/(2-s)-C_B,       F_hat=C_T/(2-s)-C_hat.

Then the entire legal parameter rectangle obeys the certified comparison

    F_hat - (1-k²)² v⁸(2-v²)²/[288(1-v²)⁶] <= F <= F_hat.

Thus F_hat<0 certifies the scalar observation B has larger Chernoff information per cost. F_hat exceeding the explicit rational error certifies the full-source observation T has larger Chernoff information per cost. These sign tests concern the actual optimized Chernoff information.

## Proof

**1. Exact optimizer.** For 0<s<1 and h>0 all X,Y,alpha,gamma are positive, and Z is strictly convex. The stationary equation

    X alpha exp(alpha delta_*) = Y gamma exp(-gamma delta_*)

has the unique unconstrained solution

    delta_* = log(Y gamma/(X alpha))/(alpha+gamma).

Introduce g(x)=sqrt(1-x²)atanh(x)/x with continuous g(0)=1, and phi(x)=log g(x). Because k=s/(2-s),

    Y gamma/(X alpha)=g(kv)/g(v),

so delta_*=[phi(kv)-phi(v)]/[atanh(v)+atanh(kv)]. The s=1 case follows by symmetry and yields delta_*=0. The s=0 endpoint is excluded: B then carries no information and has nonunique optimizer.

**2. Elementary uniform bounds.** Exact differentiation gives

    -phi'(x) = [atanh(x)-x]/[x(1-x²)atanh(x)].

For real 0<x<1, the positive atanh power series implies

    x³/3 <= atanh(x)-x <= x³/[3(1-x²)],
    x <= atanh(x) <= x/(1-x²).

Hence x/3 <= -phi'(x) <= x/[3(1-x²)²]. Integrate from kv to v to obtain

    (1-k²)v²/6 <= phi(kv)-phi(v)
                 <= (1-k²)v²/[6(1-v²)²].

Similarly,

    (1+k)v <= atanh(v)+atanh(kv) <= (1+k)v/(1-v²).

Dividing proves the displayed delta_* enclosure. Since v<=1/21, its upper endpoint is <=v/[6(1-v²)²]<=3087/387200<1/125, validating the unconstrained stationary point as the true Chernoff minimizer with t=(1+delta_*)/2 in [0,1].

**3. Exact curvature and rational error.** Let L(delta)=log Z(delta) and w(delta)=X exp(alpha delta)/Z(delta). Then

    L''(delta)=w(delta)(1-w(delta))(alpha+gamma)²
              <=(alpha+gamma)²/4.

Because L'(delta_*)=0, Taylor's integral remainder gives

    0<=L(delta_0)-L(delta_*)<=(alpha+gamma)²(delta_0-delta_*)²/8.

The optimizer enclosure gives

    |delta_0-delta_*| <= delta_0[(1-v²)^(-2)-1],

and alpha+gamma <= (1+k)v/(1-v²). Substitute delta_0=(1-k)v/6:

    L(delta_0)-L(delta_*)
        <= (1-k²)² v⁸(2-v²)²/[288(1-v²)⁶].

By C_B=-L(delta_*) and C_hat=-L(delta_0), this is the information-error bound.

**4. Uniform constant and cost sign.** For x=v² in (0,1), x⁴(2-x)²/(288(1-x)⁶) is increasing since its logarithmic derivative is 4/x-2/(2-x)+6/(1-x)>0. The maximum on v<=1/21 is exactly 776161/2089818390528000000 < 4/10¹³, by integer rational arithmetic. Since F=F_hat-(C_B-C_hat), the claimed cost-efficiency enclosure follows. QED.

## Evidence and use

VERIFY.py performs a Python standard-library fractions.Fraction interval audit of 24 rational (v,k) pairs using explicit positive atanh series, alternating log(1+x) series, negative log(1-x) series, and proven tail bounds; it also checks the exact global constants. The analytic argument establishes the theorem over all real admissible s,h, while the 24-point program audits implementations and representative exact cases. Independent mathematical review and native Result admission remain pending.

Scientific next step: use F_hat and its explicit rational error to certify signs in full s bands for h=1/42, separately treating s near 0 via a normalized endpoint series and s near 1 via the (1-k²)² factor. The full-s crossing uniqueness question remains open at this finite h. The original unrestricted ten-label minimax remains in [1/2,2/3].
