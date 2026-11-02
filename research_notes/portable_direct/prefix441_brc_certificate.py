#!/usr/bin/env python3
"""PREFIX-441 exact X6/BRC moment-fiber certificate; run from repo root with PYTHONPATH=."""
from itertools import combinations_with_replacement
from fractions import Fraction
from math import comb
from experiments.x6_signed_native_spatial_v16_20260905 import signed_brc as brc

def moments(K,n,upto=3):
    return tuple(sum((n-2*k)**j for k in K) for j in range(upto+1)
def feasible(K,n):
    return all(K.count(k)<=comb(n,k) for k in set(K))
def det(a):
    a=[[Fraction(v) for v in row] for row in a]; result=Fraction(1)
    for j in range(len(a)):
        i=next((i for i in range(j,len(a)) if a[i][j]),None)
        if i is None: return 0
        if i!=j: a[i],a[j]=a[j],a[i]; result=-result
        p=a[j][j]; result*=p
        for i in range(j+1,len(a)):
            ratio=a[i][j]/p
            for k in range(j+1,len(a)):a[i][k]-=ratio*a[j][k]
            a[i][j]=0
    return result

def main():
    for n in range(4):
        for mass in range(1,4):
            seen={}
            for K in combinations_with_replacement(range(n+1),mass):
                if not feasible(K,n):continue
                sig=moments(K,n,2)
                assert sig not in seen or seen[sig]==K,(n,mass,K)
                seen[sig]=K
    print('PASS small-fiber exhaustive: n<=3, mass<=3')
    A3=(0,2,2,2);B3=(1,1,1,3)
    assert feasible(A3,3) and feasible(B3,3)
    assert moments(A3,3,2)==moments(B3,3,2)==(4,0,12)
    assert moments(A3,3)[3]-moments(B3,3)[3]==48
    print('PASS n=3 sharp mass=4, M3 gap=48')
    A=(0,3,3);B=(1,1,4)
    for n in range(4,65):
        assert feasible(A,n) and feasible(B,n)
        assert moments(A,n,2)==moments(B,n,2)
        assert moments(A,n)[3]-moments(B,n)[3]==96
        assert sum(k%2==0 for k in A)==sum(k%2==0 for k in B)==1
        for k in (0,1,3,4):
            x=(n-2*k,0,0,0,0,0)
            assert brc.endpoint_multiplicity(n,x)>=comb(n,k)
    print('PASS n=4..64 BRC endpoint capacities; 3-path fiber and history-parity marginal')
    for n in range(4,17):
        seen={}
        for K in combinations_with_replacement(range(n+1),2):
            if not feasible(K,n):continue
            sig=moments(K,n,2)
            assert sig not in seen or seen[sig]==K
            seen[sig]=K
    print('PASS n=4..16 exhaustive mass=2 uniqueness')
    xs=(4,2,0,-2,-4)
    D=[[x**j for x in xs] for j in range(4)]+[[int(k%2==0) for k in range(5)]]
    assert det(D)==6144
    C=(0,2,2,2,2,2,2,4);E=(1,1,1,1,3,3,3,3)
    assert feasible(C,4) and feasible(E,4)
    assert moments(C,4)==moments(E,4)
    assert sum(k%2==0 for k in C)==8 and sum(k%2==0 for k in E)==0
    print('PASS n=4 complete readout det=6144 and complementary parity witness')
    W=((-2,Fraction(2,3)),(1,Fraction(3,5)),(0,Fraction(7,11)))
    total=sum((w for _,w in W),Fraction())
    for n in (4,5,8,12):
        for j in range(4):
            v=sum((w*sum((n-2*k+d)**j for k in A) for d,w in W),Fraction())
            u=sum((w*sum((n-2*k+d)**j for k in B) for d,w in W),Fraction())
            assert v-u==(96*total if j==3 else 0)
    print('PASS common positive-rational BRC translation kernel, 4 sampled horizons')
    print('BRC source: experiments/x6_signed_native_spatial_v16_20260905/signed_brc.py; frozen f42f2906d77f24085c123f3ccfe9667d41caa96d')
    print('Mathematical scope: unit-weight signed X6 word bags, affine translation futures; author-side exact checker')

if __name__=='__main__':main()
