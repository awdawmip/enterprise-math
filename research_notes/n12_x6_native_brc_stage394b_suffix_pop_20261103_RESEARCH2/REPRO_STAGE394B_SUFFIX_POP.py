#!/usr/bin/env python3
"""Stage394-B: finite-POP horizon exact suffix theorem and signed-X6 BRC tests.
Scientific source pinned to Enterprise Math 2af3fc484eb11060b69e0afc1b562bcaf5ad1419.
All paths are typed Path-formal; POP is NOT physical Cell reversal.
"""
from __future__ import annotations
from collections import defaultdict
from functools import lru_cache
from itertools import combinations, product
from math import factorial
import json

A = tuple((i,s) for i in range(6) for s in (1,-1))
B = A[:4]  # finite exhaustive test subalphabet; X6 endpoint BRC still has 12 labels
ZERO = (0,)*6


def step(d):
    v = [0]*6
    v[d[0]] = d[1]
    return tuple(v)


def endpoint(w):
    out = [0]*6
    for i, sign in w:
        out[i] += sign
    return tuple(out)


def turns(w):
    return sum(w[j]!=w[j-1] for j in range(1,len(w)))


def comps(n, dim):
    if dim == 1:
        yield (n,)
    else:
        for k in range(n+1):
            for tail in comps(n-k,dim-1):
                yield (k,)+tail


@lru_cache(None)
def native_N(m,z):
    r = sum(abs(x) for x in z)
    if m < r or (m-r)%2:
        return 0
    K = (m-r)//2
    from fractions import Fraction
    ans = Fraction(0)
    for ks in comps(K,6):
        denom=1
        for zi,k in zip(z,ks):
            denom *= factorial(max(zi,0)+k)*factorial(max(-zi,0)+k)
        ans += Fraction(factorial(m),denom)
    assert ans.denominator==1
    return int(ans)


def obs(w):
    z=endpoint(w)
    triples=[]
    for ids in combinations(range(6),3):
        v=[z[i] for i in ids]
        q=min(v)
        triples.append(tuple(x-q for x in v))
    return (tuple(triples),min(z),len(w),native_N(len(w),z),turns(w))


def suffix(w,H):
    return tuple(w[-(H+1):])


def operate(w,op):
    if op[0]=='POP':
        assert w
        return w[:-1]
    assert op[0]=='APPEND'
    return w+(op[1],)


def compressed_init(w,H):
    z=endpoint(w)
    return (z,len(w),turns(w),suffix(w,H),H)


def compressed_update(state,op):
    z,m,t,tail,r=state
    if op[0]=='POP':
        assert r>=1 and m>=1 and tail
        last=tail[-1]
        penult=tail[-2] if m>=2 else None
        newz=tuple(x-y for x,y in zip(z,step(last)))
        newt=t-int(m>=2 and penult!=last)
        r-=1
        newtail=tail[:-1]
        return newz,m-1,newt,newtail,r
    d=op[1]
    newz=tuple(x+y for x,y in zip(z,step(d)))
    newt=t+int(m>=1 and tail[-1]!=d)
    newtail=(tail+(d,))[-(r+1):]
    return newz,m+1,newt,newtail,r


def apply_trace(w,ops):
    trace=[]
    for op in ops:
        w=operate(w,op)
        trace.append(obs(w))
    return trace


def distinguish(w,v,H):
    assert obs(w)==obs(v) and suffix(w,H)!=suffix(v,H)
    m=len(w)
    j=next(k for k in range(1,min(m,H+1)+1) if w[-k]!=v[-k])
    if j<=H:
        ops=(('POP',),)*j
        assert apply_trace(w,ops)!=apply_trace(v,ops)
        return ops
    assert j==H+1
    ops=(('POP',),)*H
    if apply_trace(w,ops)!=apply_trace(v,ops):
        return ops
    ops=ops+(('APPEND',w[-(H+1)]),)
    assert apply_trace(w,ops)!=apply_trace(v,ops)
    return ops


def bounded_pair_test():
    fibers=defaultdict(list)
    for m in range(0,6):
        for w in product(B,repeat=m):
            fibers[obs(w)].append(w)
    equal=unequal=0
    counts={}
    for H in range(0,5):
        e=u=0
        for words in fibers.values():
            for i,w in enumerate(words):
                for v in words[i+1:]:
                    if suffix(w,H)==suffix(v,H):
                        e+=1
                    else:
                        distinguish(w,v,H)
                        u+=1
        counts[str(H)]={'same_suffix_pairs':e,'distinguished_pairs':u}
        equal+=e
        unequal+=u
    return {'test_alphabet':len(B),'max_length':5,'fibers':len(fibers),'per_H':counts,'pair_assertions':equal+unequal}


def bounded_dynamic_test():
    total=0
    for m in range(0,4):
        for w in product(B,repeat=m):
            for H in range(0,3):
                state0=compressed_init(w,H)
                assert state0[:3]==(endpoint(w),len(w),turns(w))
                assert len(state0[3])==min(len(w),H+1)
                agenda=[(w,state0,())]
                for depth in range(4):
                    nxt=[]
                    for actual,state,ops in agenda:
                        assert state[:3]==(endpoint(actual),len(actual),turns(actual))
                        assert state[3]==suffix(actual,state[4])
                        assert native_N(state[1],state[0])==obs(actual)[3]
                        total+=1
                        if depth<3:
                            choices=[('APPEND',d) for d in B]
                            if state[4]>0 and len(actual)>0:
                                choices.append(('POP',))
                            for op in choices:
                                nxt.append((operate(actual,op),compressed_update(state,op),ops+(op,)))
                    agenda=nxt
    return total


def brc_endpoint_check():
    dp={ZERO:1}
    comparisons=0
    visited=0
    for m in range(0,6):
        for z,value in dp.items():
            assert value == native_N(m,z)
            comparisons+=1
        if m==5:break
        nxt=defaultdict(int)
        for z,v in dp.items():
            for d in A:
                sd=step(d)
                nxt[tuple(a+b for a,b in zip(z,sd))]+=v
                visited+=1
        dp=dict(nxt)
    return comparisons,visited


def family_test():
    E1=(0,1); ME1=(0,-1)
    for n in range(1,6):
        common=None
        unique=set()
        for axis_choices in product(range(6),repeat=n):
            blocks=sum((((axis,1),(axis,-1)) for axis in axis_choices),())
            w=(ME1,)+blocks+(E1,)
            o=obs(w)
            if common is None: common=o
            assert o==common
            unique.add(suffix(w,2*n))
        assert len(unique)==6**n
    return 5


def main():
    pair=bounded_pair_test()
    transitions=bounded_dynamic_test()
    checks,visited=brc_endpoint_check()
    fam=family_test()
    report={'stage':'394-B','source_em_pin':'2af3fc484eb11060b69e0afc1b562bcaf5ad1419','P000_blob':'bcc2590d3168a28f72e8b9f0f9b1f76faadcd488', 'alphabet_size':12,'bounded_pairs':pair,'dynamic_state_assertions':transitions,'native_BRC_endpoint_checks':checks,'native_BRC_dp_edges':visited,'six_choice_exponential_family_n_max':fam, 'scope':'signed-X6 ordered Path-formal APPEND/POP; at most H total POPs; observer includes 20 triple readouts, h, m, N_m, turns','status':'PASS'}
    print(json.dumps(report,ensure_ascii=False,sort_keys=True,separators=(',',':')))
    print('STAGE394B_SHARP_SUFFIX_MEMORY_PASS')

if __name__=='__main__':main()
