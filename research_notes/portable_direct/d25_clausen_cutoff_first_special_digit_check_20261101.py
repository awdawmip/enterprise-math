#!/usr/bin/env python3
"""Check exact first p^2 Clausen-cutoff digit at z=1/2. No floats."""
from math import isqrt

def primes_upto(lim):
    a=bytearray(b"\x01")*(lim+1)
    a[:2]=b"\x00\x00"
    for i in range(2,isqrt(lim)+1):
        if a[i]: a[i*i::i]=b"\x00"*len(a[i*i::i])
    return [i for i in range(2,lim+1) if a[i]]

def compute(p,full=True):
    modulus=p**3
    r=(p-1)//6
    u=[1]
    for n in range(1,p):
        u.append(u[-1]*(6*n-5)*(3*n-2)*pow(18*n*n,-1,modulus)%modulus)
    c=[pow(10,-1,p)]
    for d in range(1,r):
        c.append(c[-1]*18*d*d*pow((6*d+5)*(3*d+2),-1,p)%p)
    inv2=pow(2,-1,p)
    short=0
    for j in range(r):
        inner=sum((u[i]%p)*c[i-j-1] for i in range(j+1,r+1))%p
        short=(short+(6*j+1)*pow(inv2,j,p)*inner)%p
    if not full:return short
    inv2_3=pow(2,-1,modulus)
    weighted=0
    inv2n=pow(inv2_3,p,modulus)
    for n in range(p,2*p-1):
        k=sum(u[i]*u[n-i] for i in range(n-(p-1),p))%modulus
        weighted=(weighted+(6*n+1)*k*inv2n)%modulus
        inv2n=inv2n*inv2_3%modulus
    assert weighted%(p*p)==0
    direct=weighted//(p*p)
    assert direct==short,(p,direct,short)
    return short

def main():
    probes=[p for p in primes_upto(997) if p%6==1]
    results={p:compute(p) for p in probes}
    assert len(probes)==80
    high=compute(373)
    assert high==196
    assert results[13]==0 and results[19]==12 and results[37]==11
    print("PASS 80/80 p<=997 (p=1 mod6), all coefficients of the cutoff")
    print("PASS p=373, first omitted weighted digit/p^2 =",high)
    print("WITNESSES",[(p,results[p]) for p in (7,13,19,31,37,43,61,109)])
if __name__=="__main__":main()
