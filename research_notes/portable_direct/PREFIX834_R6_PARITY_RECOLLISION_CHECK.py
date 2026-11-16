#!/usr/bin/env python3
"""PREFIX-834: exact named-state Q histograms and all-parity re-alias witnesses.

Positive unnormalized BRC auxiliary model, not native X6 time licensing.
No third-party dependencies; all arithmetic uses arbitrary-precision integers.
"""
from collections import defaultdict
from math import comb, factorial
import json

A_WEIGHT, B_WEIGHT = 1, 2

def elementary(w):
    e = [1] + [0]*len(w)
    for x in w:
        for j in range(len(w), 0, -1):
            e[j] += x*e[j-1]
    return e

def named_histograms(w, steps, a=A_WEIGHT, b=B_WEIGHT):
    p = len(w)
    states = {((1<<p)-1, 0): 1}
    result=[]; updates=0
    for t in range(steps+1):
        hist = [0]*(p+1)
        for (mask, marked), mass in states.items():
            occupied=mask.bit_count()+marked
            assert 0<=occupied<=p
            hist[occupied]+=mass
        result.append(hist)
        if t == steps:
            break
        nxt=defaultdict(int)
        for (mask,marked), mass in states.items():
            for i, wi in enumerate(w):
                if mask>>i & 1:
                    nxt[(mask ^ (1<<i),marked)] += mass*wi
                    updates+=1
            if marked:
                nxt[(mask,0)] += mass*b
                updates+=1
            elif mask.bit_count()<p:
                nxt[(mask,1)] += mass*a
                updates+=1
        states=dict(nxt)
    return result,updates

def formula_difference(A,B,t,a=A_WEIGHT,b=B_WEIGHT):
    p=len(A)
    assert len(B)==p
    d=[x-y for x,y in zip(elementary(A),elementary(B))]
    out=[0]*(p+1)
    if t==0: return out
    for k in range(1,min(t,p)+1):
        for marked in (0,1):
            rem=t-k-marked
            if rem<0 or rem%2: continue
            r=rem//2
            occ=p-k+marked
            out[occ] += factorial(k)*d[k]*comb(t-1,k-1)* a**(r+marked)*b**r
    return out

def family(T):
    assert T>=3
    if T%2:
        k=4*T-1
        return [1,2*k,2*k], [2,2,k*k],1
    L=3*T-2
    return [1,4,L], [2,2,L+1],2

def singleton_pair(T):
    assert T%2==1 and T>=3
    return [1,2*T+1], [2,T+1]

def run():
    tests=[3,4,5,6,7,8,9,10,11,12,17,20,21,30,40]
    rows=[]; scalar_checks=0; transition_updates=0; parity_checks=0
    for T in tests:
        A,B,n=family(T)
        EA=elementary(A);EB=elementary(B)
        diff=[x-y for x,y in zip(EA,EB)]
        assert min(i for i,v in enumerate(diff) if v and i>0)==n
        if T%2:
            assert diff[3]==0 and 2*diff[1]+2*(T-1)*diff[2]==0
        else:
            assert diff[1]==0 and 4*diff[2]+3*(T-2)*diff[3]==0
        yA,uA=named_histograms(A,T+4)
        yB,uB=named_histograms(B,T+4)
        transition_updates+=uA+uB
        zeros=[]
        for t,(y,z) in enumerate(zip(yA,yB)):
            delta=[v-w for v,w in zip(y,z)]
            calc=formula_difference(A,B,t)
            assert delta==calc, (T,t,delta,calc)
            scalar_checks += len(delta)
            if not any(delta):zeros.append(t)
        assert zeros == ([0,T] if n==1 else [0,1,T]), (T,zeros)
        for t in range(n+1,T+5):
            if (t-n)%2==1:
                assert yA[t][3-n+1]!=yB[t][3-n+1]
                parity_checks+=1
        rows.append({"T":T,"A":A,"B":B,"first_separation":n,"elementary_difference":diff,"equality_times_through_T_plus_4":zeros,"max_source_weight":max(A+B),"histogram_at_T":yA[T]})
    two_source_checks=0
    for T in [3,5,7,11,21,31]:
        A,B=singleton_pair(T)
        yA,uA=named_histograms(A,T+2)
        yB,uB=named_histograms(B,T+2)
        transition_updates+=uA+uB
        eq=[t for t,(u,v) in enumerate(zip(yA,yB)) if u==v]
        assert eq==[0,T]
        two_source_checks+=T+3
    report={
        "schema":"PREFIX834_R6_EXACT_PARITY_RECOLLISION_V1",
        "science_pin":"awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d",
        "model":{"capacity":"p (# named initial sources)","Q":"sum of all legal removals and marked source insertions","a":A_WEIGHT,"b":B_WEIGHT,"initial_marked_present":False,"weights":"positive integers","numeric":"Python arbitrary precision integers"},
        "tested_times":tests,
        "profiles":rows,
        "two_source_odd_tests":6,
        "two_source_frame_checks":two_source_checks,
        "histogram_scalar_comparisons":scalar_checks,
        "transition_edge_updates":transition_updates,
        "opposite_parity_checks":parity_checks,
        "result":"ALL_EXACT_ASSERTIONS_PASSED",
        "proof_scope":"General theorem via exact PREFIX-833.1 and PREFIX-833.2 plus algebraic identities; tests are finite cross-checks, not universal proof.",
        "status":"AUTHOR_PROVED / EXACT_NAMED_STATE_REGRESSION / NOT_INDEPENDENTLY_REVIEWED / NOT_ADMITTED"
    }
    print(json.dumps(report,ensure_ascii=False,indent=2))

if __name__=='__main__': run()
