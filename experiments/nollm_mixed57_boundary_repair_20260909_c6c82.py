#!/usr/bin/env python3
"""Boundary-compatible, lattice-convex sections for the mixed 5/7 field.
Research experiment, not Nollm runtime or integer-label multiplication.
Run: python experiment.py --output results
Requires numpy and three unchanged hash-pinned predecessor scripts, in prior/
or alongside this file under their repository filenames. No network calls.
"""
from __future__ import annotations
import argparse, hashlib, importlib.util, json, math, sys
from functools import lru_cache
from itertools import product
from pathlib import Path
import numpy as np

ROOT=Path(__file__).resolve().parent
PINS={
 'mixed57':('nollm_mixed57_20260909_c6c82.py','e25484019497105d0110c37fcfabea8668ccf7ff1b024c8c952e3d5955c268c7'),
 'stencil_proof':('nollm_mixed57_stencil_20260909_c6c82.py','d568509d490acad5e636fba4fda11e69f45821d4f906eeb195047cae9d15980d')}
def load(name):
 filename,sha=PINS[name]
 choices=[ROOT/'prior'/f'{name}.py',ROOT/f'{name}.py',ROOT/filename]
 path=next((p for p in choices if p.exists()),None)
 if path is None:raise FileNotFoundError(filename)
 if hashlib.sha256(path.read_bytes()).hexdigest()!=sha:raise ValueError(f'{name}: source pin mismatch')
 sys.path.insert(0,str(path.parent))
 spec=importlib.util.spec_from_file_location(name,path);module=importlib.util.module_from_spec(spec)
 sys.modules[name]=module;spec.loader.exec_module(module);return module
m=load('mixed57');sp=load('stencil_proof')

ANCHORS=((-3,1),(-1,1),(-1,-2),(-1,0),(-2,3),(0,-1))

def facet_vectors(P):
    vertices=m.vertices(P)
    return [u for u in m.vectors(P) if sum((2*u[0]+u[1])*x+(u[0]+2*u[1])*y==m.Q(u)
              for x,y in vertices)>=2]

def anchor(a,b):
    similarity=5**(a//2)*m.power(m.W,(a//2)%6)@m.power(m.G,b)
    return tuple(map(int,similarity@ANCHORS[b%6]))

def tie_key(x,u):
    x=tuple(map(int,x));D=m.dot2(u,x);C=u[0]*x[1]-u[1]*x[0]
    return (-D*C,D*D)

def member(points,a,b):
    """Exact nearest representative; secondary quadratic keys on odd sections."""
    arr=np.asarray(points,dtype=np.int64);shape=arr.shape[:-1];x=arr.reshape(-1,2)
    P=m.basis(a,b);vs=m.vectors(P);closed=np.ones(len(x),dtype=bool)
    for v in vs:
        closed&=x[:,0]*(2*v[0]+v[1])+x[:,1]*(v[0]+2*v[1])<=m.Q(v)
    keep=closed.copy();u=anchor(a,b) if a%2 else None
    for v in vs:
        lhs=x[:,0]*(2*v[0]+v[1])+x[:,1]*(v[0]+2*v[1])
        ids=np.flatnonzero(closed&(lhs==m.Q(v)))
        for i in ids:
            z=tuple(map(int,x[i]))
            if a%2:
                y=(z[0]-v[0],z[1]-v[1]);kz,ky=tie_key(z,u),tie_key(y,u)
                assert kz!=ky,('unresolved minimum tie',a,b,z,y)
                if ky<kz:keep[i]=False
            elif v[0]*z[1]-v[1]*z[0]<=0:keep[i]=False
    return keep.reshape(shape)

def pool(a,b):
    if 5**a*7**b>600000:raise ValueError('full-section prototype limit is 600000')
    P=m.basis(a,b);vs=m.vertices(P)
    lo=[math.ceil(min(v[i] for v in vs)) for i in range(2)]
    hi=[math.floor(max(v[i] for v in vs)) for i in range(2)]
    return np.array(list(product(range(lo[0],hi[0]+1),range(lo[1],hi[1]+1))),dtype=np.int64)

@lru_cache(None)
def phase_stencil(parity,j,prime):
    P=m.H[j] if parity else m.I
    C=(5*m.W if parity else m.H[j]) if prime==5 else (m.G@m.H[(j+1)%6] if parity else m.G)
    vs,_=sp.stencil(P,C)
    return tuple(vs)

def children(parents,a,b,prime,wide=False):
    if prime not in (5,7):raise ValueError('prime must be 5 or 7')
    parents=np.asarray(parents,dtype=np.int64);P=m.basis(a,b)
    vs=m.STENCIL if wide else np.array(phase_stencil(a%2,b%6,prime),dtype=np.int64)
    dst=(a+(prime==5),b+(prime==7));out=[]
    for start in range(0,len(parents),1000):
        ps=parents[start:start+1000];trial=ps[:,None,:]+(vs@P.T)[None,:,:]
        mask=member(trial,*dst)
        assert np.all(mask.sum(axis=1)==prime),('degree',a,b,prime)
        out.append(trial[mask])
    return np.concatenate(out)

def shared_certificate():
    rows=[]
    for j in range(6):
        target=m.I if j%2 else m.G
        found=set(facet_vectors(m.H[j]))&set(facet_vectors(target))
        u=ANCHORS[j];assert found=={u,(-u[0],-u[1])}
        if j%2==0:
            v=tuple(map(int,m.G@ANCHORS[j+1]));assert v in found
        cases=[('5even',m.I,m.H[j]),('5odd',m.H[j],5*m.W),
               ('7even',m.I,m.G),('7odd',m.H[j],m.G@m.H[(j+1)%6])]
        for name,P,C in cases:
            common=set(facet_vectors(P))&set(facet_vectors(C))
            expected=found if (name=='5even' and j%2 or name=='7odd' and not j%2) else set()
            assert common==expected,(j,name,common,expected)
            rows.append({'j':j,'transition':name,'shared_normals':sorted(common)})
    return rows

def run(out):
    out.mkdir(parents=True,exist_ok=True);certificate=shared_certificate()
    states=[(a,b) for a in range(6) for b in range(5) if 5**a*7**b<=600000]+[(1,5),(1,6)]
    cache={};rows=[];comparisons=[];total=0
    for a,b in states:
        X=pool(a,b);P=m.basis(a,b);S=X[member(X,a,b)];n=5**a*7**b
        assert len(S)==n
        assert len(np.unique(m.coset_keys(S,P),axis=0))==n
        assert m.same_set(S,-S)
        metric=m.old.hull_metrics(S);assert metric['hull_total_lattice_sites']==n
        if not a%2:assert m.same_set(S,S@m.W.T)
        h=S.T@S;assert tuple(S.sum(0))==(0,0)
        ratio=m.old.ratio(h)
        if not a%2:assert h[0,0]==h[1,1] and 2*h[0,1]==-h[0,0]
        oldS=X[m.member_array(X,P)];oldh=m.old.hull_metrics(oldS)
        changes=len(set(map(tuple,oldS))-set(map(tuple,S)))
        rows.append(dict(a=a,b=b,count=n,holes=0,c2=True,c6=not bool(a%2),axis_ratio=ratio,
                         predecessor_holes=oldh['hull_total_lattice_sites']-n,reassigned_from_predecessor=changes))
        cache[a,b]=S;total+=n;print(rows[-1],flush=True)
    edge_rows=[];diamond_rows=[];parent_count=0
    for (a,b),S in cache.items():
        for prime,child in [(5,(a+1,b)),(7,(a,b+1))]:
            if child not in cache:continue
            assert np.all(member(S,*child)),('old-address stability',a,b,prime)
            if len(S)>5000:continue
            C=children(S,a,b,prime);assert m.same_set(C,cache[child])
            if len(S)<=300:assert m.same_set(C,children(S,a,b,prime,wide=True))
            parent_count+=len(S);edge_rows.append(dict(a=a,b=b,prime=prime,parents=len(S),
               candidates=len(phase_stencil(a%2,b%6,prime))))
    for (a,b),S in cache.items():
        if len(S)>1000 or (a+1,b+1) not in cache:continue
        c5=children(S,a,b,5);a57=children(c5,a+1,b,7)
        c7=children(S,a,b,7);a75=children(c7,a,b+1,5)
        assert m.same_set(a57,a75) and m.same_set(a57,cache[a+1,b+1])
        keys={tuple(k):i for i,k in enumerate(m.coset_keys(S,m.basis(a,b)))}
        counts=[0]*len(S)
        for k in m.coset_keys(a57,m.basis(a,b)):counts[keys[tuple(k)]]+=1
        assert set(counts)=={35}
        diamond_rows.append(dict(a=a,b=b,parents=len(S),descendants=len(a57),mismatch=0))
    # Rejected shortcut: a globally fixed linear tie choice on odd sections only.
    x=np.array([[5,3]],dtype=np.int64)
    assert m.member_array(x,m.basis(2,1))[0]
    assert not m.member_array(x,m.basis(3,1),mode='lex')[0]
    # The new selectors do retain their own chosen parent points.
    result=dict(schema='NOLLM_MIXED57_BOUNDARY_REPAIR_V1',status='PASS_RESEARCH_NOT_PROMOTED',
       event_id='NOLLM-MIXED57-BOUNDARY-REPAIR-20260909-C6C82',
       source_pins={k:v[1] for k,v in PINS.items()},anchor_table=ANCHORS,
       sections=rows,sections_count=len(rows),enumerated_points_sum=total,
       shared_boundary_certificate=certificate,edges=edge_rows,parents_checked=parent_count,
       diamonds=diamond_rows,diamond_parents=sum(d['parents'] for d in diamond_rows),
       diamond_descendants=sum(d['descendants'] for d in diamond_rows),
       max_candidates=max(len(phase_stencil(e,j,p)) for e,j,p in product(range(2),range(6),(5,7))),
       negative_witness={'old_sixth_even_lex_odd_breaks_stability':{'from':[2,1],'to':[3,1],'lost_point':[5,3]}},
       limits=['new section convention, not a no-movement migration of predecessor addresses',
               'exact index refinement, not scalar multiplication of integer labels',
               'odd bulk elongation remains; no continuous isotropy claim',
               'all-depth arguments use the 24 finite similarity types, not extrapolation from enumeration',
               'local candidate radius is in current lattice coordinates'])
    np.savez_compressed(out/'layers.npz',**{f'a{a}b{b}':S for (a,b),S in cache.items()})
    (out/'results.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:result[k] for k in ['status','sections_count','enumerated_points_sum','parents_checked','diamond_parents','diamond_descendants','max_candidates']}),flush=True)
    return result
if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--output',type=Path,default=Path('results'))
    args=parser.parse_args();run(args.output)
