#!/usr/bin/env python3
"""Exact finite-horizon, uniform nuisance-box residual certificate, R749STM."""
import json
from math import factorial,ceil
from pathlib import Path
import sympy as s
x,N=s.symbols('x N'); e,d,E,D=s.symbols('e d E D')
W=(1,1,2,3,6)
def conv(a,b):
 z=[0]*(len(a)+len(b)-1)
 for i,u in enumerate(a):
  for j,v in enumerate(b):z[i+j]+=u*v
 return z
def block(weights):
 a=[1]
 for w in weights:a=conv(a,[int(k%w==0) for k in range(7-w)])
 return a
QC=block((*W,1));QT=conv([0,1],block((1,1,1,1,2,3,6)))
def falling(t,m):return s.prod(t-i for i in range(m))/factorial(m)
def quasi(r):
 c=s.Poly(s.expand(sum(a*falling((N-1-i)/6+5,5) for i,a in enumerate(QC) if (r-1-i)%6==0)),N)
 t=s.Poly(s.expand(sum(a*falling((N-1-i)/6+6,6) for i,a in enumerate(QT) if (r-1-i)%6==0)),N)
 return c,t
S=s.Poly(18*N**4+54*N**3-345*N**2+2070*N-16315,N)
def xscaled(poly,q,degree):
 return s.Poly(s.expand(sum(poly.nth(i)*x**(degree-i)*(1+q*x)**i for i in range(degree+1))),x)
def ratio(r,q,ee,dd):
 c,t=quasi(r)
 u=xscaled(c,q,5)+s.Poly(dd*x**5,x)
 v=xscaled(t,q,6)+s.Poly(ee*x**6,x)
 sp=s.Poly(xscaled(S,q,4).as_expr()/108,x)
 raw=s.Poly((1+q*x)**3,x)*v-sp*u
 assert all(raw.nth(i)==0 for i in range(4))
 p=s.Poly(sum(raw.nth(k)*x**(k-4) for k in range(4,raw.degree()+1)),x)
 return p,u
vars=(e,d,E,D)
def norm(expr):
 pp=s.Poly(s.expand(expr),*vars)
 return sum(abs(c)*2**sum(exps) for exps,c in pp.terms())
def absbound(poly,rho,start=0):
 return sum(norm(poly.nth(i))*rho**i for i in range(start,poly.degree()+1))
def verify_six_phase_shear():
    """Symbolic proof of the shear identity for every residue, arbitrary k,h."""
    H,K=s.symbols('H K', integer=True, nonnegative=True)
    A=[54027,74412,69363,60588,62019,70092]
    def universal2(r, ee, dd):
        c,t=quasi(r);cp,tp=c,t
        arr=[cp.nth(5-i) if i<=5 else s.Integer(0) for i in range(7)]
        brr=[tp.nth(6-i) if i<=6 else s.Integer(0) for i in range(7)]
        arr[5]+=dd;brr[6]+=ee
        rr=[]
        for i in range(7):
            rr.append(s.expand((brr[i]-sum(arr[j]*rr[i-j] for j in range(1,i+1)))/arr[0]))
        ps={-4:s.Rational(18,108),-3:s.Rational(54,108),-2:s.Rational(-345,108),-1:s.Rational(2070,108),0:s.Rational(-16315,108)}
        return [s.factor(rr[i+4]-ps.get(i,0)) for i in range(3)]
    def sh(a,q):
        return [s.expand(a[0] if m==0 else sum(a[i]*s.binomial(-i,m-i)*q**(m-i) for i in range(1,m+1))) for m in range(len(a))]
    for r in range(6):
        b=[78,73,74,75,76,77][r]
        u=sh(universal2(r,e,d),b+6*K)
        v=sh(universal2(r,E,D),b+6*K+6*H)
        aa=s.factor(u[1]-v[1]); bb=s.factor(u[2]-v[2]);q=b+6*K
        assert s.factor(aa-720*(D-d))==0
        assert s.factor(bb+(q+27)*aa-4320*(e-E-H*(D-s.Rational(A[r],34992))))==0
    # Independent count checks: both five labeled sources and extra k1 mark.
    nmax=240; parts=[0]*(nmax+1);parts[0]=1
    for w in (1,1,2,3,6):
        for n in range(w,nmax+1):parts[n]+=parts[n-w]
    counts=[0]*(nmax+1);totals=[0]*(nmax+1)
    for n in range(1,nmax+1):
        counts[n]=counts[n-1]+parts[n-1]
        totals[n]=totals[n-1]+counts[n-1]
        if n>=29:
            c,t=quasi(n%6)
            assert c.eval(n)==counts[n] and t.eval(n)==totals[n]
    return {'residue_count':6,'symbolic_all_k_h':True,'dynamic_count_crosscheck':{'min_n':29,'max_n':240},'sharp_margins':{'r1':'max(0,(41*h-1296)/324)','r5':'max(0,(h-1296)/324)','r0_r2_r3_r4':'0'}}
def ceilr(z): return int(s.ceiling(z))
def cert(r,h,k=0):
 b=[78,73,74,75,76,77][r];q=b+6*k;p=q+6*h
 pq,uq=ratio(r,q,e,d);pp,up=ratio(r,p,E,D)
 den=uq*up; W=pq*up-pp*uq
 assert W.nth(0)==0
 a1=s.factor(W.nth(1)/den.nth(0));a2=s.factor((W.nth(2)-a1*den.nth(1))/den.nth(0))
 A=[54027,74412,69363,60588,62019,70092][r]
 assert s.factor(a1-720*(D-d))==0
 assert s.factor(a2+(q+27)*a1-4320*(e-E-h*(D-s.Rational(A,34992))))==0
 rem=W-s.Poly(a1*x+a2*x*x,x)*den
 assert all(rem.nth(i)==0 for i in range(3))
 Q=s.Poly(sum(rem.nth(i)*x**(i-3) for i in range(3,rem.degree()+1)),x)
 c5=uq.nth(0);assert up.nth(0)==c5
 rho=s.Rational(1,1000*p)
 uerr=absbound(uq,rho,1);perr=absbound(up,rho,1)
 assert uerr<c5/2 and perr<c5/2, (r,h,k,uerr,perr,c5)
 bq=absbound(Q,rho)
 M=s.factor(4*bq/c5**2)
 sigma=s.factor(4320*(h*s.Rational(A-69984,34992)-4)/4320)
 assert sigma>0
 # epsilon on J2hat <= M*x*(2.5+1.5*(q+27)*rho)/4320
 coeff=M*(s.Rational(5,2)+s.Rational(3,2)*(q+27)*rho)/4320
 xmax=min(rho,sigma/(2*coeff))
 J=ceilr(1/(6*xmax))
 # enforce strict x<= xmax at j>=J; if equality, still lower bound >=sigma/2
 jx=s.Rational(1,6*J)
 assert jx<=xmax and coeff*jx<=sigma/2
 # Observed differences F_j and F_2j are uncertain by <= 2 eta each.
 # Detection guarantee if eta < eta_crit where estimator noise < sigma/4.
 eta_crit=s.factor(1080*sigma*jx**2/(12+10*(q+27)*jx))
 # check strict >0 and required inequalities
 assert eta_crit>0
 return {'residue':r,'h':h,'k':k,'q':q,'p':p,
 'alpha':str(s.Rational(A,34992)),'sigma_min_abs_sheared_second_jet':str(sigma),
 'base_denominator_constant':str(c5),'radius':str(rho),
 'uq_variation_bound':str(uerr),'up_variation_bound':str(perr),
 'remainder_majorant_M':str(M),'uniform_j_threshold':str(J),
 'max_x':str(xmax),'eta_critical_at_J':str(eta_crit),
 'proof':'Exact rational P/U polynomial at x=1/(6j); F=a1*x+a2*x^2+x^3*Q/(Uq*Up); coefficientwise absolute norms with |e|,|d|,|E|,|D|<=2; U>=c5/2. Two-time jet estimator at j,2j, error <=M*x*(5/2+3/2*(q+27)*rho)/4320; positivity of |J2|>=sigma; raw-noise bound from 4 readouts.'}
def main():
 shear=verify_six_phase_shear()
 out=[cert(1,32),cert(5,1297)]
 p=Path(__file__).with_name('R749STM_TWO_TIME_FINITE_SEPARATION_RESULTS.json')
 p.write_text(json.dumps({'unit':'R749STM','source_pin':'a72226e2430ffa4786321ac86e7f0c599d5f0389','status':'AUTHOR_EXACT_NOT_REVIEWED','scope':'sharp sheared two-jet margins for all six same-residue pairs; explicit finite two-time thresholds for two first forbidden gap pairs','six_phase_shear_verification':shear,'certificates':out},indent=2,ensure_ascii=False)+'\n')
 for v in out:print('PASS',v['residue'],v['h'],'sigma=',v['sigma_min_abs_sheared_second_jet'],'j>=',v['uniform_j_threshold'],'M len=',len(v['remainder_majorant_M']),'eta threshold digits=',len(v['eta_critical_at_J']))
 print(p,p.stat().st_size)
if __name__=='__main__':main()
