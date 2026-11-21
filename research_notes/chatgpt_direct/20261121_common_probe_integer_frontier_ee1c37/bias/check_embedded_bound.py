"""Check the exact catalog inequality behind each weighted embedded bound."""
from pathlib import Path
from collections import Counter
import argparse,hashlib,json,sys
p=argparse.ArgumentParser();p.add_argument('--baseline',type=Path,required=True);p.add_argument('--plan',type=Path,required=True);p.add_argument('--output',type=Path,required=True);a=p.parse_args()
sys.path.insert(0,str(a.baseline.resolve()/'bias'))
from plan_extended import catalog,source
plan=json.loads(a.plan.read_text());q=plan['q'];assert catalog[12,1]=={1104:0,1116:0};assert catalog[13,1]=={1296:0}
rows=[];counts=Counter()
for P,E,floor,ceiling in plan['rows']:
 base_cost=sum(min(catalog[s,1])for s in E);extra=floor-base_cost;large=sum(s>=12 for s in E)
 assert extra in (0,12);assert extra==12*max(large-5,0)
 minimums=[min(q*c-d for c,d in catalog[s,1].items())for s in E]
 claimed=sum(minimums)+q*extra
 if extra:
  assert large==6 and 12 in E
  # The inherited six-large-mother lemma forces one 12-class to omit an
  # outer point: type (12,1116), whose signed difference is exactly zero.
  exact=min(sum(minimums)-minimums[i]+q*1116 for i,s in enumerate(E)if s==12)
 else:exact=sum(minimums)
 assert exact==claimed
 for s,m in zip(E,minimums):assert all(q*c-d>=m for c,d in catalog[s,1].items())
 counts[extra]+=1;rows.append({'P':P,'E':E,'floor':floor,'extra_cost':extra,'weighted_bound':claimed,'exact_separable_minimum_under_required_outer_deletion':exact})
result={'q':q,'profiles_checked':len(rows),'extra_cost_histogram':dict(counts),'twelve_embedded_catalog':catalog[12,1],'thirteen_embedded_catalog':catalog[13,1],'all_bounds_verified':True,'condition_for_extra_12':'Inherited six-large-mother geometry forces one outer-point deletion of a 12-point embedded class; a scalar total-cost lower bound alone would not justify the correction.','single_class_catalog_sha256':source['single_class_catalog_sha256'],'rows':rows}
a.output.write_text(json.dumps(result,indent=2,sort_keys=True)+'\n');print(json.dumps({k:v for k,v in result.items()if k!='rows'}),flush=True)
