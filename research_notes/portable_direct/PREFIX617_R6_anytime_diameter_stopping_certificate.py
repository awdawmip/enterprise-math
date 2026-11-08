#!/usr/bin/env python3
"""PREFIX-617: exact arithmetic evidence for anytime confidence-diameter BRC stopping.
Relies on PREFIX-610 signed-label likelihood and PREFIX-613 beta-binomial e-martingale.
No simulation or original native 96-port graph rerun is claimed.
"""
from fractions import Fraction as F
from math import comb
from functools import lru_cache
import json
from pathlib import Path

alpha = F(1,20)
d = 2
beta = alpha / d
q = 12
width_p = F(1,4)
checks = 0

def check(condition, msg):
    global checks
    if not condition:
        raise AssertionError(msg)
    checks += 1

def L(m, k, p):
    """(m+1)*Binom(m,k)*p^k*(1-p)^(m-k), inverse e-value."""
    return (m+1) * comb(m,k) * p**k * (1-p)**(m-k)

# The all-positive interval is ( (beta/(m+1))^(1/m), 1 ) in p.
# Its diameter <= 1/4 iff (m+1)*(3/4)^m <= beta.
thresholds = [m for m in range(1,320) if (m+1)*F(3,4)**m <= beta]
m_star = min(thresholds)
check(m_star == 25, 'first 1/4-width all-positive count')
for m in range(1,m_star):
    check((m+1)*F(3,4)**m > beta, f'no earlier all-positive stop m={m}')
check((m_star+1)*F(3,4)**m_star < beta, 'strict stop at m_star')
check((m_star)*F(3,4)**(m_star-1) > beta, 'strict failure at m_star-1')
for m in range(1,321):
    # Bound L(m,k,p_hat) >=1 (MLE binomial mass at its mode >=1/(m+1)).
    for k in range(m+1):
        phat=F(k,m)
        check(L(m,k,phat) >= 1, f'MLE core m={m} k={k}')

# Sign adaptivity witness at SAME count m=25:
# all-positive width <1/4, but k=12 interval includes 1/4 and 3/4
# hence diameter >=1/2 for the mixed-sign observation.
check(L(25,12,F(1,4))>beta, 'mixed k=12 accepts p=1/4')
check(L(25,12,F(3,4))>beta, 'mixed k=12 accepts p=3/4')

# Finite rational certificate for log(12840)<10 using exp(10) > 12840.
# At m=320, (m+1)/beta =12840. Hence Pinsker gives diameter_p<1/4.
factorial=1
exp_lower=F(1)
for i in range(1,11):
    factorial *= i
    exp_lower+= F(10**i,factorial)
check(exp_lower > 12840, 'finite Taylor exp(10) lower bound')
check(F(2*10,320)==F(1,16), 'universal diameter 1/4 cap')

# Exact independent expectation checks for the coupon waiting time when
# at the one-sided p->1 boundary every informative sign is positive.
r=25
G=F(2*r)-sum((F(comb(a+b,a),2**(a+b+1)) for a in range(r) for b in range(r)), F(0))
E_gamma=q*G

@lru_cache(None)
def E_dp(a,b):
    if a==r and b==r:
        return F(0)
    successors=[]
    if a<r: successors.append((a+1,b))
    if b<r: successors.append((a,b+1))
    return F(q,len(successors)) + sum((E_dp(*s) for s in successors),F(0))/len(successors)

E_markov=E_dp(0,0)
check(E_gamma == E_markov, 'gamma maximum and count Markov recurrence agreement')
check(E_gamma == F(11740411062003525,35184372088832), 'published exact q12 boundary expected cost')
check(2*E_markov == F(11740411062003525,17592186044416), 'q24 geometric thinning')

# Check all-m upper-bound control for equal-tailed e-CS; m=320 implies
# Pinsker radius; t>=320 only improves log((m+1)/beta)/m.
# Its continuous derivative is negative since log(1+x)> x/(1+x), x>0.
# E stopped cost is dominated by T_{q,d,320}; exact count cap expectation.
r_cap=320
G_cap=F(2*r_cap)-sum((F(comb(a+b,a),2**(a+b+1)) for a in range(r_cap) for b in range(r_cap)), F(0))
E_cap=q*G_cap
check(E_cap>E_gamma, 'uniform cap dominates one-sided boundary')

report={
 'schema':'PREFIX617_R6_ANYTIME_DIAMETER_STOPPING_V1',
 'science_pin':'f42f2906d77f24085c123f3ccfe9667d41caa96d',
 'dependencies':['PREFIX-610 signed-label observation law','PREFIX-613 e-martingale and rectangular confidence sequence','PREFIX-615 geometric thinning','PREFIX-616 sign-completion rare-sign bound'],
 'alpha':str(alpha),'d':d,'q':q,'beta':str(beta),'target_p_diameter':str(width_p),'target_theta_diameter':str(width_p/48),
 'all_positive_first_count':m_star,
 'uniform_sufficient_per_direction_count':320,
 'boundary_limit_q12_mean_exact':str(E_gamma),
 'boundary_limit_q12_mean_rounded':round(float(E_gamma),8),
 'boundary_limit_q24_mean_exact':str(2*E_gamma),
 'uniform_q12_mean_bound_exact':str(E_cap),
 'uniform_q12_mean_bound_rounded':round(float(E_cap),8),
 'checks':checks,
 'verification':'ALL_CHECKS_PASS',
 'verification_scope':'Exact Fraction combinatorics and elementary integer bounds in declared d=2 native-derived signed-label model; no re-execution of PREFIX-565 original 96-port graph.'
}
with open(Path(__file__).with_name('PREFIX617_R6_RESULTS.json'),'w',encoding='utf-8') as f:
    json.dump(report,f,ensure_ascii=False,indent=2)
print('ALL_CHECKS_PASS',checks)
print(json.dumps(report,ensure_ascii=False,indent=2))
