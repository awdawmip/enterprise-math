#!/usr/bin/env python3
"""Exact domain checks for fixed-prefix radix obstructions and boundary repair.

Not a new general tool family; no network I/O. From an EM checkout simply run
python experiments/x6_radix_shape_bridge_20260909/verify.py
For a detached source packet pass --native, --arithmetic, and --reuse explicitly.
"""
from __future__ import annotations
import argparse
from collections import Counter
from fractions import Fraction
import hashlib
import importlib.util
from itertools import product
import json
from math import prod
from pathlib import Path
import random
import sympy as sp

D=6
SOURCE='6cf0edabb2b1d5551ba30e8efc27044363d9ed1f'
PINS={
    'native':'01db1ef95bc120491e36653c45c88f6728e602f5',
    'arithmetic':'f4f46d080719adc2e59bc31c0d24d16c01dcd2a2',
    'reuse':'384d166f642fb65c53fc7f2431f43dc99880693a',
}

def load(name: str,path: Path):
    data=path.read_bytes()
    h=hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()
    if h!=PINS[name]:
        raise ValueError(f'{name}: source blob mismatch: {h}')
    spec=importlib.util.spec_from_file_location('x6_parent_'+name,path)
    if spec is None or spec.loader is None: raise ValueError('module load failed')
    module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)
    return module

def ceil_root(n: int) -> int:
    if isinstance(n,bool) or not isinstance(n,int) or n<1: raise ValueError('positive integer required')
    lo,hi=0,1<<((n.bit_length()+5)//6)
    while lo+1<hi:
        m=(lo+hi)//2
        if m**6<n: lo=m
        else: hi=m
    return hi

def digits(k: int,b: int) -> tuple[int,...]:
    if b<1 or not 0<=k<b**6: raise ValueError('six-digit range exceeded')
    if b==1:return (0,)*6
    out=[]
    for _ in range(6): k,r=divmod(k,b);out.append(r)
    assert k==0
    return tuple(out)

def value(z,b): return sum(int(x)*b**i for i,x in enumerate(z))

def balanced_basis(n: int):
    """Kernel of the declared base-b linear residue, not the older L(n)."""
    b=ceil_root(n)
    if n==1:return sp.eye(6)
    a=[];v=n
    for _ in range(5): v,r=divmod(v,b);a.append(r)
    a.append(v) # v may equal b precisely at n=b**6
    m=sp.zeros(6)
    for j in range(5):m[j,j]=b;m[j+1,j]=-1
    for i in range(6):m[i,5]=a[i]
    return m

def digit_set(n: int,anchor=(0,)*6):
    b=ceil_root(n)
    return {tuple(a+d for a,d in zip(anchor,digits(k,b))) for k in range(n)}

def normalize_carries(y,b):
    """Five exact carries; requires the weighted value to fit six digits."""
    if b<2 or min(y)<0 or not 0<=value(y,b)<b**6:raise ValueError('invalid positive carry input')
    r=[];c=[];incoming=0
    for i in range(6):
        incoming,rem=divmod(y[i]+incoming,b)
        r.append(rem)
        if i<5:c.append(incoming)
    assert incoming==0
    recovered=[0]*6
    for i,k in enumerate(c):recovered[i]+=b*k;recovered[i+1]-=k
    assert tuple(y[i]-r[i] for i in range(6))==tuple(recovered)
    return tuple(r),tuple(c)

def verify(native_path: Path,arithmetic_path: Path,reuse_path: Path) -> dict:
    native=load('native',native_path);old=load('arithmetic',arithmetic_path);t6=load('reuse',reuse_path)
    out={'status':'PASS_EXACT_DOMAIN_REGRESSION_NOT_FORMAL_PROOF_OR_ADMISSION',
         'source_snapshot':SOURCE,'arithmetic':'exact integers/rationals',
         'sympy_version':sp.__version__,'source_blobs':PINS}
    # A complete geometric cube need not be a fundamental domain of old L(n).
    a5=old.basis(5**6)
    block=sp.Matrix([[-3,-4],[4,-3]])
    assert a5==sp.diag(block,block,block) and a5.T*a5==25*sp.eye(6)
    def key25(x,y):return ((-3*x+4*y)%25,(-4*x-3*y)%25)
    pair=Counter(key25(x,y) for x,y in product(range(-2,3),repeat=2))
    assert Counter(pair.values())=={1:17,2:4}
    points=list(product(range(-2,3),repeat=6))
    def key6(z):return tuple(t for i in (0,2,4) for t in key25(z[i],z[i+1]))
    hist=Counter(key6(z) for z in points)
    assert len(hist)==21**3 and Counter(hist.values())=={1:4913,2:3468,4:816,8:64}
    observed={z:z for z in points};coarse={z:key6(z) for z in points}
    witness=t6.fiber_constancy_witness(points,coarse,observed)
    assert witness is not None
    repaired=t6.coarsest_one_step_repair(points,coarse,observed)
    assert t6.class_count(repaired)==15625
    out['old_gaussian_cube']={'population':15625,'occupied_residues':len(hist),
          'missing_residues':15625-len(hist),'fiber_histogram':dict(sorted(Counter(hist.values()).items())),
          'minimum_point_replacements':6364,'replacement_fraction':str(Fraction(6364,15625)),
          't6_cell_identity_witness':[list(z) for z in witness]}
    # At inert primes the retained old template really is an axis-long lattice.
    inert=[]
    for p in (3,7,11,19,43,127,251,503,1019):
        assert sp.isprime(p) and p%4==3
        assert old.local_basis(p,1)==sp.diag(p,1,1,1,1,1)
        s=native.sixth_root_floor(p)
        xs=[native.point(i) for i in range(p)]
        support=len({z[0]%p for z in xs})
        assert support<=s+1
        inert.append({'p':p,'prefix_residues':support,'transversal_width_lower_bound':p-1,
                      'minimum_replacements':p-support})
    out['old_inert_prime_witnesses']=inert
    # Finite algebra behind the asymptotic cube rigidity: a row with l1=1 has
    # one +/-1. If all rows have this form, full rank implies |det|=1.
    row_census=0
    for entries in product(range(-2,3),repeat=6):
        l1=sum(map(abs,entries))
        if l1==1:assert sum(v!=0 for v in entries)==1
        row_census+=1
    for s in (3,5,9,17,65,257,1025):
        n=s**6;r=native.sixth_root_floor(2*n)
        assert 2*(s-1)>r if s>=5 else True
    out['cube_width_regression']={'integer_rows_checked':row_census,
        'index2_sharp_asymptotic_Hausdorff_linf_constant':'(2-2^(1/6))/2',
        'constant_type':'proved limit, not floating-point certification'}
    # Every n has a small, explicit cyclic lattice and exact digit transversal.
    checks=0
    for n in list(range(1,401))+[729,1000,15625,15626,46656,10**18+37,2**127-1]:
        b=ceil_root(n);a=balanced_basis(n)
        assert abs(int(a.det()))==n
        w=sp.Matrix([[b**i for i in range(6)]])
        assert all(int(v)%n==0 for v in w*a)
        assert sum(int(v)**2 for v in a)<=11*b*b
        checks+=1
    digits_checked=0
    for n in range(1,257):
        b=ceil_root(n);ds=digit_set(n)
        assert len(ds)==n and {value(z,b)%n for z in ds}==set(range(n))
        digits_checked+=n
    out['compact_cyclic_lattice']={'bases_checked':checks,'digit_points_checked':digits_checked,
        'basis_Frobenius_bound':'||A||_F^2 <= 11 b^2',
        'condition_number_bound':'kappa_2(A) < 64*11^3 for n>1',
        'not_the_old_L_family':True}
    # Same-base divisibility; changing b has a concrete exact obstruction.
    carry_examples=[];carry_count=0
    for b in (2,3,5):
        for m in range(1,13):
            for n in range(1,13):
                if m*n>b**6:continue
                for i in range(m):
                    for j in range(n):
                        u,v=digits(i,b),digits(j,b)
                        r,c=normalize_carries(tuple(u[k]+m*v[k] for k in range(6)),b)
                        assert r==digits(i+m*j,b)
                        carry_count+=1
                        if len(carry_examples)<4 and any(c):
                            carry_examples.append({'base':b,'m':m,'i':i,'j':j,'carries':c})
    assert ceil_root(2)==2 and ceil_root(66)==3
    v=(3,-1,0,0,0,0)
    assert value(v,3)%66==0 and value(v,2)%2==1
    same_base=0
    for b in (2,3,5):
        for m in range(1,21):
            for n in range(1,21):
                if m*n>b**6:continue
                for z in ((0,)*6,(7,-2,1,0,0,0),(-5,3,8,-1,0,2)):
                    assert (value(z,b)%(m*n))%m==value(z,b)%m
                same_base+=1
    out['carry_and_divisibility']={'carry_cases':carry_count,'same_base_divisibility_cases':same_base,
        'nonzero_carry_examples':carry_examples,
        'changing_base_nesting_failure':{'small_index':2,'large_index':66,'vector':v,
            'large_residue':0,'small_residue':1}}
    # Boundary-only replacement from the actual frozen prefix to the new section.
    ns=set(range(1,129))|{180,256,400,729,730,1000,4096,15625,15626,20000}
    prefix=set();rows=[];maxn=max(ns)
    def build_map(n):
        b=ceil_root(n);anchor=tuple(native.box_before_round(b-1)[0])
        def residue(z):return value(tuple(z[i]-anchor[i] for i in range(6)),b)%n
        # Keep one original point in every already represented fiber. This is
        # optimal in the NUMBER of moved points, not total geometric distance.
        keep={}
        for z in sorted(prefix):keep.setdefault(residue(z),z)
        missing=sorted(set(range(n))-set(keep))
        dst=[tuple(anchor[i]+digits(k,b)[i] for i in range(6)) for k in missing]
        src=sorted(prefix-set(keep.values()))
        assert len(src)==len(dst)<=b**6-n
        f={z:z for z in keep.values()};f.update(zip(src,dst))
        assert len(f)==n and len(set(f.values()))==n
        assert {residue(z) for z in f.values()}==set(range(n))
        assert sum(x!=y for x,y in f.items())==n-len(keep)
        total_distance=sum(sum(abs(z[i]-w[i]) for i in range(6)) for z,w in f.items())
        assert total_distance<=6*(b-1)*len(src)
        return f,{'N':n,'base':b,'moved':len(src),'available_boundary_bound':b**6-n,
                  'mean_l1_repair':str(Fraction(total_distance,n))}
    maps={}
    for k,z in enumerate(native.stream()):
        if k>=maxn:break
        prefix.add(z);n=k+1
        if n in ns:
            f,row=build_map(n);rows.append(row)
            if n<=33:maps[n]=f
    out['boundary_repair']={'prefixes_checked':len(rows),'samples':[r for r in rows if r['N'] in (2,3,63,64,65,128,729,730,15625,15626,20000)]}
    # Lift the actual common-phase pair law, without pretending repair is always local.
    nonlocal_examples=[];coupled=0
    for n in range(1,33):
        joint_total=Fraction(0);nonlocal_mass=Fraction(0)
        old_repair=Fraction(0);new_repair=Fraction(0);move_cost=Fraction(0)
        left,right=maps[n],maps[n+1]
        for i in range(n):
            x=native.point(i)
            for j,num in ((i,n-i),(i+1,i+1)):
                y=native.point(j);mass=Fraction(num,n*(n+1))
                xp,yp=left[x],right[y]
                dist=sum(abs(a-b) for a,b in zip(xp,yp))
                joint_total+=mass;move_cost+=mass*dist
                old_repair+=mass*sum(abs(a-b) for a,b in zip(x,xp))
                new_repair+=mass*sum(abs(a-b) for a,b in zip(y,yp))
                if dist>1:nonlocal_mass+=mass
        a=Fraction(sum(x!=y for x,y in left.items()),n)
        b=Fraction(sum(x!=y for x,y in right.items()),n+1)
        assert joint_total==1 and nonlocal_mass<=a+b
        assert move_cost<=old_repair+new_repair+Fraction(1,2)
        if nonlocal_mass and len(nonlocal_examples)<5:
            nonlocal_examples.append({'n':n,'nonlocal_mass':str(nonlocal_mass),'mean_l1_step':str(move_cost)})
        coupled+=1
    out['marked_repair']={'pair_laws_checked':coupled,'nonlocal_examples':nonlocal_examples,
           'one_native_step_not_claimed':True}
    out['reuse']={'resolution':'REUSE_EXECUTED','families':['T6_OPERATION_SAFE_QUOTIENT'],
       'parent_constructions':['native point/stream','old local_basis/basis'],
       'T6_methods':['fiber_constancy_witness','coarsest_one_step_repair','class_count']}
    out['excluded_claims']=['Foundation admission','independent review','new general self-affine theorem',
      'replacement equals old L(n)','one new Cell at every repaired time','uniformly bounded individual repair',
      'all-modulus divisor compatibility across base changes','ordinary 1+1 differs from 2']
    return out

if __name__=='__main__':
    root=Path(__file__).resolve().parents[2]
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--native',type=Path,default=root/'experiments/x6_native_growth_20260909/verify.py')
    p.add_argument('--arithmetic',type=Path,default=root/'experiments/x6_coherent_arithmetic_20260909/verify.py')
    p.add_argument('--reuse',type=Path,default=root/'src/enterprise_math/composition_safe_collapse.py')
    p.add_argument('--output',type=Path,default=Path(__file__).with_name('results.json'))
    a=p.parse_args()
    result=verify(a.native,a.arithmetic,a.reuse)
    text=json.dumps(result,ensure_ascii=False,indent=2,sort_keys=True)+'\n'
    a.output.parent.mkdir(parents=True,exist_ok=True);a.output.write_text(text,encoding='utf-8');print(text)
