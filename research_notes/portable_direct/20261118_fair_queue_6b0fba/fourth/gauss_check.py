"""Exact checks in Z[omega][Z/p]/(1+X+...+X^(p-1)); Python 3.9+."""
from collections import Counter
from math import isqrt
import argparse

ROOTS=((1,0),(0,1),(-1,-1))
def prime(p):
    return p>=2 and all(p%d for d in range(2,isqrt(p)+1))

def primary_pair(p):
    # Norm=(a-b/2)^2+3b^2/4, so 0<b<=sqrt(4p/3).
    candidates=[]
    for b in range(3,isqrt(4*p//3)+1,3):
        delta=4*p-3*b*b
        r=isqrt(delta)
        if r*r!=delta:continue
        for k in (b+r,b-r):
            if k%2==0 and k//2%3==1:candidates.append((k//2,b))
    assert len(candidates)==1,(p,candidates)
    a,b=candidates[0]
    return (a,b),(a-b,-b)

def reduction(pair,p):
    a,b=pair
    u=-a*pow(b,-1,p)%p      # omega in O/(pi)
    t=(2*a-b)%p            # abs rational representatives: Tr(x/pi)=T*x/p
    assert (u*u+u+1)%p==0 and pow(t,(p-1)//3,p)==1
    return u,t

def add(acc,i,val):
    acc[i][0]+=val[0]
    acc[i][1]+=val[1]

def canonical(poly):
    # A degree <=p-1 multiple of Phi_p has a constant coefficient vector.
    # For p!=3 the minimal polynomial over Q(omega) is still Phi_p.
    a,b=poly[-1]
    return tuple((u-a,v-b) for u,v in poly[:-1])

def split_check(p,carry):
    pair=primary_pair(p)
    u,t=reduction(pair[0],p)
    v,other_t=reduction(pair[1],p)
    assert (u*v)%p==1 and t==other_t
    table={pow(u,i,p):ROOTS[i] for i in range(3)}
    other={pow(v,i,p):ROOTS[i] for i in range(3)}
    symbols=[(0,0)]+[table[pow(x,(p-1)//3,p)] for x in range(1,p)]
    conjugate=[(0,0)]+[other[pow(x,(p-1)//3,p)] for x in range(1,p)]
    assert all((a-b,-b)==w for (a,b),w in zip(symbols,conjugate))
    # Gauss side retains the trace coefficient and both original generators.
    hs=sorted({0,1,2,-1,6,30,105,p,-p})
    for h in hs:
        gauss=[[0,0] for _ in range(p)]
        kubic=[[0,0] for _ in range(p)]
        for x in range(p):
            k=h*t*x%p
            add(gauss,k,symbols[x]);add(gauss,k,conjugate[x])
            kubic[h*pow(x,3,p)%p][0]+=1
        if h%p==0:kubic[0][0]-=p
        assert canonical(gauss)==canonical(kubic),(p,h)
    if carry is not None:
        carry.append((p,*pair[0],*pair[1],u,v,t))
    return len(hs)

def multiply(x,y,q):
    a,b=x;c,d=y
    return ((a*c-b*d)%q,(a*d+b*c-b*d)%q)

def exponent(x,k,q):
    out=(1,0)
    while k:
        if k&1:out=multiply(out,x,q)
        x=multiply(x,x,q);k//=2
    return out

def inert_check(q):
    embedding={(a%q,b%q):(a,b) for a,b in ROOTS}
    # Store the source symbol histogram at each trace, before evaluation.
    trace=[[0,0] for _ in range(q)]
    for a in range(q):
        for b in range(q):
            if (a,b)==(0,0):continue
            residue=exponent((a,b),(q*q-1)//3,q)
            add(trace,(2*a-b)%q,embedding[residue])
    assert trace==[[q-1,0]]+[[-1,0] for _ in range(q-1)]
    hs=sorted({0,1,2,-1,6,30,105,q,-q})
    for h in hs:
        gauss=[[0,0] for _ in range(q)]
        rational=[[0,0] for _ in range(q)]
        for k,weight in enumerate(trace):add(gauss,(-h*k)%q,weight)
        gauss[0][0]-=q*int(h%q!=0)
        for x in range(q):rational[h*pow(x,3,q)%q][0]+=1
        rational[0][0]-=q*int(h%q==0)
        assert not any(any(x) for x in canonical(gauss))
        assert not any(any(x) for x in canonical(rational))
    return len(hs)

def main():
    args=argparse.ArgumentParser(description=__doc__)
    args.add_argument("--pairs",action="store_true",help="print all split primary representatives and reduction data")
    opts=args.parse_args()
    rows=[];split_tests=inert_tests=0;inerts=[]
    for p in range(2,258):
        if not prime(p):continue
        if p%3==1:split_tests+=split_check(p,rows)
        if p%3==2 and p<=103:
            inert_tests+=inert_check(p);inerts.append(p)
    for h in (0,1,2,3,30):
        counts=Counter(h*pow(x,3,3)%3 for x in range(3))
        assert counts==(Counter({0:3}) if h%3==0 else Counter(range(3)))
    print("split primes / prime-frequency checks",len(rows),split_tests)
    print("inert primes / prime-frequency checks",len(inerts),inert_tests)
    print("ramified prime-frequency checks",5)
    print("p, a, b, conjugate_a, conjugate_b, omega_mod_pi, omega_mod_conjugate, trace_mod_p")
    for row in rows if opts.pairs else rows[:6]:print(*row,sep=",")
    for X in (3,4,24,25,120,121,10000):
        counts=[sum(1 for p in range(2,isqrt(X)+1) if prime(p) and p%3==2 and h%p)
                for h in (1,30,0)]
        print("cutoff / inert correction for h=1,30,0",X,counts)
if __name__=="__main__":
    main()
