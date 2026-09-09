#!/usr/bin/env python3
"""Mixed coprime lattice refinements: exact arithmetic, finite research prototype.
Not an ordinary-number multiplication embedding. Run --output DIR.
Requires numpy and hash-pinned baseline.py (prior EM experiment).
"""
from __future__ import annotations
from fractions import Fraction as F
from itertools import product, combinations
from pathlib import Path
import argparse, hashlib, importlib.util, json, math
import numpy as np

BASE_SHA='ab10be88cd4d827a90976aa8a32963a690abdd6b151c46e4c5ba915273637a7e'
p=Path(__file__).with_name('baseline.py')
if not p.exists():p=Path(__file__).with_name('nollm_hecke_layer_views_20260909_c6c82.py')
if hashlib.sha256(p.read_bytes()).hexdigest()!=BASE_SHA:raise ValueError('baseline mismatch')
spec=importlib.util.spec_from_file_location('baseline',p);old=importlib.util.module_from_spec(spec);spec.loader.exec_module(old)
I=np.eye(2,dtype=np.int64)
M=np.array([[2,-1],[1,2]],dtype=np.int64)
B=np.array([[1,-1],[2,3]],dtype=np.int64) # right-prefix companion: M B=5 W
G=np.array([[1,-2],[2,3]],dtype=np.int64)
W=np.array([[0,-1],[1,1]],dtype=np.int64)
ORB=['3','4','2','0','1','inf']
H=[M, np.array([[-2,1],[-3,-1]],dtype=np.int64),
   np.array([[-2,-1],[1,-2]],dtype=np.int64),np.array([[-1,2],[0,-5]],dtype=np.int64),
   np.array([[-3,-1],[2,-1]],dtype=np.int64),np.array([[-5,0],[2,-1]],dtype=np.int64)]
STENCIL=np.array([(q,r) for q in range(-7,8) for r in range(-7,8) if q*q+q*r+r*r<=36],dtype=np.int64)

def power(A,n):
    r=I.copy()
    for _ in range(n):r=r@A
    return r

def basis(a,b):
    if a<0 or b<0 or a>14 or b>14 or 5**a*7**b>10**15:raise ValueError('bounded int64 prototype')
    return 5**(a//2)*power(W,(a//2)%6)@power(G,b)@(H[b%6] if a%2 else I)

def Q(x):q,r=map(int,x);return q*q+q*r+r*r

def qf(x):q,r=x;return q*q+q*r+r*r

def dot2(x,y):a,b=map(int,x);c,d=map(int,y);return 2*a*c+a*d+b*c+2*b*d

def reduced(P):
    u=[int(x) for x in P[:,0]];v=[int(x) for x in P[:,1]]
    for _ in range(100):
        if Q(v)<Q(u):u,v=v,u
        nu=Q(u);d=dot2(u,v)
        if abs(d)<=nu:
            if d>0:v=[-x for x in v]
            return np.array([u,v],dtype=np.int64).T
        k=(d+nu)//(2*nu);v=[v[i]-k*u[i] for i in range(2)]
    raise ArithmeticError('Gauss reduction failed')

def vectors(P):
    U=reduced(P)
    return [tuple(int(x) for x in U@v) for v in product([-1,0,1],repeat=2) if v!=(0,0)]

def vertices(P):
    rows=[(2*q+r,q+2*r,Q((q,r))) for q,r in vectors(P)];out=set()
    for (a,b,c),(d,e,f) in combinations(rows,2):
        dt=a*e-b*d
        if dt:
            x,y=F(c*e-b*f,dt),F(a*f-c*d,dt)
            if all(g*x+h*y<=t for g,h,t in rows):out.add((x,y))
    return sorted(out)

def zmul(x,y):
    a,b=map(int,x);c,d=map(int,y);return (a*c-b*d,a*d+b*c+b*d)

def invariant_key(x):
    """Global total order. Sixth power is C6-invariant; q,r break orbit ties."""
    x=tuple(map(int,x));z=(1,0)
    for _ in range(6):z=zmul(z,x)
    return (Q(x),2*z[0]+z[1],z[1],*x)

def member_array(points,P,mode='sixth'):
    pts=np.asarray(points,dtype=np.int64);shape=pts.shape[:-1];x=pts.reshape(-1,2)
    keep=np.ones(len(x),dtype=bool)
    vs=vectors(P)
    for u in vs:
        lhs=x[:,0]*(2*u[0]+u[1])+x[:,1]*(u[0]+2*u[1]);rhs=Q(u)
        keep &= lhs<=rhs
    # Gauss-reduced +/-u,+/-v,+/-(u+v),+/-(u-v) include all co-nearest ties.
    ids=np.flatnonzero(keep)
    for u in vs:
        lhs=x[ids,0]*(2*u[0]+u[1])+x[ids,1]*(u[0]+2*u[1]);equal=ids[lhs==Q(u)]
        for j in equal:
            a=tuple(map(int,x[j]));c=(a[0]-u[0],a[1]-u[1])
            ka,kc=(invariant_key(a),invariant_key(c)) if mode=='sixth' else (a,c)
            if kc<ka:keep[j]=False
    return keep.reshape(shape)

def section(a,b,mode='sixth'):
    if 5**a*7**b>600000:raise ValueError('full-section enumeration limit exceeded')
    P=basis(a,b);vs=vertices(P)
    lo=[math.ceil(min(v[i] for v in vs)) for i in range(2)]
    hi=[math.floor(max(v[i] for v in vs)) for i in range(2)]
    pts=np.array(list(product(range(lo[0],hi[0]+1),range(lo[1],hi[1]+1))),dtype=np.int64)
    pts=pts[member_array(pts,P,mode)]
    assert len(pts)==old.det(P)==5**a*7**b,(a,b,len(pts),old.det(P))
    return pts

def coset_keys(pts,P):
    return (np.asarray(pts,dtype=np.int64)@old.adj(P).T)%old.det(P)

def same_set(a,b):
    return np.array_equal(np.unique(a,axis=0),np.unique(b,axis=0))

def descendants(pts,a,b,which,stencil=None):
    stencil=STENCIL if stencil is None else np.asarray(stencil,dtype=np.int64)
    P=basis(a,b);child=basis(a+(which==5),b+(which==7));out=[];maxq=0
    for start in range(0,len(pts),1000):
        parents=pts[start:start+1000]
        trial=parents[:,None,:]+(stencil@P.T)[None,:,:]
        mask=member_array(trial,child)
        assert np.all(mask.sum(axis=1)==which),(a,b,which,np.unique(mask.sum(axis=1)))
        used=stencil[mask.any(axis=0)];maxq=max(maxq,max(map(Q,used)))
        out.append(trial[mask])
    return np.concatenate(out),maxq

def audit_geometry(a,b,pts):
    N=len(pts);h=N*(pts.T@pts)-np.outer(pts.sum(axis=0),pts.sum(axis=0))
    hull=old.hull_metrics(pts);c6=same_set(pts,pts@W.T)
    assert len(np.unique(coset_keys(pts,basis(a,b)),axis=0))==N
    if a%2==0:
        assert c6
        if N>1:assert h[0,0]==h[1,1] and 2*h[0,1]==-h[0,0]
    return dict(a=a,b=b,count=N,c6=c6,axis_ratio=old.ratio(h),**hull)

def run(out):
    out.mkdir(parents=True,exist_ok=True)
    assert np.array_equal(M@B,5*W)
    assert np.array_equal(power(G,6)%5,2*I)
    # All lattice incidences in a bounded grid, plus exact primitive-state properties.
    inclusions=0
    for a,b in product(range(10),range(10)):
        P=basis(a,b)
        for da,db,q in [(1,0,5),(0,1,7)]:
            Pc=basis(a+da,b+db);X=old.adj(P)@Pc
            assert not np.any(X%old.det(P))
            assert old.det(X//old.det(P))==q;inclusions+=1
        P5=basis(a,0);P7=basis(0,b)
        for Pa in [P5,P7]:assert not np.any((old.adj(Pa)@P)%old.det(Pa))
        assert old.det(P)==5**a*7**b
    states=[(a,b) for a in range(5) for b in range(4) if 5**a*7**b<=50000]
    states +=[(0,4),(1,4),(2,4),(1,5),(1,6)]
    states=sorted(set(states));cache={};rows=[]
    for a,b in states:
        pts=section(a,b);cache[a,b]=pts;r=audit_geometry(a,b,pts);rows.append(r)
        print(r,flush=True)
    edge_rows=[]
    for (a,b),pts in cache.items():
        if len(pts)>5000:continue
        for q,childstate in [(5,(a+1,b)),(7,(a,b+1))]:
            if childstate not in cache:continue
            child,mq=descendants(pts,a,b,q)
            assert same_set(child,cache[childstate])
            assert np.all(member_array(pts,basis(*childstate))) # old points stable
            edge_rows.append(dict(a=a,b=b,prime=q,parents=len(pts),max_carry_Q=mq))
    # 35-path diamonds from complete parent layers, with both route orders.
    diamonds=[]
    for a,b in product(range(3),range(3)):
        if (a+1,b+1) not in cache or len(cache[a,b])>300:continue
        parents=cache[a,b]
        c5,_=descendants(parents,a,b,5);xy,_=descendants(c5,a+1,b,7)
        c7,_=descendants(parents,a,b,7);yx,_=descendants(c7,a,b+1,5)
        assert same_set(xy,yx) and same_set(xy,cache[a+1,b+1])
        # Same final point has the same parent; each parent receives 35 distinct children.
        pkeys={tuple(k):i for i,k in enumerate(coset_keys(parents,basis(a,b)))}
        bins=np.zeros(len(parents),dtype=int)
        for k in coset_keys(xy,basis(a,b)):bins[pkeys[tuple(k)]]+=1
        assert np.all(bins==35)
        diamonds.append(dict(a=a,b=b,parents=len(parents),paths=len(xy),mismatch=0))
    shape=[]
    for j,h in enumerate(H):
        v=vertices(h);rho2=max(qf(x) for x in v)
        a,bb,c,d=map(int,h.ravel());u=-(bb+c);v0=a+c-d;delta=u*u+u*v0+v0*v0
        assert delta==(1 if j%2==0 else 12)
        shape.append(dict(b_mod6=j,line=ORB[j],H=h.tolist(),delta=delta,
                          rho_squared=str(rho2),sigma_min_squared=3 if j%2==0 else 1))
    result=dict(schema='NOLLM_MIXED57_INTERSECTION_V1',status='EXACT_FINITE_CHECKS_NOT_PROMOTED',
                source_parent='fa10d35c280e284c90acc4ac5e84b71771e73472',
                matrices=dict(M=M.tolist(),B=B.tolist(),G=G.tolist(),W=W.tolist(),commutator=(M@G-G@M).tolist()),
                stencil_count=len(STENCIL),stencil_max_Q=36,inclusion_checks=inclusions,
                shape_states=shape,layers=rows,edges=edge_rows,diamonds=diamonds,
                limits=['index refinement is not multiplication of ordinary integer labels',
                        'Q<=36 bound is in current basis coordinates, not fine-grid physical distance',
                        'canonical sixth-power tie choice may affect odd-layer boundary occupancy',
                        'does not enumerate the complete Hecke correspondence'])
    np.savez_compressed(out/'layers.npz',**{f'a{a}b{b}':v for (a,b),v in cache.items()})
    (out/'results.json').write_text(json.dumps(result,indent=2)+'\n')
    return result

if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--output',type=Path,default=Path('results'))
    args=parser.parse_args();run(args.output)
