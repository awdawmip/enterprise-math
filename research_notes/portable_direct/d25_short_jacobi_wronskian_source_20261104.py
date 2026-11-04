#!/usr/bin/env python3
"""Exact finite-field Green/Wronskian source certificate for p = 8q+5.

Author-side check only, not a native Enterprise Math experiment.
"""
from math import comb, isqrt


def primes_upto(n):
    sieve=bytearray(b'\x01')*(n+1)
    sieve[0:2]=b'\x00\x00'
    for d in range(2,isqrt(n)+1):
        if sieve[d]:
            sieve[d*d:n+1:d]=b'\x00'*((n-d*d)//d+1)
    return [p for p in range(5,n+1) if sieve[p] and p%8==5]


def parameters(p):
    q=(p-5)//8
    zinv9=pow(9,-1,p)
    J=[]
    power=1
    for j in range(q+1):
        J.append(comb(q,j)*comb(3*q+1,j)*power%p)
        power=power*zinv9%p
    return q,J


def source_flux(p, q, J):
    """Compute W from the shortened Jacobi source, WITHOUT harmonic K."""
    inv72=pow(72,-1,p)
    inv9=pow(9,-1,p)
    H=[(-(4*j-6*q-1)*J[j]*inv72)%p for j in range(q)]
    source=[0]*(2*q)
    for i,ja in enumerate(J):
        for j,hj in enumerate(H):
            source[i+j]=(source[i+j]+ja*hj)%p
    W=[]
    previous=0
    for t in range(2*q):
        current=(source[t]-(4*q-t+1)*inv9*previous)*pow(t+1,-1,p)%p
        W.append(current)
        previous=current
    if q:
        # The true Wronskian has degree exactly 2q-2, with an explicit unit top term.
        top=(2*q+5)*J[q]*J[q-1]*pow(16*(q+1),-1,p)%p
        assert W[-1]==0 and W[-2]==top and top!=0
    else:
        assert H==[] and W==[]
    return W,source,H

def harmonic_independent(p,q,J):
    inv=[0]+[pow(d,-1,p) for d in range(1,3*q+2)]
    harmonic=[0]*(3*q+2)
    for k in range(1,3*q+2):
        harmonic[k]=(harmonic[k-1]+inv[k])%p
    inv8=pow(8,-1,p)
    K=[]
    for j,x in enumerate(J):
        h=(harmonic[q]-harmonic[q-j]+3*(harmonic[3*q+1]-harmonic[3*q+1-j]))*inv8%p
        K.append(x*h%p)
    j0=sum(J)%p
    j1=sum(i*x for i,x in enumerate(J))%p
    k0=sum(K)%p
    k1=sum(i*x for i,x in enumerate(K))%p
    # independent from source reconstruction
    w0=(j0*k1-k0*j1)%p
    return j0,j1,k0,k1,w0,K


def gauss_coeffs(p,a,b,n,mod):
    arr=[1]
    for k in range(n):
        arr.append(arr[-1]*(8*k+a)*(8*k+b)*pow(576*(k+1)**2,-1,mod)%mod)
    return arr


def second_digit_observer(p,q,J,K,W):
    """Independent p^2 Gauss coefficients, no full polynomial convolution."""
    m=p*p
    v=gauss_coeffs(p,1,3,p-1,m)
    c=gauss_coeffs(p,5,7,q,m)
    S=sum(v)%m
    D=sum(k*x for k,x in enumerate(v))%m
    C=sum(c)%m
    C1=sum(k*x for k,x in enumerate(c))%m
    N=(p+1)//2
    u=pow(8*pow(9,-1,m)%m,N,m)
    e0numer=(S-u*C)%m
    e1numer=(D-u*(C1-N*pow(8,-1,m)*C))%m
    assert e0numer%p==0 and e1numer%p==0
    e0=e0numer//p
    e1=e1numer//p
    # independent mod-p^2 Jacobi values and derivatives
    j_m=j1_m=0;pow9=1
    zinv9=pow(9,-1,m)
    for j in range(q+1):
        term=comb(q,j)*comb(3*q+1,j)*pow9%m
        j_m=(j_m+term)%m
        j1_m=(j1_m+j*term)%m
        pow9=pow9*zinv9%m
    j0,j1,k0,k1,_ ,_=harmonic_independent(p,q,J)
    assert j_m%p==j0 and j1_m%p==j1
    assert W==(j0*k1-k0*j1)%p
    if p%24==13:
        assert j0==0 and j1!=0
        # selected factor F(1)=0 mod p^2: K(1)=-W/J'(1).
        source_res=(u*(j_m//p+W*pow(j1,-1,p))+e0)%p
        directly=S%m
    else:
        assert p%24==5 and j1==0 and j0!=0
        # selected factor F(1)+16 theta F(1)=0 mod p^2: K'(1)=W/J(1).
        source_res=(u*(16*(j1_m//p)-j0-16*W*pow(j0,-1,p))+e0+16*e1)%p
        directly=(S+16*D)%m
    assert source_res==directly//p%p if directly%p==0 else False
    return {"p":p,"q":q,"J0":j0,"J1":j1,"K0":k0,"K1":k1,"W":W,"e0":e0,"e1":e1,"selected":directly,"residue":source_res}


def verify(p,full_poly=False):
    q,J=parameters(p)
    W,source,H=source_flux(p,q,J)
    j0,j1,k0,k1,w0,K=harmonic_independent(p,q,J)
    assert sum(W)%p==w0
    if full_poly:
        real=[0]*(max(0,2*q))
        for i,a in enumerate(J):
            for j,b in enumerate(K):
                if j:
                    real[i+j-1]=(real[i+j-1]+a*j*b)%p
        for i,a in enumerate(K):
            for j,b in enumerate(J):
                if j:
                    real[i+j-1]=(real[i+j-1]-a*j*b)%p
        assert real==W,(p,'coeffwise W')
    out=second_digit_observer(p,q,J,K,w0)
    return out

if __name__=='__main__':
    ps=primes_upto(5000)
    rows=[verify(p,full_poly=p<=503) for p in ps]
    assert len(ps)==168,len(ps)
    assert all(row['residue']==0 for row in rows)
    print('PASS primes=%d source_recursions=%d source_vs_direct_W=%d selected_gauss_modp2=%d' % (len(ps), sum(2*r['q'] for r in rows),sum(1 for r in rows if r['p']<=503),len(ps)))
    for x in rows:
        if x['p'] in (5,13,29,37,53,61,373):print('CASE',x)
