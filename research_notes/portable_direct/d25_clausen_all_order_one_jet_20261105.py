"""D25: exact all-order one-jet recurrence and Hensel lift (2<=r<=p).
Author-side verification; original native H0/B0 is not simulated.
"""
import math

def primes_1mod6(limit):
    for p in range(7,limit+1,6):
        if all(p%d for d in range(2,math.isqrt(p)+1)): yield p

def one_jet(p,r):
    n=(p-1)//6; M=p**r; term=1; g=1; J=0
    for k in range(n):
        den=(k+1)*(2*k+2-p)
        term=term*(k-n)*(k-2*n)*pow(den,-1,M)%M
        g=(g+term)%M; J=(J+(k+1)*term)%M
    return g,2*J%M

def derivatives(p,r,g,v):
    M=p**r; u=p-1; n=(p-1)//6; q=[g,v]
    for m in range(r-1):
        c=4*m*(m-1)-2*m*(u-2)+8*n*n
        q.append((u*q[-1]+c*q[-2])%M)
    return q

def psi_jet(p,r,h,q):
    M=p**r; g=0; v=0; power=1; fac=1
    for m in range(r):
        if m: power=power*h%M; fac*=m
        w=power*pow(fac,-1,M)%M
        g=(g+w*q[m])%M; v=(v+w*q[m+1])%M
    z=(pow(2,-1,M)+h)%M
    return g*(g+12*z*v)%M

def psi_original(p,r,h):
    M=p**r; n=(p-1)//6; z=(pow(2,-1,M)+h)%M
    term=1; g=1; J=0
    for k in range(n):
        d=(k+1)*(2*k+2-p)
        term=term*(2*(k-n)*(k-2*n))*z*pow(d,-1,M)%M
        g=(g+term)%M; J=(J+(k+1)*term)%M
    return g*(g+12*J)%M

def lift(p,r):
    assert p>=7 and p%6==1 and 2<=r<=p
    M=p**r; g,v=one_jet(p,r); q=derivatives(p,r,g,v)
    assert psi_jet(p,r,0,q)==psi_original(p,r,0)
    A=(14*g*v+6*(v*v+g*q[2]))%p
    assert psi_original(p,r,0)%p==0 and A!=0
    inv=pow(A,-1,p); h=0
    for e in range(1,r):
        f=psi_jet(p,r,h,q)
        assert f%(p**e)==0
        digit=(-(f//(p**e))*inv)%p
        h+=digit*p**e
        assert psi_jet(p,r,h,q)%(p**(e+1))==0
    assert psi_original(p,r,h)==0
    return (pow(2,-1,M)+h)%M,A

def main():
    data=[]; tested=0
    for p in primes_1mod6(1200):
        root,A=lift(p,6); tested+=1
        if p in (7,13,19,31,37,73,373):
            data.append((p,root,A,root%(p**4)))
    assert tested==94
    assert {p:r4 for p,_,_,r4 in data if p in (13,19,373)}=={13:23888,19:62406,373:7348554128}
    print("PASS",tested,"primes p=1 (mod 6), 7<=p<=1200, r=6")
    for p,root,A,r4 in data:
        print(f"p={p} root_mod_p6={root} dPsi_mod_p={A} root_mod_p4={r4}")

if __name__=="__main__": main()
