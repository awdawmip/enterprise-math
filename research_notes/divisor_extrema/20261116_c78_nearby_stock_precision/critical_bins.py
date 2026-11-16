"""Certified half-open dyadic bins for the two physical block measurements."""
from collections import Counter
from functools import cache
import json
import sys

# Every integer endpoint is a multiple of 2^-BITS. Inputs are nonnegative.
BITS = 176
UNIT = 1 << BITS


def ratio(a, b):
    return UNIT*a//b, -(-UNIT*a//b)


def add(a, b):
    return a[0]+b[0], a[1]+b[1]


def mul(a, b):
    return a[0]*b[0]//UNIT, -(-a[1]*b[1]//UNIT)


def div(a, b):
    assert b[0] > 0
    return UNIT*a[0]//b[1], -(-UNIT*a[1]//b[0])


def cube_ceiling(n):
    i = 1
    while i**3 < n:
        i += 1
    return i


@cache
def kernel(n, s, k):
    from math import prod
    rho = div(prefix[k][n], prefix[k][s-1])
    rho = mul(ratio(4,1),rho)
    factor = ratio(28*(k-1+4*s)*prod(range(s+k,s+4*k)),
                   (k-1+s)*prod(range(n+k+1,n+4*k+1)))
    return rho,mul(rho,factor)


ONE = (UNIT,UNIT)
prefix = {}


def prepare(n):
    for k in (1,3,5):
        row = [ONE]
        for j in range(1,n+1):
            row.append(mul(row[-1], ratio(4*j+k,4*(j+k))))
        prefix[k] = row
    kernel.cache_clear()


@cache
def terminal(w):
    amp = div(prefix[1][w],prefix[1][2])
    t = ratio(840,(w+2)*(w+3)*(w+4))
    result = []
    for a,b in (((3,32),(15,32)),((3,2),(15,8)),((6,1),(3,1))):
        ta = mul(t,ratio(*a))
        result.append(div(mul(amp,add(ta,ratio(*b))),add(ONE,mul(amp,ta))))
    return result


def block(n, v, k, values):
    rho,tau=kernel(n,v,k)
    weighted=[mul(tau,z) for z in values]
    return [div(add(rho,z),add(ONE,z)) for z in weighted]


def full_width(n, v, inner):
    cols=block(n,v,5,inner)
    hi=tuple(max(q[i] for q in cols) for i in (0,1))
    lo=tuple(min(q[i] for q in cols) for i in (0,1))
    return div(hi,lo)


def bin_number(value,p,offset):
    a,b=offset
    endpoints=[((u << p)*b+a*UNIT)//(b*UNIT) for u in value]
    if endpoints[0]!=endpoints[1]:
        raise ArithmeticError("increase BITS to resolve this bin")
    return endpoints[0]


def scan(c, verify_direct=False):
    b=cube_ceiling(c)
    stocks=(c,c+1,c+b,2*c)
    prepare(2*c)
    terminal.cache_clear()
    base=(c**2).bit_length()-1
    precisions=(base,base+3,base+6)
    offsets=((0,1),(1,3),(2,5),(3,7))
    counts={(p,n):Counter() for p in precisions for n in stocks[1:]}
    for v in range(2,c+1):
        for w in range(2,v+1):
            mid=block(v,w,3,terminal(w))
            vals=[full_width(n,v,mid) for n in stocks]
            if verify_direct:
                from check_finite import native_tail_ratios
                for n,(lo,hi) in zip(stocks, vals):
                    tails=native_tail_ratios(n,v,w)
                    exact=max(tails)/min(tails)
                    assert lo<=exact*UNIT<=hi
            for p in precisions:
                keys=[bin_number(q,p,o) for q,o in zip(vals,offsets)]
                for key,n in zip(keys[1:],stocks[1:]):
                    counts[p,n][keys[0],key]+=1
    return {"c":c,"templates":c*(c-1)//2,"offsets":[list(o) for o in offsets],
            "stocks":list(stocks),"rows":[{"p":p,"singletons":[sum(t==1 for t in counts[p,n].values())
                                         for n in stocks[1:]]} for p in precisions]}


if __name__=="__main__":
    sizes = [8,64,128,256] if len(sys.argv)==1 else list(map(int,sys.argv[1:]))
    print(json.dumps([scan(c,verify_direct=c==8) for c in sizes],indent=2))
