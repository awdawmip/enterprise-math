"""Exact integer author checker for D25 symmetric Green descent.
No external numerical libraries; p=6m+1, all declared tests use exact modular arithmetic.
No native CM Frobenius, Lean check or independent review is asserted.
"""
from math import comb
PRIMES = (13, 19, 37, 43, 61, 67, 211, 373)
EXPECTED = {13:(6,6),19:(3,98),37:(26,655),43:(6,1210),61:(21,753),67:(63,666),211:(43,26418),373:(286,99504)}

def plus(a,b,q):
    z=[0]*max(len(a),len(b))
    for i,x in enumerate(a): z[i]=(z[i]+x)%q
    for i,x in enumerate(b): z[i]=(z[i]+x)%q
    return z

def times(a,b,q):
    z=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b): z[i+j]=(z[i+j]+x*y)%q
    return z

def replace_z_with_1_minus_4y(coefs,q):
    z=[0]
    for x in reversed(coefs):
        z=times(z,[1,-4],q)
        z[0]=(z[0]+x)%q
    return z

def recurrence(n,q,initial):
    a,b=[initial],[1]
    for _ in range(2,n+1):
        a,b=b,plus(b,[0]+[-v for v in a],q)
    return b

def pairmul(x,y,q):
    a,b=x;c,d=y
    return ((a*c+2*b*d)%q,(a*d+b*c)%q)

def check_prime(p):
    n=(p-1)//3
    assert p==3*n+1 and n%2==0 and p>=13
    q=p*p;r=p**3
    c=[1]
    for k in range(n):
        c.append(c[-1]*(3*k+1)*(3*k+2)*(3*k+3)*pow(27*(k+1)**3,-1,r)%r)
    # Expand original A((1-t)/2), independently of the prior Green inverse.
    x=[0]*(n+1)
    for k,ck in enumerate(c):
        a=ck*pow(2,-k,r)%r
        for j in range(k+1):x[j]=(x[j]+(-1)**j*a*comb(k,j))%r
    assert all(x[j]%p==0 for j in range(1,n+1,2))
    G=replace_z_with_1_minus_4y([x[j]%q for j in range(0,n+1,2)],q)
    Phi=replace_z_with_1_minus_4y([2*(x[j]//p)%q for j in range(1,n+1,2)],q)
    F=recurrence(n-1,q,1)
    S=recurrence(n,q,2)
    C=(p+1)*c[-1]*pow(9,-1,q)%q
    FG=times(F,G,q)
    SP=[p*pow(2,-1,q)*v%q for v in times(S,Phi,q)]
    integrand=plus(FG,SP,q)
    Y=pow(8,-1,q)
    integral=(-C*sum(v*pow(i+1,-1,q)*pow(Y,i+1,q)
                     for i,v in enumerate(integrand)))%q
    leading=(-C*sum(v*pow(i+1,-1,p)*pow(Y%p,i+1,p)
                    for i,v in enumerate(FG)))%p
    # Independent raw A(u), A'(u) in quadratic coefficient ring modulo p^3.
    iv4=pow(4,-1,r)
    u=(2*iv4%r,-iv4%r)
    A=(0,0);Aprime=(0,0);power=(1,0);previous=(1,0)
    for k,ck in enumerate(c):
        A=((A[0]+ck*power[0])%r,(A[1]+ck*power[1])%r)
        if k:
            Aprime=((Aprime[0]+k*ck*previous[0])%r,
                    (Aprime[1]+k*ck*previous[1])%r)
        previous,power=power,pairmul(power,u,r)
    a,b=A;e,d=Aprime
    B=(a,-b%r);Bprime=(-e%r,d)
    left=pairmul(A,Bprime,r);right=pairmul(Aprime,B,r)
    W=tuple((left[j]-right[j])*pow(8,-1,r)%r for j in (0,1))
    assert W[1]==0 and W[0]%p==0
    assert (leading,integral)==EXPECTED[p]
    assert W[0]//p==integral
    assert leading==integral%p
    return p,leading,integral,W[0]

if __name__=="__main__":
    for v in map(check_prime,PRIMES):
        print("p=%d leading=%d full_mod_p2=%d W_mod_p3=%d PASS"%v)
