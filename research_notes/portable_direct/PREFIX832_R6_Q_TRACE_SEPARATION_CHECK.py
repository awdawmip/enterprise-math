#!/usr/bin/env python3
"""Exact independent named-state BRC-Q regression; standard Python integers only."""
from math import comb, factorial
from collections import defaultdict
import json

A7=[1,19,28,59,65,90,102]
B7=[2,14,39,45,76,85,103]
A10=[1,13,126,214,215,413,414,502,615,627]
B10=[6,7,134,183,243,385,445,494,621,622]
A12=[1,12,25,66,91,130,174,213,238,279,292,303]
B12=[4,6,31,58,105,117,187,199,246,273,298,300]
A16=[2,18,49,54,79,111,113,116,143,175,187,190,206,246,251,276]
B16=[1,26,31,71,87,90,102,134,161,164,166,198,223,228,259,275]


def elementary(weights):
    e=[1]+[0]*len(weights)
    for j,w in enumerate(weights,1):
        for k in range(j,0,-1):e[k]+=w*e[k-1]
    return e


def predicted(t,p,delta,a=2,b=3):
    result=[0]*(p+1)
    if t==0:return result
    for d in range(1,min(t,p)+1):
        for mark in (0,1):
            n=t-d-mark
            occupancy=p-d+mark
            if n<0 or n%2 or occupancy>p:continue
            r=n//2
            result[occupancy]+=factorial(d)*delta[d]*comb(t-1,d-1)*(a**(r+mark))*(b**r)
    return result


def named_histograms(weights, max_t, a=2,b=3):
    p=len(weights)
    full=(1<<p)-1
    state={(full,0):1}
    hist=[]
    transitions=0
    for t in range(max_t+1):
        obs=[0]*(p+1)
        for (mask,mark),mass in state.items():
            obs[mask.bit_count()+mark]+=mass
        hist.append(obs)
        if t==max_t: break
        next_state=defaultdict(int)
        for (mask,mark),mass in state.items():
            bits=mask
            while bits:
                bit=bits&-bits
                i=bit.bit_length()-1
                next_state[(mask^bit,mark)]+=mass*weights[i]
                bits-=bit
                transitions+=1
            if mark:
                next_state[(mask,0)]+=mass*b
                transitions+=1
            elif mask.bit_count()<p:
                next_state[(mask,1)]+=mass*a
                transitions+=1
        state=next_state
    return hist,transitions


def run_case(name,A,B,max_t,a=2,b=3):
    assert len(A)==len(B) and all(x>0 for x in A+B)
    p=len(A)
    eA=elementary(A); eB=elementary(B)
    delta=[x-y for x,y in zip(eA,eB)]
    n=next(i for i,x in enumerate(delta) if x)  # first nonzero
    D=max(i for i,x in enumerate(delta) if x)
    observed_A,trans_A=named_histograms(A,max_t,a,b)
    observed_B,trans_B=named_histograms(B,max_t,a,b)
    comparisons=0
    for t in range(max_t+1):
        direct=[x-y for x,y in zip(observed_A[t],observed_B[t])]
        expected=predicted(t,p,delta,a,b)
        assert direct==expected,(name,t,'full recurrence mismatch',direct,expected)
        comparisons+=p+1
        if t<n:assert all(x==0 for x in direct)
        if t==n:
            assert direct[p-n]==factorial(n)*delta[n]
            assert sum(x!=0 for x in direct)==1
        if t>=D and (t-D)%2==0:
            assert direct[p-D]==factorial(D)*delta[D]*comb(t-1,D-1)*(a*b)**((t-D)//2)
            assert direct[p-D]!=0
        if t>=D+1 and (t-D)%2==1:
            m=(t-D-1)//2
            witness=factorial(D)*delta[D]*comb(t-1,D-1)*a*(a*b)**m
            if D>=2:
                witness+=factorial(D-1)*delta[D-1]*comb(t-1,D-2)*(a*b)**(m+1)
            assert direct[p-D+1]==witness
    return {'case':name,'p':p,'a':a,'b':b,'first_difference_n':n,'last_nonzero_D':D,
            'delta_e_n':str(delta[n]),'delta_e_D':str(delta[D]),
            'checked_t':list(range(max_t+1)), 'full_histogram_scalar_comparisons':comparisons,
            'named_state_transition_updates':trans_A+trans_B,
            'last_step_difference_bins':[i for i,v in enumerate(predicted(max_t,p,delta,a,b)) if v!=0]}

if __name__=='__main__':
    results=[run_case('ideal_7',A7,B7,16),run_case('ideal_10',A10,B10,17),
             run_case('ideal_12',A12,B12,17),run_case('nonideal_16',A16,B16,17),
             run_case('exact_recollision_p2',[1,6],[3,3],7,2,12)]
    assert named_histograms([1,6],3,2,12)[0][3]==named_histograms([3,3],3,2,12)[0][3]==[0,216,0]
    data={'result':'ALL_EXACT_ASSERTIONS_PASSED','arithmetic':'Python exact integers, no floating point',
          'scope':'q=p, saturated absent mark, named positive source weights, Q=R+A, per-case a and b',
          'results':results,
          'total_histogram_scalar_comparisons':sum(x['full_histogram_scalar_comparisons'] for x in results),
          'total_named_transition_updates':sum(x['named_state_transition_updates'] for x in results)}
    print(json.dumps(data,ensure_ascii=False,indent=2))
