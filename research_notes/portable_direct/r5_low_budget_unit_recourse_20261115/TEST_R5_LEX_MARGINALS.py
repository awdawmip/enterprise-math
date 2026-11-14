"""Independent exhaustive small-instance check for center-path lexicographic marginals."""
import itertools,random,sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parent))
import VERIFY_R5_FORCED_COORDINATES as v
rng=random.Random(20261115)
checks=0
for n in range(3,9):
 for rep in range(12):
  ds=[rng.choice((1,1,1,2,3)) for _ in range(n-1)]
  z=[0]
  for d in ds:z.append(z[-1]+d)
  g=v.graph(z)
  for k in range(1,min(n,5)+1):
   v.K=k
   feas=[]
   for T in itertools.combinations(range(n),k):
    d=[min(abs(z[t]-z[j]) for j in T) for t in range(n)]
    if max(d)<=2:feas.append((sum(d),T))
   if not feas: continue
   optimum=min(x[0] for x in feas)
   opts=[set(T) for c,T in feas if c==optimum]
   for draw in range(3):
    S=sorted(rng.sample(range(n),k))
    mx=max(len(set(S)&T) for T in opts)
    near=[T for T in opts if len(set(S)&T)==mx]
    R=v.analyze(S,g,expected_cost=optimum)
    assert R['closest_swaps']==k-mx
    assert R['nearest_count']==len(near)
    assert R['forced_removed']==sorted(set(S)-set.union(*near))
    assert R['common_retained']==sorted(set(S)&set.intersection(*near))
    assert R['forced_additions']==sorted(set.intersection(*near)-set(S))
    checks+=1
print('PASS_EXHAUSTIVE_SMALL_LEX_MARGINALS',checks)
