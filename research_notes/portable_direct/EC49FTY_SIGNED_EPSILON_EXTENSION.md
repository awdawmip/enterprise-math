# EC49FTY signed-parameter extension: the complete real epsilon interval

Date 2026-11-19. AUTHOR_PROVED / EXACT_RATIONAL_VERIFIED / PARENT_DEPENDENT / NOT_REVIEWED. Extends EC49FTY_SHARP_EPSILON_THEOREM.md; same frozen BRC16943 native input and inherited external price-chart postprocessing.

For the SAME price rectangle R=[3/4,49/64] x [7/16,57/128] and the SAME joint prior
    h_epsilon(a,b)=1-epsilon*M_*(a,b)*Z_*(a,b)
with M_*=525a/8-231b/4-9/8, Z_*=35a/32-b/16-5/96, we establish the following COMPLETE REAL parameter theorem:

The joint density is globally nonnegative on R if and only if
    -infinity < epsilon <= 1048576/18958647.
For EVERY such finite real epsilon, the actual clipped optimum Law(Z|M=m) is first-order stochastically increasing for all 1469/64<m<187/8. The strictly positive-on-the-closed-box range is the same with the right endpoint excluded.

The primary EC49FTY theorem has already proved the nonnegative-epsilon portion 0<=epsilon<=epsilon_max, including the complete positivity cutoff. It remains to prove the unrestricted negative half-line.

## Negative-epsilon continuous component

For epsilon<0, h_epsilon=1+abs(epsilon)*M_*Z_*>0 everywhere on R because both affine forms are positive. Each fixed such epsilon yields a finite positive normalizing constant on the compact box.

On the inherited continuous (m,z) fiber,
    K_epsilon(m,z)=(16/945)*(1-epsilon*m*z).
Its exact mixed log derivative is
    partial_m partial_z log K=-epsilon/(1-epsilon*m*z)^2>0
for ALL epsilon<0. Hence K is strictly TP2 and gives monotone likelihood ratio in z as m increases.

The allowed fiber support [L(m),3/4] has a nondecreasing lower endpoint L(m)=(8m+173)/480. Given m<m', first truncate the earlier distribution to [L(m'),U] (removing its lower segment, a stochastic right shift). On the shared remaining support, tilt by the increasing positive likelihood ratio K(m',z)/K(m,z), another stochastic right shift. This proves normalized continuous-component FOSD for EVERY negative epsilon, without a small-parameter bound.

## Negative-epsilon clipped-atom ratio

Reuse the EXACT atom/continuous mass polynomials A(t,u), B(t,u), and
    (B_t*A-B*A_t)=-P(t,u)/4246560321495367680000000000
from the parent EC49FTY theorem. This identity is algebraic and valid for all real u=1000epsilon, not just positive u.

Write P(t,u)=C+u*L1(t)+u^2*Q(t), with C=161810711838720000000 and
    L1(t)=-5717812295230560000+305754824245248000*t
          -7490036957184000*t^2+362941513728000*t^3,
    Q(t)=50508727815805875-5444018553646575*t
         +259868534207292*t^2-8611122157056*t^3+142745649152*t^4.
For 0<=t<=27/64=T, exact term bounds give
    L1(t) <= -5717812295230560000
             +305754824245248000*T+362941513728000*T^3
           = -5588794727402400000 <0,
    Q(t) >= 50508727815805875
            -5444018553646575*T-8611122157056*T^3
          = 24684229593641242071/512>0.
Therefore for EVERY u<0,
    P(t,u)=C+u*L1(t)+u^2*Q(t) >= C >0.
Since A and B are positive masses from the same positive h, B/A decreases with t and hence INCREASES with m. Thus the clipped top-atom probability increases in m throughout the negative-epsilon half-line.

## Full mixed-law conclusion and limits

For z<U, the conditional CDF is
    F_m(z)=F_m^continuous(z)/(1+B(m)/A(m)).
Both numerator monotonicity and denominator increase have now been proved; for z>=U the CDF is identically 1. Hence full FOSD holds for every epsilon<0. The primary theorem establishes it for all 0<=epsilon<=epsilon_max. Beyond epsilon_max the function changes sign on an open subset and is not an admissible probability density. This proves the exact complete real parameter domain and FOSD there.

Independent exact-Fraction sign-bound verifier: EC49FTY_SIGNED_EPSILON_VERIFY.py, certificate EC49FTY_SIGNED_EPSILON_CERT.json. Analytic TP2 plus truncation supplies continuous order over all negative real epsilon; exact rational bounds supply the atom-ratio monotonicity. All-real conclusion depends on inherited native Bellman author geometry; NOT_REVIEWED; no new native BRC, CLAIM, Result or Review.

Next: map original Bellman lower-gap transition branches; do not extrapolate high-gap formulas. Also investigate changed nonnegative priors beyond epsilon_max by genuinely changing the density family/domain, rather than interpreting a sign-changing function as probability.