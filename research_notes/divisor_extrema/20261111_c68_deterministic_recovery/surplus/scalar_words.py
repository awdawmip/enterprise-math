"""Compare the single physical scalar H(0,1) for every jointly legal stock."""
from argparse import ArgumentParser
from fractions import Fraction as F
from functools import cache
from itertools import combinations
import json
from terminal_words import R,column,allwords,roots_at_and_after,bound,y_next,matrix_value

def times(u,v):
    out=[R.zero]*(len(u)+len(v)-1)
    for i,p in enumerate(u):
        for j,q in enumerate(v):out[i+j]+=p*q
    return tuple(out)

@cache
def ratio(w):
    a,b,h,d=column(w,2)
    e,f,g,i=column(w,0)
    numerator=times((b,a),(i,g))
    denominator=times((f,e),(d,h))
    coeff=numerator+denominator
    gcd=coeff[0]
    for p in coeff[1:]:gcd=gcd.gcd(p)
    return tuple(p.exquo(gcd) for p in numerator),tuple(p.exquo(gcd) for p in denominator)

def census(budget):
    words=[w for r in range(1,budget+1) for w in allwords(r,budget-r)]
    first=max(sum(w)+4 for w in words)
    roots=set()
    count=0
    for u,v in combinations(words,2):
        p,q=ratio(u)
        a,b=ratio(v)
        for nu,de in ((a,b),(b,a)):
            diff=tuple(x-y for x,y in zip(times(p,de),times(q,nu)))
            nonzero=[z for z in diff if z]
            assert nonzero
            g=nonzero[0]
            for z in nonzero[1:]:g=g.gcd(z)
            c0=max(sum(u),sum(v))+4
            roots.update(roots_at_and_after(g,c0))
            reduced=tuple(z.exquo(g) for z in diff)
            first=max(first,bound(reduced,c0))
            count+=1
    last=max({first-1}|roots)
    y=F(1)
    hits=[]
    tests=0
    for c in range(2,last+1):
        if c>2:y=y_next(y,c)
        if c>=first and c not in roots:continue
        seen={}
        for w in words:
            if c<sum(w)+2:continue
            triple=[matrix_value(column(w,j),c,y) for j in range(3)]
            H=max(triple)/min(triple)
            for v in seen.get(H,[]):hits.append([c,w,v])
            seen.setdefault(H,[]).append(w)
            tests+=1
    return dict(length_plus_internal_fives_at_most=budget,words=len(words),equations=count,
                largest_stock_evaluated=last,first_stock_dominated_by_denominator=first,
                possible_gcd_root_stocks=sorted(roots),exact_H_calculations=tests,
                distinct_words_with_equal_H=hits)

if __name__=='__main__':
    p=ArgumentParser(description=__doc__)
    p.add_argument('--budget',default=5,type=int)
    args=p.parse_args()
    print(json.dumps(census(args.budget),indent=2))
