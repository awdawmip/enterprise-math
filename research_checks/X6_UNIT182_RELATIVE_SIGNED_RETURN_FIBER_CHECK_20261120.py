#!/usr/bin/env python3
"""Exact integer checks for six signed native axes and derived min-zero observer.

Exhaustive over all endpoint paths of lengths 0..8 by integer dynamic programming;
independent multinomial endpoint count by nonnegative pair-composition sums.
This is author checking, not native R063 benchmark execution.
"""
from collections import defaultdict
from itertools import product
from math import factorial
import json
import hashlib

DIM=6
ZERO=(0,)*DIM

def can6(z):
    minimum=min(z)
    return tuple(x-minimum for x in z)

def count_signed_endpoints(length):
    state={ZERO:1}
    states_by_length=[state]
    for step in range(1,length+1):
        new=defaultdict(int)
        for z,multiplicity in state.items():
            for i in range(DIM):
                for sign in (-1,1):
                    a=list(z)
                    a[i]+=sign
                    new[tuple(a)]+=multiplicity
        state=dict(new)
        states_by_length.append(state)
    return states_by_length

def compositions(n,k):
    if k==1:
        yield (n,)
    else:
        for x in range(n+1):
            for rest in compositions(n-x,k-1):
                yield (x,)+rest

def exact_native_count(length,z):
    minimum=sum(map(abs,z))
    if length<minimum or (length-minimum)%2:
        return 0
    K=(length-minimum)//2
    numerator=factorial(length)
    result=0
    for c in compositions(K,DIM):
        denominator=1
        for zi,ki in zip(z,c):
            denominator*=factorial(max(zi,0)+ki)*factorial(max(-zi,0)+ki)
        if numerator%denominator != 0: raise ArithmeticError("multinomial integrality")
        result+=numerator//denominator
    return result

def relative_count_formula(length,a):
    if len(a)!=DIM or any(x<0 for x in a) or min(a)!=0: raise ValueError("not canonical can6")
    # A zero coordinate of a is equal to h in z=a+h1: |h|<=length for reachable states.
    return sum(exact_native_count(length,tuple(v+h for v in a)) for h in range(-length,length+1))

def main():
    profiles=[]
    comparisons=0
    max_states=0
    states_by_length=count_signed_endpoints(8)
    for M,states in enumerate(states_by_length):
        max_states=max(max_states,len(states))
        if sum(states.values()) != 12**M: raise ArithmeticError("word mass conservation")
        relative=defaultdict(int)
        for z,count in states.items():
            relative[can6(z)]+=count
            # independent convolution count for every native endpoint
            exact=exact_native_count(M,z)
            if exact!=count:
                raise ValueError(('native',M,z,exact,count))
            comparisons+=1
        if sum(relative.values())!=12**M:
            raise ValueError(('mass',M))
        # Exact group-level projection of the entire length-M signed walk population
        for a,count in relative.items():
            actual=relative_count_formula(M,a)
            if actual!=count:
                raise ValueError(('fiber',M,a,actual,count))
            comparisons+=1
        native_return=states.get(ZERO,0)
        observed_return=relative.get(ZERO,0)
        leak=observed_return-native_return
        if M%2 or M<6:
            if leak != 0: raise AssertionError("early diagonal return leakage")
        if M==6:
            if native_return!=19920: raise AssertionError("native length-six return")
            if leak!=1440: raise AssertionError("six-step diagonal leakage")
            if observed_return!=21360: raise AssertionError("six-step relative return")
        profiles.append({"events":M,"native_return":native_return,"relative_observer_return":observed_return,"lost_diagonal_lift_count":leak,"native_endpoints":len(states),"relative_fibers":len(relative)})
    # For all k=1..4, distinct all-positive and all-negative all-axis shortest paths are
    # nonnative spatial returns but observer returns in the positive-min-zero quotient.
    for k in range(1,5):
        m=6*k
        extremal=factorial(m)//(factorial(k)**6)
        if exact_native_count(m,(k,)*DIM)!=extremal: raise AssertionError("positive extremal lift")
        if exact_native_count(m,(-k,)*DIM)!=extremal: raise AssertionError("negative extremal lift")
    certificate={"schema":"X6_UNIT182_RELATIVE_SIGNED_RETURN_FIBER_CERTIFICATE_V1","observation_model":"signed native Z6 nearest-axis words; derived min-zero can6 observer","source_frozen_scientific_pin":"59538f585d037d09ef687b28715c4bc1a3f9fe03","source_historical_commit":"fd2bcff10ca6e147348b6c1236027fc0d2877df3","scope":"exhaustive all path lengths 0..8 exact integer DP and independent multinomial composition formula; k<=4 extremal lift certificates","native_and_relative_count_comparisons":comparisons,"max_native_endpoint_support":max_states,"profiles":profiles,"pass":True,"formal_review":"UNREVIEWED / NOT_ADMITTED"}
    return certificate

if __name__=='__main__':
    result=main()
    print(json.dumps(result,ensure_ascii=False,sort_keys=True,indent=2))
