#!/usr/bin/env python3
"""R762JT: exhaustive exact GF(2) parity + certified rainbow forest, Python 3 stdlib.
Success is verified by checking the explicit forest witnesses, never by relying on
random success flags. Can regenerate every witness with the seeded search below.
"""
from itertools import combinations
from collections import Counter
from hashlib import sha256
from random import Random
from pathlib import Path
import json, zlib, base64, sys

AXES = tuple(range(6))
PORTS = tuple(combinations(AXES, 2))
COLORS = tuple(combinations(AXES, 3))
PATTERNS = ((), ((0,1),), ((0,1),(2,3)), ((0,1),(2,3),(4,5)))

def basis(vecs):
    b = {}
    for v in vecs:
        while v:
            k = v.bit_length()-1
            if k in b: v ^= b[k]
            else:
                b[k] = v
                break
    return b

def remainder(v,b):
    for k in sorted(b,reverse=True):
        if v>>k&1: v ^= b[k]
    return v

def analyze(M):
    V=tuple(p for p in PORTS if p not in M)
    idx={p:i for i,p in enumerate(V)}
    full=tuple(s for s in COLORS if all(p in idx for p in combinations(s,2)))
    forced=tuple(s for s in COLORS if s not in full)
    components={p:p for p in V}
    def root(a):
        while components[a]!=a: a=components[a]
        return a
    for s in forced:
        active=tuple(p for p in combinations(s,2) if p in idx)
        assert len(active)==2
        components[root(active[0])] = root(active[1])
    roots={root(v) for v in V}
    cid={v:i for i,v in enumerate(sorted(roots))}
    co={p:cid[root(p)] for p in V}
    edges={s:tuple(combinations(tuple(combinations(s,2)),2)) for s in full}
    vec={s:tuple((1<<idx[a])^(1<<idx[b]) for a,b in edges[s]) for s in full}
    paircomp={s:tuple((co[a],co[b]) for a,b in edges[s]) for s in full}
    return V,full,forced,edges,vec,paircomp,len(roots)

def is_pencil(D,M):
    if len(D)!=4: return False
    return any(all(p in tuple(combinations(s,2)) for s in D)
               and all(set(p).isdisjoint(m) for m in M)
               for p in PORTS if p not in M)

def forest_valid(tree,allowed,pairs,ncomponents):
    if len(tree)!=ncomponents-1: return False
    parent=list(range(ncomponents))
    def root(x):
        while parent[x]!=x: x=parent[x]
        return x
    used=set()
    for s,i in tree:
        if s not in allowed or s in used or i not in range(3):return False
        used.add(s)
        a,b=pairs[s][i]
        x,y=root(a),root(b)
        if x==y:return False
        parent[x]=y
    return len(set(root(i) for i in range(ncomponents)))==1

def find_forest(F,D,pairs,ncomponents,mindex):
    allowed=tuple(s for s in F if s not in D)
    seed=int.from_bytes(sha256((str(mindex)+':'+repr(tuple(D))).encode()).digest()[:8],'big')
    rng=Random(seed)
    for attempt in range(400):
        par=list(range(ncomponents));n=ncomponents;tree=[]
        def root(x):
            while par[x]!=x:x=par[x]
            return x
        order=list(allowed);rng.shuffle(order)
        for s in order:
            choices=list(range(3));rng.shuffle(choices)
            for i in choices:
                a,b=pairs[s][i];a=root(a);b=root(b)
                if a!=b:
                    par[a]=b;n-=1;tree.append((s,i));break
            if n==1:break
        if n==1:
            assert forest_valid(tree,allowed,pairs,ncomponents)
            return tree
    raise AssertionError(f'cannot construct rainbow forest for M={mindex} D={D}')

def run():
    out_dir=Path(__file__).resolve().parent
    totals=[];all_cert=[]
    for mindex,M in enumerate(PATTERNS):
        V,F,G,edges,vec,pairs,ncomp=analyze(M)
        cases=0;parity_ok=0;rainbow_ok=0;exceptions=0
        ranks=Counter();pencils=[]
        for k in range(5):
            for D in combinations(F,k):
                Dset=set(D);cases+=1
                B=basis(v for s in F if s not in Dset for v in vec[s])
                residues={0}
                for s in D:residues={remainder(r^v,B) for r in residues for v in vec[s]}
                needed=1 << (len(V)-1-len(B))
                assert len(residues)==needed,(mindex,D,'parity failure')
                parity_ok+=1;ranks[(k,len(B),len(residues))]+=1
                if is_pencil(D,M):
                    exceptions+=1;pencils.append(tuple(COLORS.index(s) for s in D))
                    continue
                forest=find_forest(F,Dset,pairs,ncomp,mindex)
                assert forest_valid(forest,set(F)-Dset,pairs,ncomp)
                rainbow_ok+=1
                # independent input-readable record: m index, singleton-support indices, (support-index, local-edge-index) per tree edge
                all_cert.append((mindex,[COLORS.index(s) for s in D],[[COLORS.index(s),i] for s,i in forest]))
        totals.append({'missing_ports':mindex,'active_vertices':len(V),'full_colors':len(F),
                      'forced_colors':len(G),'forced_components':ncomp,
                      'patterns':cases,'parity_pass':parity_ok,'rainbow_pass':rainbow_ok,
                      'pencil_exceptions':exceptions,'rank_hist':{str(key):v for key,v in sorted(ranks.items())},
                      'exception_masks':pencils})
    certificate=json.dumps(all_cert,separators=(',',':')).encode()
    packed=base64.b64encode(zlib.compress(certificate,9)).decode()
    open(out_dir/'R762JT_RAINBOW_CERTS.b64','w').write(packed+'\n')
    evidence={'schema':'R762JT_EXACT_FINITE_EVIDENCE_V1',
              'scope':'composite_6_axis_Port_Euler; all matching inactive port sizes 0..3; full support singleton subsets <=4',
              'totals':totals,'total_patterns':sum(x['patterns'] for x in totals),
              'parity_pass':sum(x['parity_pass'] for x in totals),
              'rainbow_pass':sum(x['rainbow_pass'] for x in totals),
              'excluded_pencils':sum(x['pencil_exceptions'] for x in totals),
              'certificate_format':'zlib(json list of (matching_index, [singleton support indices], [[support index, side index], ...])); base64',
              'certificate_records_sha256':sha256(certificate).hexdigest(),
              'certificates_b64_sha256':sha256((packed+'\n').encode()).hexdigest(),
              'review':'AUTHOR_EXACT_FINITE_VERIFIED_NOT_INDEPENDENTLY_REVIEWED'}
    open(out_dir/'R762JT_EVIDENCE.json','w').write(json.dumps(evidence,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({k:v for k,v in evidence.items() if k not in ('totals',)},indent=2))
    for item in totals:print({k:v for k,v in item.items() if k not in ('rank_hist','exception_masks')})

if __name__=='__main__':run()
