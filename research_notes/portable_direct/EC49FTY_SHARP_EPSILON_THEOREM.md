# EC49FTY: The exact sharp admissible epsilon interval for the reverse-TP2 price prior

Date: 2026-11-19. Evidence: AUTHOR_PROVED / EXACT_RATIONAL_VERIFIED / PARENT_DEPENDENT / NOT_REVIEWED.

## Scientific origin and scope

Frozen native scientific input: awdawmip/enterprise-math@fc0f038e7bfd12c886b4d37f900bfb770c0f61ab.
Native Bellman optimizer: author-proved EC49FTH PR #2774 @999bf1069403306b3813e0e390dae4435d7b4b8c.
Immediate external price-prior parent: EC49FTX PR #2809 @da282b9f72ee11a8cd05fb6a98d2c8917d736975.
No new BRC run, native X6/P000 modification, formal CLAIM, Result or Review is asserted. This is exact **external price-probability postprocessing** of the frozen author geometry.

## Main theorem

On the ORIGINAL external price rectangle
    R=[3/4,49/64] x [7/16,57/128],
set
    M_*(a,b)=525*a/8 -231*b/4 -9/8,
    Z_*(a,b)=35*a/32 -b/16 -5/96,
    h_epsilon(a,b)=1-epsilon*M_*(a,b)*Z_*(a,b), epsilon>=0.
M_*, Z_* are the inherited affine chart forms. On the clipped stratum the actual optimized Z remains 3/4, NOT Z_*.

Put E=1048576/18958647=0.05530858821307238... . The exact complete parameter range for globally NONNEGATIVE h_epsilon is 0<=epsilon<=E, with strict positivity throughout the CLOSED box precisely for 0<=epsilon<E.

For EVERY 0<=epsilon<=E and ALL 1469/64 < m < m' < 187/8, the actual clipped optimizer obeys
    Law(Z | M=m) <=_st Law(Z | M=m').
At epsilon=E the density has one zero corner yet defines a valid probability law; for epsilon>E the function is negative on a positive-area subset of R, hence is not an admissible joint density. Thus within this concrete globally valid polynomial prior family, loss of prior positivity occurs before any continuous-tail or clipped-atom stochastic-order failure. This resolves the sharp nonnegative-epsilon follow-up from EC49FTX.

## Proof 1. Sharp global positivity

M_*, Z_* are positive on R and each strictly increases in a, decreases in b. Thus their positive product uniquely maximizes at (a,b)=(49/64,7/16). Exact substitution gives
    max M_* =12213/512,
    max Z_* =4657/6144,
    max M_* Z_* =18958647/1048576.
For epsilon<E, h_epsilon>0 everywhere. At E, its only zero is the maximizing corner. Above E, continuity makes a negative region with nonzero area. This proves the first statement.

## Proof 2. The continuous conditional distribution increases over the ENTIRE admissible range

Write
    m=187/8-t,  0<t<T=27/64,
    U=3/4,  L(m)=U-t/60,
    K_epsilon(m,z)=(16/945)*(1-epsilon*m*z),  L(m)<z<U.
For a fixed z=U-w, 0<w<t/60, the normalized continuous conditional upper tail equals
    H_m(z)=(60w/t)*N/D,
    N=1-epsilon*m*(U-w/2),
    D=1-epsilon*m*(U-t/120).
At fixed w and hence fixed threshold z, dt/dm=-1. Exact differentiation gives
    d_m log H_m(z)
      =1/t + epsilon*[ (m/120)*N - (t/120-w/2) ]/(N*D).
The following GLOBAL rational bounds hold for every epsilon<=E:
    N >= 1-E*(187/8)*(3/4)=191933/6319549>0,
    m*N-t >= (1469/64)*(191933/6319549)-27/64
          =55660877/202225568>0.
Also D>0 since D>=N where w<t/60. Therefore the log derivative is STRICTLY POSITIVE. When m grows and L(m) crosses the fixed z, H_m(z) becomes 1 and remains 1. Hence the normalized continuous fiber is stochastically increasing even though the continuous K is strictly reverse-TP2 when epsilon>0.

## Proof 3. Clipped-atom ratio rises across the entire epsilon interval

Define u=1000*epsilon, u_max=1048576000/18958647. Exact integration of the SAME h over the inherited continuous fiber and actual clipped slice (not an assigned atom) gives
    A(t,u)=t*(960000-16830u+907tu-8t^2u)/3402000000,
    B(t,u)=(441-64t)*(764411904000-13610488725u
       +606886272tu-462848t^2u)/2496508125511680000.
For t in (0,T), A and B are positive fiber masses.

Their exact rational polynomial derivative identity is
    (dB/dt)*A-B*(dA/dt)=-P(t,u)/4246560321495367680000000000,
where
    P(t,u)=161810711838720000000
      -5717812295230560000u+50508727815805875u^2
      +305754824245248000tu-5444018553646575tu^2
      -7490036957184000t^2u+259868534207292t^2u^2
      +362941513728000t^3u-8611122157056t^3u^2
      +142745649152t^4u^2.

We establish P>0 EXACTLY, not by mesh evaluation. Differentiate:
    P_t=u*(a(t)+u*b(t)),
    a(t)=305754824245248000-14980073914368000t+1088824541184000t^2,
    b(t)=-5444018553646575+519737068414584t
         -25833366471168t^2+570982596608t^3.
For 0<=t<=27/64,
    b(t) <= b(0)+519737068414584*T+570982596608*T^3
         =-41797692846880281/8<0,
    b'(t) >= 519737068414584-51666732942336*T
          =497940165454536>0,
    a'(t)>=-14980073914368000.
As b<0 and 0<=u<=u_max,
    a(t)+u*b(t) >= a(t)+u_max*b(t).
The last expression has derivative >=
    79375391185081466880000/6319549>0,
and its value at t=0 is
    29410194168062410752000/6319549>0.
Thus P_t>=0 and P(t,u)>=P(0,u).

The quadratic P(0,u) decreases on [0,u_max], as its u derivative is increasing and at u_max is
    -825835120387682761440000/6319549<0.
Therefore, uniformly for the WHOLE rectangle,
    P(t,u)>=P(0,u_max)
        =2987318260952797009674240000000/39936699563401>0.

It follows that d_t(B/A)<0 and d_m(B/A)>0. The actual optimized top atom has strictly increasing weight.

## Proof 4. Full mixed stochastic order

Below U, the mixed conditional CDF factors exactly as
    F_m(z)=F_m^continuous(z)/(1+B(m)/A(m)).
Proof 2 makes the numerator nonincreasing in m; Proof 3 makes the denominator increasing. For z>=U the CDF is 1. Hence F_m(z)>=F_m'(z) for all m<m' and all z, as claimed.

## Verification and limits

Standalone standard-library Fraction verifier EC49FTY_SHARP_EPSILON_VERIFY.py checks corner rational products, the independently specified original fiber integrals, the entire two-variable derivative polynomial by coefficient equality, every exact rational lower/upper bound, and diagnostic endpoint nodes. Machine output is EC49FTY_SHARP_EPSILON_CERT.json. All real parameter claims follow from the displayed inequalities, not from finite-grid inference.

Native 228-observer Bellman optimality is inherited AUTHOR_PROVED/NOT_REVIEWED. This result has not had an independent reviewer and no new native operation was performed.

Next: examine epsilon<0 as a genuinely different prior family; and determine whether the mixed order extends across inherited lower Bellman phase boundaries, which demands reading and preserving those precise native branch transitions.