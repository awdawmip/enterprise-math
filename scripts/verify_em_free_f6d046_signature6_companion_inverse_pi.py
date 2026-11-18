#!/usr/bin/env python3
"""High-precision verifier for two signature-6 companion inverse-pi identities."""
from decimal import Decimal, getcontext
import json

getcontext().prec=120
D=Decimal
ONE=D(1)

def A(t):return t**4+D(24)*t**3+D(192)*t*t+D(528)*t+D(144)
def Ap(t):return D(4)*t**3+D(72)*t*t+D(384)*t+D(528)
def DD(t):return t*t+D(12)*t+D(24)
def Dp(t):return D(2)*t+D(12)
def D6(t):return t*(t+D(8))**3*(t+D(9))**2
def y3(t):return t*(t+D(9))**2/(t+D(6))**3
def x4(t):return t*(t+D(8))**3/DD(t)**2
def z3(t):
    y=y3(t);return D(4)*y*(ONE-y)
def z4(t):
    x=x4(t);return D(4)*x*(ONE-x)
def z6(t):return D(1728)*D6(t)/A(t)**3

def kappa3(t):
    y=y3(t)
    L=ONE/t+D(2)/(t+D(9))-D(3)/(t+D(6))
    return ONE/(t*L*(ONE-D(2)*y)/(ONE-y))
def kappa4(t):
    x=x4(t)
    L=ONE/t+D(3)/(t+D(8))-D(2)*Dp(t)/DD(t)
    return ONE/(t*L*(ONE-D(2)*x)/(ONE-x))
def kappa6(t):
    L=ONE/t+D(3)/(t+D(8))+D(2)/(t+D(9))-D(3)*Ap(t)/A(t)
    return ONE/(t*L)
def zprime(zfun,kfun,t):return zfun(t)/(kfun(t)*t)

def root(zfun,kfun,target,t):
    for _ in range(30):
        step=(zfun(t)-target)/zprime(zfun,kfun,t)
        t-=step
        if abs(step)<D('1e-112'):break
    return t

def transport(t,signature,a,b):
    if signature==3:
        Rs=(t+D(6))**2/D(36);delta=D(2)*t/(t+D(6));ks=kappa3(t)
    elif signature==4:
        Rs=DD(t)/D(24);delta=t*Dp(t)/DD(t);ks=kappa4(t)
    else:raise ValueError(signature)
    v=-A(t).sqrt();R6=-v/D(12);d6=t*Ap(t)/(D(2)*A(t));k6=kappa6(t)
    C0=Rs*(a+b*ks*delta);C1=Rs*b*ks
    b6=C1/(k6*R6);a6=(C0-C1*d6)/R6
    return {'t':t,'v':v,'z6':z6(t),'R6':R6,'kappa_source':ks,'kappa6':k6,'C0':C0,'C1':C1,'a6':a6,'b6':b6}

def f6(z):
    term=ONE;f=ONE;theta=D(0)
    n=0
    while True:
        n+=1;k=D(n-1)
        term*=((D(1)/D(2)+k)*(D(1)/D(6)+k)*(D(5)/D(6)+k))/(D(n)**3)*z
        f+=term;theta+=D(n)*term
        if abs(term)<D('1e-112'):return f,theta,n
        if n>10000:raise RuntimeError('series did not converge')

def agm_pi(iterations=10):
    a=ONE;b=(ONE/D(2)).sqrt();t=ONE/D(4);p=ONE
    for _ in range(iterations):
        an=(a+b)/D(2);b=(a*b).sqrt();t-=p*(a-an)**2;a=an;p*=D(2)
    return (a+b)**2/(D(4)*t)

sqrt2=D(2).sqrt();sqrt3=D(3).sqrt()
t3=root(z3,kappa3,-ONE/D(250000),D('-0.00000266666'))
t4=root(z4,kappa4,ONE/(D(99)**4),D('0.000000002928'))
r3=transport(t3,3,D(827)/(D(1500)*sqrt3),D(14151)/(D(1500)*sqrt3))
r4=transport(t4,4,D(2206)*sqrt2/D(9801),D(52780)*sqrt2/D(9801))
pi=agm_pi();ref=ONE/pi
checks={}
for label,r in [('signature3_source',r3),('signature4_source',r4)]:
    f,th,n=f6(r['z6']);val=r['a6']*f+r['b6']*th;res=val-ref
    r.update({'F6':f,'thetaF6':th,'terms':n,'inverse_pi':val,'residual':res})
    checks[label+'_source_equation']=abs((z3(t3)+ONE/D(250000)) if label.startswith('signature3') else (z4(t4)-ONE/(D(99)**4)))<D('1e-105')
    checks[label+'_companion_inverse_pi']=abs(res)<D('1e-100')
    checks[label+'_nonzero_target_derivative']=r['kappa6']!=0
checks['distinct_t_basepoints']=t3!=t4
checks['distinct_signature6_arguments']=r3['z6']!=r4['z6']
checks['canonical_v_branches']=r3['v']<0 and r4['v']<0
checks['target_series_convergent']=abs(r3['z6'])<1 and abs(r4['z6'])<1
out={'schema':'EM_FREE_F6D046_SIGNATURE6_COMPANION_INVERSE_PI_VERIFICATION_V1','researcher_id':'EM-FREE-F6D046','research_unit':'EM-FREE-F6D046-R9-SIGNATURE6-COMPANION-INVERSE-PI','all_passed':all(checks.values()),'check_count':len(checks),'checks':checks,'source_signature_3':{k:str(v) for k,v in r3.items()},'source_signature_4':{k:str(v) for k,v in r4.items()},'inverse_pi_reference':str(ref)}
print(json.dumps(out,ensure_ascii=False,indent=2))
raise SystemExit(0 if out['all_passed'] else 1)
