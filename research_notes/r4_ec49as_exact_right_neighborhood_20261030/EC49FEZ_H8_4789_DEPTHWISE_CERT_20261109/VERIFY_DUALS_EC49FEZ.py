#!/usr/bin/env python3
"""Independent Python-stdlib exact audit of pooled-key group-prefix dual certificates.
Floating solver never called. Frozen science fc0f038e7bfd12c886b4d37f900bfb770c0f61ab.
"""
import sys,json,itertools,collections
from VERIFY_EC49FEZ import words,eligible,signed_steps,counts,LETTERS,NEXT,OBS

def verify(path):
 cert=json.load(open(path)); mixed=int(cert['mixed']);hs=tuple(map(int,cert['highset']))
 assert mixed==8 and len(hs)==4 and mixed in hs and 9 in hs
 assert cert['science_pin']=='fc0f038e7bfd12c886b4d37f900bfb770c0f61ab'
 Q=cert['Q']; assert Q>0; gamma=cert['gamma']; assert len(gamma)==23 and min(gamma)>=0
 sparse={int(k):int(v) for k,v in cert['weights']};assert all(v>0 for v in sparse.values())
 pool={(3,1,1)};high=set(hs)|{3}
 for h in sorted(high-{3}):pool.update(eligible(h,(16,) if h==mixed else (16,32)))
 pool=tuple(sorted(pool))
 prefix_id={}; pair_id={}; sums=collections.defaultdict(int)
 minweight=[]; minword=[]; group_counts=[];wordcheck=0
 for h in range(2,10):
  labels=(1,8,16) if h==mixed else ((16,32) if h in high else (1,2,4,8))
  for sig in labels:
   W=sorted({w for key in pool for label,w in words(h,key) if label==sig})
   assert W,(h,sig)
   lower=None;witness=''
   for w in W:
    assert len(w)==h
    displacement=[0]*6;st=0
    for ch in w:
     st=NEXT[st][LETTERS.index(ch)]
     for z in signed_steps(ch):displacement[abs(z)-1]+=1 if z>0 else -1
    assert displacement==[2,0,0,0,0,0] and OBS[st]==sig
    a=0
    prefix=()
    for step in signed_steps(w):
     prefix=prefix+(step,)
     pid=prefix_id.setdefault(prefix,len(prefix_id))
     pair=pair_id.setdefault((len(minweight),pid),len(pair_id))
     a+=sparse.get(pair,0)
    if lower is None or a<lower:lower=a;witness=w
    wordcheck+=1
   minweight.append(lower);minword.append(witness);group_counts.append(len(W))
 assert len(minweight)==23
 assert gamma==minweight,('gamma mismatch',gamma,minweight)
 assert max(sparse)<len(pair_id),('weight index out of range')
 for (g,p),idx in pair_id.items(): sums[p]+=sparse.get(idx,0)
 assert all(z<=Q for z in sums.values())
 LB=sum(minweight)
 output={'status':'EXACT_INTEGER_PASS','mixed':mixed,'highset':''.join(map(str,hs)),
         'pool_size':len(pool),'required_groups':23,'original_words_by_group':wordcheck,
         'unique_native_signed_prefixes':len(prefix_id),'group_prefix_pairs':len(pair_id),
         'nonzero_integer_weights':len(sparse),'Q':Q,'exact_numerator':LB,
         'strict_cost_lower_bound':(LB+Q-1)//Q,'min_signed_native_prefix_capacity_margin':int(Q-max(sums.values()))}
 return output
if __name__=='__main__':print(json.dumps(verify(sys.argv[1]),sort_keys=True))
