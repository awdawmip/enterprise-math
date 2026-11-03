#!/usr/bin/env python3
"""Exact four-moment normal form for the p-lifted D25 high-strip Green operator."""
from math import isqrt, comb

def primes():
    for p in range(7,2001):
        if p % 6 == 1 and all(p % q for q in range(2,isqrt(p)+1)):
            yield p

def mul(a,b,M):
    v=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b): v[i+j]=(v[i+j]+x*y)%M
    return v

def add(a,b,M):
    return [((a[i] if i<len(a) else 0)+(b[i] if i<len(b) else 0))%M
            for i in range(max(len(a),len(b)))]

def trim(v):
    while len(v)>1 and v[-1]==0: v.pop()
    return v

def shift1(P,M):
    v=[0]*len(P)
    for i,a in enumerate(P):
        for j in range(i+1):v[j]=(v[j]+comb(i,j)*a)%M
    return v

def operator(P,p,M):
    # (2s+3) times L_p(P), a polynomial after clearing the denominator.
    b=shift1(P,M)
    inv9=pow(9,-1,M);inv18=pow(18,-1,M)
    A=[(35*inv9)%M,(107*inv9)%M,(108*inv9)%M,(36*inv9)%M]
    X=[1,6,12,8] # (2s+1)^3
    D=[(111*inv18)%M,(220*inv18)%M,(108*inv18)%M]
    a=mul([3,2],add(mul(A,b,M),[-x%M for x in mul(X,P,M)],M),M)
    d=mul(D,b,M)
    return trim(add(a,[(p*x)%M for x in d],M))

def reduce_w(W,p,M):
    rem=trim(W[:]);P=[0]
    while len(rem)>4:
        m=len(rem)-5
        a=rem[-1]*pow(-8,-1,M)%M
        cand=[0]*m+[a]
        P=add(P,cand,M)
        rem=trim(add(rem,[-x%M for x in operator(cand,p,M)],M))
    return trim(P),rem

def orig(k,p,M,F):
    return F[2*k]*F[3*k]*pow(F[k],-5,M)*pow(216,-k,M)%M

def one(p):
    r=(p-1)//6;n=3*r;M=p*p
    F=[1]*(3*(4*r+1)+1)
    for i in range(1,len(F)):
        v=i
        while v%p==0:v//=p
        F[i]=F[i-1]*v%M
    ys=[orig(n+1+s,p,M,F) for s in range(r)]
    yr=p*orig(4*r+1,p,M,F)%M
    moments=[sum(pow(s,j,M)*ys[s]*pow(2*s+3,-1,M) for s in range(r))%M
             for j in range(4)]
    for deg in range(4,11):
        W=[0]*deg+[1]
        P,rem=reduce_w(W,p,M)
        assert len(rem)<=4
        assert trim(add(operator(P,p,M),rem,M))==W,('poly',p,deg)
        lhs=sum(pow(s,deg,M)*ys[s]*pow(2*s+3,-1,M) for s in range(r))%M
        rhs=(sum(rem[j]*moments[j] for j in range(len(rem)))+
             pow(2*r+1,3,M)*yr*sum(P[i]*pow(r,i,M) for i in range(len(P)))
             -P[0]*ys[0])%M
        assert lhs==rhs,('observer',p,deg,lhs,rhs)
    N4=sum(pow(s,4,M)*ys[s]*pow(2*s+3,-1,M) for s in range(r))%M
    inv=lambda n:pow(n,-1,M)
    expected=(ys[0]*inv(8)-pow(2*r+1,3,M)*yr*inv(8)
              -3*inv(2)*moments[3]
              +(53*inv(36)+3*p*inv(4))*moments[2]
              +(211*inv(72)+55*p*inv(36))*moments[1]
              +(13*inv(12)+37*p*inv(48))*moments[0])%M
    assert N4==expected,('N4',p,N4,expected)
    return(p,r,N4,tuple(moments),yr)

def main():
    count=0;slots=0
    for p in primes():
        z=one(p);count+=1;slots+=z[1]
        if p in (7,13,19,37,373):print('sample',z)
    print('PASS',count,'primes,',slots,'source positions, polynomial degrees 4..10, exact mod p^2 normal form')

if __name__=='__main__':main()
