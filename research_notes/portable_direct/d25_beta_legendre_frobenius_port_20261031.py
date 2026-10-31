"""D25 beta-specific Legendre p-adic observer certificate.

Exact universal polynomial identity is proved in the companion research note.
Selected mod-p^2 vanishing is checked only for the ten finite primes below.
"""
from math import comb, factorial

PRIMES=[5,7,13,23,29,31,37,47,71,373]

def q_coeff(n, m):
    assert n%2==1
    inv=pow(2,-n,m)
    a=[0]*((n+1)//2)
    for j in range((n+1)//2):
        a[(n-1)//2-j]=((-1)**j*comb(n,j)*comb(2*n-2*j,n)*inv)%m
    return a

def q_values(q,s,m):
    v=d=0
    for j,c in enumerate(q):
        v=(v+c*pow(s,j,m))%m
        if j:
            d=(d-j*c*pow(s,j-1,m))%m
    return v,d

def polynomial_check(p,n,e,q):
    m=(n-1)//2
    Qz=[0]*(m+1)
    for k,c in enumerate(q):
        for j in range(k+1):
            Qz[j]=(Qz[j]+c*comb(k,j)*((-1)**j))%p
    S=[0]*(e+m+1)
    for a in range(e+1):
        for b,c in enumerate(Qz):
            S[a+b]=(S[a+b]+((-1)**a)*comb(e,a)*c)%p
    F=[1]
    c=1
    for k in range(p-1):
        c=c*(8*k+1)*(8*k+3)*pow(64*(k+1)**2,-1,p)%p
        F.append(c)
    assert len(S)<p
    assert S==F[:len(S)]
    assert all(c==0 for c in F[len(S):])
    return len(S)-1

def verify(p):
    m=p*p
    n=(p-1)//4 if p%8==5 else (p-3)//4
    e=(p+1)//2
    q=q_coeff(n,m)
    z=pow(9,-1,m)
    s=8*z%m
    q0,dq=q_values(q,s,m)
    se=pow(s,e,m)
    G0=se*q0%m
    H0=se*(-p*q0+16*z*dq)%m
    G=H=0
    term=1
    for k in range(p):
        if p in (5,7,13,23,29):
            numerator=1
            for j in range(k):
                numerator*=(8*j+1)*(8*j+3)
            assert numerator*pow(576**k*factorial(k)**2,-1,m)%m==term
        G=(G+term)%m
        H=(H+(16*k+1)*term)%m
        if k+1<p:
            term=term*(8*k+1)*(8*k+3)*pow(576*(k+1)**2,-1,m)%m
    assert (G-G0)%p==0
    assert (H-H0)%p==0
    dG=((G-G0)%m)//p
    dH=((H-H0)%m)//p
    chi=pow(3,(p-1)//2,p)
    choose='G' if chi==1 else 'H'
    selected=G if choose=='G' else H
    if choose=='G':
        assert q0%p==0
        carry=se*(q0//p)%p
        defect=dG
    else:
        assert dq%p==0
        carry=se*(-q0+16*z*(dq//p))%p
        defect=dH
    assert (carry+defect)%p==selected//p%p
    assert selected==0, (p,choose,selected)
    degree=polynomial_check(p,n,e,[c%p for c in q])
    return p,n,degree,choose,q0%p,dq%p,carry,defect

if __name__=="__main__":
    print("p n deg selected Q_mod_p Qprime_mod_p carry defect")
    for p in PRIMES:
        print(*verify(p))
    print("PASS 10 exact polynomial and selected-p2 finite checks; 5 direct numerator checks")
