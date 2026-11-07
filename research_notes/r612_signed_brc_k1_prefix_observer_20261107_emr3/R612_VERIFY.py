#!/usr/bin/env python3
"""R612 exact original-signed-branch prefix-probe and source-fibre checks.
Frozen R462@18783e01e3646c72b7aab3b16d3f565e83e6446f; theta=0.
Int/Fraction only; isolated history summands, not whole native X6 states.
"""
from math import comb
from fractions import Fraction as F
from hashlib import sha256
from pathlib import Path
import json

def C(n,j): return comb(n,j) if 0<=j<=n else 0
def add(p,q):
    z=[0]*max(len(p),len(q))
    for i,v in enumerate(p): z[i]+=v
    for i,v in enumerate(q): z[i]+=v
    return tuple(z)
def mul(p,q):
    z=[0]*(len(p)+len(q)-1)
    for i,a in enumerate(p):
        for j,b in enumerate(q): z[i+j]+=a*b
    return tuple(z)
def term(n,c,h):
    return (0,)*h+tuple(c*C(n,j) for j in range(n+1)) if n>=0 else (0,)
def K(i):
    ds=(-C(4,i)+C(2,i-1),C(5,i-1)-C(5,i-2),C(7,i-2),-C(9,i-3))
    z=(0,)
    for j,d in enumerate(ds,1):
        if d:z=add(z,term(i+1-j,-d,i-1))
    return z
def coeff(p,j):return p[j] if j<len(p) else 0
def k1power(n):return tuple(C(n,j)*2**(n-j)*3**j for j in range(n+1))
def prefix_probe(s,p,n):
    assert n>=s
    a=coeff(mul(k1power(n),p),n)
    b=sum(p[j]*C(n,j)*2**j*3**(n-j) for j in range(min(n,len(p)-1)+1))
    assert a==b
    return 2**(n-s)*a
def norm_val(s,p,n):
    return F(prefix_probe(s,p,n),2**(n-s)*3**n)
def genbin(n,k):
    z=F(1)
    for j in range(k):z=z*(n-j)/F(j+1)
    return z
def interpolate_to_p(s,p):
    degree=len(p)-1
    vals=[norm_val(s,p,n) for n in range(s,s+degree+1)]
    diffs=[]
    a=vals[:]
    while a:
        diffs.append(a[0]);a=[a[i+1]-a[i] for i in range(len(a)-1)]
    def at(n): return sum(diffs[j]*genbin(n-s,j) for j in range(len(diffs)))
    z=[at(n) for n in range(degree+1)]
    rec=[]
    for j in range(degree+1):
        rec.append(z[0]*F(3,2)**j)
        z=[z[i+1]-z[i] for i in range(len(z)-1)]
    assert tuple(rec)==tuple(map(F,p)),(s,p,rec)
    return len(vals)
def main():
    kernels=[K(i) for i in range(1,13)]
    assert kernels[0]==(2,3) and kernels[1]==(0,-1,4,4)
    P=mul(mul(kernels[0],kernels[1]),(1,1))
    assert P==(0,-2,3,25,32,12)
    pair_checks=0
    for words in [(),(1,),(2,),(1,1),(2,1),(1,2),(3,1),(1,2,3)]:
        v=P;u=P
        for i in words:v=mul(kernels[i-1],v)
        for i in words:u=mul(kernels[i-1],u)
        assert v==u
        pair_checks+=1
    Q=mul(mul(mul(kernels[0],kernels[0]),kernels[0]),(1,1))
    assert P!=Q
    first_diff=next(n for n in range(3,3+max(len(P),len(Q)))
                    if prefix_probe(3,P,n)!=prefix_probe(3,Q,n))
    perturb=(17,0,0,0,0,0,0,-9)
    assert prefix_probe(6,perturb,6)==12393
    assert prefix_probe(6,perturb,7)==72054
    tests=0;probes=0
    for s in range(9):
        for degree in range(10):
            for seed in range(4):
                p=tuple((((s+3)*j+7*seed+1)%17)-8 for j in range(degree+1))
                if p[-1]==0:p=p[:-1]+(1,)
                probes+=interpolate_to_p(s,p)
                tests+=1
    record={
      'schema':'R612_EXACT_K1_PREFIX_OBSERVER_SEPARATION_V1',
      'source_pin':'R462@18783e01e3646c72b7aab3b16d3f565e83e6446f',
      'actual_signed_kernel_K1':list(kernels[0]),'actual_signed_kernel_K2':list(kernels[1]),
      'history_pair':{'level_s':3,'history_12':[1,2],'history_21':[2,1],
                      'signed_polynomial':list(P),'blind_prefix_samples_equal':pair_checks},
      'distinct_legitimate_history_comparison':{
          'second_history':[1,1,1],'second_polynomial':list(Q),
          'first_differing_k1_prefix_length_n':first_diff,
          'D_first':prefix_probe(3,P,first_diff),'D_second':prefix_probe(3,Q,first_diff)},
      'R611_free_family_invisible_band_repair':{
          's':6,'delta_coefficients':list(perturb),'isolated_D_q6_k6_after_six_K1_prefixes':12393,
          'isolated_D_q7_k6_after_seven_K1_prefixes':72054},
      'interpolation_exact_cases':tests,'exact_prefix_probes':probes,
      'numeric_semantics':'Python int / Fraction; exact checks for declared finite loops',
      'claim_scope':'isolated original signed BRC expansion-history contributions, not whole native X6 states',
      'terminal_marker':'R612_EXACT_PREFIX_OBSERVER_LENS_PASS'}
    body=json.dumps(record,ensure_ascii=False,sort_keys=True,indent=2)+'\n'
    Path(__file__).with_name('R612_EVIDENCE.json').write_text(body,encoding='utf-8')
    print(record['terminal_marker'],'cases',tests,'probes',probes,'different n',first_diff)
    print('evidence sha256',sha256(body.encode()).hexdigest())
if __name__=='__main__':main()
