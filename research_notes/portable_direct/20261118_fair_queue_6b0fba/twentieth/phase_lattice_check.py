"""Exact joint phase counts, annihilators, and weighted simplex identities."""
import json
from fractions import Fraction as F
from functools import cache
from itertools import combinations, product
from math import gcd, isqrt, prod
from random import Random


def det(rows):
    if not rows:
        return 1
    return sum((-1)**j * x * det([r[:j]+r[j+1:] for r in rows[1:]])
               for j,x in enumerate(rows[0]))


def differences(points):
    return [tuple(x-y for x,y in zip(p,points[0])) for p in points[1:]]


def actual_phases():
    # Exact Legendre sieve count on the inverse-translated target intervals.
    X,p,W=3000000,53,210
    lo,hi=56490,57330
    period=hi-lo
    primes=[q for q in range(2,isqrt(hi)+1) if all(q%i for i in range(2,isqrt(q)+1))]
    @cache
    def sift(n,k):
        if n==0 or k==0: return n
        return sift(n,k-1)-sift(n//primes[k-1],k-1)
    def slice_size(a,b):
        # All addresses in [lo,hi) exceed the sieving primes.
        return sift(b-1,len(primes))-sift(a-1,len(primes))
    widths=[F(1,100),F(3,1000),F(1,1000)]
    phases=[]
    for s in range(period//W):
        row=[]
        for eta in widths:
            left=X//p+1
            right=(X*(1+eta))//p+1
            start=(left-lo-s*W)%period
            length=right-left
            n=slice_size(lo+start,lo+min(period,start+length))
            if start+length>period:
                n+=slice_size(lo,lo+start+length-period)
            row.append(n)
        phases.append(row)
    return phases


def covariance(points, weights):
    d=len(points[0])
    mean=[sum(w*p[i] for p,w in zip(points,weights)) for i in range(d)]
    return [[sum(w*(p[i]-mean[i])*(p[j]-mean[j]) for p,w in zip(points,weights))
             for j in range(d)] for i in range(d)]


def covariance_check(points,weights):
    d=len(points[0])
    determinants=[(indices,det(differences([points[i] for i in indices])))
                  for indices in combinations(range(len(points)), d+1)]
    total=sum(prod(weights[i] for i in indices)*v*v for indices,v in determinants)
    assert total==det(covariance(points,weights))
    anchor=gcd(*(abs(v) for indices,v in determinants if 0 in indices))
    assert anchor==gcd(*(abs(v) for _,v in determinants))
    return total


def main():
    points=actual_phases()
    assert points==[[57,16,4],[58,17,7],[57,19,6],[59,18,4]]
    ds=differences(points)
    minors=[ds[i][a]*ds[j][b]-ds[i][b]*ds[j][a]
            for i,j in combinations(range(3),2) for a,b in combinations(range(3),2)]
    divs=[gcd(*(abs(x) for r in ds for x in r)),gcd(*minors),abs(det(ds))]
    assert divs==[1,1,18]
    u=(7,2,-3)
    levels=[sum(a*b for a,b in zip(p,u)) for p in points]
    assert levels==[419,419,419,437]
    mask_counts={}
    for m in range(1,37):
        g=gcd(18,m)
        wanted={tuple(t*(m//g)*v%m for v in u) for t in range(g)}
        actual={(i,j,k) for i,j,k in product(range(m),repeat=3)
                if (i+j+3*k)%m==0 and (3*j+2*k)%m==0 and (2*i+2*j)%m==0}
        assert actual==wanted and len(actual)==g
        mask_counts[m]=g
    indep=[sum(u[j]*points[s[j]][j] for j in range(3))%18
           for s in product(range(4),repeat=3)]
    assert indep.count(5)==9
    weights=[F(1,4)]*4
    cov=covariance(points,weights)
    full=covariance_check(points,weights)
    assert full==F(81,64) and full*F(4,3)**3==3
    rng=Random(1804); extra=0
    for d in range(1,5):
        for n in range(d+1,d+4):
            for _ in range(9):
                pts=[[rng.randrange(-3,5) for _ in range(d)] for _ in range(n)]
                mass=[rng.randrange(1,10) for _ in range(n)]
                covariance_check(pts,[F(v,sum(mass)) for v in mass])
                extra+=1
    return dict(source_windows_phases=points,differences=ds,minor_gcds=divs,
                smith_factors=[divs[0],divs[1]//divs[0],divs[2]//divs[1]],
                linear_levels=levels,modular_probe_counts=mask_counts,
                independent_phase_choices=64,independent_satisfying_residue_5=indep.count(5),
                population_covariance=[[str(v) for v in r] for r in cov],
                population_determinant=str(full),unbiased_sample_determinant=3,
                additional_weighted_clouds=extra)


if __name__=='__main__':
    print(json.dumps(main(),ensure_ascii=False,indent=2,sort_keys=True))
