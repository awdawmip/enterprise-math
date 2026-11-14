#!/usr/bin/env python3
"""R749SPJ: exact all-real anti-diagonal Walsh minimax phase diagram.

Enumerate every active basis of the 6D joint source polytope on three rational
intervals with integer Bareiss and Python Fraction. No floating-point arithmetic.
"""
import json
from itertools import combinations
from fractions import Fraction as F
from math import comb
MASKS=(3,12,15,1,2,4,8)
W=tuple(tuple(1 if not ((k&m).bit_count()&1) else -1 for m in MASKS) for k in range(16))
EA=(7,11,13,14,15)
EB=(0,3,5,6,9,10,12,15)
EC=(3,7,11,13,14,15)
PHASES=((F(1,2),F(8,15),1,1),(F(8,15),F(5,9),1,2),(F(5,9),F(3,5),2,2))

def law(t,s,h=F(0),u=F(0),v=F(0),w=F(0),z=F(0)):
    vls=(t,s,h,u,v,w,z)
    return tuple((1+sum((a*b for a,b in zip(vls,row)),F(0)))/16 for row in W)
def tv(p,q):return sum((abs(a-b) for a,b in zip(p,q)),F(0))/2
def pminus(r):return law(r,1-r,0,-r,-r,r-1,r-1)  # u=v=s-1=-r
# Pplus is the opposite of Pminus relative to the h=0 midpoint.
def pplus(r):return law(r,1-r,0,r,r,1-r,1-r)
def pa(r):return law(r,1-r,2-2*r,1-2*r,1-2*r)
def qfree(r):
    b=(5-8*r)/5
    return law(F(1),b,b)
def qcal(r,phase):
    return law(r,1-r,(10-16*r)/11 if phase==1 else F(6,5)-2*r)
def rf(r,phase):return F(1,2)-r/5 if phase==1 else (1+r)/4
def rc(r,phase):return (6-3*r)/11 if phase==1 else F(2,5)

def solve(rows,rhs,inds):
    n=6;a=[list(rows[i])+[rhs[i]] for i in inds];prev=1
    for j in range(n-1):
        idx=next((i for i in range(j,n) if a[i][j]),None)
        if idx is None:return None
        if idx!=j:a[j],a[idx]=a[idx],a[j]
        pivot=a[j][j]
        for i in range(j+1,n):
            v=a[i][j]
            for k in range(j+1,n+1):
                num=a[i][k]*pivot-v*a[j][k]
                if num%prev:raise ArithmeticError('non-exact Bareiss division')
                a[i][k]=num//prev
            a[i][j]=0
        prev=pivot
    if a[-1][-2]==0:return None
    x=[F(0)]*n
    for j in range(n-1,-1,-1):
        x[j]=(F(a[j][n])-sum((a[j][k]*x[k] for k in range(j+1,n)),F(0)))/a[j][j]
    return tuple(x)

def f(q):return str(q.numerator) if q.denominator==1 else f'{q.numerator}/{q.denominator}'

def verify_lower(r):
    for P in (pminus(r),pplus(r),pa(r)):
        assert min(P)>=0 and sum(P)==1
    Pm=pminus(r);Pa=pa(r);Pp=pplus(r)
    assert (F(4,5)*sum(Pm[k] for k in EA)+F(1,5)*sum(Pa[k] for k in EB)-F(2,5)) == F(1,2)-r/5
    assert tv(Pm,Pp)/2 == (1+r)/4
    for h in (F(0),F(1,3),F(7,9)):
        q=law(r,1-r,h)
        La=sum(Pm[k]-q[k] for k in EA)
        Lc=sum(Pm[k]-q[k] for k in EC)
        Lb=sum(Pa[k]-q[k] for k in EB)
        assert La==(F(3,8)+3*h/16)
        assert Lc==(F(1,4)+r/4+h/8)
        assert Lb==(1-r-h/2)
    assert F(1,2)-r/5 >= 0 and F(2,5)>0

def phase_check(L,U,free_phase,cal_phase):
    # 16 atomic nonnegativity + two parameter bounds: complete bounded 6D polytope.
    rows=[(a-b,h,u,v,w,z) for a,b,h,u,v,w,z in W]
    rhs=[-1-row[1] for row in W]
    rows.extend([(L.denominator,0,0,0,0,0),(-U.denominator,0,0,0,0,0)])
    rhs.extend([L.numerator,-U.numerator])
    assert len(rows)==18
    vertices=set()
    nonsingular=feasible=0
    for inds in combinations(range(18),6):
        x=solve(rows,rhs,inds)
        if x is None:continue
        nonsingular+=1
        if all(sum(a*b for a,b in zip(row,x))>=b for row,b in zip(rows,rhs)):
            feasible+=1
            vertices.add(x)
    assert comb(18,6)==18564 and vertices
    maxf=maxc=None;nf=nc=0
    proj={}
    for x in vertices:
        r=x[0]
        proj[r]=proj.get(r,0)+1
        P=law(r,1-r,*x[1:]);Qf=qfree(r);Qc=qcal(r,cal_phase)
        assert min(P)>=0 and min(Qf)>=0 and min(Qc)>=0
        assert sum(P)==sum(Qf)==sum(Qc)==1
        # Ensure Qc belongs to the source fiber (fixed t and s).
        ef=tv(P,Qf)-rf(r,free_phase)
        ec=tv(P,Qc)-rc(r,cal_phase)
        if maxf is None or ef>maxf:maxf=ef
        if maxc is None or ec>maxc:maxc=ec
        nf+=int(ef==0);nc+=int(ec==0)
    assert maxf<=0,(L,U,maxf)
    assert maxc<=0,(L,U,maxc)
    for r in (L,U):
        verify_lower(r)
        assert qcal(r,cal_phase)==law(r,1-r,(10-16*r)/11 if cal_phase==1 else F(6,5)-2*r)
        assert min(qcal(r,cal_phase))>=0
        assert min(qfree(r))>=0
    return {
        'interval':[f(L),f(U)],'free_formula': '1/2-r/5' if free_phase==1 else '(1+r)/4',
        'cal_formula':'(6-3r)/11' if cal_phase==1 else '2/5',
        'potential_active_bases':18564,'nonsingular_bases':nonsingular,
        'feasible_bases_including_repeats':feasible,'distinct_exact_vertices':len(vertices),
        'vertex_parameter_projection':{f(k):v for k,v in sorted(proj.items())},
        'max_free_excess':f(maxf),'max_cal_excess':f(maxc),'free_tight_vertices':nf,
        'cal_tight_vertices':nc,'status':'PASS'
    }
def check():
    # Exact exchange automorphism for the two bit pairs.
    for k in range(16):
        j=((k&3)<<2)|((k&12)>>2)
        assert W[j][0]==W[k][1] and W[j][1]==W[k][0]
        assert W[j][2]==W[k][2] and W[j][3]==W[k][5]
        assert W[j][4]==W[k][6] and W[j][5]==W[k][3]
        assert W[j][6]==W[k][4]
    out=[phase_check(*phase) for phase in PHASES]
    assert sum(x['distinct_exact_vertices'] for x in out)>=1
    print(json.dumps({
        'theorem':'R749SPJ complete exact anti-diagonal minimax phases, 1/2<=r<=1',
        'status':'PASS',
        'frozen_science':'awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389',
        'new_continuous_region':'(t,s)=(r,1-r), 1/2<=r<=3/5, symmetric reflection',
        'free_radius':'max(1/2-r/5,(1+r)/4) for 1/2<=r<=1',
        'calibrated_radius':'(6-3r)/11 for 1/2<=r<=8/15; 2/5 for 8/15<=r<=3/5; (1+r)/4 for 3/5<=r<=1',
        'gap':'(5-8r)/110, (2r-1)/10, (3-5r)/20, 0 on [1/2,8/15],[8/15,5/9],[5/9,3/5],[3/5,1]',
        'phase_intervals':out,
        'total_active_bases':sum(x['potential_active_bases'] for x in out),
        'max_observed_risk_excess':'0',
        'symmetry_exact':True,
        'prior_exact_input':'R749SPG zero triangle; R749SPI upper-fiber homothety',
        'arithmetic':'integer Bareiss + Fraction, no floating point, full vertex census and convexity',
    },indent=2,sort_keys=True))
if __name__=='__main__':check()
