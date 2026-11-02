"""D25 exact reflected original 216 coefficient checker; author-side, not native."""
import json
from math import comb

def primes_up_to(n):
    sieve=bytearray(b'\x01')*(n+1)
    sieve[:2]=b'\x00\x00'
    for q in range(2,int(n**.5)+1):
        if sieve[q]:
            sieve[q*q:n+1:q]=b'\x00'*(((n-q*q)//q)+1)
    return [p for p in range(5,n+1) if sieve[p]]

def coeff(p):
    mod=p**3
    inv36=pow(36,-1,mod)
    inv=[0]*p
    inv[1]=1
    for k in range(2,p):
        inv[k]=-(mod//k)*inv[mod%k]%mod
    b=[1]
    for k in range(p-1):
        num=(2*k+1)*(3*k+1)*(3*k+2)
        b.append(b[-1]*num*inv36*pow(inv[k+1],3,mod)%mod)
    return b

def run(limit=3000):
    rows=[]
    for p in primes_up_to(limit):
        mod=p**3
        b=coeff(p)
        a,m,c=p//3,(p-1)//2,2*p//3
        assert a+c==p-1
        for k in range(p):
            v=(2*k)//p+(3*k)//p
            assert b[k]%p**v==0
            if v<3: assert b[k]%p**(v+1)!=0
            j=p-1-k
            assert v+(2*j)//p+(3*j)//p==(2 if k in (a,m,c) else 3)
        if p<=43:
            for k in range(p):
                ref=comb(2*k,k)**2*comb(3*k,k)*pow(216,-k,mod)%mod
                assert b[k]==ref
        chi6=1 if pow(6,(p-1)//2,p)==1 else -1
        assert b[a]*b[c]//p**2%p==3%p
        assert b[m]//p%p==(-2*chi6)%p
        vals=[]
        for f in [lambda k:1,lambda k:k,lambda k:6*k+1,lambda k:k*k]:
            observed=sum(f(k)*b[k]*b[p-1-k] for k in range(p))%mod
            predicted=p*p*(3*f(a)+4*f(m)+3*f(c))%mod
            assert observed==predicted
            vals.append(observed)
        assert vals[0]==10*p*p%mod
        assert vals[1]==-5*p*p%mod
        assert vals[2]==-20*p*p%mod
        assert vals[2]==(3*p-2)*vals[0]%mod
        W=sum((6*k+1)*b[k] for k in range(p))%mod
        sign=1 if p%6==1 else -1
        assert W==sign*p%mod
        if p in (5,7,11,13,19,37,43,373,997,2999):
            rows.append({"p":p,"a":a,"m":m,"c":c,"C1":vals[0],"C6k1":vals[2],"W":W})
    return {"status":"PASS","method":"EXACT_ZMOD_P3_STDLIB","prime_range":[5,limit],
      "tested_primes":len(primes_up_to(limit)),
      "class1_count":sum(p%6==1 for p in primes_up_to(limit)),
      "class5_count":sum(p%6==5 for p in primes_up_to(limit)),
      "candidate_only":"W_p=p*Legendre(-3,p) mod p^3 on finite tested domain",
      "theorem_checks":"Exact valuations, 3-source units, 4 weighted moments",
      "selected":rows}

if __name__=="__main__":
    print(json.dumps(run(),sort_keys=True,indent=2))
