#!/usr/bin/env python3
"""R247: exact 21-point rational parameter-grid, two-mode threshold certificate.
Scientific source pinned: enterprise-math@43ec6098b1330ae86d0a7863be336c5d97f6ef34.
All PASS decisions are exact Fraction comparisons; float only for optional display.
"""
from fractions import Fraction as F
from math import lcm
from hashlib import sha256
import json,sys
sys.set_int_max_str_digits(1000000)
W=(144,576,1440,4320,17280,86400,518400)
GRID=tuple(F(j,1000) for j in range(390,411))
TARGETS=((270,100),(403,1000))

def params(s):
    t=(1691*s-2615)/(2615*s-3539)
    alpha=(F(1,5),F(1,4),F(3,10),F(9,20),s,F(2,3),t)
    b=(F(13,60),)+tuple(F(5,18)*abs(F(1,2)-u) for u in alpha[1:])
    pi=tuple(v/(1-u) for u,v in zip(alpha,b))
    assert sum(pi)==1 and all(0<u<1 for u in alpha)
    Z=sum((v/(1-u)**2 for u,v in zip(alpha,b)),F(0))
    rho=tuple(v/(1-u)**2/Z for u,v in zip(alpha,b))
    return alpha,b,pi,Z,rho

def ids(mask):
    return [0]+[i for i in range(1,7) if mask & (1<<(i-1))]

def root_bounds(alpha,b,mask,steps=104):
    index=ids(mask)
    def sec(x):return sum((b[i]/(x-alpha[i]) for i in index), F(0))-1
    low=max(alpha[i] for i in index); high=F(1)
    assert sec(high)<0
    for _ in range(steps):
        mid=(low+high)/2
        if sec(mid)>0:low=mid
        else:high=mid
    assert low<high and sec(low)>0 and sec(high)<0
    return low,high

def amplitude_bounds(alpha,b,Z,mask,l,h):
    index=ids(mask)
    def S(x):return sum((b[i]/((1-alpha[i])*(x-alpha[i])) for i in index),F(0))
    def Q(x):return sum((b[i]/(x-alpha[i])**2 for i in index),F(0))
    w=W[mask.bit_count()]
    return w*S(h)**2/(Z*Q(l)),w*S(l)**2/(Z*Q(h))

def exact_phi(s,npoints):
    alpha,b,pi,Z,rho=params(s)
    C=lcm(*(u.denominator for u in alpha))
    Q=lcm(*(u.denominator for u in pi))
    d=C*Q
    diagonal=[int(d*u) for u in alpha]
    L=[int(C*(1-u)) for u in alpha]
    R=[int(Q*u) for u in pi]
    den=lcm(*(u.denominator for u in rho))
    rho_num=[int(den*u) for u in rho]
    nsteps={n-1 for n in npoints}
    kmax=max(nsteps)
    totals={k:0 for k in nsteps}
    for mask in range(63):
        index=ids(mask)
        v=[1]*len(index)
        wt=W[mask.bit_count()]
        for k in range(kmax+1):
            if k in totals:
                totals[k]+=wt*sum(rho_num[i]*v[j] for j,i in enumerate(index))
            if k<kmax:
                dot=sum(R[i]*v[j] for j,i in enumerate(index))
                v=[diagonal[i]*v[j]+L[i]*dot for j,i in enumerate(index)]
    return {k+1:F(total,den*d**k) for k,total in totals.items()},(alpha,b,Z)

def digest(v):
    assert v!=0
    return {'sign':'positive' if v>0 else 'negative',
            'numerator_bits':abs(v.numerator).bit_length(),
            'denominator_bits':v.denominator.bit_length(),
            'sha256':sha256((str(v.numerator)+'/'+str(v.denominator)).encode()).hexdigest()}

def check(s):
    nvals={n for n,d in TARGETS}
    if s==GRID[-1]:nvals.update({269,402})
    phi,(alpha,b,Z)=exact_phi(s,nvals)
    amps=[]
    for mask in (59,55):
        l,h=root_bounds(alpha,b,mask)
        al,ah=amplitude_bounds(alpha,b,Z,mask,l,h)
        assert 0<al<ah and h<1
        amps.append((l,h,al,ah))
    assert amps[1][1]<amps[0][0]
    def check_case(n,d,expect):
        k=n-1
        Xlo=sum(al*l**k for l,h,al,ah in amps)
        Xhi=sum(ah*h**k for l,h,al,ah in amps)
        assert 0<Xlo<Xhi
        if expect=='below':
            margin=(d+1)*Xlo-d*phi[n]
        else:
            margin=d*phi[n]-(d+1)*Xhi
        assert margin>0,(str(s),n,d,expect,float(margin))
        return {'event':n,'tolerance':f'1/{d}','comparison':expect,'margin':digest(margin)}
    checked=[check_case(n,d,'below') for n,d in TARGETS]
    if s==GRID[-1]:
        checked += [check_case(n-1,d,'above') for n,d in TARGETS]
    return {'s':str(s),'checks':checked}

def main():
    rows=[check(s) for s in GRID]
    result={'schema':'EM_R247_EXACT_21_POINT_TWO_MODE_HORIZONS_V1',
       'frozen_science':'43ec6098b1330ae86d0a7863be336c5d97f6ef34',
       'predecessor':'R246@f27cf3726bb58f2b5705cb80c4b8f48d254011f9',
       'domain':'S={j/1000 : j=390,...,410}; endpoints included',
       'per_point':'63 proper masks; exact integer rank-one propagation; 104 dyadic bisections per root; 2 Perron modes, masks 59/55',
       'uniform_first_1pct':270,'uniform_first_0_1pct':403,
       'meaning':'SHARP_FOR_THIS_FINITE_21_POINT_GRID_ONLY; continuous real interval not certified',
       'certified_comparisons':sum(len(r['checks']) for r in rows),
       'all_pass':True,'review':'NOT_REVIEWED','native_BRC':'NOT_EXECUTED','rows':rows}
    print(json.dumps(result,indent=2,ensure_ascii=False,sort_keys=True))
if __name__=='__main__':main()
