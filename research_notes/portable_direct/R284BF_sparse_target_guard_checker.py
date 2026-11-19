#!/usr/bin/env python3
"""R284BF: targeted-degree Q=2A+1 guard, exact finite verification.
Requires sibling R284BE_shared_sidon_cofactor_checker.py (unchanged).
"""
from collections import defaultdict
from fractions import Fraction
from itertools import combinations, product
from math import factorial
from random import Random
import hashlib, json
from R284BE_shared_sidon_cofactor_checker import first_odd_prime, observe, decode

def controls(n,H,delta=0):
    assert n>=3 and H>=2 and delta>=0
    p=first_odd_prime(n)
    a=[2*p*i+(i*i%p) for i in range(n)]
    A=max(a);Q=2*A+1
    e=[Q+v for v in a];S=sum(e);K=S+1
    t=[0]+[K+2*a[i] for i in range(1,n)]
    L=n*factorial(n)*(1+H)**n
    delta=Fraction(delta)
    ceil_delta=(delta.numerator+delta.denominator-1)//delta.denominator
    b=2*L+1 if not delta else 4*L+8*ceil_delta+9
    return dict(n=n,H=H,p=p,a=a,Q=Q,e=e,S=S,K=K,t=t,L=L,b=b,
       d=[pow(b,x) for x in e],z=[0]+[pow(b,x) for x in t[1:]])

def target_census(n):
    c=controls(n,2);e,S,t=c['e'],c['S'],c['t']
    mon=defaultdict(list)
    for mask in range(1<<n):
        U=tuple(j for j in range(n) if mask>>j&1)
        mon[sum(e[j] for j in U)].append(('F',U))
    for i in range(1,n):
        idx=[j for j in range(1,n) if j!=i]
        for mask in range(1<<(n-2)):
            U=tuple(j for v,j in enumerate(idx) if mask>>v&1)
            mon[t[i]+sum(e[j] for j in U)].append((i,U))
    target=[]
    for i in range(n):
        target.append((S-e[i],('F',tuple(j for j in range(n) if j!=i))))
    for i,j in combinations(range(n),2):
        target.append((S-e[i]-e[j],
          ('F',tuple(k for k in range(n) if k not in (i,j)))))
    for i in range(1,n):
        idx=tuple(j for j in range(1,n) if j!=i)
        target.append((t[i]+S-e[0]-e[i],(i,idx)))
        for j in range(1,n):
            if i!=j:
                target.append((t[i]+S-e[0]-e[i]-e[j],
                    (i,tuple(k for k in idx if k!=j))))
    for k,v in target:
        assert mon[k]==[v],(n,k,v,mon[k])
    return len(target),len(mon)

def run():
    cases=[];total=0
    for n,H,count in [(3,2,512),(3,3,20),(4,2,18),(4,3,8),(5,2,3),(6,2,1)]:
        c=controls(n,H)
        rng=Random(284241+17*n+H)
        seq=product(range(1,H+1),repeat=n*n) if (n,H)==(3,2) else (
            [rng.randint(1,H) for _ in range(n*n)] for _ in range(count))
        h=hashlib.sha256();bits=0
        for flat in seq:
            flat=list(flat)
            C=[flat[i*n:(i+1)*n] for i in range(n)]
            y=observe(C,c)
            assert decode(y,c)==C
            h.update(bytes(flat));h.update(b'-' if y<0 else b'+')
            h.update(abs(y).to_bytes((abs(y).bit_length()+7)//8,'big'))
            bits=max(bits,abs(y).bit_length())
        cases.append(dict(n=n,H=H,count=count,
            coverage='exhaustive' if (n,H)==(3,2) else 'seeded',
            max_control_bits=max(v.bit_length() for v in c['d']+c['z'][1:]),
            max_readout_bits=bits,sha256_inputs_outputs=h.hexdigest(),status='PASS'))
        total+=count
    census=[]
    for n in range(3,13):
        targets,addresses=target_census(n)
        census.append(dict(n=n,target_count=targets,address_count=addresses))
    c=controls(3,2,delta=Fraction(7000,1))
    rng=Random(284241);noise=0
    for _ in range(32):
        flat=[rng.randint(1,2) for _ in range(9)]
        C=[flat[i*3:(i+1)*3] for i in range(3)]
        y=observe(C,c)
        for eps in (-7000,7000,Fraction(6999,2),Fraction(-6999,2)):
            assert decode(y+eps,c)==C
            noise+=1
    return dict(schema='R284BF_TARGET_ONLY_GUARD_VALIDATION_V1',
      exact_arithmetic='unbounded Python ints, Fraction, Bareiss determinant',
      matrix_reconstructions=total,bounded_noise_reconstructions=noise,
      target_address_census=census,cases=cases,status='PASS',
      scope='finite validation, not independent review')

if __name__=='__main__':
    print(json.dumps(run(),indent=2,ensure_ascii=False))
