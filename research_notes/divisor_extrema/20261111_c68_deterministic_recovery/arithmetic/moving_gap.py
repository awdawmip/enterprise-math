"""Exact component certificates for the deterministic one-growing-gap theorem."""
from argparse import ArgumentParser
from fractions import Fraction as Q
from functools import cache
from itertools import product
from math import prod,comb
from pathlib import Path
import json
import sys


def mul(u,v):
    a,b,h,d=u
    e,f,g,i=v
    return a*e+b*g,a*f+b*i,h*e+d*g,h*f+d*i


def apply(mat,z):
    a,b,h,d=mat
    return (a*z+b)/(h*z+d)


def dual(r,c,m):
    k=2*r+1
    v=c-m
    a=prod(k+4*(c-j) for j in range(m+1))
    b=prod(k+c-j for j in range(m+1))
    e=(k-1+v)*prod(4*k+c-j for j in range(m+1))
    t=28*(k-1+4*v)*a*b
    return t,a*e,t,4**m*e*b


@cache
def G(k,n):
    return prod((Q(j)+Q(k,4))/(j+k) for j in range(1,n+1))


def split_coefficients(k,n,v):
    rho_pref=4/G(k,v-1)
    bv=28*Q(k-1+4*v,k-1+v)*prod(v+j for j in range(k,4*k))
    den=prod(n+j for j in range(k+1,4*k+1))
    scale=rho_pref*G(k,n)
    return scale,scale*bv/den


def split_check():
    checked=0
    for r in range(1,9):
        k=2*r+1
        for n in range(2,32):
            for v in range(2,n+1):
                x,b,_,d=dual(r,n,n-v)
                rho,tau=split_coefficients(k,n,v)
                assert (rho,tau)==(Q(b,d),Q(x,d))
                checked+=1
    return checked


def factor_linear(cstar,c0,terms):
    """Return order and leading coefficient of an integral product at c=cstar."""
    n=0
    for a,b in terms:
        value=a*cstar+b
        if value:c0*=value
        else:
            assert a
            n+=1
            c0*=a
    return n,c0


def primitive_at(r,a,m):
    k=2*r+1
    cstar=-4*k+a+1
    aa=[(4,k-4*j) for j in range(m+1)]
    bb=[(1,k-j) for j in range(m+1)]
    ee=[(1,k-1-m)]+[(1,4*k-j) for j in range(m+1)]
    tt=[(4,k-1-4*m)]+aa+bb
    vals=[factor_linear(cstar,c0,f) for c0,f in ((28,tt),(1,aa+ee),(28,tt),(4**m,bb+ee))]
    order=min(v for v,b in vals)
    return tuple(b if v==order else 0 for v,b in vals)


def singular(mat):
    a,b,h,d=mat
    return a*d==b*h


def rank_check():
    counts=[0,0]
    for r in range(1,9):
        for a in (*range(12),*range(6*r+1,6*r+9)):
            for gap in (1,2,5):
                s=primitive_at(r,a,a)
                l=primitive_at(r,a,a+gap)
                assert any(s) and any(l) and singular(s)!=singular(l)
                counts[int(singular(s))]+=1
                for r2 in range(1,r):
                    for m2 in (0,1,3):
                        mat=dual(r2,-4*(2*r+1)+1,m2)
                        assert not singular(mat) and Q(mat[1],mat[3])>4
    return dict(small_invertible_large_singular=counts[0],small_singular_large_invertible=counts[1])


def native(r,c,path,model,tail):
    c0=c;mat=(1,0,0,1)
    for i,m in enumerate(path[:-1]):
        a,b,h,d=model(r-i,c,m)
        mat=mul((a,b,h,d),mat)
        c-=m
    assert c-2==path[-1] and len(path)==r+1 and sum(path)==c0-2
    a,b,h,d=mat
    return [1+(p*a+s*h)/(p*b+s*d) for p,s in tail(c)]


def split_columns(r,c,path,position,model,tail):
    groups=(1,0,0,1)
    for i,m in enumerate(path[:position]):
        groups=mul(groups,dual(r-i,c,m))
        c-=m
    if position==r:
        # Pure end columns when all visible pairs have already been used.
        cols=native(0,c,path[position:],model,tail)
    else:
        v=c-path[position]
        cols=native(r-position-1,v,path[position+1:],model,tail)
        rho,tau=split_coefficients(2*(r-position)+1,c,v)
        cols=[(rho+tau*z)/(1+tau*z) for z in cols]
    return [apply(groups,z) for z in cols]


def compare_native(c64):
    sys.path.insert(0,str(c64.resolve()))
    from observed_four import tail_forms
    from suffix_limits import block
    block=cache(block)
    tails=cache(tail_forms)
    examples=[]
    total=0
    for r in range(1,5):
        families=[]
        for i in range(r+1):
            for fixed in product(range(3),repeat=r):
                families.append((i,fixed))
        for c in (15,31,62):
            actual=set()
            for i,fixed in families:
                moving=c-2-sum(fixed)
                w=fixed[:i]+(moving,)+fixed[i:]
                zz=native(r,c,w,block,tails)
                assert zz==split_columns(r,c,w,i,block,tails)
                actual.add((min(zz),max(zz)))
            assert len(actual)==len(families)
            total+=len(families)
            examples.append(dict(r=r,c=c,distinct_responses=len(actual)))
    return dict(total_exact_native_responses=total,rows=examples)


if __name__=='__main__':
    ap=ArgumentParser(description=__doc__)
    ap.add_argument('--c64',type=Path,required=True)
    args=ap.parse_args()
    print(json.dumps(dict(moving_rate_factorizations=split_check(),primitive_rank_checks=rank_check(),
                          native=compare_native(args.c64)),indent=2))
