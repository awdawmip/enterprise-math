#!/usr/bin/env python3
"""R608 exact integer verification of a scope-typed X6 word observer hierarchy.

Magnus coefficients are computed in the noncommutative truncated polynomial ring
Z<X_1,...,X_6> / (words of length > depth). No exp, floats or analytic limit.
Capital letters are inverse native steps, lower case positive native steps.
"""
from itertools import product
from collections import Counter

AXES = 'abcdef'
P = 'abABAbaB'

def invert(word):
    return ''.join(c.upper() if c.islower() else c.lower() for c in reversed(word))

def mul(u,v,depth):
    out=Counter()
    for a,x in u.items():
        for b,y in v.items():
            if len(a)+len(b)<=depth:
                out[a+b]+=x*y
    return {k:v for k,v in out.items() if v}

def atom(letter,depth):
    i=AXES.index(letter.lower())
    mono=(i,)
    if letter.islower():
        return {():1,mono:1}
    return {mono*n:(-1)**n for n in range(depth+1)}

def magnus(word,depth):
    result={():1}
    for letter in word:
        result=mul(result,atom(letter,depth),depth)
    return result

def trunc(t,d):
    return {k:v for k,v in t.items() if len(k)<=d}

def d_A(word):
    d=[0]*6; A=[0]*15
    pairs=[(i,j) for i in range(6) for j in range(i+1,6)]
    letters=[]
    for c in word:
        i=AXES.index(c.lower()); s=1 if c.islower() else -1
        letters.append((i,s)); d[i]+=s
    for a in range(len(letters)):
        i,s=letters[a]
        for b in range(a+1,len(letters)):
            j,t=letters[b]
            if i!=j:
                A[pairs.index((min(i,j),max(i,j)))]+=(s*t if i<j else -s*t)
    return tuple(d),tuple(A)

def adj_a_power_on_b(k):
    # ad_Xa^k(Xb) = sum_j (-1)^j binom(k,j) Xa^(k-j) Xb Xa^j
    from math import comb
    result={}
    for j in range(k+1):result[(0,)*(k-j)+(1,)+(0,)*j]=(-1)**j*comb(k,j)
    return result

p=P;q=invert(p)
assert len(p)==len(q)==8
assert d_A(p)==d_A(q)==((0,)*6,(0,)*15)
sp=magnus(p,3);sq=magnus(q,3)
assert trunc(sp,2)==trunc(sq,2)=={():1}
assert {k:v for k,v in sp.items() if len(k)==3}==adj_a_power_on_b(2)
assert {k:v for k,v in sq.items() if len(k)==3}=={k:-v for k,v in adj_a_power_on_b(2).items()}

# Exact both-sided context invariance (all 12 signed letters and empty at each end).
ctx=['']+[x for a in AXES for x in (a,a.upper())]
for left,right in product(ctx,repeat=2):
    lp=magnus(left+p+right,3)
    lq=magnus(left+q+right,3)
    assert trunc(lp,2)==trunc(lq,2)
    diff={k:lp.get(k,0)-lq.get(k,0) for k in set(lp)|set(lq)}
    diff={k:v for k,v in diff.items() if v}
    assert diff=={k:2*v for k,v in adj_a_power_on_b(2).items()}

# Arbitrarily deep symbolic construction W_(n+1) = a W_n A W_n^{-1}.
# For n=3,4,5,6, exact leading Magnus word is ad_a^(n-1)(b).
lengths={}
w=P
for n in range(3,7):
    s=magnus(w,n)
    assert trunc(s,n-1)=={():1}
    layer={k:v for k,v in s.items() if len(k)==n}
    assert layer==adj_a_power_on_b(n-1), (n,layer)
    assert d_A(w)==((0,)*6,(0,)*15)
    lengths[n]=len(w)
    w='a'+w+'A'+invert(w)

# Independent exact link from R607 d,A to degree <= 2 Magnus coefficients.
# Exhaustively cover all 12-letter words of length 0..4 (22,621 words).
words=0
alphabet=[v for a in AXES for v in (a,a.upper())]
for length in range(5):
    for tup in product(alphabet,repeat=length):
        w=''.join(tup)
        d,A=d_A(w)
        sig=magnus(w,2)
        assert sig.get((),0)==1
        for i in range(6):
            assert sig.get((i,),0)==d[i]
            assert sig.get((i,i),0)==d[i]*(d[i]-1)//2
        idx=0
        for i in range(6):
            for j in range(i+1,6):
                assert (d[i]*d[j]+A[idx])%2==0
                assert (d[i]*d[j]-A[idx])%2==0
                assert sig.get((i,j),0)==(d[i]*d[j]+A[idx])//2
                assert sig.get((j,i),0)==(d[i]*d[j]-A[idx])//2
                idx+=1
        words+=1
assert words==22621
print('R608_EXACT_MAGNUS_HIERARCHY_PASS')
print('p='+p, 'q='+q, 'length_each=8', 'd=0', 'A=0')
print('degree3_p='+str(sorted((tuple(i+1 for i in k),v) for k,v in sp.items() if len(k)==3)))
print('degree3_q='+str(sorted((tuple(i+1 for i in k),v) for k,v in sq.items() if len(k)==3)))
print('context_pairs='+str(len(ctx)**2))
print('degree2_correspondence_words='+str(words))
print('higher_degree_checked='+str(lengths))
print('arithmetic=exact_integers_noncommutative_truncated_polynomials')
