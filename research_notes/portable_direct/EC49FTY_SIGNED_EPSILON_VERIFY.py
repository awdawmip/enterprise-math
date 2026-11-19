#!/usr/bin/env python3
"""EC49FTY signed parameter extension: exact Fraction signs, no native BRC run."""
from fractions import Fraction as F
import json
T=F(27,64)
C=F(161810711838720000000)
linear_upper=(-F(5717812295230560000)
    +F(305754824245248000)*T+F(362941513728000)*T**3)
quadratic_lower=(F(50508727815805875)
    -F(5444018553646575)*T-F(8611122157056)*T**3)
assert linear_upper==-F(5588794727402400000)<0
assert quadratic_lower==F(24684229593641242071,512)>0
for t in (F(0),T/3,T):
    L1=-F(5717812295230560000)+F(305754824245248000)*t-F(7490036957184000)*t*t+F(362941513728000)*t**3
    Q=F(50508727815805875)-F(5444018553646575)*t+F(259868534207292)*t*t-F(8611122157056)*t**3+F(142745649152)*t**4
    assert L1<=linear_upper<0 and Q>=quadratic_lower>0
    for u in (F(-1),F(-1000),F(-1000000)):
        assert C+u*L1+u*u*Q>=C>0
print(json.dumps({
 "schema":"EC49FTY_SIGNED_EPSILON_CERT_V1",
 "admissible_real_epsilon":"(-infinity,1048576/18958647]",
 "strictly_positive_real_epsilon":"(-infinity,1048576/18958647)",
 "full_mixed_FOSD":"all admissible real epsilon, inherited high-gap interval",
 "P_linear_coefficient_upper":str(linear_upper),
 "P_quadratic_coefficient_lower":str(quadratic_lower),
 "P_lower_for_negative_epsilon":str(C),
 "analytic_continuous_argument":"strict TP2 plus moving lower cutoff",
 "native_bellman_rerun":False,
 "status":"AUTHOR_PROVED_EXACT_FRACTION_VERIFIED_PARENT_DEPENDENT_NOT_REVIEWED"
},indent=2))
