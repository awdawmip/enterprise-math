#!/usr/bin/env python3
"""PREFIX-1006. Exact integer transfer for PREFIX-1005 final-observer
marked collisions. This is post-observer combinatorics of an existing typed
Stage46 Z2 BRC identity, not a new native evolution or physical time model.
"""
import json
from math import comb, factorial, prod
from fractions import Fraction
from functools import lru_cache

DIM = 6
ORBIT_POLYS = [
 ((0,0,0,0,0,0), (21660,-138300,241650)),
 ((-1,0,0,0,0,1), (22680,-142260,355440)),
 ((-2,0,0,0,0,2), (-3420,14100,-11100)),
 ((-2,0,0,0,1,1), (-30240,163200,-219840)),
 ((-1,-1,0,0,1,1), (-49680,324720,-539280)),
 ((-3,0,0,0,0,3), (120,-420,-240)),
 ((-3,0,0,0,1,2), (2880,-12960,2880)),
 ((-3,0,0,1,1,1), (2880,-14400,7200)),
 ((-2,-1,0,0,1,2), (12960,-71280,51840)),
 ((-2,-1,0,1,1,1), (17280,-103680,95040)),
 ((-1,-1,-1,1,1,1), (2880,-18720,20160)),
]

def h_transfer(m, delta):
    """T_s(r): signed-imbalance partial multinomial collision, exact integers."""
    d = 0
    prev = [0]*(m+1)
    for s, v in enumerate(delta):
        d += v
        if s == 0:
            prev = [int(r+v >= 0) for r in range(m+1)]
            continue
        row = [0]*(m+1)
        for r in range(m+1):
            upper = r+d
            if upper < 0:
                continue
            total=0
            for a in range(r+1):
                b = a+v
                if 0 <= b <= upper and prev[r-a]:
                    total += comb(r,a)*comb(upper,b)*prev[r-a]
            row[r]=total
        prev=row
    return prev[m]

@lru_cache(None)
def compositions(s,m):
    if s==1: return ((m,),)
    return tuple((a,)+x for a in range(m+1) for x in compositions(s-1,m-a))

def h_direct(m,delta):
    f=factorial(m)
    total=0
    for a in compositions(DIM,m):
        b=[x+y for x,y in zip(a,delta)]
        if min(b)<0:continue
        total += (f//prod(factorial(x) for x in a))*(f//prod(factorial(x) for x in b))
    return total

def polynomial(co,n):
    return co[0]*n*n + co[1]*n + co[2]

def masked_mass(n):
    m=n-4
    return Fraction(sum(polynomial(c,n)*h_transfer(m,d) for d,c in ORBIT_POLYS),36**n)

KNOWN={5:'5285/419904',6:'9715/1259712',7:'1341545/272097792',
       8:'259181485/78364164096',9:'2182586395/940369969152',
       10:'172091043715/101559956668416',
       12:'130785910556945/131621703842267136',
       14:'3036179298003535/4738381338321616896',
       16:'5427336630506440015/12281884428929630994432',
       20:'89379684726508120031933065/371319292745659279662190166016'}

def run():
    checks=[]
    for m in range(0,9):
        for d,_ in ORBIT_POLYS:
            a=h_transfer(m,d)
            assert a == h_direct(m,d),(m,d,a)
            assert 0 <= a <= h_transfer(m,(0,)*DIM)
        checks.append(m)
    for n,old in KNOWN.items():
        got=str(masked_mass(n))
        assert got == old,(n,got,old)
    for m in range(0,12):
        unit=(-1,0,0,0,0,1)
        assert 30*h_transfer(m,unit)==h_transfer(m+1,(0,)*DIM)-6*h_transfer(m,(0,)*DIM)
    # Whole-space root-lattice transfer, checked for a nontrivial nonzero shift.
    for m in range(0,6):
        d=(-2,0,0,0,0,2)
        rhs=0
        for i in range(DIM):
            for j in range(DIM):
                v=list(d);v[i]+=1;v[j]-=1
                rhs += h_transfer(m,tuple(v))
        assert rhs == h_transfer(m+1,d)
    sample={str(n):str(masked_mass(n)) for n in [5,6,8,12,20,30,50,100]}
    m=100
    profile={str(d):str(h_transfer(m,d)) for d,_ in ORBIT_POLYS}
    return {
        'schema':'PREFIX1006_MARKED_COLLISION_TRANSFER_V1',
        'source':'PREFIX-1005 full joint-port observer, frozen P000 V5@f42f2906',
        'tool':'Python 3 exact big integers (post-BRC final-observer combinatorics)',
        'identity':'T_s(r)=sum_a binom(r,a) binom(r+D_s,a+delta_s) T_(s-1)(r-a); H_m(delta)=T_6(m) when sum(delta)=0',
        'complexity':'For fixed delta, O(6*m^2) arithmetic operations, O(m) stored integers, excluding integer bit complexity; direct composition has binom(m+5,5) candidate terms.',
        'checked_direct_compositions_m':checks,
        'checked_prior_mass_n':list(KNOWN),
        'checked_first_orbit_m':'0..11',
        'checked_root_lattice_recurrence_m':'0..5 for delta=(-2,0,0,0,0,2)',
        'masked_mass':sample,
        'marked_collision_m100':profile,
        'limitations':'Exact final scalar only; 11 orbits are not a finite invariant kernel for SU convolution; no new native Stage46 or heartbeat execution, no independent review'
    }

if __name__=='__main__':
    print(json.dumps(run(),indent=2,ensure_ascii=False))
