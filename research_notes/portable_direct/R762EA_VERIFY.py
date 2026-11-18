#!/usr/bin/env python3
"""Exact positive-six-branch BRC cyclotomic leading-coefficient check.
No roots or floating point; coefficients below w^6 are reduced mod 3.
"""
from collections import Counter
from itertools import product
from math import comb
import json

B = ((0,0,0),(1,0,0),(0,0,1),(1,1,0),(0,1,1),(1,1,1))

def six_branch_leading_coefficients(i,j,k,q):
    exps = [(u*i+v*j+w*k) % q for u,v,w in B]
    return tuple(sum(comb(e,m) if e>=m else 0 for e in exps) % 3
                 for m in range(6))

def predicted_order(i,j,k):
    a,b,c = i%3,j%3,k%3
    d=(2*a*b+a*c+2*b*c)%3
    if d:
        return 2
    A,B,C=(i//3)%3,(j//3)%3,(k//3)%3
    b2=lambda s: int(s==2)
    K=(2*b2(a)*b2(b)+b2(a)*b2(c)+2*b2(b)*b2(c)
       +b2(a)*b*c+a*b2(b)*c+a*b*b2(c))
    e4=((2*b+c)*A+(2*a+2*c)*B+(a+2*b)*C+K)%3
    return 4 if e4 else 6

def check(q):
    hist=Counter()
    for i,j,k in product(range(q),repeat=3):
        v=six_branch_leading_coefficients(i,j,k,q)
        actual=next((m for m,r in enumerate(v) if r),6)
        predicted=predicted_order(i,j,k)
        assert actual==predicted,(q,i,j,k,actual,predicted,v)
        hist[actual]+=1
    assert hist=={2:2*q**3//3,4:16*q**3//81,6:11*q**3//81}
    return {str(k):hist[k] for k in (2,4,6)}

if __name__=='__main__':
    result={'model':'six named positive BRC branches P=1+X+Z+XY+YZ+XYZ',
      'field':'F3, exact truncated expansion in w=zeta-1, w^6',
      'test_ranges':{'q9':'all 9^3 characters','q27':'all 27^3 characters'},
      'histogram_q9':check(9),'histogram_q27':check(27),
      'scope':'character w-valuations exactly 2 or 4; remaining >=6; all a>=2 via mod9 digit argument',
      'status':'PASS'}
    print(json.dumps(result,indent=2,sort_keys=True))
