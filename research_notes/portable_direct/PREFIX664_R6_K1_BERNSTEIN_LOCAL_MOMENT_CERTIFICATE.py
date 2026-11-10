#!/usr/bin/env python3
"""PREFIX-664: exact k=1 Bernstein layer, local-mean BRC edge-strip certificate.
Frozen scientific pin f42f2906d77f24085c123f3ccfe9667d41caa96d.
"""
from functools import lru_cache
from fractions import Fraction as F
from math import comb
import json

N,D=189,2**18
EPS=F(1,2**15)
Q=F(19,128)
JLO,JHI=F(607,4096),F(609,4096)
checks=0

def ck(flag,label):
    global checks
    assert flag,label
    checks+=1

@lru_cache(None)
def inside(n,k,a):
    return 40*(n+1)*comb(n,k)*a**k*(D-a)**(n-k)>D**n

@lru_cache(None)
def wide(n,k):
    if k>n//2:return wide(n,n-k)
    mid=k*D//n
    ck(inside(n,k,mid),('central',n,k))
    if k==0:ll=lh=0
    else:
        lo,hi=0,mid
        while hi-lo>1:
            m=(lo+hi)//2
            if inside(n,k,m):hi=m
            else:lo=m
        ll,lh=lo,hi
    lo,hi=mid,D
    while hi-lo>1:
        m=(lo+hi)//2
        if inside(n,k,m):lo=m
        else:hi=m
    rl,rh=lo,hi
    if 4*(rl-lh)>D:return True
    if 4*(rh-ll)<D:return False
    raise AssertionError(('ambiguous',n,k))

def certificate():
    row=[1,0,0,0];rows=[tuple(row)]
    for n in range(1,N):
        row=[((row[k] if k<=n-1 else 0)+(row[k-1] if 0<k<=n else 0))
             if k<=n else 0 for k in range(4)]
        row=[v if wide(n,k) else 0 for k,v in enumerate(row) if k<=n]+[0]*max(0,3-n)
        rows.append(tuple(row))
    ck(len(rows)==N,'189 rows')
    ck(all(rows[n][k]==comb(n,k) for n in range(4,25) for k in range(4)),'initial complete rows')
    ck(all(rows[n][k]==0 for n in range(42,N) for k in range(3)),'k<=2 tail')
    ck(all(rows[n][3]==0 for n in range(49,N)),'k=3 tail')
    ck(rows[48][3]>0 and rows[49][3]==0,'k=3 cutoff')
    deltas=[]
    for n in range(2,N):
        f=[F(rows[n][k],comb(n,k)) for k in range(min(n+1,4))]
        d0=f[2]-2*f[1]+f[0]
        d1=f[3]-2*f[2]+f[1] if n>=3 else F(0)
        deltas.append((n,d0,d1))
    A0=sum(n*(n-1)*abs(d0) for n,d0,d1 in deltas)
    A1=sum(n*(n-1)*(n-2)*abs(d1) for n,d0,d1 in deltas)
    B2=sum(n*(n-1)*(n-2)*(n-3) for n,d0,d1 in deltas)
    C0=sum((n+1)*n*(n-1)*abs(d0) for n,d0,d1 in deltas)
    C1=sum((n+1)*n*(n-1)*(n-2)*abs(d1) for n,d0,d1 in deltas)
    E2=sum((n+1)*n*(n-1)*(n-2)*(n-3) for n,d0,d1 in deltas)
    ck((A0,A1,B2,C0,C1,E2)==(13800,670800,45727338888,485400,28815600,7240161990600),'exact budgets')
    ck(JLO<Q<JHI and Q-JLO==F(1,4096) and JHI-Q==F(1,4096),'band center')
    ck(JLO>=F(63,512) and JHI<=F(1,6),'interior score domain')
    ck(4*21**2*JLO*(1-JLO)>188,'score derivative strictly below 21')
    mu_pp=A0+A1*EPS+B2*EPS**2
    H_pp=C0+C1*EPS+E2*EPS**2
    mu_p=225+A0*EPS+F(A1,2)*EPS**2+F(B2,3)*EPS**3
    mu_upper=F('89.456')+F(3969,4096)+EPS*mu_p
    ck(mu_upper<91,'mu uniformly below 91')
    W_pp=2*H_pp+2*mu_p**2+2*F(91)*mu_pp
    K=576*W_pp+24*mu_pp
    loss=EPS*K
    ck(loss<64000,'new gradient loss < 64000')
    ck(-76650+loss< -12650,'strict negative derivative')
    ck(EPS/F(1,2**17)==4,'fourfold over PREFIX-663')
    ck(EPS/F(1,2**21)==64,'64-fold over PREFIX-662')
    ck(EPS/F(1,2**30)==32768,'32768-fold over PREFIX-661')
    return {
      'schema':'EM_PREFIX664_R6_K1_BERNSTEIN_LOCAL_MEAN_STRIP_V1',
      'date':'2026-11-10',
      'frozen_scientific_pin':'f42f2906d77f24085c123f3ccfe9667d41caa96d',
      'domain':{'p':['0','1/32768'],'z':['607/4096','609/4096'],'q':['12','24']},
      'integer_budgets':{'A0':str(A0),'A1':str(A1),'B2':str(B2),'C0':str(C0),'C1':str(C1),'E2':str(E2)},
      'mean_uniform_upper_rational':str(mu_upper),
      'mean_uniform_strict':'<91',
      'gradient_loss_exact':str(loss),
      'gradient_loss_strict':'<64000',
      'gradient_strict':'d_p V_q < -12650',
      'unique_maximizer':'(0,z_star(q))',
      'stability':'M_q-V_q(p,z) >= 12650*p+6400000*(z-z_star(q))^2',
      'area_gain_vs_prefix663':4,'area_gain_vs_prefix662':64,'area_gain_vs_prefix661':32768,
      'dependencies':['PREFIX-659 exact mean at Q and score bound','PREFIX-660 edge concavity',
                      'PREFIX-661 boundary inward p-gradient','PREFIX-662 frozen Bernstein kernels'],
      'checks_passed':checks,'result':'ALL_CHECKS_PASS',
      'status':'AUTHOR_DERIVED / EXACT_RATIONAL_CHECKED / UNREVIEWED / NOT_ADMITTED'}

if __name__=='__main__':
    r=certificate()
    print(json.dumps(r,indent=2,ensure_ascii=False))
    print('ALL_CHECKS_PASS',r['checks_passed'])
