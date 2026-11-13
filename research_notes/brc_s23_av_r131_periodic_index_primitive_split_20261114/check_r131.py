#!/usr/bin/env python3
"""Exact quotient-index validation for a correlated S23 auxiliary observer.
Reuses R130's mathematics, self-contained. All phases are Fraction; no floating point.
"""
from bisect import bisect_left
from collections import defaultdict
from fractions import Fraction as F
from math import gcd
from random import Random
from statistics import median
from time import perf_counter
import json
from pathlib import Path

def frac(q): return q-(q.numerator//q.denominator)

def word(x,A,d,E,m,theta):
    v=frac(E*theta)
    return tuple(int(frac(x+(A+i*d)*theta)<v) for i in range(m))

def integer_roots(b,s,l,h):
    if not s: return []
    lo,hi=sorted((b+s*l,b+s*h))
    first=lo.numerator//lo.denominator+1
    last=(hi.numerator+hi.denominator-1)//hi.denominator-1
    return [(F(n)-b)/s for n in range(first,last+1)]

def sweep_unit(x,A,d,E,m):
    affected=defaultdict(set)
    for p in integer_roots(F(0),E,F(0),F(1)):
        affected[p].update(range(m))
    for i in range(m):
        v=A+i*d
        for p in integer_roots(x,v,F(0),F(1)): affected[p].add(i)
        for p in integer_roots(x,v-E,F(0),F(1)): affected[p].add(i)
    cuts=sorted(affected)
    left=(cuts[0])/2 if cuts else F(1,2)
    state=list(word(x,A,d,E,m,left))
    init=tuple(state)
    events=[]; incidences=0; delta_count=0
    for k,p in enumerate(cuts):
        r=(p+(cuts[k+1] if k+1<len(cuts) else F(1)))/2
        dc=[];dr=[]
        for i in sorted(affected[p]):
            c= int(frac(x+(A+i*d)*p)<frac(E*p))
            z= int(frac(x+(A+i*d)*r)<frac(E*r))
            if c!=state[i]: dc.append((i,c))
            if z!=state[i]: dr.append((i,z))
        incidences+=len(affected[p]); delta_count+=len(dc)+len(dr)
        for i,z in dr: state[i]=z
        events.append((p,dc,dr))
    return init,events,incidences,delta_count

def build(v,a,b):
    if b-a==1:return v[a]
    c=(a+b)//2
    return build(v,a,c),build(v,c,b)

def replace(root,a,b,i,z):
    if b-a==1:return z
    c=(a+b)//2
    if i<c: return replace(root[0],a,c,i,z),root[1]
    return root[0],replace(root[1],c,b,i,z)

def bit(root,a,b,i):
    if b-a==1:return root
    c=(a+b)//2
    return bit(root[0],a,c,i) if i<c else bit(root[1],c,b,i)

class PeriodicIndex:
    def __init__(self,x,A,d,E,m):
        self.x,self.A,self.d,self.E,self.m=F(x),A,d,E,m
        self.g=gcd(gcd(abs(A),abs(d)),abs(E))
        self.cuts=[];self.at=[];self.after=[];self.replacements=0
        self.incidences=0;self.log_deltas=0
        if self.g:
            an,dn,en=A//self.g,d//self.g,E//self.g
            init,events,self.incidences,self.log_deltas=sweep_unit(self.x,an,dn,en,m)
            self.initial=build(init,0,m)
            current=self.initial
            for t,dc,dr in events:
                cut=right=current
                for i,z in dc:cut=replace(cut,0,m,i,z);self.replacements+=1
                for i,z in dr:right=replace(right,0,m,i,z);self.replacements+=1
                self.cuts.append(t);self.at.append(cut);self.after.append(right)
                current=right
        else:
            self.initial=build((0,)*m,0,m)
    def query(self,t,i):
        if not 0<=i<self.m:raise IndexError(i)
        if not self.g:return 0
        phase=frac(self.g*F(t))
        if not phase:return 0
        p=bisect_left(self.cuts,phase)
        if p<len(self.cuts) and self.cuts[p]==phase:return bit(self.at[p],0,self.m,i)
        return bit(self.initial if p==0 else self.after[p-1],0,self.m,i)
    def signature(self,t): return tuple(self.query(t,i) for i in range(self.m))

def test():
    rng=Random(13120261114)
    cases=0; queries=0; total_cuts=0; all_boundary=0
    edge=[(F(0),0,0,0,8),(F(0),0,1,1,16),(F(1,7),-5,5,10,6),
          (F(1,2),-4,-2,6,7),(F(1,3),5,0,-5,9),(F(0),3,-3,-9,11)]
    triples=list(edge)
    for _ in range(140):
        g=rng.randint(1,30)
        x=F(rng.randint(-7,7),rng.randint(1,11))
        A,d,E=[rng.randint(-7,7)*g for _ in range(3)]
        m=rng.randint(1,10)
        triples.append((x,A,d,E,m))
    for x,A,d,E,m in triples:
        idx=PeriodicIndex(x,A,d,E,m);cases+=1;total_cuts+=len(idx.cuts)
        probes=[F(rng.randint(-300,300),rng.randint(1,101)) for _ in range(40)]
        if idx.g:
            probes.extend(F(j,idx.g) for j in range(-3,5))
            all_boundary+=8
            for c in idx.cuts:
                k=rng.randint(-3,3)
                probes.append((c+k)/idx.g)
                left=(idx.cuts[idx.cuts.index(c)-1]+c)/2 if idx.cuts.index(c)>0 else c/2
                probes.append((left+k)/idx.g)
        for t in probes:
            w=idx.signature(t); target=word(x,A,d,E,m,t)
            assert w==target,('mismatch',x,A,d,E,m,t,w,target)
            queries+=m
    magnitudes=[1,10**3,10**12,10**90]
    scale=[]
    for g in magnitudes:
        t0=perf_counter()
        idx=PeriodicIndex(F(0),0,g,g,32)
        build_ms=(perf_counter()-t0)*1000
        probes=[F(rng.randint(-10**95,10**95),rng.randint(1,10**6)) for _ in range(120)]
        probes += [F(j,g) for j in [-4,-1,0,1,5]]
        t0=perf_counter()
        for t in probes: assert idx.signature(t)==word(F(0),0,g,g,32,t)
        query_ms=(perf_counter()-t0)*1000
        scale.append({'g_digits':len(str(g)),'cut_count':len(idx.cuts),'deltas':idx.log_deltas,
                      'incidences':idx.incidences,'build_ms':round(build_ms,3),
                      '125_full_word_queries_ms':round(query_ms,3),'raw_interval_lower_bound_cuts':g-1})
    primitive=[]
    for K in [11,101,1001]:
        delta=F(1,4*K*(K+1))
        left=right=0
        for j in range(1,K):
            t=F(j,K)
            a=word(F(0),K,1,1,3,t-delta)[0]
            b=word(F(0),K,1,1,3,t)[0]
            c=word(F(0),K,1,1,3,t+delta)[0]
            assert (a,b,c)==(0,1,1),(K,j,a,b,c)
            left+=1;right+=1
        primitive.append({'K':K,'gcd':1,'verified_true_jump_points':K-1,'total_possible_word_types':8})
    out={'status':'R131_PERIODIC_PRIMITIVE_SPLIT_PASS','seed':13120261114,
         'random_instances':140,'edge_instances':len(edge),'instances':cases,
         'full_word_query_bits_checked':queries,'total_normalized_cuts':total_cuts,
         'period_boundary_probes':all_boundary,'large_gcd_scaling':scale,
         'primitive_jump_checks':primitive,
         'arithmetic':'fractions.Fraction exact; timing perf_counter CPython, uncontrolled environment'}
    Path(__file__).with_name('verification_r131.json').write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
    print(json.dumps(out,indent=2,sort_keys=True))
if __name__=='__main__':test()
