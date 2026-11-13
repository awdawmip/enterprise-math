#!/usr/bin/env python3
"""Exact S23/AV R24 extension: all integer cut counts through n=15000.
Runs the original published VERIFY_R24.py integer-affine engine at larger N.
"""
import VERIFY_R24 as m
from fractions import Fraction
from pathlib import Path
from hashlib import sha256

EXPECTED = [
 (7622,7687,(-854,3257)),
 (7688,7723,(0,0)),
 (7724,7784,(-854,3257)),
 (7785,10877,(0,0)),
 (10878,10944,(-854,3257)),
 (10945,10980,(0,0)),
 (10981,11041,(-854,3257)),
 (11042,14134,(0,0)),
 (14135,14201,(2895,-11041)),
 (14202,14237,(0,0)),
 (14238,14298,(2895,-11041)),
 (14299,15000,(0,0))
]

def run():
    m.N=15000
    r, rows, order_tests, maximum_tests = m.build()
    assert r[7621]==(-43477,165817)
    ep=[]
    for item in rows:
        n=item['t']+1
        if n<=7621: continue
        d=item['delta']
        if ep and ep[-1][1] == n-1 and ep[-1][2] == d:
            start,_,delta=ep[-1];ep[-1]=(start,n,delta)
        else:ep.append((n,n,d))
    assert ep==EXPECTED,(ep,EXPECTED)
    for a,b,d in ep:
        if d!=(0,0):m.certify_positive(d)
    assert r[14134]==(-261247,996352)
    assert r[14298]==r[15000]==(109313,-416896)
    comparisons=(7621,7687,7688,7723,7724,7784,7785,9000,10877,
        10878,10944,10945,10980,10981,11041,11042,14134,14135,
        14201,14202,14237,14238,14298,14299,15000)
    for n in comparisons:
        assert r[n]==m.direct_partition(n),('independent',n,r[n])
    print('FROZEN_PIN enterprise-math@43ec6098b1330ae86d0a7863be336c5d97f6ef34')
    print('EXACT_SUBINTERVAL',m.THETA_LOW,m.THETA_HIGH)
    print('EXACT_UPDATES',m.N-m.M,'THROUGH',m.N,'ORDER_SIGN_TESTS',order_tests,'MAX_SIGN_TESTS',maximum_tests)
    print('EXTENDED_EPOCHS',len(ep),'DIRECT_FULL_PARTITIONS',len(comparisons))
    for a,b,d in ep:
        print('EPOCH',a,b,'count',b-a+1,'delta',d,'risk_after',r[b])
    print('PASS_R24_EXACT_EXTENSION_THROUGH_15000')

if __name__=='__main__':run()
