#!/usr/bin/env python3
"""D25 exact signed half-endpoint jet/carry observer. Native H0/B0 NOT executed."""
from math import comb
from argparse import ArgumentParser
import json

def prime(n):
    if n < 2: return False
    for d in range(2,int(n**.5)+1):
        if n%d==0: return False
    return True

def tuples(p):
    h=(p-1)//2; n=(p-1)//6
    a=[(-h,1,2),(-2*n,1,3),(-4*n,2,3)]
    if p%4==1:
        s=(p-1)//4
        b=[(-h,1,2),(-s,1,4),(-3*s,3,4)]
    else:
        s=(p-3)//4
        b=[(-h,1,2),(-(3*p-1)//4,3,4),(-s,1,4)]
    for (num,den),(m,cn,cd) in zip([(1,2),(1,3),(2,3)],a):
        assert m*cd*den+cn*p*den==num*cd
    for (num,den),(m,cn,cd) in zip([(1,2),(1,4),(3,4)],b):
        assert m*cd*den+cn*p*den==num*cd
    return a,b

def jets(p,params,t,weight):
    p2=p*p; p3=p*p*p; h=(p-1)//2
    r=1; L1=L2=zero=zc=0
    S0=S1=S2=0
    for k in range(h+1):
        if k:
            for m,cn,cd in params:
                x=m+k-1
                if x==0:
                    zero+=1; zc=cn*pow(cd,-1,p2)%p2
                else:
                    assert x%p!=0
                    r=r*x%p3
                    cc=cn*pow(cd,-1,p2)%p2
                    L1=(L1+cc*pow(x,-1,p2))%p2
                    z=cn*pow(cd,-1,p)*pow(x,-1,p)%p
                    L2=(L2+z*z)%p
            r=r*pow(t,-1,p3)*pow(k,-3,p3)%p3
        assert zero<=1
        w=weight*k+1
        if zero==0:
            S0=(S0+w*r)%p3
            S1=(S1+w*r*L1)%p2
            S2=(S2+w*r*(L1*L1-L2)*pow(2,-1,p))%p
        else:
            S1=(S1+w*r*zc)%p2
            S2=(S2+w*r*zc*L1)%p
    return S0,S1,S2

def half(p):
    p3=p*p*p; a=b=1; wa=wb=0
    for k in range((p-1)//2+1):
        wa=(wa+(6*k+1)*a)%p3
        wb=(wb+(8*k+1)*b)%p3
        if k<(p-1)//2:
            a=a*(2*k+1)*(3*k+1)*(3*k+2)*pow(36*(k+1)**3,-1,p3)%p3
            b=b*(4*k+1)*(4*k+2)*(4*k+3)*pow(576*(k+1)**3,-1,p3)%p3
    return wa,wb

def shell(p):
    f=[1]*p
    for i in range(1,p): f[i]=f[i-1]*i%p
    val=0
    for k in range((p+1)//2,(2*p-1)//3+1):
        u=f[2*k-p]*f[3*k-p]*pow(216,-k,p)*pow(f[k],-5,p)%p
        val=(val+(6*k+1)*u)%p
    return val

def check(p):
    assert p%24 in (13,19)
    p2=p*p; p3=p*p*p
    a,b=tuples(p)
    aa=jets(p,a,2,6); bb=jets(p,b,9,8)
    x0=(aa[0]-bb[0])%p3
    x1=(aa[1]-bb[1])%p2
    x2=(aa[2]-bb[2])%p
    wa,wb=half(p)
    assert (aa[0]+p*aa[1]+p2*aa[2])%p3==wa
    assert (bb[0]+p*bb[1]+p2*bb[2])%p3==wb
    base=(x0+p*x1)%p3
    assert base%p2==0
    carry=base//p2; ca=shell(p)
    assert (((wa-wb)%p3)//p2)==(carry+x2)%p
    if p in (13,19,139,373):
        sw=sv=0
        for k in range((p-1)//2+1):
            sw=(sw+(6*k+1)*comb(2*k,k)**2*comb(3*k,k)*pow(216,-k,p3))%p3
            sv=(sv+(8*k+1)*comb(2*k,k)**2*comb(4*k,2*k)*pow(2304,-k,p3))%p3
        assert (sw,sv)==(wa,wb)
    return {'p':p,'S0':x0,'S1':x1,'S2':x2,'carry':carry,'CA':ca,'certificate_residue':(carry+x2+ca)%p}

def main():
    ap=ArgumentParser(); ap.add_argument('--bound',type=int,default=4999)
    bound=ap.parse_args().bound
    rows=[check(p) for p in range(13,bound+1) if p%24 in (13,19) and prime(p)]
    print(json.dumps({'schema':'D25_MATCHED_HALF_JET_EXACT_CHECK_V1','bound':bound,
        'target_primes':len(rows),'nonzero_certificates':sum(x['certificate_residue']!=0 for x in rows),
        'selected':[x for x in rows if x['p'] in (13,19,139,373)],'native_H0B0':'NOT_EXECUTED'},
        ensure_ascii=False,indent=2))
if __name__=='__main__': main()
