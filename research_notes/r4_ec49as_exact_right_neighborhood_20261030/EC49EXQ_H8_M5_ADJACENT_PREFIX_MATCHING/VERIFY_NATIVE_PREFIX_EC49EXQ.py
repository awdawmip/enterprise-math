#!/usr/bin/env python3
"""Independent native operation-word verification of L-3 collision lemma, h=2..5."""
from itertools import product,combinations
from collections import defaultdict,Counter
import json
CODES={'a':(-1,-1),'b':(-2,-2),'c':(1,2,-1,-2),
'd':(2,1,-2,-1),'e':(3,1,1,-3),'f':(1,-1),'g':(2,-2)}
assert len({code[:2] for code in CODES.values()})==7
W=[];per_h=Counter()
for h in range(2,6):
 for z in product('abcdefg',repeat=h):
  if z.count('b')!=0 or z.count('e')!=z.count('a')+1:continue
  native=sum((CODES[c] for c in z),())
  disp=tuple(native.count(i)-native.count(-i) for i in range(1,7))
  if disp!=(2,0,0,0,0,0):continue
  K=tuple(native.count(i) for i in range(1,4))
  assert len(native)==2*(sum(K)-1)
  W.append((h,''.join(z),K,native));per_h[h]+=1
assert [per_h[h] for h in range(2,6)]==[8,51,304,1770]
groups=defaultdict(list);pairs=Counter()
for h,z,k,n in W: groups[(k,n[:len(n)-3])].append((h,z,n))
for v in groups.values():
 hs=[x[0] for x in v]
 assert len(v)<=2 and len(hs)==len(set(hs))
 if len(v)==2:
  assert abs(hs[0]-hs[1])==1
  pairs[(min(hs),max(hs))]+=1
bykey=defaultdict(list)
for x in W:bykey[x[2]].append(x)
tested=0
for v in bykey.values():
 for (h,z,k,a),(j,y,k2,b) in combinations(v,2):
  lcp=next((i for i,(x,y) in enumerate(zip(a,b)) if x!=y),min(len(a),len(b)))
  assert lcp<=len(a)-3
  if lcp==len(a)-3:assert abs(h-j)==1
  tested+=1
print(json.dumps({'status':'PASS','window_counts':dict(per_h),'native_words':len(W),
'pairwise_same_key_checked':tested,'two_word_shared_prefix_groups':sum(pairs.values()),
'adjacent_horizon_pair_groups':{str(k):v for k,v in pairs.items()}},indent=2))
