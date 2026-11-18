# S23 n=3: exact A-event minimax-feasible interval on the sharp 22-dimensional face

2026-11-07; author-side exact conditional theorem, independent review pending.
Frozen science: enterprise-math@43ec6098b1330ae86d0a7863be336c5d97f6ef34.
Previous frontier: sharp-face theorem PR #1777@a37728ad9336b039dd1ee50163dddcfff7e86d9d and three-class exact theorem @87f4ba417ba88cc440e52206254c47fd1b443f71.

## Statement

Let a,c range over *all real numbers* in [1/2,7/8], z=(1-a)c, and the three ordered outputs share the same hidden (a,c), with target law Q=(a,z,(1-a)(1-c))^⊗3. The compressed input law is Bernoulli(z)^⊗3. Let A be the event that at least one of the three output labels is 2, with true probability F(a,c)=1-(a+z)^3. Set d=5211/21952.

On the **necessary sharp face** from the predecessor (assuming a full-27-output kernel has uniform TV error ≤d, after symmetrization), the histogram kernel has deterministic 111 column (1,0,0,0), and the A-event row masses for input k=0,1,2,3 are
(0,u,v,t), where u=3t-919/12348 and v=30839/37044-2t.

**Exact interval theorem.** On this face, the row-mass nonnegativity requirements and the all-real event-A inequality |Pr_K(A;z)-F(a,c)|≤d hold together **if and only if**
    
    919/37044 ≤ t ≤ 345827/1407672.

This strengthens the old elementary row-stochastic upper t≤13267/37044 to 345827/1407672. Every t in the exact interval admits a row-stochastic 4×3 A/B/C decoder with the declared margins. All such decoders have exactly d worst-case three-class total variation loss. This theorem concerns the A-event projection of the full 27-output problem; full histogram compatibility remains the next question.

## Proof

1. For z fixed, the lawful a interval is [max(1/2,1-2z), min(7/8,1-8z/7)]; z ranges over [1/16,7/16]. Because F=1-(a+z)^3 decreases in a, let H(z)=max F and L(z)=min F. Exact formulas:

   H=1-(1-z)^3 for 1/16≤z≤1/4;
   H=1-(1/2+z)^3 for 1/4≤z≤7/16;
   L=1-(7/8+z)^3 for 1/16≤z≤7/64;
   L=1-(1-z/7)^3 for 7/64≤z≤7/16.

   The desired bound for all parameters is thus equivalent to H(z)-d≤g_t(z)≤L(z)+d for all feasible z, where g_t(z)=sum_{k=1}^3 binom(3,k)z^(3-k)(1-z)^k times the corresponding A row mass.

2. With t0=919/37044 and t1=345827/1407672, two exact polynomial identities hold for every real z:

   g_t0(z)=(1-z)^2 (86084z+919)/37044;
   g_t(z)=g_t0(z)+(t-t0)(1-z)(4z-1)^2.

   Nonnegative u=3t-919/12348 forces t≥t0. At t0 the A row masses are (0,0,1381/1764,t0). At t1 they are (0,705/1064,5717/16758,t1). Since all three row probabilities are affine in t, every t∈[t0,t1] gives valid A masses and valid complementary B masses, while C has mass 1 only in row0.

3. For the lawful corner a=c=7/8, z*=7/64 and F=L(z*), a *polynomial identity* gives

   g_t(z*)-L(z*)-d = 9(1407672t-345827)/44957696.

   Therefore the bound at this single corner forces t≤t1, proving necessity.

4. Sufficiency holds on the entire continuous parameter box. Because z≤7/16<1, the factor (1-z)(4z-1)^2 is nonnegative; hence g_t0(z)≤g_t(z)≤g_t1(z) throughout the exact interval. Thus it suffices to prove H-g_t0≤d and g_t1-L≤d. The following are global polynomial identities, and each displayed right side is nonnegative on the specified z interval:

   - d-H+g_t0 = (4z-1)(196160z²-191428z-155401)/592704, z∈[1/16,1/4]. Both factors are nonpositive.
   - d-H+g_t0 = (4z-1)(492512z²-339604z+363215)/592704, z∈[1/4,7/16]. First factor is nonnegative; second is ≥363215-339604(7/16)>0.
   - d-g_t1+L = (64z-7)(295616z²-4617064z-4141441)/90091008, z∈[1/16,7/64]. Both factors are nonpositive.
   - d-g_t1+L = 13339(4z-1)²(64z-7)/11261376, z∈[7/64,7/16]. All factors are nonnegative.

   These inequalities cover the full feasible z range, proving the uniform A-event loss bound. At z0=1/4, all g_t coincide at 935/2744; the two lawful endpoint targets differ from this value by ±d. Hence the maximal loss is exactly d for each t in the interval.

## Exact verification and scope

The companion VERIFY.py uses only the Python standard-library Fraction type and checks all six degree≤3 polynomial identities at four distinct rational nodes each (therefore verifies the identities over the real polynomial ring), row probabilities, endpoint saturation, and 867 rational regression examples. The sign arguments above are the all-real proof; grid checks are additional diagnostics. The actual stdout is in RUN_EVIDENCE.txt.

The BRC interface here is explicitly the finite positive-mass input branches, three shared-parameter observation steps, and event A's exact marginal. The reduction discards other histogram events only under the declared A observer; no transfer is inferred to native Heartbeat-X6, preserved path provenance, or the six-source ten-label S23 mother model. P000, the ACTIVE worldview, and immutable scientific source remain unchanged.

## Next question

On the exact interval t∈[919/37044,345827/1407672], solve full 10-histogram/27-ordered TV inequalities across at least two distinct z fibers using exact rational LP or a full continuous Bernstein certificate. Start with t=t0, where u=0. Establish either a feasible full-output kernel with a valid all-real proof at d or a finite rational dual contradiction that applies to all candidate kernels. Formal owner/CLAIM and independent review require their separate live authority.
