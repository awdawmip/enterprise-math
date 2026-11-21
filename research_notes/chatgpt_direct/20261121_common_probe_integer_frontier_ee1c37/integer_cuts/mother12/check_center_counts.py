"""Exact substitution of the proved center-count bound into the complete plan."""
from pathlib import Path
from hashlib import sha256
import json

HERE=Path(__file__).resolve().parent
raw=(HERE/'plan_9995.json').read_bytes();plan=json.loads(raw)
assert plan['budget']==9995 and len(plan['profiles'])==2194
excluded=[];skipped=0;by_e={}
for row in plan['profiles']:
    p=row['proper_sizes'];e=row['embedded_count']
    by_e[e]=by_e.get(e,0)+1
    if min(p)<8:
        skipped+=1;continue
    lower=row['minimum_total_cost']-15*p.count(11)-18*p.count(12)+9*max(5-e,0)
    if lower>9995:
        excluded.append({'proper_sizes':p,'embedded_sizes':row['embedded_sizes'],
                         'minimum_total_cost':row['minimum_total_cost'],'center_bound':lower})
assert skipped==229 and len(excluded)==2
e3=[r for r in excluded if len(r['embedded_sizes'])==3]
assert e3==[{'proper_sizes':[8]+[10]*7+[11],'embedded_sizes':[10,13,13],
            'minimum_total_cost':9995,'center_bound':9998}]
result={'complete':True,'plan_sha256':sha256(raw).hexdigest(),'profiles':2194,
        'profiles_with_proper_size_below_8_not_using_this_bound':skipped,
        'excluded_by_center_bound':excluded,
        'basis':'center_count_lemma.md plus native_sublevels mixed-bound certificate',
        'review_status':'NOT_REVIEWED'}
(HERE/'center_count_verification.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
