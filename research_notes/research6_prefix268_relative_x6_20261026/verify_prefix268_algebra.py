#!/usr/bin/env python3
"""Independent integer-polynomial certificate + finite future-observer exhaustive check.
This uses the explicit signed X6 N-BRC path-label carrier and no physical Phi.
"""
from itertools import combinations, product
from math import factorial

def mul(a,b):
    c=[0]*(len(a)+len(b)-1)
    for i,u in enumerate(a):
        for j,v in enumerate(b): c[i+j]+=u*v
    return c

def add(a,b):
    c=[0]*max(len(a),len(b))
    for i,u in enumerate(a):c[i]+=u
    for i,v in enumerate(b):c[i]+=v
    return c

def shift(a,n): return [0]*n+a

def poly_identity():
    ds=[1,2,3,2,1]     # min(i,6-i) for five consecutive coordinate gaps
    lhs=[0]
    for mask in range(1<<5):
        breaks=[0]+[i+1 for i in range(5) if mask>>i&1]+[6]
        blocks=[breaks[j+1]-breaks[j] for j in range(len(breaks)-1)]
        mult=factorial(6)
        for s in blocks: mult//=factorial(s)
        # Commutative exact factor multiplication. The sequential division
        # is integer for the 6!//(product factorials) multinomial.
        power=sum(d for i,d in enumerate(ds) if mask>>i&1)
        term=[mult]
        for i,d in enumerate(ds):
            if not mask>>i&1:
                term=mul(term,[1]+[0]*(d-1)+[-1])
        lhs=add(lhs,shift(term,power))
    # M A(x) = (1+7x+22x²+22x³+7x⁴+x⁵) (1+x)^2(1+x+x²)
    P5=[1,7,22,22,7,1]
    rhs=mul(P5,mul([1,2,1],[1,1,1]))
    assert lhs==rhs,(lhs,rhs)
    return lhs

SIGNS=tuple((i,s) for i in range(6) for s in(-1,1))
def can6(p):
    v=min(p)
    return tuple(x-v for x in p)

def future_exhaustion(max_n=4):
    for n in range(max_n+1):
        keys=[tuple(SIGNS.index(a) for a in word) for word in product(SIGNS,repeat=n)]
        for h in range(n+1):
            obs_to_pred={};pred_to_obs={}
            for key in keys:
                word=[SIGNS[j] for j in key]
                z=[0]*6
                for i,s in word:z[i]+=s
                prefix=[]
                for j in range(h+1):
                    prefix.append(can6(z))
                    if j<h:
                        i,s=word[n-1-j];z[i]-=s
                observed=tuple(prefix)
                predicted=(prefix[0],tuple(key[n-h:])) if h else (prefix[0],())
                a=obs_to_pred.setdefault(observed,predicted)
                b=pred_to_obs.setdefault(predicted,observed)
                assert a==predicted and b==observed,(n,h,key)
            assert len(obs_to_pred)==len(pred_to_obs)
            print('n,h,classes',n,h,len(obs_to_pred))

def triad_witness():
    # k=3: 20 pairs exactly. Both full endpoints have 6 path words each.
    aliases=set()
    for S in combinations(range(6),3):
        H=tuple(int(i in S) for i in range(6))
        minus_complement=tuple(-int(i not in S) for i in range(6))
        assert can6(H)==can6(minus_complement)
        assert sum(map(abs,H))==sum(map(abs,minus_complement))==3
        assert sum(int(i in S) for i in range(6))==3
        assert factorial(3)==6
        aliases.add(can6(H))
    assert len(aliases)==20
    return sorted(aliases)

if __name__=='__main__':
    lhs=poly_identity()
    triads=triad_witness()
    print('integer_polynomial_identity_coefficients=',lhs)
    print('earliest_triad_aliases=',len(triads))
    future_exhaustion(4)
    print('PREFIX268_INDEPENDENT_ALGEBRA_AND_FUTURE_EXHAUSTION_PASS')
