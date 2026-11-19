# EC49FTX addendum — a whole interval of strictly reverse-TP2 priors with full mixed FOSD

Date: 2026-11-19. Extends [EC49FTX original theorem](EC49FTX_REVERSE_TP2_FOSD_THEOREM.md); same frozen native BRC16943 input, external price-prior model and inherited optimizer. Status **AUTHOR_PROVED / EXACT_FRACTION_VERIFIED / PARENT_DEPENDENT / NOT_REVIEWED**.

**Strengthened theorem.** For every real epsilon in [0,1/1000], let

    h_epsilon(a,b)=1-epsilon*M_*(a,b)*Z_*(a,b)

on the original price rectangle, where the affine M_* and Z_* are exactly those in the parent EC49FTX note. Then for all m<m' in I=(1469/64,187/8),

    Law(Z | M=m) <=_st Law(Z | M=m').

For every epsilon>0 in this interval, the continuous kernel is **strictly reverse-TP2**, not TP2. At epsilon=0 it has TP2 equality.

**Proof.** Let t=187/8-m in (0,T), T=27/64, and set u=1000*epsilon in [0,1]. The common prior is positive on the entire price rectangle because 0<M_*<24, 0<Z_*<1 and epsilon<=1/1000.

The continuous kernel is K=(16/945)*(1-epsilon*m*z), and partial_m partial_z log K=-epsilon/(1-epsilon*m*z)^2<0 for epsilon>0. The moving-boundary continuous upper-tail derivation in the parent note is uniform in epsilon∈[0,1/1000]: its m-log-derivative is >64/27-1/976=62437/26352>0. Thus the normalized continuous component shifts stochastically right for every parameter in the interval.

Exactly integrating the original price density over the continuous and clipped fibers gives, respectively,

    A(t,u)=t*(960000-16830*u+907*t*u-8*t^2*u)/3402000000,

    B(t,u)=(441-64*t)*
       (764411904000-13610488725*u+606886272*t*u-462848*t^2*u)
       /2496508125511680000.

Both are positive (integrals of a strictly positive density over nonempty fibers). Differentiation with respect to t yields

    B_t*A-B*A_t = -P(t,u)/4246560321495367680000000000,

where the entire bivariate polynomial is

    P(t,u)=161810711838720000000
       -5717812295230560000*u
       +50508727815805875*u^2
       +305754824245248000*t*u
       -5444018553646575*t*u^2
       -7490036957184000*t^2*u
       +259868534207292*t^2*u^2
       +362941513728000*t^3*u
       -8611122157056*t^3*u^2
       +142745649152*t^4*u^2.

For t∈[0,27/64] and u∈[0,1], **every unlisted coefficient after the four negative monomials is positive**. Bound all four negative monomials at their maximal absolute value to obtain the exact uniform inequality

    P(t,u) >= 161810711838720000000
       -5717812295230560000
       -5444018553646575*T
       -7490036957184000*T^2
       -8611122157056*T^3
       = 79917705797600818522071/512 > 0.

Thus (B/A)_t<0 and (B/A)_m>0 throughout I for the entire epsilon interval. The full clipped conditional CDF below U is the continuous CDF divided by 1+B/A; both factors are nonincreasing in m. This proves the strengthened theorem for all parameter values without any grid extrapolation.

The separate standard-library Fraction checker EC49FTX_EPS_INTERVAL_VERIFY.py recomputes the entire bivariate derivative identity from two input mass polynomials and verifies the exact lower bound. An equivalent local run exited successfully (0). The native Bellman parent remains author-proved, NOT_REVIEWED; no new native BRC runtime operation, Activity checkpoint, CLAIM, Result, Review or main merge is asserted.

**Next:** determine the sharp upper epsilon threshold for this particular global polynomial family, including whether failure first occurs through reversed continuous tails, falling clipped-atom ratio, or loss of density positivity.