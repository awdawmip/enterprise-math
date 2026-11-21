#!/usr/bin/env python3
"""R762IE exact Port quotient / orbit witnesses, integer bitsets only."""
from itertools import combinations, permutations
from collections import Counter
from pathlib import Path
import json, random

T=list(combinations(range(6),3))
LABEL=[''.join(map(str,s)) for s in T]
P=list(combinations(range(6),2))
PI={p:i for i,p in enumerate(P)}
TRI=[tuple(PI[p] for p in combinations(s,2)) for s in T]
CORES=[
 ('024','035','125','134'),
 ('012','015','025','034','123','124'),
 ('012','013','014','025','035','045','125','135','145','234')]
BAD=[
 ('13301','19122','23222','2a121','42528','43114','5b525','63339','81524','83038','93336','ab52a'),
 ('6ccc9','80cc8'),('1d347',)]

def components(q):
    parent=list(range(15))
    def find(x):
        while parent[x]!=x:
            parent[x]=parent[parent[x]]
            x=parent[x]
        return x
    def join(a,b):
        parent[find(a)]=find(b)
    for i,t in enumerate(TRI):
        if (q>>i)&1:
            join(t[0],t[1]);join(t[1],t[2])
    roots=[find(i) for i in range(15)]
    ids={}
    return tuple(ids.setdefault(r,len(ids)) for r in roots)

def quotient_degree(core,comp):
    achievable={0}
    for s in core:
        ps=TRI[LABEL.index(s)]
        opts={(1<<comp[u])^(1<<comp[v]) for u,v in combinations(ps,2)}
        achievable={a^b for a in achievable for b in opts}
    return 0 in achievable

def original_degree(core,q):
    """Independent GF(2)^15 edge-boundary elimination."""
    achievable={0}
    for s in core:
        ps=TRI[LABEL.index(s)]
        opts={(1<<u)^(1<<v) for u,v in combinations(ps,2)}
        achievable={a^b for a in achievable for b in opts}
    basis=[0]*15
    for i,ps in enumerate(TRI):
        if not (q>>i)&1: continue
        for u,v in combinations(ps,2):
            x=(1<<u)^(1<<v)
            for k in range(14,-1,-1):
                if not x & (1<<k):continue
                if basis[k]:x^=basis[k]
                else:basis[k]=x;break
    for x in achievable:
        for k in range(14,-1,-1):
            if (x>>k)&1:x^=basis[k]
        if x==0:return True
    return False

def support_components(core,q):
    """Supports connected when triples intersect in two original axes."""
    ss=set(core)|{LABEL[i] for i in range(20) if (q>>i)&1}
    left=set(ss);out=[]
    while left:
        seed=min(left); reached={seed}; todo=[seed];left.remove(seed)
        while todo:
            s=todo.pop()
            nxt={t for t in left if len(set(s)&set(t))==2}
            left-=nxt;reached|=nxt;todo.extend(nxt)
        out.append(reached)
    return out

def relabel(q,permutation):
    out=0
    for i,t in enumerate(T):
        if (q>>i)&1:
            new=tuple(sorted(permutation[x] for x in t))
            out|=1<<T.index(new)
    return out

def automorphisms(core):
    orig=set(core)
    return [p for p in permutations(range(6))
            if {''.join(map(str,sorted(p[int(x)] for x in s))) for s in core}==orig]

def main():
    report=[]
    expected=((24,[8,4]),(4,[1,1]),(36,[1]))
    for ci,(core,masks,e) in enumerate(zip(CORES,BAD,expected)):
        aut=automorphisms(core)
        assert len(aut)==e[0]
        remaining={int(x,16) for x in masks}
        lens=[]
        while remaining:
            candidate=min(remaining)
            orbit={relabel(candidate,p) for p in aut}
            assert orbit<=set(int(x,16) for x in masks)
            lens.append(len(orbit));remaining-=orbit
        assert sorted(lens,reverse=True)==e[1]
        rows=[]
        for h in masks:
            q=int(h,16);comp=components(q)
            ok=quotient_degree(core,comp)
            assert ok==original_degree(core,q)
            separated=sum(bool(set(core)&c) for c in support_components(core,q))>1
            assert (not ok) or separated
            triples=[tuple(comp[i] for i in TRI[LABEL.index(s)]) for s in core]
            transverse=[s for s,colors in zip(core,triples) if len(set(colors))>1]
            if ci==0 and not ok:
                assert len(set(comp))==3
                assert sorted(Counter(comp).values())==[5,5,5]
                assert len(transverse)==1
                assert len(set(triples[core.index(transverse[0])]))==3
            if ci==0 and ok:
                assert not transverse and separated
            rows.append({'mask':h,'component_sizes':sorted(Counter(comp).values(),reverse=True),
                         'parity_possible':ok,'core_disconnected':separated,
                         'transverse_cores':transverse})
        report.append({'core':list(core),'automorphism_order':len(aut),
                       'orbit_sizes':sorted(lens,reverse=True),'rows':rows})
    rng=random.Random(762116)
    checks=0
    for core in CORES:
        for q in (0,(1<<20)-1,*[rng.randrange(1<<20) for _ in range(500)]):
            assert quotient_degree(core,components(q))==original_degree(core,q)
            checks+=1
    data={'schema':'EM_R762IE_PORT_COMPONENT_QUOTIENT_V1',
          'model':'six-axis composite Port/support/sign observer',
          'scientific_pin':'a72226e2430ffa4786321ac86e7f0c599d5f0389',
          'odd_core_quotient_crosschecks':checks,'classes':report,
          'status':'AUTHOR_PROVED / EXACT_FINITE_CHECKED / NOT_REVIEWED',
          'check':'PASS R762IE port-component quotient and orbit certificate'}
    output=Path(__file__).with_name('R762IE_EVIDENCE.json')
    output.write_text(json.dumps(data,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
    print(data['check'])
    for r in report:
        print('core',len(r['core']),'automorphism',r['automorphism_order'],
              'orbits',r['orbit_sizes'],
              'parity_failures',sum(not x['parity_possible'] for x in r['rows']),
              'connectivity_failures',sum(x['core_disconnected'] for x in r['rows']))

if __name__=='__main__':main()
