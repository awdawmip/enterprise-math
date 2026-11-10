#!/usr/bin/env python3
"""PREFIX-667: exact signed Bernstein proof of p<=1/128 variance curvature.
Run in research_notes/portable_direct next to PREFIX665_R6_SIGNED_CURVATURE_CERTIFICATE.py.
Standard-library integer/Fraction arithmetic only; no numerical decision.
Frozen model pin: f42f2906d77f24085c123f3ccfe9667d41caa96d.
"""
from collections import defaultdict
from fractions import Fraction as F
from math import comb, factorial
import json
from PREFIX665_R6_SIGNED_CURVATURE_CERTIFICATE import N, Q, wide

EPS, DELTA, R, PARTS = F(1,128), F(1,4096), 22, 16

def fall(n,r):
    return factorial(n)//factorial(n-r) if n>=r else 0

def solve():
    checks=0
    def ck(ok,reason):
        nonlocal checks
        assert ok, reason
        checks+=1
    ck(N==189 and Q==F(19,128), 'frozen constants')
    ck(4*21**2*(Q-DELTA)*(1-Q+DELTA)>188, 'uniform z score bound')
    state={0:1}; rows=[state.copy()]
    for n in range(1,N+1):
        nxt=defaultdict(int)
        for k,v in state.items():
            nxt[k]+=v; nxt[k+1]+=v
        state={k:v for k,v in nxt.items() if wide(n,k)}
        rows.append(state.copy())
    ck(not rows[N] and len(rows)==N+1, 'exact 189-layer stop')
    ck(all(sum(rows[n].values())==2**n for n in range(25)), '25 full-survival layers')
    ck(all(0<=v<=comb(n,k) for n,row in enumerate(rows) for k,v in row.items()), 'survivor coefficients')
    ck(all(rows[n].get(0,0)==(1 if n<25 else 0) for n in range(N)), 'Gamma-25 boundary')
    t=[];tz=[]
    for n,row in enumerate(rows[:N]):
        weights=[(k,F(v*Q.numerator**k*(Q.denominator-Q.numerator)**(n-k),Q.denominator**n)) for k,v in row.items()]
        t.append(sum((v for k,v in weights),F(0)))
        tz.append(sum((v*(k-n*Q) for k,v in weights),F(0))/(Q*(1-Q)))
    a=[];b=[];az=[];bz=[]
    for n in range(N):
        aa,bb,da,db=F(1),F(n+1),F(0),F(0)
        for m in range(N):
            if not t[m] and not tz[m]:continue
            w=F(comb(n+m,n),2**(n+m+1))
            aa-=w*t[m];bb-=F(n+m+1,2)*w*t[m]
            da-=w*tz[m];db-=F(n+m+1,2)*w*tz[m]
        a.append(aa);b.append(bb);az.append(da);bz.append(db)
    ck(all(0<=a[n]<=1 and 0<=b[n]<=n+1 for n in range(N)), 'positive moment kernels')
    D={key:[F(0)]*(R+1) for key in ('mu','H','muz','Hz')}
    Zmu=ZH=F(0);mup=F(0)
    for n,row in enumerate(rows[:N]):
        f=[F(row.get(k,0),comb(n,k)) if k<=n else F(0) for k in range(R+1)]
        mup+=a[n]*n*(f[1]-f[0])
        sn_bound=F(0)
        for r in range(2,R+1):
            if r>n:continue
            deriv=fall(n,r)*sum(((-1)**(r-j))*comb(r,j)*f[j] for j in range(r+1))
            for name,coef in (('mu',a[n]),('H',b[n]),('muz',az[n]),('Hz',bz[n])):
                D[name][r]+=coef*deriv
            if r<R:sn_bound+=abs(deriv)*EPS**(r-2)/factorial(r-2)
        if R<=n:sn_bound+=2**(R-1)*fall(n,R)*EPS**(R-2)/factorial(R-2)
        Zmu+=2*(n+1)*(n+2)*sn_bound
        ZH+=2*(n+1)*(n+2)*(n+3)*sn_bound
    Bmu=2**(R-1)*sum(fall(n,R) for n in range(R,N))
    BH=2**(R-1)*sum((n+1)*fall(n,R) for n in range(R,N))
    def zfirst(name,B):
        return sum(abs(D[name][r])*EPS**(r-2)/factorial(r-2) for r in range(2,R))+21*F(B)*EPS**(R-2)/factorial(R-2)
    # Taylor polynomial for g(p,Q) where g=mu_pp or H_pp;
    # every exact degree-(R-3) Bernstein control point bounds g's polynomial part.
    d=R-3
    def poly_bounds(name):
        c=[D[name][j+2]/factorial(j) for j in range(d+1)]
        mins=[];maxs=[]
        for i in range(PARTS):
            u=EPS*F(i,PARTS);h=EPS/PARTS
            shifted=[sum((c[r]*comb(r,j)*u**(r-j)*h**j for r in range(j,d+1)),F(0)) for j in range(d+1)]
            bern=[sum((shifted[j]*F(comb(k,j),comb(d,j)) for j in range(k+1)),F(0)) for k in range(d+1)]
            mins.append(min(bern));maxs.append(max(bern))
        return min(mins),max(maxs)
    mupoly,hpoly=poly_bounds('mu'),poly_bounds('H')
    mu_rem=F(Bmu)*EPS**(R-2)/factorial(R-2)
    H_rem=F(BH)*EPS**(R-2)/factorial(R-2)
    mu_zerr=DELTA*zfirst('muz',Bmu)+DELTA**2*Zmu/2
    H_zerr=DELTA*zfirst('Hz',BH)+DELTA**2*ZH/2
    mu2lower=mupoly[0]-mu_rem-mu_zerr
    H2upper=hpoly[1]+H_rem+H_zerr
    # Once mu_pp>0, mu_p is increasing, hence mu has this global lower bound.
    mu0=sum(t)+sum(a[n] for n in range(25))
    mulower=mu0-21*(N+25)*DELTA-EPS*(abs(mup)+21*sum(range(N))*DELTA)
    W2upper=2*H2upper-2*mulower*mu2lower # discard non-positive -2*mu_p**2
    ck(F('89.455')<mu0<F('89.456'), 'center mean interval')
    ck(mu2lower>226, 'positive lower mu_pp')
    ck(H2upper<15362, 'upper H_pp')
    ck(mulower>F(876,10), 'lower mu')
    ck(W2upper < -8900, 'signed strict curvature')
    ck(EPS/F(1,256)==2, 'double PREFIX-666 strip')
    ck(all(x>=0 for x in (Zmu,ZH,Bmu,BH,mu_rem,H_rem)), 'nonnegative error budgets')
    ck(F(-8994)<W2upper<F(-8993), 'exact curvature bracket')
    ck(F(226)<mu2lower<F(227), 'exact mu_pp bracket')
    ck(F(15361)<H2upper<F(15362), 'exact H_pp bracket')
    ck(F(876,10)<mulower<F(877,10), 'exact mean bracket')
    return {'schema':'EM_PREFIX667_R6_BERNSTEIN_DOUBLE_STRIP_V1',
      'science_pin':'f42f2906d77f24085c123f3ccfe9667d41caa96d',
      'domain':{'p':['0','1/128'],'z':['607/4096','609/4096'],'q':['12','24']},
      'taylor_order':R-2,'bernstein_degree':d,'subinterval_count':PARTS,
      'exact_envelopes':{'mu_lower':str(mulower),'mu_pp_lower':str(mu2lower),
         'H_pp_upper':str(H2upper),'W_pp_upper':str(W2upper),
         'mu_pp_poly_min':str(mupoly[0]),'H_pp_poly_max':str(hpoly[1]),
         'mu_taylor_remainder':str(mu_rem),'H_taylor_remainder':str(H_rem),
         'mu_z_error':str(mu_zerr),'H_z_error':str(H_zerr)},
      'certified':{'mu_lower':'>87.6','mu_pp':'>226','H_pp':'<15362',
         'W_pp':'<-8900','V_q_pp':'<-8900*q^2',
         'stability':'M_q-V_q(p,z)>=76650*p+4450*q^2*p^2+6400000*(z-z_star(q))^2',
         'area_gain_vs_prefix666':2},
      'dependencies':['PREFIX665 frozen survivor predicate','PREFIX660 exact edge z maximum and gap',
                      'PREFIX661 strict edge normal slope'],
      'checks_passed':checks,'result':'ALL_CHECKS_PASS',
      'status':'AUTHOR_PROVED / EXACT_FRACTION_REPLAY_CHECKED / UNREVIEWED / NOT_ADMITTED'}

if __name__=='__main__':
    r=solve()
    print(json.dumps(r,indent=2,ensure_ascii=False))
    print('ALL_CHECKS_PASS',r['checks_passed'])
