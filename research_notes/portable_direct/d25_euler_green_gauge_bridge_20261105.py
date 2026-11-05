#!/usr/bin/env python3
"""Author-side exact Gauss/Euler/short-Jacobi Green normalisation bridge.
No native H0/B0 or service execution claims.
"""
from math import comb, isqrt


def selected_primes(limit):
    sieve = bytearray(b'\x01')*(limit+1)
    sieve[0:2] = b'\x00\x00'
    for d in range(2,isqrt(limit)+1):
        if sieve[d]:
            sieve[d*d:limit+1:d] = b'\x00'*(((limit-d*d)//d)+1)
    return [p for p in range(5,limit+1) if sieve[p] and p%8==5]


def check(p, coefficientwise=False):
    q=(p-5)//8; ell=(5*p-1)//8; N=(p+1)//2; mod=p*p
    inv9=pow(9,-1,mod); inv8=pow(8,-1,mod)
    u=pow(8*inv9%mod,N,mod)
    # Original Gauss coefficients evaluated at x=1/9; upper cutoff is explicit.
    f=[1]
    for k in range(1,p):
        f.append(f[-1]*(8*k-7)*(8*k-5)*pow(576*k*k,-1,mod)%mod)
    F=sum(f)%mod; FD=sum(k*v for k,v in enumerate(f))%mod
    Flo=sum(f[:ell+1])%mod; FloD=sum(k*v for k,v in enumerate(f[:ell+1]))%mod
    U0raw=sum(f[ell+1:])%mod; U1raw=sum(k*v for k,v in enumerate(f[ell+1:],ell+1))%mod
    assert U0raw%p==U1raw%p==0
    U0=U0raw//p; U1=U1raw//p
    # Finite Jacobi J and its genuinely p-local harmonic deformation K_h.
    jc=[]; h=[]; jpower=1
    harmonic=[0]*(3*q+2)
    for k in range(1,3*q+2):
        harmonic[k]=(harmonic[k-1]+pow(k,-1,p))%p
    for j in range(q+1):
        coeff=comb(q,j)*comb(3*q+1,j)*jpower%mod
        jc.append(coeff)
        hj=(harmonic[q]-harmonic[q-j]+3*(harmonic[3*q+1]-harmonic[3*q+1-j]))*pow(8,-1,p)%p
        h.append(hj)
        jpower=jpower*inv9%mod
    J0=sum(jc)%mod; J1=sum(j*c for j,c in enumerate(jc))%mod
    H0=sum((v%p)*k for v,k in zip(jc,h))%p
    H1=sum(j*(v%p)*k for j,(v,k) in enumerate(zip(jc,h)))%p
    # Earlier Gauss low-Euler and high-band exact source ports.
    K0numer=(Flo-u*J0)%mod
    K1numer=(FloD-u*(J1-N*inv8*J0))%mod
    assert K0numer%p==K1numer%p==0
    K0=K0numer//p; K1=K1numer//p
    V0=(K0+U0)%p; V1=(K1+U1)%p
    # Independent short (5/8,7/8) hypergeometric p^2 evaluation.
    c=[1]
    for j in range(1,q+1):
        c.append(c[-1]*(8*j-3)*(8*j-1)*pow(576*j*j,-1,mod)%mod)
    C0=sum(c)%mod; C1=sum(j*v for j,v in enumerate(c))%mod
    E0numer=(F-u*C0)%mod
    E1numer=(FD-u*(C1-N*inv8*C0))%mod
    assert E0numer%p==E1numer%p==0
    E0=E0numer//p; E1=E1numer//p
    assert (C0-J0+p*H0)%mod==0
    assert (C1-J1+p*H1)%mod==0
    assert E0==(V0+(u%p)*H0)%p
    assert E1==(V1+(u%p)*(H1-(N*pow(8,-1,p)%p)*H0))%p
    W=((J0%p)*H1-H0*(J1%p))%p
    if p%24==13:
        assert J0%p==0 and J1%p!=0
        green=(u*(J0//p+W*pow(J1%p,-1,p))+E0)%p
        reduced=((u%p)*(J0//p)+V0)%p
        selected=F
    else:
        assert p%24==5 and J1%p==0 and J0%p!=0
        green=(u*(16*(J1//p)-(J0%p)-16*W*pow(J0%p,-1,p))+E0+16*E1)%p
        reduced=(u*(16*(J1//p)-(J0%p))+V0+16*V1)%p
        selected=(F+16*FD)%mod
    assert selected%p==0 and green==reduced==selected//p%p
    if coefficientwise:
        # Verify polynomial E(z) = V(z/9) + (1-z/9)^N K_h(z)
        # on every coefficient, independently of scalar evaluations.
        ucoeff=[comb(N,i)*pow(-inv9,i,mod)%mod for i in range(N+1)]
        UJ=[0]*p; UC=[0]*p; UH=[0]*p
        for j in range(q+1):
            for i in range(N+1):
                if i+j<p:
                    UJ[i+j]=(UJ[i+j]+ucoeff[i]*jc[j])%mod
                    UC[i+j]=(UC[i+j]+ucoeff[i]*c[j])%mod
                    UH[i+j]=(UH[i+j]+(ucoeff[i]%p)*h[j]*(jc[j]%p))%p
        for k in range(p):
            e=(f[k]-UC[k])%mod; v=(f[k]-UJ[k])%mod
            assert e%p==v%p==0,(p,k,'divisibility')
            assert e//p%p==(v//p+UH[k])%p,(p,k,'polynomial-gauge')
    return dict(p=p, q=q, K0=K0,Ktheta=K1,U0=U0,Utheta=U1,V0=V0,Vtheta=V1,
                harmonicK0=H0,harmonicKtheta=H1,W=W,e0=E0,e1=E1,
                green=green,normalized=reduced,selected=selected)


if __name__=='__main__':
    ps=selected_primes(5000)
    rows=[check(p,coefficientwise=p<=149) for p in ps]
    assert len(rows)==168
    assert all(row['green']==0 for row in rows)
    print('PASS primes=%d coefficientwise=%d selected_second_digit_zero=%d' %
          (len(rows),sum(p<=149 for p in ps),sum(row['normalized']==0 for row in rows)))
    for r in rows:
        if r['p'] in (5,13,29,37,53,373): print('CASE',r)
