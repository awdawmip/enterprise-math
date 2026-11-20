#!/usr/bin/env python3
"""Exact q=-1 pole test for the frozen R5 five-set failure model."""
from fractions import Fraction
from functools import lru_cache
from math import comb, prod
from pathlib import Path
import hashlib, json

PIN='50e87f0194cfb3780e84b7bbb6f9a2dca4f79bb4901cab06f1a5b59256fb470b'
P=tuple(range(214,315))
S=[
    tuple(range(214,219)),
    (214,216,217,218,219,220,221),
    tuple(range(215,222)),
    tuple(range(223,291)),
    tuple(range(296,313))
]
E0=tuple(p for p in P if p not in S[0])
E2=tuple(p for p in P if p not in S[2])

def signed_numerator(prices,m):
    a=[1]+[0]*(m-1)
    for p in prices:
        sign=-1 if p%2 else 1
        b=[0]*m
        for n in range(m):
            b[n]=a[n]+(sign*b[n-1] if n else 0)
        a=b
    return sum(a)

def direct(prices,m):
    @lru_cache(None)
    def rec(i,left):
        if i==len(prices):return 1
        return sum((-1 if prices[i]%2 else 1)**n * rec(i+1,left-n)
                   for n in range(left+1))
    return rec(0,m-1)

def a_closed(m):
    return sum((j+1)*(m-2*j) for j in range((m-1)//2+1))

def b_closed(m):
    return comb((m-1)//2+3,3) if m%2 else 0

def leading_constant(m):
    Q=prod(p for p in range(222,315,2))
    return Fraction(a_closed(m),2**48*220*Q)+Fraction(b_closed(m),2**46*214*Q)

def pole_table():
    sets=[set(S[0]),set(S[1]),set(S[2]),set(range(214,222)),
          set(S[4]),set(S[0]+S[4]),set(S[1]+S[4]),set(S[2]+S[4]),
          set(tuple(range(214,222))+S[4]),set(S[3])]
    names=['G0','G1','G2','-Gh','G4','-G04','-G14','-G24','+Gh4','A3']
    return [{'event':name,'free':sum(p not in t for p in P),
             'even_free':sum(p not in t and p%2==0 for p in P)}
            for name,t in zip(names,sets)]

def main():
    f=Path(__file__).with_name('EXACT_R5_ALL_101_BUDGETS.json')
    frozen=hashlib.sha256(f.read_bytes()).hexdigest() if f.exists() else None
    if frozen is not None: assert frozen==PIN
    rows=[]
    for m in range(1,121):
        x=signed_numerator(S[0],m)
        y=signed_numerator(S[2],m)
        assert (x,y)==(a_closed(m),b_closed(m))
        assert leading_constant(m)>0
        if m<=5:
            assert x==direct(S[0],m)
            assert y==direct(S[2],m)
        if m in (1,2,3,4,5,8,17,32,120):
            rows.append({'m':m,'a':x,'b':y,
                         'C_over_C1':str(leading_constant(m)/leading_constant(1))})
    events=pole_table()
    assert [r['event'] for r in events if r['even_free']==48]==['G0','G2']
    assert len(E0)==96 and len(E2)==94
    assert (sum(p%2 for p in E0),sum(p%2 for p in E2))==(48,46)
    payload={'schema':'R5_PARITY_LEADING_ALL_M_V1','frozen_sha256':PIN,
             'frozen_input_verified_if_local':frozen==PIN,'samples':rows,
             'events':events,'test_m_1_to_120':True,'direct_m_1_to_5':True,
             'independent_review':'NOT_REVIEWED'}
    target=Path(__file__).with_name('RESULT_PARITY_ALL_M.json')
    target.write_text(json.dumps(payload,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({'verified':True,'frozen':frozen,'rows':len(rows)},
                     ensure_ascii=False))

if __name__=='__main__':main()
