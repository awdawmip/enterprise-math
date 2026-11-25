# R284HP — Exact adjacent tilted-port coupling and uniform residual curvature payment

2026-11-25. Author proof, NOT_REVIEWED. Auxiliary binary-tag safe-word total-count observer, as in frozen R284HM and R284HO; no new native physical attribution. Frozen sources: ee8f08bb614ff06cb63f6e2567d14ead674e42ff:research_notes/portable_direct/R284HM_SUBCRITICAL_POLYA_PORT_TRANSPORT_20261125.md and 35dc10f164c6a93ea5d65c4b5285304188fae549:research_notes/portable_direct/R284HO_EXACT_FIXED_DEFICIT_POLYNOMIAL_STRIPS_20261125.md. P000 and ACTIVE worldview read unchanged. Prior registration request r1-20261124-0256-r284gd-session-v1 returned SUCCEEDED; current private capability not established by that receipt. Independent research only; no CLAIM, shared task state or Result changed. Fresh LEASED inventory r1-20261125-1358-owner-inventory-read was RUNNING at last prepublication observation.

## Theorem (exact joint transport)

For nonnegative integers n,m let M_n(k)=(k+1)/(n+1) binom(2n+2,n-k) for 0<=k<=n, zero elsewhere. Put C_g=sum_k M_n(k)M_m(g-k), c_g=binom(g+3,3), A_g=C_g/(M_n(0)M_m(0)c_g). Let mu_g(k)=M_n(k)M_m(g-k)/C_g for 0<=g<=n+m, r_g=A_(g+1)/A_g (so r_(n+m)=0).

1. For each 0<=g<n+m there exists a coupling of mu_g and mu_(g+1) such that K_(g+1)-K_g is either 0 or 1 almost surely. Thus both actual port coordinates (k,g-k) are nondecreasing and their total increment is exactly one. No independence of the two ports is assumed.
2. Uniformly for all 0<=g<n+m,
   |r_(g+1)-r_g| < 4/(min(n,m)+3).
   This improves HM's O(1/u+(g+2)^2/u^2) absolute curvature bound to O(1/u) whenever n,m are comparable to u, without a square-root restriction.
3. For 0<=g<n, m>=0, one has
   1 <= r_g(n+1,m)/r_g(n,m) <= 1+(2g+3)/[(n-g)(n+g+4)].
   The symmetric statement holds on shifting m for g<m. This is an exact signed mixed transport inequality. In a band g=O(sqrt(u log u)), n,m comparable to u, the cost is O((g+1)/u^2), rather than the O((g+1)^2/u^2) obtained by paying both adjacent levels independently.

## Proof

Write a_k=M_n(k), b_l=M_m(l). The port ratios a_(k+1)/a_k = [(k+2)/(k+1)] [(n-k)/(n+k+3)] strictly decrease over the positive support (and the last ratio is zero). Same for b. Thus mu_(g+1)(k)/mu_g(k), on common positive support, is a positive normalization constant times b_(g+1-k)/b_(g-k), which is nondecreasing in k. The supports are integer intervals [max(0,g-m),min(n,g)] and [max(0,g+1-m),min(n,g+1)], with both endpoints nondecreasing. Therefore the likelihood ratio including possible boundary zeros crosses 1 at most once from below to above: summing the signed mass difference below a cut gives F_(g+1)(k)<=F_g(k). Applying the same argument to the second port g-k yields F_(g+1)(k)>=F_g(k-1). Use the same uniform quantile for the two CDFs; their integer inverse CDFs differ by 0 or 1. This constructs the asserted coupling of the actual tilted laws, not the unweighted Polya law and not a reweighting estimate.

HM's exact Polya identity, including support boundaries by setting rho_n(n)=0, gives
 r_g=1-E_mu_g a_g(k),
 a_g(k)=p_g(k)b_n(k)+(1-p_g(k))b_m(g-k),
 p_g(k)=(k+2)/(g+4), b_z(j)=(2j+3)/(z+j+3).
Here b_z is the rejection probability, unrelated to the moment array b_l used above. The identity also holds at g=n+m, where both rejection probabilities equal one. On each coupled step k'=k+delta, delta in {0,1}, put l=g-k, l'=g+1-k'. Exactly one of k,l increases. The absolute change of p is <=1/(g+5); |b_z(j+1)-b_z(j)|=(2z+3)/[(z+j+3)(z+j+4)] < 2/(z+3). At the old endpoints each rejection probability is in [0,(2g+3)/(min(n,m)+3)], so their difference is bounded by this same number, not twice it. Decompose the change of a into the change of the weights times the old rejection difference, and the new weights times the changed rejection probability. With t=min(n,m), the pointwise bound is
 |a_(g+1)(k')-a_g(k)| < [2+(2g+3)/(g+5)]/(t+3) < 4/(t+3).
Taking the expectation over the coupling proves part 2. In particular if g+1<=alpha*t for fixed alpha<1, r_g and r_(g+1) are bounded below by (t-g-1)/(t+g+4) (each accepted branch has at least this probability). On such a band the same O(1/t) curvature bound holds for log r. No uniform log claim is made at the support edge where r=0.

For part 3 let w_n(k)=M_n(k)/(M_n(0)(k+1)). For k<=n the exact telescoping size ratio is
 R(k)=w_(n+1)(k)/w_n(k)=(n+1)(n+3)/[(n+1-k)(n+k+3)].
The hypothesis g<n ensures no new-support term in either level g or g+1. Consequently
 A_j(n+1,m)/A_j(n,m)=E_mu_j R(k) for j=g,g+1.
For 0<=k<=g,
 R(k+1)/R(k)=1+(2k+3)/[(n-k)(n+k+4)].
This ratio is >=1 and bounded above by its value at g, because the numerator increases and the positive denominator decreases with k. On the coupled step, R(k)<=R(k')<=R(k)[1+(2g+3)/((n-g)(n+g+4))]. Average over the coupling and divide by the old positive expectation. The resulting ratio is exactly r_g(n+1,m)/r_g(n,m), proving part 3. The m version follows by exchanging ports.

## Scientific use and limits

In HN's remaining effective-constant problem and HO's exact monotonicity problem, the relevant ratios of normalized joint sums can now be transported directly: at fixed sizes their adjacent log curvature is O(1/u) uniformly in any g<=alpha min(n,m); for a unit size shift their log change is O((g+1)/u^2) under the same condition. This removes a growing logarithmic loss in the mixed port shift at g=O(sqrt(u log u)). The coupling preserves the two coordinates and their joint law, and only reduces the target total-count observation. These bounds alone do not settle the signed cross products for K, because the O(1/u) pure curvature remains of the same scale as the true neighboring K gap. Next: exploit the signed mixed inequality and the structure of the weighted pure-curvature term to determine the sign or sharper constant in K's exact product/quotient. Retain HO fixed-deficit certificate and HN eventual result as separate dependencies; no new full-domain monotonicity claim.

## Executed exact validation

Python 3 arbitrary integers and Fraction. All n,m=0..24, all g in 0..n+m-1 for curvature and all CDF cuts k=-1..min(n,g+1); all g=0..n-1 for the n-shift. The other shift follows by symmetry. Code:
```python
from math import comb
from fractions import Fraction as F
from functools import lru_cache
@lru_cache(None)
def M(n):
    return [((k+1)*comb(2*n+2,n-k))//(n+1) for k in range(n+1)]
@lru_cache(None)
def C(n,m,g):
    return sum(M(n)[k]*M(m)[g-k] for k in range(max(0,g-m),min(n,g)+1))
def r(n,m,g):
    return F(C(n,m,g+1)*(g+1), C(n,m,g)*(g+4))
def cdf(n,m,g,k):
    return F(sum(M(n)[j]*M(m)[g-j] for j in range(max(0,g-m),min(n,g,k)+1)),C(n,m,g))
curv=mixed=coupling=0; maxscaled=F(0); arg=None
for n in range(25):
    for m in range(25):
        for g in range(n+m):
            a,b=r(n,m,g),r(n,m,g+1)
            v=abs(b-a)*(min(n,m)+3)
            assert v<4
            curv+=1
            if v>maxscaled:maxscaled,arg=v,(n,m,g)
            for k in range(-1,min(n,g+1)+1):
                assert cdf(n,m,g,k-1)<=cdf(n,m,g+1,k)<=cdf(n,m,g,k)
                coupling+=1
        for g in range(n):
            if g>=n+m:continue
            a=r(n,m,g); b=r(n+1,m,g)
            assert a<=b<=a*(1+F(2*g+3,(n-g)*(n+g+4)))
            mixed+=1
print('curvature',curv,'CDF inequalities',coupling,'mixed',mixed,'max_scaled',maxscaled,'arg',arg,'decimal',float(maxscaled))
```
Executed stdout:
```
curvature 15000 CDF inequalities 185000 mixed 7500 max_scaled 153/140 arg (24, 24, 0) decimal 1.0928571428571427
```
185000 cuts each check both CDF bounds (370000 scalar comparisons); 7500 mixed cases each check both bounds. Observed maximum is finite evidence, not a global sharp constant. All checks passed. The theorem is analytic and does not rely on finite enumeration.
