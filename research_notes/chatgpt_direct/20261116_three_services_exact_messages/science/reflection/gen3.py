from collections import Counter,defaultdict
from itertools import combinations_with_replacement
from pathlib import Path
from geom import G,image
D=Path(__file__).parent
T={(a,b):n for a,b,n in (map(int,l.split()) for l in (D/'fixed_again.txt').open()) if b>0}
shapes=[tuple(sorted(s,key=lambda t:T[t])) for s in combinations_with_replacement(T,5) if sum(a for a,b in s)==25 and sum(b for a,b in s)>=17]
types={s[0] for s in shapes};allrep=defaultdict(set)
for l in (D/'fixed_all_masks.txt').open():
 hi,lo,a,b=map(int,l.split());t=(a,b)
 if t in types:allrep[t].add((hi<<64)|lo)
with (D/'rare.txt').open('w') as fw:
 for t,S in allrep.items():
  while S:
   z=min(S);orb={image(z,g) for g in G};assert orb<=S
   S-=orb
   print(*t,z>>64,z%(1<<64),file=fw)
with (D/'shapes.txt').open('w') as f:
 for sh in shapes:print(*(16*a+b for a,b in sh),file=f)
print('shapes',len(shapes),'first_counts',{k:T[k] for k in types},'total_reps',len((D/'rare.txt').read_text().splitlines()))
