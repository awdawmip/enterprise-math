"""D25 W216: unsigned Clausen square, signed first jet, exact p-adic checks.
Author-side reproducible arithmetic; not a native H0/B0 result or formal review.
"""
from math import isqrt

def primes_to(n):
    sieve=bytearray(b"\x01")*(n+1)
    sieve[:2]=b"\x00\x00"
    for k in range(2,isqrt(n)+1):
        if sieve[k]:
            sieve[k*k:n+1:k]=b"\x00"*((n-k*k)//k+1)
    return [k for k in range(2,n+1) if sieve[k]]

def certificate(p, direct=False):
    assert p>3 and p%6==1 and p in primes_to(p)
    m=(p-1)//6
    mod=p**3
    A=[1]*p
    B=[1]*p
    for k in range(p-1):
        A[k+1]=(A[k]*(2*k+1)*(3*k+1)*(3*k+2)
                *pow(36*(k+1)**3,-1,mod))%mod
        B[k+1]=(B[k]*(6*k+1)*(3*k+1)
                *pow(36*(k+1)**2,-1,mod))%mod
    J=sum(B)%mod
    K=sum(k*B[k] for k in range(p))%mod
    F=sum(A)%mod
    W=sum((6*k+1)*A[k] for k in range(p))%mod
    Q0=(J*J-F)%mod
    Qw=(J*J+12*J*K-W)%mod
    assert Q0%(p*p)==0 and Qw%(p*p)==0
    S=T=U=R=0
    for i in range(1,m+1):
        assert B[p-i]%(p*p)==0
        v=B[p-i]//(p*p)%p
        S=(S+v)%p
        T=(T+i*v)%p
        U=(U+2*B[i]*S)%p
        R=(R+2*B[i]*((6*i+1)*S-6*T))%p
    assert U==Q0//(p*p)%p
    assert R==Qw//(p*p)%p
    assert F==(J*J-p*p*U)%mod
    if direct:
        q0=qw=0
        for i in range(p):
            for j in range(p-i,p):
                v=B[i]*B[j]
                q0=(q0+v)%mod
                qw=(qw+(6*(i+j)+1)*v)%mod
        assert q0==Q0 and qw==Qw
    result={"p":p,"J_mod_p":J%p,"K_mod_p":K%p,
            "U":U,"R":R,"F_mod_p2":F%(p*p),"W_mod_p2":W%(p*p)}
    if J%p==0:
        j=J//p%(p*p)
        assert F%(p*p)==0
        alpha=F//(p*p)%p
        assert alpha==(j*j-U)%p
        result.update(j=j%p,alpha=alpha)
        if W%(p*p)==p:
            assert (12*j*K-1)%p==0
            tau=(12*j*K-1)//p%p
            lam=(W-p)//(p*p)%p
            assert lam==(tau+j*j-R)%p
            result.update(tau=tau,lambda_p=lam)
    return result

if __name__=="__main__":
    ps=[p for p in primes_to(2000) if p%6==1]
    for p in ps:
        c=certificate(p,direct=p in (7,13,19,37,43,373,997))
        if p%24 in (13,19):
            assert c["J_mod_p"]==0
            assert c["F_mod_p2"]==0
            assert c["W_mod_p2"]==p
    print("PASS: 148 p=1(mod6) primes <=2000, independent double sums at 7 selected primes")
    for p in (13,19,37,43,373,997,10069,10099):
        print(certificate(p))
