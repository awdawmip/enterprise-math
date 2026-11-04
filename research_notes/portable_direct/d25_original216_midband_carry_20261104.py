#!/usr/bin/env python3
"""Exact original-216 middle-band p-adic carry check (author evidence)."""
def primes(n):
    sieve=[True]*(n+1); sieve[:2]=[False,False]
    for i in range(2,int(n**.5)+1):
        if sieve[i]:
            for j in range(i*i,n+1,i): sieve[j]=False
    return [p for p in range(7,n+1) if sieve[p] and p%6==1]
def facts(p,M,n):
    U=[1]*(n+1); v=[0]*(n+1)
    for k in range(1,n+1):
        x=k; e=0
        while x%p==0: x//=p; e+=1
        U[k]=U[k-1]*x%M; v[k]=v[k-1]+e
    return U,v
def term(U,v,k,p,M,quartic=False):
    if quartic:
        e=v[4*k]-4*v[k]
        x=U[4*k]*pow(U[k],-4,M)*pow(pow(2304,k,M),-1,M)%M
    else:
        e=v[2*k]+v[3*k]-5*v[k]
        x=U[2*k]*U[3*k]*pow(U[k],-5,M)*pow(pow(216,k,M),-1,M)%M
    return e,x
def check(p):
    r=(p-1)//6; h=(p-1)//2; N=p**3; M=p*p
    U,v=facts(p,N,max(4*h,3*(p-1)))
    low=mid=high=0
    for k in range(p):
        e,x=term(U,v,k,p,N)
        z=(6*k+1)*pow(p,e,N)*x%N
        if k<=2*r:low=(low+z)%N
        elif k<=3*r:mid=(mid+z)%N
        elif k<=4*r:high=(high+z)%N
        else:assert e>=3
    half=0
    for k in range(h+1):
        e,x=term(U,v,k,p,N,True)
        half=(half+(8*k+1)*pow(p,e,N)*x)%N
    assert mid%p==0 and high%M==0
    e,gamma=term(U,v,2*r+1,p,M); assert e==1
    K=1; D=0; A=0; E=0; midpoint=0
    for s in range(r):
        e,x=term(U,v,2*r+1+s,p,M);assert e==1
        assert x==gamma*K*(1+p*D)%M,(p,s,x)
        w=5+6*s
        midpoint=(midpoint+(w+2*p)*x)%M
        A=(A+w*K)%M; E=(E+2*K+w*K*D)%p
        if s<r-1:
            K=K*3*(6*s+7)*(s+1)*(3*s+4)*pow(4*(3*s+5)**3,-1,M)%M
            d=(2*pow(6*s+7,-1,p)+pow(3*(s+1),-1,p)+pow(3*s+4,-1,p)-3*pow(3*s+5,-1,p))%p
            D=(D+d)%p
    assert midpoint==mid//p%M==gamma*(A+p*E)%M,(p,midpoint)
    if p%24 in (13,19):
        assert (low-half)%p==0
        T=((low-half)%N)//p
        assert (T+mid//p)%p==0
        assert (T+mid//p+p*(high//M))%M==((low+mid+high-half)%N)//p
        if p in (13,19,373):
            print(dict(p=p,gamma=gamma,A=A,E=E,mid_div_p=mid//p,T_low=T,Hbar=high//M))
    return r
if __name__=="__main__":
    ps=primes(2000); positions=sum(check(p) for p in ps)
    print(f"PASS primes={len(ps)} mid_positions={positions} target_classes={sum(p%24 in (13,19) for p in ps)}")
