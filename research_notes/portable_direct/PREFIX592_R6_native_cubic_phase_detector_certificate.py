#!/usr/bin/env python3
"""Exact native X6-BRC certificate: W3 = W2 + Q*1_{phase=(3,-2,4)}.
Depends on published PREFIX591 and PREFIX565; their import reconstructs
original six labeled BRC actions at the frozen zero root.
"""
from fractions import Fraction as F
from math import comb
import json
from PREFIX591_R6_unbounded_cubic_observer_invariant_module_certificate import (
    SCIENCE_PIN, W, EXPS, weighted_op, EDGES
)
from PREFIX565_positive_marginal_certificate import PHASES
assert SCIENCE_PIN == 'f42f2906d77f24085c123f3ccfe9667d41caa96d'
assert len(PHASES)==48 and len(EDGES)==96
assert PHASES[42] == (3,-2,4)
assert [len(s) for s in W] == [1,13,32,33]

g = [int(i//2==42) for i in range(96)]
assert [i for i,x in enumerate(g) if x] == [84,85]

def mod_W2(vec):
    v=[F(x) for x in vec]
    for p,r in sorted(W[2].pivots.items()):
        if v[p]:
            c=v[p]
            for j in range(p,96):
                v[j]-=c*r[j]
    return v

assert W[3].contains(g) and not W[2].contains(g)
assert W[3].vectors[-1] == g
assert mod_W2(g)==g
assert mod_W2(weighted_op((0,0,1),W[2].vectors[24])) == [F(3,4)*x for x in g]
assert sorted(W[3].pivots)==sorted(W[2].pivots)+[84]

# Exact unnormalized native path-moment recurrence, six original action labels.
M={a:([1]*96 if a==(0,0,0) else [0]*96) for a in EXPS}
by_depth={}
for n in range(5):
    new={}
    for alpha in EXPS:
        if sum(alpha)!=3:continue
        rem=mod_W2(M[alpha])
        assert all(rem[i]==0 for i in range(96) if i not in (84,85))
        assert rem[84]==rem[85]
        if rem[84]:new['/'.join(map(str,alpha))]=str(rem[84])
    by_depth[str(n)]=new
    if n==4:break
    N={}
    for alpha in EXPS:
        value=[F() for _ in range(96)]
        for beta in EXPS:
            if all(beta[k]<=alpha[k] for k in range(3)):
                gamma=tuple(alpha[k]-beta[k] for k in range(3))
                coeff=comb(alpha[0],beta[0])*comb(alpha[1],beta[1])*comb(alpha[2],beta[2])
                v=weighted_op(gamma,M[beta])
                for i in range(96):value[i]+=coeff*v[i]
        N[alpha]=value
    M=N
assert all(by_depth[str(n)]=={} for n in range(4))
assert by_depth['4']=={'2/0/1':'-13824','2/1/0':'13824','3/0/0':'331776'}
result={
 'schema':'PREFIX592_R6_PHASE_DETECTOR_CERTIFICATE_V1',
 'status':'ALL_CHECKS_PASS','science_pin':SCIENCE_PIN,
 'native_input':'PREFIX565 original edge, zero root, 96 ports, six labeled actions',
 'graded_dimensions':[len(s) for s in W],
 'native_phase_index':42,'native_phase_tuple':[3,-2,4],
 'branch_ports':[84,85],
 'generator':'g(i)=1 if i//2==42 else 0',
 'exact_decomposition':'W3 = W2 direct_sum Q*g',
 'native_operator_witness':'B_(0,0,1) applied to W2 basis[24] has quotient remainder 3/4*g',
 'proof':'W3.contains(g), not W2.contains(g), dim W3=33, dim W2=32',
 'cubic_moment_residuals_mod_W2_by_depth':by_depth,
 'scope':'All path lengths via previously certified W3 closure; root zero; cubic and lower T,P0,P1 moments; arbitrary initial port law',
 'formal_native_claim_or_review':False
}
print('ALL_CHECKS_PASS')
print(json.dumps(result,ensure_ascii=False,indent=2))
