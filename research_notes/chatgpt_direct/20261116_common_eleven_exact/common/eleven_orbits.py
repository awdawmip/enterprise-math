"""Affine isomorphism types of eleven-label partitions in the extendible five-maximum type."""
from collections import Counter
from itertools import product,permutations
import json
from pathlib import Path
from cyclic11 import P,index,setbits,observations
from six13 import enumerate_classes
p=json.loads(Path(__file__).with_name('cyclic11.json').read_text())
large={sum(1<<i for i in c)for c in p['classes'][:5]}
space=(1<<125)-1-sum(large)
bad,_=observations()
rows=enumerate_classes(space,10,bad)
sol=set()
def cover(free,available,chosen):
    if not free:
        sol.add(tuple(sorted(chosen)))
        return
    freq={i:[] for i in setbits(free)}
    for s in available:
        for i in setbits(s):freq[i].append(s)
    for s in min(freq.values(),key=len):
        cover(free^s,[r for r in available if not r&s],chosen+[s])
cover(space,rows,[])
def image(m,t):
    return sum(1<<t[i]for i in setbits(m))
stabilizer=[]
for per in permutations(range(3)):
    for k in (1,2):
        for sg in product((1,-1),repeat=3):
            T=[tuple(k*sg[j]*p[per[j]]%5 for j in range(3)) for p in P]
            for d in P:
                t=tuple(index(tuple((q+w)%5 for q,w in zip(v,d)))for v in T)
                if all(image(s,t) in large for s in large):stabilizer.append(t)
reps=[]
seen=set()
for part in sorted(sol):
    if part in seen:continue
    orbit={tuple(sorted(image(s,t)for s in part))for t in stabilizer}
    assert orbit<=sol
    seen.update(orbit)
    reps.append(dict(number_of_completions=len(orbit),automorphism_group_order=len(stabilizer)//len(orbit),
      global_number_of_partitions=12000//(len(stabilizer)//len(orbit)),
      representative=[[i for i in setbits(s)]for s in part]))
ans=dict(completions=len(sol),fixed_large_stabilizer=len(stabilizer),full_type_count=len(reps),types=reps)
print(json.dumps(ans,indent=2))
