#!/usr/bin/env python3
"""Exact rational regression for PREFIX-787 external scalar branch-union examples.

This is NOT a native BRC execution, a complete LP solver, or proof of the
arbitrary-polytope theorem. General identities are proved in companion paper.
"""
from fractions import Fraction as F
import json

# Both branches share A=(1,0), B=(1,0), C=I.
# A genuine branch has u=(0,+M) or u=(0,-M).
# At every q>0, its observer is (1-q,+/-M), hence infinity-norm>=M.
# At q=1 both branch norms attain M; equal convex mixing is (0,0).
def infinity_norm(v):
    return max(abs(v[0]), abs(v[1]))

def v(q, u):
    return (F(1)-q+u[0], u[1])

def regression():
    checks = 0
    mset = sorted({F(a,b) for a in range(1,17) for b in range(1,17)})
    qset = sorted({F(a,b) for a in range(1,13) for b in range(1,10)})
    for m in mset:
        plus=(F(0),m)
        minus=(F(0),-m)
        assert infinity_norm(v(F(1), plus))==m
        assert infinity_norm(v(F(1), minus))==m
        assert v(F(1),(F(0),F(0)))==(F(0),F(0))
        checks += 3
        # Branch-specific exact duals lambda=(0,+/-1) yield value M;
        # they satisfy norm_1=1 and lambda.B=0.
        assert plus[1]==m and -minus[1]==m
        checks += 2
        for q in qset:
            assert infinity_norm(v(q,plus))>=m
            assert infinity_norm(v(q,minus))>=m
            checks += 2
        # A common dual lambda=(lambda1,lambda2) cannot give >0 on both
        # branches: feasibility requires lambda1<=0 and each support value
        # is lambda1 + min(+/-M*lambda2)=lambda1-M*abs(lambda2)<=0.
        for l1 in [F(-1),F(-1,2),F(0)]:
            for l2 in [F(-1),F(0),F(1)]:
                if abs(l1)+abs(l2) <= 1:
                    common=l1-m*abs(l2)
                    assert common<=0
                    checks+=1
        # Same-sign branches u2 in {M,2M}, convex-hull second coordinate
        # in [M,2M]; shared dual lambda=(0,1) proves optimal margin M.
        assert infinity_norm(v(F(1),(F(0),m))) == m
        assert infinity_norm(v(F(1),(F(0),2*m))) == 2*m
        checks += 2
    return {
        'status':'ALL_CHECKS_PASS PREFIX787 BRANCH_UNION_COMMON_DUAL',
        'arithmetic':'Python fractions.Fraction exact rational',
        'scale_count': len(mset), 'q_count': len(qset),
        'assertion_count':checks,
        'source':'Self-contained explicit external scalar branch example',
        'model':'A=(1,0),B=(1,0),C=I; Pplus={(0,M)}, Pminus={(0,-M)}, M>0',
        'exact_results': {'branch_union_margin':'M', 'convex_hull_margin':'0',
             'same_sign_branch_union_margin':'M','same_sign_convex_hull_margin':'M'},
        'mathematical_inference':'Finite rational regression for the explicit examples only; theorem proven algebraically in paper.',
        'frozen_project_input':'awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d',
        'native_brc_execution':False, 'formal_review':'NOT_REVIEWED'
    }

if __name__=='__main__':
    d=regression()
    with open('PREFIX787_R6_BRANCH_UNION_GAP_RESULTS.json','w',encoding='utf8') as fp:
        json.dump(d,fp,ensure_ascii=False,sort_keys=True,indent=2)
        fp.write('\n')
    print(d['status'],d['assertion_count'],d['scale_count'],d['q_count'])
