"""Exact two-stock zero-center reconstruction on all tested landing pairs."""
from bisect import bisect_right, bisect_left
from fractions import Fraction as F
from functools import lru_cache
from itertools import product
from math import prod
import json

d, D = F(1, 2), F(5)
t = D-d

def rising(s,n):
    return prod(range(s,s+n))

@lru_cache(None)
def P(k,n):
    return rising(n+k+1,3*k)

@lru_cache(None)
def B(k,n):
    return F(28*(4*n+k-1)*rising(n+k,3*k),n+k-1)

@lru_cache(None)
def svalue(n):
    return F(840,rising(n+2,3))

def center(c,v,w):
    a,b=F(P(5,c),B(5,v)),F(P(3,v),B(3,w))
    s=svalue(w)
    def column(j):
        p=s/(s+j)
        return (1+b*p)/(1+a+b*p)
    return column(d)/column(D)

def data(c1,c2,v,w):
    z1,z2=(1/(center(c,v,w)-1) for c in (c1,c2))
    p1,p2=P(5,c1),P(5,c2)
    intercept=(z2*p2-z1*p1)/(p2-p1)
    slope=(z1-intercept)*p1
    h=t*intercept-d
    M=(slope/intercept)*h/(h+D)
    assert B(5,v)==M*(1-svalue(w)/h)
    return intercept,slope/intercept,h,M

def continuous_witness():
    v,w=50,4
    I,T,H,M=data(121,122,v,w)
    signs=[]
    for y,expected_sign in [(30,-1),(40,1)]:
        s=svalue(y)
        required=M*(1-s/H)
        assert B(5,104) < required < B(5,105)
        E=B(3,y)*(d+s)*(D+s)/s
        witnesses=[E*M/H-P(3,u)*B(5,u) for u in (104,105)]
        assert all(z*expected_sign>0 for z in witnesses)
        signs.append(dict(w=y,first_landing_between=[104,105],residual_sign=expected_sign))
    return dict(exact_integer_template=[50,4],second_real_terminal_between=[30,40],
                second_real_first_between=[104,105],certified_endpoints=signs)


def main():
    n=120
    # Formal d,D endpoint labels even for w=2,3 in the decoder's possible competitors.
    # Targets use the physical endpoint labels, hence w>=4 for them.
    stocks=(121,122)
    Bs=[B(5,u) for u in range(2,n+1)]
    cubes={rising(y+2,3):y for y in range(2,n+1)}
    recovered=all_integer_candidates=comparisons=0
    vals=set()
    for v in range(4,n+1):
        for w in range(4,v+1):
            I,T,h,M=data(*stocks,v,w)
            assert (I,T) not in vals
            vals.add((I,T))
            lo=bisect_left(Bs,M*(1-7/h));hi=bisect_left(Bs,M)
            candidates=[]
            for idx in range(lo,hi):
                u=idx+2
                s=h*(1-Bs[idx]/M)
                comparisons+=1
                polynomial=840/s
                if polynomial.denominator!=1 or polynomial.numerator not in cubes:
                    continue
                y=cubes[polynomial.numerator]
                if y>u:
                    continue
                all_integer_candidates+=1
                if data(*stocks,u,y)[:2]==(I,T):
                    candidates.append((u,y))
            assert candidates == [(v,w)]
            recovered+=1
    print(json.dumps(dict(stocks=stocks,landing_upper=n,physical_center_targets=recovered,
                          distinct_center_lines=len(vals),first_landing_candidates_examined=comparisons,
                          candidate_pairs_after_cubic=all_integer_candidates,continuous_double_point=continuous_witness()),indent=2))

if __name__=='__main__':
    main()
