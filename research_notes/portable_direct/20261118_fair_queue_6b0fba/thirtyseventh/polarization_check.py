"""Exact finite Gauss sums and independent energy-momentum feasibility checks."""
import cmath
from collections import Counter
from fractions import Fraction as F
from functools import lru_cache
from itertools import product
import json
from math import cos, gcd, pi, sin, sqrt


def remainder(polynomial, monic):
    a = list(polynomial)
    for pos in range(len(a)-1, len(monic)-2, -1):
        c=a[pos]
        if c:
            for j,v in enumerate(monic):
                a[pos+1-len(monic)+j]-=c*v
    return a[:len(monic)-1]


def divide(poly, divisor):
    a=list(poly)
    q=[0]*(len(a)-len(divisor)+1)
    for i in reversed(range(len(q))):
        q[i]=a[i+len(divisor)-1]
        for j,coeff in enumerate(divisor):
            a[i+j]-=q[i]*coeff
    assert not any(a)
    return q


@lru_cache(None)
def cyclotomic(n):
    factors=[-1]+[0]*(n-1)+[1]
    for d in range(1,n):
        if n%d==0:
            factors=divide(factors,cyclotomic(d))
    return tuple(factors)


def gauss_audit():
    result=Counter()
    for n in range(1,37):
        ring=cyclotomic(n)
        for r,l in product(range(n),repeat=2):
            phase=Counter((r*j*j+l*j)%n for j in range(n))
            tensor=[0]*n
            for a,m in phase.items():
                for b,t in phase.items():
                    tensor[(a-b)%n]+=m*t
            d=gcd(2*r,n)
            predicted=n*d if (l+r*(n//d))%d==0 else 0
            tensor[0]-=predicted
            assert not any(remainder(tensor,ring))
            result["nonzero" if predicted else "zero"]+=1
    return {"N_range":[1,36],"exact_cyclotomic_intensity_tests":dict(result)}


def bandwidth_audit():
    # Uniform in squared energy y on [1,4]. The integral is checked by an independent sum.
    errors=[]
    n=4096
    for k in (0.25,1.,2.,pi,8.):
        target=cmath.exp(2.5j*k)*sin(1.5*k)/(1.5*k)
        estimate=sum(cmath.exp(1j*k*(1+3*(i+.5)/n)) for i in range(n))/n
        err=abs(estimate-target)
        assert err < k*3/(4*n)
        errors.append(round(err,12))
    # Exact extrema for two antipodal samples, a common source angle, p_j in [0,1].
    assert max(abs(p1-p2)/2 for p1,p2 in product((0,1),repeat=2))==F(1,2)
    cone=[]
    for t in (F(0),F(1,10),F(1,5),F(1,4),F(1,3),F(1,2),F(1)):
        # tan(epsilon/2)=t. At the antipodal two-bin extrema choose zero amplitude
        # or a unit vector rotated towards the other channel.
        c=(1-t*t)/(1+t*t)
        s=2*t/(1+t*t)
        choices=((F(0),F(0)),(c,s),(c,-s))
        max_square=max(((a-x)**2+(b-y)**2)/4 for (a,b),(x,y) in product(choices,repeat=2))
        assert max_square==max(F(1,4),s*s)
        cone.append([str(t),str(max_square)])
    alias_rows=[]
    for ns in ((3,4,5),(3,5,7),(2,4,6),(3,3,3)):
        ds=[m*m-ns[0]**2 for m in ns]
        g=gcd(*ds)
        for b in range(1,25):
            for a in range(1,b+1):
                alias=all((a*d)%b==0 for d in ds)
                assert alias==((a*g)%b==0)
        alias_rows.append({"frequency_indices":ns,"gcd_of_square_differences":g})
    return {"continuous_midpoint_bins":n,"uniform_squared_energy_max_abs_errors":errors,
            "antipodal_nuisance_tan_halfwidth_and_max_power":cone,"discrete_phase_aliases":alias_rows,"opposite_equal_weight_amplitude_nuisance_max":"1/2"}


def two_baselines():
    # Exact angles are measured in turns; b_over_pi=b/pi. Gains are positive.
    lenses=(2,5)
    frequencies=(F(1,2),F(3,2),F(5,2))
    source=(F(1,13),F(3,11),F(-2,7))
    instrument=(F(1,17),F(-1,19))
    def read(b_over_pi):
        raw=[[src+instrument[i]+b_over_pi*lenses[i]*e*e
              for e,src in zip(frequencies,source)] for i in range(2)]
        return [(raw[1][j]+raw[0][0]-raw[0][j]-raw[1][0])%1 for j in range(3)]
    b=F(1,100)
    observed=read(b)
    assert observed==[0,F(3,50),F(9,50)]
    assert read(b+F(1,6))==observed and read(b+F(1,12))!=observed
    ntests=0
    for d in range(1,16):
        for a in range(1,20):
            if gcd(a,d)==1:
                assert gcd(*(d*j*j+2*a*j for j in range(7)))==gcd(d+2*a,2*d)
                ntests+=1
    return {"L":lenses,"energy":list(map(str,frequencies)),"source_turns":list(map(str,source)),
            "instrument_turns":list(map(str,instrument)),"b_over_pi":str(b),"alias_spacing_in_b_over_pi":"1/6",
            "double_ratio_turns":list(map(str,observed)), "offset_grid_gcd_tests":ntests}


def vc_predicate(p,k,energy,c,m):
    gap=(c*k)**2-energy**2
    a=c*(2*p-k)
    return gap>0 and a>=0 and a*a*gap>=energy**2*(gap+4*m*m)


def vc_geometric(p,ep,k,energy,c,m):
    ef=ep-energy
    if ef<m:
        return False
    final_sq=(ef*ef-m*m)/(c*c)
    return (p-k)**2<=final_sq<=(p+k)**2


def kinematics():
    cases=Counter()
    models=(F(-1,20),F(0),F(1,20))
    for a,b,c,m,e in product(models,models,(F(4,5),F(1),F(6,5)),(F(1,2),F(1)),(F(1),F(2),F(3))):
        for s in (-1,1):
            ell=a+s*b
            k=e+ell*e*e
            assert k>0 and 1+2*ell*e>0
            # Check fixed-k energy minimum against many longitudinal momentum splittings.
            delta=e**2-(c*k)**2-4*m*m
            transverse_sq=delta/(4*c*c)
            if transverse_sq>=0:
                assert 4*(m*m+c*c*((k/2)**2+transverse_sq))==e*e
            for t in range(-4,13):
                y=F(t,8)
                left=m*m+(c*k*y)**2
                right=m*m+(c*k*(1-y))**2
                z=e*e-left-right
                allowed=z>=0 and z*z>=4*left*right
                assert not allowed or delta>=0
                if y==F(1,2):
                    assert allowed==(delta>=0)
            cases["pair_allowed" if delta>=0 else "pair_forbidden"]+=1
            # Rational rapidity gives exact electron momentum and energy.
            for u in (F(1),F(3,2),F(2),F(3),F(5),F(8),F(15)):
                p=m*(u-1/u)/(2*c)
                ep=m*(u+1/u)/2
                direct=vc_geometric(p,ep,k,e,c,m)
                assert direct==vc_predicate(p,k,e,c,m)
                cases["cherenkov_allowed" if direct else "cherenkov_forbidden"]+=1
    # Construct exact forward-emission thresholds from independently chosen electron states.
    boundary=0
    for c,m,u,v in product((F(4,5),F(1),F(6,5)),(F(1,2),F(1)),(F(2),F(3),F(5)),(F(2,3),F(1),F(3,2))):
        p=m*(u-1/u)/(2*c)
        p2=m*(v-1/v)/(2*c)
        ee=m*(u+1/u)/2
        energy=ee-m*(v+1/v)/2
        k=p-p2
        assert energy>0 and k>0 and 2*k>energy
        j=(c*k)**2-energy**2
        assert c*c*(2*p-k)**2*j==energy**2*(j+4*m*m)
        assert vc_geometric(p,ee,k,energy,c,m) and vc_predicate(p,k,energy,c,m)
        assert not vc_predicate(p-F(1,10000),k,energy,c,m)
        boundary+=1
    return {"rational_tests":dict(cases),"constructed_exact_cherenkov_boundaries":boundary,
            "toy_energy":3,"toy_m":"1/2","toy_b":"1/20",
            "k_plus":"69/20","k_minus":"51/20",
            "pair_gap_minus_at_c1":str(F(9)-(F(51,20))**2-1),
            "pair_gap_minus_at_c6_over5":str(F(9)-(F(6,5)*F(51,20))**2-1)}


if __name__=="__main__":
    print(json.dumps({"gauss":gauss_audit(),"band":bandwidth_audit(),"two_baselines":two_baselines(),"reactions":kinematics()},indent=2,sort_keys=True))
