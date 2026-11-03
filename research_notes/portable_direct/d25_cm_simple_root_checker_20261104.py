#!/usr/bin/env python3
"""D25 original weighted-216 polynomial: exact CM simple-root/Hensel regression.
Executed author-side 2026-11-04, no native H0/B0 source or compute is claimed.
Only tests 7<=p<=2000, p=1 mod6; 77 target primes.
"""
from math import isqrt
import json

def primes_to(n):
    a=bytearray(b'\x01')*(n+1)
    a[0]=a[1]=0
    for i in range(2,isqrt(n)+1):
        if a[i]:
            a[i*i:n+1:i]=b'\x00'*(((n-i*i)//i)+1)
    return [i for i in range(2,n+1) if a[i]]

def compute(p):
    assert p%6==1 and p>=7
    r=(p-1)//6
    N=p**3
    inv2=pow(2,-1,N)
    z0=inv2
    a=1
    F=1
    dF=0
    thF=0
    G=1
    g=1
    for k in range(1,r+1):
        a=a*(-r+k-1)*(-2*r+k-1)*pow(k,-1,N)*pow(k-inv2*p,-1,N)%N
        zk=pow(z0,k,N)
        F=(F+a*zk)%N
        thF=(thF+k*a*zk)%N
        dF=(dF+k*a*zk*2)%N
        g=g*(-r+k-1)*(-2*r+k-1)*pow(k,-2,N)%N
        G=(G+g*zk)%N
    b=1
    W=1
    W1=0
    W2=0
    for k in range(p-1):
        b=b*(2*k+1)*(3*k+1)*(3*k+2)*pow(36*(k+1)**3,-1,N)%N
        i=k+1
        t=(6*i+1)*b%N
        W=(W+t)%N
        W1=(W1+2*i*t)%N
        W2=(W2+4*i*(i-1)*t)%N
    target=p%24 in (13,19)
    if target:
        assert F%p==G%p==0,(p,F%p,G%p)
        assert dF%p!=0,(p,dF%p)
        assert W%p==0,(p,W%p)
        assert W1%p==24*(thF%p)**2%p
        assert W%p**2==p
        aF=(-((F//p)%p)*pow(dF%p,-1,p))%p
        aG=(-((G//p)%p)*pow(dF%p,-1,p))%p
        aW=(-((W//p)%p)*pow(W1%p,-1,p))%p
        assert aW==(-pow(W1%p,-1,p))%p
        assert (F+p*aF*dF)%p**2==0
        assert (G+p*aG*dF)%p**2==0
        t=(W+p*aW*W1+p*p*(aW*aW*W2*inv2%N))%N
        assert t%p**2==0
        bW=(-(t//(p*p))*pow(W1%p,-1,p))%p
        baseline=(p+p*aW*W1+p*p*(aW*aW*W2*inv2%N))%N
        assert baseline%p**2==0
        bbaseline=(-((baseline//(p*p))%p)*pow(W1%p,-1,p))%p
        assert (bW-bbaseline)%p== -((W-p)//(p*p))*pow(W1%p,-1,p)%p
        rootW=(z0+p*aW+p*p*bW)%N
        val=0
        coef=1
        for k in range(p):
            if k:
                coef=coef*(2*k-1)*(3*k-2)*(3*k-1)*pow(18*k*k*k,-1,N)%N
            val=(val+(6*k+1)*coef*pow(rootW,k,N))%N
        assert val==0,(p,'root',val)
        return dict(p=p,r=r,F_p2=F%p**2,G_p2=G%p**2,
                    thetaF_modp=thF%p,dF_modp=dF%p,W_modp3=W,
                    W1_modp=W1%p,W1_modp2=W1%p**2,W2_modp=W2%p,
                    aF=aF,aG=aG,aW=aW,bW=bW,bbaseline=bbaseline,
                    rootW_modp3=rootW,second_residue=(W-p)//(p*p)%p)
    return dict(p=p,r=r,target=False)

def main():
    ps=[p for p in primes_to(2000) if p%6==1]
    rows=[compute(p) for p in ps]
    target=[x for x in rows if x.get('target',True)]
    assert len(ps)==148 and len(target)==77
    out={'method':'exact integer modulo p^3','tested_count':len(ps),
         'target_count':len(target),'target_results':target,
         'all_second_residues_zero':all(x['second_residue']==0 for x in target)}
    print(json.dumps(out,ensure_ascii=False,indent=2))

if __name__=='__main__':
    main()
