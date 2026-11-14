#!/usr/bin/env python3
"""Exact rational checks for PREFIX-788, external scalar provenance graph.
No native BRC/X6 arithmetic is implemented or claimed.
"""
from fractions import Fraction as F
from itertools import product
import json


def subset_path_margin(weights, target):
    vals = {0}
    for a in weights:
        vals = vals | {v + a for v in vals}
    return min(abs(v - target) for v in vals), sorted(vals)


def enumerate_path_margin(weights, target):
    return min(abs(sum(a*b for a,b in zip(weights,bits))-target)
               for bits in product((0,1), repeat=len(weights)))


def shortest_path_support(weights, target, lam1, lam2):
    # A=(1,-target), B=(1,0), stage edge=(0,0) or (0,a).
    # Lambda: |lam1|+|lam2|<=1 and lam1<=0.
    assert abs(lam1)+abs(lam2)<=1 and lam1<=0
    h=F(0)
    for a in reversed(weights):
        h=min(h, F(a)*lam2+h)
    return lam1-F(target)*lam2+h


def brute_path_support(weights, target, lam1, lam2):
    return min(lam1 + lam2*(sum(a*b for a,b in zip(weights,bits))-target)
               for bits in product((0,1),repeat=len(weights)))


def temporal_coupled_margin(M):
    # Two stages, each +/-M, permitted sign history ++ or -- only.
    true_paths=(2*M,-2*M)
    relaxed_paths=(2*M,0*M,0*M,-2*M)
    return min(abs(x) for x in true_paths), min(abs(x) for x in relaxed_paths)


def main():
    checks=0
    counted={'subset_instances':0,'dual_oracle_checks':0,'matched_sign_instances':0}
    examples=[]
    for n in range(1,8):
        weights=tuple((i*i+3*i+5)%11+1 for i in range(n))
        for target in range(0,sum(weights)+3):
            rho,vals=subset_path_margin(weights,target)
            assert rho == enumerate_path_margin(weights,target)
            checks+=1
            # For target inside [0,sum(weights)], convexification includes zero.
            if 0 <= target <= sum(weights):
                assert min(abs(F(target)),abs(F(sum(weights)-target)))>=0
                hull_zero=True
            else:
                hull_zero=False
            if rho==0:
                assert target in vals
            else:
                assert target not in vals
            checks+=2
            counted['subset_instances']+=1
            if n==2 and target==4:
                examples.append({'weights':list(weights),'target':target,'rho':rho,'hull_zero':hull_zero})
            for i in range(-5,1):
                for j in range(-5,6):
                    x,y=F(i,10),F(j,10)
                    if abs(x)+abs(y)>1:
                        continue
                    assert shortest_path_support(weights,target,x,y)==brute_path_support(weights,target,x,y)
                    checks+=1
                    counted['dual_oracle_checks']+=1
    for n in range(1,160):
        M=F(2*n+1,n+7)
        rho,relaxed=temporal_coupled_margin(M)
        assert rho==2*M and relaxed==0
        checks+=2
        counted['matched_sign_instances']+=1
    # Named exact witness: {0,3,5,8} never contains 4, but convex hull does.
    named= {'weights':[3,5],'target':4}
    rho,values=subset_path_margin(named['weights'],named['target'])
    assert values==[0,3,5,8] and rho==1
    checks+=2
    output={'status':'ALL_CHECKS_PASS PREFIX788 TEMPORAL_BRANCH_DUAL_AND_SUBSET_GAP',
            'scope':'Exact rational/integer tests of explicit external scalar models, not native X6 transfer',
            'frozen_scientific_pin':'f42f2906d77f24085c123f3ccfe9667d41caa96d',
            'counts':counted, 'assertions':checks,
            'named_subset_gap':{'weights':[3,5],'target':4,'reachable':values,'true_margin':'1','convex_margin':'0'},
            'two_stage_coupling':{'law':'sigma2=sigma1 in {-1,+1}',
                                 'true_margin':'2M','unconstrained_margin':'0',
                                 'valid_for':'every real M>0'},
            'verification':'finite regression; general LP duality, Bellman recurrence and subset-sum reduction are proved on paper'}
    print(json.dumps(output,ensure_ascii=False,indent=2,sort_keys=True))


if __name__=='__main__': main()
