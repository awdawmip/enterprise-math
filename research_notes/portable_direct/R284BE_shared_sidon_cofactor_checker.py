#!/usr/bin/env python3
"""R284BE: shared Sidon cofactor-block exact star-Port decoder.
Exact Python integer/Fraction arithmetic; standalone checker; no external packages.
"""
from collections import defaultdict
from fractions import Fraction
from itertools import combinations, product
from math import factorial, isqrt
from random import Random
import hashlib, json

def first_odd_prime(n):
    p=max(3,n)
    if p%2==0:p+=1
    while any(p%d==0 for d in range(3,isqrt(p)+1,2)):p+=2
    return p

def controls(n,H,delta=0):
    assert n>=3 and H>=2 and delta>=0
    p=first_odd_prime(n)
    a=[2*p*i+(i*i%p) for i in range(n)]
    A=max(a);Q=n*A+1
    e=[Q+u for u in a];S=sum(e);K=S+1
    t=[0]+[K+2*a[i] for i in range(1,n)]
    L=n*factorial(n)*(1+H)**n
    delta=Fraction(delta)
    ceil_delta=(delta.numerator+delta.denominator-1)//delta.denominator
    b=2*L+1 if delta==0 else 4*L+8*ceil_delta+9
    return dict(n=n,H=H,p=p,a=a,Q=Q,e=e,S=S,K=K,t=t,L=L,b=b,
                d=[pow(b,x) for x in e],
                z=[0]+[pow(b,x) for x in t[1:]])

def determinant(A):
    A=[row[:] for row in A]
    n=len(A);den=1;sgn=1
    for k in range(n-1):
        if A[k][k]==0:
            s=next((i for i in range(k+1,n) if A[i][k]),None)
            if s is None:return 0
            A[k],A[s]=A[s],A[k];sgn=-sgn
        pivot=A[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                q,r=divmod(A[i][j]*pivot-A[i][k]*A[k][j],den)
                assert r==0
                A[i][j]=q
            A[i][k]=0
        den=pivot
    return sgn*A[-1][-1]

def observe(C,cfg):
    n=cfg['n']
    A=[[(cfg['d'][i] if i==j else 0)-C[i][j] for j in range(n)]
       for i in range(n)]
    for j in range(1,n):A[0][j]-=cfg['z'][j]
    return determinant(A)

def balanced_coefficient(y,b,k):
    scale=pow(b,k)
    q=(Fraction(y)+Fraction(scale,2))//scale
    return (q+b//2)%b-b//2

def decode(y,cfg):
    n,b,e,S,t=(cfg[k] for k in ('n','b','e','S','t'))
    C=[[0]*n for _ in range(n)];pair={}
    for i in range(n):
        C[i][i]=-balanced_coefficient(y,b,S-e[i])
    for i,j in combinations(range(n),2):
        pair[i,j]=C[i][i]*C[j][j]-balanced_coefficient(y,b,S-e[i]-e[j])
    for i in range(1,n):
        C[i][0]=-balanced_coefficient(y,b,t[i]+S-e[0]-e[i])
        assert C[i][0]>0
        C[0][i],r=divmod(pair[0,i],C[i][0]);assert r==0
    for i in range(1,n):
        for j in range(1,n):
            if i==j:continue
            g=balanced_coefficient(y,b,t[i]+S-e[0]-e[i]-e[j])
            C[i][j],r=divmod(C[i][0]*C[j][j]-g,C[j][0]);assert r==0
    assert all(1<=v<=cfg['H'] for row in C for v in row)
    return C

def address_census(n):
    cfg=controls(n,2);a,e,S,t=(cfg[k] for k in ('a','e','S','t'))
    assert len({a[i]+a[j] for i in range(n) for j in range(i,n)})==n*(n+1)//2
    mon=defaultdict(list)
    for mask in range(1<<n):
        U=tuple(i for i in range(n) if mask>>i&1)
        mon[sum(e[i] for i in U)].append(('F',U))
    for i in range(1,n):
        avail=[j for j in range(n) if j not in (0,i)]
        for mask in range(1<<(n-2)):
            U=tuple(j for k,j in enumerate(avail) if mask>>k&1)
            mon[t[i]+sum(e[j] for j in U)].append((f'G{i}',U))
    targets=[];allidx=tuple(range(n))
    for i in range(n):
        targets.append((S-e[i],('F',tuple(j for j in allidx if j!=i))))
    for i,j in combinations(range(n),2):
        targets.append((S-e[i]-e[j],('F',tuple(k for k in allidx if k not in (i,j)))))
    for i in range(1,n):
        cof=tuple(j for j in allidx if j not in (0,i))
        targets.append((t[i]+S-e[0]-e[i],(f'G{i}',cof)))
        for j in range(1,n):
            if i==j:continue
            targets.append((t[i]+S-e[0]-e[i]-e[j],
                            (f'G{i}',tuple(k for k in cof if k!=j))))
    for k,label in targets:
        assert mon[k]==[label],(n,k,label,mon[k])
    return len(targets),len(mon)

def run():
    cases=[];count_total=0
    for n,H,count in [(3,2,512),(3,3,20),(4,2,18),(4,3,8),(5,2,3),(6,2,1)]:
        cfg=controls(n,H)
        rng=Random(284241+17*n+H)
        seq=(product(range(1,H+1),repeat=n*n) if (n,H)==(3,2)
             else ([rng.randint(1,H) for _ in range(n*n)] for _ in range(count)))
        h=hashlib.sha256();maxbits=0
        for flat in seq:
            flat=list(flat)
            C=[flat[i*n:(i+1)*n] for i in range(n)]
            y=observe(C,cfg)
            assert decode(y,cfg)==C
            h.update(bytes(flat));h.update(b'-' if y<0 else b'+')
            h.update(abs(y).to_bytes((abs(y).bit_length()+7)//8,'big'))
            maxbits=max(maxbits,abs(y).bit_length())
        old_T=n*(cfg['Q']+max(cfg['a']))+1
        old_exp=max(cfg['e'][-1],(n-1)*old_T)
        cases.append(dict(n=n,H=H,count=count,
             coverage='exhaustive' if (n,H)==(3,2) else 'seeded',
             exact_max_control_bits_new=max(x.bit_length() for x in cfg['d']+cfg['z'][1:]),
             exact_max_control_bits_old=pow(cfg['b'],old_exp).bit_length(),
             max_actual_readout_bits=maxbits,
             sha256_inputs_outputs=h.hexdigest(),status='PASS'))
        count_total+=count
    census=[]
    for n in range(3,13):
        a,b=address_census(n)
        census.append(dict(n=n,unique_targets=a,distinct_addresses=b))
    cfg=controls(3,2,delta=Fraction(7000,1))
    rng=Random(284241);noise_count=0
    for _ in range(32):
        flat=[rng.randint(1,2) for _ in range(9)]
        C=[flat[i*3:(i+1)*3] for i in range(3)]
        y=observe(C,cfg)
        for eps in (-7000,7000,Fraction(6999,2),Fraction(-6999,2)):
            assert decode(y+eps,cfg)==C
            noise_count+=1
    return dict(schema='R284BE_SHARED_SIDON_PORT_VALIDATION_V1',
      exact_arithmetic='Python integers and rational fractions; Bareiss determinant',
      scope='author-side finite tests; mathematical generality from separate proof',
      matrix_reconstruction_tests=count_total,noise_tests=noise_count,
      address_census=census,cases=cases,status='PASS')

if __name__=='__main__':
    print(json.dumps(run(),indent=2,ensure_ascii=False))
