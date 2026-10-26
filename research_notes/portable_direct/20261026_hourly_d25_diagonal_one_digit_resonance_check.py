#!/usr/bin/env python3
"""Exact author-level corrected-Hasse jets and oriented one-digit Green checks."""
from fractions import Fraction as Q
from math import isqrt
CHANNELS = [(0,2),(1,2),(0,3)]

def jets(m, order=3):
    p=6*m+1
    u=[[Q(0) for _ in range(order+1)] for r in range(p)]
    u[0][0]=Q(1)
    def get(r,k):return u[r][k] if 0<=k<=order and 0<=r<p else Q(0)
    for r in range(1,p):
        A=Q(r)*(Q(r)-Q(p,2));B=Q(r-1-m)*Q(r-1-2*m);C=Q(3*(r-1)-4*m)
        for k in range(order+1):
            u[r][k]=(B*get(r-1,k)+3*r*get(r,k-1)-C*get(r-1,k-1)+2*get(r-1,k-2))/A
    return p,u

def direct_product_jets(m, order=3):
    """Independent truncated finite Pochhammer product, not the Hasse recurrence."""
    p=6*m+1
    arr=[[Q(0) for _ in range(order+1)] for _ in range(p)]
    arr[0][0]=Q(1)
    def mul(a,b):
        out=[Q(0)]*(order+1)
        for i in range(order+1):
            for j in range(order+1-i):
                out[i+j]+=a[i]*b[j]
        return out
    for r in range(1,p):
        f1=[Q(r-1-m),Q(-1)]+[Q(0)]*(order-1)
        f2=[Q(r-1-2*m),Q(-2)]+[Q(0)]*(order-1)
        inv=[Q(3)**k/Q(r)/Q(r-Q(p,2))**(k+1) for k in range(order+1)]
        arr[r]=mul(mul(mul(arr[r-1],f1),f2),inv)
    return arr

def moments(p,m,u):
    M=2*m; out={}
    for a in range(4):
        for b in range(4):
            for n in range(1-M,M):
                row=[]
                for s in range(2):
                    row.append(sum((Q(j**s)*u[j][a]*u[p-(j+n)][b]
                                    for j in range(1,M+1) if 1<=j+n<=M),Q(0)))
                out[a,b,n]=row
    def get(a,b,n,s=0):
        return out.get((a,b,n),[Q(0),Q(0)])[s] if a>=0 and b>=0 else Q(0)
    return get

def sources(m,p,u,G,n,a,b):
    U=lambda r,k: u[r][k] if 0<=r<p and 0<=k<4 else Q(0)
    J=3*G(a-1,b,n,1)-3*G(a-1,b,n+1,1)+4*m*G(a-1,b,n+1)+2*G(a-2,b,n+1)
    J-=3*((p-n)*G(a,b-1,n)-G(a,b-1,n,1))
    J+=(14*m-3*n)*G(a,b-1,n+1)-3*G(a,b-1,n+1,1)-2*G(a,b-2,n+1)
    if n>=0:
        E=(2*m*m*(a==0)+4*m*(a==1)+2*(a==2))*U(p-n-1,b)
        E+=U(2*m-n,a)*(-6*m*m*U(4*m,b)+8*m*U(4*m,b-1)-2*U(4*m,b-2))
    else:
        E=U(-n,a)*(20*m*m*U(p-1,b)-14*m*U(p-1,b-1)+2*U(p-1,b-2))
        E+=U(p-(2*m+n+1),b)*(2*m*U(2*m,a-1)-2*U(2*m,a-2))
    return J,E

def modulo(q,p):
    assert q.denominator%p,('non-p-unit denominator',q,p)
    return q.numerator*pow(q.denominator,-1,p)%p

def prod(xs):
    z=Q(1)
    for x in xs:z*=x
    return z

def is_prime(p):
    return p>1 and all(p%d for d in range(2,isqrt(p)+1))

def test(m):
    p,u=jets(m);G=moments(p,m,u); lo=1-2*m; hi=2*m
    if m<=5:
        assert direct_product_jets(m)==u,('independent jet generator differs',m)
    assertion_count=0
    outputs=[]
    for a,b in CHANNELS:
        S={n:sum(sources(m,p,u,G,n,a,b)) for n in range(lo,hi)}
        Y=lambda n:G(a,b,n,1)-Q(p-n,2)*G(a,b,n)
        for n in range(lo,hi):
            assert (p-2*n)*Y(n)-(p-2*n-1)*Y(n+1)==S[n],(m,a,b,n)
            assertion_count+=1
        rec=Y(lo)
        for n in range(lo,hi):
            rec=(Q(p-2*n)*rec-S[n])/Q(p-2*n-1)
            assert rec==Y(n+1),(m,a,b,n,'iterate')
            assertion_count+=1
        assert rec==0
        assertion_count+=1
        rho=lambda n:Q(p-2*n,p-2*n-1)
        sigma=lambda n:Q(1,p-2*n-1)
        coeff=lambda h: sigma(h)*prod(rho(k) for k in range(h+1,hi))
        P=prod(rho(k) for k in range(lo,hi))
        left=P*Y(lo)-sum((coeff(h)*S[h] for h in range(lo,0)),Q(0))
        pos=sum((coeff(h)*S[h] for h in range(0,hi)),Q(0))
        assert left==pos,(m,a,b,'global flux',left,pos)
        assertion_count+=1
        if is_prime(p):
            assert modulo(pos,p)==0,(m,a,b,'mod p Ward',modulo(pos,p))
            assertion_count+=1
            H=sum((S[h]*Q(1,2*h+1)*prod(Q(2*k,2*k+1)
                 for k in range(h+1,hi)) for h in range(0,hi)),Q(0))
            assert modulo(H,p)==0,(m,a,b,'finite hypergeometric Ward')
            assertion_count+=1
            S0=S[0];y0=Y(0);y1=Y(1)
            assert modulo(y1-S0-p*(S0-y0),p*p)==0,(m,a,b,'one digit')
            assertion_count+=1
            outputs.append((a,b,modulo(y0,p*p),modulo(S0,p*p),
                            modulo(y1,p*p),modulo(pos/p,p)))
    return p,assertion_count,outputs

if __name__=='__main__':
    total=0
    for m in range(1,13):
        p,n,out=test(m);total+=n
        print('m=',m,'p=',p,'prime=',is_prime(p),'PASS=',n,'sample=',out)
    print('ALL PASS assertions=',total)
