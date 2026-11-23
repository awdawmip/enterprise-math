#!/usr/bin/env python3
"""EC49FXU exact genuine-anchor census under frozen BRC16943; standard library."""
from collections import Counter, defaultdict
from itertools import product
from math import gcd
import json

SLOPES = {(0,0): {3}, (0,1): {0,3,4,5},
          (1,0): {2,3,4,5}, (1,1): {2,3}}

def p10(h,n):
    h,n = h%10,n%10
    if h%5 == n%5 == 0:
        return False
    s = 5 if h%5 == 0 else n*pow(h,-1,5)%5
    return s in SLOPES[(h%2,n%2)]

def representatives():
    result = {}
    for a,c in product(range(10),repeat=2):
        if gcd(gcd(a,c),10) != 1: continue
        x,y = next((x,y) for x,y in product(range(10),repeat=2)
                   if (c*x-a*y+1)%10 == 0)
        u = sum(int(p10(x+a*t,y+c*t))<<t for t in range(10))
        result[(a,c)] = (x,y,u)
    assert len(result)==72 and len({x[2] for x in result.values()})==50
    return result

def normalize(a,c,reps):
    assert a>0 and c>0 and gcd(a,c)==1
    b=a+c
    e=pow(a,-1,b)
    h=(a*e-1)//b; n=e-h
    x,y,u=reps[(a%10,c%10)]
    t0=next(t for t in range(10) if (h+a*t-x)%10==(n+c*t-y)%10==0)
    l0=9*(h+a*t0)+10*(n+c*t0)
    l1=9*a+10*c
    hole=None if l1%11==0 else (-l0*pow(l1,-1,11))%11
    return (u,hole),(a,b,t0)

def direct(a,b,t0,t):
    c=b-a; e=pow(a,-1,b)
    h=(a*e-1)//b+a*(t0+t)
    n=e-(a*e-1)//b+c*(t0+t)
    return int(p10(h,n) and (9*h+10*n)%11 != 0)

def product_bit(u,hole,t):
    return int(bool(u&(1<<(t%10))) and (hole is None or t%11!=hole))

def spectrum(u,hole):
    A={i for i in range(10) if (u>>i)&1}
    B=set(range(11)) if hole is None else set(range(11))-{hole}
    return tuple(2*(len(A)*len(B)-
      sum(i in A and (s-i)%10 in A for i in range(10))*
      sum(j in B and (t-j)%11 in B for j in range(11)))
      for s in range(10) for t in range(11))

def main():
    reps=representatives()
    witnesses={}
    for a,c in product(range(1,80),repeat=2):
        if gcd(a,c)==1:
            state,anchor=normalize(a,c,reps)
            witnesses.setdefault(state,anchor)
    small={normalize(a,c,reps)[0] for a,c in product(range(1,79),repeat=2)
           if gcd(a,c)==1}
    assert len(witnesses)==600 and len(small)==599
    assert set(witnesses)-small=={(788,5)}
    assert len({u for u,z in witnesses})==50
    for (u,z),(a,b,t0) in witnesses.items():
        assert all(direct(a,b,t0,t)==product_bit(u,z,t)
                   for t in range(110))
    fibers=defaultdict(list)
    for state in witnesses:
        fibers[spectrum(*state)].append(state)
    assert len(fibers)==478
    assert Counter(map(len,fibers.values()))=={1:356,2:122}
    supports=Counter(); example={}
    for fiber in fibers.values():
        if len(fiber)==2:
            (u,z),(v,zz)=fiber
            assert z==zz
            support=tuple(j for j in range(10) if (u^v)&(1<<j))
            supports[support]+=1
            example.setdefault(support,[(*s,*witnesses[s]) for s in fiber])
    assert len(supports)==7
    minimal={"A":(1,4,6,9),"B":(2,7),"C":(3,8)}
    return {
      "result":"ALL PASS",
      "frozen_science":"BRC16943",
      "normalization":"lexicographic determinant-minus-one mod10 representative; t0 in 0..9",
      "bound_a_and_c":79,"bound_78_states":len(small),
      "bound_79_states":len(witnesses),
      "only_new_state_at_79":{"u":788,"hole":5,"anchor":witnesses[(788,5)]},
      "direct_trace_bit_checks":600*110,
      "mask_count":50,"factor_count":12,
      "indexed_spectra":len(fibers),
      "fiber_size_histogram":{"1":356,"2":122},
      "difference_support_histogram":{"-".join(map(str,k)):v for k,v in sorted(supports.items())},
      "minimal_support_examples":{name:example[s] for name,s in minimal.items()},
      "witnesses":[{"u":u,"hole":z,"a":a,"b":b,"t0":t0}
          for (u,z),(a,b,t0) in sorted(
            witnesses.items(),key=lambda item:(item[0][0],
                  -1 if item[0][1] is None else item[0][1]))],
      "scope":"Farey determinant-one C11 auxiliary observer; not native Heartbeat X6"
    }

if __name__=="__main__":
    print(json.dumps(main(),ensure_ascii=False,sort_keys=True,indent=2))
