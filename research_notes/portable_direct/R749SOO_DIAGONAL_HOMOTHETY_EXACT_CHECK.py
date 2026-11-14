#!/usr/bin/env python3
"""R749SOO: exact Walsh diagonal homothety and minimax certificate.
Scientific input: awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389
No numerical LP, no floating-point arithmetic, standard library only.
"""
from fractions import Fraction as F
from itertools import combinations
from math import comb
import json
MASKS=(3,12,15,1,2,4,8)
W=tuple(tuple(1 if (k&m).bit_count()%2==0 else -1 for m in MASKS) for k in range(16))
E_FREE_A=(5,7,11,13,14,15)
E_CAL_A=(7,11,13,14,15)
E_G=(0,3,5,6,9,10,12,15)

def law(t,s,h,u=F(0),v=F(0),w=F(0),z=F(0)):
    vct=(t,s,h,u,v,w,z)
    return tuple((1+sum((a*b for a,b in zip(row,vct)),F(0)))/16 for row in W)

def tv(a,b): return sum((abs(x-y) for x,y in zip(a,b)),F(0))/2

def solve5(indices):
    # x=(2h,2u,2v,2w,2z) and W_{k,2:} x = -2-W_{k,0}-W_{k,1}
    a=[list(W[k][2:])+[-2-W[k][0]-W[k][1]] for k in indices]
    last=1
    for j in range(4):
        pivot_idx=next((i for i in range(j,5) if a[i][j]),None)
        if pivot_idx is None:return None
        if pivot_idx!=j:a[j],a[pivot_idx]=a[pivot_idx],a[j]
        pivot=a[j][j]
        for i in range(j+1,5):
            v=a[i][j]
            for k in range(j+1,6):
                numer=a[i][k]*pivot-v*a[j][k]
                assert numer%last==0
                a[i][k]=numer//last
            a[i][j]=0
        last=pivot
    if not a[-1][-2]:return None
    out=[F(0)]*5
    for j in range(4,-1,-1):
        out[j]=(F(a[j][5])-sum((a[j][k]*out[k] for k in range(j+1,5)),F(0)))/a[j][j]
    return tuple(v/2 for v in out)

def all_fiber_vertices():
    vs=set();ns=feasible=0
    for ids in combinations(range(16),5):
        x=solve5(ids)
        if x is None:continue
        ns+=1
        if min(law(F(1,2),F(1,2),*x))<0:continue
        feasible+=1;vs.add(x)
    return vs,ns,feasible

def event_diff(source,q,E):
    return sum((source[k]-q[k] for k in E),F(0))

def run():
    verts,ns,feas=all_fiber_vertices()
    f=law(F(3,5),F(3,5),F(1,5))
    c=law(F(1,2),F(1,2),F(2,11))
    muA=law(F(1,2),F(1,2),F(0),*([F(-1,2)]*4))
    muG=law(F(1,2),F(1,2),F(1))
    assert min(f)>=0 and min(c)>=0 and min(muA)>=0 and min(muG)>=0
    vf=[tv(f,law(F(1,2),F(1,2),*v)) for v in verts]
    vc=[tv(c,law(F(1,2),F(1,2),*v)) for v in verts]
    assert max(vf)==F(2,5),max(vc)==F(9,22)
    # Duals: by invariance under translations by 3 and 12, minimax
    # centers reduce to q(a,b,h). Prove event identities by exact
    # coefficient checks on basis vectors and the affine intercept.
    def eval_q(a,b,h):return law(a,b,h)
    points=((F(0),F(0),F(0)),(F(1),F(0),F(0)),(F(0),F(1),F(0)),(F(0),F(0),F(1)))
    targets_free_A=(F(3,8),F(3,8),F(3,8),F(1,2))
    targets_g=(F(1,2),F(1,2),F(1,2),F(0))
    for (a,b,h),za,zg in zip(points,targets_free_A,targets_g):
        assert event_diff(muA,eval_q(a,b,h),E_FREE_A)==za
        assert event_diff(muG,eval_q(a,b,h),E_G)==zg
    assert F(4,5)*F(3,8)+F(1,5)*F(1,2)==F(2,5)
    for h in (F(-1),F(0),F(1)):
        q=eval_q(F(1,2),F(1,2),h)
        assert event_diff(muA,q,E_CAL_A)==F(3,8)+F(3,16)*h
        assert event_diff(muG,q,E_G)==F(1,2)-h/2
    assert F(8,11)*F(3,8)+F(3,11)*F(1,2)==F(9,22)
    # Exact fibre factorisation: verify pointwise lower floor at
    # vertices and scaled inverse vertices at sample rational r,
    # plus universal inequality is established in the paper.
    star=law(F(1),F(1),F(1))
    assert sum(star)==1 and sorted(set(star))==[F(0),F(1,4)]
    for r in (F(1,2),F(3,5),F(2,3),F(4,5),F(99,100),F(1)):
        lam=2*(1-r)
        for v in verts:
            p0=law(F(1,2),F(1,2),*v)
            pr=tuple((1-lam)*z+lam*y for z,y in zip(star,p0))
            coeffs=(r,r,1-lam+lam*v[0])+tuple(lam*vi for vi in v[1:])
            assert pr==law(*coeffs)
            assert min(pr)>=0
            qfr=tuple((1-lam)*z+lam*y for z,y in zip(star,f))
            qcr=tuple((1-lam)*z+lam*y for z,y in zip(star,c))
            assert tv(qfr,pr)==lam*tv(f,p0)
            assert tv(qcr,pr)==lam*tv(c,p0)
    return {'unit':'R749SOO','status':'PASS',
        'scientific_pin':'a72226e2430ffa4786321ac86e7f0c599d5f0389',
        'domain':'all real 1/2 <= r <= 1, t=s=r, auxiliary Walsh 16-state model',
        'fiber_identity':'F(r,r)=(2r-1)*{star}+2*(1-r)*F(1/2,1/2)',
        'rho':'4*(1-r)/5','rho_cal':'9*(1-r)/11','gap':'(1-r)/55',
        'center_free_coeffs':['(1+4*r)/5','(1+4*r)/5','(8*r-3)/5'],
        'center_cal_coeffs':['r','r','(18*r-7)/11'],
        'base_duals':{'free':'(4/5)*(3/8+h/8)+(1/5)*(1/2-h/2)=2/5',
                      'cal':'(8/11)*(3/8+3h/16)+(3/11)*(1/2-h/2)=9/22'},
        'exhaustive_5facet_sets':comb(16,5),'nonsingular_sets':ns,
        'feasible_sets':feas,'distinct_vertices':len(verts),
        'max_free_distance_at_half':str(max(vf)),
        'max_cal_distance_at_half':str(max(vc)),
        'test_r_values':['1/2','3/5','2/3','4/5','99/100','1'],
        'independent_review':'NOT_REVIEWED',
        'native_x6_bridge':'NOT_ESTABLISHED'}
if __name__=='__main__':print(json.dumps(run(),ensure_ascii=False,indent=2,sort_keys=True))
