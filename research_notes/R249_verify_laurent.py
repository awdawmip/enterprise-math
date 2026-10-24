#!/usr/bin/env python3
"""R249 exact author-side BRC-algebra checker (not an original Source import).

Independent direct positive (control,weight,X6 translation) histogram versus
prime-valuation Laurent coefficient-dictionary propagation. All six axes
remain typed. Signed differences are external comparison only.
"""
from fractions import Fraction
from collections import defaultdict
from itertools import product
from random import Random
import json

ZERO = (0,)*6
E1 = (1,0,0,0,0,0)
def axis(k): return (k,0,0,0,0,0)

def factors(v):
    assert v>0
    out=[];p=2
    while p*p<=v:
        if v%p==0:
            out.append(p)
            while v%p==0: v//=p
        p+=1
    if v>1:out.append(v)
    return out

def allprimes(packets):
    return sorted({p for edges in packets.values() for _,_,w,_,_ in edges
                   for k in (w.numerator,w.denominator) for p in factors(k)})

def vals(w,primes):
    a,b=w.numerator,w.denominator;out=[]
    for p in primes:
        e=0
        while a%p==0:a//=p;e+=1
        while b%p==0:b//=p;e-=1
        out.append(e)
    assert a==b==1
    return tuple(out)

def add(d,key,v):
    d[key]+=v
    if not d[key]:del d[key]

def matrix(edges,n,primes):
    M=[[defaultdict(int) for t in range(n)] for s in range(n)]
    for s,t,w,delta,c in edges:
        assert w>0 and c>0 and len(delta)==6
        add(M[s][t],vals(w,primes)+delta,c)
    return M

def poly_step(row,M):
    n=len(row);out=[defaultdict(int) for _ in range(n)]
    for s in range(n):
        for ex,v in row[s].items():
            for t in range(n):
                for ey,m in M[s][t].items():
                    add(out[t],tuple(a+b for a,b in zip(ex,ey)),v*m)
    return out

def direct_step(hist,edges):
    out=defaultdict(int)
    for (s,w,delta),v in hist.items():
        for u,t,w2,delta2,c in edges:
            if s==u:
                add(out,(t,w*w2,tuple(a+b for a,b in zip(delta,delta2))),v*c)
    return out

def observed(hist,row,labels,primes):
    a=defaultdict(int);b=defaultdict(int)
    for (s,w,delta),v in hist.items():
        add(a,(labels[s],vals(w,primes)+delta),v)
    for s,poly in enumerate(row):
        for exp,v in poly.items():add(b,(labels[s],exp),v)
    assert dict(a)==dict(b)
    return dict(a)

def eval_word(packets,n,word,start,labels,primes):
    hist={(start,Fraction(1),ZERO):1}
    row=[defaultdict(int) for _ in range(n)]
    row[start][(0,)*(len(primes)+6)]=1
    matrices={k:matrix(v,n,primes) for k,v in packets.items()}
    for letter in word:
        hist=direct_step(hist,packets[letter])
        row=poly_step(row,matrices[letter])
    return observed(hist,row,labels,primes)

def run():
    # n=3 sharp witness: trace difference 0,0,X-1.
    sharp={'a':[(0,2,Fraction(1),ZERO,1),
                (1,0,Fraction(1),ZERO,1),
                (2,2,Fraction(1),E1,1)]}
    p=allprimes(sharp)
    equals=[eval_word(sharp,3,'a'*m,0,[0]*3,p)==
            eval_word(sharp,3,'a'*m,1,[0]*3,p) for m in range(4)]
    assert equals==[True,True,False,False]
    from sympy import Matrix,symbols,simplify
    x=symbols('x')
    M=Matrix([[0,0,1],[1,0,0],[0,0,x]])
    alpha=Matrix([[1,-1,0]]);beta=Matrix([1,1,1])
    traces=[str(simplify((alpha*M**j*beta)[0])) for j in range(4)]
    ranks=[Matrix.vstack(*[alpha*M**j for j in range(k+1)]).rank() for k in range(3)]
    assert traces==['0','0','x - 1','x*(x - 1)'] and ranks==[1,2,3]
    # Equal count and mass but different exact weight histogram.
    weights={'b':[(0,0,Fraction(1),ZERO,1),
                  (0,0,Fraction(3),ZERO,1),
                  (1,1,Fraction(2),ZERO,2)]}
    p2=allprimes(weights)
    assert p2==[2,3]
    assert eval_word(weights,2,'b',0,[0,0],p2)!=eval_word(weights,2,'b',1,[0,0],p2)
    # One-state, unbounded translation effects: (1+X)^m.
    loop=[(0,0,Fraction(1),ZERO,1),(0,0,Fraction(1),E1,1)]
    h={(0,Fraction(1),ZERO):1}
    for m in range(13):
        assert len(h)==m+1 and sum(h.values())==2**m
        h=direct_step(h,loop)
    # Fixed-seed branched positive-algebra comparison, m <= 3.
    rng=Random(249241);checked=0
    ws=[Fraction(1),Fraction(2),Fraction(3,2),Fraction(5,3)]
    for trial in range(36):
        n=rng.choice([2,3,4]);packets={}
        for letter in ['a','b']:
            edges=[]
            for s in range(n):
                for _ in range(rng.choice([1,2,3])):
                    edges.append((s,rng.randrange(n),rng.choice(ws),
                                  axis(rng.choice([-2,-1,0,1,2])),rng.choice([1,2])))
            packets[letter]=edges
        primes=allprimes(packets);labels=[s%2 for s in range(n)]
        for m in range(4):
            for w in product(['a','b'],repeat=m):
                for s in range(n):
                    eval_word(packets,n,w,s,labels,primes);checked+=1
    assert checked==1620
    print(json.dumps({'status':'PASS','model_scope':'finite positive rational-weight BRC algebra / integer X6 translation / full weight-effect keys',
                      'native_enterprise_math_module_imported':False,
                      'sharp_length2_n3':{'equal_by_word_length':equals,'traces':traces,'field_ranks':ranks},
                      'weight_collision':'count2 and mass4 on both starts, but full histograms differ',
                      'binomial_family':'m=0..12 checked, at m12 support13, path count4096',
                      'random_exact_cases':checked,'models':36,'seed':249241},indent=2))
if __name__=='__main__':run()
