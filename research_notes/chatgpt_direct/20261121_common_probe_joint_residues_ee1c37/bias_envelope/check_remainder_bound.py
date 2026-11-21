"""Verify every Bellman upper-bound inequality for the remaining-class table."""
from pathlib import Path
import argparse,hashlib,json
p=argparse.ArgumentParser(description=__doc__);p.add_argument('--table',type=Path,required=True);p.add_argument('--catalog',type=Path,required=True);p.add_argument('--output',type=Path,required=True);a=p.parse_args();cap=6410
lines=a.catalog.read_text().splitlines();assert int(lines[0])==len(lines)-1;types={9:[],10:[],11:[]}
for line in lines[1:]:
 s,c,d=map(int,line.split());assert s in types and c>=d>=0 and (c-d)%2==0;types[s].append((c,d))
T={(i,j,k):{}for i in range(2)for j in range(3)for k in range(5)}
for line in a.table.read_text().splitlines():
 i,j,k,c,d=map(int,line.split());assert 0<=c<=cap and d>=0 and c not in T[i,j,k];T[i,j,k][c]=d
assert T[0,0,0]=={0:0}
checks=0
for counts,current in T.items():
 for pos,s in enumerate([9,10,11]):
  if not counts[pos]:continue
  before=list(counts);before[pos]-=1
  for cost,value in T[tuple(before)].items():
   for price,diff in types[s]:
    if cost+price>cap:continue
    assert current.get(cost+price,-1)>=value+diff,(counts,s,cost,price)
    checks+=1
assert T[1,2,4][6410]==1026
out={'table_sha256':hashlib.sha256(a.table.read_bytes()).hexdigest(),'catalog_sha256':hashlib.sha256(a.catalog.read_bytes()).hexdigest(),'configurations':len(T),'nonnegative_cells':sum(len(t)for t in T.values()),'bellman_upper_inequalities':checks,'base_state_verified':True,'root_remaining_cost':6410,'root_upper_absolute_difference_sum':1026,'all_upper_bounds_certified':True,'scope':'For every possible remaining class multiset of the stated sizes and exact cost, the sum of absolute differences is bounded by this table; unreachable cells are also certified by induction.'}
a.output.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n');print(json.dumps(out),flush=True)
