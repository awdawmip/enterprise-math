#!/usr/bin/env python3
"""Certify first strict increase of S23/AV R(128,L) after L=200000.

Dependencies: VERIFY_FAREY_GAP_RISK.py (same directory).
"""
from VERIFY_FAREY_GAP_RISK import risk, M, LOW, HIGH, certify_theta
from functools import lru_cache

@lru_cache(None)
def value(L):
    return risk(M,M+L)[0]

def sign_diff(x,y):
    a,b=x[0]-y[0],x[1]-y[1]
    if a==0 and b==0: return 0
    left=a+b*LOW
    right=a+b*HIGH
    assert (left>0 and right>0) or (left<0 and right<0)
    return 1 if left>0 else -1

def run():
    certify_theta()
    baseline=value(200000)
    assert baseline==(479873,-1830144)
    left,right=200000,400000
    assert sign_diff(value(right),baseline)>0
    while right-left>1:
        middle=(left+right)//2
        if sign_diff(value(middle),baseline)>0:
            right=middle
        else:
            left=middle
    assert left==322048 and right==322049
    assert value(left)==baseline
    assert value(right)==(520258,-1984165)
    delta=(value(right)[0]-baseline[0],value(right)[1]-baseline[1])
    assert delta==(40385,-154021)
    assert delta[0]+delta[1]*LOW>0 and delta[0]+delta[1]*HIGH>0
    print('CERTIFIED_PLATEAU',200001,left)
    print('FIRST_POSITIVE',right,'DELTA',*delta)
    print('LEFT_R',*value(left),'RIGHT_R',*value(right))
    print('FLOOR_SUM_QUERIES',value.cache_info().misses)
    print('PASS_FIRST_INCREMENT_AFTER_200000')
if __name__=='__main__': run()
