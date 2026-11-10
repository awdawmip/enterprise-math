#!/usr/bin/env python3
"""PREFIX-666: exact 16x BRC variance strip expansion.
Reuses the frozen 189-layer survivor predicate of PREFIX-665.
"""
from collections import defaultdict
from fractions import Fraction as F
from math import comb, factorial
import json
from PREFIX665_R6_SIGNED_CURVATURE_CERTIFICATE import N, Q, wide

EPS, DELTA, K = F(1,256), F(1,4096), 12
assert 4*21**2*(Q-DELTA)*(1-Q+DELTA)>188
checks=0
def ck(condition, label):
    global checks
    assert condition,label
    checks+=1

def build_rows():
    state={0:1};rows=[state.copy()]
    for n in range(1,N+1):
        nxt=defaultdict(int)
        for k,v in state.items():nxt[k]+=v;nxt[k+1]+=v
        state={k:v for k,v in nxt.items() if wide(n,k)}
        rows.append(state.copy())
    ck(len(rows)==N+1 and not rows[-1], '189-stop')
    ck(all(sum(rows[n].values())==2**n for n in range(25)), 'initial survival')
    ck(all(rows[n].get(0,0)==(1 if n<25 else 0) for n in range(N)), 'p0-Gamma25')
    ck(all(0<=v<=comb(n,k) for n,row in enumerate(rows) for k,v in row.items()), 'Bernstein masses')
    return rows

def solve():
    rows=build_rows(); R=K+2
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
    ck(all(0<=a[n]<=1 and 0<=b[n]<=n+1 for n in range(N)),'kernel bounds')
    D={name:[F(0)]*(R+1) for name in ('mu','H','muz','Hz')}
    Zmu=ZH=F(0);mup=F(0)
    for n,row in enumerate(rows[:N]):
        f=[F(row.get(k,0),comb(n,k)) if k<=n else F(0) for k in range(R+1)]
        mup+=a[n]*n*(f[1]-f[0])
        sn_bound=F(0)
        for r in range(2,R+1):
            if r>n:continue
            deriv=F(factorial(n),factorial(n-r))*sum(((-1)**(r-j))*comb(r,j)*f[j] for j in range(r+1))
            D['mu'][r]+=a[n]*deriv;D['H'][r]+=b[n]*deriv
            D['muz'][r]+=az[n]*deriv;D['Hz'][r]+=bz[n]*deriv
            if r<R:sn_bound+=abs(deriv)*EPS**(r-2)/factorial(r-2)
        if R<=n:sn_bound+=2**(R-1)*F(factorial(n),factorial(n-R))*EPS**K/factorial(K)
        Zmu+=2*(n+1)*(n+2)*sn_bound
        ZH+=2*(n+1)*(n+2)*(n+3)*sn_bound
    Bmu=2**(R-1)*sum(factorial(n)//factorial(n-R) for n in range(R,N))
    BH=2**(R-1)*sum((n+1)*factorial(n)//factorial(n-R) for n in range(R,N))
    def pshift(name,B):
        return sum(abs(D[name][r])*EPS**(r-2)/factorial(r-2) for r in range(3,R))+F(B)*EPS**K/factorial(K)
    def zfirst(name,B):
        return abs(D[name][2])+sum(abs(D[name][r])*EPS**(r-2)/factorial(r-2) for r in range(3,R))+21*F(B)*EPS**K/factorial(K)
    mu2lower=D['mu'][2]-pshift('mu',Bmu)-DELTA*zfirst('muz',Bmu)-DELTA**2*Zmu/2
    H2upper=D['H'][2]+pshift('H',BH)+DELTA*zfirst('Hz',BH)+DELTA**2*ZH/2
    mu0=sum(t)+sum(a[n] for n in range(25))
    # First establish mu_pp>0.  Then mu_p is increasing in p.
    # On the z band, |mu_z(0,z)|<=21*(N+25), and
    # |mu_p(0,z)-mu_p(0,Q)|<=21*DELTA*sum_n(n).
    mu_lower=mu0-21*(N+25)*DELTA-EPS*(abs(mup)+21*sum(range(N))*DELTA)
    W2upper=2*H2upper-2*mu_lower*mu2lower
    ck(F('89.455')<mu0<F('89.456'), 'exact center mean')
    ck(mu2lower>193,'positive mu_pp')
    ck(H2upper<12855,'H_pp upper')
    ck(mu_lower>F(879,10),'mean lower')
    ck(W2upper < -8000, 'signed W_pp')
    ck(EPS/F(1,4096)==16,'16x strip')
    ck(all(x>=0 for x in (Zmu,ZH,Bmu,BH)),'envelope nonnegative')
    return {'schema':'EM_PREFIX666_R6_TAYLOR_BERNSTEIN_STRIP_V1',
       'science_pin':'f42f2906d77f24085c123f3ccfe9667d41caa96d',
       'researcher_id':'EM-DIRECT-4D0FD7','activity_id':'RA-FF547EFAD41019F3529D02C5',
       'domain':{'p':['0','1/256'],'z':['607/4096','609/4096'],'q':['12','24']},
       'taylor_order':K, 'center_mean':str(mu0), 'center_mu_pp':str(D['mu'][2]),
       'center_H_pp':str(D['H'][2]), 'p_shift_mu_pp':str(pshift('mu',Bmu)),
       'p_shift_H_pp':str(pshift('H',BH)), 'z_first_mu_pp':str(zfirst('muz',Bmu)),
       'z_first_H_pp':str(zfirst('Hz',BH)), 'z_second_mu_pp':str(Zmu),
       'z_second_H_pp':str(ZH),'mu_lower':str(mu_lower),
       'mu_pp_lower':str(mu2lower),'H_pp_upper':str(H2upper), 'W_pp_upper':str(W2upper),
       'theorem':'mu_pp>193, H_pp<12855, mu>879/10, W_pp<-8000 on rectangle',
       'stability':'M_q - V_q(p,z) >= 76650*p + 4000*q^2*p^2 + 6400000*(z-z_star(q))^2',
       'area_gain_vs_PREFIX665':16,
       'dependencies':['PREFIX665 frozen survivor predicate/moment kernels',
                       'PREFIX660 boundary z_star and gap','PREFIX661 boundary normal slope'],
       'checks_passed':checks,'result':'ALL_CHECKS_PASS',
       'status':'AUTHOR_PROVED / EXACT_FRACTION_CHECKED / UNREVIEWED / NOT_ADMITTED'}

if __name__=='__main__':
    result=solve()
    print(json.dumps(result,indent=2,ensure_ascii=False))
    print('ALL_CHECKS_PASS', result['checks_passed'])
