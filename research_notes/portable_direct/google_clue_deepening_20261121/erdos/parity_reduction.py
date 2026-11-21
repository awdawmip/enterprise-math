"""Parity of per-position CRT counts without enumerating local residue classes."""
from math import isqrt

def primes(n):
    sieve=bytearray(b'\x01')*(n+1)
    sieve[:2]=b'\x00\x00'
    for p in range(2,isqrt(n)+1):
        if sieve[p]: sieve[p*p:n+1:p]=b'\x00'*((n-p*p)//p+1)
    return [p for p in range(2,n+1) if sieve[p]]

def vf(n,p):
    answer=0
    while n:
        n//=p;answer+=n
    return answer

def logfloor(n,p):
    h=0
    while n>=p:n//=p;h+=1
    return h

def odd_positions(k,ps=None):
    if ps is None:ps=primes(k)
    h=k.bit_length()-1;e=2*h-1
    if k==2:return [0,1]
    if k==3:return [0,2]
    ak=vf(k,2)
    candidates=[i for i in range(k) if
        (max(i,k-1-i).bit_length()-1)+ak-vf(i,2)-vf(k-1-i,2)==e]
    # The last test already has positive valuation for k>=4.
    for p in reversed(ps):
        if p>k or p==2:continue
        a=vf(k,p)
        if k%2:
            zodd=(a-2*vf(k//2,p)==0)
        else:
            zodd=(a-2*vf(k//2,p)>=logfloor(k-1,p))
        candidates=[i for i in candidates if
            (a-vf(i,p)-vf(k-1-i,p)>0)!=zodd]
        if not candidates:break
    return candidates

if __name__=='__main__':
    import sys,time,json
    limit=int(sys.argv[1]) if len(sys.argv)>1 else 512
    ps=primes(limit);out=[];start=time.time()
    for k in range(2,limit+1):
        odd=odd_positions(k,ps)
        if odd and not (k%2 and odd==[k//2]):out.append((k,odd))
        if k%1000==0:print(k,time.time()-start,flush=True)
    print(json.dumps(out))
