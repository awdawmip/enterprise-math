#!/usr/bin/env python3
"""Exact integer audit for four BRC null-ideal generators and minimal projector denominator.
Only Python 3 standard library; no floating point or trigonometric calculations.
"""
import hashlib, json, sys
from collections import defaultdict

BRANCHES=((0,0,0),(1,0,0),(0,0,1),(1,1,0),(0,1,1),(1,1,1))
FAMILIES=('A','B','C','D')

def add(v,w,q): return tuple((v[i]+w[i])%q for i in range(3))
def a(r): return 2 if r%3==0 else -1

def generator(q,f):
    out=defaultdict(int)
    for r in range(q):
        for s in range(q):
            if f=='A': v=(0,r+s,-s)
            elif f=='B': v=(r+s,0,s)
            elif f=='C': v=(r+s,-s,0)
            elif f=='D': v=(r+2*s,r+s,-s)
            v=tuple(x%q for x in v)
            out[v]+=a(r)
    return dict(out)

def pair_prod(f,g,q):
    out=defaultdict(int)
    for v,c in f.items():
        for w,e in g.items():
            out[add(v,w,q)]+=c*e
    return dict(out)

def convolution_by_P(f,q):
    out=defaultdict(int)
    for v,c in f.items():
        for b in BRANCHES:
            out[add(v,b,q)]+=c
    return {v:c for v,c in out.items() if c}

def lines(q):
    d=q//3
    o={f:set() for f in FAMILIES}
    for s in range(q):
        for t in (d,2*d):
            o['A'].add((s,t,t))
            o['B'].add((t,s,(-t)%q))
            o['C'].add((t,t,s))
            o['D'].add((s,(t-s)%q,(t+s)%q))
    return o

def digest(f,q):
    h=hashlib.sha256()
    for x in range(q):
      for y in range(q):
       for z in range(q): h.update((str(f.get((x,y,z),0))+'\n').encode())
    return h.hexdigest()

def audit(q):
    assert q in (3,9,27) and (q==3 or q%9==0)
    ks={f:generator(q,f) for f in FAMILIES}
    for f,k in ks.items():
        assert len(k)==q*q,(q,f,len(k))
        assert not convolution_by_P(k,q),(q,f,'P*K nonzero')
    ls=lines(q)
    assert all(len(u)==2*q for u in ls.values())
    pairs=[]; prods={}
    for i,f in enumerate(FAMILIES):
        for g in FAMILIES[i+1:]:
            both=ls[f]&ls[g]
            assert len(both)==2 and all(((-v[0])%q,(-v[1])%q,(-v[2])%q) in both for v in both)
            v=sorted(both)[0]
            assert all(vi%(q//3)==0 for vi in v)
            p=pair_prod(ks[f],ks[g],q)
            assert len(p)==q**3
            for x,c in p.items():
                predicted=q*a(sum((v[i]//(q//3))*x[i] for i in range(3)))
                assert c==predicted,(q,f,g,x,c,predicted)
            prods[(f,g)]=p
            pairs.append(f+g)
    assert len(set().union(*ls.values())) == 8*q-12
    assert len(set().union(*ls.values())) == sum(map(len,ls.values()))-12
    allpts=((x,y,z) for x in range(q) for y in range(q) for z in range(q))
    H={}; N={}
    for v in allpts:
        vH=q*sum(ks[f].get(v,0) for f in FAMILIES)-sum(prods[p][v]//q for p in prods)
        assert vH%3==0,(q,v,vH)
        H[v]=vH; N[v]=vH//3
    assert H[(0,0,0)]==8*q-12
    L=q**3//3
    assert not convolution_by_P(N,q)
    if q<=9:
        NN=pair_prod({v:c for v,c in N.items() if c},{v:c for v,c in N.items() if c},q)
        assert all(NN.get(v,0)==L*N.get(v,0) for v in N),(q,'N^2 != LN')
    return {"Q":q,"characters_checked":q**3,"zero_characters":8*q-12,
        "six_pair_products_checked":6*q**3,"generator_P_annihilation_checks":4*q**3,
        "projector_integrality_checks":q**3,"projector_annihilation_checks":q**3,
        "idempotent_direct_check":q<=9,"minimal_projector_denominator":L,
        "coefficient_at_identity_numerator":8*q-12,"sha256_integer_projector_N":digest(N,q),
        "sha256_K":{f:digest(ks[f],q) for f in FAMILIES},"pair_names":pairs}

if __name__=='__main__':
    result={"schema":"R762EF_INTEGER_NULL_PROJECTOR_EVIDENCE_V1",
       "method":"exact integer convolution in Z[(Z/Q)^3], dense ordered digest x/y/z, no floating point",
       "source":"R762ED eight-line zero locus; frozen positive six-branch P",
       "results":[audit(q) for q in (3,9,27)],"status":"PASS",
       "verification_scope":"finite Q=3,9,27; all-Q proposition is symbolic, using R762ED theorem"}
    content=json.dumps(result,indent=2,ensure_ascii=False,sort_keys=True)+'\n'
    if len(sys.argv)>1:
        with open(sys.argv[1],'w',encoding='utf-8') as f:f.write(content)
    print(content)
