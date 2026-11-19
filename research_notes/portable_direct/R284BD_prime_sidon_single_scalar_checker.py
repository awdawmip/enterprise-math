#!/usr/bin/env python3
"""R284BD: exact quadratic-mod-prime Sidon scalar Port decoder validation.
Python standard library; signed integer Bareiss determinant; no floating point.
"""
from itertools import product, combinations
from math import factorial, isqrt
from random import Random
import hashlib, json


def next_odd_prime_at_least(n):
    p=max(3,n)
    if p%2==0: p+=1
    while any(p%d==0 for d in range(3,isqrt(p)+1,2)):
        p+=2
    return p


def weights(n):
    p=next_odd_prime_at_least(n)
    a=[2*p*j+(j*j%p) for j in range(n)]
    assert len({a[i]+a[j] for i in range(n) for j in range(i+1,n)})==n*(n-1)//2
    A=max(a)
    Q=n*A+1
    e=[Q+u for u in a]
    T=n*(Q+A)+1
    return p,a,Q,e,T


def setup(n,H,delta=0,variant='prime'):
    assert n>=3 and H>=2 and delta>=0
    if variant=='prime':
        p,a,Q,e,T=weights(n)
    else:
        p=None; a=[j+(2*n+1)*j*j for j in range(n)]
        Q=n*max(a)+1
        e=[Q+u for u in a]
        T=n*(Q+max(a))+1
    L=n*factorial(n)*(1+H)**n
    base=2*L+1 if delta==0 else 4*L+2*(4*delta)+9
    return {'n':n,'H':H,'prime':p,'a':a,'Q':Q,'e':e,'T':T,'L':L,'base':base,
            'd':[pow(base,v) for v in e],
            'z':[0]+[pow(base,i*T) for i in range(1,n)]}


def exact_det(mat):
    n=len(mat)
    A=[list(row) for row in mat]
    sign=1; den=1
    for k in range(n-1):
        if A[k][k]==0:
            s=next((t for t in range(k+1,n) if A[t][k]!=0),None)
            if s is None:return 0
            A[k],A[s]=A[s],A[k];sign=-sign
        pivot=A[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                num=A[i][j]*pivot-A[i][k]*A[k][j]
                q,r=divmod(num,den)
                assert r==0
                A[i][j]=q
            A[i][k]=0
        den=pivot
    return sign*A[-1][-1]


def observe(C,cfg):
    n=len(C)
    A=[[(cfg['d'][i] if i==j else 0)-C[i][j] for j in range(n)]for i in range(n)]
    for j in range(1,n):A[0][j]-=cfg['z'][j]
    return exact_det(A)


def coeff(y,b,k):
    scale=pow(b,k)
    q=(y+scale//2)//scale
    return (q+b//2)%b-b//2


def decode(y,cfg):
    n=cfg['n'];b=cfg['base']; e=cfg['e'];total=sum(e);T=cfg['T']
    C=[[0]*n for _ in range(n)];pair={}
    for i in range(n):C[i][i]=-coeff(y,b,total-e[i])
    for i,j in combinations(range(n),2):
        pair[i,j]=C[i][i]*C[j][j]-coeff(y,b,total-e[i]-e[j])
    for i in range(1,n):
        C[i][0]=-coeff(y,b,i*T+total-e[0]-e[i]);assert C[i][0]>0
        C[0][i],r=divmod(pair[0,i],C[i][0]);assert r==0
    for i in range(1,n):
        for j in range(1,n):
            if i==j:continue
            g=coeff(y,b,i*T+total-e[0]-e[i]-e[j])
            C[i][j],r=divmod(C[i][0]*C[j][j]-g,C[j][0]);assert r==0
    assert all(1<=u<=cfg['H'] for row in C for u in row)
    return C


def run():
    data=[];cases_total=0; noise_total=0
    for n,H,count in ((3,2,512),(3,3,16),(4,2,8),(4,3,8),(5,2,3),(6,2,1)):
        rng=Random(284240+n*19+H)
        cfg=setup(n,H)
        legacy=setup(n,H,variant='legacy')
        arr=product(range(1,H+1),repeat=n*n) if (n,H)==(3,2) else ([rng.randint(1,H) for _ in range(n*n)] for _ in range(count))
        digest=hashlib.sha256();maxbits=0
        for flat in arr:
            flat=list(flat);C=[flat[n*i:n*(i+1)]for i in range(n)]
            y=observe(C,cfg)
            got=decode(y,cfg)
            assert got==C,(n,H,C,got)
            maxbits=max(maxbits,abs(y).bit_length())
            digest.update(bytes(flat));digest.update(b"-" if y<0 else b"+");digest.update(abs(y).to_bytes((abs(y).bit_length()+7)//8,"big"))
        assert maxbits>0
        cases_total+=count
        data.append({'n':n,'H':H,'coverage':'exhaustive' if (n,H)==(3,2) else 'fixed_seed',
          'count':count,'prime':cfg['prime'],'sidon_weights':cfg['a'],
          'max_target_exponent':(n-1)*cfg['T']+sum(cfg['e'])-cfg['e'][0]-cfg['e'][n-1],
          'legacy_max_target_exponent':(n-1)*legacy['T']+sum(legacy['e'])-legacy['e'][0]-legacy['e'][n-1],
          'max_actual_readout_bits':maxbits,
          'max_control_bits':max(v.bit_length() for v in cfg['d']+cfg['z'][1:]),
          'legacy_max_control_bits':max(v.bit_length() for v in legacy['d']+legacy['z'][1:]),
          'sha256_inputs_outputs':digest.hexdigest(),'status':'PASS'})
    rng=Random(284240)
    cfg=setup(3,2,delta=7000)
    for _ in range(32):
        flat=[rng.randint(1,2)for _ in range(9)]
        C=[flat[3*i:3*i+3]for i in range(3)]
        y=observe(C,cfg)
        for eps in (-7000,7000):
            assert decode(y+eps,cfg)==C
            noise_total+=1
    for n in range(3,70):
        p,a,Q,e,T=weights(n)
        assert p>=n and p<2*n and all(e[i]>0 for i in range(n))
    return {'schema':'R284BD_PRIME_SIDON_EXACT_VERIFICATION_V1',
      'precision':'exact signed Python integers, Bareiss determinant',
      'weights_census_n_min':3,'weights_census_n_max':69,
      'matrix_reconstruction_count':cases_total,'bounded_noise_count':noise_total,
      'noise_bound':7000,'cases':data,'overall_status':'PASS',
      'claim_limit':'finite tests corroborate algebraic theorem; no independent peer review'}


if __name__=='__main__':
    print(json.dumps(run(),indent=2,ensure_ascii=False))
