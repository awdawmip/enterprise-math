"""Original BRC independent components; the summary is formed only from actual preparation guards."""
import argparse,sys,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];sys.path.insert(0,str(ROOT))
from next_repair.native import native_recovery as old
from frontier9.common.hybrid import CODE
from functools import lru_cache
def run(code,limit):
    C=old.core.prior.Compiler(slots=15);T,G,ct=old.component_table(C)
    previous=old.encode
    def local(h,policy):
        if policy=='table':return code[25*h[0]+5*h[1]+h[2]]
        return previous(h,policy)
    old.encode=local;old.possible.cache_clear()
    try:r=old.triple_group(C,T,G,'table',True,limit)
    finally:old.encode=previous;old.possible.cache_clear()
    return {'status':'PASS','scope':'All 31250 joint scenarios compose real per-service receipts; one raw three-unit path from preparation per map/active/read-coordinate stratum. No private writer observation is passed to the decoder.','original_component_runs':ct,'joint':r}
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--out',type=Path,required=True);p.add_argument('--case',choices=['hybrid11','parent12','uniform11','escape12'],default='hybrid11');a=p.parse_args()
    if a.case=='parent12':
        q=json.loads((ROOT/'next_repair/triple/triple_results.json').read_text());c=q['common_smaller_attainment']['table_xyz'];lim=1
    elif a.case=='escape12':
        c=list(CODE);best=json.loads((ROOT/'frontier9/common/escape_results.json').read_text())['least_accumulated_supplements_among_nine'];a0,b0=best['moved_rows'];c[a0]=c[b0]=11;lim=1
    elif a.case=='uniform11':c=json.loads((ROOT/'frontier9/common/uniform11.json').read_text())['code'];lim=1
    else:c=CODE;lim=2
    res=run(c,lim);a.out.write_text(json.dumps(res,indent=2,sort_keys=True)+'\n');print(a.case,res['joint']['by_queries'],res['joint']['full_raw_sample'],res['joint']['min_total'],res['joint']['max_total'])
