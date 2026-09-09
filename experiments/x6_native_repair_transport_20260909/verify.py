#!/usr/bin/env python3
"""Exact-certificate domain experiment: native coset repair transport.

SciPy proposes an assignment; integer dual inequalities independently certify
its optimality. No claim of a new matching algorithm or native dynamics.
"""
from __future__ import annotations
import argparse
from collections import Counter, deque
from fractions import Fraction
import hashlib
import importlib.util
from itertools import permutations, product
import json
from pathlib import Path
import numpy as np
import scipy
from scipy.optimize import linear_sum_assignment

PIN = '01db1ef95bc120491e36653c45c88f6728e602f5'
T6_PIN = '384d166f642fb65c53fc7f2431f43dc99880693a'

def load(path: Path, expected: str, name: str):
    raw = path.read_bytes()
    sha = hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest()
    if sha != expected:
        raise ValueError(f'Pinned source mismatch: {path}: {sha}')
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

def certified_assignment(cost):
    """Return permutation and integer primal/dual certificate; fail closed."""
    c = np.asarray(cost, dtype=np.int64)
    if c.ndim != 2 or c.shape[0] != c.shape[1] or np.any(c < 0):
        raise ValueError('nonnegative square integer costs required')
    n = c.shape[0]
    if not n:
        return [], 0, {'alpha': [], 'beta': [], 'dual_value': 0}
    _, perm = linear_sum_assignment(c)
    chosen = c[np.arange(n), perm]
    beta = np.zeros(n, dtype=np.int64)
    # beta[j] - beta[perm[i]] <= c[i,j]-c[i,perm[i]].
    for _ in range(n):
        nxt = np.minimum(beta, np.min(beta[perm,None]+c-chosen[:,None],axis=0))
        if np.array_equal(nxt, beta):
            break
        beta = nxt
    else:
        raise AssertionError('No stable integral dual; candidate is not certified')
    alpha = chosen-beta[perm]
    assert np.all(alpha[:,None]+beta[None,:] <= c)
    assert np.all(alpha+beta[perm] == chosen)
    value = sum(map(int,chosen))
    assert value == sum(map(int,alpha))+sum(map(int,beta))
    return list(map(int,perm)), value, {'alpha':list(map(int,alpha)),
        'beta':list(map(int,beta)), 'dual_value':value}

def cyclic_geometry(n: int, generators):
    if n < 1:
        raise ValueError('positive order required')
    moves = sorted(set(int(x)%n for x in generators)|set(-int(x)%n for x in generators))
    dist = [-1]*n
    parent = [None]*n
    dist[0] = 0
    queue = deque([0])
    while queue:
        x=queue.popleft()
        for g in moves:
            y=(x+g)%n
            if dist[y]<0:
                dist[y]=dist[x]+1; parent[y]=(x,g); queue.append(y)
    if min(dist)<0:
        raise ValueError('generators do not generate the quotient')
    return np.array(dist,dtype=np.int64), parent

def repair_case(labels, generators):
    labels=np.array(labels,dtype=np.int64)
    n=len(labels)
    labels %= n
    dist,_=cyclic_geometry(n,generators)
    cost=dist[(np.arange(n)[None,:]-labels[:,None])%n]
    perm, total, cert=certified_assignment(cost)
    counts=Counter(map(int,labels))
    surplus=[c for c,a in sorted(counts.items()) for _ in range(a-1)]
    missing=[c for c in range(n) if c not in counts]
    small=dist[(np.array(missing,dtype=np.int64)[None,:]
                 -np.array(surplus,dtype=np.int64)[:,None])%n]
    small_perm, small_total,_=certified_assignment(small)
    assert small_total==total
    # All already represented fibers can retain one original point at zero cost.
    fixed=set(); reconstructed=[]; idx=0
    for c in map(int,labels):
        if c not in fixed:
            fixed.add(c); reconstructed.append(c)
        else:
            # Match grouped surplus occurrences back to their assigned targets.
            reconstructed.append(None)
    by_class={}
    for k,c in enumerate(surplus):
        by_class.setdefault(c,deque()).append(missing[small_perm[k]])
    for i,c in enumerate(map(int,labels)):
        if reconstructed[i] is None:
            reconstructed[i]=by_class[c].popleft()
    assert len(set(reconstructed))==n
    assert sum(int(cost[i,c]) for i,c in enumerate(reconstructed))==total
    assert sum(c!=int(labels[i]) for i,c in enumerate(reconstructed))==len(missing)
    return {'n':n,'support':len(counts),'minimum_moved':len(missing),
            'minimum_total_unit_distance':total,'mean_unit_distance':str(Fraction(total,n)),
            'quotient_diameter':int(max(dist))}, cert, cost

def boxed_case(points, walk):
    """Exact best endpoint cost with all representatives inside the next box."""
    n=len(points)
    s=walk.sixth_root_floor(n); b=s if s**6==n else s+1
    lo,hi,_=walk.box_before_round(b-1)
    box=np.array(list(product(*(range(lo[i],hi[i]+1) for i in range(6)))),dtype=np.int64)
    coeff=np.array([b**i for i in range(6)],dtype=np.int64)
    lab=((box-np.array(lo))@coeff)%n
    distances=np.abs(np.array(points)[:,None,:]-box[None,:,:]).sum(axis=2)
    cost=np.empty((n,n),dtype=np.int64)
    for c in range(n):
        mask=(lab==c)
        assert np.any(mask)
        cost[:,c]=distances[:,mask].min(axis=1)
    _,value,_=certified_assignment(cost)
    return value

def verify(root: Path):
    walk=load(root/'experiments/x6_native_growth_20260909/verify.py',PIN,'repair_walk')
    t6=load(root/'src/enterprise_math/composition_safe_collapse.py',T6_PIN,'repair_t6')
    rows=[]; certificates=[]; boxed=[]
    indices=list(range(2,81))+[96,127,128,129,180,251,256,257,511,512,513,728,729,730]
    for n in indices:
        pts=[walk.point(k) for k in range(n)]
        s=walk.sixth_root_floor(n); b=s if s**6==n else s+1
        coeff=[b**i for i in range(6)]
        labels=[sum(a*x for a,x in zip(coeff,z))%n for z in pts]
        row,cert,_=repair_case(labels,coeff)
        row['family']='adaptive_cyclic'; row['base']=b; rows.append(row)
        if n in (3,7,31,65,67,127,257,730):
            certificates.append({'family':'adaptive_cyclic','n':n,**cert})
        if n in (3,7,31,63,64,65,66,67,80,127):
            bounded=boxed_case(pts,walk)
            assert bounded>=row['minimum_total_unit_distance']
            boxed.append({'n':n,'unrestricted_cost':row['minimum_total_unit_distance'],
                          'next_box_cost':bounded})
    inert_primes=[3,7,11,19,31,43,67,127,251,503]
    inert=[]
    for p in inert_primes:
        pts=[walk.point(k) for k in range(p)]
        labels=[z[0]%p for z in pts]
        row,cert,_=repair_case(labels,[1])
        baseline=p*p//4
        bound=sum(min(z[0]%p,(-z[0])%p) for z in pts)
        w=row['minimum_total_unit_distance']
        assert baseline-bound<=w<=baseline+bound
        row.update(family='old_and_conjugate_inert_first_step',baseline=baseline,
                   exact_error_bound=bound)
        inert.append(row)
        if p in (3,7,31,67,127,503):
            certificates.append({'family':'inert_axis','n':p,**cert})
    # Independent exhaustive small-population assignment verification.
    brute=0; hall_checks=0
    for n in range(2,7):
        for shift in range(n):
            labels=[(k*k+shift)%n for k in range(n)]
            row,_,cost=repair_case(labels,[1])
            perms=list(permutations(range(n)))
            values=[sum(int(cost[i,p[i]]) for i in range(n)) for p in perms]
            assert min(values)==row['minimum_total_unit_distance']; brute+=len(perms)
            bottleneck=min(max(int(cost[i,p[i]]) for i in range(n)) for p in perms)
            counts=Counter(labels)
            for r in range(n):
                hall=True
                for mask in range(1<<n):
                    a=[i for i in range(n) if mask>>i&1]
                    neighbors={j for i in a for j in range(n)
                               if min((j-i)%n,(i-j)%n)<=r}
                    if sum(counts[i] for i in a)>len(neighbors):
                        hall=False; break
                assert hall==(bottleneck<=r); hall_checks+=1
    # Same total optimum, conflicting minimum-moved and bottleneck objectives.
    labels=[0,0,1,2,3,5,6,7]
    toy,_,cost=repair_case(labels,[1])
    assert toy['minimum_moved']==1 and toy['minimum_total_unit_distance']==4
    relay_targets=[1,0,2,3,4,5,6,7]
    assert len(set(relay_targets))==8
    assert max(int(cost[i,j]) for i,j in enumerate(relay_targets))==1
    assert sum(int(cost[i,j]) for i,j in enumerate(relay_targets))==4
    # Native single-step, no-collision realization of the four-token relay.
    positions=[0,8,1,2,3,5,6,7]
    for i in (4,3,2,0):
        positions[i]+=1
        assert len(set(positions))==8
    assert len({x%8 for x in positions})==8
    # Scope-typed BRC/T6: quotient cost descends; boxed costs need not.
    domain=(0,8); coarse={0:0,8:0}
    assert t6.descends_through(domain,coarse,{0:1,8:1})
    assert t6.fiber_constancy_witness(domain,coarse,{0:1,8:7})==(0,8)
    return {'status':'PASS_INTEGER_PRIMAL_DUAL_CERTIFICATES_NOT_FORMAL_OR_ADMITTED',
        'scipy_version':scipy.__version__,'cost_unit':'native signed unit steps / l1',
        'adaptive_cases':rows,'inert_cases':inert,'boxed_cases':boxed,
        'brute_assignment_candidates':brute,'hall_radius_checks':hall_checks,
        'relay_example':{'minimum_moved':1,'distance_if_only_one_moved':4,
            'optimal_total_distance':4,'unit_relay_moves':4,'bottleneck':1},
        'saved_dual_certificates':certificates,
        'reuse':{'walk_blob':PIN,'t6_blob':T6_PIN,'assignment':'scipy.optimize.linear_sum_assignment'},
        'boundaries':['unrestricted theorem allows final representatives anywhere',
                      'next-box case has a separately declared cost matrix',
                      'unit repair changes internal time and may move incumbents',
                      'no all-integer compact divisor-compatible filtration constructed']}

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--source-root',type=Path,default=Path(__file__).resolve().parents[2])
    parser.add_argument('--output',type=Path)
    parser.add_argument('--full-output',type=Path)
    args=parser.parse_args(); full=verify(args.source_root)
    if args.full_output:
        args.full_output.parent.mkdir(parents=True,exist_ok=True)
        args.full_output.write_text(json.dumps(full,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    chosen={3,7,31,65,67,127,251,257,730}
    result={'status':full['status'],'scipy_version':full['scipy_version'],
        'cost_unit':full['cost_unit'], 'adaptive_case_count':len(full['adaptive_cases']),
        'inert_case_count':len(full['inert_cases']),
        'adaptive_selected':[x for x in full['adaptive_cases'] if x['n'] in chosen],
        'inert_selected':full['inert_cases'], 'boxed_cases':full['boxed_cases'],
        'brute_assignment_candidates':full['brute_assignment_candidates'],
        'hall_radius_checks':full['hall_radius_checks'], 'relay_example':full['relay_example'],
        'saved_dual_certificates':[c for c in full['saved_dual_certificates'] if c['n']==67],
        'reuse':full['reuse'], 'boundaries':full['boundaries']}
    text=json.dumps(result,ensure_ascii=False,separators=(',',':'))+'\n'
    if args.output:
        args.output.parent.mkdir(parents=True,exist_ok=True)
        args.output.write_text(text,encoding='utf-8')
    print(text)
if __name__=='__main__': main()
