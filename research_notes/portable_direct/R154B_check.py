#!/usr/bin/env python3
"""Exact one-defect word-alias check; run in same directory as R154_check.py."""
from fractions import Fraction
import json
from R154_check import support

def cuts(word):
    m = len(word)
    ps = [0]
    for ch in word:
        ps.append(ps[-1] + (ch == '1'))
    bound = support(word)
    assert bound is not None
    a,b,c,d = bound
    U = min(b*(ps[j]+1)-j*a for j in range(m+1))
    V = max(d*ps[j]-j*c for j in range(m+1))
    return (a,b,c,d,U,V)

def ceildiv(a,b): return -(-a//b)
def count(p,L):
    a,b,c,d,U,V = p
    return ceildiv(c*L-V,d)-(a*L-U)//b-1

def verify(max_m=32, max_h=200):
    cases=0; aliases=[]; complements=0
    for m in range(2,max_m+1):
        group={}
        for p in range(m):
            q=m-1-p
            w='0'*p+'1'+'0'*q
            z=cuts(w)
            a,b,c,d,U,V=z
            r=max(p,q)
            predicted=min(Fraction(1,r),Fraction(2,m)) if r else Fraction(1)
            assert (a,b)==(0,1) and Fraction(c,d)==predicted
            assert U==1 and V==max(0,d-(p+1)*c)
            key=(z[:4],tuple(count(z,L) for L in range(1,2*m+8)))
            group.setdefault(key,[]).append(w)
            cases+=1
        pairgroups=[v for v in group.values() if len(v)>1]
        expected=[] if m%2 else [['0'*(m//2)+'1'+'0'*(m//2-1),
                                      '0'*(m//2-1)+'1'+'0'*(m//2)]]
        assert sorted([sorted(z) for z in pairgroups])==sorted([sorted(z) for z in expected]),(m,pairgroups)
        aliases.extend({'m':m,'words':v} for v in pairgroups)
    family_checks=0
    for h in range(2,max_h+1):
        a='0'*h+'1'+'0'*(h-1)
        b='0'*(h-1)+'1'+'0'*h
        expected=(0,1,1,h,1,0)
        assert cuts(a)==cuts(b)==expected
        ca=cuts(''.join('1' if c=='0' else '0' for c in a))
        cb=cuts(''.join('1' if c=='0' else '0' for c in b))
        for L in [1,2,h-1,h,h+1,2*h+7,10**12+17]:
            answer=ceildiv(L,h)
            assert count(expected,L)==count(ca,L)==count(cb,L)==answer
            family_checks+=1
        complements+=2
    return {'tag':'R154B_SINGLE_DEFECT_ALIAS_PASS',
            'single_one_word_checks':cases,'lengths':[2,max_m],
            'alias_pairs':len(aliases),'alias_examples':aliases[:10],
            'center_family_h':[2,max_h], 'large_integer_count_checks':family_checks,
            'complement_words_checked':complements,
            'arithmetic':'Fraction and unlimited integers, no floating point',
            'scope':'Finite corroboration; proof covers all lengths and K>=2.'}

if __name__=='__main__':
    o=verify()
    open('R154B_verification.json','w').write(json.dumps(o,ensure_ascii=False,indent=2)+'\n')
    print(o['tag'],o['single_one_word_checks'],o['alias_pairs'],o['large_integer_count_checks'])
