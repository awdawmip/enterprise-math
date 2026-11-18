#!/usr/bin/env python3
"""R279 exact finite-horizon hierarchy: ring witnesses, Fraction arithmetic."""
from fractions import Fraction as F
import json

def det(A):
    n=len(A)
    B=[r[:] for r in A]
    d=F(1)
    for i in range(n):
        j=next((j for j in range(i,n) if B[j][i]),None)
        if j is None:return F(0)
        if i!=j:B[i],B[j]=B[j],B[i];d=-d
        pivot=B[i][i];d*=pivot
        for j in range(i+1,n):
            t=B[j][i]/pivot
            for l in range(i+1,n):B[j][l]-=t*B[i][l]
            B[j][i]=F(0)
    return d

def star_ring(m,c,mask,weight=F(1,4)):
    W=[[F(0) for _ in range(m)] for _ in range(m)]
    W[1][1]=c
    for i in range(m):
        if mask>>i&1:W[i][(i+1)%m]+=weight
    assert all(sum(row)<1 for row in W)
    A=[[F(i==j)-W[i][j] for j in range(m)] for i in range(m)]
    cofactor=det([row[1:] for row in A[1:]])
    return cofactor/det(A)

def main():
    results=[];comparisons=0
    for m in range(2,9):
        allmask=(1<<m)-1
        for mask in range(1<<m):
            a=star_ring(m,F(0),mask)
            b=star_ring(m,F(1,2),mask)
            if mask!=allmask:assert a==b==1
            else:
                q=F(1,4)**m
                assert a==1/(1-q) and b==1/(1-2*q) and a!=b
            comparisons+=1
        results.append({'m':m,'partial_subsets':(1<<m)-1,'complete_product':str(F(1,4)**m),
                        'joint_response_c0':str(star_ring(m,F(0),allmask)),
                        'joint_response_c_half':str(star_ring(m,F(1,2),allmask))})
    return {'schema':'R279_EXACT_HORIZON_CERTIFICATE_V1','status':'PASS','m_range':[2,8],
            'subset_pairs_checked':comparisons,'models_per_subset':2,'results':results,
            'scope':'Every subset of labeled cycle-edge types; rational weight 1/4; two hidden Port-loop values c=0 and 1/2'}

if __name__=='__main__':print(json.dumps(main(),indent=2))
