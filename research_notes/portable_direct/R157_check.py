#!/usr/bin/env python3
"""R157 exact Farey-cell exhaustive certificates; Python stdlib only."""
from collections import defaultdict
from fractions import Fraction
from math import gcd
import json


def farey_cells(m):
    fractions = sorted({Fraction(a, b) for b in range(1, m+1)
                        for a in range(b + 1) if gcd(a, b) == 1})
    return zip(fractions, fractions[1:])


def mechanical_words(m):
    result = set()
    for p, q in farey_cells(m):
        theta = (p + q) / 2
        changes = sorted({Fraction(0), Fraction(1)} |
                         {(-j * theta) % 1 for j in range(1, m+1)})
        for lo, hi in zip(changes, changes[1:]):
            x = (lo + hi) / 2
            word = tuple(int((j + 1) * theta + x) - int(j * theta + x)
                         for j in range(m))
            result.add(word)
    return result


def exact_signature(w):
    m = len(w)
    p = [0]
    for digit in w:
        p.append(p[-1] + digit)
    a,b,c,d = 0,1,1,1
    for i in range(m):
        for j in range(i+1,m+1):
            k=j-i
            q=p[j]-p[i]
            if (q-1)*b > a*k:a,b=q-1,k
            if (q+1)*d < c*k:c,d=q+1,k
    if a*d >= c*b:
        return None
    g=gcd(abs(a),b);a//=g;b//=g
    g=gcd(abs(c),d);c//=g;d//=g
    U=b + min(p[j]*b-a*j for j in range(m+1))
    V=max(p[j]*d-c*j for j in range(m+1))
    return (a,b,c,d,U,V)


def count_at_L(k,L):
    a,b,c,d,U,V=k
    # ceil((L*c-V)/d) - floor((L*a-U)/b) -1
    return -((V-L*c)//d) - ((L*a-U)//b) - 1


def permanent_threshold(k):
    a,b,c,d,_,_=k
    period=b*d//gcd(b,d)
    # C(L+period+1)=C(L+1)+integer_positive => first-period scan exhaustive.
    last=max((L for L in range(1,period+1) if count_at_L(k,L)==0),default=0)
    return last+2


def main(max_length=32):
    results=[]
    for m in range(1,max_length+1):
        bykey=defaultdict(list)
        for w in mechanical_words(m):
            key=exact_signature(w)
            assert key is not None, (m,w)
            bykey[key].append(''.join(map(str,w)))
        fibers=[len(v) for v in bykey.values()]
        T_by_sig={k:permanent_threshold(k) for k in bykey}
        optimum=max(T_by_sig.values())
        optimal=[(k,bykey[k]) for k,t in T_by_sig.items() if t==optimum]
        pred = (m-2)*((m-1)//2)+1 if m>=5 else None
        if m>=5:
            assert optimum==pred,(m,optimum,pred)
            assert {tuple(sorted(words)) for _,words in optimal}=={
                ('0'+'1'*(m-2)+'0',), ('1'+'0'*(m-2)+'1',)
            },(m,optimal)
        assert max(fibers)<=2, (m,max(fibers))
        data={'m':m,'sturmian_words':sum(fibers),'signatures':len(fibers),
              'alias_pairs':sum(x==2 for x in fibers),
              'max_fiber':max(fibers),'global_threshold':optimum,
              'maximizer_words':sorted(w for _,words in optimal for w in words)}
        results.append(data)
        print(f"m={m:2d} n={data['sturmian_words']:5d} alias={data['alias_pairs']:4d} T={optimum:4d} maximizers={data['maximizer_words']}",flush=True)
    with open('R157_verification.json','w') as f:
        json.dump({'marker':'R157_FAREY_EXHAUSTIVE_M32_PASS',
                   'scope':'all binary Sturmian words length 1..32, exact arithmetic',
                   'all_lengths_max_fiber':max(x['max_fiber'] for x in results),
                   'by_length':results}, f,indent=2)


if __name__=='__main__':main()
