#!/usr/bin/env python3
"""Exact rational interval certificate for a full-road cross-thickness sign failure.

No floating-point arithmetic enters certificate construction or its inequalities.
Road thicknesses 1/10 and 1/5 are algebraic prime factors; logs use positive
atanh series with rational remainders; Euler gamma uses an elementary harmonic
sum enclosure. JSON endpoints are rounded outwards to explicit rational decimals.
"""
from fractions import Fraction as F
from pathlib import Path
import json


def add(x,y): return x[0]+y[0],x[1]+y[1]
def sub(x,y): return x[0]-y[1],x[1]-y[0]
def scale(x,c):
    c=F(c)
    return (c*x[0],c*x[1]) if c>=0 else (c*x[1],c*x[0])
def point(x): return F(x),F(x)
def mul(x,y):
    z=[a*b for a in x for b in y]
    return min(z),max(z)


def atanh_log(z,terms=32):
    """log((1+z)/(1-z)) for rational 0<=z<=1/3."""
    assert 0<=z<=F(1,3)
    acc=F(0)
    zz=z*z; p=z
    for k in range(terms):
        acc+=p/F(2*k+1);p*=zz
    lower=2*acc
    remainder=2*p/(F(2*terms+1)*(1-zz))
    return lower,lower+remainder

LOG2=atanh_log(F(1,3))

def log_integer(n):
    assert n>=1
    k=n.bit_length()-1
    z=F(n-(1<<k),n+(1<<k))
    return add(scale(LOG2,k),atanh_log(z))


def floor_nth_root(n,k):
    assert n>=0 and k>=1
    lo=0; hi=1<<((n.bit_length()+k-1)//k)
    while lo+1<hi:
        mid=(lo+hi)//2
        if mid**k<=n:lo=mid
        else:hi=mid
    if hi**k<=n:lo=hi
    assert lo**k<=n<(lo+1)**k
    return lo


def reciprocal_prime_root(p,k=10,digits=24):
    S=10**digits
    q=floor_nth_root(p*S**k,k)
    return F(S,q+1),F(S,q)


def outward_decimal(x,digits=16):
    S=10**digits
    lo=(x[0].numerator*S)//x[0].denominator
    hi=-((-x[1].numerator*S)//x[1].denominator)
    def decimal(v):
        sign='-' if v<0 else ''
        v=abs(v)
        return f'{sign}{v//S}.{v%S:0{digits}d}'
    return {'lower':decimal(lo),'upper':decimal(hi),'rounding':'OUTWARD_EXACT_RATIONAL'}


def main():
    Y,Z=25,125
    gamma_m=1000
    H=sum((F(1,k) for k in range(1,gamma_m+1)),F(0))
    log_m=log_integer(gamma_m)
    gamma=(H-log_m[1]-F(1,gamma_m),H-log_m[0])
    factors=[[] for _ in range(Z+1)]
    for p in range(2,Z+1):
        if not factors[p]:
            for n in range(p,Z+1,p):factors[n].append(p)
    prime_reciprocals={p:reciprocal_prime_root(p) for p in range(2,Z+1) if factors[p]==[p]}
    A=[point(0),point(0)];B=[point(0),point(0)]
    endpoints=[]
    for n in range(2,Z+1):
        for j,thickness in enumerate([F(1,10),F(1,5)]):
            road=point(1)
            for p in factors[n]:
                r=prime_reciprocals[p]
                if j==1:r=mul(r,r)
                road=mul(road,sub(point(1),r))
            coefficient=scale(road,1/thickness)
            A[j]=add(A[j],scale(coefficient,F(1,n)))
            B[j]=add(B[j],coefficient)
        if n<Y:continue
        common=scale(sub(add(point(1),gamma),log_integer(n)),n)
        g=[add(common,sub(scale(A[j],n),B[j])) for j in (0,1)]
        ca=sub(scale(A[0],2),A[1]);cb=sub(scale(B[0],2),B[1])
        combo=add(common,sub(scale(ca,n),cb))
        endpoints.append((n,g[0],g[1],combo))
    upper_original=[]
    for j in (1,2):
        bound=max(max(endpoints[k][j][1],endpoints[k+1][j][1])+F(1,8*endpoints[k][0]) for k in range(len(endpoints)-1))
        upper_original.append(bound)
        assert bound<0
    lower_combo=min(e[3][0] for e in endpoints)
    assert lower_combo>F(1,6)
    # integral_25^125 y^(-5/2) dy > 1/250; certify sqrt(5)>559/250.
    sqrt5_lower=F(559,250)
    assert sqrt5_lower**2<5
    weight_integral_lower=F(2,3)*(F(1,125)-1/(625*sqrt5_lower))
    assert weight_integral_lower>F(1,250)
    energy_lower=lower_combo**2*weight_integral_lower
    assert energy_lower>F(1,9000)
    result={
      'status':'PASS_EXACT_RATIONAL_CERTIFICATE',
      'window':{'Y':Y,'Z':Z,'lambda':'3/2','theta':'3/4','all_real_points_covered':True},
      'thicknesses':['1/10','1/5'],
      'combination':'2 G_(1/10) - G_(1/5)',
      'arithmetic':'fractions.Fraction only; no floats in certificate inequalities',
      'log_enclosure':'positive atanh series; 32 terms; exact rational upper tail',
      'gamma_enclosure':{'M':gamma_m,**outward_decimal(gamma)},
      'prime_root_enclosure':{'root_degree':10,'decimal_grid_digits':24,'integer_power_bracket_verified':True},
      'integer_endpoints_checked':len(endpoints),
      'unit_cells_checked':len(endpoints)-1,
      'G_h_uniform_upper':outward_decimal(point(upper_original[0])),
      'G_2h_uniform_upper':outward_decimal(point(upper_original[1])),
      'corrected_uniform_lower':outward_decimal(point(lower_combo)),
      'strict_certified_inequalities':['G_(1/10)(y)<0 for every y in [25,125]','G_(1/5)(y)<0 for every y in [25,125]','2G_(1/10)(y)-G_(1/5)(y)>1/6 for every y in [25,125]','positive-part energy of the corrected combination > 1/9000 at theta=3/4'],
      'corrected_energy_lower':outward_decimal(point(energy_lower)),
      'endpoint_enclosures':[{'n':n,'G_h':outward_decimal(gh),'G_2h':outward_decimal(g2h),'corrected':outward_decimal(gc)} for n,gh,g2h,gc in endpoints],
      'scope':'A finite full-road power-window counterexample to positive-part-only control under signed extrapolation. No asymptotic energy bound or RH claim; these fixed thicknesses are not asserted to satisfy the earlier matching schedule.'
    }
    dest=Path(__file__).with_name('positive_window_certificate.json')
    dest.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({k:result[k] for k in ['status','integer_endpoints_checked','unit_cells_checked','G_h_uniform_upper','G_2h_uniform_upper','corrected_uniform_lower','corrected_energy_lower']},ensure_ascii=False))

if __name__=='__main__':main()
