#!/usr/bin/env python3
"""R158: exact two-sided residue certificate and complete Sturmian window.
Python standard library, integer arithmetic only; external scalar model.
Run in bounded batches, e.g. python R158_residue_check.py 33 48.
"""
import json, sys
from collections import defaultdict
from math import gcd
from random import Random

def farey_pairs(m):
    a,b,c,d=0,1,1,m
    while c<=d:
        yield a,b,c,d
        k=(m+b)//d
        a,b,c,d=c,d,k*c-a,k*d-b

def mechanical_words(m):
    out=set()
    for a,b,c,d in farey_pairs(m):
        P=a*d+b*c; Q=2*b*d
        stops=sorted({0,Q}|{(-j*P)%Q for j in range(1,m+1)})
        for lo,hi in zip(stops,stops[1:]):
            x=lo+hi; den=2*Q; num=2*P
            old=x//den; w=0
            for j in range(1,m+1):
                new=(num*j+x)//den
                w=(w<<1)|(new-old)
                old=new
            out.add(w)
    return out

def signature(w,m):
    p=[0]*(m+1)
    for j in range(1,m+1):p[j]=p[j-1]+((w>>(m-j))&1)
    a,b,c,d=0,1,1,1
    for i in range(m):
        for j in range(i+1,m+1):
            k=j-i; q=p[j]-p[i]
            if (q-1)*b>a*k:a,b=q-1,k
            if (q+1)*d<c*k:c,d=q+1,k
    assert a*d<c*b
    g=gcd(abs(a),b);a//=g;b//=g
    g=gcd(abs(c),d);c//=g;d//=g
    U=b+min(p[j]*b-a*j for j in range(m+1))
    V=max(p[j]*d-c*j for j in range(m+1))
    return a,b,c,d,U,V

def count(k,L):
    a,b,c,d,U,V=k
    return -((V-L*c)//d)-((L*a-U)//b)-1

def last_left(k):
    a,b,c,d,U,V=k;D=b*c-a*d
    last=0
    for t in range(1,b+1):
        r=(a*t-U)%b
        H=b*d+b*V-d*(U+r)
        j=(H-D*t)//(D*b)
        if j>=0:last=max(last,t+b*j)
    return last

def last_right(k):
    a,b,c,d,U,V=k;D=b*c-a*d
    last=0
    for t in range(1,d+1):
        s=(c*t-V-1)%d+1
        H=b*s+b*V-d*U
        j=(H-D*t)//(D*d)
        if j>=0:last=max(last,t+d*j)
    return last

def last_direct(k):
    a,b,c,d,U,V=k;D=b*c-a*d
    max_L=(b*d+b*V-d*U)//D
    return max((L for L in range(1,max_L+1) if count(k,L)<=0),default=0)

def test_arbitrary():
    tested=0
    for b in range(1,9):
      for d in range(1,9):
       for a in range(b):
        if gcd(a,b)!=1:continue
        for c in range(1,d+1):
         if gcd(c,d)!=1 or a*d>=b*c:continue
         for U in range(-2,4):
          for V in range(-2,4):
           k=a,b,c,d,U,V
           assert last_left(k)==last_right(k)==last_direct(k),(k,'arbitrary')
           tested+=1
    return tested

def run(start,end):
    rng=Random(158)
    results=[]
    for m in range(start,end+1):
        by=defaultdict(list)
        for w in mechanical_words(m):by[signature(w,m)].append(w)
        peak=-1;maxwords=[];width=0
        for k,ws in by.items():
            a,b,c,d,U,V=k;D=b*c-a*d
            width=max(width,(b*d+b*V-d*U)//D)
            z=last_left(k)
            assert z==last_right(k),(m,k,z)
            if m<=20 or rng.randrange(37)==0:
                assert z==last_direct(k),(m,k,z)
            if z>peak:peak=z;maxwords=list(ws)
            elif z==peak:maxwords+=ws
        T=peak+2
        if m>=5:
            n=m-2
            assert T==n*((m-1)//2)+1,(m,T)
            assert width==n*(n+1)//2-1,(m,width)
            expected={'0'+'1'*n+'0','1'+'0'*n+'1'}
            assert {format(w,f'0{m}b') for w in maxwords}==expected,(m,'maximizers')
        assert max(map(len,by.values()))<=2
        result={'m':m,'words':sum(map(len,by.values())),
                'signatures':len(by),'alias_pairs':sum(len(v)==2 for v in by.values()),
                'T':T,'max_width_certificate':width}
        results.append(result)
        print(result,flush=True)
    return results

if __name__=='__main__':
    start=int(sys.argv[1]) if len(sys.argv)>1 else 1
    end=int(sys.argv[2]) if len(sys.argv)>2 else 24
    n=test_arbitrary() if start==1 else None
    data={'marker':'R158_RESIDUE_CERTIFICATE_EXACT_PASS',
          'unconstrained_parameter_cases':n,'by_length':run(start,end)}
    with open(f'R158_window_{start}_{end}.json','w') as f:
        json.dump(data,f,indent=2)
    print('unconstrained_parameter_cases:',n)
