#!/usr/bin/env python3
"""Exact X6 domain experiment: a cyclotomic ideal lattice compatibility bridge.

This is not a new generic tool or a native rotation law. The retained native
metric is sum of six coordinate squares. Run from any directory with:
python verify.py --source-root /path/to/enterprise-math --output results.json
Requires SymPy, NumPy and the pinned existing repair/path/T6 source files.
"""
from __future__ import annotations
import argparse
from collections import Counter, deque
from fractions import Fraction
from functools import lru_cache
import hashlib
import importlib.util
from itertools import product
import json
from pathlib import Path
import random
import warnings
import numpy as np
import sympy as sp
from sympy.matrices.normalforms import hermite_normal_form as hnf

SOURCE = 'e59f44244bce8745cb806e5331b183f6666615ae'
PINS = {
 'walk': ('experiments/x6_native_growth_20260909/verify.py', '01db1ef95bc120491e36653c45c88f6728e602f5'),
 't6': ('src/enterprise_math/composition_safe_collapse.py', '384d166f642fb65c53fc7f2431f43dc99880693a'),
 'transport': ('experiments/x6_native_repair_transport_20260909/verify.py', 'd614aada84c281ec722c2dc8165d7484b0a17a38'),
}
X = sp.Symbol('x')
PHI = sp.Poly(sum(X**i for i in range(7)), X)
U = sp.zeros(6)
for i in range(5): U[i+1,i] = 1
for i in range(6): U[i,5] = -1
G = 7*sp.eye(6)-sp.ones(6)
EYE = sp.eye(6)

def load(root, key):
    rel, expected = PINS[key]
    raw = (root/rel).read_bytes()
    got = hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest()
    if got != expected: raise ValueError(f'Pinned source mismatch: {rel}: {got}')
    spec = importlib.util.spec_from_file_location('cyc7_'+key, root/rel)
    module = importlib.util.module_from_spec(spec); spec.loader.exec_module(module)
    return module

def imat(m): return [[int(v) for v in m.row(i)] for i in range(m.rows)]

def integral(m): return all(v.q == 1 for v in m)

def multiply(a,b):
    out = [0]*11
    for i in range(6):
        for j in range(6): out[i+j] += int(a[i])*int(b[j])
    for k in range(10,5,-1):
        v = out[k]
        for j in range(6): out[k-6+j] -= v
    return sp.Matrix(out[:6])

def ideal_product(a,b):
    return hnf(sp.Matrix.hstack(*(multiply(a[:,i],b[:,j]) for i in range(6) for j in range(6))))

def residue_degree(p):
    if p == 7: return 1
    if not sp.isprime(p): raise ValueError('prime required')
    f=1
    while pow(p,f,7) != 1: f += 1
    return f

@lru_cache(None)
def prime_ideal(p):
    if p==7: return hnf(EYE-U)
    with warnings.catch_warnings():
        warnings.simplefilter('ignore')
        factors=sp.factor_list(PHI, modulus=p)[1]
    polys=[]
    for poly,_ in factors:
        cs=tuple(int(poly.nth(i))%p for i in range(poly.degree()+1))
        polys.append(cs)
    cs=min(polys)
    assert len(cs)-1 == residue_degree(p)
    gu=sp.zeros(6)
    for i,c in enumerate(cs): gu += c*(U**i)
    a=hnf((p*EYE).row_join(gu))
    assert int(a.det()) == p**residue_degree(p)
    assert integral(a.inv()*U*a)
    return a

@lru_cache(None)
def ideal(n):
    if not isinstance(n,int) or n<1: raise ValueError('positive integer required')
    a=EYE
    for p,e in sorted(sp.factorint(n).items()):
        p,e=int(p),int(e); f=residue_degree(p)
        if e%f: raise ValueError(f'index {n} excluded: exponent of {p} not divisible by {f}')
        for _ in range(e//f): a=ideal_product(a,prime_ideal(p))
    assert int(a.det()) == n
    return a

def reduce_h(z,h):
    v=list(map(int,z))
    for i in range(5,-1,-1):
        q=v[i]//int(h[i,i])
        for j in range(i+1): v[j] -= q*int(h[j,i])
    return tuple(v)

class Quotient:
    def __init__(self,h):
        self.h=h; self.n=int(h.det())
        self.diag=tuple(int(h[i,i]) for i in range(6))
        self.points=tuple(product(*(range(a) for a in self.diag)))
        self.ids={z:i for i,z in enumerate(self.points)}
        self.generators=tuple(self.label(EYE[:,i]) for i in range(6))
        self.cyclic=self.diag[0]==self.n and all(d==1 for d in self.diag[1:])
    def label(self,z): return self.ids[reduce_h(z,self.h)]
    def add(self,a,b): return self.label(tuple(x+y for x,y in zip(self.points[a],self.points[b])))
    def distances(self):
        ds=[-1]*self.n; ds[0]=0; q=deque([0])
        moves=[tuple(s*int(EYE[j,i]) for j in range(6)) for i in range(6) for s in (-1,1)]
        while q:
            a=q.popleft(); z=self.points[a]
            for m in moves:
                b=self.label(tuple(x+y for x,y in zip(z,m)))
                if ds[b]<0: ds[b]=ds[a]+1; q.append(b)
        assert min(ds)>=0
        return np.asarray(ds,dtype=np.int64)

def mod_rank(rows,p):
    a=[list(map(lambda x:int(x)%p,row)) for row in rows]; r=0
    for j in range(6):
        k=next((k for k in range(r,len(a)) if a[k][j]),None)
        if k is None: continue
        a[r],a[k]=a[k],a[r]; inv=pow(a[r][j],-1,p)
        a[r]=[(v*inv)%p for v in a[r]]
        for k in range(r+1,len(a)):
            c=a[k][j]
            if c: a[k]=[(u-c*v)%p for u,v in zip(a[k],a[r])]
        r+=1
    return r

def projective_spectrum(p):
    counts=Counter()
    u=imat(U)
    for first in range(6):
        for tail in product(range(p),repeat=5-first):
            normal=[0]*first+[1]+list(tail); row=normal; orbit=[]
            for _ in range(6):
                orbit.append(row)
                row=[sum(row[i]*u[i][j] for i in range(6))%p for j in range(6)]
            counts[p**mod_rank(orbit,p)]+=1
    if p==7: expected={p**k:p**(k-1) for k in range(1,7)}
    else:
        f=residue_degree(p); g=6//f
        expected={p**(f*t):int(sp.binomial(g,t))*(p**f-1)**t//(p-1) for t in range(1,g+1)}
    assert dict(counts)==expected
    return dict(sorted(counts.items()))

def norm_matrix(z): return sp.Matrix.hstack(*(U**i*sp.Matrix(z) for i in range(6)))

def repair(root,walk,transport,n):
    h=ideal(n); q=Quotient(h)
    pts=[walk.point(k) for k in range(n)]
    labels=[q.label(z) for z in pts]
    if q.cyclic:
        row,cert,_=transport.repair_case(labels,q.generators)
        return {**row,'ideal_hnf':imat(h),'generators':list(q.generators)},cert
    ds=q.distances(); occ=Counter(labels)
    surplus=[c for c,a in sorted(occ.items()) for _ in range(a-1)]
    missing=[c for c in range(n) if c not in occ]
    cost=np.empty((len(surplus),len(missing)),dtype=np.int64)
    for i,c in enumerate(surplus):
        z=q.points[c]
        for j,d in enumerate(missing):
            w=q.points[d]; k=q.label(tuple(b-a for a,b in zip(z,w)))
            cost[i,j]=ds[k]
    _,total,cert=transport.certified_assignment(cost)
    return {'n':n,'support':len(occ),'minimum_moved':len(missing),
        'minimum_total_unit_distance':total,'mean_unit_distance':str(Fraction(total,n)),
        'quotient_diameter':int(ds.max()),'ideal_hnf':imat(h),'generators':list(q.generators)},cert

def verify(root):
    walk=load(root,'walk'); t6=load(root,'t6'); transport=load(root,'transport')
    assert U**7==EYE and sum((U**i for i in range(7)),sp.zeros(6))==sp.zeros(6)
    assert U.T*G*U==G and G.eigenvals()=={sp.Integer(1):1,sp.Integer(7):5}
    assert PHI.is_irreducible and int(norm_matrix([1,0,0,0,0,0]).det())==1
    assert int((U*EYE[:,5]).dot(U*EYE[:,5]))==6  # Not a native isometry.
    # All 63 binary observations: exact coarsest operation-safe refinement.
    domain=tuple(product((0,1),repeat=6))
    transition={z:tuple(int(a)%2 for a in U*sp.Matrix(z)) for z in domain}
    refined_counts=Counter(); binary={}
    for normal in domain[1:]:
        coarse={z:sum(a*b for a,b in zip(normal,z))%2 for z in domain}
        parts=t6.stable_future_partition(domain,transition,coarse)
        count=t6.class_count(parts); refined_counts[count]+=1
        assert t6.transition_compatible(domain,transition,parts)
        binary[''.join(map(str,normal))]=count
    assert dict(refined_counts)=={8:14,64:49}
    # A fixed integer functional is algebraically coherent but loses shape.
    r=13
    coeff=[2**i for i in range(6)]
    assert sum(coeff[i]*v for i,v in enumerate((2,-1,0,0,0,0)))==0
    # Prime factor degrees, ideals, repeated powers and all selected products.
    primes=list(sp.primerange(2,150))
    degree_rows=[]
    for p in primes:
        p=int(p); f=residue_degree(p); a=prime_ideal(p)
        assert int(a.det())==p**f and integral(a.inv()*U*a)
        degree_rows.append({'p':p,'f':f,'first_index':p**f})
    indices=[1,7,8,13**2,29,43,49,64,71,113,127,3**6,5**6,29**2,43**2,
             8*7,8*13**2,29*43,43*71,29*43*71,7**4,2**9,
             29**3*43**2*7**3,2**12*13**4]
    indices=sorted(set(indices))
    for n in indices:
        a=ideal(n)
        assert integral(a.inv()*U*a) and int(a.det())==n
    assert ideal(64) != 2*EYE
    assert not integral(ideal(64).inv()*(2*EYE[:,0]))
    pair_indices=[1,7,8,29,43,49,64,71,169]
    pair_checks=0; diamond_checks=0
    for m in pair_indices:
        a=ideal(m)
        for n in pair_indices:
            b=ideal(n); c=ideal(m*n)
            assert ideal_product(a,b)==c
            assert integral(a.inv()*c) and integral(b.inv()*c)
            assert hnf(a.row_join(b)) == ideal(int(sp.gcd(m,n)))
            # Sum/determinant formula proves intersection at lcm after inclusion.
            l=ideal(int(sp.ilcm(m,n)))
            assert integral(a.inv()*l) and integral(b.inv()*l)
            assert int(l.det())==m*n//int(sp.gcd(m,n))
            pair_checks+=1
    for k in (1,7,8):
        for m in (7,8,29,43):
            for n in (7,8,29,43):
                a=ideal(k); b=ideal(k*m); c=ideal(k*n); d=ideal(k*m*n)
                left=(a.inv()*b)*(b.inv()*d); right=(a.inv()*c)*(c.inv()*d)
                assert left==right and integral(left); diamond_checks+=1
    # Integer resultant/norm divisibility and exact sixth-power inequality.
    rng=random.Random(20260910); norm_checks=0; examples=[]
    for n in (7,8,29,43,127,169,729,1247,3053,88537):
        a=ideal(n); red=a.T.lll().T
        for j in range(12):
            w=sp.Matrix([rng.randint(-2,2) for _ in range(6)])
            if not any(w): w[0]=1
            z=red*w; norm=abs(int(norm_matrix(z).det()))
            q=int(z.dot(z)); trace=7*q-int(sum(z))**2
            assert norm>0 and norm%n==0 and 216*norm<=trace**3
            assert 216*n<=343*q**3
            assert norm_matrix(z).rank()==6
            for k in range(7): assert (U**k*z).dot(G*(U**k*z))==trace
            norm_checks+=1
        if n in (8,43,127,1247):
            examples.append({'n':n,'reduced_basis':imat(red),
                'basis_squared_lengths':[int(red[:,i].dot(red[:,i])) for i in range(6)]})
    costs=[]; certs=[]
    for n in (7,8,29,43,49,64,71,113,127,169,211,239,56,232,344,841,1247,1849,3053):
        row,cert=repair(root,walk,transport,n); costs.append(row)
        if n in (43,127,1247): certs.append({'n':n,**cert})
    # True joint CRT population for coprime local ideals.
    a,b=ideal(29),ideal(43); c=ideal(29*43)
    qa,qb,qc=Quotient(a),Quotient(b),Quotient(c)
    pairs={(qa.label(z),qb.label(z)) for z in qc.points}
    assert len(pairs)==29*43
    # Geometric mixed-prime finite observation beyond matching-sized populations.
    h=ideal(88537); qq=Quotient(h)
    assert qq.cyclic
    dd,_=transport.cyclic_geometry(88537,qq.generators)
    # Restoring divisibility by freezing the old base preserves a short kernel.
    fixed_rows=[]
    fixed_coeff=[2**i for i in range(6)]
    for nn in (29,43,1247):
        labels=[sum(c*z for c,z in zip(fixed_coeff,walk.point(k)))%nn for k in range(nn)]
        row,_,_=transport.repair_case(labels,fixed_coeff); fixed_rows.append(row)
    fixed_dist,_=transport.cyclic_geometry(88537,fixed_coeff)
    # Norm criterion excludes each named unadmitted index.
    excluded=[]
    for n in (2,3,4,5,6,9,13,25,27,67):
        try: ideal(n)
        except ValueError: excluded.append(n)
        else: raise AssertionError('Excluded index accepted')
    return {'status':'PASS_EXACT_INTEGER_CHECKS_AND_ASSIGNMENT_DUALS_NOT_ADMISSION',
      'source_snapshot':SOURCE,'dimension':6,'cyclotomic_order':7,
      'native_isometry':False,'operator':imat(U),'auxiliary_gram':imat(G),
      'binary_refinement_histogram':dict(refined_counts),'binary_observers':binary,
      'general_prime_refinement_spectra':{p:projective_spectrum(p) for p in (2,3,5,7)},
      'prime_factor_degree_checks':degree_rows,'ideal_indices_checked':indices,
      'product_and_lcm_pairs':pair_checks,'multiplication_diamonds':diamond_checks,
      'norm_and_trace_cases':norm_checks,'reduced_basis_witnesses':examples,
      'repair_costs':costs,'integer_dual_certificates':certs,
      'crt_pair_count':len(pairs),'triple_prime_index':88537,
      'triple_prime_quotient_diameter':int(dd.max()),'excluded_indices':excluded,
      'fixed_base_repair_costs':fixed_rows,'fixed_base_triple_diameter':int(fixed_dist.max()),
      'reuse':{k:{'path':p,'blob':s,'resolution':'REUSE_EXECUTED'} for k,(p,s) in PINS.items()},
      'limits':['not every positive integer admitted','not a P000 native rotation',
          'no O(1) average repair bound proved','no vanishing changed-point fraction',
          'no fixed-prefix transversal claim','no independent review or Foundation promotion']}

def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--source-root',type=Path,default=Path(__file__).resolve().parents[2])
    p.add_argument('--output',type=Path,required=True)
    p.add_argument('--full-output',type=Path)
    args=p.parse_args(); result=verify(args.source_root)
    args.output.parent.mkdir(parents=True,exist_ok=True)
    if args.full_output:
        args.full_output.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    summary={k:v for k,v in result.items() if k not in ('binary_observers','reduced_basis_witnesses','prime_factor_degree_checks','ideal_indices_checked')}
    summary['repair_costs']=[{k:v for k,v in row.items() if k not in ('ideal_hnf','generators')} for row in result['repair_costs']]
    summary['prime_factor_degree_checks']=len(result['prime_factor_degree_checks'])
    summary['ideal_indices_checked']=result['ideal_indices_checked']
    summary['integer_dual_certificates']=[c for c in result['integer_dual_certificates'] if c['n'] in (43,127)]
    args.output.write_text(json.dumps(summary,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({k:result[k] for k in ('status','binary_refinement_histogram','product_and_lcm_pairs',
        'multiplication_diamonds','norm_and_trace_cases','triple_prime_quotient_diameter')},indent=2))
    print('repair costs:',[(r['n'],r['minimum_total_unit_distance']) for r in result['repair_costs']])
if __name__=='__main__': main()
