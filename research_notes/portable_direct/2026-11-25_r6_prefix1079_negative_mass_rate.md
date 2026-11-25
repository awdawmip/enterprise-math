# PREFIX-1079 — Sharp rare-negative mass exponent and terminal localization

2026-11-25. AUTHOR_CONDITIONAL_ANALYTIC_PROOF / HUMAN_RECHECKABLE / NOT_REVIEWED. Existing informed line EM-DIRECT-780BBE / TASK_RESEARCH; own session metadata recovered by r6-20261125-1346-recover-own. No formal run or CLAIM; fresh owner read r6-20261125-1346-owner-read last observed RUNNING. No shared task mutation.

Frozen science unchanged: P000 V5 f42f2906d77f24085c123f3ccfe9667d41caa96d:p000_reality_foundation.json; Stage46 chart O, incoming -e1, reversal signed -5 (phase cover 5q), other weights 1, next incoming -d, both orientations of Link {O,e1} blocked without renormalization, exactly two negative steps. The full X6 paired Cell, port, phase/sign and multiplicity are retained in the inherited exact CT observer. All probability/entropy coordinates below are analytic readouts of that observer, not native spatial or time coordinates.

Parents (immutable source):
- aaa7a24becaa6c9726271daf5fcf283672834a18:research_notes/portable_direct/2026-11-25_r6_prefix1078_sharp_horizon_signed_joint_tail.md, signed joint law, (H),(R),(N), finite order observer.
- 7e8adcd9dac8e9ae5662c71aed1e2211458f12f0:research_notes/portable_direct/2026-11-25_r6_prefix1075_uniform_positive_tail.md, section 5 (last boundary and local sign), exact finite order representation.
- b47b157958692d0a62f438a3d546baa044168341:research_notes/portable_direct/2026-11-25_r6_prefix1076_uniform_beta_tail_transport.md, uniform positive beta tail (as quoted in PREFIX-1078).
The arguments below are conditional on these inherited analytic results, not independent review.

## 1. Statement

Write D_m(k)=L(x^m(1-x)^k). Let p=b_last in (0,1/9), rho=(1-p)/p. K(j)=rho*j+O(1) is the last strictly negative integer; the regular effective density g is negative in (p,p+epsilon) for some epsilon>0. The exact full observer L has finite order <=3 on [0,1] and locally equals integration against g at regular points. Let k tend to infinity through integers, m=m(k)>=0 with m=o(k), and r=r(k)>=1 with r/k -> theta>0. By the inherited beta tail the initial denominator D_m(k)>0 for large k. Define
    J_r(l)=D_(m+r)(k+s)/D_m(k), s=sum_i l_i,
    N_r=sum_l (-J_r(l))_+.
With C_r(s)=binomial(s+r-1,r-1), the exact joint grouping is
    N_r=D_m(k)^(-1) sum_(s>=0) C_r(s) (-D_(m+r)(k+s))_+.
This preserves signed mass with all ordered multiplicities; the grouping does not claim equivalence of native states.

If theta<1/rho then N_r=0 eventually. If theta>1/rho put
    T=rho*theta-1>0, U=theta+T=theta/p-1,
    I(theta)= -log(1-p)+ U*KL(theta/U || p),
    KL(v||p)=v log(v/p)+(1-v) log((1-v)/(1-p)).
Then
    lim_(k->infty) k^(-1) log N_r = -I(theta).               (LD)
In particular the previous exponential upper estimate has a matching logarithmic lower bound; N_r=exp(-k I(theta)+o(k)). The rate is strictly positive. It applies also to nonfixed initial paths m=o(k). No assertion at the critical theta=1/rho without specifying integer/offset behavior.

## 2. Proof of logarithmic rate

For t>=0 define
    H_theta(t)=(theta+t)log(theta+t)-theta log theta-t log t,
    Phi_theta(t)=theta log(theta/(theta+1+t))
                 +(1+t) log((1+t)/(theta+1+t)),
    F_theta(t)=H_theta(t)+Phi_theta(t),
with 0 log 0=0. The first is composition entropy; the second is the maximum of theta log x+(1+t)log(1-x) on [0,1], with unique saddle x_t=theta/(theta+1+t). Both expressions arise from the inherited exact signed observer; no positive mixture assumption is used.

Denominator: D_m(k)/(A0*B(m+4,k+1))->1 by the parent. The beta integral has logarithm o(k): its upper bound is 1, and for any fixed 0<d<1/2 its lower bound from [d/2,d] is (d/2)^(m+4)*(1-d)^k. First take liminf divided by k then let d decrease to zero. Thus log D_m(k)/k->0.

Support: by K(m+r)=rho*(m+r)+O(1) all negative summands have 0<=s<=K(m+r)-k, with the upper endpoint divided by k tending to T. For theta below threshold this set is empty. For theta above threshold all relevant s/k lie in a fixed compact interval. On such an interval, uniformly in s, Stirling's bound log n!=n log n-n+O(log(n+2)), including s=0, gives
    log C_r(s)=k H_theta(s/k)+o(k).
Here binomial(s+r-1,r-1) differs from binomial(s+r,r) by r/(r+s), bounded away from zero in this range.

Finite-order observer: write |L(h)| <= M sum_(j=0)^3 ||h^(j)||_infty, inherited from the finite variation derivative measures. Derivatives of x^M(1-x)^Q, M=m+r, Q=k+s, are sums of falling-factorial coefficients bounded by O(k^3) times x^(M-i)(1-x)^(Q-j), i+j<=3. M/k->theta>0, Q/k=1+s/k>=1, so for large k all exponents are positive. Their maximum over [0,1] is attained at (M-i)/(M+Q-i-j), uniformly bounded away from 0 and 1 on this compact s/k range. The logarithm of each maximum divided by k is Phi_theta(s/k)+o(1), uniformly, by continuity of the peak expression in the scaled positive exponents. Therefore
    |D_(m+r)(k+s)| <= exp(k Phi_theta(s/k)+o(k))
uniformly. Zero terms satisfy the bound too. There are O(k) possible s. Combining with the denominator and composition estimates gives limsup log N_r/k <= max_(0<=t<=T) F_theta(t).

F is strictly increasing for t>0:
    F'_theta(t)=log((theta+t)(1+t)/(t(theta+1+t)))>0,
since numerator minus denominator equals theta. Continuity at zero gives the maximum at T. Its value is
    F_theta(T)=H_theta(T)+theta log p+(1+T)log(1-p)
              =log(1-p)-U*KL(theta/U||p)=-I(theta).
This proves the sharp upper exponent without a global density or absolute summation of a singular effective density.

Lower bound: fix t<T sufficiently close to T, with t>0 and x_t in the open negative regular interval (p,p+epsilon). Set s=floor(t*k). Pick a nonnegative smooth cutoff chi supported in that interval and equal to one near x_t. The localized contribution L(chi h)=integral chi*g*h is strictly negative. Its magnitude is at least exp(k(Phi_theta(t)-epsilon1)) for every fixed epsilon1>0 and all sufficiently large k, by continuity of the phase and a sufficiently small fixed interval around x_t where g is bounded above by a negative constant. The complementary support lies away from x_t. The strict unique maximum of the phase implies a fixed gap c>0 there; the same finite-order derivative estimate, including derivatives of the fixed cutoff, bounds |L((1-chi)h)| <= exp(k(Phi_theta(t)-c/2)) for large k. For rigor choose epsilon1<c/4, then arbitrarily small. The shifted exponents used in the derivatives have the same phase uniformly on interior compact sets, while near either endpoint their peaks on the restricted region are attained at its inner boundary; hence the gap persists there as well. Consequently D_(m+r)(k+s)<0 and its magnitude has log/k->Phi_theta(t). The single s-term including its full composition multiplicity has log/k->F_theta(t). Thus liminf log N_r/k>=F_theta(t); take t upward to T. This order of limits avoids any need for a finite-scale nonzero gap at the integer closest to the sign crossing. Together the bounds prove (LD).

## 3. The dominant negative combinations localize at the last sign boundary

Let W_k(s)=C_r(s)*(-D_(m+r)(k+s))_+/(D_m(k)*N_r), a probability on terminal offsets when N_r>0. For every 0<d<T,
    limsup k^(-1) log sum_(s/k<=T-d) W_k(s)
       <= F_theta(T-d)-F_theta(T)<0.
This follows from the same compact uniform upper bound and (LD). Offsets s/k>=T+d are absent eventually by K. Hence s/k->T in W_k probability, with an exponential bound for every fixed nonzero downward displacement. Conditioned on s, ordered compositions are exactly uniform in the negative-mass law, not independently sampled. The dominant macroscopic negative observation has (k+s)/k->rho*theta and spectral saddle ->p. This does not yet determine the O(1) distance of the largest contribution from K or its polynomial prefactor.

## 4. Rate versus depth and precision

For theta>1/rho, v=theta/U belongs to (p,1). The derivative along the boundary T=rho*theta-1 is
    d F_theta(T)/d theta
       = log(p/v)+rho log((1-p)/(1-v))
       = KL(p||v)/p >0.
Thus I strictly decreases with theta. The one-sided threshold limit is
    I(1/rho+)= -log(1-p)-(1/rho) log p,
and as theta->infinity (after taking the large-k limit at each fixed theta),
    I(theta)= -log(1-p)+p^2/(2(1-p)*theta)+O(theta^(-2)).
Indeed v=p+p/U and Taylor expansion of KL around p gives U KL(v||p)=p/(2(1-p)U)+O(U^(-2)). The iterated limit is not a simultaneous unbounded-theta theorem.

The least l1 distance of J_r to any probability equals 2*N_r: negative coordinates contribute N_r, and on nonnegative coordinates the net mass removed must be N_r, so the triangle inequality gives the second N_r. The normalized positive part attains it (PREFIX-1078). Therefore this minimum distance has the exact exponential rate I(theta). A tolerance exp(-gamma*k) with gamma<I(theta) exceeds that distance eventually and cannot alone certify the sign structure; with gamma>I(theta) no probability lies in that l1 tolerance of the exact J_r eventually. The equality case remains unresolved. In bit units the separation threshold is I(theta)/log 2 per k. This is a norm-level distinguishability statement, not a universal machine mantissa requirement or a new native state quotient.

## 5. Evidence and remaining work

Analytic derivation using only the inherited exact signed BRC observation, last-boundary theorem, finite-order observer and local negative density. No new path enumeration, native kernel execution, classical pi/trigonometric evaluation, floating-point experiment or formal checker. The proof explicitly avoids differentiating singular densities or assuming global positivity. No new external reference calculation. Mother B_fix,odd(32) is open.

Next: refine the terminal localization to a bounded-distance law and determine the polynomial prefactor via the odd zero multiplicity and the integer crossing phase. Analyze critical depth r/k->1/rho including near-zero rounding; certify p numerically using the authorized BRC carrier, and preserve the other regular-band classification problems. No repetition of endpoint algebra or native enumeration.
