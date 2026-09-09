#!/usr/bin/env python3
"""Exact local residue address field (EM/Nollm research, not runtime architecture).

Run: python experiment.py --output results
Requires numpy and the unchanged prior experiment beside this file as baseline.py,
or nollm_hecke_layer_views_20260909_c6c82.py. No network access is used.
All membership, branching, indexing and hull counts use integer arithmetic.
Eigenvalue ratios are numerical readouts, never acceptance tests for exact symmetry.
"""
from __future__ import annotations
import argparse, hashlib, importlib.util, json, math, random
from pathlib import Path
import numpy as np

BASE_SHA = 'ab10be88cd4d827a90976aa8a32963a690abdd6b151c46e4c5ba915273637a7e'
A = ((2,-1),(1,2))
B = ((1,-1),(2,3))
R = ((0,-1),(1,1))
STENCIL = [(0,0)] + [(q,r) for q in range(-2,3) for r in range(-2,3)
                         if (q,r)!=(0,0) and q*q+q*r+r*r<=4]

def mm(a,b):
    return tuple(tuple(sum(a[i][h]*b[h][j] for h in range(2)) for j in range(2)) for i in range(2))
def mv(a,x): return tuple(sum(a[i][j]*x[j] for j in range(2)) for i in range(2))
def rot(t):
    u=((1,0),(0,1))
    for _ in range(t%6):u=mm(u,R)
    return u

def basis(k):
    n=5**(k//2);c=mm(rot(k//2), A if k%2 else ((1,0),(0,1)))
    return tuple(tuple(n*x for x in row) for row in c)

def member(x,k):
    """Canonical shortest representative for L/P_k L; exact boundary rules."""
    n=5**(k//2)
    q,r=mv(rot(-(k//2)),x) if k%2 else x
    if k%2:
        # Lexicographic tie selection on the rotated index-5 Voronoi hexagon.
        return -7*n<=5*q+4*r<7*n and -n<r<=n and -7*n<=5*q+r<7*n
    # C6-equivariant handed tie selection. n=5**t is coprime to 6;
    # no lattice point lies at a Voronoi corner or edge midpoint.
    for v,cross in ((2*q+r,r),(q+2*r,-q),(q-r,q+r)):
        if abs(v)>n or (abs(v)==n and v*cross<=0): return False
    return True

def children(x,k):
    """Five refinements from depth k; zero carry first, at most 19 candidates."""
    if not member(x,k): raise ValueError('parent is not canonical at this depth')
    p=basis(k); out=[]
    for v in STENCIL:
        d=mv(p,v);y=(x[0]+d[0],x[1]+d[1])
        if member(y,k+1):out.append(y)
    if len(out)!=5 or out[0]!=x:raise AssertionError('local refinement invariant')
    return out

def address(label):
    """Stable positive-integer label -> axial lattice point. Not a similarity homomorphism."""
    if type(label) is not int or label<1:raise ValueError('label must be a positive integer')
    m=label-1;x=(0,0);k=0
    while m:
        m,j=divmod(m,5);x=children(x,k)[j];k+=1
    return x

def label_of(x):
    if len(x)!=2 or any(type(v) is not int for v in x):raise ValueError('two integer coordinates required')
    k=0
    while not member(x,k):k+=1
    ans=0
    for d in range(k,0,-1):
        p=basis(d-1);ps=[]
        for v in STENCIL:
            z=mv(p,v);y=(x[0]-z[0],x[1]-z[1])
            if member(y,d-1):ps.append(y)
        if len(ps)!=1:raise AssertionError('parent uniqueness')
        y=ps[0];ans+=children(y,d-1).index(x)*5**(d-1);x=y
    return ans+1

def members_np(x,k):
    n=5**(k//2)
    if k%2:x=x@np.array(rot(-(k//2)),dtype=np.int64).T
    q=x[...,0];r=x[...,1]
    if k%2:
        return ((-7*n<=5*q+4*r)&(5*q+4*r<7*n)&(-n<r)&(r<=n)&(-7*n<=5*q+r)&(5*q+r<7*n))
    yes=np.ones(q.shape,dtype=bool)
    for v,c in ((2*q+r,r),(q+2*r,-q),(q-r,q+r)):
        yes&=(np.abs(v)<=n)&((np.abs(v)!=n)|(np.sign(v)*c>0))
    return yes

def load_baseline():
    folder=Path(__file__).parent
    candidates=[folder/'nollm_hecke_layer_views_20260909_c6c82.py',folder/'baseline.py']
    path=next((p for p in candidates if p.exists()),None)
    if path is None:raise FileNotFoundError('unchanged prior experiment is required beside this file')
    if hashlib.sha256(path.read_bytes()).hexdigest()!=BASE_SHA:raise ValueError('baseline SHA256 mismatch')
    spec=importlib.util.spec_from_file_location('verified_prior',path)
    old=importlib.util.module_from_spec(spec);spec.loader.exec_module(old)
    return old

def run(out):
    old=load_baseline();out.mkdir(parents=True,exist_ok=True)
    assert mm(A,B)==((0,-5),(5,5)) and len(STENCIL)==19
    # Extend, rather than repeat, the prior 256-choice optimization experiment.
    options=old.compact_options();baseline=[]
    for name,pullback in [('current_frame_greedy',False),('pullback_frame_greedy',True)]:
        h=np.zeros((2,2),dtype=np.int64);p=np.eye(2,dtype=np.int64);choice=[]
        for m,ds in zip(old.MATS,options):
            p=m@p;ap=old.adj(p)
            variants=[m@h@m.T+d.T@d for d in ds]
            i=min(range(len(ds)),key=lambda i:old.objective(ap@variants[i]@ap.T if pullback else variants[i]))
            h=variants[i];choice.append(i)
        baseline.append(dict(name=name,choice=choice,endpoint_ratio=old.ratio(h)))
    # Frozen negative witness from radius-2 coordinate descent; not a global optimum.
    witness_digits=np.array([[[0, 0], [1, -1], [-1, 1], [2, -1], [-2, 1]], [[0, 0], [1, -1], [-1, 1], [2, -1], [-2, 1]], [[0, 0], [1, 0], [-1, 0], [2, 0], [-2, 0]], [[0, 0], [0, 1], [0, -1], [0, 2], [0, -2]], [[0, 0], [1, -1], [-1, 1], [2, -2], [-2, 2]], [[0, 0], [2, -2], [-2, 2], [2, -1], [-2, 1]], [[0, 0], [0, 2], [0, -2], [2, 0], [-2, 0]], [[0, 0], [0, 1], [0, -1], [0, 2], [0, -2]]],dtype=np.int64)
    wp=np.zeros((1,2),dtype=np.int64);wh=np.zeros((2,2),dtype=np.int64)
    for m,d in zip(old.MATS,witness_digits):
        assert old.complete(m,d)
        wp=((wp@m.T)[:,None,:]+d[None,:,:]).reshape(-1,2)
        wh=m@wh@m.T+d.T@d
    assert len(np.unique(wp%625,axis=0))==390625
    witness=dict(digits=witness_digits.tolist(),axis_ratio=old.ratio(wh),**old.hull_metrics(wp))
    points=np.zeros((1,2),dtype=np.int64);layers={'L0':points};rows=[];parent_checks=0
    stencil=np.array(STENCIL,dtype=np.int64)
    for k in range(8):
        p=np.array(basis(k),dtype=np.int64);previous=points
        candidates=previous[:,None,:]+(stencil@p.T)[None,:,:]
        mask=members_np(candidates,k+1)
        assert np.all(mask.sum(axis=1)==5);parent_checks+=len(previous)
        points=candidates[mask].reshape(len(previous),5,2).transpose(1,0,2).reshape(-1,2)
        assert np.array_equal(points[:len(previous)],previous) # stable old addresses
        pk=np.array(basis(k+1),dtype=np.int64);det=old.det(pk)
        assert len(points)==5**(k+1)==det
        assert len(np.unique((points@old.adj(pk).T)%det,axis=0))==len(points)
        h=len(points)*(points.T@points)-np.outer(points.sum(axis=0),points.sum(axis=0))
        hull=old.hull_metrics(points)
        assert hull['hull_total_lattice_sites']==len(points)
        if (k+1)%2==0:
            assert np.array_equal(np.unique(points,axis=0),np.unique(points@np.array(R).T,axis=0))
            assert h[0,0]==h[1,1] and 2*h[0,1]==-h[0,0]
        # An independent rectangular enumeration checks region construction.
        if k+1<=6:
            n=5**((k+1)//2);lim=3*n
            direct=np.array([(q,r) for q in range(-lim,lim+1) for r in range(-lim,lim+1) if member((q,r),k+1)],dtype=np.int64)
            assert np.array_equal(direct,np.unique(points,axis=0))
        row=dict(depth=k+1,count=len(points),cloud_axis_ratio=old.ratio(h),map_axis_ratio=5/3 if (k+1)%2 else 1,
                 max_carry_norm_sq=max(int(q*q+q*r+r*r) for (q,r),used in zip(STENCIL,mask.any(axis=0)) if used),**hull)
        rows.append(row);layers[f'L{k+1}']=points.copy();print(row,flush=True)
    rng=random.Random(60909)
    tests=[1,2,5,6,25,26,125,126,625,626,390625]+[rng.randrange(1,5**40) for _ in range(100)]
    for n in tests: assert label_of(address(n))==n
    for x in [(rng.randrange(-10**12,10**12),rng.randrange(-10**12,10**12)) for _ in range(100)]:
        assert address(label_of(x))==x
    for _ in range(100):
        n=rng.randrange(1,len(points)+1);assert address(n)==tuple(map(int,points[n-1]))
    # Boundary class frequencies are full finite data, not Monte Carlo estimates.
    assert all(member(tuple(map(int,x)),8) for x in points[::101])
    results=dict(schema='NOLLM_LOCAL_CARRY_FIELD_V1',status='CHECKED_RESEARCH_NOT_PROMOTED',
                 baseline_sha256=BASE_SHA,baseline_local_rules=baseline,radius2_negative_witness=witness,A=A,B=B,
                 matrix_convention='right-prefix nested sublattice chain; AB=5R60',
                 stencil=STENCIL,layers=rows,parent_five_child_checks=parent_checks,
                 address_roundtrips=len(tests)+100,full_array_address_checks=100,
                 limits=['radix labels are not represented by a single multiplicative similarity',
                         'two-phase matrices differ from prior frozen eight-step matrices',
                         'locality is in current lattice coordinates, not finest-grid distance',
                         'only p=5 constructed; no Nollm runtime parameter changes'])
    np.savez_compressed(out/'layers.npz',**layers)
    (out/'results.json').write_text(json.dumps(results,indent=2)+'\n')
    print(json.dumps({'status':'PASS','parents':parent_checks,'roundtrips':len(tests)+100}))
    return results

if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',type=Path,default=Path('results'))
    args=parser.parse_args();run(args.output)
