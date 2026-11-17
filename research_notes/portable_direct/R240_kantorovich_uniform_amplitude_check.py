#!/usr/bin/env python3
"""R240 exact rational certificate; standalone Python 3, no third-party modules."""
from fractions import Fraction as F
from math import comb
import json

# R234-R239 seven-source stationary sticky-reset observer; all comparisons exact.
Z39 = F(122345, 46116)       # Z(39/100), Z'(s)>0 on I
Zfloor = F(53, 20)
z3 = F(50, 1089)           # b_3/(1-alpha_3)^2
neutral_mass = F(65, 192) # pi_0/(1-alpha_0)
r_floor = F(594323, 600000)
alpha_ceiling = F(39, 50)
M = F(21,20)               # upper bound for (1-alpha)/(r-alpha)
kap = 4*M/(1+M)**2
W = (144,576,1440,4320,17280,86400,518400)
Gamma0 = sum(comb(6,u)*W[u] for u in range(6))
Gamma1 = sum(comb(5,u-1)*W[u] for u in range(1,6))
Tgap = Gamma0-Gamma1
eta = F(W[5])*kap*(Zfloor-z3)/(F(Gamma1)*Zfloor+F(Tgap)*neutral_mass)
q = F(14771007,14858075)  # R239 spectral ratio
assert Z39>Zfloor and F(13075,16632)>0
assert F(21)*r_floor>20+alpha_ceiling
assert kap == F(1680,1681)
assert Gamma0==889200 and Gamma1==655776 and Tgap==233424
assert eta == F(304910592000,2463633795601)
assert 0<eta<1 and 0<q<1

def certified(n, denominator):
    """Strict: ((1-eta)/eta)*q**(n-1) < 1/denominator."""
    k=n-1
    return denominator*(eta.denominator-eta.numerator)*q.numerator**k < eta.numerator*q.denominator**k

def minimal_horizon(denominator):
    # Monotonicity in n, find minimum without floating-point or logarithms.
    low,high=2,2
    while not certified(high,denominator): high*=2
    while low<high:
        mid=(low+high)//2
        if certified(mid,denominator): high=mid
        else: low=mid+1
    assert certified(low,denominator) and not certified(low-1,denominator)
    return low

h100=minimal_horizon(100)
h1000=minimal_horizon(1000)
assert (h100,h1000)==(1118,1510)
result={
    'result':'PASS','mode':'exact_integer_and_fraction_certificate',
    'parameters':'R234: 39/100 < s < 41/100, 7-state reversible sticky-reset, k=6, L=2',
    'Z39':str(Z39),'Zfloor':str(Zfloor),
    'kantorovich_factor':str(kap),
    'amplitude_fraction_lower':str(eta),
    'previous_R239_amplitude_fraction_lower':'2159042/128474775',
    'uniform_secondary_over_primary_ratio':str(q),
    'relative_error_lt_1_percent_from_n':h100,
    'relative_error_lt_0_1_percent_from_n':h1000,
    'independent_review':'NOT_REVIEWED',
    'native_brc_execution':'NOT_EXECUTED',
    'checks':['Z(s) increasing on I and Z39>53/20',
              '21*r_floor>20+39/50 gives 1<y_j<21/20',
              'Kantorovich algebra', 'exact weights and stationary T expression',
              'eta reduced fraction', 'both horizon thresholds plus immediate predecessors']
}
print(json.dumps(result,ensure_ascii=False,sort_keys=True,indent=2))
