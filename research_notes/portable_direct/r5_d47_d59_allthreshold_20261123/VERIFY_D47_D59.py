#!/usr/bin/env python3
"""Exact finite-field witnesses for frozen R5 (not a characteristic-zero zero proof)."""
from itertools import permutations, combinations

SUPPORTS = (set(range(214, 219)), {214,216,217,218,219,220,221},
            {215,216,217,218,219,220,221})
CASES = ((47,283,163),(47,659,568),(59,827,671),(59,1063,572))

def calculate(d, prime, z, count):
    assert pow(z,d,prime)==1 and z%prime!=1
    assert all(prime % k for k in range(2,int(prime**0.5)+1))
    def root(k): return pow(z,k%d,prime)
    def inverse(x): return pow(x%prime,prime-2,prime)
    def product(values):
        out=1
        for x in values: out=out*x%prime
        return out
    def series(factors):
        out=[0]*(count+1)
        out[0]=1
        for v,k in factors:
            for n in range(k,count+1):
                out[n]=(out[n]+v*out[n-k])%prime
        return out
    def threshold(seq):
        out=[0]*(count+1)
        run=0
        for n in range(1,count+1):
            run=(run+seq[n-1])%prime
            out[n]=run
        return out
    alpha,beta=root(214),root(215)
    gammas=[root(k) for k in (219,220,221)]
    K=product((1-root(p)) for p in range(214,222))
    coeffs=[0]*(count+1)
    for j,gamma in enumerate(gammas):
        kappa=gamma*gamma%prime
        for k,other in enumerate(gammas):
            if k!=j: kappa=kappa*inverse(gamma-other)%prime
        weights=(alpha,beta,gamma)
        for order in permutations(range(3)):
            u1,u2,u3=(weights[k] for k in order)
            e1,e2=int(order[0]>order[1]),int(order[1]>order[2])
            factor=(kappa*pow(u1,e1,prime)*
                    pow(u1*u2%prime,e2,prime)*inverse(1-u1))%prime
            seq=series([(root(k),1) for k in (216,217,218)]+
                       [(u1*u2%prime,1),(u1*u2*u3%prime,2)])
            for n in range(e2,count+1):
                coeffs[n]=(coeffs[n]+factor*seq[n-e2])%prime
    A=[K*x%prime for x in threshold(coeffs)]
    def singleton(prices):
        prod=product(1-root(k) for k in prices)
        if prod==0: return [0]*(count+1)
        return [prod*x%prime for x in
                threshold(series([(root(k),1) for k in prices]))]
    B,C=singleton(range(223,291)),singleton(range(296,313))
    R=[(a+b+c-a*b-a*c-b*c+a*b*c)%prime for a,b,c in zip(A,B,C)]
    direct=0
    for k in (1,2,3):
        for subset in combinations(range(3),k):
            support=set().union(*(SUPPORTS[i] for i in subset))
            direct+=(-1)**(k+1)*product(1-root(price) for price in support)
    assert A[1]==direct%prime
    assert C[1]==product(1-root(price) for price in range(296,313))
    assert B==[0]*(count+1)
    return A,C,R

def main():
    for d,p,z in CASES:
        T=2*d
        A,C,R=calculate(d,p,z,2*T)
        predicted={T-4,T-3,T-2,T-1,T}
        zeros={r for r in range(1,T+1) if R[r]==0}
        assert zeros==predicted,(d,p,zeros)
        assert all(A[m]==A[m+T] and R[m]==R[m+T] for m in range(1,T+1))
        assert all(C[m]==C[m+d] for m in range(1,3*d+1))
        print(f'd={d} prime={p} root={z}: zeros={sorted(zeros)}; '
              f'nonzeros={T-len(zeros)}/{T-len(predicted)}; '
              f'period={T}; R_1={R[1]}; R_{T+1}={R[T+1]}')
    print('ALL EXACT FINITE-FIELD WITNESS CHECKS PASS')

if __name__=='__main__': main()
