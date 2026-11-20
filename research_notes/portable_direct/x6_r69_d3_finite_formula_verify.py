#!/usr/bin/env python3
"""X6 R69 exact, self-contained D=3 weighted common-bias BRC test.

No floating-point; independently compares five-vector formula against all
integer histogram differences for bounded populations and positive weights.
"""
from fractions import Fraction as F
from itertools import product
import json

# (a2,a3), source threshold q, (x,y) with z=(0,2x,2y)
CAND = [((1,0),1,(1,3)), ((-3,1),3,(0,3)), ((4,-1),4,(1,0)),
        ((5,-1),5,(2,3)), ((9,-2),9,(3,3))]

def q(a,b):
    return max(max(0,a)+max(0,b),max(0,-a)+max(0,-b))

def xy(a,b):
    return a+3*b,3*a+12*b

def value(x,y,w):
    a,b,c=w
    return max(F(abs(x),a+b),F(abs(y),a+c),F(abs(x-y),b+c))

def finite(p,w):
    return min((value(x,y,w),(a,b)) for (a,b),cost,(x,y) in CAND if cost <= p)[0]

def brute(p,w):
    out=None
    n=0
    for a in range(-p,p+1):
        for b in range(-p,p+1):
            if not (a or b) or q(a,b)>p: continue
            n+=1
            v=value(*xy(a,b),w)
            if out is None or v<out:out=v
    return out,n

def pareto_check(p):
    for a in range(-p,p+1):
        for b in range(-p,p+1):
            if not (a or b) or q(a,b)>p:continue
            x,y=xy(a,b)
            o=(abs(x),abs(y),abs(x-y))
            assert any(cost<=p and all(t<=s for t,s in zip((abs(cx),abs(cy),abs(cx-cy)),o))
                        for (_,cost,(cx,cy)) in CAND), (p,a,b)

assert [q(*a) for a,_,_ in CAND] == [1,3,4,5,9]
for (a,b),_,(x,y) in CAND:
    assert xy(a,b) == (x,y)

profiles=list(product((1,2,3,5,11),repeat=3))
count=0; integer_candidates=0
for p in range(3,16):
    pareto_check(p)
    for w in profiles:
        v,n=brute(p,w)
        assert v==finite(p,w),(p,w,str(v),str(finite(p,w)))
        count+=1; integer_candidates+=n

samples=[]
for w in ((100,1,1),(1,1,100),(1,100,100),(1,1,1),(1,2,17)):
    for p in (3,4,5,8,9):
        val=finite(p,w)
        achievers=[{'a':list(a),'xy':[x,y],'q':cost} for a,cost,(x,y) in CAND if cost<=p and value(x,y,w)==val]
        samples.append({'p':p,'weights':list(w),'eta_star':str(val),'five_candidate_minimizers':achievers})

result={
 'schema':'X6_R69_D3_WEIGHTED_FIVE_CANDIDATES_V1',
 'status':'EXACT_AUTHOR_ENUMERATION_NOT_INDEPENDENT_REVIEW',
 'model':'D=3 normalized positive BRC degree moments with unknown shared additive bias',
 'theorem':'for all p>=3 and positive w, minimize max(|x|/(w1+w2),|y|/(w1+w3),|x-y|/(w2+w3)) among 5 candidates satisfying q<=p',
 'candidates':[{'a':list(a),'q':cost,'xy':[x,y]} for a,cost,(x,y) in CAND],
 'verification':{'p_range':[3,15],'weight_alphabet':[1,2,3,5,11], 'weight_triples':len(profiles),
     'instances':count,'feasible_vectors_inspected_with_multiplicity':integer_candidates,
     'pareto_vectors_checked_per_p':True,'all_assertions_passed':True},
 'examples':samples,
 'freeze':'p000_reality_foundation.json@a72226e2430ffa4786321ac86e7f0c599d5f0389',
 'native_triads':'ADMISSION_PENDING'
}
with open('x6_r69_d3_finite_formula_results.json','w') as f:json.dump(result,f,ensure_ascii=False,indent=2)
print(json.dumps({'verified_instances':count,'vectors_with_multiplicity':integer_candidates,'sample_at_100_1_1':[s for s in samples if s['weights']==[100,1,1]]},indent=2))
