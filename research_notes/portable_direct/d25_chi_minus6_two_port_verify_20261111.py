"""Exact finite field check of D25 chi(-6) two-port branch (author-side)."""
import argparse
import json
from math import isqrt

def primes_through(n):
    prime = bytearray([1]) * (n + 1)
    prime[:2] = bytearray([0, 0])
    for q in range(2, isqrt(n) + 1):
        if prime[q]:
            prime[q*q:n+1:q] = bytearray((n-q*q)//q+1)
    return [p for p in range(5, n+1) if prime[p]]

def ratio_port(p, m, eps):
    n = 2*m+eps
    inv = [0]*(m+1)
    if m: inv[1] = 1
    for k in range(2,m+1):
        inv[k] = -(p//k)*inv[p%k] % p
    t,a,jet = 1,1,0
    inv2 = (p+1)//2
    for k in range(1,m+1):
        t = t*(m-k+1)*(n-k+1) % p
        t = t*inv[k]*inv[k]*inv2 % p
        a = (a+t) % p
        jet = (jet+k*t) % p
    return a, ((1-6*eps)*a+12*jet) % p

def factorial_port(p, m, eps):
    n = 2*m+eps
    f = [1]*(n+1)
    for k in range(1,n+1): f[k]=f[k-1]*k % p
    fi = [1]*(n+1)
    fi[n]=pow(f[n],p-2,p)
    for k in range(n,0,-1): fi[k-1]=fi[k]*k % p
    a=jet=0
    x=1
    inv2=(p+1)//2
    for k in range(m+1):
        cm = f[m]*fi[k]*fi[m-k] % p
        cn = f[n]*fi[k]*fi[n-k] % p
        t = cm*cn*x % p
        a = (a+t) % p
        jet = (jet+k*t) % p
        x = x*inv2 % p
    return a, ((1-6*eps)*a+12*jet) % p

def verify(limit):
    counts = {"A_ZERO":0,"B_ZERO":0}
    residues = {str(i):{"total":0,"A_ZERO":0,"B_ZERO":0}
                for i in [1,5,7,11,13,17,19,23]}
    records=[]
    for p in primes_through(limit):
        m=p//6
        eps=(p-1-6*m)//4
        a,b=ratio_port(p,m,eps)
        assert (a,b)==factorial_port(p,m,eps),(p,"independent mismatch")
        chi=1 if pow(-6 % p,(p-1)//2,p)==1 else -1
        assert chi==(-1)**(m//2),(p,"selector mismatch")
        kind="A_ZERO" if chi<0 else "B_ZERO"
        assert (a==0)!=(b==0),(p,"double/neither zero")
        assert (a==0 if kind=="A_ZERO" else b==0),(p,"classification mismatch")
        counts[kind]+=1
        residues[str(p%24)]["total"]+=1
        residues[str(p%24)][kind]+=1
        records.append({"p":p,"m":m,"eps":eps,"A":a,"B":b,
                        "chi_minus6":chi,"type":kind})
    return {"bound":limit,"prime_count":len(records),"counts":counts,
            "by_mod24":residues,"records":records}

if __name__=="__main__":
    parser=argparse.ArgumentParser()
    parser.add_argument("--limit",type=int,default=30000)
    parser.add_argument("--out",default=None)
    args=parser.parse_args()
    result=verify(args.limit)
    if args.out:
        with open(args.out,"w",encoding="utf-8") as f:
            json.dump(result,f,separators=(",",":"),ensure_ascii=False)
    print(json.dumps({k:v for k,v in result.items() if k!="records"},indent=2))
