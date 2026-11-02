#!/usr/bin/env python3
"""D25 author-side Hensel/Teich and original Cauchy carry certificate, exact Z/p^k only."""
from math import isqrt, comb

def inv(a,n):
    return pow(a%n,-1,n)

def targets(limit):
    sieve=bytearray(b'\x01')*(limit+1)
    sieve[:2]=b'\0\0'
    for j in range(2,isqrt(limit)+1):
        if sieve[j]:
            sieve[j*j:limit+1:j]=b'\0'*((limit-j*j)//j+1)
    return [p for p in range(7,limit+1) if sieve[p] and p%24 in (13,19)]

def cm(p):
    r=(p-1)//6; M=p*p; z=inv(2,M); P=ck=zp=1; J=0
    for k in range(1,r+1):
        ck=ck*(r-k+1)*(2*r-k+1)*inv(k*k,M)%M
        zp=zp*z%M; v=ck*zp%M
        P=(P+v)%M; J=(J+k*v)%M
    assert P%p==0 and J%p!=0
    j=J%p; tc=-(P//p)*inv(2*j,p)%p
    w=pow(z,p,M); tt=((w-z)%M)//p
    assert tt==(-(((pow(2,p-1,M)-1)%M)//p)*inv(2,p))%p
    assert pow(w,p-1,M)==1
    def eval_at(z):
        C=Z=ans=1
        for k in range(1,r+1):
            C=C*(r-k+1)*(2*r-k+1)*inv(k*k,M)%M
            Z=Z*z%M; ans=(ans+C*Z)%M
        return ans
    assert eval_at((z+p*tc)%M)==0
    PW=eval_at(w)
    assert PW%p==0 and PW//p==2*j*(tt-tc)%p
    return j,P//p,tc,tt,PW//p

def carry(p):
    r=(p-1)//6; A=B=1; U=V=K0=K1=L0=L1=0
    for m in range(1,2*r+1):
        A=A*(2*m-1)*(3*m-2)*(3*m-1)*inv(36*m**3,p)%p
        B=B*(2*m-1)*inv(4*m,p)%p
        u=-inv(4*m*B,p)
        V=(V+U)%p; U=(U+u)%p
        K0=(K0+A*U)%p; K1=(K1+A*V)%p
        L0=(L0+m*A*U)%p; L1=(L1+m*A*V)%p
    return K0,K1,L0,L1

def triangle(p,z,via_binomial=False):
    M=p**3; A=[]; B=[]
    if via_binomial:
        v=1
        for k in range(p):
            A.append(comb(2*k,k)**2*comb(3*k,k)*v%M)
            v=v*inv(108,M)*z%M
        v=1
        for k in range(p):
            B.append(comb(2*k,k)*v%M)
            v=v*inv(8,M)%M
    else:
        a=1;A=[1]
        for k in range(1,p):
            a=a*(2*k-1)*(3*k-2)*(3*k-1)*inv(18*k**3,M)*z%M
            A.append(a)
        B=[1]
        for k in range(1,p):
            B.append(B[-1]*(2*k-1)*inv(4*k,M)%M)
    S=[0]*(p+1);W=[0]*(p+1)
    for j in range(p-1,-1,-1):
        S[j]=(S[j+1]+B[j])%M;W[j]=(W[j+1]+j*B[j])%M
    C0=C1=0
    for m in range(1,p):
        C0=(C0+A[m]*S[p-m])%M
        C1=(C1+A[m]*(m*S[p-m]+W[p-m]))%M
    return C0,C1

def main():
    arr=targets(10000); ndirect=nindep=0; cases=[]
    for p in arr:
        j,pq,tc,tt,pw=cm(p)
        k0,k1,l0,l1=carry(p)
        assert (k0,k1,l0)==(0,(p-1)//2,p-1) # finite hypotheses only
        actual=('n/a','n/a')
        if p<=3000:
            M=p**3; z=inv(2,M); zc=(z+p*tc)%M; zt=(z+p*tt)%M
            C=triangle(p,zc); T=triangle(p,zt)
            assert C[0]%p==C[1]%p==0
            assert C[0]//p%p==k0 and C[1]//p%p==k1
            actual=tuple(((T[i]-C[i])%M)//(p*p) for i in (0,1))
            assert actual==(2*(tt-tc)*l0%p,2*(tt-tc)*l1%p)
            ndirect+=1
            if p in (13,19,37,373):
                assert triangle(p,zc,True)==C
                assert triangle(p,zt,True)==T
                nindep+=2
        if p in (13,19,37,373,1171):
            cases.append((p,j,pq,tc,tt,(tt-tc)%p,pw,k0,k1,l0,l1,*actual))
    print("EXACT_AUTHOR_CHECK: target primes p<=10000:",len(arr))
    print("Hensel/Teich formula + K0=0 K1=-1/2 L0=-1 finite checks: PASS")
    print("Independent original triangular C0/C1 comparisons p<=3000:",ndirect,"PASS")
    print("Original integer-binomial cross-checks:",nindep,"PASS")
    print("p | J1 | P/p | tCM | tT | gap | P(Teich)/p | K0 | K1 | L0 | L1 | DeltaC0/p² | DeltaC1/p²")
    for row in cases:print(" | ".join(map(str,row)))

if __name__=="__main__":
    main()
