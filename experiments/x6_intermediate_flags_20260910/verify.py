#!/usr/bin/env python3
"""Exact domain experiment: all-index flags and minimum U-future information.

Run: python verify.py --source-root /path/to/enterprise-math --output results.json
Frozen parent, native path, T6 and certified-assignment modules are reused.
Finite tests are not a formal proof, independent review or project admission.
"""
from __future__ import annotations
import argparse
from collections import Counter
from fractions import Fraction
import json
import random
import numpy as np
from pathlib import Path
import importlib.util, sys, hashlib
from functools import lru_cache
import sympy as sp
from sympy.matrices.normalforms import hermite_normal_form as hnf
from itertools import product
SOURCE='a12be839318bded31998207ee18ef76762b7a856'
PARENT_PATH='experiments/x6_cyclotomic_compatibility_20260910/verify.py'
PARENT_BLOB='0d4ea1d29281236c80ae8502de7d75a5d76c39e9'
c=None; I=sp.eye(6); U=sp.zeros(6)
old_hnf=hnf

def configure(root):
 global c,U
 raw=(root/PARENT_PATH).read_bytes()
 actual=hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest()
 if actual!=PARENT_BLOB: raise ValueError('Frozen parent mismatch: '+actual)
 spec=importlib.util.spec_from_file_location('x6_flags_parent',root/PARENT_PATH)
 c=importlib.util.module_from_spec(spec);spec.loader.exec_module(c);U=c.U
 block.cache_clear();local.cache_clear();family.cache_clear()

def hnf(m):
 if not c.integral(m):raise ValueError('Integer lattice matrix required')
 return old_hnf(m.applyfunc(sp.Integer))

def nullspace_mod(a,p):
 a=[[int(v)%p for v in a.row(i)] for i in range(a.rows)]
 rows=len(a); cols=len(a[0]); r=0; piv=[]
 for j in range(cols):
  k=next((k for k in range(r,rows) if a[k][j]),None)
  if k is None: continue
  a[r],a[k]=a[k],a[r]; inv=pow(a[r][j],-1,p); a[r]=[(inv*v)%p for v in a[r]]
  for k in range(rows):
   if k!=r and a[k][j]:
    t=a[k][j]; a[k]=[(u-t*v)%p for u,v in zip(a[k],a[r])]
  piv.append(j); r+=1
  if r==rows:break
 out=[]
 for j in range(cols):
  if j in piv:continue
  v=[0]*cols;v[j]=1
  for k,i in enumerate(piv):v[i]=-a[k][j]%p
  out.append(v)
 return sp.Matrix(out)

def modular_kernel(rows,p):
 h=I
 for a in rows.tolist():
  w=[int(v)%p for v in sp.Matrix([a])*h]
  j=next((j for j,v in enumerate(w) if v),None)
  if j is None:continue
  k=I.copy();k[j,j]=p; inv=pow(w[j],-1,p)
  for i in range(6):
   if i!=j:k[j,i]=-w[i]*inv%p
  h=hnf(h*k)
 return h

def intersect(a,b):
 d=sp.ilcm(int(a.det()),int(b.det()))
 k=hnf((d*a.inv().T).row_join(d*b.inv().T))
 out=d*k.inv().T
 assert c.integral(out)
 return hnf(out)

@lru_cache(None)
def block(p,r):
 f=c.residue_degree(p); a=c.ideal(p**(r*f));b=c.ideal(p**((r+1)*f))
 rel=a.inv()*b
 q=nullspace_mod(rel.T,p)
 assert q.rows==f
 u=a.inv()*U*a
 base=1
 while base**6<p:base+=1
 ell=(sp.Matrix([[pow(base,i,p) for i in range(f)]])*q).applyfunc(lambda x:int(x)%p)
 return a,b,u,q,ell

@lru_cache(None)
def local(p,k):
 f=c.residue_degree(p);r,s=divmod(k,f)
 if s==0:return c.ideal(p**k)
 a,b,u,q,ell=block(p,r)
 rows=sp.Matrix.vstack(*(ell*u**j for j in range(s))).applyfunc(lambda x:int(x)%p)
 out=hnf(a*modular_kernel(rows,p))
 assert out.det()==p**k
 return out

@lru_cache(None)
def family(n):
 a=I
 for p,k in sorted(sp.factorint(n).items()):a=intersect(a,local(int(p),int(k)))
 assert a.det()==n
 return a

def rounded(n,h=None,up=False):
 out=1
 for p,k in sp.factorint(n).items():
  p,k=int(p),int(k);f=c.residue_degree(p);r,s=divmod(k,f)
  e=f*r
  if s:
   e+=f if up else (s+min(h,f-s) if h is not None else 0)
  out*=p**e
 return out

def repair(h,walk,transport):
 """Finite unrestricted native repair; reuse the existing exact dual checker."""
 q=c.Quotient(h);n=int(h.det());labels=[q.label(walk.point(k)) for k in range(n)]
 if q.cyclic:
  row,cert,_=transport.repair_case(labels,q.generators)
  return row,cert
 ds=q.distances();counts=Counter(labels)
 surplus=[a for a,size in sorted(counts.items()) for _ in range(size-1)]
 missing=[a for a in range(n) if a not in counts]
 cost=np.empty((len(surplus),len(missing)),dtype=np.int64)
 if surplus:
  targets=np.array([q.points[x] for x in missing],dtype=np.int64)
  hh=np.array(c.imat(h),dtype=np.int64)
  assert n<=10000 and int(np.max(np.abs(hh)))<=10000
  weights=np.array([int(sp.prod(q.diag[i+1:])) for i in range(6)],dtype=np.int64)
  for i,a in enumerate(surplus):
   values=targets-np.array(q.points[a],dtype=np.int64)
   for j in range(5,-1,-1):
    quot=values[:,j]//hh[j,j]
    values[:,:j+1]-=quot[:,None]*hh[:j+1,j]
   cost[i,:]=ds[values@weights]
 _,total,cert=transport.certified_assignment(cost)
 return {'n':n,'support':len(counts),'minimum_moved':len(missing),
  'minimum_total_unit_distance':total,'mean_unit_distance':str(Fraction(total,n)),
  'quotient_diameter':int(ds.max())},cert

def verify(root):
 configure(root)
 walk=c.load(root,'walk');t6=c.load(root,'t6');transport=c.load(root,'transport')
 local_checks=0
 for p in (2,3,5,7,11,13,17,19,23,29,31,43,67):
  f=c.residue_degree(p)
  for r in range(3):
   a,b,u,_,ell=block(p,r)
   rows=sp.Matrix.vstack(*(ell*u**j for j in range(f)))
   assert c.mod_rank(rows.tolist(),p)==f
   assert hnf(a*modular_kernel(rows,p))==b
   previous=a
   for s in range(f+1):
    current=local(p,f*r+s)
    assert int(current.det())==p**(f*r+s)
    assert c.integral(previous.inv()*current)
    previous=current;local_checks+=1
 print('Local flag blocks verified',flush=True)
 indices=list(range(1,121))+[127,169,201,256,257,512,729,1247,3053,2**10*3**7*13**3*29]
 horizons=0;envelopes=0
 for n in indices:
  a=family(n);b=a
  for h in range(6):
   assert int(b.det())==rounded(n,h)
   assert b==family(rounded(n,h)),(n,h)
   b=intersect(b,U**6*b);horizons+=1
  assert b==c.ideal(rounded(n,up=True))
  envelope=hnf(sp.Matrix.hstack(*(U**j*a for j in range(6))))
  assert envelope==c.ideal(rounded(n));envelopes+=1
 print('All-index core and envelope identities verified',flush=True)
 selected=[1,2,3,4,5,6,7,8,9,12,13,16,24,27,29,43];pairs=0
 for m in selected:
  for n in selected:
   a,b=family(m),family(n)
   assert intersect(a,b)==family(int(sp.ilcm(m,n)))
   assert hnf(a.row_join(b))==family(int(sp.gcd(m,n)))
   pairs+=1
 diamonds=0
 for k in (1,2,3,6):
  for m in (2,3,5,13):
   for n in (2,3,5,13):
    a,b,d,e=family(k),family(k*m),family(k*n),family(k*m*n)
    ab,be,ad,de=a.inv()*b,b.inv()*e,a.inv()*d,d.inv()*e
    assert all(c.integral(x) for x in (ab,be,ad,de))
    assert ab*be==ad*de;diamonds+=1
 product_index=int(c.ideal_product(family(2),family(2)).det())
 assert product_index==1 and family(4).det()==4
 unit=I[:,2]
 assert c.integral(family(2).inv()*unit)
 assert not c.integral(family(2).inv()*U*unit)
 assert int(c.norm_matrix(unit).det())==1
 print('Divisibility and multiplication boundaries verified',flush=True)
 arbitrary_checks=0; arng=random.Random(70120260910)
 for n in (2,3,4,6,9,12,18,26,27):
  for sample in range(5):
   diag=[1]*6
   for prime,power in sp.factorint(n).items():diag[arng.randrange(6)]*=int(prime)**int(power)
   v=I.copy()
   for _ in range(8):
    i,j=arng.sample(range(6),2);sign=arng.choice((-1,1))
    for k in range(6):v[i,k]+=sign*v[j,k]
   z=hnf(v*sp.diag(*diag));assert z.det()==n
   for h in range(6):
    assert int(z.det())%rounded(n,h)==0
    z=intersect(z,U**6*z);arbitrary_checks+=1
 sequences={};microstates=0;witnesses={}
 for n in (2,3,4,6,7,9,12,16,26):
  core=c.Quotient(c.ideal(rounded(n,up=True)));current=c.Quotient(family(n))
  domain=core.points
  transition={z:core.points[core.label((-z[5],z[0]-z[5],z[1]-z[5],z[2]-z[5],z[3]-z[5],z[4]-z[5]))] for z in domain}
  observed={z:current.label(z) for z in domain}
  stages=t6.future_partition_sequence(domain,transition,observed)
  got=[t6.class_count(part) for part in stages]
  expected=list(dict.fromkeys(rounded(n,h) for h in range(6)))
  assert got==expected and got[-1]==core.n
  sequences[str(n)]=got;microstates+=core.n
  witnesses[str(n)]=t6.fiber_constancy_witness(domain,observed,{z:observed[transition[z]] for z in domain})
 print('T6 minimum state sequences verified',flush=True)
 a,b,u,q,_=block(2,0);binary=[]
 for coeffs in product((0,1),repeat=3):
  if not any(coeffs):continue
  ell=(sp.Matrix([coeffs])*q).applyfunc(lambda x:int(x)%2)
  h2=hnf(a*modular_kernel(ell,2))
  h4=hnf(a*modular_kernel(sp.Matrix.vstack(ell,ell*u),2))
  assert intersect(h2,U**6*h2)==h4 and intersect(h4,U**6*h4)==b
  r2,_=repair(h2,walk,transport);r4,_=repair(h4,walk,transport)
  binary.append({'normal':[int(x) for x in ell],'cost_at_2':r2['minimum_total_unit_distance'],'cost_at_4':r4['minimum_total_unit_distance']})
 costs=[];certs=[]
 for n in (2,3,4,5,6,9,10,12,13,15,16,18,24,27,32,43,64,67,127,134,169,201,256,257,512,729,1247):
  row,cert=repair(family(n),walk,transport)
  row.update(lower_ideal_index=rounded(n),safe_ideal_index=rounded(n,up=True),extra_safe_states=rounded(n,up=True)//n)
  costs.append(row)
  if n in (6,67,201):certs.append({'n':n,**cert})
 rng=random.Random(20260910);norm_checks=0
 for n in (2,6,12,16,24,43,67,127,201,1247):
  a=family(n)
  for _ in range(6):
   w=sp.Matrix([rng.randint(-2,2) for _ in range(6)])
   if not any(w):w[0]=1
   z=a*w;norm=int(c.norm_matrix(z).det());qv=int(z.dot(z))
   assert norm>0 and norm%rounded(n)==0
   assert 216*rounded(n)<=343*qv**3;norm_checks+=1
 print('Native repair costs and envelope norm checks verified',flush=True)
 return {'status':'PASS_EXACT_DOMAIN_REGRESSION_NOT_FORMAL_OR_INDEPENDENT_REVIEW',
  'source_snapshot':SOURCE,'arithmetic':'integer/rational; bounded integer cost tables with exact dual verification',
  'local_flag_checks':local_checks,'all_index_bases':len(indices),'horizon_lattice_checks':horizons,
  'invariant_envelope_checks':envelopes,'gcd_lcm_pairs':pairs,'relative_multiplication_diamonds':diamonds,'arbitrary_lattice_lower_bound_checks':arbitrary_checks,
  't6_sequences':sequences,'t6_total_microstates':microstates,'t6_one_step_witnesses':witnesses,
  'binary_seed_flags':binary,'repair_costs':costs,'integer_dual_certificates':certs,'envelope_norm_checks':norm_checks,
  'ring_product_counterexample':{'indices':[2,2],'product_index':product_index,'target_lattice_index':4},
  'unit_norm_counterexample':{'index':2,'vector':[0,0,1,0,0,0],'norm':1},
  'binary_intermediate_bases':{'2':c.imat(family(2)),'4':c.imat(family(4))},
  'large_index_basis_only':indices[-1],'reused_parent_blob':PARENT_BLOB,
  'reused_t6_blob':c.PINS['t6'][1],'reused_transport_blob':c.PINS['transport'][1],'reused_walk_blob':c.PINS['walk'][1],
  'boundaries':['U is not a native isometry','intermediate lattices are not ideals','no all-integer uniform shape bound',
   'no constant average repair theorem','no strict local or nested representative selection',
   'no global mathematical novelty claim','no Foundation or Working Truth admission']}

def main():
 parser=argparse.ArgumentParser(description=__doc__)
 parser.add_argument('--source-root',type=Path,required=True)
 parser.add_argument('--output',type=Path,required=True)
 args=parser.parse_args();result=verify(args.source_root.resolve())
 args.output.parent.mkdir(parents=True,exist_ok=True)
 args.output.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
 print('PASS',flush=True)

if __name__=='__main__':main()
