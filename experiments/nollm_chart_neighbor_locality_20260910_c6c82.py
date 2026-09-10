#!/usr/bin/env python3
"""Exact neighborhood audit of the rotating prime-power chart transports.
Research-only ordinary hex lattice slice; not scalar-label multiplication.
Requires numpy and the unchanged tower_transport.py alongside, or bundled prior/.
Run: python experiment.py --output results
"""
from __future__ import annotations
import argparse, hashlib, importlib.util, json, math, sys
from fractions import Fraction
from itertools import product
from pathlib import Path
from collections import Counter
import numpy as np
ROOT=Path(__file__).resolve().parent
PIN='f6f80926e626944203e4537345737bc64c470190d9da32f14290b907fbe2cb47'
FILES=[ROOT/'tower_transport.py',ROOT/'nollm_prime_power_chart_transport_20260910_c6c82.py',
       ROOT/'prior/nollm_prime_power_chart_transport/tower_transport.py']
pth=next((p for p in FILES if p.exists()),None)
if pth is None:raise FileNotFoundError('unchanged prime-power predecessor required')
if hashlib.sha256(pth.read_bytes()).hexdigest()!=PIN:raise ValueError('predecessor hash mismatch')
spec=importlib.util.spec_from_file_location('tower_predecessor',pth)
t=importlib.util.module_from_spec(spec);sys.modules[spec.name]=t;spec.loader.exec_module(t)
D=np.array([(1,0),(0,1),(-1,1),(-1,0),(0,-1),(1,-1)],dtype=np.int64)
C=np.array([[-4,1],[21,-5]],dtype=np.int64)
CI=np.array([[5,1],[21,4]],dtype=np.int64)

def qnorm(x):q,r=map(int,x);return q*q+q*r+r*r
def hop(x):q,r=map(int,x);return max(abs(q),abs(r),abs(q+r))
def torus_metric(x,m,word=False):
    """Squared Euclidean hex norm, or graph distance, minimized over period lifts.
    Residues lie in [0,m)^2. A closest lift occurs among the 3x3 neighboring
    translates; enlarging to 5x5 is independently checked in run().
    """
    x=np.asarray(x,dtype=np.int64)%m
    best=np.full(x.shape[:-1],10*m*m,dtype=np.int64)
    for i,j in product((-1,0,1),repeat=2):
        q=x[...,0]+i*m;r=x[...,1]+j*m
        v=np.maximum.reduce([abs(q),abs(r),abs(q+r)]) if word else q*q+q*r+r*r
        best=np.minimum(best,v)
    return best

def image_table(p,k,kind):
    m=p**(k//2)
    X=np.array(t.reps(p,k,0),dtype=np.int64)
    if kind=='additive':Y=(X@np.array(t.matrix(p,k,0,3),dtype=np.int64).T)%m
    elif kind=='digit':Y=np.array([t.digit_transport(tuple(map(int,x)),p,k,0,3) for x in X],dtype=np.int64)
    elif kind=='bounded_lift':Y=(X@C.T)%m
    else:raise ValueError(kind)
    assert len(np.unique(Y,axis=0))==len(X)
    # predecessor even representatives are q-major/r-minor
    assert np.all(X[:,0]*m+X[:,1]==np.arange(len(X)))
    return X,Y

def explicit_edges(p,k,kind):
    m=p**(k//2);X,Y=image_table(p,k,kind);retained=0;sumq=0;maxhop=0;n=len(X)
    push_checks=0
    for d in D:
        nb=(X+d)%m;ids=nb[:,0]*m+nb[:,1]
        dif=(Y[ids]-Y)%m;qs=torus_metric(dif,m)
        retained+=int((qs==1).sum());sumq+=int(qs.sum())
        maxhop=max(maxhop,int(torus_metric(dif,m,True).max()))
        if kind!='digit':
            A=np.array(t.matrix(p,k,0,3),dtype=np.int64) if kind=='additive' else C
            assert np.all(dif==(A@d)%m);push_checks+=n
    disp=(Y-X)%m;distq=torus_metric(disp,m)
    return dict(p=p,depth=k,kind=kind,classes=n,directed_edges=6*n,
                retained_edges=retained,retained_fraction=str(Fraction(retained,6*n)),
                mean_edge_Q=str(Fraction(sumq,6*n)),max_edge_hops=maxhop,
                fixed=int(np.all(Y==X,axis=1).sum()),
                mean_migration_Q=str(Fraction(int(distq.sum()),n)),
                transported_edge_checks=push_checks)

def ambient_moments(m):
    total=0;totalhop=0;hist=Counter()
    for q in range(m):
        X=np.column_stack((np.full(m,q,dtype=np.int64),np.arange(m,dtype=np.int64)))
        qs=torus_metric(X,m);total+=int(qs.sum());totalhop+=int(torus_metric(X,m,True).sum())
        if m<=121:hist.update(map(int,qs))
    return total,totalhop,hist

def lift_cost(A):
    AA=tuple(tuple(map(int,row)) for row in A)
    Ad=np.array(t.adj(AA),dtype=np.int64)
    return max(map(hop,np.vstack((D@A.T,D@Ad.T))))

def exhaust_lifts(bound):
    """Complete certificate inside an edge-hop budget.
    Hop(C e_i)<=bound implies every entry of C is in [-bound,bound].
    The three rotating-line constraints make C mod 11 a nonzero scalar times U.
    For this pair determinant +/-1 permits only scalars 3,8 and determinant -1.
    Enumeration solves for the fourth entry exactly; first entry is never 0 mod11.
    """
    U=np.array(t.matrix(11,2,0,3),dtype=np.int64);rows=[];best=10**9
    scalar_cases=[]
    for c in range(1,11):
        R=(c*U)%11
        ds=[z for z in (-1,1) if t.det(tuple(map(tuple,R)))%11==z%11]
        for determinant in ds:
            scalar_cases.append([c,determinant])
            ar=[v for v in range(-bound,bound+1) if v%11==R[0,0]]
            br=[v for v in range(-bound,bound+1) if v%11==R[0,1]]
            cr=[v for v in range(-bound,bound+1) if v%11==R[1,0]]
            for a,b,cc in product(ar,br,cr):
                if a==0:raise AssertionError('not possible for these residue cases')
                rhs=determinant+b*cc
                if rhs%a:continue
                d=rhs//a
                if abs(d)>bound or d%11!=R[1,1]:continue
                A=np.array([[a,b],[cc,d]],dtype=np.int64);co=lift_cost(A)
                if co<=bound:
                    rows.append(dict(scalar=c,det=determinant,matrix=A.tolist(),hop_bound=co));best=min(best,co)
    return dict(entry_bound=bound,scalar_cases=scalar_cases,admissible_rows=rows,
                best=None if not rows else best)

def run(out):
    out.mkdir(parents=True,exist_ok=True)
    assert t.mm(tuple(map(tuple,C)),tuple(map(tuple,CI)))==t.I
    assert t.det(tuple(map(tuple,C)))==-1
    assert np.array_equal(C%11,3*np.array(t.matrix(11,2,0,3))%11)
    all_pairs=[];rotation_class_checks=0
    for p in (5,11):
        for src,dst in product(range(p+1),repeat=2):
            for n in (1,2,3):
                mod=p**n;A=np.array(t.matrix(p,2*n,src,dst),dtype=np.int64)
                ds=(D@A.T)%mod;ret=int((torus_metric(ds,mod)==1).sum())
                assert ret in (0,6)
                orbit={t.active_line(p,src,j) for j in range(3)}
                if dst not in orbit:assert ret==0;rotation_class_checks+=1
                all_pairs.append(dict(p=p,source=src,target=dst,t=n,retained_generators=ret))
    # Full population metrics, not plots or sampling.
    edge_rows=[]
    for p in (5,11):
        for k in (2,4):
            for kind in ('additive','digit'):
                edge_rows.append(explicit_edges(p,k,kind))
    for k in (2,4):edge_rows.append(explicit_edges(11,k,'bounded_lift'))
    # Distances at larger populations can be reduced by translation invariance.
    scales=[]
    for p in (5,11):
        for n in (1,2,3):
            mod=p**n;A=np.array(t.matrix(p,2*n,0,3),dtype=np.int64)
            inv=np.array(t.matrix(p,2*n,3,0),dtype=np.int64)
            total,th,_=ambient_moments(mod)
            assert t.det(tuple(map(tuple,A-np.eye(2,dtype=np.int64))))%p!=0
            for j in range(6):
                R=np.array(t.powm(t.W,j),dtype=np.int64)
                assert t.det(tuple(map(tuple,A-R)))%p!=0
            steps=(D@A.T)%mod
            scales.append(dict(p=p,t=n,period=mod,classes=mod**2,
                 forward_edge_Q=list(map(int,torus_metric(steps,mod))),
                 forward_edge_hops=list(map(int,torus_metric(steps,mod,True))),
                 inverse_edge_hops=list(map(int,torus_metric(D@inv.T,mod,True))),
                 mean_migration_Q=str(Fraction(total,mod**2)),
                 normalized_RMS=math.sqrt(total/mod**4),mean_migration_hops=str(Fraction(th,mod**2))))
            if mod<=121:
                X,Y=image_table(p,2*n,'additive')
                # Every displacement occurs once, even after any global hex rotation.
                for j in range(6):
                    R=np.array(t.powm(t.W,j),dtype=np.int64)
                    d=(Y-X@R.T)%mod
                    assert len(np.unique(d,axis=0))==mod**2
                    assert int(torus_metric(d,mod).sum())==total
    # Unchanged source transport versus seven-site nearest patch.
    mod=11;X,Y=image_table(11,2,'additive');U=np.array(t.matrix(11,2,0,3),dtype=np.int64)
    patch=np.vstack((np.zeros((1,2),dtype=np.int64),D))%mod
    dest=(patch@U.T)%mod
    def within(S,gens):
        SS=set(map(tuple,S));return sum(tuple((v+d)%mod) in SS for v in S for d in gens)//2
    patch_stats=dict(points=7,source_internal_edges=within(patch,D),
                     target_internal_edges_fixed_hex=within(dest,D),
                     target_internal_edges_transported=within(dest,(D@U.T)%mod),
                     source=patch.tolist(),destination=dest.tolist())
    assert [patch_stats[z] for z in ('source_internal_edges','target_internal_edges_fixed_hex','target_internal_edges_transported')]==[12,0,12]
    # Exactly conjugate message-passing; deterministic arbitrary integer signal.
    f=(np.arange(mod*mod,dtype=np.int64)*37+19)%101;g=np.empty_like(f)
    g[Y[:,0]*mod+Y[:,1]]=f
    def aggregate(vals,gens):
        out=np.zeros_like(vals)
        for d in gens:
            N=(X+d)%mod;out+=vals[N[:,0]*mod+N[:,1]]
        return out
    af=aggregate(f,D);ag=aggregate(g,(D@U.T)%mod)
    assert np.array_equal(af,ag[Y[:,0]*mod+Y[:,1]])
    fixed_wrong=aggregate(g,D)
    wrong=int((af!=fixed_wrong[Y[:,0]*mod+Y[:,1]]).sum())
    # Two-sided finite-hop lift proof witness; all-depth membership from three mod-p lines.
    for j in range(3):
        la=t.active_line(11,0,j);lb=t.active_line(11,3,j)
        v=(0,1) if la==11 else (1,la)
        assert t.chi(t.mv(tuple(map(tuple,C)),v),lb,11)==0
    natural_checks=0;new_norm=0;scalarchecks=0
    CT=tuple(tuple(map(int,row)) for row in C)
    for k in range(1,5):
        S=t.reps(11,k,0);images=set()
        for x in S:
            y=t.canon(t.mv(CT,x),11,k,3);images.add(y)
            assert t.project(y,11,k,3)==t.canon(t.mv(CT,t.project(x,11,k,0)),11,k-1,3)
            natural_checks+=1
            if k==1:assert t.chi(y,3,11)==3*t.chi(x,0,11)%11;new_norm+=1
        assert len(images)==11**k
    # For any t these modular matrices have the same bounded integer lift.
    deep=[]
    for n in (1,2,3,6,12,50):
        mm=11**n
        # No large population enumeration: verify both exact lattice inclusions.
        generator_cases=0
        for k in (2*n,2*n+1):
            for A,src,dst in ((CT,0,3),(tuple(tuple(map(int,row)) for row in CI),3,0)):
                Ps=t.basis(11,k,src);Pt=t.basis(11,k,dst)
                test=t.mm(t.adj(Pt),t.mm(A,Ps));den=t.det(Pt)
                assert all(v%den==0 for row in test for v in row)
                generator_cases+=1
        deep.append(dict(t=n,period=str(mm),exact_lattice_generator_cases=generator_cases,forward_and_inverse_bound=26))
    cert25=exhaust_lifts(25);cert26=exhaust_lifts(26)
    assert cert25['best'] is None and cert26['best']==26
    assert C.tolist() in [r['matrix'] for r in cert26['admissible_rows']]
    # Determinant-residue barriers to a uniformly bounded two-sided compatible lift.
    obstacles=[]
    for p in (5,11):
        d=t.det(t.matrix(p,2,0,3))%p
        attainable=sorted({(c*c*d)%p for c in range(1,p)})
        allowed=sorted(set(attainable)&{1,p-1})
        obstacles.append(dict(p=p,normalized_det_mod_p=d,exact_labels_allow_unimodular=d in (1,p-1),
                              arbitrary_scalar_determinants=attainable,unimodular_signs_mod_p=allowed))
    assert obstacles[0]['unimodular_signs_mod_p']==[]
    assert obstacles[1]['unimodular_signs_mod_p']==[10]
    # Metric guard: for small full tori compare neighboring translates to larger boxes.
    metricchecks=0
    for mod in (5,11,25):
        X=np.array(list(product(range(mod),repeat=2)),dtype=np.int64)
        for word in (False,True):
            B=np.full(len(X),10*mod*mod,dtype=np.int64)
            for i,j in product(range(-2,3),repeat=2):
                q=X[:,0]+i*mod;r=X[:,1]+j*mod
                val=np.maximum.reduce([abs(q),abs(r),abs(q+r)]) if word else q*q+q*r+r*r
                B=np.minimum(B,val)
            assert np.array_equal(B,torus_metric(X,mod,word));metricchecks+=len(X)
    result=dict(schema='NOLLM_CHART_NEIGHBOR_LOCALITY_V1',status='PASS_RESEARCH_NOT_PROMOTED',
      event_id='NOLLM-NEIGHBOR-LOCALITY-20260910-C6C82',predecessor_sha256=PIN,
      population='even quotient tori (Z/p^t Z)^2 with all six physical hex edges',
      edge_rows=edge_rows,scales=scales,all_pair_rows=len(all_pairs),cross_rotation_orbit_checks=rotation_class_checks,
      patch=patch_stats,message_passing_exact_rows=121,message_passing_wrong_fixed_graph_rows=wrong,
      lift=dict(matrix=C.tolist(),inverse=CI.tolist(),determinant=-1,first_digit_multiplier=3,
                two_sided_hop_bound=26,optimal_within_declared_integer_lifts=True,
                no_solution_under_26=cert25['best'] is None,naturality_full_classes=natural_checks,
                finite_deep_certificates=deep),determinant_obstacles=obstacles,metric_crosschecks=metricchecks,
      limits=['ordinary research hex slice; not native Nollm implementation',
              'geometric nearest neighbors are a proxy, no semantic data tested',
              'additive/digit transports preserve different contracts',
              '26-hop lift changes first numerical labels by factor 3 and reverses orientation',
              '26 is only optimal among additive natural integer-unimodular lifts for this chart pair',
              'single 11-tower locality is not global coprime-plane locality',
              'transported six ports preserve graph degree, not physical one-hop cost',
              'no integer-label multiplicative embedding or theorem promotion'])
    (out/'results.json').write_text(json.dumps(result,indent=2)+'\n')
    (out/'pair_edges.json').write_text(json.dumps(all_pairs,indent=2)+'\n')
    (out/'lift_certificate.json').write_text(json.dumps({'excluded':cert25,'attained':cert26},indent=2)+'\n')
    np.savez_compressed(out/'patch.npz',source=patch,destination=dest)
    print(json.dumps({k:result[k] for k in ('status','all_pair_rows','cross_rotation_orbit_checks','patch','lift','determinant_obstacles','metric_crosschecks')},indent=2))
    return result
if __name__=='__main__':
    ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--output',type=Path,default=ROOT/'results')
    run(ap.parse_args().output)
