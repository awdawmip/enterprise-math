#!/usr/bin/env python3
"""R86 independent exact extreme-ray bound: pure Python integer arithmetic."""
from itertools import combinations
from math import gcd
from functools import reduce
rows=[(1,0,0),(0,1,0),(0,0,1),(2,6,12),(6,24,60),(14,78,252),(4,18,48),(12,72,240),(8,54,192)]
def cross(a,b):return(a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def primitive(v):
 d=reduce(gcd,v);w=tuple(k//d for k in v)
 return tuple(-k for k in w) if next(k for k in w if k)<0 else w
def q(v):return max(sum(max(0,x) for x in v),sum(max(0,-x) for x in v))
lines={primitive(v) for a,b in combinations(rows,2) if any(v:=cross(a,b))}
rays=sorted(lines|{tuple(-x for x in v) for v in lines})
images=[tuple(sum(x*y for x,y in zip(row,v)) for row in rows) for v in rays]
def conformal(i,j):return all(a*b>=0 for a,b in zip(images[i],images[j]))
pairs=[[conformal(i,j) for j in range(len(rays))] for i in range(len(rays))]
triples=[(i,j,k) for i,j,k in combinations(range(len(rays)),3) if pairs[i][j] and pairs[i][k] and pairs[j][k]]
res={'primitive_lines':len(lines),'oriented_rays':len(rays),'conformal_triples':len(triples),'largest_ray_q':max(map(q,rays)),'largest_triplet_q_sum':max(sum(q(rays[i]) for i in t) for t in triples)}
assert res==dict(primitive_lines=28,oriented_rays=56,conformal_triples=212,largest_ray_q=125,largest_triplet_q_sum=235)
import json
print(json.dumps(res,sort_keys=True))
atlas=[(1,0,0),(0,2,-1),(1,-3,1),(2,-3,1),(3,-1,0),(1,3,-1),(3,-4,1),(4,-1,0),
       (3,2,-1),(4,-4,1),(5,-1,0),(4,-4,1),(6,-1,0),(3,-7,2),(6,-4,1),(7,-1,0),
       (7,2,-1),(9,-5,1),(10,-5,1),(15,-6,1),(21,-7,1),(24,-14,3),(36,-16,3),
       (39,-20,4),(42,-24,5),(45,-21,4),(66,-28,5),(114,-56,11)]
# The exact R72 atlas entry at index 11 is (5,-4,1), not (4,-4,1).
atlas[11]=(5,-4,1)
core_indices={14,17,18,19,21,22,23,25,27}
def halfgap(v):
 x,y,z=v;t=(0,2*x+6*y+12*z,6*x+24*y+60*z,14*x+78*y+252*z)
 return tuple(abs(t[i]-t[j])//2 for i in range(4) for j in range(i+1,4))
gaps=list(map(halfgap,atlas))
dominators={i:next((j for j in sorted(core_indices) if all(x<=y for x,y in zip(gaps[j],gaps[i]))),None)
            for i in range(28) if i not in core_indices}
assert len([i for i in dominators if dominators[i] is not None])==17
assert {i for i in dominators if dominators[i] is None}=={24,26}
print(json.dumps({'atlas_size':len(atlas),'core_size':len(core_indices),'coordinate_dominated':17,
 'two_exceptions':[{'index':i,'vector':atlas[i],'halfgap':gaps[i]} for i in (24,26)],
 'dominator_index_mapping':{str(i):j for i,j in dominators.items() if j is not None}},sort_keys=True))
