import geometry
from cyclic11 import observations
def orbits(count):
 a=geometry.linear_actions();bad,obs=observations();parents,centres=geometry.inventory(a,bad,obs)
 masks=[p^(1<<i) for p,i in zip(parents,centres)]
 canon=geometry.normalize(parents,centres,a)
 index={m:i for i,m in enumerate(masks)};base=masks[0]
 stab=[]
 for t in a:
  d=tuple((x-y)%5 for x,y in zip(geometry.P[centres[0]],geometry.P[t[centres[0]]]))
  both=tuple(geometry.shifted(geometry.P[j],d) for j in t)
  if geometry.image(base,both)==base:stab.append([index[geometry.image(m,both)] for m in masks])
 seen=set();global_keys=set();leaves=0
 def rec(prefix,remain):
  nonlocal leaves
  if len(prefix)==count:
   leaves+=1
   key=tuple(prefix)
   if key not in seen:
    seen.update(tuple(sorted(t[i]for i in prefix))for t in stab)
    global_keys.add(canon(prefix))
   return
  for j,i in enumerate(remain):
   rec(prefix+[i],[k for k in remain[j+1:] if not masks[i]&masks[k]])
 rec([0],[i for i,m in enumerate(masks)if i and not base&m])
 reps=[([masks[i] for i in ids], [centres[i] for i in ids])for ids in sorted(global_keys)]
 return leaves,len(seen),reps

def write_all(folder):
    counts = {}
    for k in range(1,7):
        fixed, seen, reps = orbits(k)
        assert fixed == seen
        counts[k] = len(reps)
        with (folder/f'cores{k}.txt').open('w') as out:
            for rows,centres in reps:
                remaining = ((1<<125)-1) ^ sum(rows)
                print(remaining % (1<<64), remaining>>64, *centres, file=out)
    assert list(counts.values()) == [1,6,22,61,19,4]
    return counts
