#!/usr/bin/env python3
"""Exact, polynomial-bit deterministic single-scalar star-Port reconstruction.
Author-proof research tool; no third-party dependencies.
"""
from itertools import product
from math import factorial
from random import Random
import hashlib, json

def exact_det(a):
    """Bareiss exact determinant with pivoting, supports huge signed integer entries."""
    n=len(a)
    if n==0: return 1
    b=[list(row) for row in a]
    sign=1
    denom=1
    for k in range(n-1):
        if b[k][k]==0:
            p=next((p for p in range(k+1,n) if b[p][k]),None)
            if p is None:return 0
            b[k],b[p]=b[p],b[k]
            sign=-sign
        v=b[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                q,r=divmod(b[i][j]*v-b[i][k]*b[k][j],denom)
                assert r==0
                b[i][j]=q
            b[i][k]=0
        denom=v
    return sign*b[-1][-1]

def setup(n,h,delta_bound=0):
    assert n>=3 and h>=2
    b=2*n+1
    a=[j+b*j*j for j in range(n)]
    q=n*max(a)+1
    e=[q+x for x in a]
    t=n*(q+max(a))+1
    magnitude=n*factorial(n)*(1+h)**n
    assert delta_bound>=0
    if delta_bound:
        # Odd base, with B > 4*L+4 and B > 4*delta+4.
        base=4*magnitude+2*(4*delta_bound)+9
    else:
        base=2*magnitude+1
    d=[pow(base,x) for x in e]
    z=[None]+[pow(base,i*t) for i in range(1,n)]
    return {"n":n,"H":h,"sidon_B":b,"a":a,"Q":q,"E":e,"T":t,"L":magnitude,"base":base,"d":d,"z":z}

def observe(c,config):
    n=config["n"]
    a=[[(-c[i][j] + (config["d"][i] if i==j else 0)) for j in range(n)] for i in range(n)]
    for i in range(1,n):a[0][i]-=config["z"][i]
    return exact_det(a)

def balanced_coeff(y,base,exponent):
    # Every exponent has a signed coefficient bounded by L < base/2.
    # Lower-place tail magnitude < base**exponent/2; nearest-quotient discards it.
    scale=pow(base,exponent)
    q=(y+scale//2)//scale
    return (q+base//2)%base-base//2

def decode(y,config):
    n=config["n"]
    e=config["E"]
    total=sum(e)
    base=config["base"]
    block=config["T"]
    c=[[0]*n for _ in range(n)]
    for i in range(n):
        c[i][i]=-balanced_coeff(y,base,total-e[i])
    pair={}
    for i in range(n):
        for j in range(i+1,n):
            minor=balanced_coeff(y,base,total-e[i]-e[j])
            pair[i,j]=c[i][i]*c[j][j]-minor
    for i in range(1,n):
        c[i][0]=-balanced_coeff(y,base,i*block+total-e[0]-e[i])
        assert c[i][0]>0
        c[0][i],remainder=divmod(pair[0,i],c[i][0]);assert remainder==0
    for i in range(1,n):
        for j in range(1,n):
            if i==j:continue
            minor=balanced_coeff(y,base,i*block+total-e[0]-e[i]-e[j])
            c[i][j],remainder=divmod(c[i][0]*c[j][j]-minor,c[j][0]);assert remainder==0
    return c

def execute_tests():
    cases=[]
    for n,h in [(3,2),(3,3),(4,2),(4,3),(5,2)]:
        rnd=Random(28423+10*n+h)
        cfg=setup(n,h)
        if n==3 and h==2:
            arr=(list(v) for v in product(range(1,h+1),repeat=n*n))
            scope="all 512 matrices in {1,2}^{3x3}"
        else:
            count=16 if n==3 else (8 if n==4 else 3)
            arr=([rnd.randint(1,h) for _ in range(n*n)] for _ in range(count))
            scope=f"{count} seeded random matrices"
        visited=0
        max_output_bits=0
        max_control_bits=max([x.bit_length() for x in cfg["d"]]+[x.bit_length() for x in cfg["z"][1:]])
        digest=hashlib.sha256()
        for flat in arr:
            c=[flat[i*n:(i+1)*n] for i in range(n)]
            y=observe(c,cfg)
            recovered=decode(y,cfg)
            assert recovered==c,(n,h,flat,recovered)
            visited+=1
            max_output_bits=max(max_output_bits,abs(y).bit_length())
            digest.update(bytes(flat))
            digest.update(str(abs(y).bit_length()).encode())
            digest.update(bytes(int(recovered[i][j]) for i in range(n) for j in range(n)))
        cases.append({"n":n,"H":h,"scope":scope,"verified":visited,"max_control_bits":max_control_bits,"max_output_bits":max_output_bits,"Q":cfg["Q"],"T":cfg["T"],"base":cfg["base"],"digest_sha256":digest.hexdigest(),"status":"PASS"})
    # Adversarial-noise fixture: integer disturbance at the exact allowed bound.
    cfg=setup(3,2,delta_bound=7000)
    rnd=Random(284237)
    tests=0
    max_noisy_bits=0
    for k in range(48):
        flat=[rnd.randint(1,2) for _ in range(9)]
        c=[flat[3*i:3*i+3] for i in range(3)]
        y=observe(c,cfg)
        for eps in (-7000,7000):
            assert decode(y+eps,cfg)==c
            max_noisy_bits=max(max_noisy_bits,abs(y+eps).bit_length())
            tests+=1
    return {"schema":"R284BC_EXACT_VERIFICATION_V1","method":"integer Bareiss determinant + direct balanced-digit coefficient extraction","cases":cases,"total_verified":sum(x["verified"] for x in cases),"adversarial_noise":{"n":3,"H":2,"delta":7000,"tested":tests,"errors":[-7000,7000],"max_noisy_output_bits":max_noisy_bits,"status":"PASS"},"status":"PASS","review":"AUTHOR_EXACT_FINITE_CHECK_NOT_INDEPENDENT_REVIEW"}

if __name__=='__main__':
    result=execute_tests()
    print(json.dumps(result,ensure_ascii=False,indent=2))
