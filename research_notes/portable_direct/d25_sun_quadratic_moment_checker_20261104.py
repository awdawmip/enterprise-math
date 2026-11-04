#!/usr/bin/env python3
"""Exact integer verification: D25 Sun quadratic square and weighted derivatives."""
from math import comb
import json

def primes_under(n):
    sieve=[True]*(n+1);sieve[0]=sieve[1]=False
    for i in range(2,int(n**0.5)+1):
        if sieve[i]:
            for j in range(i*i,n+1,i):sieve[j]=False
    return [x for x in range(5,n+1) if sieve[x]]
def mul(a,b,m):
    return ((a[0]*b[0]+2*a[1]*b[1])%m,(a[0]*b[1]+a[1]*b[0])%m)
def plus(a,b,m):
    return ((a[0]+b[0])%m,(a[1]+b[1])%m)
def scale(a,k,m):
    return (a[0]*k%m,a[1]*k%m)
def period(p,d):
    m=p*p; x=(pow(2,-1,m),pow(4 if d==3 else 3,-1,m))
    f=df=(0,0); coeff=1; xn=(1,0); prev=None
    for k in range(p):
        f=plus(f,scale(xn,coeff,m),m)
        if k:df=plus(df,scale(prev,k*coeff,m),m)
        if k+1<p:
            coeff=coeff*(d*k+1)*(d*k+d-1)*pow(d*d*(k+1)**2,-1,m)%m
            prev=xn; xn=mul(xn,x,m)
    weight=(0,-pow({3:4,4:24}[d],-1,m)%m)
    return f,df,mul(f,f,m),mul(mul(f,df,m),weight,m)
def original(p):
    m=p**3; A=B=MA=MB=0
    for k in range(p):
        common=comb(2*k,k)**2
        a=common*comb(3*k,k)*pow(216,-k,m)%m
        b=common*comb(4*k,2*k)*pow(2304,-k,m)%m
        A=(A+a)%m;B=(B+b)%m;MA=(MA+k*a)%m;MB=(MB+k*b)%m
    return A,B,MA,MB
def main():
    rows=[];bad=[]
    for p in primes_under(500):
        if p%24 not in (13,19):continue
        A,B,MA,MB=original(p)
        fa,da,qa,ma=period(p,3);fb,db,qb,mb=period(p,4);m=p*p
        ua=tuple(z//p for z in fa);ub=tuple(z//p for z in fb)
        pair=plus(scale(mul(ub,db,p),2,p),scale(mul(ua,da,p),-9,p),p)
        checks={
          'a_square':qa==(A%m,0),'b_square':qb==(B%m,0),
          'a_moment':ma==(MA%m,0),'b_moment':mb==(MB%m,0),
          'a_vanish':A%m==0,'b_vanish':B%m==0,
          'a_period_zero':all(z%p==0 for z in fa),
          'b_period_zero':all(z%p==0 for z in fb),
          'signed_weighted':(A-B+6*MA-8*MB)%p**3==0,
          'period_pair':pair==(0,0),
          'first_moment_units':(6*(MA//p))%p==1 and (8*(MB//p))%p==1
        }
        if not all(checks.values()):bad.append((p,checks))
        rows.append({'p':p,'A_over_p2':A//p**2%p,'B_over_p2':B//p**2%p,
                     'D':((A-B)%p**3)//p**2,'MA_over_p':MA//p%p,'MB_over_p':MB//p%p,
                     'Ua':ua,'Ub':ub,'pair':pair,'checks':checks})
    report={'primes':len(rows),'checks':sum(len(x['checks']) for x in rows),
            'failed':len(bad),'bad':bad,'sample':[x for x in rows if x['p'] in (13,19,37,61,67,373)]}
    print(json.dumps(report,ensure_ascii=False,indent=2))
    assert not bad
if __name__=='__main__':main()
