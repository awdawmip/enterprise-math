"""Reproduce counts, three Dirichlet convolutions and outward constants. Python 3.9+, stdlib."""
from collections import Counter
from fractions import Fraction as Q
from functools import lru_cache
from math import comb, gcd, isqrt, prod
import json


@lru_cache(None)
def factor(n):
    out=[]
    p=2
    while p*p<=n:
        k=0
        while n%p==0:
            n//=p
            k+=1
        if k:out.append((p,k))
        p=3 if p==2 else p+2
    if n>1:out.append((n,1))
    return tuple(out)


def phi(n):
    return prod((p-1)*p**(k-1) for p,k in factor(n))


def M(n):
    def local(p,k):
        if p==2:return 2**(k//2) if k<5 else 4*(k-4)
        return 2*k-Q(2,p-1)
    return prod(local(p,k) for p,k in factor(n))


def raw_numerator(a,q):
    # q^2 times 12*s(a,q), directly from the sawtooth definition.
    return 3*sum((2*r-q)*(2*(r*a%q)-q) for r in range(1,q))


def direct(bound=320):
    units=candidates=equal=0
    tables={}
    for q in range(2,bound+1):
        frac,full=Counter(),Counter()
        for a in range(1,q):
            if gcd(a,q)!=1:continue
            v=raw_numerator(a,q)
            assert v%(q*q)==q*((a+pow(a,-1,q))%q)
            frac[v%(q*q)]+=1
            full[v]+=1
        tot=sum(frac.values())
        pairs=sum(z*z for z in frac.values())
        true=sum(z*z for z in full.values())
        assert tot==phi(q) and Q(pairs,tot)==M(q)
        p=isqrt(q)
        if p*p==q and p!=2 and factor(p)==((p,1),):
            assert pairs-true==4*(p-1)
            assert all(Q(raw_numerator(1+p*t,q),q*q)==-2+Q(2,q) for t in range(1,p))
        if q in [2,4,8,9,16,25,49,225,256]:
            tables[str(q)]=[pairs,true,str(M(q))]
        units+=tot;candidates+=pairs;equal+=true
    return {"q_max":bound,"units":units,"fractional_ordered_pairs":candidates,
            "equal_ordered_pairs":equal,"false_positive_ordered_pairs":candidates-equal,
            "sample_q_to_fractional_true_and_mean":tables}


def local_poly(p,variant):
    h=[1,-1,1,-1,2,-2,4] if p==2 else [1,-Q(2,p-1),Q(p+1,p-1)]
    if variant=="H":return h
    if variant=="J":return [z-t for z,t in zip(h+[0,0],[0,0]+h)]
    if variant in ("G","JG"):
        hg=[Q(p-1,p)*v+Q(w,p) for v,w in zip(h,[1,-2,1]+[0]*(len(h)-3))]
        if variant=="G":return hg
        return [z-t for z,t in zip(hg+[0,0],[0,0]+hg)]
    raise ValueError(variant)


def arithmetic_coeff(n,variant):
    z=1
    for p,k in factor(n):
        v=local_poly(p,variant)
        if k>=len(v):return 0
        z*=v[k]
    return z


def conv(x,y):
    N=len(x)-1
    z=[0]*(N+1)
    for d in range(1,N+1):
        if x[d]:
            for j in range(1,N//d+1):z[d*j]+=x[d]*y[j]
    return z


def convolution_check(N=2048):
    tau=[0]+[prod(k+1 for p,k in factor(n)) for n in range(1,N+1)]
    sq=[0]+[int(isqrt(n)**2==n) for n in range(1,N+1)]
    h,j,hg=([0]+[arithmetic_coeff(n,name) for n in range(1,N+1)] for name in ("H","J","G"))
    vals=[0]+[M(n) for n in range(1,N+1)]
    d112=conv(tau,sq)
    assert conv(tau,h)==vals==conv(d112,j) and conv(sq,j)==h
    jg=[0]+[arithmetic_coeff(n,"JG") for n in range(1,N+1)]
    assert conv(tau,hg)==conv(d112,jg)==[0]+[Q(phi(n),n)*vals[n] for n in range(1,N+1)]
    for p in range(2,100):
        if factor(p)!=((p,1),):continue
        z=Q(1,p)
        ev=lambda h:sum(t*z**i for i,t in enumerate(h))
        assert ev(local_poly(p,'H'))==1-z*z
        assert ev(local_poly(p,'G'))==(1-z)**2*(1+2*z)
        # Reduce modulo T^2 - 1/p to check both Euler products at s=1/2.
        def at_root(poly):
            return tuple(sum(c*z**(k//2) for k,c in enumerate(poly) if k%2==i) for i in [0,1])
        assert at_root(local_poly(p,'J'))==(1+z*z,-2*z)
        assert at_root(local_poly(p,'JG'))==((1-z)*(1+z+2*z*z),-4*z*(1-z))
    # Independently count the 1,1,2 hyperbola split at both integer and noninteger X/K^2.
    prefix=[0]
    for d in tau[1:]:prefix.append(prefix[-1]+d)
    for X in [1,2,7,63,127,128,511,1000,N]:
        for K in {1,isqrt(X),max(1,isqrt(isqrt(X)))}:
            Y=X//(K*K)
            lhs=sum(d112[:X+1])
            rhs=sum(prefix[X//(c*c)] for c in range(1,K+1))
            rhs+=sum(tau[n]*(isqrt(X//n)-K) for n in range(1,Y+1))
            assert lhs==rhs
    return {"identities_checked_through":N,"exact_fiber_mean_at_625":str(vals[625]),
            "two_uniformity_protocols_at_10":[str(sum(vals[1:11])/10),
            str(Q(sum(phi(n)*vals[n] for n in range(1,11)),sum(phi(n) for n in range(1,11))))]}


SCALE=10**18


def floorq(x):return Q((SCALE*x)//1,SCALE)
def ceilq(x):return -floorq(-x)


def bounds_sqrt(q):
    z=Q(q);n=isqrt((z.numerator*SCALE*SCALE)//z.denominator)
    return Q(n,SCALE),Q(n+1,SCALE)


def zeta_half_square():
    # Euler transform of the alternating eta series: differences are in [0,1]
    # by the Laplace representation of (j+1)^(-1/2).
    limit=40
    intervals=[bounds_sqrt(Q(1,j+1)) for j in range(limit+1)]
    lo=hi=Q(0)
    for j in range(limit+1):
        for i in range(j+1):
            c=Q((-1)**i*comb(j,i),2**(j+1))
            a,b=intervals[i]
            lo+=c*(a if c>0 else b)
            hi+=c*(b if c>0 else a)
    hi+=Q(1,2**(limit+1))
    a,b=bounds_sqrt(2)
    return (lo/(b-1))**2,(hi/(a-1))**2


def constants(H=10000):
    # Positive factors. The tail sums are dominated by sums over all integers.
    A_lo=A_hi=B_lo=B_hi=J_lo=J_hi=Q(1)
    primes=0
    for p in range(2,H+1):
        if factor(p)!=((p,1),):continue
        primes+=1
        a=1-Q(1,p*p); b=1-Q(2,p*(p+1))
        A_lo=floorq(A_lo*a);A_hi=ceilq(A_hi*a)
        B_lo=floorq(B_lo*b);B_hi=ceilq(B_hi*b)
        pl,pu=bounds_sqrt(Q(1,p))
        J_lo=floorq(J_lo*(1+Q(1,p*p)-2*pu/p))
        J_hi=ceilq(J_hi*(1+Q(1,p*p)-2*pl/p))
    A_lo*=1-Q(1,H); B_lo*=1-Q(2,H+1)
    J_lo*=1-Q(4,isqrt(H))
    zlo,zhi=zeta_half_square()
    def pack(a,b):
        den=10**9
        return [str(Q((a*den)//1,den)),str(Q(-((-b*den)//1),den))]
    assert 0<B_lo<B_hi<A_lo<A_hi<1 and 0<J_lo<J_hi
    return {"prime_cutoff":H,"prime_count":primes,"equal_moduli_leading":pack(A_lo,A_hi),
            "equal_unit_pairs_leading":pack(B_lo,B_hi),
            "zeta_half_squared":pack(zlo,zhi),"sqrt_X_coefficient":pack(J_lo*zlo,J_hi*zhi)}


if __name__=="__main__":
    print(json.dumps({"sawtooth":direct(),"arithmetic":convolution_check(),"enclosures":constants()},indent=2))
