#!/usr/bin/env python3
"""R259 exact positive-BRC branch check for frozen R258 model; not native import."""
from collections import Counter,defaultdict
from itertools import product
import json
E=(((2,-1,-1),(2,1,-1)),((0,-1,-1),(0,1,-1)),((1,1,1),(2,1,-1)))
D=((1,0),(2,0),(2,2))
B={7:('1110101','1011010','0000000'),
   8:('11110101','10111010','00011010'),
   9:('101101011','010101010','000000011')}
P='101'; U='1011101'; V='1101101'
def go(q,r,s,k,a):
    t,e,b=E[q][a]
    return t,D[r][a],e*s,e*k+b
def word(w):
    v=(0,0,1,0)
    for x in w: v=go(*v,int(x))
    return v
def next_hist(h):
    y=Counter()
    for (q,r,s,k),cnt in h.items():
        for a in (0,1): y[go(q,r,s,k,a)]+=cnt
    return y
def params(m):
    j=7+(m-7)%3;h=(m-j)//3;K,rem=divmod(h,7)
    return j,K,rem,{7:1,8:2,9:-1}[j]+9*K+rem
def verify():
    assert word(P)==(0,0,1,-1)
    assert word(U)==word(V)==(0,0,1,-3)
    for j,words in B.items():
        assert all(word(w)==(2,r,-1,{7:1,8:2,9:-1}[j])
                   for r,w in enumerate(words))
    h=Counter({(0,0,1,0):1});first=None; samples={}
    for m in range(129):
        assert sum(h.values())==2**m
        fibres=defaultdict(set)
        for q,r,s,k in h: fibres[q,s,k].add(r)
        if first is None and any(len(x)==3 for x in fibres.values()): first=m
        if m<=12:
            brute=Counter(word(''.join(w)) for w in product('01',repeat=m))
            assert brute==h
        if m>=7:
            j,K,rem,b=params(m)
            c=[h.get((2,r,-1,b),0) for r in range(3)]
            assert min(c)>=2**(3*K),(m,c)
            if m in (7,8,9,28,49,70,91,112,128):
                samples[str(m)]={'DFA_counts':[str(x) for x in c],
                                 'lower_bound_each':str(2**(3*K)),
                                 'fiber_offset':b}
        h=next_hist(h)
    assert first==7
    for m in list(range(7,85))+[91,112,128,257,511]:
        j,K,rem,b=params(m)
        p=U*(3*K)+P*rem
        for r,w in enumerate(B[j]):
            a=p+w
            assert len(a)==m and word(a)==(2,r,-1,b)
            if K:
                v=V+U*(3*K-1)+P*rem+w
                assert v!=a and word(v)==word(a)
    return {'status':'PASS','model':'R258 scoped positive BRC',
            'native_package_executed':False,
            'first_three_mode_fiber':first,
            'exact_dynamic_depth':'0..128','enumerated_raw_depth':'0..12',
            'proof_all_m_ge_7': 'j=7+(m-7)%3; m=j+21K+3r',
            'fiber_lower_bound_each_DFA':'2^(3K)',
            'samples':samples}
if __name__=='__main__': print(json.dumps(verify(),sort_keys=True,indent=2))
