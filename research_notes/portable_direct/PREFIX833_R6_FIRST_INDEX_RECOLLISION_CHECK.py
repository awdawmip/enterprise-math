#!/usr/bin/env python3
"""PREFIX-833: exact Q-only named-source regression for first-index recollision criterion.
Standard-library exact integer arithmetic. No transition formula is used in the state DP.
"""
from collections import defaultdict
from itertools import combinations_with_replacement, combinations
from math import comb, factorial
import json

def elementary(weights):
    out=[1]+[0]*len(weights)
    for j,w in enumerate(weights,1):
        for k in range(j,0,-1):
            out[k]+=w*out[k-1]
    return out

def observe(weights,a,b,horizon):
    p=len(weights)
    full=(1<<p)-1
    states={(full,0):1}
    hist=[]
    trans=0
    for t in range(horizon+1):
        y=[0]*(p+1)
        for (mask,mark),mass in states.items():
            y[mask.bit_count()+mark]+=mass
        hist.append(y)
        if t==horizon:break
        nxt=defaultdict(int)
        for (mask,mark),mass in states.items():
            maskbits=mask
            while maskbits:
                bit=maskbits&-maskbits
                idx=bit.bit_length()-1
                nxt[(mask^bit,mark)]+=mass*weights[idx]
                maskbits-=bit
                trans+=1
            if mark:
                nxt[(mask,0)]+=b*mass;trans+=1
            elif mask.bit_count()<p:
                nxt[(mask,1)]+=a*mass;trans+=1
        states=nxt
    return hist,trans

def full_criterion(delta,n,t,b,p):
    if t<n:return True
    if t==n:return False
    if (t-n)%2:
        return False
    for k in range(n,min(p,t)+1,2):
        if k==t:
            if delta[k]:return False
        else:
            high=delta[k+1] if k+1<=p else 0
            if b*k*delta[k]+(k+1)*(t-k)*high:
                return False
    return True

def predicted_difference(delta,t,p,a,b):
    ans=[0]*(p+1)
    if t==0:return ans
    for d in range(1,min(t,p)+1):
        for mark in (0,1):
            x=t-d-mark
            if x<0 or x%2:continue
            r=x//2
            ans[p-d+mark]+=factorial(d)*delta[d]*comb(t-1,d-1)*a**(r+mark)*b**r
    return ans

def fixed_operator_witness(T,a=1,b=2):
    assert T>=3 and T%2==1
    A=(1,2*T+1);B=(2,T+1)
    delta=[x-y for x,y in zip(elementary(A),elementary(B))]
    assert delta==[0,T-1,-1]
    YA,ta=observe(A,a,b,T+3)
    YB,tb=observe(B,a,b,T+3)
    for t in range(T+4):
        diff=[x-y for x,y in zip(YA[t],YB[t])]
        assert diff==predicted_difference(delta,t,2,a,b)
        assert (not any(diff))==(t==0 or t==T)
        if t>=2 and t%2==0:
            assert diff[2]==a*(T-1)*(a*b)**((t-2)//2)
            assert diff[0]==-2*(t-1)*(a*b)**((t-2)//2)
        if t>=3 and t%2==1:
            assert diff[1]==a*(a*b)**((t-3)//2)*(b*(T-1)-2*(t-1))
    return {"T":T,"a":a,"b":b,"A":list(A),"B":list(B),
            "delta_e":delta,"equal_histogram_at_T":YA[T],
            "histogram_at_T_plus_1_A":YA[T+1],
            "histogram_at_T_plus_1_B":YB[T+1],
            "named_transition_updates":ta+tb}

def exhaustive():
    pair_cases=0;time_checks=0;future_checks=0;first_index_checks=0;transitions=0;recollisions=[]
    for p in range(1,4):
        profiles=list(combinations_with_replacement(range(1,6),p))
        for a in (1,2):
            for b in (1,4,8,12,16):
                results={}
                for profile in profiles:
                    results[profile],ts=observe(profile,a,b,12)
                    transitions+=ts
                for A,B in combinations(profiles,2):
                    delta=[x-y for x,y in zip(elementary(A),elementary(B))]
                    n=next(i for i in range(1,p+1) if delta[i])
                    pair_cases+=1
                    YA,YB=results[A],results[B]
                    seen=[]
                    for t in range(13):
                        actual=[x-y for x,y in zip(YA[t],YB[t])]
                        assert actual==predicted_difference(delta,t,p,a,b)
                        equal=not any(actual)
                        assert equal==full_criterion(delta,n,t,b,p),(p,A,B,a,b,t,delta)
                        time_checks+=1
                        if t>=n:
                            future_checks+=1
                            if (t-n)%2:assert not equal;first_index_checks+=1
                            if equal:seen.append(t)
                    assert len(seen)<=1
                    if seen and len(recollisions)<8:
                        recollisions.append({"p":p,"A":list(A),"B":list(B),"a":a,"b":b,"t":seen[0],"delta":delta})
    return {"unordered_profile_pairs_with_parameter_choices":pair_cases,
            "complete_histogram_time_comparisons":time_checks,
            "post_first_separation_time_comparisons":future_checks,
            "forced_noncoincidence_checks":first_index_checks,
            "named_state_transition_updates":transitions,
            "sample_recollisions":recollisions}

if __name__=='__main__':
    w=[fixed_operator_witness(T) for T in (3,5,7,11,21)]
    d=exhaustive()
    print(json.dumps({"status":"ALL_EXACT_ASSERTIONS_PASSED",
        "scope":"q=p, full initial occupancy, absent mark, distinct named unmarked sources, Q=R+A",
        "arithmetic":"arbitrary-precision Python integers; independent named-mask DP",
        "fixed_operator_witness_family":w,"exhaustive_parameter_grid":d},indent=2,ensure_ascii=False))
