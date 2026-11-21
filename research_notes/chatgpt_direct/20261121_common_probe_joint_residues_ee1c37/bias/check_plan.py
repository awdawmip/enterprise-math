"""Regenerate the complete q=3 dangerous-profile plan, independently of cache."""
from pathlib import Path
import argparse,hashlib,json,sys,time
p=argparse.ArgumentParser();p.add_argument('--baseline',type=Path,required=True);p.add_argument('--plan',type=Path,required=True);p.add_argument('--output',type=Path,required=True);a=p.parse_args()
sys.path.insert(0,str(a.baseline.resolve()/'bias'))
from plan_extended import dangerous,source,catalog
start=time.time();saved=json.loads(a.plan.read_text());q=saved['q'];cap,rows=dangerous(q)
assert cap==saved['cap'];assert json.loads(json.dumps(rows))==saved['rows']
keys=sorted({(len(e),sum(e))for p,e,f,c in rows})
out={'q':q,'cap':cap,'profiles':len(rows),'last_dangerous_budget':max(c for p,e,f,c in rows),'normalized_mother_keys':keys,'profile_sha256':hashlib.sha256(json.dumps(rows,separators=(',',':')).encode()).hexdigest(),'plan_file_sha256':hashlib.sha256(a.plan.read_bytes()).hexdigest(),'global_difference_cap':source['global_difference_cap'],'independently_regenerated':True,'elapsed_seconds':time.time()-start}
a.output.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n');print(json.dumps(out),flush=True)
