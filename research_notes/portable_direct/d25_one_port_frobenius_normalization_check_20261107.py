"""Exact D25 Fricke single-port reduction; finite original 216/2304 check, not native H0/B0."""
from math import comb, isqrt

def prime_list(hi):
    for p in range(5, hi):
        if all(p % d for d in range(2, isqrt(p)+1)):
            yield p

def chi(a,p):
    return 1 if pow(a%p,(p-1)//2,p)==1 else -1

def sums(p,mode="ratio"):
    M=p**4
    A=J=B=K=0
    if mode=="ratio":
        a=b=1
        inv36=pow(36,-1,M); inv576=pow(576,-1,M)
        for k in range(p):
            A=(A+a)%M;J=(J+k*a)%M
            B=(B+b)%M;K=(K+k*b)%M
            if k<p-1:
                inv=pow((k+1)**3,-1,M)
                a=a*(3*k+1)*(3*k+2)*(2*k+1)*inv*inv36%M
                b=b*(4*k+1)*(4*k+2)*(4*k+3)*inv*inv576%M
    elif mode=="binomial":
        x=y=1;inv216=pow(216,-1,M);inv2304=pow(2304,-1,M)
        for k in range(p):
            a=comb(2*k,k)**2*comb(3*k,k)*x%M
            b=comb(2*k,k)**2*comb(4*k,2*k)*y%M
            A=(A+a)%M;J=(J+k*a)%M
            B=(B+b)%M;K=(K+k*b)%M
            x=x*inv216%M;y=y*inv2304%M
    else: raise ValueError(mode)
    return A,J,B,K

def check(p,mode="ratio"):
    M=p**4;A,J,B,K=sums(p,mode)
    Q=lambda x,d:x*pow(d,-1,M)%M
    W=(A+6*J)%M;V=(B+8*K)%M
    u=(-2*J+Q(7*B,8)+4*K)%M
    v=(Q(3*J,2)-Q(5*B,8)-3*K)%M
    assert (3*u+4*v-Q(B,8))%M==0
    assert (-Q(3*B,4)+18*u+24*v)%M==0
    assert (A-3*u+Q(9*B,8)-W+Q(3*V,2))%M==0
    c=chi(-3,p)
    F=(Q(V,2)-A-Q(9*B,8)+3*u-p*c)%M
    assert F==(2*V-W-p*c)%M
    baseline=(Q(p*c,6)+Q(A,3)+Q(3*B,8))%M
    delta=(u-baseline)%M
    eg=None
    if (V-p*c)%p**3==0 and delta%p**3==0:
        eta=((V-p*c)%M//p**3)%p
        gamma=(delta//p**3)%p
        assert (eta*pow(2,-1,p)+3*gamma)%p==F//p**3
        eg=(eta,gamma)
    return (A,J,B,K,u,v,W,V,F,eg)

def main():
    count=0; normalized=0; observed_bridge=0
    samples={}
    for p in prime_list(2000):
        result=check(p);count+=1
        F=result[8];eg=result[9]
        if eg is not None: normalized+=1
        if F==0: observed_bridge+=1
        if p in (13,19,43,67,373):
            assert check(p,"binomial")==result
            samples[p]=eg
    assert (count,normalized,observed_bridge)==(301,301,301)
    for p,(eta,gamma) in samples.items():
        print(f"p={p} eta={eta} gamma={gamma} residual=0")
    print("PASS 301 primes p<2000, five independent binomial recalculations; finite evidence only")

if __name__=="__main__":
    main()
