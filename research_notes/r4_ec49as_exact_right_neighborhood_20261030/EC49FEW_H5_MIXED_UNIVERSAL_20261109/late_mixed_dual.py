#!/usr/bin/env python3
"""EC49FEW author-side H5-mixed full finite branch elimination.

For each H5-mixed B branch with a positive signature-feasible census, construct a
SUPerset of the branch's original words by pooling all eligible complete BRC keys
for its five high-bearing horizons.  Every original valid five-key system is
contained in this larger pooled optimization problem.  SciPy is used only to
find a candidate integer dual certificate.  EC49FEW_VERIFY_UNIVERSAL.py checks
all conditions without SciPy, LP or numerical assumptions.

Original science pin: fc0f038e7bfd12c886b4d37f900bfb770c0f61ab.
"""
import json,sys,time
from pathlib import Path
from collections import defaultdict
import numpy as np
from scipy.optimize import linprog
from scipy.sparse import coo_array
from WORD_MODEL_EC49FET import words_with_label,native_prefixes
from EC49FEU_STANDALONE import keys as eligible_keys
Q=10**6
PIN='fc0f038e7bfd12c886b4d37f900bfb770c0f61ab'

def make_groups(mixed,highset):
    high=set(highset)|{3}
    assert mixed in high and 9 in high and len(high)==5
    # Exact native eligibility: H3's high key is uniquely (3,1,1).
    K_pool={(3,1,1)}
    for h in sorted(high - {3}):
        need=frozenset((16,)) if h==mixed else frozenset((16,32))
        K_pool.update(eligible_keys(h,need))
    K_pool=tuple(sorted(K_pool))
    G=[]
    for h in range(2,10):
        sigs=(1,8,16) if h==mixed else ((16,32) if h in high else (1,2,4,8))
        for sig in sigs:
            ws=sorted({w for key in K_pool for label,w in words_with_label(h,key) if label==sig})
            assert ws,(h,sig,highset)
            G.append((h,sig,ws))
    assert len(G)==23
    return K_pool,G

def solve(mixed,highset):
  t=time.monotonic();pool,G=make_groups(mixed,highset)
  words=[];gids=[];pref={};pairs={};wi=[];row=[]
  for h,s,W in G:
    gi=len(set(gids)) if not words else max(gids)+1 # before current group
    for w in W:
      j=len(words);words.append(w);gids.append(gi)
      for p in native_prefixes(w):
        ip=pref.setdefault(p,len(pref));ix=pairs.setdefault((gi,ip),len(pairs));wi.append(j);row.append(ix)
  n=len(words);npref=len(pref);m=len(pairs)
  A=coo_array((np.r_[np.ones(len(row)),-np.ones(m)],
         (np.r_[np.asarray(row,np.int32),np.arange(m,dtype=np.int32)],
          np.r_[np.asarray(wi,np.int32),np.array([n+p for g,p in pairs],np.int32)])),
         shape=(m,n+npref)).tocsr()
  E=coo_array((np.ones(n),(np.asarray(gids,np.int32),np.arange(n,dtype=np.int32))),shape=(23,n+npref)).tocsr()
  c=np.r_[np.zeros(n),np.ones(npref)]
  res=linprog(c,A_ub=A,b_ub=np.zeros(m),A_eq=E,b_eq=np.ones(23),bounds=(0,None),method='highs')
  assert res.status==0,res.message
  W=np.floor(np.maximum(0,-res.ineqlin.marginals)*Q+1e-7).astype(np.int64)
  loads=defaultdict(int)
  for (_,p),v in zip(pairs,W):loads[p]+=int(v)
  assert all(v<=Q for v in loads.values())
  sums=[0]*n
  for j,r in zip(wi,row):sums[j]+=int(W[r])
  gamma=[min(sums[j] for j,g in enumerate(gids) if g==i) for i in range(23)]
  LB=sum(gamma);assert LB>93*Q, (mixed,highset,res.fun,LB/Q)
  cert={'schema':'EC49FEW_UNIVERSAL_POOLED_PREFIX_DUAL_V1','science_pin':PIN,
      'mixed_horizon':mixed,'late_high_horizons':list(highset),
      'Q':Q,'gamma':gamma,'t_sparse':[[int(i),int(v)] for i,v in enumerate(W) if v>0],
      'semantics':'Every five-key inventory of this branch is a subset of pooled eligible keys; all operation words are original signed-X6 words; dual indexed by first-seen group/prefix pair.'}
  stats={'mixed':mixed,'late_high_horizons':list(highset),'eligible_pool_keys':len(pool),'pooled_words':n,'prefixes':npref,'group_prefix_pairs':m,
         'nonzero_integer_weights':len(cert['t_sparse']),'lp_value_finding_only':float(res.fun),'exact_dual_numerator':int(LB),'Q':Q,
         'integer_lower_bound':int((LB+Q-1)//Q),'elapsed_s':round(time.monotonic()-t,3)}
  return cert,stats

if __name__=='__main__':
 source=json.load(open(sys.argv[1]));dst=Path(sys.argv[2]);dst.mkdir(exist_ok=True)
 branch={h:c for h,c in source['by_high_set']['5'].items() if c['feasible']>0}
 assert set(branch)==set(('4569','4579','4589','5679','5689','5789'))
 out=[]
 for string in sorted(branch):
  cert,s=solve(5,tuple(map(int,string)))
  path=dst/f'UNIVERSAL_H5_{string}.json';path.write_text(json.dumps(cert,separators=(',',':'))+'\n')
  s['signature_feasible_in_original_census']=branch[string]['feasible'];s['certificate_file']=path.name
  out.append(s);print(json.dumps(s),flush=True)
 report={'schema':'EC49FEW_H5_MIXED_COMPLETE_LOWER_BOUND_V1','science_pin':PIN,'branch_count':len(out),'signature_feasible_original_sum':sum(x['signature_feasible_in_original_census'] for x in out),
         'qualification':'Complete H5 type-B late-high-set branches, mixed labels (1,8,16), exactly 23 native words and five BRC full keys. Original 90,258 type-B late-mixed possibilities include other mixed placements H5-H8.',
         'method':'Pool all possible complete keys separately by high horizon; ignore five-key coupling (relaxation), then exact integer group-native-prefix dual. Unpooled costs cannot be lower than pooled optimum.',
         'results':out}
 assert report['signature_feasible_original_sum']==15812
 (dst/'EC49FEW_REPORT.json').write_text(json.dumps(report,indent=2)+'\n')
