#!/usr/bin/env python3
"""Exact chart transports for rotating prime-power quotient towers (research).
No floating-point decisions; this is not a scalar-label multiplication embedding.
Run: python tower_transport.py --output results
"""
from __future__ import annotations
import argparse
import json
import random
from collections import Counter
from functools import lru_cache
from itertools import product
from pathlib import Path

I=((1,0),(0,1)); W=((0,-1),(1,1))

def mm(a,b):
    return tuple(tuple(sum(a[i][h]*b[h][j] for h in range(2)) for j in range(2)) for i in range(2))
def mv(a,x):return tuple(sum(a[i][j]*x[j] for j in range(2)) for i in range(2))
def adj(a):return ((a[1][1],-a[0][1]),(-a[1][0],a[0][0]))
def det(a):return a[0][0]*a[1][1]-a[0][1]*a[1][0]
def plus(a,b):return (a[0]+b[0],a[1]+b[1])
def scale(n,x):return (n*x[0],n*x[1])
def powm(a,t):
    out=I
    while t:
        if t&1:out=mm(out,a)
        a=mm(a,a);t//=2
    return out

def validate(p,k,l):
    if p not in (5,11) or type(k) is not int or k<0 or not 0<=l<=p:
        raise ValueError('p=5 or 11; nonnegative integer depth; line 0..p (p=vertical)')

def chi(x,l,p):return (x[0] if l==p else x[1]-l*x[0])%p
@lru_cache(None)
def active_line(p,l,t):
    v=mv(powm(W,t%3),(0,1) if l==p else (1,l))
    return p if v[0]%p==0 else v[1]*pow(v[0],-1,p)%p

@lru_cache(None)
def basis(p,k,l):
    validate(p,k,l);t=k//2;s=p**t
    if k%2==0:return ((s,0),(0,s))
    h=((p,0),(0,1)) if l==p else ((1,0),(l,p))
    a=mm(powm(W,t%6),h)
    return tuple(tuple(s*v for v in row) for row in a)

def canon(x,p,k,l):
    """Small exact coordinate representative; NOT the geometric nearest section."""
    t=k//2;s=p**t;q=x[0]%s;r=x[1]%s
    if k%2==0:return(q,r)
    line=active_line(p,l,t)
    c=chi(((x[0]-q)//s,(x[1]-r)//s),line,p)
    return (q+s*c,r) if line==p else (q,r+s*c)

def reps(p,k,l):
    validate(p,k,l);s=p**(k//2)
    if p**k>200000:raise ValueError('full enumeration limited to 200000 classes')
    if k%2==0:return list(product(range(s),repeat=2))
    line=active_line(p,l,k//2)
    return [(q+s*c,r) if line==p else (q,r+s*c)
            for q,r,c in product(range(s),range(s),range(p))]

@lru_cache(None)
def chart(l,p):
    validate(p,0,l)
    if l==p:return ((0,1),(-1,-1)),1 # -W, chi_vertical(-W x)=r
    return ((1,-l),(l,1+l)),1+l+l*l

@lru_cache(None)
def matrix(p,k,src,dst):
    """C_dst C_src^-1 modulo p^ceil(k/2); C_l=(I+l W)/norm."""
    validate(p,k,src);validate(p,k,dst)
    b,n=chart(dst,p);a,_=chart(src,p);num=mm(b,adj(a))
    m=p**((k+1)//2)
    if m==1:return ((0,0),(0,0))
    inv=pow(n,-1,m)
    return tuple(tuple(v*inv%m for v in row) for row in num)

def transport(x,p,k,src,dst):return canon(mv(matrix(p,k,src,dst),x),p,k,dst)
def project(x,p,k,l):
    if k<1:raise ValueError('cannot project below depth zero')
    return canon(x,p,k-1,l)

# A second construction: explicitly label p-adic coordinate digits. It commutes
# with truncation but need not preserve addition/carries. Kept as a contrast.
def frame(x,l,p):return (chi(x,l,p), (x[1] if l==p else x[0])%p)
def unframe(a,b,l,p):return (a,b) if l==p else (b,(a+l*b)%p)
def encode_digits(x,p,k,l):
    out=[]
    for t in range((k+1)//2):
        v=((x[0]//p**t)%p,(x[1]//p**t)%p)
        a,b=frame(v,active_line(p,l,t),p);out.append(a)
        if len(out)<k:out.append(b)
    return tuple(out)
def decode_digits(ds,p,l):
    k=len(ds);q=r=0
    for t in range((k+1)//2):
        a=ds[2*t];b=ds[2*t+1] if 2*t+1<k else 0
        u,v=unframe(a,b,active_line(p,l,t),p);q+=p**t*u;r+=p**t*v
    return canon((q,r),p,k,l)
def digit_transport(x,p,k,src,dst):return decode_digits(encode_digits(x,p,k,src),p,dst)

def run(out):
    out.mkdir(parents=True,exist_ok=True);rng=random.Random(20260910)
    rows=[];naturality=0;well_defined=0;additivity=0;composition=0;scalar_checks=0
    for p in (5,11):
        # Every chart pair through p^3, plus all p^4 classes for selected pairs.
        for k in range(1,5):
            pairs=list(product(range(p+1),repeat=2)) if k<=3 else [(0,1),(0,3),(p,2)]
            for src,dst in pairs:
                S=reps(p,k,src);T=[transport(x,p,k,src,dst) for x in S]
                assert len(set(T))==p**k
                A=basis(p,k,src)
                for v in zip(*A):
                    assert transport(v,p,k,src,dst)==(0,0);well_defined+=1
                tx=[transport(v,p,k,src,dst) for v in ((1,0),(0,1))]
                prev={z:transport(z,p,k-1,src,dst) for z in reps(p,k-1,src)}
                for x,y in zip(S,T):
                    assert project(y,p,k,dst)==prev[project(x,p,k,src)];naturality+=1
                    # Generator tests certify the finite additive map on all elements.
                    for v,tv in zip(((1,0),(0,1)),tx):
                        assert transport(canon(plus(x,v),p,k,src),p,k,src,dst)==canon(plus(y,tv),p,k,dst)
                        additivity+=1
                rows.append(dict(p=p,depth=k,source=src,target=dst,classes=len(S),fixed=sum(x==y for x,y in zip(S,T))))
        # All chart triples, matrix equality at much deeper precisions.
        for k in (1,2,3,4,10,40,101):
            modulus=p**((k+1)//2)
            for a,b,c in product(range(p+1),repeat=3):
                lhs=mm(matrix(p,k,b,c),matrix(p,k,a,b));rhs=matrix(p,k,a,c)
                assert all((lhs[i][j]-rhs[i][j])%modulus==0 for i,j in product(range(2),repeat=2));composition+=1
        # Deep samples and integer scalar compatibility (not geometric expansion).
        for _ in range(1200):
            k=rng.randrange(1,102);src=rng.randrange(p+1);dst=rng.randrange(p+1)
            m=p**((k+1)//2);x=(rng.randrange(-m,m),rng.randrange(-m,m));z=rng.randrange(-100,101)
            y=transport(x,p,k,src,dst)
            assert transport(scale(z,x),p,k,src,dst)==canon(scale(z,y),p,k,dst);scalar_checks+=1
            assert project(y,p,k,dst)==transport(project(x,p,k,src),p,k-1,src,dst);naturality+=1
    # Common even checkpoint cannot be identity under changed previous-line fibers.
    reset=dict(p=11,depth=2,source_line=0,target_line=3,x=[1,0],
               target_projection_with_identity=chi((1,0),3,11),
               transported_source_projection=transport((0,0),11,1,0,3)[1])
    assert reset['target_projection_with_identity']==8 and reset['transported_source_projection']==0
    # Exhaust GL2(Fp) mapping all three rotating source lines to target lines.
    rigid=[]
    for p in (5,11):
        accepted=[]
        for a,b,c,d in product(range(p),repeat=4):
            A=((a,b),(c,d))
            if det(A)%p==0:continue
            ok=True
            for t in range(3):
                l=active_line(p,0,t);v=(0,1) if l==p else (1,l)
                if chi(mv(A,v),active_line(p,3,t),p):ok=False;break
            if ok:
                assert ((a-1)*(d-1)-b*c)%p!=0;accepted.append(A)
        assert len(accepted)==p-1
        rigid.append(dict(p=p,matrices_examined=p**4,admissible_mod_p=p-1,all_U_minus_I_invertible=True))
    # Honest digitwise alternative and its non-additivity witness.
    digit_checks=0
    for p in (5,11):
        for k in range(1,5):
            for src,dst in [(0,3),(p,1),(2,p)]:
                for x in reps(p,k,src):
                    y=digit_transport(x,p,k,src,dst)
                    assert digit_transport(y,p,k,dst,src)==x
                    assert project(y,p,k,dst)==digit_transport(project(x,p,k,src),p,k-1,src,dst)
                    digit_checks+=1
    x=(10,0);y=(1,0);dsum=digit_transport(plus(x,y),11,4,0,3)
    sd=canon(plus(digit_transport(x,11,4,0,3),digit_transport(y,11,4,0,3)),11,4,3)
    assert dsum!=sd
    # Product CRT-square verification: refine 5 and 11; local transports commute
    # with both projections. Split-prime components are exactly unchanged.
    product_checks=0
    for a,c in [(1,1),(2,1),(1,2),(2,2),(2,3),(3,2)]:
        for x,z in product(reps(5,a,0),reps(11,c,0)):
            X=transport(x,5,a,0,2);Z=transport(z,11,c,0,3)
            via5=(transport(project(x,5,a,0),5,a-1,0,2),project(Z,11,c,3))
            via11=(project(X,5,a,2),transport(project(z,11,c,0),11,c-1,0,3))
            assert via5==via11;product_checks+=1
    # Full observer carrier: at odd depth all p+1 charts determine the next even residue.
    envelopes=[];joint_checks=0
    for p in (5,11):
        for k in range(1,5):
            m=p**((k+1)//2);X=list(product(range(m),repeat=2))
            pairs={(canon(x,p,k,0),canon(x,p,k,3)) for x in X}
            expected=p**(k+(k%2))
            assert len(pairs)==expected
            cnt=Counter(a for a,b in pairs);assert set(cnt.values())=={p if k%2 else 1}
            # all charts reconstruct from the full vector residue (no invented branch mass)
            for x in X:
                assert all(canon((x[0]+m,x[1]-2*m),p,k,l)==canon(x,p,k,l) for l in range(p+1))
                joint_checks+=1
            envelopes.append(dict(p=p,depth=k,single_classes=p**k,joint_classes=expected,
                                  missing_factor=p if k%2 else 1))
    # Forward refinements are fibers, not deterministic multiplication of a label.
    fiber_parents=0;fiber_children=0
    for p in (5,11):
        for k in range(4):
            left={x:set() for x in reps(p,k,0)}
            right={x:set() for x in reps(p,k,3)}
            for x in reps(p,k+1,0):
                left[project(x,p,k+1,0)].add(transport(x,p,k+1,0,3))
            for y in reps(p,k+1,3):right[project(y,p,k+1,3)].add(y)
            for parent,ys in left.items():
                assert len(ys)==p and ys==right[transport(parent,p,k,0,3)]
                fiber_parents+=1;fiber_children+=len(ys)
    fixed=[]
    for k in (2,4):
        S=reps(11,k,0)
        fixed.append(dict(depth=k,classes=len(S),additive_fixed=sum(transport(x,11,k,0,3)==x for x in S),
                          digitwise_fixed=sum(digit_transport(x,11,k,0,3)==x for x in S)))
    result=dict(schema='NOLLM_PRIME_POWER_CHART_TRANSPORT_V1',status='PASS_RESEARCH_NOT_PROMOTED',
                event_id='NOLLM-TOWER-CHART-TRANSPORT-20260910-C6C82',
                all_chart_pairs_through_depth=3,selected_full_pairs_at_depth=4,deep_max_depth=101,
                fully_enumerated_pair_rows=len(rows),enumerated_class_appearances=sum(r['classes'] for r in rows),
                naturality_checks=naturality,lattice_well_defined_checks=well_defined,
                additive_generator_checks=additivity,chart_cocycle_matrix_checks=composition,
                scalar_checks=scalar_checks,product_refinement_checks=product_checks,
                forward_fiber_parents=fiber_parents,forward_fiber_children=fiber_children,
                digitwise_checks=digit_checks,joint_observer_checks=joint_checks,
                source0_target3_matrix={'numerator':[[1,-3],[3,4]],'denominator':13},
                identity_reset_counterexample=reset,additive_rigidity=rigid,even_fixed_counts=fixed,
                digitwise_additivity_counterexample=dict(p=11,depth=4,x=[10,0],y=[1,0],
                    transport_of_sum=dsum,sum_of_transports=sd),
                envelopes=envelopes,
                limits=['prime-local CRT transports, not one ambient integer lattice map',
                        'identity means chart-coordinate isomorphism, not the same ambient point',
                        'natural additive transports permute even checkpoint addresses',
                        'digitwise alternative is not additive',
                        'all-depth proofs are separate from finite checks',
                        'no ordinary integer-label multiplication embedding or Nollm runtime changes'])
    (out/'results.json').write_text(json.dumps(result,indent=2)+'\n')
    (out/'pair_certificate.json').write_text(json.dumps(rows,indent=2)+'\n')
    print(json.dumps(result,indent=2),flush=True)
    return result

if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--output',type=Path,default=Path('results'))
    run(parser.parse_args().output)
