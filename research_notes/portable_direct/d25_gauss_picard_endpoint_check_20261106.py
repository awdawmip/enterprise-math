"""D25 original Gauss finite Picard--Fuchs endpoint and two-moment scalar.
All computations are exact modular integers / small rational fractions.
"""
from fractions import Fraction

def primes_upto(limit):
    ok=bytearray(b'\x01')*(limit+1)
    ok[:2]=b'\x00\x00'
    for k in range(2,int(limit**0.5)+1):
        if ok[k]:
            ok[k*k:limit+1:k]=b'\x00'*((limit-k*k)//k+1)
    return [k for k in range(limit+1) if ok[k]]

def rational_check(N):
    d=Fraction(1)
    S=T=M2=Fraction()
    for n in range(N):
        S+=d; T+=n*d; M2+=n*n*d
        if n<N-1:
            d*=Fraction((6*n+1)*(3*n+1),36*(n+1)**2)
    assert 18*M2-9*T-S==-(6*N-5)*(3*N-2)*d

def verify(p):
    mod=p**3
    d=1;S=T=M2=0
    for n in range(p):
        S=(S+d)%mod
        T=(T+n*d)%mod
        M2=(M2+n*n*d)%mod
        if n<p-1:
            d=d*(6*n+1)*(3*n+1)*pow(36*(n+1)**2,-1,mod)%mod
    assert d%(p*p)==0 and d//(p*p)%p==pow(10,-1,p)
    assert (18*M2-9*T-S)%mod==(-(6*p-5)*(3*p-2)*d)%mod==(-p*p)%mod
    K=(S+12*T)%mod
    assert (3*K+S-72*M2)%mod==4*p*p%mod

    # Independent original weighted 216 recurrence.
    a=1;W=0
    for n in range(p):
        W=(W+(6*n+1)*a)%mod
        if n<p-1:
            a=a*(2*n+1)*(3*n+1)*(3*n+2)*pow(36*(n+1)**3,-1,mod)%mod
    # Independent signed triangular reflection-prefix observer.
    m=(p-1)//6
    f=1;e=E=R=J=0
    for i in range(m+1):
        if i:
            if i==1:e=pow(10,-1,p)
            else:e=e*36*(i-1)**2*pow((6*i-1)*(3*i-1),-1,p)%p
            E=(E+e)%p;R=(R+i*e)%p
            J=(J+f*((1+6*i)*E-6*R))%p
        if i<m:
            f=f*(m-i)*(2*m-i)*pow(2*(i+1)**2,-1,p)%p
    inv3=pow(3,-1,mod)
    assert W==(24*S*M2-S*S*inv3+4*p*p*S*inv3-2*p*p*J)%mod
    if p%24 in (13,19):
        assert S%p==0
        G=S//p
        B=(24*G*M2-p*G*G*inv3)%(p*p)
        assert (B-1)%p==0
        Delta=((B-1)//p)%p
        assert (Delta-2*J)%p==((W-p)//(p*p))%p
        assert W==p # explicit finite observation, NOT an all-prime proof
    return (p,S,M2,J,W)

if __name__=="__main__":
    for N in range(1,12): rational_check(N)
    rows=[verify(p) for p in primes_upto(997) if p%6==1]
    assert len(rows)==80
    assert sum(p%24 in (13,19) for p,*_ in rows)==45
    for row in rows:
        if row[0] in (13,19,67,373): print(row)
    print("11 exact rational N / 80 prime finite identities / 45 target scalar checks PASS")
