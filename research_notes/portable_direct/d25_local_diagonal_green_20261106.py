#!/usr/bin/env python3
"""D25 standalone finite-field coefficientwise observer check (stdlib only)."""
import json
from math import comb
def primes_upto(n):
    s=[True]*(n+1);s[0]=s[1]=False
    for i in range(2,int(n**0.5)+1):
        if s[i]:
            for j in range(i*i,n+1,i):s[j]=False
    return [i for i in range(7,n+1) if s[i] and i%6==1]
def check_prime(p):
    m=(p-1)//6
    inv=lambda x:pow(x%p,-1,p)
    # Original 216 sequence independent of Gauss-side input
    a=[1]
    for k in range(1,m+1):
        a.append(a[-1]*(2*k-1)*(3*k-2)*(3*k-1)*inv(36*k**3)%p)
    P=[0]*(m+1)
    for t in range(1,m+1):
        P[t]=(P[t-1]+(6*(t-1)+1)*a[t-1])%p
    # Independent Gauss/source pair
    d=[1]
    for i in range(1,m+1):
        d.append(d[-1]*(6*i-5)*(3*i-2)*inv(36*i*i)%p)
    e=[0,inv(10)]
    for r in range(2,m+1):
        e.append(e[-1]*36*(r-1)**2*inv((6*r-1)*(3*r-1))%p)
    c=[0]*m
    for i in range(1,m+1):
        for r in range(1,i+1):
            c[i-r]=(c[i-r]+d[i]*e[r])%p
    # Universal prime-independent kernel, no d/e used
    h=[0]*(m+1);h[1]=inv(24)
    for t in range(1,m):
        h[t+1]=h[t]*t*t*(6*t+1)*inv((t+1)*(2*t+1)*(3*t+2))%p
    for t in range(1,m+1):
        h_bin=(-1 if t%2 else 1)*comb(m,t)*inv(12*t*t*comb(3*m,t)*comb(4*m,t))%p
        h_source=d[t]*inv(12*t*t*a[t])%p
        assert h[t]==h_bin==h_source,(p,t,h[t],h_bin,h_source)
    total=0
    for k in range(m-1,-1,-1):
        total=(total+h[k+1])%p
        assert c[k]==a[k]*total%p,(p,k)
    moments={}
    for name,q in {'unit':lambda k:1,'first':lambda k:k,
                   'second':lambda k:k*k,'signed':lambda k:1+6*k,
                   'cubic':lambda k:2*k**3-3*k+7}.items():
        direct=sum(q(k)*c[k] for k in range(m))%p
        prefix=0;value=0
        for t in range(1,m+1):
            prefix=(prefix+q(t-1)*a[t-1])%p
            value=(value+h[t]*prefix)%p
        assert direct==value,(p,name,direct,value)
        moments[name]=direct
    assert moments['signed']==sum(h[t]*P[t] for t in range(1,m+1))%p
    return {'p':p,'m':m,'J':moments['signed'],
            'C0':moments['unit'],'C1':moments['first'],
            'C2':moments['second'],'H1':h[1]}
def main():
    cases=[check_prime(p) for p in primes_upto(1999)]
    obj={'schema':'D25_MODP_DIAGONAL_GREEN_CHECK_V1',
         'publication':'TP2-B6F4FC938FF94941C1B7',
         'frozen_science':'c47e13e4aba0e006366f989d6334d443f6333ae3',
         'tested_primes':len(cases),
         'target_primes':sum(c['p']%24 in (13,19) for c in cases),
         'coefficient_checks':sum(c['m'] for c in cases),
         'observer_checks':len(cases)*5,'all_checks_pass':True,
         'examples':[x for x in cases if x['p'] in (13,19,67,373,997)],
         'cases':cases}
    print(json.dumps(obj,ensure_ascii=False))
if __name__=='__main__':main()
