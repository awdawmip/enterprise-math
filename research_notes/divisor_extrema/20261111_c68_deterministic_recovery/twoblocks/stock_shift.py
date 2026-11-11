"""Exact two-stock reconstruction and exclusion of two distinct coincidence stocks."""
from argparse import ArgumentParser
from fractions import Fraction as Q
from functools import cache
from itertools import combinations
from math import prod
from pathlib import Path
import json
import sys


def words(r,c):
    if r==0:
        yield (c-2,)
        return
    for m in range(c-1):
        for rest in words(r-1,c-m):
            yield (m,)+rest


@cache
def block(r,c,m):
    k=2*r+1
    v=c-m
    rho=Q(k+4*v,k+v)
    tau=Q(28*(k+4*v)*(k-1+4*v),(4*k+v)*(k-1+v))
    for i in range(v+1,c+1):
        rho*=Q(k+4*i,4*(k+i))
        tau*=Q(k+4*i,4*(4*k+i))
    return rho,tau


def tail(c):
    x=Q(840,(c+2)*(c+3)*(c+4))
    y=prod((Q(4*j+1,4*j+4) for j in range(3,c+1)),start=Q(1))
    return tuple(y*(x*a+b)/(1+x*y*a) for a,b in zip((Q(3,32),Q(3,2),Q(6)),(Q(15,32),Q(15,8),Q(3))))


@cache
def points(r,c,w):
    if r==0:return tail(c)
    rho,tau=block(r,c,w[0])
    return tuple((rho+tau*z)/(1+tau*z) for z in points(r-1,c-w[0],w[1:]))


def read(z):
    a,b=max(z)-1,min(z)-1
    return (1+a/2)/(1+b/2),(1+a)/(1+b)


def endpoints(hg):
    h,g=hg
    low=(2*h-g-1)/(g-h)
    return 1+low,g*(1+low)


def signed_width(pair):
    lo,hi=pair
    assert lo<hi and (1-lo)*(1-hi)>0
    return (1 if lo<1 else -1)*abs(1/(1-lo)-1/(1-hi))


def one_label(x,y,theta,eta):
    den=theta*(1-x)-eta*(1-y)
    if den==0:
        assert x==Q(4,5) and y==theta*Q(4,5)
        return None
    return (y*(1-x)-eta*x*(1-y))/den


def undo(r,c,m,pair):
    rho,tau=block(r,c,m)
    return tuple(sorted((z-rho)/(tau*(1-z)) for z in pair))


def rho_table(r,c):
    return {block(r,c,m)[0]:m for m in range(c-1)}


@cache
def lasts(c):
    return {tuple(sorted((min(z),max(z)))):w for w in words(1,c) for z in (points(1,c,w),)}


def decode(r,c,measurements):
    result=[]
    original=endpoints(measurements[0])
    for j in range(r-1):
        augmented=endpoints(measurements[j+1])
        stock=c+1
        for i,m in enumerate(result):
            augmented=undo(r-i,stock,m,augmented)
            stock-=m
        cnow=stock-1
        k=2*(r-j)+1
        theta=Q(k+4*stock,4*(k+stock))
        eta=Q(k+4*stock,4*(4*k+stock))
        d=eta*signed_width(original)/signed_width(augmented)
        recovered=(d-1)/(d-theta)
        m=rho_table(r-j,cnow)[recovered]
        result.append(m)
        original=undo(r-j,cnow,m,original)
    return tuple(result)+lasts(c-sum(result))[original]


def event_test(limit):
    """Distinct first landing stocks: equations for a(c),P(c), tested without a c cutoff."""
    k=5
    def a(v):return prod((Q(k+4*i,4*(k+i)) for i in range(3,v+1)),start=Q(1))
    def P(v):return prod(range(v+k+1,v+4*k+1))
    records=[]
    for v in range(2,limit+1):
        rho,tau=block(2,v,0)
        A=rho/a(v)
        for w in words(1,v):
            z=points(1,v,w)
            scale=tau*P(v)/a(v)
            records.append((v,A,scale*min(z),scale*max(z)))
    tested=positive=integer=feasible=0
    for (v,A,b0,b1),(w,B,d0,d1) in combinations(records,2):
        if v==w:continue
        tested+=1
        db=b1-b0;dd=d1-d0
        den=A*dd-B*db
        if not den:continue
        astar=(dd-db)/den
        pstar=(db*d0-dd*b0)/den
        if astar<=0 or astar>a(max(v,w)) or pstar<P(max(v,w)):continue
        positive+=1
        if pstar.denominator!=1:continue
        integer+=1
        lo=max(v,w);hi=lo
        while P(hi)<pstar:hi*=2
        while lo<hi:
            mid=(lo+hi)//2
            if P(mid)<pstar:lo=mid+1
            else:hi=mid
        if P(lo)==pstar and a(lo)==astar:feasible+=1
    assert not feasible
    return dict(post_first_stock_through=limit,cross_stock_template_pairs=tested,
                positive_and_in_range=positive,integer_P_candidates=integer,
                all_ambient_stock_ties=feasible)


def core_case(r,c,w):
    originals=points(r,c,w)
    observations=[read(originals)]
    for i in range(r-1):
        altered=tuple(m+(i==j) for j,m in enumerate(w))
        observations.append(read(points(r,c+1,altered)))
    assert decode(r,c,observations)==w
    altered=(w[0]+1,)+w[1:]
    augmented=points(r,c+1,altered)
    k=2*r+1
    theta=Q(k+4*(c+1),4*(k+c+1));eta=Q(k+4*(c+1),4*(4*k+c+1))
    rho=block(r,c,w[0])[0]
    for x,y in zip(originals,augmented):
        ans=one_label(x,y,theta,eta)
        assert ans in (None,rho)
    return observations


def main(native,check):
    sys.path.insert(0,str(native.resolve()))
    sys.path.insert(0,str(check.resolve()))
    from mixed_kernel import responses,simplex_rows
    from enterprise_math import brc_histogram as brc
    count=total=0
    for r in range(1,6):
        for c in range(2,9):
            for w in words(r,c):
                obs=core_case(r,c,w)
                count+=1;total+=len(obs)
    native_cases=[];branches=0
    for r,c,w in ((2,2,(0,0,0)),(2,8,(0,6,0)),(2,8,(6,0,0)),(3,7,(1,0,3,1)),(4,8,(0,1,3,0,2))):
        observations=[]
        for i in range(-1,r-1):
            v=c+(i>=0)
            word=tuple(m+(i==j) for j,m in enumerate(w))
            matrix,b=responses(r,v,word,brc);branches+=b
            x,y=simplex_rows(matrix,7)
            raw=tuple(b/a for a,b in zip(x[3:],y[3:]))
            assert raw==points(r,v,word)
            observations.append(read(raw))
        assert decode(r,c,observations)==w
        native_cases.append(dict(r=r,c=c,word=w,first_pair_H=[str(z) for z in observations[0]]))
    return dict(decoded_words=count,rational_measurements=2*total,depth_range=[1,5],stock_range=[2,8],
                native_examples=native_cases,positive_tail_branches=branches,one_exception_test=event_test(18))


if __name__=='__main__':
    ap=ArgumentParser(description=__doc__)
    ap.add_argument('--native',type=Path,required=True)
    ap.add_argument('--c67-joint',type=Path,required=True)
    args=ap.parse_args()
    print(json.dumps(main(args.native,args.c67_joint),indent=2))
