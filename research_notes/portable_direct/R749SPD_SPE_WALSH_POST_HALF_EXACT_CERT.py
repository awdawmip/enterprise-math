#!/usr/bin/env python3
"""R749SPD-SPE: extended exact Walsh slice with two calibrated-center phases.
Frozen scientific input: enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389.
Pure Python 3 standard library, exact integer Bareiss + Fraction.
"""
from fractions import Fraction as F
from itertools import combinations
from math import comb
import json

MASKS=(3,12,15,1,2,4,8)
W=tuple(tuple(1 if ((k&m).bit_count() & 1)==0 else -1 for m in MASKS) for k in range(16))
S=F(3,5); L=F(2,5); U=F(1,2)
E1=(7,11,12,13,14,15)
E2=(0,3,5,6,9,10,12,15)

def law(t,s,h=F(0),u=F(0),v=F(0),w=F(0),z=F(0)):
    c=(t,s,h,u,v,w,z)
    return tuple((1+sum((a*b for a,b in zip(c,row)),F(0)))/16 for row in W)

def tv(p,q):
    return sum((abs(x-y) for x,y in zip(p,q)),F(0))/2

def source_pair(t):
    h=t-L
    return (law(t,S,h,F(2,5),F(2,5),1-t,1-t),
            law(t,S,h,-F(2,5),-F(2,5),t-1,t-1))

def source_two(t):
    return law(t,S,t+L,F(0),F(0),t-S,t-S)

def free_center(t):
    d=2*t-2*L
    return law(d,1,d)

def calibrated_center(t):
    return law(t,S,F(9,5)*(t-L))

def free_radius(t):return S-t/2
def calibrated_radius(t):return F(14,25)-F(2,5)*t

def solve_bareiss(rows,rhs,idx):
    n=6
    a=[list(rows[i])+[rhs[i]] for i in idx]
    prev=1
    for j in range(n-1):
        piv=next((i for i in range(j,n) if a[i][j]!=0),None)
        if piv is None:return None
        if piv!=j:a[j],a[piv]=a[piv],a[j]
        pivot=a[j][j]
        for i in range(j+1,n):
            factor=a[i][j]
            for k in range(j+1,n+1):
                numerator=a[i][k]*pivot-factor*a[j][k]
                assert numerator%prev==0
                a[i][k]=numerator//prev
            a[i][j]=0
        prev=pivot
    if a[n-1][n-1]==0:return None
    x=[F(0)]*n
    for j in range(n-1,-1,-1):
        x[j]=(F(a[j][n])-sum((a[j][i]*x[i] for i in range(j+1,n)),F(0)))/a[j][j]
    return tuple(x)


# New R749SPD-SPE certification: all rational arithmetic, no floating point.
EA=(7,11,13,14,15)
EB=E2
E1=(7,11,12,13,14,15)
def PM(t):return source_pair(t)[1]
def PT(t):return source_two(t)
def qfree(t):
    a=F(8,5)*t-F(3,5)
    return law(a,F(1),a)
def qcal(t,phase):
    h=F(9,5)*(t-F(2,5)) if phase==1 else (85*t-32)/55
    return law(t,F(3,5),h)
def rf(t):return F(1,2)-F(3,10)*t
def rc(t,phase):
    return F(14,25)-F(2,5)*t if phase==1 else F(27,55)-F(3,11)*t
def ev(p,E):return sum((p[k] for k in E),F(0))
def endpoints_check(lower,upper,phase):
    checks=[]
    for t in (lower,upper):
        pm=PM(t);pt=PT(t);qf=qfree(t);qc=qcal(t,phase)
        h=F(9,5)*(t-F(2,5)) if phase==1 else (85*t-32)/55
        for p in (pm,pt,qf,qc):
            assert min(p)>=0 and sum(p)==1
        assert ev(pm,EA)==F(19,20)-t/2
        assert ev(pt,EB)==F(7,10)+t/2
        assert tv(pm,qf)==rf(t) and tv(pt,qf)==rf(t)
        assert tv(pm,qc)==rc(t,phase) and tv(pt,qc)==rc(t,phase)
        if phase==1:
            assert ev(pm,E1)-ev(qc,E1)==F(13,20)-F(5,8)*t+h/8==rc(t,phase)
        else:
            assert ev(pm,EA)-ev(qc,EA)==F(3,5)-F(9,16)*t+F(3,16)*h==rc(t,phase)
        assert ev(pt,EB)-ev(qc,EB)==F(1,5)+t/2-h/2==rc(t,phase)
        checks.append({'t':str(t),'rho':str(rf(t)), 'rho_cal':str(rc(t,phase)),
                       'gap':str(rc(t,phase)-rf(t)), 'h_cal':str(h),
                       'min_center_atom':str(min(qf+qc))})
    # The group G translating the four sign blocks preserves the source fiber.
    # In order (--),(-+),(+-),(++), event atom counts:
    blocks=[tuple(k for k,row in enumerate(W) if row[0]==a and row[1]==b)
            for a,b in [(-1,-1),(-1,1),(1,-1),(1,1)]]
    assert [[len(set(E)&set(block)) for block in blocks]
            for E in (EA,EB)]==[[0,2,2,1],[4,0,0,4]]
    # Thus for any G-invariant free q, with per-atom class masses x_0...x_3:
    # 4/5*(PM(EA)-q(EA)) + 1/5*(PT(EB)-q(EB))
    # = 1/2-3*t/10+4*x_0/5 >= 1/2-3*t/10.
    # Both calibrated event identities are affine in (t,h):
    for t in (lower,upper):
        for h in (-F(1),F(1)):
            q=law(t,S,h)
            if phase==1:
                assert ev(PM(t),E1)-ev(q,E1)==F(13,20)-F(5,8)*t+h/8
            else:
                assert ev(PM(t),EA)-ev(q,EA)==F(3,5)-F(9,16)*t+F(3,16)*h
            assert ev(PT(t),EB)-ev(q,EB)==F(1,5)+t/2-h/2
    return checks

def upper_check(lower,upper,phase):
    # Six variables (t,h,u,v,w,z); atom rows multiply by 35.
    rows=[];rhs=[]
    for r in W:
        rows.append(tuple(35*r[i] for i in (0,2,3,4,5,6)))
        rhs.append(-35-21*r[1])
    assert lower in (F(1,2),F(19,35))
    if phase==1:
        rows.extend([(2,0,0,0,0,0),(-35,0,0,0,0,0)])
        rhs.extend([1,-19])
    else:
        rows.extend([(35,0,0,0,0,0),(-5,0,0,0,0,0)])
        rhs.extend([19,-3])
    assert len(rows)==18
    vertices=set();nonsingular=feasible=0
    for idx in combinations(range(18),6):
        x=solve_bareiss(rows,rhs,idx)
        if x is None:continue
        nonsingular+=1
        if any(sum((a*b for a,b in zip(r,x)),F(0))<c for r,c in zip(rows,rhs)):
            continue
        feasible+=1;vertices.add(x)
    assert vertices
    hist={}; ef=[];ec=[]
    for t,h,u,v,w,z in vertices:
        p=law(t,S,h,u,v,w,z)
        f=qfree(t);c=qcal(t,phase)
        for d in (p,f,c):assert sum(d)==1 and min(d)>=0
        x=tv(p,f)-rf(t);y=tv(p,c)-rc(t,phase)
        assert x<=0 and y<=0, (str(t),str(x),str(y))
        ef.append(x);ec.append(y)
        hist[str(t)]=hist.get(str(t),0)+1
    assert max(ef)==max(ec)==0
    assert set(hist)=={str(lower),str(upper)}
    return {'active_bases':comb(18,6),'nonsingular':nonsingular,
      'feasible_including_repetition':feasible,'distinct_vertices':len(vertices),
      'vertex_t_histogram':dict(sorted(hist.items())),
      'free_tight_vertices':sum(x==0 for x in ef),
      'cal_tight_vertices':sum(y==0 for y in ec),
      'max_free_excess':str(max(ef)),'max_cal_excess':str(max(ec))}

def main():
    phases=[]
    for name,lower,upper,phase in [('SPD',F(1,2),F(19,35),1),
                                   ('SPE',F(19,35),F(3,5),2)]:
        phases.append({'name':name,'domain':[str(lower),str(upper)],
          'lower_endpoint_event_checks':endpoints_check(lower,upper,phase),
          'complete_joint_polytope':upper_check(lower,upper,phase)})
    return {'status':'PASS','research_ids':['R749SPD','R749SPE'],
      'frozen_science':'awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389',
      'scope':'auxiliary 16-atom Walsh all real t in [1/2,3/5], s=3/5',
      'free_radius':'1/2-3*t/10',
      'cal_radius_1':'14/25-2*t/5 on [1/2,19/35]',
      'cal_radius_2':'27/55-3*t/11 on [19/35,3/5]',
      'gap_1':'3/50-t/10','gap_2':'(3*t-1)/110',
      'free_center':'p(8*t/5-3/5,1,8*t/5-3/5,0,0,0,0)',
      'cal_h1':'9/5*(t-2/5)','cal_h2':'(85*t-32)/55',
      'lower':'weighted event free bound; two-event calibrated bounds',
      'upper':'exact integer Bareiss 18 choose 6, convexity on two joint polytopes',
      'review':'AUTHOR_EXACT_NOT_REVIEWED','native_transfer':'OPEN','phases':phases}
if __name__=='__main__':
    print(json.dumps(main(),ensure_ascii=False,sort_keys=True,indent=2))
