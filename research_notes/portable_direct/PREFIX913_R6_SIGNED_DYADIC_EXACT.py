#!/usr/bin/env python3
"""PREFIX-913 signed-dyadic two-flip census. Python 3, standard library only.

Counts the entire (k,ell)=(3,1) sufficient family on strict 19-bit odd
moduli, not the net-new complement of any previous PREFIX certificate.
"""
import hashlib
import json

P = 32
N = 1 << P
LOW, HIGH, M = 262145, 524287, 131072
K, ELL = 3, 1

def signed_values():
    out = {}
    for i in range(2, 23):
        for j in range(1, i):
            for eps in (-1, 1):
                for eta in (-1, 1):
                    d = eps*(1 << i) - eta*(1 << j)
                    out.setdefault(d, (i,j,eps,eta))
    return out

def witness(a,b,params):
    i,j,eps,eta = params
    x = (0 if eps == 1 else (1 << i)) + (
        ((0 if eta == 1 else (1 << j)) - K*a) % (1 << (j+1)))
    y = x + K*a
    u,v = x ^ (1 << i), y ^ (1 << j)
    assert 0 <= x < N and 0 <= y < N and 0 <= u < N and 0 <= v < N
    assert u == x + eps*(1 << i) and v == y + eta*(1 << j)
    assert y-x == K*a and v-u == ELL*b
    assert x%a == y%a and u%b == v%b
    return x,u,y,v

def odd_count(lo,hi):
    lo,hi = max(LOW,lo),min(HIGH,hi)
    return 0 if lo > hi else (hi+1)//2 - lo//2

def main():
    options=signed_values()
    positive=sorted(d for d in options if odd_count(
        (LOW+d+2)//3, (HIGH+d)//3)>0)
    totals={}
    h1=hashlib.sha256()
    count=overlap=diagonal=0
    example=None
    for d in positive:
        lo=max(LOW,(LOW+d+2)//3)
        hi=min(HIGH,(HIGH+d)//3)
        lo+=lo%2 == 0
        hits=0
        for a in range(lo,hi+1,2):
            b=3*a-d
            assert LOW <= b <= HIGH and (b&1)
            x,u,y,v=witness(a,b,options[d])
            z=((a-LOW)//2)*M+(b-LOW)//2
            h1.update(z.to_bytes(8,"little"))
            hits+=1
            overlap += (3*b-a in options)
            diagonal += (a==b)
            if example is None and a != b and a*b >= 33*(1<<32):
                i,j,eps,eta=options[d]
                example=dict(a=a,b=b,D=d,i=i,j=j,eps=eps,eta=eta,
                             first=[x,u],second=[y,v])
        assert hits == odd_count((LOW+d+2)//3,(HIGH+d)//3)
        totals[str(d)]=hits
        count+=hits
    h2=hashlib.sha256()
    independently={}
    overlap2=0
    for d in positive:
        found=0
        for b in range(LOW,HIGH+1,2):
            if (b+d)%3:
                continue
            a=(b+d)//3
            if a<LOW or a>HIGH or not (a&1):
                continue
            z=((a-LOW)//2)*M+(b-LOW)//2
            h2.update(z.to_bytes(8,"little"))
            overlap2+=(3*b-a in options)
            found+=1
        independently[str(d)]=found
    assert independently==totals
    assert h1.hexdigest()==h2.hexdigest()
    assert overlap==overlap2
    assert (len(options),len(positive),count,overlap,diagonal)==(
        884,86,3036491,362,2)
    assert 2*count-overlap==6072620
    certificate=dict(
        schema="EM_PREFIX913_SIGNED_DYADIC_EXACT_V1",
        frozen_scientific_input="f42f2906d77f24085c123f3ccfe9667d41caa96d",
        model=dict(p=32,moduli="odd integers 262145..524287",
                   count_moduli=M,named_trajectories="zero-or-one-XOR-bit"),
        parameter_family=dict(k=3,ell=1,i="2..22",j="1..i-1",
                              eps=[-1,1],eta=[-1,1]),
        result=dict(distinct_signed_D=len(options),
                    contributing_D=len(positive),
                    oriented_pairs=count,
                    transpose_intersection=overlap,
                    diagonal_pairs=diagonal,
                    symmetric_ordered_union=2*count-overlap,
                    full_domain=M*M),
        per_D_counts=totals,
        example=example,
        verification=dict(first_scan="a-first, all XOR witnesses",
             second_scan="independent b-first, exact stream identity",
             witness_checks=count,
             ordered_stream_sha256=h1.hexdigest(),
             independent_stream_sha256=h2.hexdigest(),
             exact_agreement=True),
        interpretation="Sufficient family only; not net-new vs PREFIX-912")
    with open("PREFIX913_R6_SIGNED_DYADIC_RESULTS.json","w",encoding="utf-8") as f:
        json.dump(certificate,f,ensure_ascii=False,sort_keys=True,indent=2)
        f.write("\n")
    print(json.dumps(certificate["result"],sort_keys=True))

if __name__=="__main__":
    main()
