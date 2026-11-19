# EC49FTN — Exponential-price-prior robustness of the BRC16943 optimizer/gap stochastic order

Date: 2026-11-19. Research mode: independent portable follow-up; AUTHOR_PROVED / AUTHOR_NUMERIC_CHECKED / PARENT_DEPENDENT / NOT_REVIEWED.
Scientific source is frozen at awdawmip/enterprise-math@fc0f038e7bfd12c886b4d37f900bfb770c0f61ab. Native original-index Bellman theorem is inherited from EC49FTH PR #2774 (head 999bf1069403306b3813e0e390dae4435d7b4b8c); optimized-price and mixed joint/conditional laws from EC49FTK PR #2776, EC49FTL PR #2779 and EC49FTM PR #2783 (head 559f337d296368c3eebd12d8fc9cc471cd6aa20a). No native Bellman rerun or independent review is asserted.

## Typed model and exact parent premise

The 310 original configurations, 141 separately named response profiles and 228 original physical observations stay fixed. The randomness below belongs only to the externally chosen price parameters, not to those native BRC profiles.

On A=[3/4,49/64], B=[7/16,57/128], allowed q140 discount z in [11/16,3/4], the parent exact affine Bellman expressions imply

D=min(329-36a-68b-141z, 334-141a-62b-45z, 326-141a-47b-43z);
S=332-141a-8b-105z;
Z=z_*=min(3/4,(105a-6b-5)/96);
M=max_z(D-S)=(525a-462b-9)/8 if a<a_c(b), and M=47-54b otherwise;
a_c(b)=(77+6b)/105.

Assume a and b are independently distributed with strictly positive normalized densities proportional to exp(lambda*a) on A and exp(mu*b) on B, for arbitrary real lambda,mu. Let

Phi(t;x,y)=integral_x^y exp(t*u) du,  F_t(s)=integral_0^s exp(t*u) du.
In particular F_0(s)=s, and F_t(s)=expm1(t*s)/t when t is nonzero.
The normalizing constant is C=[Phi(lambda;3/4,49/64)*Phi(mu;7/16,57/128)]^(-1).

Set m0=11457/512, m1=1461/64, m2=1469/64, m3=187/8.
Define

A(m)=(4m+2647)/3696, B0(m)=(8m+173)/480, B1(m)=(64m+1411)/3840.

At almost every m in (m0,m3) the continuous conditional Z-support [L(m),U(m)] is:

m0<m<m1: [A(m),B1(m)];
m1<m<m2: [B0(m),B1(m)];
m2<m<m3: [B0(m),3/4].

These intervals and breakpoints depend only on the parent price rectangle, not on lambda or mu. On m>m2 the law also has an atom at Z=3/4. Endpoint versions may be chosen by one-sided limits.

## Theorem 1 — complete nonuniform mixed joint law

Put kappa=(44/45)*lambda+(10/9)*mu, b_*(m)=(47-m)/54,
a_*(m)=(740-m)/945=a_c(b_*(m)), J=945/16.

On the above continuous-support region, the joint (M,Z) density is

f_cont(m,z) = (16*C/945)*exp(lambda*((47-m)/945+(44/45)*z)
                            +mu*(1/27-m/54+(10/9)*z)).

On m2<m<m3 there is also line density at z=3/4 equal to

g(m) = (C/54)*exp(mu*b_*(m))*integral_[a_*(m),49/64] exp(lambda*a) da.

For every bounded measurable test function phi, its expectation equals the integral of phi against the displayed two-dimensional density plus the integral of phi(m,3/4)*g(m) dm.

Proof: in the un-clipped component, invert the parent affine map:
a=(47-m)/945+(44/45)z and b=1/27-m/54+(10/9)z.
Its absolute Jacobian is 945/16, so the change-of-variables formula gives f_cont. In the clipped component, m=47-54b while a ranges from a_c(b) to 49/64, giving g by one-dimensional integration and |db/dm|=1/54. This exactly partitions the original price rectangle up to zero-measure boundaries.

## Theorem 2 — conditional exponential family and strict atom monotonicity

For m in (m0,m2), conditional Z given M=m has density proportional to exp(kappa*z) on [L(m),U(m)].

For m in (m2,m3), its continuous component is a truncated exp(kappa*z) law on [B0(m),3/4], with continuous mixture weight 1-p(m) and a point atom of weight p(m) at 3/4, where

d(m)=49/64 - (740-m)/945, T(m)=3/4 - (8m+173)/480,

p(m)=35*F_lambda(d(m)) / [35*F_lambda(d(m))+32*F_{-kappa}(T(m))].

Here F_t(s)>0 for s>0. Since d'(m)=1/945>0 and T'(m)=-1/60<0, the numerator's F_lambda(d) strictly increases and the second term F_{-kappa}(T) strictly decreases; hence p(m) strictly increases through (m2,m3), and p(m)->1 as m->m3.

For any conditional quantile level u in (0,1), define Q_m(u) by
Q_m(u)=U(m) when u>=1-p(m), and otherwise
Q_m(u)=L(m)+F_kappa^{-1}([u/(1-p(m))]*F_kappa(U(m)-L(m))).
Set p=0 in the lower two segments. The inverse is log(1+kappa*y)/kappa if kappa!=0 and y if kappa=0.

**First-order stochastic-order theorem (every real lambda,mu):**
For all interior m<m', the conditional Z|M=m' first-order stochastically dominates Z|M=m, with the natural one-sided choice at the breakpoints.

Proof: all three intervals have nondecreasing lower and upper endpoints (check the displayed positive slopes), and the unnormalized continuous conditional density exp(kappa*z) is identical for every m. For any positive fixed base density, conditioning to an interval with both endpoints increasing yields a first-order stochastically larger distribution, by deleting left mass and/or adding right mass. At m1 the intervals join continuously. At m2 the conditional interval joins at [B0(m2),3/4] while a strictly positive atom appears at its rightmost point, producing an upward stochastic jump. Above m2, L increases, U=3/4 is fixed and p strictly increases; both changes independently shift the law right. This proves the quantile inequality at all ordered interior levels; the zero-measure breakpoint versions do not affect the regular conditional law.

The noteworthy subfamily mu=-22*lambda/25 has kappa=0: even though the external a,b prior is nonuniform unless lambda=0, the entire continuous conditional Z law remains uniform on its moving support, while clipping weights change.

At lambda=mu=0, the exact parent conditional law is recovered, including p(m2+)=115/223.

## Theorem 3 — global clipping probability and signed prior sensitivity

Define the clipping probability P_clip(lambda,mu)=Pr(Z=3/4). For lambda!=0,

P_clip = [exp(lambda*49/64)*Phi(mu;7/16,57/128)
          -exp(77*lambda/105)*Phi(mu+2*lambda/35;7/16,57/128)]
         / [lambda*Phi(lambda;3/4,49/64)*Phi(mu;7/16,57/128)].

The formula extends continuously to lambda=0 by its defining integral. In particular,
P_clip(0,0)=19/42. For every finite real lambda,mu,

partial_lambda P_clip > 0 and partial_mu P_clip < 0.

Proof: for fixed b, the clipping event is the strictly interior threshold
a>=a_c(b). Exponential tilting in a strictly increases the probability of every such upper tail, so the b-mixture strictly increases with lambda. For fixed lambda, its tail probability q_lambda(b)=Pr_lambda(a>=a_c(b)) is strictly decreasing in b because a_c'(b)=2/35>0. Exponential tilting b upward makes the expectation of that decreasing nonconstant q strictly decrease with mu (or use the strict negative covariance with b). The formula follows by integrating exp(mu*b) times the a-tail over b. No native response-profile probabilities enter this measure.

## Scope, validation and next frontier

The three theorems are universal analytic deductions *given* the cited affine Bellman parent, for all real lambda,mu and almost all m in the specified support. The attached standard-library Python checker evaluates rational breakpoints and two exact uniform endpoints, compares the clipping integral against an independent Simpson quadrature for seven exponential tilts, and tests 67,200 conditional quantiles plus 693 upper-region atom comparisons. Those finite regression tests are not used as the universal proof; numerical integration is double-precision, not a rigorous enclosure.

Frozen-science scope, provenance, q140 observer identity, P000 assumptions and original BRC strategy trees are unchanged. The parent native optimality remains AUTHOR_PROVED/NOT_REVIEWED. No formal Task publication, CLAIM, Result, Review or Activity update is represented by this paper.

Next: characterize the maximal class of non-exponential independent price priors preserving this monotone conditional law, or construct an exact smooth counterexample; separately study the native Bellman switching region below z=11/16 without repinning frozen data.
