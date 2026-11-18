#!/usr/bin/env python3
"""R284V exact cofactor/Hall tests; requires neighboring R284U checker."""
from fractions import Fraction as F
from itertools import product
from R284U_observer_cut_scc_certificate import determinant, matrices
import json


def det_pair(n, a, b, baseline, edits, vals):
    m = matrices(n, baseline, edits, vals)
    minor = [[m[i][j] for j in range(n) if j != a] for i in range(n) if i != b]
    return (-1)**(a+b) * determinant(minor), determinant(m)


def minor_has_matching(n, a, b, u, v, baseline, edits):
    if u == b or v == a:
        return False
    rows = [i for i in range(n) if i not in (b,u)]
    cols = [j for j in range(n) if j not in (a,v)]
    edit_edges=set(edits.values())
    support={(i,j) for i in rows for j in cols
             if i==j or baseline.get((i,j), F(0)) > 0 or (i,j) in edit_edges}
    def augment(k, taken):
        if k==len(rows):
            return True
        return any(augment(k+1, taken|{j}) for j in cols if j not in taken and (rows[k],j) in support)
    return augment(0,set())


def run():
    e = {'x': (1,2)}
    b1 = {(0,2): F(1,4), (2,1): F(1,8)}
    b2 = {(0,2): F(1,5), (2,1): F(1,4)}
    assert not minor_has_matching(3,0,2,1,2,b1,e)
    assert not minor_has_matching(3,0,2,1,2,b2,e)
    observations = []
    for x in [F(0), F(1,16), F(1,8), F(1,4)]:
        n1,d1=det_pair(3,0,2,b1,e,{'x':x})
        n2,d2=det_pair(3,0,2,b2,e,{'x':x})
        assert n1==F(1,4) and n2==F(1,5)
        assert d1==1-x/8 and d2==1-x/4
        assert n1*d2-n2*d1==F(1,20)-F(3,80)*x
        observations.append([x.numerator,x.denominator])

    # A previously absent 0->1 path breaks the no-matching condition.
    b2nonzero={**b2,(0,1):F(1,8)}
    assert minor_has_matching(3,0,2,1,2,b2nonzero,e)
    for x in [F(0),F(1,16),F(1,8),F(1,4)]:
        n1,d1=det_pair(3,0,2,b1,e,{'x':x})
        n2,d2=det_pair(3,0,2,b2nonzero,e,{'x':x})
        assert n2 == F(1,5)+x/8 and d2==1-x/4
        assert n1*d2-n2*d1==F(1,20)-F(13,80)*x+x*x/64

    # Exhaustive 3-port support sufficiency over all observer pairs,
    # edit endpoints and baseline subsets. 9*9*256 = 20,736 cases.
    edges=list(product(range(3),repeat=2))
    tests=0
    no_matching=0
    for a,b in product(range(3),repeat=2):
        for u,v in edges:
            other=[f for f in edges if f!=(u,v)]
            for mask in range(256):
                baseline={f:F(1,16) for j,f in enumerate(other) if mask&(1<<j)}
                edits={'x':(u,v)}
                cert=minor_has_matching(3,a,b,u,v,baseline,edits)
                n0,_=det_pair(3,a,b,baseline,edits,{'x':F(0)})
                n1,_=det_pair(3,a,b,baseline,edits,{'x':F(1,8)})
                if not cert:
                    no_matching+=1
                    assert n0==n1,(a,b,u,v,mask,n0,n1)
                tests+=1
    assert tests==9*9*256
    return {'schema':'R284V_EXACT_COFACTOR_HALL_VERIFICATION_V1',
        'result':'PASS','arithmetic':'Fraction exact determinants; exhaustive 3-port support enumeration',
        'primary_example':{'a':0,'b':2,'edit':'x:1->2','matched_models':2,'no_matching_for_both':True,'N1':'1/4','N2':'1/5','P':'1/20-3*x/80','sample_nodes':observations},
        'negative_control':{'added_baseline_edge':'0->1, weight 1/8','complement_minor_matching':True,'P':'1/20-13*x/80+x^2/64','quadratic_coefficient':[1,64]},
        'exhaustive_support_cases':tests,'exhaustive_no_matching_cases':no_matching,
        'exhaustive_no_matching_implies_zero_cofactor_derivative':'PASS',
        'scope':'Finite exact instances support general Leibniz matching proof; no converse for matching-present inputs claimed'}

if __name__=='__main__':
    print(json.dumps(run(),indent=2,sort_keys=True))
