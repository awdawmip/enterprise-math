#!/usr/bin/env python3
"""Exact author-only finite ring check. No native H0/B0 computation."""
import json
from collections import defaultdict

def add(a,b,m):
    return ((a[0]+b[0])%m,(a[1]+b[1])%m)

def mul(a,b,m):
    return ((a[0]*b[0]+2*a[1]*b[1])%m,(a[0]*b[1]+a[1]*b[0])%m)

def conj(a,m):
    return (a[0]%m,-a[1]%m)

def norm(a,m):
    return (a[0]*a[0]-2*a[1]*a[1])%m

def inv(a,m):
    q=pow(norm(a,m),-1,m)
    t=conj(a,m)
    return ((t[0]*q)%m,(t[1]*q)%m)

def root(z,p,n):
    m=p**n; z%=m; assert z%p==1
    s,step=1,p
    for _ in range(1,n):
        assert (z-s*s)%step==0
        s+=(((z-s*s)//step)*pow(2*s,-1,p)%p)*step
        step*=p
    assert (s*s-z)%m==0 and s%p==1
    return s

def from_obs(z,y,p,n):
    m=p**n; assert z%p==1 and y%p==0
    e=(root((z+2*y*y)%m,p,n),y%m)
    assert norm(e,m)==z%m
    return e

def bridge(eta,xi,p,n):
    m=p**n
    assert eta[0]%p==xi[0]%p==1 and eta[1]%p==xi[1]%p==0
    assert norm(eta,m)==norm(xi,m)
    alpha=mul(xi,inv(eta,m),m)
    assert norm(alpha,m)==1 and alpha[0]%p==1
    u=add((1,0),alpha,m)
    assert norm(u,m)%p!=0
    ratio=mul(u,inv(conj(u,m),m),m)
    assert ratio==alpha and mul(eta,ratio,m)==xi
    return u

def complete(p,n):
    m=p**n
    fibers=defaultdict(list)
    for x in range(1,m,p):
        for y in range(0,m,p):
            z=norm((x,y),m)
            fibers[z].append((x,y))
            assert from_obs(z,y,p,n)==(x,y)
    assert len(fibers)==p**(n-1)
    assert all(len(v)==p**(n-1) for v in fibers.values())
    return dict(p=p,n=n,norm_values=len(fibers),fiber_size=p**(n-1),operators=sum(map(len,fibers.values())))

def sampled(p,n):
    m=p**n
    norms={1,(1+p)%m,(1+3*p+p*p)%m,(1+p*(p**(n-2)))%m}
    offsets=[0,1,2,3,7,11,19,29,37,43,101,202,m//p-1]
    count=0
    for z in norms:
        es=[from_obs(z,p*q%m,p,n) for q in offsets]
        for e in es:
            assert from_obs(z,e[1],p,n)==e
            assert norm(e,m)==z
            assert (2*e[1]*e[1]-e[0]*e[0])%m==(-z)%m
            bridge(es[0],e,p,n)
            count+=1
    return count

def main():
    allcases=[(5,2),(5,3),(5,4),(7,2),(7,3),(13,2),(13,3),(19,2)]
    exact=[complete(*pair) for pair in allcases]
    sampled_rows=[]
    for p in (13,19,37,43,109,211,373):
        for n in (2,3,4,5):
            sampled_rows.append(dict(p=p,n=n,checked_conjugations=sampled(p,n)))
    p,n=373,4; m=p**n
    plus=from_obs(1,p,p,n); minus=from_obs(1,(-p)%m,p,n)
    u=bridge(plus,minus,p,n)
    assert plus[1]%p**2==p and minus[1]%p**2==(-p)%p**2
    report=dict(schema="D25_ALL_ORDER_GAUGE_AUTHOR_CHECK_V1",status="PASS",
        native_experiment=False,complete_enumerations=exact,
        target_prime_sample_cases=sampled_rows,
        checked_target_conjugations=sum(r["checked_conjugations"] for r in sampled_rows),
        p373_n4=dict(modulus=m,eta_plus=plus,eta_minus=minus,conjugator=u,norm=1),
        review="AUTHOR_ONLY_UNREVIEWED_NOT_ADMITTED")
    print(json.dumps(report,indent=2))

if __name__=="__main__":
    main()
