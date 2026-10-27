#!/usr/bin/env python3
"""Exact BigInt BRC Newton scan, including the entire specified triangle.
Usage: python R325_scan_triangle_1024.py --max 1024 --json R325_SCAN.json
"""
import argparse, json, hashlib, time
from math import comb

def C(n,k):
    return comb(n,k) if 0 <= k <= n else 0

def kernel(i):
    # -t^(i-1) (1+t)^(i+1) delta_i((1+t)^(-1))
    d=[-C(4,i)+C(2,i-1), C(5,i-1)-C(5,i-2),
       C(7,i-2), -C(9,i-3)]
    a=[0]*(2*i+1)
    for j,v in enumerate(d,1):
        if v==0: continue
        p=i+1-j
        assert p>=0
        for k in range(p+1): a[i-1+k]-=v*C(p,k)
    while a and a[-1]==0: a.pop()
    return a

def source(s):
    if s>10: return []
    a=[0]*(2*s+2)
    for v,p in ((-C(3,s-1),s),(-C(6,s-1),s-1),
                (C(8,s-2),s-2)):
        if v==0: continue
        for k in range(p+1): a[s+k]+=v*C(p,k)
    while a and a[-1]==0: a.pop()
    return a

K=[None]+[kernel(i) for i in range(1,13)]

def scan(n=1024):
    start=time.monotonic()
    history={0:[1,1]}
    checksum=hashlib.sha256()
    triangle_count=0
    negative_tail_count=0
    tail_family_count=0
    first_negative_tail=None
    samples={}
    max_length=0
    for s in range(n+1):
        if s==0:
            b=history[0]
        else:
            b=source(s)
            b.extend([0]*(2*s+2-len(b)))
            for i in range(1,min(s,12)+1):
                v=history[s-i]
                for j,c in enumerate(K[i]):
                    if c:
                        for q,a in enumerate(v): b[q+j]+=c*a
            while b and b[-1]==0: b.pop()
            history[s]=b
            if s>=12: del history[s-12]
        assert len(b)<=2*s+2
        assert b[0]==2**s
        max_length=max(max_length,len(b))
        if s>=13 and (s+3)%4==0:
            r=(s+3)//4
            assert len(b)-1==7*r-5 and b[-1]==-1,(s,r,b[-1])
            tail_family_count+=1
        for q in range(s+1):
            a=b[q] if q<len(b) else 0
            assert a>0,(s,q,a)
            checksum.update(str(a).encode("ascii")+b"\n")
            triangle_count+=1
        for q in range(s+1,len(b)):
            if b[q]<0:
                negative_tail_count+=1
                if first_negative_tail is None:
                    first_negative_tail=[s,q,str(b[q])]
        if s in (0,1,2,3,4,8,12,13,128,129,256,512,1024):
            samples[str(s)]={"degree":len(b)-1,"triangle_edge":str(b[s]),
                 "negative_tail_count":sum(1 for v in b[s+1:] if v<0)}
    return dict(status="PASS",max_s=n,
                triangle_coefficients_checked=triangle_count,
                triangle_sha256=checksum.hexdigest(),
                negative_tail_coefficients=negative_tail_count,
                first_negative_tail=first_negative_tail,
                unbounded_tail_family_samples_checked=tail_family_count,
                max_polynomial_length=max_length,samples=samples,
                elapsed_seconds=round(time.monotonic()-start,3))

if __name__=="__main__":
    p=argparse.ArgumentParser()
    p.add_argument("--max",type=int,default=1024)
    p.add_argument("--json",default=None)
    args=p.parse_args()
    evidence=scan(args.max)
    print(json.dumps({k:v for k,v in evidence.items() if k!="samples"},
                     ensure_ascii=False))
    if args.json:
        with open(args.json,"w",encoding="utf-8") as f:
            json.dump(evidence,f,indent=2,ensure_ascii=False)
            f.write("\n")
