#!/usr/bin/env python3
"""R749SPF: exact full right-half s=3/5 Walsh minimax diagram.
Frozen science: awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389.
Standard-library-only integer Bareiss and Fraction certificate; no numerical LP.
"""
import json
from fractions import Fraction as F
from itertools import combinations
from math import comb

MASKS=(3,12,15,1,2,4,8)
W=tuple(tuple(1 if ((k&m).bit_count()&1)==0 else -1 for m in MASKS) for k in range(16))
S=F(3,5)
EA=(7,11,13,14,15)
EC=(3,7,11,13,14,15)
EB=(0,3,5,6,9,10,12,15)

def p(t,s,h=0,u=0,v=0,w=0,z=0):
    return tuple((1+sum((a*b for a,b in zip((t,s,h,u,v,w,z),row)),F(0)))/16 for row in W)

def tv(x,y):return sum((abs(a-b) for a,b in zip(x,y)),F(0))/2

def ev(x,E):return sum((x[i] for i in E),F(0))

def pm(t):return p(t,S,t-F(2,5),-F(2,5),-F(2,5),t-1,t-1)
def pp(t):return p(t,S,t-F(2,5), F(2,5), F(2,5),1-t,1-t)
def pa(t):return p(t,S,F(8,5)-t,S-t,S-t,0,0)

def fc(t,phase):
    if phase in ('A','B'):return p(1,F(9,25),F(9,25))
    if phase=='C':return p(1,2*t-1,2*t-1)
    return p(t,S,t-F(2,5))

def cc(t,phase):
    if phase=='A':h=(5*t+16)/55
    elif phase in ('B','C'):h=(12-5*t)/25
    else:h=t-F(2,5)
    return p(t,S,h)

def rf(t,phase):return F(31,50)-t/2 if phase in ('A','B') else F(9,20)-t/4

def rc(t,phase):
    if phase=='A':return F(36,55)-6*t/11
    if phase in ('B','C'):return F(14,25)-2*t/5
    return F(9,20)-t/4

def solve(rows,rhs,pick):
    n=6;a=[list(rows[i])+[rhs[i]] for i in pick];old=1
    for j in range(n-1):
        ii=next((i for i in range(j,n) if a[i][j]),None)
        if ii is None:return None
        if ii!=j:a[ii],a[j]=a[j],a[ii]
        pivot=a[j][j]
        for i in range(j+1,n):
            factor=a[i][j]
            for k in range(j+1,n+1):
                numer=a[i][k]*pivot-factor*a[j][k]
                assert numer%old==0
                a[i][k]=numer//old
            a[i][j]=0
        old=pivot
    if a[n-1][n-1]==0:return None
    x=[F(0)]*n
    for j in range(n-1,-1,-1):
        x[j]=(F(a[j][n])-sum((a[j][i]*x[i] for i in range(j+1,n)),F(0)))/a[j][j]
    return tuple(x)

def endpoint_lower(t,phase):
    Pm,Pp,Pa=pm(t),pp(t),pa(t)
    for src in (Pm,Pp,Pa):assert sum(src)==1 and min(src)>=0
    free,cal=fc(t,phase),cc(t,phase)
    for q in (free,cal):assert sum(q)==1 and min(q)>=0
    # Exact affine free lower: G-invariant q has block masses x0..x3, 4*sum(x)=1.
    # A/B: 4/5(Pm(EA)-q(EA))+1/5(Pa(EB)-q(EB)) = 31/50-t/2+4*x0/5.
    assert ev(Pm,EA)==F(19,20)-t/2
    assert ev(Pa,EB)==F(13,10)-t/2
    # C/D: Pm(EC)-q(EC)=9/20-t/4+2*x0.
    assert ev(Pm,EC)==F(19,20)-t/4
    # Calibrated center lower from two events. Identities tested for arbitrary h.
    for h in (-F(1), F(0), F(1)):
        q=p(t,S,h)
        assert ev(Pm,EA)-ev(q,EA)==F(3,5)-F(9,16)*t+F(3,16)*h
        assert ev(Pm,EC)-ev(q,EC)==F(1,2)-F(3,8)*t+h/8
        assert ev(Pa,EB)-ev(q,EB)==F(4,5)-t/2-h/2
    if phase=='A':
        h=(5*t+16)/55
        assert ev(Pm,EA)-ev(p(t,S,h),EA)==rc(t,phase)
        assert ev(Pa,EB)-ev(p(t,S,h),EB)==rc(t,phase)
    elif phase in ('B','C'):
        h=(12-5*t)/25
        assert ev(Pm,EC)-ev(p(t,S,h),EC)==rc(t,phase)
        assert ev(Pa,EB)-ev(p(t,S,h),EB)==rc(t,phase)
    else:
        assert tuple((x+y)/2 for x,y in zip(Pp,Pm))==cal==free
        assert tv(Pp,Pm)==2*rc(t,phase)
    return {'t':str(t),'rho':str(rf(t,phase)),'rho_cal':str(rc(t,phase)),
            'gap':str(rc(t,phase)-rf(t,phase))}

def check_phase(phase,left,right):
    # 16 Walsh atom inequalities, two interval inequalities, 6 variables (t,h,u,v,w,z).
    # Multiply all source inequalities by 15 and t bounds by lcm of their denominators.
    rows=[];rhs=[]
    for row in W:
        rows.append(tuple(15*row[i] for i in (0,2,3,4,5,6)))
        rhs.append(-15-9*row[1])
    den=left.denominator*right.denominator
    rows.extend([(den,0,0,0,0,0),(-den,0,0,0,0,0)])
    rhs.extend([int(den*left),-int(den*right)])
    vertices=set(); nonsingular=feasible=0
    for pick in combinations(range(18),6):
        x=solve(rows,rhs,pick)
        if x is None:continue
        nonsingular+=1
        if any(sum((a*b for a,b in zip(r,x)),F(0))<b for r,b in zip(rows,rhs)):
            continue
        feasible+=1;vertices.add(x)
    assert vertices
    maxfree=maxcal=None;hist={};tightfree=tightcal=0
    for t,h,u,v,w,z in vertices:
        source=p(t,S,h,u,v,w,z);free=fc(t,phase);cal=cc(t,phase)
        for x in (source,free,cal):assert min(x)>=0 and sum(x)==1
        excessf=tv(source,free)-rf(t,phase)
        excessc=tv(source,cal)-rc(t,phase)
        assert excessf<=0 and excessc<=0,(phase,t,excessf,excessc)
        maxfree=excessf if maxfree is None else max(maxfree,excessf)
        maxcal=excessc if maxcal is None else max(maxcal,excessc)
        tightfree+=int(excessf==0);tightcal+=int(excessc==0)
        hist[str(t)]=hist.get(str(t),0)+1
    assert maxfree==maxcal==0
    return {'phase':phase,'domain':[str(left),str(right)],
        'endpoints':[endpoint_lower(t,phase) for t in (left,right)],
        'active_bases':comb(18,6),'nonsingular_bases':nonsingular,
        'feasible_bases_including_repetition':feasible,'distinct_vertices':len(vertices),
        'parameter_histogram':dict(sorted(hist.items())),
        'tight_free_vertices':tightfree,'tight_cal_vertices':tightcal,
        'max_free_excess':str(maxfree),'max_cal_excess':str(maxcal)}

def main():
    phases=[('A',F(3,5),F(13,20)),('B',F(13,20),F(17,25)),
            ('C',F(17,25),F(11,15)),('D',F(11,15),F(1))]
    # Four G orbits ordered (--),(-+),(+-),(++); exact event incidence counts.
    blocks=[set(k for k,row in enumerate(W) if row[0]==a and row[1]==b)
            for a,b in [(-1,-1),(-1,1),(1,-1),(1,1)]]
    assert [len(b) for b in blocks]==[4]*4
    assert [[len(set(E)&B) for B in blocks] for E in (EA,EB,EC)]==[
        [0,2,2,1],[4,0,0,4],[0,2,2,2]]
    return {'schema':'R749SPF_FULL_RIGHT_WALSH_V1','status':'PASS',
        'frozen_science':'awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389',
        'model':'complete 16-atom auxiliary Walsh fiber, s=3/5, all real t in [3/5,1]',
        'method':'four-orbit BRC symmetrization, exact event lower bounds, complete 6D joint-vertex upper bounds',
        'review':'AUTHOR_EXACT_NOT_REVIEWED','native_transfer':'OPEN',
        'phases':[check_phase(*phase) for phase in phases]}

if __name__=='__main__':
    print(json.dumps(main(),ensure_ascii=False,indent=2,sort_keys=True))
