"""D25 exact integer-shadow Clausen/harmonic second-jet verification, 2026-11-05."""
from math import comb
from fractions import Fraction

def primes(bound):
    a=[True]*(bound+1);a[:2]=[False,False]
    for i in range(2,int(bound**0.5)+1):
        if a[i]:
            a[i*i:bound+1:i]=[False]*((bound-i*i)//i+1)
    return [p for p in range(7,bound+1) if a[p] and p%6==1]

def test(p):
    n=(p-1)//6;mod=p**3
    inv=lambda x:pow(x%mod,-1,mod)
    h=G=1;J=0
    for k in range(n):
        h=h*(k-n)*(k-2*n)*inv(k+1)*inv(2*k+2-p)%mod
        G=(G+h)%mod;J=(J+(k+1)*h)%mod
    S=U1=U11=U2=H1=H2=0
    for k in range(2*n+1):
        if k:
            r=inv(k);H1=(H1+r)%mod;H2=(H2+r*r)%mod
        f=(-1)**k*comb(2*n,k)*comb(3*n,k)*comb(4*n,k)
        f=f*pow(inv(2),k,mod)%mod
        w=(6*k+1)*f%mod
        S=(S+w)%mod;U1=(U1+w*H1)%mod
        U11=(U11+w*H1*H1)%mod;U2=(U2+w*H2)%mod
    E1=3*U1*inv(2)%mod; E2=(9*U11+5*U2)*inv(8)%mod
    assert S==(G*(G+12*J)-p*E1-p*p*E2)%mod,(p,S)
    return (p,G%p,(G+12*J)%p,S,E1%(p*p),E2%p)

def rational_clausen(n):
    p=6*n+1;c=Fraction(1,2)-3*n
    g=[Fraction(1)]
    for k in range(n):
        g.append(g[-1]*Fraction((k-n)*(k-2*n),k+1)/(c+k))
    for k in range(2*n+1):
        a=Fraction((-1)**k*comb(2*n,k)*comb(3*n,k)*comb(4*n,k))
        for j in range(1,k+1):
            a*=Fraction(2*j*j,(j-p)*(2*j-p))
        assert a==sum(g[t]*g[k-t] for t in range(max(0,k-n),min(k,n)+1)),(n,k)

if __name__=="__main__":
    ps=primes(1200)
    for p in ps:test(p)
    for n in (1,2,3):rational_clausen(n)
    print("PASS",len(ps),"primes; rational n=1,2,3")
    for p in (7,13,19,31,37,73,373):print(test(p))
