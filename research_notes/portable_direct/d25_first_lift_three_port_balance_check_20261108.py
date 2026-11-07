#!/usr/bin/env python3
"""D25 first-lift: independent exact checks; AUTHOR_SIDE, not native H0/B0."""
from math import comb

def primes(n):
    sieve=[True]*(n+1)
    sieve[:2]=[False,False]
    for q in range(2,int(n**0.5)+1):
        if sieve[q]:
            sieve[q*q:n+1:q]=[False]*(((n-q*q)//q)+1)
    return [p for p in range(5,n+1) if sieve[p] and p%24 in (13,19)]

def base(u,v,z,p):
    mod=p*p
    return sum(comb(u,n)*comb(v,n)*pow(z,-n,mod)
               for n in range(u+1))%mod

def gauss(p,a,b,A,B,z):
    mod=p*p
    term=1;total=1
    for n in range(1,p):
        j=n-1
        term=term*(a+A*j)*(b+B*j)*pow(A*B*z*n*n,-1,mod)%mod
        total=(total+term)%mod
    return total

def derivative_ports(u,v,z,lam,mu,p):
    h1=h2=0;low=0
    for n in range(u+1):
        if n:
            h1=(h1+pow(n-1-u,-1,p))%p
            h2=(h2+pow(n-1-v,-1,p))%p
        fn=comb(u,n)*comb(v,n)*pow(z,-n,p)%p
        low=(low+fn*(lam*h1+mu*h2))%p
    fac=[1]*(v+1)
    for n in range(1,v+1):
        fac[n]=fac[n-1]*n%p
    tail=0
    for n in range(u+1,v+1):
        der=(-1)**(u+n)*fac[u]*fac[n-u-1]*fac[v]
        der=der*pow(fac[v-n]*fac[n]*fac[n],-1,p)%p
        tail=(tail+lam*der*pow(z,-n,p))%p
    return low,tail

def check(p):
    eps=int(p%24==13)
    m=(p-1)//6
    k=(p-(5 if eps else 3))//8
    QA,QB=base(m,2*m,2,p),base(k,3*k+1,9,p)
    GA=gauss(p,1,1,6,3,2)
    GB=gauss(p,3+2*eps,1+6*eps,8,8,9)
    assert QA%p==QB%p==GA%p==GB%p==0
    qA,qB=QA//p,QB//p
    gA,gB=GA//p,GB//p
    LA,TA=derivative_ports(m,2*m,2,pow(6,-1,p),pow(3,-1,p),p)
    LB,TB=derivative_ports(k,3*k+1,9,pow(8,-1,p),3*pow(8,-1,p),p)
    assert (qA+LA+TA-gA)%p==0
    assert (qB+LB+TB-gB)%p==0
    JA=sum(n*comb(m,n)*comb(2*m,n)*pow(2,-n,p)
           for n in range(m+1))%p
    JB=sum(n*comb(k,n)*comb(3*k+1,n)*pow(9,-n,p)
           for n in range(k+1))%p
    assert JA and JB
    t=(-pow(8,-1,p) if eps else pow(6,-1,p))*JA*pow(JB,-1,p)%p
    r=(-4*pow(27,-1,p) if eps else 2*pow(9,-1,p))%p
    RQ,RL,RT=(t*qA-r*qB)%p,(t*LA-r*LB)%p,(t*TA-r*TB)%p
    assert (RQ+RL+RT)%p==(t*gA-r*gB)%p
    return dict(p=p,epsilon=eps,qA=qA,qB=qB,gA=gA,gB=gB,
                LA=LA,TA=TA,LB=LB,TB=TB,JA=JA,JB=JB,t=t,r=r,
                RQ=RQ,RL=RL,RT=RT,observed_C_basis=(RQ+RL+RT)%p)

def main():
    rows=[check(p) for p in primes(2000)]
    assert len(rows)==77
    # The following 77-prime cross-model assertion is experimental, not proved:
    assert all(row["observed_C_basis"]==0 for row in rows)
    for row in rows:
        if row["p"] in (13,19,43,67,373): print(row)
    print("PASS: 77 p; both proved first-order expansions; "
          "cross-model equality checked in this finite sample only")

if __name__=="__main__":
    main()
