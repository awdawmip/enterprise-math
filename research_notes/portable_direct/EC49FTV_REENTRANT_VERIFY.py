#!/usr/bin/env python3
"""EC49FTV reentrant lambda=3 exact rational phase witness; stdlib only."""
from fractions import Fraction as F
import json
def P(x):return -101128098337841727*x*x+13756372856507671600*x-343441077286459320000
lo=-F(960,7)
hi=F(6720,59)
assert lo<32<33<103<104<hi
assert P(F(32))<0<P(F(33))
assert P(F(103))>0>P(F(104))
assert P(lo)<0 and P(hi)<0
# P concave quadratic, so precisely two crossing roots in full domain.
a=F(101128098337841727)
b=F(13756372856507671600)
c=F(343441077286459320000)
disc=b*b-4*a*c
assert disc==F(50311622018943600935576908117264000000)>0
assert disc==F(28000**2)*F(64172987269060715479052178721)
print(json.dumps({
 'schema':'EC49FTV_REENTRANT_LAMBDA3_V1',
 'lambda':3,'domain':['-960/7','6720/59'],
 'phase_polynomial':'-101128098337841727*theta^2+13756372856507671600*theta-343441077286459320000',
 'lower_root':'(6878186428253835800 - 14000*sqrt(64172987269060715479052178721))/101128098337841727',
 'upper_root':'(6878186428253835800 + 14000*sqrt(64172987269060715479052178721))/101128098337841727',
 'lower_root_in':'(32,33)','upper_root_in':'(103,104)',
 'exact_sign_witness':{'theta_32':str(P(F(32))),'theta_33':str(P(F(33))),
                       'theta_103':str(P(F(103))),'theta_104':str(P(F(104)))},
 'condition':'complete FOSD iff theta in [lower_root,upper_root] for lambda=3',
 'mathematical_status':'AUTHOR_PROVED / EXACT_RATIONAL_CHECKED / PARENT_DEPENDENT / NOT_REVIEWED'
},indent=2))
