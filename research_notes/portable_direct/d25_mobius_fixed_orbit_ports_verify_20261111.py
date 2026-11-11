#!/usr/bin/env python3
"""Exact modular checks of author-proved Möbius fixed-orbit theorem. Produces a certificate."""
import math, json
from pathlib import Path

def primes_le(n):
    a=bytearray([1])*(n+1);a[0:2]=b'\x00\x00'
    for d in range(2,math.isqrt(n)+1):
        if a[d]: a[d*d::d]=b'\x00'*(((n-d*d)//d)+1)
    return [i for i in range(7,n+1) if a[i]]
def chi(a,p):
    c=pow(a%p,(p-1)//2,p)
    return 0 if c==0 else (1 if c==1 else -1)
def params(p):
    e=0 if p%6==1 else 1
    m=(p-1-4*e)//6
    assert 6*m+1+4*e==p and m>=1
    return m,e
def norm(p,m,e):
    return -pow(2,-(2*m+e)%(p-1),p)%p
def term(t,p,m,e):
    u=(t+1)*pow(t+2,2,p)*pow(t,-1,p)%p
    v=pow(u,m,p)*pow(t+2,e,p)%p
    w=(2-12*e-(3+10*e)*t)*pow(t+2,-1,p)%p
    return v,v*w%p
def fixed_formula(p,m,e):
    n=m+e
    if chi(2,p)==-1:return 0,0
    sn=0 if n%2 else 2*pow(2,n//2,p)%p
    sn1=0 if (n+1)%2 else 2*pow(2,(n+1)//2,p)%p
    c=norm(p,m,e)*(-1 if m%2 else 1)
    return c*sn%p,c*((4+4*e)*sn1-(3+10*e)*sn)%p
def fixed_direct(p,m,e):
    a=b=0
    for r in range(p):
        if r*r%p!=2:continue
        t=(r-2)%p
        assert t not in (0,p-1,p-2)
        assert (-2*(t+1)*pow(t+2,-1,p))%p==t
        v,vw=term(t,p,m,e)
        a=(a+v)%p;b=(b+vw)%p
    f=norm(p,m,e)
    return a*f%p,b*f%p
def binomial(p,m,e):
    a=b=0
    for k in range(m+1):
        q=math.comb(m,k)*math.comb(2*m+e,k)*pow(2,-k%(p-1),p)%p
        a=(a+q)%p;b=(b+q*(1-6*e+12*k))%p
    return a,b
def moments(p,m,e):
    a=b=0
    for t in range(1,p-2):
        q,z=term(t,p,m,e);a=(a+q)%p;b=(b+z)%p
    f=norm(p,m,e)
    return a*f%p,b*f%p
def main():
    ps=primes_le(30000); records=[]; nsq=0
    for p in ps:
        m,e=params(p);fixed=fixed_formula(p,m,e);s=chi(2,p)
        assert (fixed[1]!=0)==(s==1)
        assert (fixed[0]!=0)==(s==1 and (m+e)%2==0)
        nsq+=(s==1)
        if p<=2500:
            assert fixed==fixed_direct(p,m,e)
            port=moments(p,m,e)
            assert port==binomial(p,m,e)
            records.append(dict(p=p,m=m,epsilon=e,legendre2=s,A_total=port[0],B_total=port[1],
                                A_fixed=fixed[0],B_fixed=fixed[1],
                                A_moving=(port[0]-fixed[0])%p,B_moving=(port[1]-fixed[1])%p))
    x=next(v for v in records if v["p"]==7)
    assert (x["A_total"],x["B_total"],x["A_fixed"],x["B_fixed"],x["A_moving"],x["B_moving"])==(2,0,0,4,2,3)
    out=dict(primes_checked=len(ps),legendre2_plus=nsq,legendre2_minus=len(ps)-nsq,
             full_port_crosschecks=len(records),examples=[v for v in records if v["p"] in (7,23,157,373)],
             records=records,status="EXACT_INTEGER_PASS",author_only=True)
    path=Path(__file__).with_name("d25_mobius_fixed_orbit_ports_certificate_20261111.json")
    path.write_text(json.dumps(out,indent=2)+"\n")
    print(json.dumps({k:v for k,v in out.items() if k!="records"},indent=2))
if __name__=="__main__":main()
