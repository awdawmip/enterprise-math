#!/usr/bin/env python3
"""D25 ordinary Gauss second-jet reduction, exact Z/p^3 arithmetic.
Independent checker: no native H0/B0 or authenticated Source authority implied.
"""
import json
from math import comb
from pathlib import Path


def primes(n):
    sieve=bytearray(b'\x01')*(n+1)
    sieve[:2]=b'\x00\x00'
    for d in range(2,int(n**.5)+1):
        if sieve[d]:
            sieve[d*d::d]=b'\x00'*(((n-d*d)//d)+1)
    return [p for p in range(7,n+1) if sieve[p]]


def bands(p):
    m=(p-1)//6;mod=p**3
    i2=pow(2,-1,mod);i3=pow(3,-1,mod);i6=pow(6,-1,mod);i9=pow(9,-1,mod)
    x0,x1,x2=1,0,0
    A0=A1=A2=B1=B2=C2=0
    for k in range(p):
        w=6*k+1
        if k<=2*m:
            A0=(A0+w*x0)%mod;A1=(A1+w*x1)%mod;A2=(A2+w*x2)%mod
        elif k<=3*m:
            assert x0==0
            B1=(B1+w*x1)%mod;B2=(B2+w*x2)%mod
        elif k<=4*m:
            assert x0==0 and x1==0
            C2=(C2+w*x2)%mod
        else:
            assert x0==x1==x2==0
        if k==p-1:break
        a=k-3*m;b=k-2*m;c=k-4*m
        f0=a*b*c%mod
        f1=(b*c*i2+a*c*i3+a*b*2*i3)%mod
        f2=(c*i6+b*i3+a*2*i9)%mod
        inv=pow(2*(k+1)**3,-1,mod)
        x0,x1,x2=(x0*f0*inv)%mod,((x1*f0+x0*f1)*inv)%mod,((x2*f0+x1*f1+x0*f2)*inv)%mod
    W=(A0+p*(A1+B1)+p*p*(A2+B2+C2))%mod
    return (A0,A1,A2,B1,B2,C2,W)


def direct_w(p):
    M=p**3;t=1;total=0
    for k in range(p):
        total=(total+(6*k+1)*t)%M
        if k<p-1:
            t=t*(2*k+1)*(3*k+1)*(3*k+2)*pow(36*(k+1)**3,-1,M)%M
    return total


def one(p, check_direct=False):
    assert p>3 and p%6==1
    m=(p-1)//6;n=2*m;M=p**3
    i2=pow(2,-1,M);i8=pow(8,-1,M)
    H=[0]*(n+1);H2=[0]*(n+1)
    for k in range(1,n+1):
        u=pow(k,-1,M)
        H[k]=(H[k-1]+u)%M
        H2[k]=(H2[k-1]+u*u)%M
    # Ordinary Gauss: beta_k=binom(m,k)binom(2m,k) 2^{-k}.
    P0=J=C=Cth=D2=D2th=0;zp=1
    for k in range(m+1):
        bk=comb(m,k)*comb(2*m,k)*zp%M
        P0=(P0+bk)%M;J=(J+k*bk)%M
        C=(C+bk*H[k])%M;Cth=(Cth+k*bk*H[k])%M
        hsq=(H[k]*H[k]+H2[k])%M
        D2=(D2+bk*hsq)%M;D2th=(D2th+k*bk*hsq)%M
        zp=zp*i2%M
    # Direct terminating deformed Gauss sum and Euler derivative; no use of ordinary jet.
    dk=1;Pd=Jd=0
    for k in range(m+1):
        Pd=(Pd+dk)%M;Jd=(Jd+k*dk)%M
        if k<m:
            dk=dk*(k-m)*(k-2*m)*pow((2*k+2-p)*(k+1),-1,M)%M
    assert (Pd-P0-p*i2*C-p*p*i8*D2)%M==0,(p,'deformed Gauss second jet')
    assert (Jd-J-p*i2*Cth-p*p*i8*D2th)%M==0,(p,'Euler Gauss second jet')
    square=Pd*(Pd+12*Jd)%M
    # Exact Clausen single-index coefficient, avoids a quadratic convolution.
    q=1;calH1=calH2=0
    for k in range(n+1):
        v=(6*k+1)*q%M
        calH1=(calH1+v*H[k])%M
        calH2=(calH2+v*(9*H[k]*H[k]-5*H2[k]))%M
        if k<n:
            q=q*(k-2*m)*(k-3*m)*(k-4*m)*pow((2*k+2-p)*(k+1-p)*(k+1),-1,M)%M
    A0,A1,A2,B1,B2,C2,W=bands(p)
    assert (square-3*p*i2*calH1+p*p*i8*calH2-A0)%M==0,(p,'Clausen source bridge')
    ordinary_quad=(P0*(P0+12*J)+p*i2*(C*(2*P0+12*J)+12*P0*Cth)+p*p*i8*(D2*(2*P0+12*J)+12*P0*D2th+2*C*C+24*C*Cth))%M
    assert square==ordinary_quad,(p,'generic ordinary quadratic expansion',square,ordinary_quad)
    cm=(p%24 in (13,19))
    out={'p':p,'cm_target':cm,'A0':A0,'W':W}
    if cm:
        assert P0%p==0 and J%p!=0 and A0%p==0,(p,'CM invariant')
        # A=(P0/p + C/2) integral mod p^2; N must be divisible by p.
        A=(P0//p+i2*C)%(p*p)
        N=(12*J*A-3*i2*calH1+A1+B1-1)%(p*p)
        assert N%p==0,(p,'first-digit signed bracket',N)
        v_base=(N//p)%p
        v_quad=(A*A+6*A*Cth+3*i2*J*D2)%p
        v_gauge=(i8*calH2)%p
        v_bands=(A2+B2+C2)%p
        assert (square-12*p*J*A-p*p*(A*A+6*A*Cth+3*i2*J*D2))%M==0,(p,'CM reduced quadratic')
        assert (v_base+v_quad+v_gauge+v_bands)%p==(W-p)//p**2%p,(p,'LIFT equivalence')
        out.update({'ordinary_A_mod_p':A%p,'first_bracket_divided':v_base,'ordinary_quadratic':v_quad,'clausen_gauge':v_gauge,'three_band_second':v_bands,'new_LIFT_digit':(v_base+v_quad+v_gauge+v_bands)%p,'P0_over_p':(P0//p)%p,'J':J%p,'C':C%p,'Ctheta':Cth%p,'D2':D2%p,'H1':calH1%p,'H2':calH2%p,'A1':A1%(p*p),'B1':B1%(p*p),'A2':A2%p,'B2':B2%p,'C2':C2%p})
        if check_direct:
            assert W==direct_w(p),(p,'independent complete unmodified W')
            out['full_independent_crosscheck']=True
    return out


def run(limit=3000,path='/mnt/data/d25_next/d25_ordinary_second_jet_check_20261102.json'):
    ps=[p for p in primes(limit) if p%6==1]
    trials=[one(p,p in (13,19,37,373,1171)) for p in ps]
    selection={str(x['p']):x for x in trials if x['p'] in (7,13,19,37,373,1171)}
    report={'schema':'D25_ORDINARY_GAUSS_SECOND_JET_SOURCE_PRESERVING_REDUCTION_V1',
            'date':'2026-11-02','status':'AUTHOR_SIDE_PROOF_WITH_EXACT_FINITE_REGRESSION_UNREVIEWED_NOT_ADMITTED',
            'domain':'p>3 prime, p=1 mod6; divided reduction on p=13,19 mod24',
            'prime_limit':limit,'all_1mod6':len(trials),'target':sum(x['cm_target'] for x in trials),
            'zero_mismatch':True,'independent_full_original':[p for p in (13,19,37,373,1171) if p<=limit],
            'selected':selection,'cases':trials}
    Path(path).write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8')
    print(json.dumps({k:v for k,v in report.items() if k!='cases'},ensure_ascii=False,indent=2))

if __name__=='__main__':
    run()
