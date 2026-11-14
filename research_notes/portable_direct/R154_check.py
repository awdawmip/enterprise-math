#!/usr/bin/env python3
"""R154: exact full-count alias certificate for equal rational endpoint denominators.
External S23 scalar observer only. Pure integer arithmetic, no numerical tolerance.
"""
from math import gcd
import json


def ceildiv(n,d):return -((-n)//d)
def C(L,a,b,c,U,V):
    return ceildiv(c*L-V,b)-(a*L-U)//b-1

def S(b,t,a,U):
    inv=pow(a,-1,b)
    return frozenset((inv*(U+j))%b for j in range(t))

def alias(b,a,c,U,V,t):
    return S(b,t,a,U)==S(b,t,c,V+1)

def enumerate_endpoints(max_b=18):
    endpoint_pairs=0; cut_states=0; positive_shift_tests=0; equality_cases=0; universal_edges=0; full_recheck=0
    for b in range(3,max_b+1):
        for a in range(1,b):
            if gcd(a,b)!=1: continue
            for c in range(a+1,b):
                if gcd(c,b)!=1: continue
                endpoint_pairs+=1
                for U in range(b):
                    for V in range(b):
                        cut_states+=1
                        for t in range(b):
                            expected=alias(b,a,c,U,V,t)
                            observed=all(C(L,a,b,c,U+t,V+t)==C(L,a,b,c,U,V) for L in range(b))
                            assert observed==expected,(b,a,c,U,V,t,expected,observed)
                            positive_shift_tests+=1
                            equality_cases+=expected
                        universal=(c*U-a*(V+1))%b==0
                        observed=all(C(L,a,b,c,U+1,V+1)==C(L,a,b,c,U,V) for L in range(b))
                        assert observed==universal
                        universal_edges+=universal
                        r=-b+1
                        assert all(C(L,a,b,c,U+r,V+r)==C(L,a,b,c,U,V) for L in range(b)) == alias(b,a,c,U,V,1)
                        assert any(C(L,a,b,c,U+1,V+2)!=C(L,a,b,c,U,V) for L in range(b))
                        full_recheck+=2
    return dict(max_denominator=max_b, endpoint_pairs=endpoint_pairs,cut_states=cut_states,
                shift_set_checks=positive_shift_tests,exact_aliases=equality_cases,
                universal_unit_aliases=universal_edges, extra_checks=full_recheck)

def complement_family(max_b=32):
    cases=0; pairwise_collisions=0; count_waveforms=0
    for b in range(3,max_b+1):
        for a in range(1,b//2+1):
            if gcd(a,b)!=1:continue
            c=b-a
            if not a<c:continue
            maps={}
            for U in range(b):
                for V in range(b):
                    D=tuple(C(L+1,a,b,c,U,V)-C(L,a,b,c,U,V) for L in range(b))
                    maps.setdefault(D,[]).append((U,V))
                    cases+=1
            assert len(maps)==b*(b+1)//2,(a,b,len(maps))
            assert sorted(map(len,maps.values())).count(2)==b*(b-1)//2
            assert sorted(map(len,maps.values())).count(1)==b
            pairwise_collisions+=b*(b-1)//2
            count_waveforms+=len(maps)
    return dict(max_denominator=max_b,cut_states=cases,waveforms=count_waveforms,paired_aliases=pairwise_collisions)

def word_bounds(bits):
    m=len(bits); prefix=[0]
    for x in bits: prefix.append(prefix[-1]+x)
    an,ad,bn,bd=0,1,1,1
    for q in range(1,m+1):
        mn=m+1;mx=-1
        for i in range(m-q+1):
            t=prefix[i+q]-prefix[i]
            if t<mn:mn=t
            if t>mx:mx=t
        lo=mx-1;hi=mn+1
        if lo*ad>an*q: an,ad=lo,q
        if hi*bd<bn*q: bn,bd=hi,q
        if an*bd>=bn*ad: return None
    g=gcd(an,ad);an//=g;ad//=g
    g=gcd(bn,bd);bn//=g;bd//=g
    return an,ad,bn,bd

def words_check(max_m=16):
    rows=[]; num=0
    for m in range(1,max_m+1):
        valid=0; equal=[]
        for x in range(1<<m):
            word=tuple((x>>j)&1 for j in range(m))
            bounds=word_bounds(word)
            if bounds is None: continue
            valid+=1
            if bounds[1]==bounds[3] and bounds[1]>1:
                equal.append((''.join(map(str,word)),bounds))
        expected={'01'*(m//2),'10'*(m//2)} if m>=4 and m%2==0 else set()
        assert set(k for k,z in equal)==expected,(m,equal)
        assert len(equal)==len(expected),(m,equal)
        num+=valid
        rows.append(dict(m=m,valid_words=valid,equal_denominator_words=len(equal),examples=equal[:2]))
    return dict(max_m=max_m,total_valid=num,rows=rows)

def main():
    res={'result':'R154_EQUAL_DENOMINATOR_FULL_COUNT_ALIAS_CERTIFICATE_PASS',
         'arithmetic':'Python arbitrary-precision integers and modular arithmetic',
         'endpoint_sweep':enumerate_endpoints(16),
         'complementary_slopes':complement_family(22),
         'word_sweep':words_check(16)}
    print(json.dumps(res,ensure_ascii=False,indent=2))
    with open('R154_verification.json','w',encoding='utf8') as f: json.dump(res,f,ensure_ascii=False,indent=2)

if __name__=='__main__':main()
