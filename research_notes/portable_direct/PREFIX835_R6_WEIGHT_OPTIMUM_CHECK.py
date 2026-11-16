#!/usr/bin/env python3
"""PREFIX-835: exact finite minimum-max-weight exhaustive search for even-time Q aliases.

Fixed auxiliary positive named-source BRC model: p=q=3; Q=R+A; insertion a=1;
marked removal b=2. No native X6 physical-time event claim.
"""
from collections import defaultdict
import json

TIMES=list(range(4,41,2))

def e23(a,b,c):
    return a*b+a*c+b*c,a*b*c

def opt(T, max_bound=135):
    assert T>=4 and T%2==0
    seen={}; checked=0
    for M in range(1,max_bound+1):
        for a in range(1,M+1):
            for b in range(a,M+1):
                c=M
                s=a+b+c; e2,e3=e23(a,b,c)
                k=(s,4*e2+3*(T-2)*e3)
                checked+=1
                previous=seen.get(k)
                if previous is not None and (previous[3],previous[4])!=(e2,e3):
                    A=list(previous[:3]); B=[a,b,c]
                    assert max(A+B)==M
                    assert sum(A)==sum(B)
                    ea2,ea3=e23(*A);eb2,eb3=e23(*B)
                    assert 4*(ea2-eb2)+3*(T-2)*(ea3-eb3)==0
                    assert ea2!=eb2
                    return {'T':T,'minimum_max_weight':M,'A':A,'B':B,
                            'delta_e2':ea2-eb2,'delta_e3':ea3-eb3,
                            'triples_examined_before_first_solution':checked}
                seen[k]=(a,b,c,e2,e3)
    raise RuntimeError(f'Not found for T={T} through {max_bound}')

def hist(w,steps):
    p=3;states={(7,0):1}; out=[];edge_updates=0
    for t in range(steps+1):
        y=[0]*4
        for (mask,flag),mass in states.items():y[mask.bit_count()+flag]+=mass
        out.append(y)
        if t==steps:break
        ns=defaultdict(int)
        for (mask,flag),mass in states.items():
            for i,wi in enumerate(w):
                if mask&(1<<i):ns[(mask^(1<<i),flag)]+=mass*wi;edge_updates+=1
            if flag:ns[(mask,0)]+=mass*2;edge_updates+=1
            elif mask.bit_count()<3:ns[(mask,1)]+=mass;edge_updates+=1
        states=dict(ns)
    return out,edge_updates

def run():
    data=[];compares=0;updates=0
    for T in TIMES:
        row=opt(T)
        A,B=row['A'],row['B']
        yA,uA=hist(A,T+2);yB,uB=hist(B,T+2);updates+=uA+uB
        equal=[t for t in range(T+3) if yA[t]==yB[t]]
        assert equal==[0,1,T], (T,equal)
        row['equality_times_through_T_plus_2']=equal
        row['histogram_at_T']=[str(x) for x in yA[T]]
        row['linear_family_max_weight']=3*T-1
        compares+=4*(T+3)
        data.append(row)
    payload={'schema':'PREFIX835_R6_EVEN_RECOLLISION_EXHAUSTIVE_MIN_MAX_WEIGHT_V1',
             'fixed_operator':{'a':1,'b':2},'capacity':3,'T_even_domain':TIMES,
             'method':'Complete sorted triple enumeration by increasing maximum weight; equal (sum,4e2+3(T-2)e3) hash buckets; first distinct pair certifies optimum.',
             'rows':data,'all_tested_instances':len(data),
             'triples_examined':sum(r['triples_examined_before_first_solution'] for r in data),
             'named_edge_updates':updates,'histogram_scalar_comparisons':compares,
             'result':'ALL_EXACT_ASSERTIONS_PASSED',
             'scope':'Exact finite optimum only for even T=4,6,...,40 and p=3 fixed b=2; unbounded T optimum remains open.'}
    print(json.dumps(payload,indent=2))

if __name__=='__main__':run()
