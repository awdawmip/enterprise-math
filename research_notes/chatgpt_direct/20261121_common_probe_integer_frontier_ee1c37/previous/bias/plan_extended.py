from pathlib import Path
from functools import cache
from itertools import product
import importlib.util,json,time
root=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location('bias_geometric',root/'previous/bias_geometry/replay.py')
mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod)
previous=root/'previous/previous'
import sys
sys.path.insert(0,str(previous/'mothers'))
from costs import partitions
catalog,visits,checksum=mod.bias.census(previous)
source=json.loads((root/'previous/bias/result.json').read_text())
assert checksum==source['single_class_catalog_sha256']
catalog[12,2]={1116:0}
minimum={key:min(prices) for key,prices in catalog.items()}
@cache
def profile_bounds(slots,slack):
 if not slots:return (0,)+(-1,)*slack
 prefix=profile_bounds(slots[:-1],slack);key=slots[-1];out=[-1]*(slack+1)
 for price,difference in catalog[key].items():
  spent=price-minimum[key]
  for i in range(slack-spent+1):
   if prefix[i]>=0:out[spent+i]=max(out[spent+i],prefix[i]+difference)
 return tuple(out)
def dangerous(q):
 cap=mod.bias.OPTIMAL+(source['global_difference_cap']-mod.bias.OPTIMAL_DIFFERENCE)//q
 todo=[]
 for sizes in partitions(125,11):
  full=sizes.count(13)
  if full>=5 or (full==4 and cap<11365):continue
  if sum(min(minimum.get((s,i),10000)for i in (0,1))for s in sizes)>cap:continue
  levels=sorted(set(sizes));possible=[(0,)if s in (1,13)else range(sizes.count(s)+1)for s in levels]
  for counts in product(*possible):
   p=tuple(s for s,n in zip(levels,counts)for _ in range(n));e=tuple(s for s,n in zip(levels,counts)for _ in range(sizes.count(s)-n))
   if len(p)<4 or (len(p)==4 and sum(p)<42):continue
   if any(sum(e[-k:])>mod.bias.MOTHER_UNIONS[k]for k in range(1,len(e)+1)):continue
   large=e.count(12)+full
   if large>6:continue
   embedded_floor=sum(minimum[s,1]for s in e)+12*max(large-5,0)
   floor=embedded_floor+sum(minimum[s,0]for s in p)
   if floor>cap:continue
   slots=[(s,0)for s in p]+[(s,1)for s in e]
   if large==6:slots[slots.index((12,1))]=(12,2)
   diffs=profile_bounds(tuple(sorted(slots,reverse=True)),cap-floor)
   risk=[c for c in range(max(floor,mod.bias.FIRST_OTHER,11365 if full==4 else 0),cap+1)if diffs[c-floor]>=mod.bias.OPTIMAL_DIFFERENCE+q*(c-mod.bias.OPTIMAL)]
   if risk:todo.append((p,e,embedded_floor,max(risk)))
 return cap,todo
if __name__=='__main__':
 for q in [25,20,15,10]:
  start=time.time();cap,todo=dangerous(q)
  print(json.dumps({'q':q,'cap':cap,'profiles':len(todo),'last_budget':max(c for p,e,f,c in todo),'keys':sorted(set((len(e),sum(e))for p,e,f,c in todo)),'elapsed':time.time()-start}),flush=True)
  (root/'bias'/f'profiles_q{q}.json').write_text(json.dumps(todo,indent=2)+'\n')
