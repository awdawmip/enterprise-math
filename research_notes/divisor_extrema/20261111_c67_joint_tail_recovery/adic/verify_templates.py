"""No simultaneous two-column response tie for redistributions on c=3r.

All polynomial identities are certified over the nonnegative integers by Newton
coefficients, computed from exact model integer dual matrices.
"""
from argparse import ArgumentParser
from collections import Counter
from functools import cache
from fractions import Fraction
from math import prod
from itertools import combinations
import json


def words(length, total):
    if length == 1:
        yield (total,)
    else:
        for gap in range(total+1):
            for rest in words(length-1,total-gap):
                yield (gap,)+rest


def times(u,v):
    a,b,c,d=u
    e,f,g,h=v
    return a*e+b*g,a*f+b*h,c*e+d*g,c*f+d*h


def adjugate(u):
    a,b,c,d=u
    return d,-b,-c,a


def det(u):
    a,b,c,d=u
    return a*d-b*c


@cache
def dual(r,c,m):
    k=2*r+1
    v=c-m
    ns=range(v,c+1)
    l=prod(k+4*n for n in ns)
    b=prod(k+n for n in ns)
    e=(k-1+v)*prod(4*k+n for n in ns)
    t=28*(k-1+4*v)*l*b
    return t,l*e,t,4**m*e*b


def block_word(r,c,word):
    out=(1,0,0,1)
    for gap in word:
        out=times(out,dual(r,c,gap))
        r-=1
        c-=gap
    return out


def positive_newton(samples):
    """Each sample is successively one unit further from a fixed base."""
    sign=1 if samples[0]>0 else -1
    if not samples[0]:
        return 0
    row=samples
    while row:
        if sign*row[0]<0:
            return 0
        row=[y-x for x,y in zip(row,row[1:])]
    return sign


def finite_rule(u,v,r,stock):
    a,b,c,d=times(adjugate(v),u)
    trace=a+d
    if det(u)*det(v)<0:
        assert trace
        return 'opposite orientations and nonzero trace'
    if not (c or b or a-d):
        raise AssertionError('proportional matrices')
    if not c or b*c>=0 or (a-d)*c<=0:
        return 'at most one positive fixed point'
    delta=(a-d)**2+4*b*c
    if delta<=0:
        return 'at most one real fixed point'
    def both_in_interval(left,right):
        midpoint=Fraction(a-d,2*c0)
        q=lambda x:c0*x*x+(d-a)*x-b
        return left<=midpoint<=right and c0*q(left)>=0 and c0*q(right)>=0
    c0=c
    # Every positive physical input through a remaining block has output between 0 and 4.
    if r and not both_in_interval(0,4):
        return 'future slopes lie below four'
    assert r>=2
    for m in range(stock-1):
        for n in range(stock-m-1):
            forward=block_word(r,stock,(m,n))
            left,right=sorted((Fraction(forward[1],forward[3]),Fraction(forward[0],forward[2])))
            assert not both_in_interval(left,right)
    return 'two future blocks exclude simultaneous roots'


def run(length,total,base):
    paths=list(words(length,total))
    pairs=list(combinations(range(len(paths)),2))
    # Product entries have degree ≤d in r; determinants and relative entries ≤2d.
    d=2*total+3*length
    minimum=max(length,(total+4)//3)
    finite=Counter()
    for r in range(minimum,base):
        ms=[block_word(r,3*r,path) for path in paths]
        for i,j in pairs:
            finite[finite_rule(ms[i],ms[j],r-length,3*r-total)]+=1
    sets=[[block_word(r,3*r,path) for path in paths] for r in range(base,base+2*d+1)]
    orientations=[positive_newton([det(ms[i]) for ms in sets]) for i in range(len(paths))]
    assert all(orientations)
    forever=Counter()
    for i,j in pairs:
        relatives=[times(adjugate(ms[j]),ms[i]) for ms in sets]
        if orientations[i]!=orientations[j]:
            assert positive_newton([a+d for a,b,c,d in relatives]),(paths[i],paths[j],'trace')
            forever['opposite orientations and nonzero trace']+=1
            continue
        sign_b=positive_newton([m[1] for m in relatives])
        sign_c=positive_newton([m[2] for m in relatives])
        if sign_b*sign_c>0:
            forever['negative fixed-point product']+=1
            continue
        sign_difference=positive_newton([a-d for a,b,c,d in relatives])
        assert sign_c*sign_difference<0,(paths[i],paths[j],'sum',sign_b,sign_c,sign_difference)
        forever['negative fixed-point sum']+=1
    return dict(ray='c=3r',consecutive_gaps=length,consumed_fives=total,template_count=len(paths),
                first_inventory=minimum,unbounded_Newton_base=base,integer_polynomial_degree=2*d,
                distinct_pairs=len(pairs),finite_certificates=dict(finite),unbounded_certificates=dict(forever))


if __name__=='__main__':
    p=ArgumentParser(description=__doc__)
    p.add_argument('--length',type=int,default=5)
    p.add_argument('--total',type=int,default=5)
    p.add_argument('--base',type=int,default=128)
    a=p.parse_args()
    print(json.dumps(run(a.length,a.total,a.base),indent=2))
