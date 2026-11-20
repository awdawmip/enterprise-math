"""Bound the action imbalance at the only algebraic endpoint candidate."""
from itertools import product
from pathlib import Path
import json
from plan_extended import root,mod,catalog,minimum,profile_bounds,partitions
C=11593
maximum=-1;profiles=0;witness=None
for sizes in partitions(125,11):
 full=sizes.count(13)
 if full>=5:continue
 if sum(min(minimum.get((s,i),10000)for i in (0,1))for s in sizes)>C:continue
 levels=sorted(set(sizes));choices=[(0,)if s in (1,13)else range(sizes.count(s)+1)for s in levels]
 for counts in product(*choices):
  p=tuple(s for s,n in zip(levels,counts)for _ in range(n));e=tuple(s for s,n in zip(levels,counts)for _ in range(sizes.count(s)-n))
  if len(p)<4 or (len(p)==4 and sum(p)<42):continue
  if any(sum(e[-k:])>mod.bias.MOTHER_UNIONS[k]for k in range(1,len(e)+1)):continue
  large=e.count(12)+full
  if large>6:continue
  floor=sum(minimum[s,0]for s in p)+sum(minimum[s,1]for s in e)+12*max(large-5,0)
  if floor>C:continue
  slots=[(s,0)for s in p]+[(s,1)for s in e]
  if large==6:slots[slots.index((12,1))]=(12,2)
  d=profile_bounds(tuple(sorted(slots,reverse=True)),C-floor)[C-floor]
  profiles+=1
  if d>maximum:maximum=d;witness=[p,e,floor]
assert maximum<1611
result={'candidate_total':C,'candidate_difference':1611,'difference_upper_bound':maximum,'size_embedding_profiles':profiles,'maximizing_relaxed_profile':witness,'stable_weighted_radius':'301/1503','stable_p_interval':['601/1503','902/1503'],'requires_completed_q5_geometric_certificate':True}
target=Path(__file__).resolve().parent/'endpoint_result.json'
if target.exists():assert json.loads(target.read_text())==json.loads(json.dumps(result))
else:target.write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
print(json.dumps(result,indent=2,sort_keys=True))
