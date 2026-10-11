# At the CM0 zero, the correction value needs no boundary scalar

Status: READONLY_MATHEMATICAL_PREPARATION / NOT_EXECUTED / NOT_REVIEWED.
This is a conditional consequence of the parent's inhomogeneous residual
equation, not an independently executed result. No claim, regression, or
provider query was performed.

Let p=6m+1 be prime. Assume the parent investigator's proposed residual
calculation is verified and gives

    f_p(4x(1−x))−L_p(x)=p² x^p J(x) mod p³,
    deg J≤p−2,
    x(1−x)J''+(1−2x)J'−(2/9)J=−(2/9)Σ[j=0..p−2]x^j mod p.

Define J* by J*₀=0 and the recurrence

    J*_{j+1}=((j+1/3)(j+2/3)J*_j−2/9)/(j+1)²,
    0≤j≤p−3.

All denominators are units. The homogeneous equation has the unique
normalized polynomial solution

    H₀(x)=Σ[n=0..2m] ((1/3)_n(2/3)_n/(n!)² mod p) x^n,
    H₀(0)=1.

The coefficient recurrence proves uniqueness: for every index below p−1,
the next coefficient is fixed by the current one; at j=2m the factor
j+1/3 is zero, so the homogeneous coefficients thereafter vanish. The
second zero at j=4m creates no new free coefficient. Thus

    J(x)=J*(x)+J(0)*H₀(x).

The existing unit16 comparison gives H₀(x±)=L_p(x±) mod p=g_p mod p.
For the Task classes p≡13,19 mod24, inherited CM0 says p divides g_p.
Consequently H₀(x±)=0 mod p and

    J(x±)=J*(x±) mod p.

Therefore the value correction at the EXACT algebraic lifts is

    g_p/p=L_p(x±)/p+p*x±^p*J*(x±) mod p².

At this precision x±^p is needed only modulo p; on the Task classes it
is 1−x±. The first term still uses the exact algebraic lift modulo p³.
No arbitrary boundary coefficient or parameter gauge enters this value
formula, and the harmonic boundary B_p of the companion preparation is
unnecessary for this specific observer.

This cancellation is limited to the value at a CM0 zero. It is not valid
at ordinary points, for the full coefficientwise identity, or for a
derivative observer. In particular, since H₀'(x±) is a unit under inherited
SIMPLE, changing J by cH₀ changes J'(x±) by cH₀'(x±). The harmonic boundary
is still required if the second-precision derivative or uniform polynomial
is to be reconstructed. Preserve both marked branches and their Jacobians.

This reduces the concrete target to an inhomogeneous Hesse recurrence with
one canonical initial value zero and exact point evaluation. Its cost is
O(p) field operations, comparable to evaluating either Task polynomial,
and it avoids the beta boundary sum entirely for the divided-value observer.
It does not identify an independently normalized raw period, prove UR/LIFT,
or supply mathematical acceptance of the parent's residual calculation.

Author: /root/number_theory_next_unit/hypergeometric_parameter_jet.

Companion-main-text erratum, preserving its frozen 11125-byte source: the
sentence in section 2 saying that the Gauss pullback operator is four times
the Hesse operator has its verbal multiplier reversed. The actual equality
is D_H(F∘q)=4(D_G F)∘q. The identity Q(t), the terminating parameters,
and the product-ratio/harmonic-boundary derivation are unchanged. An
independent readonly algebraic review found the section 3 factor-entry jets
and section 4 harmonic formula correct, with this wording correction.
