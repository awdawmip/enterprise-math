#!/usr/bin/env python3
"""Author-side exact-rational verification for D25 finite Clausen two-port cubic carrier; not native H0/B0."""
from fractions import Fraction as Q
from math import comb

def add(a,b,N):
    c=[Q(0) for _ in range(N+1)]
    for i in range(min(len(a),N+1)): c[i]+=a[i]
    for i in range(min(len(b),N+1)): c[i]+=b[i]
    return c

def mul(a,b,N):
    c=[Q(0) for _ in range(N+1)]
    for i,x in enumerate(a[:N+1]):
        for j,y in enumerate(b[:N+1-i]): c[i+j]+=x*y
    return c

def pow_series(a,k,N):
    out=[Q(1)]
    for _ in range(k): out=mul(out,a,N)
    return out+[Q(0)]*(N+1-len(out))

def scalar(a,t): return [t*x for x in a]

def inv_series(a,N):
    assert a[0]!=0
    b=[1/a[0]]
    for n in range(1,N+1):
        b.append(-sum(a[k]*b[n-k] for k in range(1,min(n,len(a)-1)+1))/a[0])
    return b

def source_direct(e,m):
    A=sum((Q(comb(m,k)*comb(2*m+e,k),2**k) for k in range(m+1)),Q(0))
    Kx=sum((Q(k*comb(m,k)*comb(2*m+e,k),2**(k-1)) for k in range(1,m+1)),Q(0))
    return A,(1-6*e)*A+6*Kx

def algebraic_series(e,N):
    # s=z*(1/2+2s+5/2 s^2+s^3), recursively over Q.
    s=[Q(0) for _ in range(N+1)]
    for n in range(1,N+1):
        sq=mul(s[:n],s[:n],n-1)
        cub=mul(sq,s[:n],n-1)
        s[n]=(Q(1,2) if n==1 else 0)+2*s[n-1]+Q(5,2)*sq[n-1]+cub[n-1]
    one=[Q(1)]+[Q(0)]*N
    oneplus=add(one,s,N)
    two=add(one,scalar(s,2),N)
    d=add(add(one,scalar(s,-1),N),scalar(mul(s,s,N),-4),N)
    dinv=inv_series(d,N)
    F=mul(mul(two,pow_series(oneplus,e+1,N),N),dinv,N)
    C=mul(mul(s,mul(two,pow_series(oneplus,e,N),N),N),dinv,N)
    B=[(1-6*e)*F[n]+12*(2*n+e)*C[n] for n in range(N+1)]
    return s,F,B

if __name__=="__main__":
    N=50
    summary={}
    for e in (0,1):
        s,A,B=algebraic_series(e,N)
        for m in range(N+1):
            a,b=source_direct(e,m)
            assert A[m]==a,("A",e,m,A[m],a)
            assert B[m]==b,("B",e,m,B[m],b)
        summary[e]={"m_range":[0,N],"independent_exact_comparisons":2*(N+1),
                    "first_s":[str(x) for x in s[:7]],
                    "first_A":[str(x) for x in A[:7]],
                    "first_B":[str(x) for x in B[:7]]}
    for p in (5,7,11,13,17,19,23,29,157,373):
        m=p//6; e=(p-1-6*m)//4
        assert e in (0,1)
        a,b=source_direct(e,m)
        def mod(v): return (v.numerator*pow(v.denominator,-1,p))%p
        x,y=mod(a),mod(b)
        assert (x*y)%p==0,(p,x,y)
        if p==157: assert (x,y)==(0,80)
        if p==373: assert (x,y)==(0,171)
        print("p={} m={} eps={} A={} B={} chi(-6)={}".format(
              p,m,e,x,y,1 if pow(p-6,(p-1)//2,p)==1 else -1))
    print("EXACT_GF_CARRIER_VERIFIED",summary)
