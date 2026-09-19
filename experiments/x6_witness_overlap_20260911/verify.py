#!/usr/bin/env python3
"""Exact X6 witness-event overlap experiment; no network I/O.

Usage: python verify.py --source-root <pinned EM dependency root> --output results.json
This is a domain experiment, not a new general probability algorithm or native law.
"""
from __future__ import annotations
import argparse
from collections import Counter
from fractions import Fraction as F
import hashlib
import importlib.util
from itertools import combinations, product
import json
from pathlib import Path
import numpy as np
import sympy as sp

SOURCE = 'a45dfb6438e8ac01086d6a775be2d36e3abde207'
PINS = {
 'flags': ('experiments/x6_intermediate_flags_20260910/verify.py','c41fdd1a468d8d7ee52c96c3a739dd59c78892ec'),
 'seeds': ('experiments/x6_seed_geometry_20260910/verify.py','e155621d04f0e354f06d48e5075bc5d43d4d0f71'),
 'ideal': ('experiments/x6_cyclotomic_compatibility_20260910/verify.py','0d4ea1d29281236c80ae8502de7d75a5d76c39e9'),
 't6': ('src/enterprise_math/composition_safe_collapse.py','384d166f642fb65c53fc7f2431f43dc99880693a')}
LOCKS = [(2,0,(1,1,1)),(3,0,(1,2,2,2,1,0)),(13,0,(1,2)),(2,1,(0,1,0))]

def load(root, name):
 path, expected = PINS[name]
 raw = (root/path).read_bytes()
 actual = hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest()
 if actual != expected: raise ValueError(f'{name} frozen blob mismatch: {actual}')
 spec = importlib.util.spec_from_file_location('overlap_'+name, root/path)
 module = importlib.util.module_from_spec(spec); spec.loader.exec_module(module)
 return module

def theoretical_spectrum(p, f, s):
 """Counts of ratios with each intersection dimension, after duality if needed."""
 k=min(s,f-s); shift=max(0,2*s-f)
 out=Counter({k+shift:p-1})
 for j in range(1,k): out[k-j+shift] += (p*p-1)*p**(2*j-1)
 out[shift] += p**f-p**(2*k-1)
 return {d:n for d,n in sorted(out.items()) if n}

def maximum_tree(pair):
 m=len(pair); parent=list(range(m)); edges=[]
 def find(i):
  while parent[i]!=i: parent[i]=parent[parent[i]]; i=parent[i]
  return i
 for w,i,j in sorted([(int(pair[i,j]),i,j) for i in range(m) for j in range(i+1,m)], reverse=True):
  a,b=find(i),find(j)
  if a!=b: parent[a]=b; edges.append((i,j,w))
 if m: assert len(edges)==m-1
 return edges

def mask_rows(inc):
 return [sum(int(v)<<j for j,v in enumerate(row)) for row in inc]

def rank(c, rows, p):
 return c.mod_rank([list(map(int,row))+[0]*(6-len(row)) for row in rows],p)

def verify(root):
 flags=load(root,'flags'); flags.configure(root); c=flags.c
 seeds=load(root,'seeds'); t6=load(root,'t6'); load(root,'ideal')
 u=np.array(c.U.tolist(),dtype=np.int64)
 spectra=[]; spectrum_rank_checks=0
 # Each vector below corresponds bijectively to a field ratio against e_0.
 for p in (2,3,5,11,13):
  _,_,ub,q,_=flags.block(p,0); f=q.rows
  piv=[]
  for j in range(6):
   test=q[:,piv+[j]]
   if rank(c,test.tolist(),p)>len(piv):piv.append(j)
   if len(piv)==f:break
  right=sp.zeros(6,f); inverse=q[:,piv].inv_mod(p)
  for i,pos in enumerate(piv):
   for j in range(f):right[pos,j]=inverse[i,j]
  action=np.array((q*ub*right).tolist(),dtype=np.int64)%p
  origin=np.zeros(f,dtype=np.int64);origin[0]=1
  base=[];x=origin
  for j in range(f):base.append(x.tolist());x=action@x%p
  assert rank(c,base,p)==f
  hist={s:Counter() for s in range(1,f)}
  for v in product(range(p),repeat=f):
   if not any(v):continue
   orbit=[];x=np.array(v,dtype=np.int64)
   for j in range(f-1):orbit.append(x.tolist());x=action@x%p
   for s in range(1,f):
    d=2*s-rank(c,base[:s]+orbit[:s],p);hist[s][d]+=1;spectrum_rank_checks+=1
  for s,h in hist.items():
   assert dict(sorted(h.items()))==theoretical_spectrum(p,f,s)
   spectra.append({'p':p,'f':f,'s':s,'intersection_counts':dict(sorted(h.items()))})
 print('All finite-field ratio spectra checked',flush=True)

 # One unchanged product ensemble: ONLY (5,0),(11,0) vary. Four earlier locks remain.
 vs=np.array([v for v in seeds.sphere_vectors(4) if next(x for x in v if x)>0],dtype=np.int64)
 qs=np.sum(vs*vs,axis=1)
 local={}; matrices={}; sample_counts={}; good_checks=[]
 for p in (5,11):
  _,_,ub,q,_=flags.block(p,0);f=q.rows
  # Every nonzero integer vector has Q>=1. Thus ALL these seeds pass the old filter.
  assert p**(f-1)<42**3
  good_checks.append({'p':p,'f':f,'largest_intermediate_index':p**(f-1),'threshold_denominator':42**3,'all_seeds_good':True})
  ds=np.array(list(seeds.projective(p,f)),dtype=np.int64); sample_counts[p]=len(ds)
  normal=ds@np.array(q.tolist(),dtype=np.int64)%p
  for s in (1,2):
   rows=normal.copy(); inc=np.ones((len(ds),len(vs)),dtype=bool)
   for j in range(s):inc &= rows@vs.T%p==0;rows=rows@u%p
   local[p,s]=inc
   matrices[p,s]=[np.array(q*flags.U**j,dtype=np.int64)%p for j in range(s)]
 locknormal={}
 for p,r,coeff in LOCKS:
  _,_,_,q,_=flags.block(p,r)
  locknormal[p,r]=np.array(coeff,dtype=np.int64)@np.array(q.tolist(),dtype=np.int64)%p
 cases=[]; event_arrays={}; pair_rank_checks=0; t6_checks=0
 for s5,s11,qmax,locked in [(1,1,1,None),(1,1,2,None),(2,1,1,None),(2,1,2,None),(1,2,2,None),(1,2,3,None),(2,2,2,None),(2,2,3,None),(2,1,4,None),(2,1,2,2),(2,1,2,3),(2,1,2,13)]:
  n=5**s5*11**s11*(locked or 1)
  keep=qs<=qmax
  if locked:keep &= vs@locknormal[locked,0]%locked==0
  vv=vs[keep];A=local[5,s5][:,keep];B=local[11,s11][:,keep]
  fingerprints={j:(np.packbits(A[:,j]).tobytes(),np.packbits(B[:,j]).tobytes()) for j in range(len(vv))}
  if len(vv):
   classids=t6.canonical_class_ids(range(len(vv)),fingerprints)
   assert t6.descends_through(range(len(vv)),classids,fingerprints);t6_checks+=1
  groups={}
  for j,key in fingerprints.items():
   if A[:,j].any() and B[:,j].any():groups.setdefault(key,[]).append(j)
  ids=[ls[0] for ls in groups.values()];A=A[:,ids];B=B[:,ids];m=len(ids)
  ai=A.astype(np.int64);bi=B.astype(np.int64)
  joint=(ai.T@ai)*(bi.T@bi);single=ai.sum(0)*bi.sum(0)
  # Independent rank evaluation of every local pair, compared to exact seed counts.
  for p,s,inc in ((5,s5,A),(11,s11,B)):
   counts=inc.astype(np.int64).T@inc.astype(np.int64);f=c.residue_degree(p)
   columns=[[mat@vv[j]%p for mat in matrices[p,s]] for j in ids]
   for i in range(m):
    for j in range(i,m):
     d=rank(c,columns[i]+columns[j],p)
     assert counts[i,j]==(p**(f-d)-1)//(p-1);pair_rank_checks+=1
  ma,mb=mask_rows(A),mask_rows(B);hist=Counter((a&b).bit_count() for a in ma for b in mb)
  total=len(ma)*len(mb);assert total==519498
  mu=F(int(single.sum()),total);second=F(int(np.triu(joint,1).sum()),total)
  exact=F(total-hist.get(0,0),total)
  assert mu==F(sum(k*v for k,v in hist.items()),total)
  assert second==F(sum(k*(k-1)*v//2 for k,v in hist.items()),total)
  tree=maximum_tree(joint);tw=F(sum(e[2] for e in tree),total);hunter=mu-tw
  kmax=max(hist);cap=mu-2*second/kmax if kmax else F(0)
  assert max(F(0),mu-second)<=exact<=min(F(1),hunter,cap)
  assert tw<=mu/F(5) # equal-marginal, distinct-profile single-block-rank bound
  if m<=6:
   for bits in range(1<<m):
    y=bits.bit_count();active=sum(bool(bits>>i&1) and bool(bits>>j&1) for i,j,_ in tree)
    assert int(y>0)<=y-active
  key=f'{n}:Q<={qmax}'
  event_arrays[key]=np.array([(a&b)!=0 for a in ma for b in mb],dtype=bool)
  cases.append({'n':n,'Q_max':qmax,'locked_prime_filter':locked,'signed_pairs_before_event_quotient':len(vv),'distinct_nonempty_events':m,'duplicate_groups':[[vv[j].tolist() for j in ls] for ls in groups.values() if len(ls)>1], 'sample_size':total,'first_moment':str(mu),'factorial_second_half':str(second),'exact_union':str(exact),'hunter_upper':str(hunter),'rank_cap_upper':str(cap),'maximum_simultaneous_events':kmax,'histogram':dict(sorted(hist.items())),'tree_edge_count':len(tree),'tree_sha256':hashlib.sha256(json.dumps(tree,separators=(',',':')).encode()).hexdigest(),'tree_edges':[[i,j,str(F(w,total))] for i,j,w in tree] if (n,qmax) in ((55,1),(275,2),(605,3)) else None,'tree_weight':str(tw)})
  print(key,'events',m,'union',exact,'Hunter',hunter,flush=True)

 # Explicit full-rank local certificates, not inference solely from outcome histograms.
 q11=np.array(flags.block(11,0)[3].tolist(),dtype=np.int64)
 triples=[]; triple_determinants=[]
 for js in combinations(range(6),3):
  d=rank(c,[q11[:,j] for j in js],11);assert d==3;triples.append(list(js));triple_determinants.append({'axes':list(js),'det_mod11':int(sp.Matrix(q11[:,list(js)].tolist()).det())%11})
 v36=vs[qs<=2]; annihilator_lines=[]
 for v in v36:
  rows=sp.Matrix([list(q11@v%11),list(q11@u@v%11)])
  line=[int(x)%11 for x in flags.nullspace_mod(rows,11)]
  inv=pow(next(x for x in line if x),-1,11);line=[x*inv%11 for x in line]
  annihilator_lines.append(line)
 assert len({tuple(x) for x in annihilator_lines})==36
 for i,j in combinations(range(len(v36)),2):
  rows=[q11@v36[i]%11,q11@u@v36[i]%11,q11@v36[j]%11,q11@u@v36[j]%11]
  assert rank(c,rows,11)==3
 covariances=[]
 for ka,kb in [('55:Q<=2','275:Q<=2'),('55:Q<=2','605:Q<=2'),('275:Q<=2','550:Q<=2')]:
  a,b=event_arrays[ka],event_arrays[kb];t=len(a)
  pa,pb,pab=F(int(a.sum()),t),F(int(b.sum()),t),F(int((a&b).sum()),t)
  covariances.append({'a':ka,'b':kb,'P_a':str(pa),'P_b':str(pb),'P_joint':str(pab),'covariance':str(pab-pa*pb)})
 return {'status':'PASS_EXACT_ENUMERATION_RANK_AND_MOMENT_CERTIFICATES_NOT_ADMISSION', 'source_snapshot':SOURCE,'locks_unchanged':[[p,r,list(co)]for p,r,co in LOCKS], 'seed_counts':sample_counts,'good_set_certificates':good_checks,'ratio_spectrum_checks':spectrum_rank_checks,'ratio_spectra':spectra,'pair_rank_checks':pair_rank_checks,'T6_event_quotient_checks':t6_checks,'cases':cases,'triple_rank_cap_certificates':len(triples),'triple_determinants_mod11':triple_determinants,'exclusive_annihilator_lines_mod11':annihilator_lines,'exclusive_pair_certificates':630,'cross_index_bad_event_covariances':covariances,'window_constants':{'gamma':'3/8','beta':1,'c':'5/59','critical_alpha':str(6*F(3,8)-2-F(5,59)),'old_critical_log_requirement':'>64/59','new_critical_log_requirement':'>1','power_frontier_unchanged':True,'tunable_epsilon':'1/200','tunable_critical_alpha':str(6*F(3,8)-2-F(1,200)),'tunable_old_eta_requirement':'>201/200','tunable_new_eta_requirement':'>1'},'boundaries':['experimental Q_max is a declared finite radius, not the asymptotic shrinking threshold','no new infinite-scale exponent improvement','no new seed lock','no independence of shared-block events','Hunter forest bound is classical; the domain spectra and applications have written proofs','no independent review or Foundation promotion'],'reuse':{name:{'path':p,'git_blob_sha1':sha,'state':'REUSE_EXECUTED'}for name,(p,sha) in PINS.items()}}

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--source-root',type=Path,required=True);ap.add_argument('--output',type=Path,required=True);args=ap.parse_args()
 result=verify(args.source_root);args.output.parent.mkdir(parents=True,exist_ok=True)
 args.output.write_text(json.dumps(result,ensure_ascii=False,separators=(',',':'))+'\n',encoding='utf-8')
 print('PASS',args.output,flush=True)
if __name__=='__main__':main()
