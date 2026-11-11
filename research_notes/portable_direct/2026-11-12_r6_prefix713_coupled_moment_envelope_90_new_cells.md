# PREFIX-713-R6: Coupled Gamma-clock moment certificate; 90 extra exact exclusion cells

Date: 2026-11-12 (Asia/Shanghai)
Frozen science: awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d.
Scope: PREFIX-675 external auxiliary BRC two-parameter observer; predecessor PREFIX-712.
Evidence: AUTHOR_DERIVED / EXACT_FRACTION_WITNESSES / UNREVIEWED / NOT_ADMITTED.

## Exact model and inherited results

For the frozen 189-layer stopping count N_p, T_p | N_p=k follows Gamma(k,1); the two independent completed streams give Y(p,z)=max(T_p,T_z). Let s_n(p)=Pr(N_p>n), n=0..188, and c_nm=binom(n+m,n)/2^(n+m+1). The correct Gamma-clock moments from PREFIX-710 are:

mu(p,z) = sum_n s_n(p)+sum_m s_m(z)-sum_nm c_nm s_n(p)s_m(z)
M2(p,z)=2sum_n(n+1)s_n(p)+2sum_m(m+1)s_m(z)
        -sum_nm (n+m+1)c_nm s_n(p)s_m(z).

PREFIX-705 supplies coordinatewise monotonicity of the survivor tails. Put W=M2-mu^2, F_t=W-t mu, t=1/q. PREFIX-712 already certified F_t(e)>F_t(x) on 137168 of 147456 fine grid cells for all t in [0,1/2], with e=(0,3/20).

## New exact cell envelope: theorem 713.1

Define positive rational influence coefficients for n=0..188:

I_n(v)=1-sum_m c_nm s_m(v),
J_n(v)=2(n+1)-sum_m (n+m+1)c_nm s_m(v).

These arise by integrating the Gamma survivor increment against the CDF of the other completed clock, with weights 1 and 2u. Because that CDF is positive for u>0, I_n,J_n>0. Both coefficients are nonincreasing in v due to the survivor-tail order.

Let a=(p0,z0), h=(p1,z1) be the lower-left and upper-right endpoints of any closed rectangle in D=[0,1/2]^2. Define

C_pz=max(max_n J_n(z0)/I_n(z0), max_n J_n(p0)/I_n(p1)),
C_zp=max(max_n J_n(p0)/I_n(p0), max_n J_n(z0)/I_n(z1)),
C=min(C_pz,C_zp),
delta=mu(h)-mu(a), B=M2(h)-M2(a).

Then for every x in [a,h], with d=mu(x)-mu(a),

0<=d<=delta,
0<=M2(x)-M2(a)<=min(B,C*d).

Proof: Increase p first, then z. Each increment is a nonnegative sum of survivor-tail differences times I_n or J_n. For the first leg, Delta M2/Delta mu is bounded by max J_n(z0)/I_n(z0). For the second leg, p belongs to [p0,p1]; monotonicity gives J_n(p)<=J_n(p0), I_n(p)>=I_n(p1), hence bound max J_n(p0)/I_n(p1). Thus Delta M2<=C_pz Delta mu. Reversing the coordinate order yields C_zp. Both hold simultaneously. Monotonicity of mu and M2 supplies delta and B. QED.

For each real t>=0 this implies the **coupled exact envelope**:

F_t(x)<=E_t(a,h)
=W(a)-t mu(a)+max_{0<=d<=delta}
{ min(B,C*d)-(2mu(a)+t)d-d^2 }.

The scalar maximization is over a concave piecewise quadratic. Its exact candidate set is d=0, d=delta, d=min(delta,B/C), and d=(C-2mu(a)-t)/2 if the last lies in [0,min(delta,B/C)]. All inputs and comparisons are rational.

Also E_t(a,h)<=M2(h)-mu(a)^2-t mu(a), so it improves or matches the PREFIX-712 endpoint bound on every rectangle.

## Theorem 713.2: 90 additional disjoint 384x384 cells

Use fine-grid denominator 768, inherited parent G=192. Parent indices (i,j) below are off-diagonal. For each of 11 pairs

(16,72), (24,64), (32,72),
(0,80), (4,80), (8,72), (8,80),
(16,80), (24,72), (24,80), (32,64),

all four children indexed (2i+di,2j+dj), di,dj in {0,1}, **failed** at least one of PREFIX-712's old strict endpoint comparisons yet **pass** both E_0(a,h)<F_0(e) and E_{1/2}(a,h)<F_{1/2}(e). Child (di,dj)=(1,1) of parent (4,72) also passes the new and fails the old. Thus 11*4+1=45 exact non-overlapping half-square children. Exchanging p and z preserves Y and all moments, producing 45 further disjoint reflected cells. The attached exact integer/Fraction verifier checks the 45 representatives and the strict margins, and thereby proves 90 new fine cells.

Because F_t is affine in t at each point and both endpoint differences are strictly positive, every point in each selected closed cell satisfies V_q(e)>V_q(x) for **all real q>=2**.

Combining with the previously certified PREFIX-712 cells gives the rigorous exclusion-area lower bound

(137168+90)/147456 = 68629/73728 = 93.08403862847222...% of D.

New additional relative area is exactly 90/147456=5/8192 of D. The remaining region has area at most 5099/73728 of D. The 90 witnesses are disjoint from the old certificate because they fail its original fine-cell tests; inherited parent-cell certification would have implied fine-cell certification.

## Exact test and next work

The companion script retains the frozen PREFIX-712 189-row integer recurrence and correct Gamma completion kernel, rebuilds 9529 nonzero count cells, tests the rational influence coefficients, the finite quadratic maximum and 45 half-square witnesses (90 reflected). A separately implemented local equivalent checker returned ALL_CHECKS_PASS PREFIX713-R6. Published-script remote CI has not been executed. This is an author-level mathematical certificate pending independent review.

Next test the coupled envelope only on PREFIX-712's 10288 still-uncertified fine cells; report the exact extra count and continue with local Bernstein derivative bounds / stationary point isolation toward PREFIX-675's actual global maximizer. The 12<=q<=24 endpoint range may be tested separately.
