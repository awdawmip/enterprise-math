#!/usr/bin/env python3
"""Exact modular test: first-digit B normalization and CM derivative Frobenius parity.
A/B are independently generated; not a native H0/B0 experiment or a general proof.
"""
from math import comb

def primes(limit):
    s = bytearray(b'\x01') * (limit + 1)
    s[0:2] = b'\x00\x00'
    for q in range(2, int(limit ** .5) + 1):
        if s[q]: s[q*q::q] = b'\x00' * ((limit-q*q)//q+1)
    return [p for p in range(5,limit+1) if s[p] and p%24 in (13,19)]

def inv(a,p): return pow(a%p,-1,p)

def fp2mul(a,b,p):
    x,y=a;u,v=b
    return ((x*u+2*y*v)%p,(x*v+y*u)%p)

def fp2add(a,b,p): return ((a[0]+b[0])%p,(a[1]+b[1])%p)

def fp2pow(a,n,p):
    r=(1,0)
    while n:
        if n&1: r=fp2mul(r,a,p)
        a=fp2mul(a,a,p); n//=2
    return r

def polydual(coeff,x,p):
    """Horner evaluation of polynomial and derivative over Fp[s]/(s²-2)."""
    val=(0,0);der=(0,0)
    for c in reversed(coeff):
        der=fp2add(fp2mul(der,x,p),val,p)
        val=fp2add(fp2mul(val,x,p),(c%p,0),p)
    return val,der

def compute(p,which):
    if which=='A':
        u,v,den,c1,c2,eps,weight=(p-1)//6,(p-1)//3,2,1,2,0,12
        d=6
    else:
        k=(p-3)//8 if p%8==3 else (p-5)//8
        u,v,den,c1,c2,eps=k,3*k+1,9,1,3,int(p%8==5)
        d=8;weight=128*inv(9,p)%p if eps else 16
    coeff=[comb(u,i)*comb(v,i) for i in range(u+1)]
    J=sum(i*coeff[i]*pow(inv(den,p),i,p) for i in range(u+1))%p
    qprime=J*den%p
    mod=p*p;x=inv(den,mod)
    term=1;xp=1;G=0
    for i in range(p):
        G=(G+xp*term)%mod
        if i+1<p:
            term=term*(i-u+c1*p*inv(d,mod))*(i-v+c2*p*inv(d,mod))*inv((i+1)**2,mod)%mod
            xp=xp*x%mod
    Q=sum(coeff[i]*pow(x,i,mod) for i in range(u+1))%mod
    assert Q%p==G%p==0 and J!=0
    g=G//p; lam=weight*J*g%p
    # Independent dual-number evaluation of R'(CM fiber).
    if which=='A':
        fiber=(inv(2,p),inv(4,p))
    else:
        fiber=(inv(2,p),inv(3,p))
    z2=fp2mul(fiber,fiber,p)
    argument=((4*(fiber[0]-z2[0]))%p,(4*(fiber[1]-z2[1]))%p)
    assert argument==(inv(den,p),0)
    qval,qder=polydual(coeff,argument,p)
    chain=fp2mul((4,0),((1-2*fiber[0])%p,(-2*fiber[1])%p),p)
    deriv=fp2mul(qder,chain,p)
    if eps:
        deriv=fp2mul(deriv,((1-2*fiber[0])%p,(-2*fiber[1])%p),p)
    assert qval==(0,0)
    if which=='A': predicted=(0,-2*qprime%p)
    elif not eps: predicted=(0,-8*inv(3,p)*qprime%p)
    else: predicted=(32*inv(9,p)*qprime%p,0)
    assert deriv==predicted and deriv!=(0,0)
    assert fp2pow(deriv,p,p)==(deriv[0],(-deriv[1])%p)
    return dict(J=J,qprime=qprime,g=g,lam=lam,deriv=deriv,eps=eps)

def main():
    ps=primes(2000)
    assert len(ps)==77
    for p in ps:
        a=compute(p,'A');b=compute(p,'B');eps=b['eps']
        a_d=a['deriv']; b_d=b['deriv']
        assert a_d[0]==0
        assert (b_d[0]==0) == (eps==0)
        if eps:
            # (RA'/RB') = -(9/16)*s*(QA'/QB')
            T=(0,-9*inv(16,p)*a['qprime']*inv(b['qprime'],p)%p)
            assert fp2mul(T,b_d,p)==a_d and T[0]==0
            coupling=fp2add(fp2mul(T,(a['g'],0),p),(0,4*inv(27,p)*b['g']%p),p)
            assert coupling==(0,0)
        else:
            # (RA'/RB') = 3/4 * QA'/QB' (Fp)
            T=(3*inv(4,p)*a['qprime']*inv(b['qprime'],p)%p,0)
            assert fp2mul(T,b_d,p)==a_d
            coupling=fp2add(fp2mul(T,(a['g'],0),p),(-2*inv(9,p)*b['g']%p,0),p)
            assert coupling==(0,0)
        assert b['lam']==1 and a['lam']==1
        if p in (13,19,43,67,373):
            print('p=',p,'eps=',eps,'JA,JB=',a['J'],b['J'],
                  'gA,gB=',a['g'],b['g'],'RAprime=',a_d,'RBprime=',b_d,'T=',T,'coupling=',coupling)
    print('PASS',len(ps),'target primes <=2000; independent Gauss lifts, B unit, CM derivative parities and paired bridge')

if __name__=='__main__': main()
