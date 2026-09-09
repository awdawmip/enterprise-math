#!/usr/bin/env python3
"""Two inert directions (5,11) with split-prime refinements.
Exact research prototype, not scalar-label multiplication or Nollm runtime.
Run: python experiment.py --output results
Requires numpy and the frozen split-prime predecessor bundle under prior_bundle/,
or predecessor repository scripts arranged alongside this file.
"""
from __future__ import annotations
import argparse, hashlib, importlib.util, json, math, sys
from collections import Counter, deque
from functools import lru_cache
from itertools import product, combinations, permutations
from pathlib import Path
import numpy as np
ROOT=Path(__file__).resolve().parent
CANDIDATES=[ROOT/'prior_bundle/nollm_split_prime_extension/nollm_split_prime_extension_20260909_c6c82.py',
            ROOT/'nollm_split_prime_extension_20260909_c6c82.py']
pth=next((p for p in CANDIDATES if p.exists()),None)
if pth is None:raise FileNotFoundError('frozen split-prime predecessor required')
PIN='0efac96492fcfa12980ef2c1e9ea80b22b4936a5401dd31d01b7fe6a9c10bda6'
if hashlib.sha256(pth.read_bytes()).hexdigest()!=PIN:raise ValueError('predecessor SHA256 mismatch')
spec=importlib.util.spec_from_file_location('split_predecessor',pth)
f=importlib.util.module_from_spec(spec);sys.modules['split_predecessor']=f;spec.loader.exec_module(f)
m=f.m;sp=f.sp;repair=f.r
I=m.I;W=m.W;M5=m.M;M11=np.array([[3,-1],[2,3]],dtype=np.int64)
ACTIVE=(5,11,7,13,19)
ES={7:m.G,13:f.E13,19:f.E19}
REG=(0,0,-1,-1)
Q=m.Q

def pline(v,p):
    a,b=(int(x)%p for x in v)
    if a:return b*pow(a,-1,p)%p
    if b:return p
    raise ValueError('zero projective vector')
def pv(l,p):return (0,1) if l==p else (1,l)
def act(A,l,p,inverse=False):return pline((m.old.adj(A) if inverse else A)@pv(l,p),p)
def key(s):
    e,g,l,k=s;return (e,g,l if e else -1,k if g else -1)
def canon(A):
    B=m.reduced(np.asarray(A,dtype=np.int64)).copy()
    if m.old.det(B)<0:B[:,1]*=-1
    return B
@lru_cache(None)
def H(e,g,l,k):
    if not e and not g:A=I
    elif e and not g:A=[[1,0],[l,5]] if l<5 else [[5,0],[0,1]]
    elif g and not e:A=[[1,0],[k,11]] if k<11 else [[11,0],[0,1]]
    elif l<5 and k<11:A=[[1,0],[l+5*((k-l)*9%11),55]]
    elif l==5 and k==11:A=[[55,0],[0,1]]
    elif l==5:A=[[5,0],[(5*k)%11,11]]
    else:A=[[11,0],[(11*l)%5,5]]
    B=canon(A);assert m.old.det(B)==5**e*11**g
    return B
@lru_cache(None)
def facets(k):return tuple(repair.facet_vectors(H(*k)))
def pos(v):
    a,b=map(int,v)
    return (a,b) if a>0 or a==0 and b>0 else (-a,-b)
def trans(s,p):
    e,g,l,k=s
    if p==5:return (1-e,g,act(W,l,5) if e else l,k),5*I if e else I
    if p==11:return (e,1-g,l,act(W,k,11) if g else k),11*I if g else I
    E=ES[p];return (e,g,act(E,l,5,True),act(E,k,11,True)),E
STATES=list(product(range(2),range(2),range(6),range(12)))
KEYS=sorted({key(s) for s in STATES})

def prime_factors(n):
    out=[];p=2
    while p*p<=n:
        if n%p==0:
            out.append(p)
            while n%p==0:n//=p
        p+=1
    if n>1:out.append(n)
    return out
NORMS=sorted({Q(v) for k in KEYS for v in facets(k)})
EXCEPT=sorted({p for n in NORMS for p in prime_factors(n) if p%3==1})
for p in EXCEPT:
    if p not in ES:
        a,b=min((a,b) for a,b in product(range(math.isqrt(p)+1),repeat=2) if a*a+a*b+b*b==p)
        ES[p]=np.array([[a,-b],[b,a+b]],dtype=np.int64)

def chirality(u,v):
    d=m.dot2(u,v);c=int(u[0])*int(v[1])-int(u[1])*int(v[0]);return d*d-3*c*c

def find_anchors():
    parent={}
    def find(x):
        parent.setdefault(x,x)
        if parent[x]!=x:parent[x]=find(parent[x])
        return parent[x]
    def union(x,y):
        a,b=find(x),find(y)
        if a!=b:parent[b]=a
    needed={k:set() for k in KEYS};edge_data=[]
    for k in KEYS:
        for v in facets(k):find((k,pos(v)))
    for s in STATES:
        for p in [5,11]+EXCEPT:
            ns,E=trans(s,p);ks,kn=key(s),key(ns)
            fc={tuple(map(int,E@v)):v for v in facets(kn)}
            common=sorted(set(facets(ks))&set(fc))
            for v in common:
                needed[ks].add(pos(v));needed[kn].add(pos(fc[v]));union((ks,pos(v)),(kn,pos(fc[v])))
            edge_data.append((s,p,ns,E,common))
    comps={}
    for n in parent:comps.setdefault(find(n),[]).append(n)
    rid={k:i for i,k in enumerate(sorted(comps,key=str))}
    fixed={rid[find((REG,pos(v)))] for v in facets(REG)}
    vectors=sorted([v for v in product(range(-15,16),repeat=2) if v!=(0,0)],key=lambda v:(Q(v),v))
    domains={}
    for k in KEYS:
        if k==REG:continue
        vs=sorted(needed[k]);patterns={}
        for u in vectors:
            sg=tuple((chirality(u,v)>0)-(chirality(u,v)<0) for v in vs)
            if 0 not in sg:patterns.setdefault(sg,u)
        opts={}
        for sg,u in patterns.items():
            d={};ok=True
            for v,a in zip(vs,sg):
                i=rid[find((k,v))]
                if i in d and d[i]!=a:ok=False;break
                d[i]=a
            if ok and all(d.get(i,1)==1 for i in fixed):opts[tuple(sorted(d.items()))]=u
        domains[k]=opts
    visits=0
    def solve(assigned):
        nonlocal visits
        visits+=1
        while True:
            ds={k:[d for d in opts if all(i not in assigned or assigned[i]==a for i,a in d)] for k,opts in domains.items()}
            if any(not v for v in ds.values()):return None
            forced={}
            for opts in ds.values():
                for i in {i for d in opts for i,_ in d}:
                    val={dict(d)[i] for d in opts}
                    if i not in assigned and len(val)==1:
                        a=next(iter(val))
                        if i in forced and forced[i]!=a:return None
                        forced[i]=a
            if not forced:break
            assigned={**assigned,**forced}
        if all(len(x)==1 for x in ds.values()):return ds
        k=min((k for k,x in ds.items() if len(x)>1),key=lambda k:len(ds[k]))
        for d in ds[k]:
            result=solve({**assigned,**dict(d)})
            if result is not None:return result
        return None
    result=solve({i:1 for i in fixed})
    if result is None:raise AssertionError('candidate quadratic direction search failed')
    anchors={k:domains[k][ds[0]] for k,ds in result.items()}
    rows=[]
    for s,p,ns,E,common in edge_data:
        P=H(*s);C=E@H(*ns);num=m.old.adj(P)@C;det=m.old.det(P)
        assert not np.any(num%det) and m.old.det(num//det)==p
        checks=[]
        for v in common:
            a=1 if key(s)==REG else chirality(anchors[key(s)],v)
            b=1 if key(ns)==REG else chirality(E@anchors[key(ns)],v)
            assert a*b>0,(s,p,v,a,b)
            checks.append([list(v),int(a),int(b)])
        rows.append(dict(state=s,prime=p,next=ns,shared=checks))
    return anchors,dict(atlas_keys=KEYS,anchors=[dict(key=k,u=u) for k,u in sorted(anchors.items())],
      short_norms=NORMS,exceptional_primes=EXCEPT,exception_matrices={str(p):ES[p].tolist() for p in EXCEPT},
      phase_states=len(STATES),phase_transitions=len(rows),shared_components=len(comps),
      fixed_components=len(fixed),solver_visits=visits,transitions=rows)
ANCHORS,CERT=find_anchors()

@lru_cache(None)
def vs(P):return tuple(m.vectors(np.array(P,dtype=np.int64)))
def pkey(P):return tuple(tuple(map(int,row)) for row in P)
def secondary(x,u):
    d=m.dot2(u,x);c=int(u[0])*int(x[1])-int(u[1])*int(x[0]);return (-d*c,d*d)
def member(X,P,u):
    arr=np.asarray(X,dtype=np.int64);sh=arr.shape[:-1];x=arr.reshape(-1,2)
    closed=np.ones(len(x),dtype=bool);vectors=vs(pkey(P))
    for v in vectors:closed &= x[:,0]*(2*v[0]+v[1])+x[:,1]*(v[0]+2*v[1])<=Q(v)
    keep=closed.copy()
    for v in vectors:
        lhs=x[:,0]*(2*v[0]+v[1])+x[:,1]*(v[0]+2*v[1]);ids=np.flatnonzero(closed&(lhs==Q(v)))
        for i in ids:
            z=tuple(map(int,x[i]))
            if u is None:
                if v[0]*z[1]-v[1]*z[0]<=0:keep[i]=False
            else:
                y=(z[0]-v[0],z[1]-v[1]);a,b=secondary(z,u),secondary(y,u)
                assert a!=b,('unresolved tie',z,y)
                if b<a:keep[i]=False
    return keep.reshape(sh)

def section(P,u,limit=700000):
    n=m.old.det(P)
    if n<1 or n>limit:raise ValueError('full section size bound')
    poly=m.vertices(P)
    lo=[math.ceil(min(v[i] for v in poly)) for i in (0,1)]
    hi=[math.floor(max(v[i] for v in poly)) for i in (0,1)]
    x=np.array(list(product(range(lo[0],hi[0]+1),range(lo[1],hi[1]+1))),dtype=np.int64)
    S=x[member(x,P,u)]
    assert len(S)==n
    return S

def section_info(S,P,regular):
    n=len(S);assert len(np.unique(m.coset_keys(S,P),axis=0))==n
    assert m.same_set(S,-S)
    hull=m.old.hull_metrics(S);assert hull['hull_total_lattice_sites']==n
    h=S.T@S
    if regular:
        assert m.same_set(S,S@W.T)
        assert h[0,0]==h[1,1] and 2*h[0,1]==-h[0,0]
    return dict(count=n,holes=0,c2=True,c6=bool(m.same_set(S,S@W.T)),axis_ratio=m.old.ratio(h))

@lru_cache(None)
def offsets(pk,ck):
    P=np.array(pk,dtype=np.int64);C=np.array(ck,dtype=np.int64)
    _,poly=sp.stencil(P,C) # reuse exact polygon, NOT the obsolete radius cutoff
    lo=[math.ceil(min(v[i] for v in poly)) for i in (0,1)]
    hi=[math.floor(max(v[i] for v in poly)) for i in (0,1)]
    V=[v for v in product(range(lo[0],hi[0]+1),range(lo[1],hi[1]+1)) if sp.in_poly(v,poly)]
    return tuple(V),tuple(tuple(str(c) for c in v) for v in poly)

def world(exponents):
    # 5,11,7,13,19 exponents, in this order.
    a,c,b,d,e=map(int,exponents)
    n=5**a*11**c*7**b*13**d*19**e
    if min(exponents)<0 or n>500000000:raise ValueError('bounded int64 prototype index')
    t,u=a//2,c//2;U=m.power(m.G,b)@m.power(f.E13,d)@m.power(f.E19,e)
    l=pline(m.old.adj(U)@m.power(W,t%6)@M5[:,0],5)
    k=pline(m.old.adj(U)@m.power(W,u%6)@M11[:,0],11)
    s=(a%2,c%2,l,k);T=5**t*11**u*U;P=T@H(*s)
    assert m.old.det(P)==n
    anchor=None if key(s)==REG else tuple(map(int,T@ANCHORS[key(s)]))
    return P,anchor,s,T

def next_exp(ex,p):
    y=list(ex);y[ACTIVE.index(p)]+=1;return tuple(y)
def children(S,ex,p):
    P,_,s,T=world(ex);en=next_exp(ex,p);C,u,ns,_=world(en)
    ns0,E=trans(s,p);assert ns0==ns
    V,_=offsets(pkey(H(*s)),pkey(E@H(*ns)))
    V=np.array(V,dtype=np.int64);out=[]
    for i in range(0,len(S),500):
        trial=S[i:i+500,None,:]+(V@P.T)[None,:,:];mask=member(trial,C,u)
        assert np.all(mask.sum(1)==p)
        out.append(trial[mask])
    return np.concatenate(out)

def run(out):
    out.mkdir(parents=True,exist_ok=True)
    (out/'phase_certificate.json').write_text(json.dumps(CERT,indent=2)+'\n')
    print('shared sign certificate PASS',CERT['phase_transitions'],flush=True)
    # Every normalized shape, and a nontrivial odd scalar expansion: direct full enumeration.
    atlas=[];cache={}
    for k in KEYS:
        P=H(*k);u=None if k==REG else ANCHORS[k]
        for scale in (1,5):
            S=section(scale*P,None if u is None else tuple(scale*v for v in u))
            row=section_info(S,scale*P,k==REG);atlas.append(dict(key=k,scale=scale,**row))
            if scale==1:cache[k]=S
    print('atlas sections PASS',len(atlas),sum(r['count'] for r in atlas),flush=True)
    # Deduplicate physical base transitions; test ALL complete parent fibers at scale 1.
    seen=set();stencil_rows=[];edge_rows=[];parents=0
    for s in STATES:
        P=H(*s);ks=key(s);S=cache[ks]
        for p in ACTIVE:
            ns,E=trans(s,p);kn=key(ns);C=E@H(*ns)
            tok=(ks,p,kn,pkey(E))
            if tok in seen:continue
            seen.add(tok)
            u=None if kn==REG else tuple(map(int,E@ANCHORS[kn]))
            V,poly=offsets(pkey(P),pkey(C));V=np.array(V,dtype=np.int64)
            trial=S[:,None,:]+(V@P.T)[None,:,:];mask=member(trial,C,u)
            assert np.all(mask.sum(1)==p)
            children0=trial[mask];dest=section(C,u)
            assert m.same_set(children0,dest) and np.all(member(S,C,u))
            section_info(dest,C,kn==REG)
            parents+=len(S)
            edge_rows.append(dict(key=ks,next_key=kn,prime=p,parents=len(S),children=len(dest)))
            stencil_rows.append(dict(key=ks,next_key=kn,prime=p,E=E.tolist(),
                  candidates=len(V),max_Q=max(map(Q,V)),offsets=V.tolist(),polygon=poly))
    print('all primitive edges PASS',len(edge_rows),'parents',parents,flush=True)
    # Concrete current-chain exponent sections. No sampling in acceptance tests.
    exs=sorted({ex for ex in product(range(4),range(4),range(2),range(2),range(2))
                if math.prod(p**r for p,r in zip(ACTIVE,ex))<=60000})
    exs=sorted(set(exs+[(1,1,1,1,1),(2,2,1,0,0),(2,2,1,1,0),(3,1,1,1,0),(1,3,0,0,1)]))
    world_cache={};rows=[]
    for ex in exs:
        P,u,s,T=world(ex);S=section(P,u);world_cache[ex]=S
        rows.append(dict(exponents=ex,phase=s,**section_info(S,P,key(s)==REG)))
    print('world sections PASS',len(rows),sum(r['count'] for r in rows),flush=True)
    world_edges=[]
    for ex,S in world_cache.items():
        for p in ACTIVE:
            dst=next_exp(ex,p)
            if dst not in world_cache:continue
            P,u,_,_=world(dst);assert np.all(member(S,P,u))
            if len(S)>1000:continue
            child=children(S,ex,p);assert m.same_set(child,world_cache[dst])
            world_edges.append(dict(exponents=ex,prime=p,parents=len(S)))
    paths=[]
    for ex in [(0,0,0,0,0),(1,0,0,0,0),(0,1,0,0,0)]:
        for primes in [(5,11,7),(5,11,13),(5,11,7,13)]:
            dst=ex
            for p in primes:dst=next_exp(dst,p)
            if dst not in world_cache:continue
            for route in permutations(primes):
                cur=ex;S=world_cache[ex]
                for p in route:S=children(S,cur,p);cur=next_exp(cur,p)
                assert m.same_set(S,world_cache[dst])
                _,cts=np.unique(m.coset_keys(S,world(ex)[0]),axis=0,return_counts=True)
                assert len(cts)==len(world_cache[ex]) and np.all(cts==math.prod(primes))
            paths.append(dict(start=ex,primes=primes,routes=math.factorial(len(primes)),
                     parents=len(world_cache[ex]),endpoints=len(world_cache[dst]),mismatches=0))
            print('order group PASS',ex,primes,flush=True)
    # Exact finite projective reachability, not uniformity of samples.
    start=(pline(M5[:,0],5),pline(M11[:,0],11));queue=[start];prev={start:None};edge={}
    for x in queue:
        for p in (7,13,19):
            y=(act(ES[p],x[0],5,True),act(ES[p],x[1],11,True))
            if y not in prev:prev[y]=x;edge[y]=p;queue.append(y)
    assert len(prev)==72
    thin=[]
    for k in KEYS:
        if k[:2]==(1,1) and min(map(Q,facets(k)))==1:thin.append(k)
    assert len(thin)==3
    word=[];x=(0,0)
    while prev[x] is not None:word.append(edge[x]);x=prev[x]
    word.reverse()
    maxc={str(p):max(x['candidates'] for x in stencil_rows if x['prime']==p) for p in ACTIVE}
    result=dict(schema='NOLLM_TWO_INERT_5_11_V1',status='PASS_RESEARCH_NOT_PROMOTED',
       event_id='NOLLM-TWO-INERT-511-20260909-C6C82',source_pin=PIN,M11=M11.tolist(),
       normalized_sublattices=len(KEYS),joint_lines_reached=len(prev),phase_states=len(STATES),
       shared_sign_cases=CERT['phase_transitions'],shared_components=CERT['shared_components'],
       short_facet_norms=NORMS,split_exception_support=EXCEPT,
       atlas_sections=len(atlas),atlas_point_appearances=sum(r['count'] for r in atlas),
       primitive_edges=len(edge_rows),primitive_parents=parents,
       exponent_sections=len(rows),exponent_point_appearances=sum(r['count'] for r in rows),
       largest_section=max(r['count'] for r in rows),world_edges=len(world_edges),
       world_parents=sum(e['parents'] for e in world_edges),order_groups=paths,
       permutation_runs=sum(x['routes'] for x in paths),hull_holes=0,
       candidate_maxima=maxc,unit_thin_keys=thin,unit_thin_route=word,
       unit_thin_basis_ratio_lower_bound=55,
       limits=['index refinement, not ordinary scalar-label multiplication',
               'new anchors migrate some old boundary representatives',
               '91 is a normalized sublattice atlas, not a minimal similarity-class count',
               'point appearances across sections are not unique memories',
               'locality in current basis; candidate count and bit costs are not globally constant',
               '11/13/19 physical fanout hierarchy not implemented'])
    for name,data in [('results.json',result),('atlas_sections.json',atlas),('sections.json',rows),
       ('primitive_edges.json',edge_rows),('stencil_certificate.json',stencil_rows),('world_edges.json',world_edges)]:
        (out/name).write_text(json.dumps(data,indent=2)+'\n')
    np.savez_compressed(out/'layers.npz',**{'e'+'_'.join(map(str,k)):v for k,v in world_cache.items()})
    print(json.dumps(result,indent=2),flush=True)
    return result
if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--output',type=Path,default=ROOT/'results')
    run(parser.parse_args().output)
