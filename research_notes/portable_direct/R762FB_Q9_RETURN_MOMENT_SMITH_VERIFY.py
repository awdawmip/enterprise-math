#!/usr/bin/env python3
"""Exact positive six-branch BRC return-moment / 3-adic Smith computation.
No numpy, floating point, native signed force cancellation, or classical comparison.
"""
import json
from collections import Counter

BRANCHES = ((0,0,0),(1,0,0),(0,0,1),(1,1,0),(0,1,1),(1,1,1))
PRIMES = (1000003, 1000033)

def brc_returns(q, last_n):
    q3=q*q*q
    positions=[(i//(q*q),(i//q)%q,i%q) for i in range(q3)]
    source_indices=[[
        (((x-dx)%q)*q+(y-dy)%q)*q+(z-dz)%q
        for x,y,z in positions] for dx,dy,dz in BRANCHES]
    state=[0]*q3; state[0]=1
    moments=[1]
    for _ in range(last_n):
        state=[sum(state[indices[i]] for indices in source_indices)
               for i in range(q3)]
        moments.append(state[0])
    return moments

def determinant_mod_prime(moments, r, p):
    a=[[moments[i+j]%p for j in range(r)] for i in range(r)]
    determinant=1
    for j in range(r):
        row=next((i for i in range(j,r) if a[i][j]),None)
        if row is None: return 0
        if row != j:
            a[j],a[row]=a[row],a[j]
            determinant=-determinant
        v=a[j][j]; determinant=determinant*v%p
        inv=pow(v,-1,p)
        for i in range(j+1,r):
            if a[i][j]:
                mult=a[i][j]*inv%p
                for k in range(j+1,r):
                    a[i][k]=(a[i][k]-mult*a[j][k])%p
                a[i][j]=0
    return determinant%p

def v3(value, cutoff):
    if value==0: return cutoff
    n=0
    while n<cutoff and value%3==0:
        value//=3;n+=1
    return n

def smith_exponents_at_3(moments,r,precision):
    # DVR Smith elimination, using unimodular row and column swaps.
    # At each stage choose a globally minimum valuation pivot. Its
    # 3^v unit quotient is invertible modulo 3^(precision-v).
    modulus=3**precision
    a=[[moments[i+j]%modulus for j in range(r)] for i in range(r)]
    exponents=[]
    for j in range(r):
        pivot=min(((v3(a[i][k],precision),i,k)
                  for i in range(j,r) for k in range(j,r)), default=None)
        if pivot is None or pivot[0]>=precision:
            raise ValueError('Insufficient 3-adic precision at column '+str(j))
        value,i,k=pivot
        a[j],a[i]=a[i],a[j]
        if k!=j:
            for row in a: row[j],row[k]=row[k],row[j]
        power=3**value
        inv=pow(a[j][j]//power,-1,modulus//power)
        for i in range(j+1,r):
            if a[i][j]:
                factor=((a[i][j]//power)*inv)%(modulus//power)
                a[i][j]=0
                for k in range(j+1,r):
                    a[i][k]=(a[i][k]-factor*a[j][k])%modulus
        exponents.append(value)
    assert exponents==sorted(exponents)
    return exponents

def run(q,r):
    moments=brc_returns(q,2*r-2)
    determinants={str(p):determinant_mod_prime(moments,r,p) for p in PRIMES}
    assert all(determinants.values())
    e140=smith_exponents_at_3(moments,r,140)
    e160=smith_exponents_at_3(moments,r,160)
    assert e140==e160
    return {
       'q':q,'BRC_branch_count':len(BRANCHES),
       'full_endpoint_count':q**3,'moment_range':[0,2*r-2],
       'Hankel_size':r,'prime_determinant_residues':determinants,
       'smith_exponents_3adic':e140,'max_exponent':max(e140),
       'sum_exponents_det_valuation':sum(e140),
       'histogram':{str(k):v for k,v in sorted(Counter(e140).items())},
       'precisions_compared':[140,160],
       'first_return_moments_decimal':[str(x) for x in moments[:14]]
    }

if __name__=='__main__':
    data={'schema':'R762FB_Q9_RETURN_MOMENT_SMITH_V1',
          'status':'AUTHOR_SIDE_EXACT_ARITHMETIC',
          'observer':'positive six-labelled branch counts returning to (0,0,0)',
          'branch_steps':[list(s) for s in BRANCHES],
          'note':'Smith precision sufficient because every selected pivot exponent is strictly below both moduli exponents',
          'q3_crosscheck':run(3,7),'q9':run(9,127)}
    assert data['q3_crosscheck']['max_exponent']==10
    assert data['q9']['max_exponent']==113
    print(json.dumps(data,sort_keys=True,indent=2,ensure_ascii=False))
