#!/usr/bin/env python3
"""Exact-rational interval certificates for EC49FUV n=30 full atlas, new early windows and gap bridges.
No external deps. All decisions use Fraction comparisons; no floating-point proofs.
"""
from fractions import Fraction as Q
from math import comb

N = 30
E = Q(31597745,1653649)
BETA = Q(3,637)
A = Q(21829245984)
B = Q(45529434409)
C = Q(456083905)
U = {z:A/(B-C*z) for z in [Q(0),E]}
S = Q(10)**12
INTERVALS = {
    1:(Q(5,10**8),Q(2,10**7)),
    2:(Q(20,100000),Q(31,100000)),
    3:(Q(32,10000),Q(42,10000)),
    4:(Q(129,10000),Q(153,10000)),
    5:(Q(302,10000),Q(342,10000)),
    6:(Q(538,10000),Q(593,10000)),
    7:(Q(824,10000),Q(890,10000)),
    8:(Q(1146,10000),Q(1219,10000)),
}

class Iv:
    def __init__(self,lo,hi=None):
        self.lo=Q(lo)
        self.hi=Q(lo) if hi is None else Q(hi)
        assert self.lo<=self.hi
    def __add__(self,other):
        other=other if isinstance(other,Iv) else Iv(other)
        return Iv(self.lo+other.lo,self.hi+other.hi)
    __radd__=__add__
    def __neg__(self):return Iv(-self.hi,-self.lo)
    def __sub__(self,other):return self+-_iv(other)
    def __rsub__(self,other):return _iv(other)+-self
    def __mul__(self,other):
        other=_iv(other)
        P=[self.lo*other.lo,self.lo*other.hi,self.hi*other.lo,self.hi*other.hi]
        return Iv(min(P),max(P))
    __rmul__=__mul__
    def __pow__(self,k):
        assert isinstance(k,int) and k>=0
        if k==0:return Iv(1)
        if self.lo>=0:return Iv(self.lo**k,self.hi**k)
        if self.hi<=0 and k%2:return Iv(self.lo**k,self.hi**k)
        if self.hi<=0:return Iv(self.hi**k,self.lo**k)
        if k%2:return Iv(self.lo**k,self.hi**k)
        return Iv(0,max(self.lo**k,self.hi**k))
    def neg(self):return self.hi<0
    def pos(self):return self.lo>0

def _iv(a):return a if isinstance(a,Iv) else Iv(a)

def prob(x,theta):
    T=(1-x)*(1-BETA*x+BETA*x*theta)
    return 1-T,1-U[theta]*T

def prob_prime(x,theta):
    Tp=-(1-BETA*x+BETA*x*theta)+(1-x)*BETA*(theta-1)
    return -Tp,-U[theta]*Tp

def delta(j,x,theta):
    p,q=prob(x,theta)
    return comb(N,j)*(q**j*(1-q)**(N-j)-p**j*(1-p)**(N-j))

def dprime(j,x,theta):
    p,q=prob(x,theta)
    pp,qp=prob_prime(x,theta)
    return N*comb(N-1,j-1)*(q**(j-1)*(1-q)**(N-j)*qp-p**(j-1)*(1-p)**(N-j)*pp)

def gprime(j,x):return dprime(j,x,E)-dprime(j,x,Q(0))

def lower_cdf(j,t):
    return sum(comb(N,k)*t**k*(1-t)**(N-k) for k in range(j))

def advantage(j,x,theta):
    p,q=prob(x,theta)
    return lower_cdf(j,p)-lower_cdf(j,q)

def G(j,x):return advantage(j,x,E)-advantage(j,x,Q(0))

def partition_check(func,a,b,pred,slabs=512):
    leaves=0
    def inspect(lo,hi,depth):
        nonlocal leaves
        val=func(Iv(lo,hi))
        if pred(val):
            leaves+=1
            return
        if depth>=25:
            raise AssertionError(f'cannot bound sign in [{float(lo)}, {float(hi)}] on {func.__name__}: bounds {float(val.lo):.12g},{float(val.hi):.12g}')
        mid=(lo+hi)/2
        inspect(lo,mid,depth+1)
        inspect(mid,hi,depth+1)
    for i in range(slabs):
        inspect(a+(b-a)*Q(i,slabs),a+(b-a)*Q(i+1,slabs),0)
    return leaves

def bracket_monotone_zero(fun,a,b,sign_lo,sign_hi,places=12):
    assert (fun(a)<0 if sign_lo=='-' else fun(a)>0)
    assert (fun(b)<0 if sign_hi=='-' else fun(b)>0)
    left,right=a,b
    # Exact bisection until width <10^-12
    while right-left>Q(1,10**(places+2)):
        mid=(left+right)/2
        if (fun(mid)<0)==(sign_lo=='-'):left=mid
        else:right=mid
    ilo=left*S;ihi=right*S
    L=ilo.numerator//ilo.denominator
    H=ihi.numerator//ihi.denominator+1
    if (fun(Q(L,S))<0)==(sign_lo=='-') and (fun(Q(H,S))<0)==(sign_hi=='-'):
        return L,H
    # Fall back to wider integer bracket when bisection crosses integer boundary
    L-=1;H+=1
    assert (fun(Q(L,S))<0)==(sign_lo=='-')
    assert (fun(Q(H,S))<0)==(sign_hi=='-')
    return L,H

# Compact exact polynomial arithmetic for nonlocal bridge signs. A single
# degree-59 Bernstein certificate avoids inflated natural intervals on gaps.
def poly_add(a,b):
    c=[Q(0)]*max(len(a),len(b))
    for i,v in enumerate(a):c[i]+=v
    for i,v in enumerate(b):c[i]+=v
    return c

def poly_neg(a):return [-v for v in a]

def poly_mul(a,b):
    c=[Q(0)]*(len(a)+len(b)-1)
    for i,v in enumerate(a):
        for j,w in enumerate(b):c[i+j]+=v*w
    return c

def poly_pow(a,n):
    r=[Q(1)]
    while n:
        if n&1:r=poly_mul(r,a)
        n//=2
        if n:a=poly_mul(a,a)
    return r

def poly_derivative(a):return [Q(i)*a[i] for i in range(1,len(a))]

def polypq(theta):
    u=U[theta]
    d=BETA*(theta-1)
    T=[Q(1),d-1,-d]
    return poly_add([Q(1)],poly_neg(T)),poly_add([Q(1)],poly_neg([u*t for t in T]))

def poly_tail_prime(j,theta):
    p,q=polypq(theta)
    onep=poly_add([Q(1)],poly_neg(p))
    oneq=poly_add([Q(1)],poly_neg(q))
    pos=poly_mul(poly_mul(poly_pow(q,j-1),poly_pow(oneq,N-j)),poly_derivative(q))
    neg=poly_mul(poly_mul(poly_pow(p,j-1),poly_pow(onep,N-j)),poly_derivative(p))
    return [v*N*comb(N-1,j-1) for v in poly_add(pos,poly_neg(neg))]

def poly_gprime(j):return poly_add(poly_tail_prime(j,E),poly_neg(poly_tail_prime(j,Q(0))))

def bernstein_coeffs(poly,a,b):
    d=len(poly)-1
    shifted=[(b-a)**i*sum((poly[k]*comb(k,i)*a**(k-i)
                for k in range(i,d+1)),Q(0)) for i in range(d+1)]
    return [sum((shifted[i]*Q(comb(j,i),comb(d,i))
                for i in range(j+1)),Q(0)) for j in range(d+1)]

def certify_monotone_gap(j,a,b):
    assert a<b
    coef=bernstein_coeffs(poly_gprime(j),a,b)
    assert len(coef)==60 and all(v>0 for v in coef), (j,min(coef))
    assert G(j,b)<0
    return len(coef)

def main():
    full=0
    rootints={}
    for j,(l,r) in INTERVALS.items():
        checks=[
          (f'E({j-1})<0',lambda x,j=j:delta(j-1,x,E),Iv.neg),
          (f'Z({j-1})<0',lambda x,j=j:delta(j-1,x,Q(0)),Iv.neg),
          (f'Z({j})<0',lambda x,j=j:delta(j,x,Q(0)),Iv.neg),
          (f'E({j+1})>0',lambda x,j=j:delta(j+1,x,E),Iv.pos),
          (f'mix1/3({j})<0',lambda x,j=j:(delta(j,x,Q(0))*2+delta(j,x,E))*Q(1,3),Iv.neg),
          (f'mix1/3({j+1})>0',lambda x,j=j:(delta(j+1,x,Q(0))*2+delta(j+1,x,E))*Q(1,3),Iv.pos),
          (f'Gprime({j})>0',lambda x,j=j:gprime(j,x),Iv.pos),
          (f'Gprime({j+1})>0',lambda x,j=j:gprime(j+1,x),Iv.pos)
        ]
        for name,fun,pred in checks:
            try:full+=partition_check(fun,l,r,pred)
            except Exception as exc:raise AssertionError(f'{j} {name} {exc}') from exc
        assert G(j,l)<0<G(j,r)
        assert delta(j,l,E)>0>delta(j,r,E)
        assert G(j+1,r)<0
        e=bracket_monotone_zero(lambda x:G(j,x),l,r,'-','+')
        c=bracket_monotone_zero(lambda x:delta(j,x,E),l,r,'+','-')
        assert e[1]<c[0], (j,e,c)
        rootints[j]=(e,c)
        print(f'j={j} entry=({e[0]},{e[1]})/10^12 exit=({c[0]},{c[1]})/10^12 8*512 rational slab checks PASS')
    for j in range(1,9):
        lo=INTERVALS[j][1]
        hi=INTERVALS[j+1][0] if j<8 else Q(749,5000)
        assert lo<hi
        full+=certify_monotone_gap(j+1,lo,hi)
        # E-Bayes threshold K>=j+1 is valid on gap by the unique count-crossings
        assert delta(j,lo,E)<0 and delta(j+1,hi,E)>0
        print(f'pure-E bridge j={j+1} [{lo},{hi}] monotone G and negative right-end PASS')
    # Explicit pure-E initial interval, where the compactified zero-endpoint
    # count-1 mass briefly has the opposite sign; E is still least favorable.
    lower=INTERVALS[1][0]
    full+=certify_monotone_gap(1,Q(0),lower)
    assert delta(1,lower,E)>0
    # Previously proven windows j=9..16 have disjoint local neighborhoods.
    # These certificates fill every intervening open gap with pure E.
    prior={9:(Q(749,5000),Q(79,500)),10:(Q(93,500),Q(49,250)),
      11:(Q(224,1000),Q(235,1000)),12:(Q(264,1000),Q(273,1000)),
      13:(Q(305,1000),Q(314,1000)),14:(Q(346,1000),Q(354,1000)),
      15:(Q(388,1000),Q(394,1000)),16:(Q(431,1000),Q(435,1000))}
    for j in range(9,16):
        lo=prior[j][1];hi=prior[j+1][0]
        full+=certify_monotone_gap(j+1,lo,hi)
        assert delta(j,lo,E)<0 and delta(j+1,hi,E)>0
        print(f'parent-window pure-E bridge j={j+1} [{lo},{hi}] PASS')
    # Independent finite dual crosschecks (strictly supplementary to real-interval proofs).
    representative=[Q(0),Q(8,10**8),Q(1,10**7),Q(1,4000),
      Q(36,10000),Q(14,1000),Q(32,1000),Q(57,1000),
      Q(85,1000),Q(118,1000),Q(125,1000),Q(16,100),
      Q(19,100),Q(24,100),Q(40,100),Q(46,100),Q(9,10),Q(1)]
    for x in representative:
        z=[delta(k,x,Q(0)) for k in range(N+1)]
        e=[delta(k,x,E) for k in range(N+1)]
        d=[e[k]-z[k] for k in range(N+1)]
        cand=[Q(0),Q(1)]
        cand += [-z[k]/d[k] for k in range(N+1)
                 if d[k] and Q(0)<-z[k]/d[k]<Q(1)]
        best=min(sum(max(Q(0),z[k]+l*d[k]) for k in range(N+1)) for l in cand)
        assert Q(0)<=best<=Q(1)
        active=[-z[j]/d[j] for j in range(1,N+1)
                if z[j]<0<e[j] and G(j,x)>0>G(j+1,x)]
        assert len(active)<=1, (x,active)
        claimed_lambda=active[0] if active else Q(1)
        claimed=sum(max(Q(0),z[k]+claimed_lambda*d[k]) for k in range(N+1))
        assert claimed==best, (x,'dual mismatch',float(claimed-best))
    print(f'ALL PASS: {full} exact rational interval/Bernstein sign inequalities, 16 root brackets, 8 new full windows, 15 pure-E bridges plus initial, 18 exact dual crosschecks.')

if __name__=='__main__': main()
