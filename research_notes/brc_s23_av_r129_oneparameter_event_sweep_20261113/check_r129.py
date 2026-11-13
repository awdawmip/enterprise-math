#!/usr/bin/env python3
"""R129 signed S23 one-parameter event algorithm; exact Fraction arithmetic."""
from fractions import Fraction as F
from math import gcd
from random import Random
import json
from pathlib import Path

def frac(y):
    return y - (y.numerator // y.denominator)

def direct_arc(x, a, c, j, N, d, m, theta):
    p, q = frac(F(a)*theta), frac(F(c)*theta)
    def contains(z):
        if p == q: return False
        if p < q: return p <= z < q
        return z >= p or z < q
    return tuple(int(contains(frac(x+(N+i*d-j)*theta))) for i in range(m))

def rotated(x, A, d, E, m, theta):
    return tuple(int(frac(x+(A+i*d)*theta) < frac(E*theta)) for i in range(m))

def roots(b, s, l, h):
    if s == 0: return []
    u, v = b+s*l, b+s*h
    low, high = min(u,v), max(u,v)
    first = low.numerator//low.denominator + 1
    last = -((-high.numerator)//high.denominator)-1
    return [(F(k)-b)/s for k in range(first,last+1)]

def exact_signatures(x, A, d, E, m, l=F(0), h=F(1)):
    assert l < h and m >= 2
    points = set(roots(F(0),E,l,h))
    for i in range(m):
        b = A+i*d
        points.update(roots(x,b,l,h))
        points.update(roots(x,b-E,l,h))
    cuts = sorted(points)
    edges = [l,*cuts,h]
    witnesses = []
    for i in range(len(edges)-1):
        witnesses.append((edges[i]+edges[i+1])/2)
        if i < len(cuts): witnesses.append(cuts[i])
    signatures = {}
    for theta in witnesses:
        signatures.setdefault(rotated(x,A,d,E,m,theta),theta)
    L=h-l
    def cnt(s):
        if s == 0: return 0
        t=abs(s)*L
        return -((-t.numerator)//t.denominator)
    limit=cnt(E)+sum(cnt(A+i*d)+cnt(A+i*d-E) for i in range(m))
    assert len(cuts)<=limit
    assert len(signatures)<=2*len(cuts)+1<=2*limit+1
    return signatures,cuts,limit,witnesses

def totient(n):
    return sum(gcd(k,n)==1 for k in range(1,n+1))

def run():
    r=Random(12920261113)
    num=0; probes=0; total_cuts=0; total_words=0; boundary_only=0; example=None
    for z in range(320):
        m=r.randint(2,9)
        a,j,c,N,d=[r.randint(-8,8) for _ in range(5)]
        x=F(r.randint(-11,11),r.randint(1,9))
        l=F(r.randint(-4,0),r.randint(1,4))
        h=l+F(r.randint(1,4),r.randint(1,4))
        A=N-j-a; E=c-a
        sig,cuts,limit,wit=exact_signatures(x,A,d,E,m,l,h)
        total_cuts+=len(cuts); total_words+=len(sig)
        for theta in wit:
            assert direct_arc(x,a,c,j,N,d,m,theta)==rotated(x,A,d,E,m,theta)
            probes+=1
        for _ in range(14):
            theta=l+(h-l)*F(r.randint(1,999),1000)
            assert direct_arc(x,a,c,j,N,d,m,theta) in sig
            probes+=1
        cells={rotated(x,A,d,E,m,(u+v)/2) for u,v in zip([l,*cuts],[*cuts,h])}
        only=set(sig)-cells
        boundary_only+=len(only)
        if example is None and only:
            for theta in cuts:
                s=rotated(x,A,d,E,m,theta)
                if s in only:
                    example={"x":str(x),"a":a,"j":j,"c":c,"N":N,"d":d,"m":m,"l":str(l),"h":str(h),"theta":str(theta),"signature":"".join(map(str,s))}
                    break
        num+=1
    farey=[]
    for m in range(2,33):
        sig,cuts,limit,wit=exact_signatures(F(0),0,1,1,m)
        expected=1+sum(totient(q) for q in range(2,m))
        assert len(sig)==expected==len(cuts)+1
        for s,theta in sig.items():
            target=(1,)+tuple(int((i*theta).numerator//(i*theta).denominator - ((i-1)*theta).numerator//((i-1)*theta).denominator) for i in range(1,m))
            assert s==target
        farey.append({"m":m,"observed":len(sig),"farey_formula":expected,"critical_points":len(cuts),"generic_bound":2*limit+1})
    result={"status":"R129_EVENT_SWEEP_PASS","seed":12920261113,
            "random_instances":num,"directed_arc_cross_checks_and_random_probes":probes,
            "distinct_exact_cuts_total":total_cuts,"sampled_signatures_total":total_words,
            "boundary_only_signatures_random_cases":boundary_only,
            "boundary_only_example":example,"farey_family":farey,
            "arithmetic":"exact fractions only",
            "scope":"sampled finite tests support implementation; universal bounds separately proved"}
    Path(__file__).with_name("verification_r129.json").write_text(json.dumps(result,ensure_ascii=False,sort_keys=True,indent=2)+"\n")
    print(result["status"])
    print({k:v for k,v in result.items() if k!="farey_family"})
    print("Farey m=32:",farey[-1])

if __name__=="__main__":
    run()
