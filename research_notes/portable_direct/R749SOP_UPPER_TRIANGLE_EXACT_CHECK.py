#!/usr/bin/env python3
"""R749SOP: exact common-core decomposition and upper-triangle Walsh phase certificate.
Frozen science: awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389
Proof of universal formula is analytic and depends on R749SOF's exact line theorem.
This check verifies the nonnegative-constraint conic identity and rational fibers.
"""
from fractions import Fraction as F
from itertools import combinations
from math import comb
import json

MASKS=(3,12,15,1,2,4,8)
W=tuple(tuple(1 if (k&m).bit_count()%2==0 else -1 for m in MASKS) for k in range(16))
S=F(0)

def D(a,b,xi,eta):
    return (1,a,b,a*b,xi,a*xi,eta,b*eta)

def avg(forms):
    n=len(forms)
    return tuple(sum((F(x[i]) for x in forms),S)/n for i in range(8))

def add(*forms):
    return tuple(sum((F(x[i]) for x in forms),S) for i in range(8))

def scale(x,c):return tuple(c*F(v) for v in x)

def law(t,s,h,u=S,v=S,w=S,z=S):
    coeffs=(t,s,h,u,v,w,z)
    return tuple((1+sum((F(x)*y for x,y in zip(row,coeffs)),S))/16 for row in W)

def tv(a,b):return sum((abs(x-y) for x,y in zip(a,b)),S)/2

def phase(r,m):
    assert F(0)<=m<=r<=1 and r+m>=1
    if 5*r-4*m<=1: free=(8-5*r-3*m)/10
    else:free=(3-r-2*m)/4
    if 8*r-7*m<=1: cal=(9-6*r-3*m)/11
    elif 3*r-2*m<=1:cal=(4-2*r-2*m)/5
    else:cal=(3-r-2*m)/4
    return free,cal

def centers(r,m):
    assert F(0)<=m<=r<=1 and r+m>=1
    if 5*r-4*m<=1: b=(8*m-3)/5
    else:b=(4*m-1-r)/2
    f=law(F(1),b,b)
    if 8*r-7*m<=1:c=(r+17*m-7)/11
    elif 3*r-2*m<=1:c=(9*m-r-3)/5
    else:c=r+m-1
    return f,law(r,m,c)

def solve5(idx,t,s):
    # At fixed (t,s), unknowns h,u,v,w,z. Bareiss exact integer elimination.
    L=t.denominator*s.denominator//__import__('math').gcd(t.denominator,s.denominator)
    a=[list(W[k][2:])+[-L-int(L*t)*W[k][0]-int(L*s)*W[k][1]] for k in idx]
    prev=1
    for j in range(4):
        pi=next((i for i in range(j,5) if a[i][j]),None)
        if pi is None:return None
        if pi!=j:a[j],a[pi]=a[pi],a[j]
        pv=a[j][j]
        for i in range(j+1,5):
            x=a[i][j]
            for k in range(j+1,6):
                n=a[i][k]*pv-x*a[j][k]
                assert n%prev==0
                a[i][k]=n//prev
            a[i][j]=0
        prev=pv
    if not a[4][4]:return None
    out=[S]*5
    for j in range(4,-1,-1):
        out[j]=(F(a[j][5])-sum((F(a[j][k])*out[k] for k in range(j+1,5)),S))/a[j][j]
    return tuple(x/L for x in out)

def vertices(t,s):
    vs=set();non=feas=0
    for ii in combinations(range(16),5):
        x=solve5(ii,t,s)
        if x is None:continue
        non+=1
        if min(law(t,s,*x))<0:continue
        feas+=1;vs.add(x)
    return vs,non,feas

def main():
    # Identity for all ++ atoms: Dpp-4(t+s-1)=mean(Dpm)+mean(Dmp)+3mean(Dmm).
    for xi in (-1,1):
        for eta in (-1,1):
            rhs=add(avg([D(1,-1,xi,z) for z in (-1,1)]),
                    avg([D(-1,1,z,eta) for z in (-1,1)]),
                    scale(avg([D(-1,-1,x,y) for x in (-1,1) for y in (-1,1)]),3))
            lhs=add(D(1,1,xi,eta),(4,-4,-4,0,0,0,0,0))
            assert lhs==rhs,(xi,eta,lhs,rhs)
    star=law(F(1),F(1),F(1))
    assert sum(star)==1 and sorted(set(star))==[F(0),F(1,4)]
    inputs=[(F(1,2),F(1,2)),(F(5,9),F(4,9)),(F(3,5),F(1,2)),
            (F(7,10),F(1,2)),(F(4,5),F(7,10)),(F(1),F(1,2)),(F(1),F(1))]
    cases=[]
    for r,m in inputs:
        alpha=r+m-1;beta=2-r-m
        f,c=centers(r,m)
        rf,rc=phase(r,m)
        assert min(f)>=0 and min(c)>=0 and rc>=rf
        if beta:
            a=(1-m)/beta;b=(1-r)/beta
            assert a+b==1
            base=law(a,b,F(0),a,a,b,b)
            assert min(base)>=0 and sum(base)==1
            needle=tuple(alpha*x+beta*y for x,y in zip(star,base))
            assert needle==law(r,m,alpha,beta*a,beta*a,beta*b,beta*b)
            assert any(needle[k]==alpha*star[k] for k in (0,3,12,15))
            for k in (0,3,12,15):
                assert min(needle[j] for j in range(16) if W[j][0]==1 and W[j][1]==1)==alpha/4
                assert needle[15]==alpha/4
            vt,non,feas=vertices(r,m)
            assert vt
            mf=max(tv(f,law(r,m,*v)) for v in vt)
            mc=max(tv(c,law(r,m,*v)) for v in vt)
            assert mf==rf and mc==rc,(r,m,mf,rf,mc,rc)
            cases.append({'r':str(r),'m':str(m),'beta':str(beta),'vertex_count':len(vt),
                          'non_singular_bases':non,'feasible_bases':feas,
                          'rho':str(rf),'rho_cal':str(rc),'gap':str(rc-rf)})
        else:
            assert f==c==star and rf==rc==0
            cases.append({'r':'1','m':'1','fiber':'singleton','rho':'0','rho_cal':'0','gap':'0'})
    assert phase(F(5,9),F(4,9))==(F(7,18),F(2,5))
    assert phase(F(1,2),F(1,2))==(F(2,5),F(9,22))
    return {'unit':'R749SOP','status':'PASS','scientific_pin':'a72226e2430ffa4786321ac86e7f0c599d5f0389',
        'region':'0<=t,s<=1, t+s>=1; put r=max(t,s), m=min(t,s)',
        'common_floor':'(t+s-1)*sigma','sigma_support':[0,3,12,15],
        'conic_identity':'Dpp-4(t+s-1)=mean(Dpm)+mean(Dmp)+3mean(Dmm)',
        'fiber_factorization':'F(t,s)=alpha*sigma+beta*F((1-s)/beta,(1-t)/beta)',
        'radii_reduction':'rho and rho_cal, and their difference, multiply by beta',
        'free_phase_threshold':'5*r-4*m=1','calibration_thresholds':['8*r-7*m=1','3*r-2*m=1'],
        'phase_gap_zero':'3*r-2*m>=1','max_gap':'1/90','maximizers':['(5/9,4/9)','(4/9,5/9)'],
        'exact_fixed_parameter_bases_each':comb(16,5),'exact_checks':cases,
        'proof_scope':'analytic common-mass factorization, SOF exact 1D input, rational vertex checks',
        'independent_review':'NOT_REVIEWED','native_x6_correspondence':'UNRESOLVED'}

if __name__=='__main__':print(json.dumps(main(),ensure_ascii=False,indent=2,sort_keys=True))
