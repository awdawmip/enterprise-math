#!/usr/bin/env python3
"""R191 exact reference checks; stdlib only; no native BRC package claimed."""
from fractions import Fraction as F
from itertools import permutations, product, combinations
from math import factorial, ceil, log2
import json


def partials(k):
    return [p for r in range(k + 1) for p in permutations(range(k), r)]

def star(a, b):
    sb = set(b)
    return tuple(x for x in a if x not in sb) + tuple(b)

def latest(word, k):
    s = ()
    for a in word:
        if a < k:
            s = star(s, (a,))
    return s

def rank_perm(s, k):
    r = len(s)
    offset = sum(factorial(k)//factorial(k-j) for j in range(r))
    rest = list(range(k))
    rank = 0
    for i, x in enumerate(s):
        j = rest.index(x)
        rank += j * (factorial(k-i-1)//factorial(k-r))
        rest.pop(j)
    return offset + rank

def unrank_perm(code, k):
    assert 0 <= code < sum(factorial(k)//factorial(k-r) for r in range(k+1))
    start = 0
    for r in range(k+1):
        size = factorial(k)//factorial(k-r)
        if code < start + size:
            break
        start += size
    v = code - start
    rest = list(range(k)); result = []
    for i in range(r):
        block = factorial(k-i-1)//factorial(k-r)
        d, v = divmod(v, block)
        result.append(rest.pop(d))
    assert v == 0
    return tuple(result)

def action(word, k):
    # x -> alpha*x+beta, diagonal affine map; event k marks an unselected source.
    alpha = [F(1)]*k
    beta = [F(0)]*k
    for a in word:
        for j in range(k):
            if j == a:
                alpha[j], beta[j] = F(0), F(1)
            else:
                alpha[j] /= 2
                beta[j] /= 2
    return tuple(alpha),tuple(beta)

def compose(A,B):
    # A.then(B) = B o A
    aa,ba=A; ab,bb=B
    return tuple(x*y for x,y in zip(aa,ab)),tuple(x*y+z for x,y,z in zip(ba,ab,bb))

def observe(beta):
    positive=[(x,i) for i,x in enumerate(beta) if x]
    assert all(x > 0 for x,i in positive)
    assert len(set(x for x,i in positive)) == len(positive)
    return tuple(i for x,i in sorted(positive))

def oracle(s, sub):
    selected=set(sub)
    return next((x for x in reversed(s) if x in selected),None)

def check():
    cnt={'rank_roundtrips':0,'rank_unique_codes':0,'append_rank_updates':0,'quotient_compositions':0,
        'dyadic_word_observations':0,'dyadic_affine_compositions':0,'oracle_checks':0,
        'dyadic_denominator_witnesses':0}
    rows=[]
    for k in range(1,8):
        sts = partials(k)
        N=sum(factorial(k)//factorial(k-r) for r in range(k+1))
        assert N==len(sts)
        codes=set()
        for s in sts:
            c=rank_perm(s,k)
            assert c not in codes and unrank_perm(c,k)==s
            codes.add(c);cnt['rank_roundtrips']+=1
            for a in range(k+1):
                new=latest(s+(a,),k)
                assert unrank_perm(rank_perm(new,k),k)==new
                cnt['append_rank_updates']+=1
        assert codes == set(range(N))
        cnt['rank_unique_codes']+=len(codes)
        rows.append({'k':k,'states':N,'optimal_fixed_bits':(N-1).bit_length(),
                     'quadratic_reset_coordinates':k*(k+1)//2,'dyadic_affine_coordinates':k})
        if k<=5:
            for a in sts:
                for b in sts:
                    c=unrank_perm(rank_perm(star(a,b),k),k)
                    assert c == latest(a+b,k)
                    cnt['quotient_compositions']+=1
        if k<=4:
            for s in sts:
                for submask in range(1,1<<k):
                    sub={i for i in range(k) if submask & (1<<i)}
                    assert oracle(s,sub)==oracle(unrank_perm(rank_perm(s,k),k),sub)
                    cnt['oracle_checks']+=1
    # all words of length 0..5 over {0,1,2, irrelevant=3}
    k=3
    words=[w for n in range(6) for w in product(range(k+1),repeat=n)]
    for w in words:
        A=action(w,k)
        assert observe(A[1])==latest(w,k)
        cnt['dyadic_word_observations']+=1
    # a dense but bounded grid of free-monoid composition checks
    small=words[:341]
    for u in small:
        Au=action(u,k)
        for v in small[:150]:
            assert compose(Au,action(v,k))==action(u+v,k)
            cnt['dyadic_affine_compositions']+=1
    for m in range(1,20):
        A=action((1,)+(0,)*m,2)
        assert A[1][1]==F(1,2**m)
        cnt['dyadic_denominator_witnesses']+=1
    assert action((0,0),2)!=action((0,),2) # quotient idempotence does NOT descend to affine maps
    assert latest((0,0),2)==latest((0,),2)
    assert action((2,0),2)!=action((0,),2) # irrelevant event changes affine action
    assert latest((2,0),2)==latest((0,),2)
    return {'schema':'EM_R191_EXACT_CHECK_V1','status':'PASS',
           'fixed_science_pin':'43ec6098b1330ae86d0a7863be336c5d97f6ef34',
           'arithmetic':'Python arbitrary integers and Fraction; no floats used in evidence',
           'rows':rows,'checks':cnt,'finite_domains':{
             'rank_unrank':'all partial permutations k=1..7',
             'append':'all partial permutations k=1..7 and every target or one unselected source',
             'star':'all state pairs k=1..5',
             'query':'all state/subset pairs k=1..4',
             'dyadic':'all words of length <=5 over 3 targets + 1 unselected symbol',
             'affine':'341 by 150 selected words; exact free-monoid composition',
             'bit_growth':'m=1..19 for word (source 1)(source 0)^m',
           },'review':'NOT_REVIEWED','native_brc_integration':'NOT_EXECUTED'}

if __name__=='__main__':
    result=check()
    print(json.dumps(result,sort_keys=True,indent=2,ensure_ascii=False))
