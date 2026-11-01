#!/usr/bin/env python3
"""Exact F_(p^2) direct character moments and all high-order zeros, p<=107.
This is a finite check of the proved GH-126 family, not an all-prime proof.
"""
from math import comb, factorial, isqrt

def prime(n):
    return n > 1 and all(n % d for d in range(2, isqrt(n)+1))

for p in range(11, 108):
    if p % 8 != 3 or not prime(p):
        continue
    N=(p-1)//2
    degree=N//2
    inv=[0]*p
    inv[1]=1
    for a in range(2,p):inv[a]=(-(p//a)*inv[p%a])%p
    chi=[0]+[1 if pow(i,N,p)==1 else -1 for i in range(1,p)]
    def add(a,b):return ((a[0]+b[0])%p,(a[1]+b[1])%p)
    def mul(a,b):return ((a[0]*b[0]+2*a[1]*b[1])%p,(a[0]*b[1]+a[1]*b[0])%p)
    B=(pow(8,-1,p),pow(12,-1,p))
    # Only for the independent Hasse-polynomial crosscheck.
    h=[factorial(N)*pow(factorial(u)**2*factorial(N-2*u),-1,p)%p for u in range(degree+1)]
    def evalpoly(coefs,x):
        y=(0,0)
        for a in reversed(coefs):y=add(mul(y,x),(a,0))
        return y
    H=evalpoly(h,B)
    Hp=(H[0],(-H[1])%p)
    # Direct full character sums of y=(x/f) powers for all 1<=r<=N.
    S=[(0,0) for _ in range(N+1)]
    square=[a*a%p for a in range(p)]
    cube=[a*square[a]%p for a in range(p)]
    count=0
    for a in range(p):
        for b in range(p):
            f0=(cube[a]+6*a*square[b]+square[a]+2*square[b]+B[0]*a+2*B[1]*b)%p
            f1=(3*square[a]*b+2*cube[b]+2*a*b+B[0]*b+B[1]*a)%p
            norm=(f0*f0-2*f1*f1)%p
            if not norm:continue
            count+=1
            factor=inv[norm]
            y=((a*f0-2*b*f1)*factor%p,(b*f0-a*f1)*factor%p)
            acc=(1,0)
            for r in range(1,N+1):
                acc=mul(acc,y)
                S[r]=add(S[r],(acc[0]*chi[norm]%p,acc[1]*chi[norm]%p))
    assert count==p*p-3
    coeffs=h[:]
    odd=1
    for r in range(1,N+1):
        coeffs=[(i+1)*coeffs[i+1]%p for i in range(len(coeffs)-1)]
        odd=odd*(2*r-1)%p
        scalar=(-1 if r%2==0 else 1)*pow(2,r,p)*inv[odd]%p
        expect=mul((scalar,0),mul(evalpoly(coeffs,B),Hp))
        assert S[r]==expect,(p,r,S[r],expect)
        if r>degree:assert S[r]==(0,0),(p,r,S[r])
    print(f'p={p} N={N} degree={degree} verified_moments={N} zero_orders={N-degree} S2={S[2]}')
print('PASS_GH126_ALL_HIGHER_MOMENTS_AND_ZERO_BAND_P_LE_107')
