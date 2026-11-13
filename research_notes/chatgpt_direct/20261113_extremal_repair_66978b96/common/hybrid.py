"""Exact decision trees for a safe 11-message fallback on the common three-copy source."""
from itertools import product,combinations
from collections import defaultdict,Counter
from pathlib import Path
import argparse,json
P=list(product(range(5),repeat=3))
CODE=[1,9,10,3,8,7,6,4,2,6,5,6,0,5,6,5,7,10,5,2,1,9,4,3,8,2,5,0,6,8,3,3,4,7,0,9,2,9,3,8,3,3,1,1,7,10,5,4,6,10,4,7,7,3,4,1,10,5,10,5,9,10,9,10,2,6,1,6,0,1,7,0,10,3,8,1,9,4,0,2,8,0,5,8,5,7,4,3,4,3,6,4,6,4,8,10,9,2,2,10,4,5,10,6,4,2,8,8,9,9,1,9,3,7,3,0,2,10,9,9,1,5,0,6,7]
def run():
    counts=Counter();ob=Counter();trip=set();penalty=0;exception=[]
    for d in (1,3):
        for starts in P:
            groups=defaultdict(list)
            for h,t in enumerate(P):
                acts=tuple(k for k in range(3)if (t[k]-starts[k])%5 in (0,d))
                y=tuple(int(t[k]!=starts[k])for k in acts);groups[(CODE[h],acts)].append((h,y))
            for (color,act),rows in groups.items():
                outputs=set(y for i,y in rows);n=len(outputs);ob[n]+=1
                if n==1:counts[0]+=len(rows);continue
                if n==2:counts[1]+=len(rows);continue
                assert n==3 and len(rows)==3
                trip.add(tuple(x for x,o in rows))
                idx=next(i for i in range(len(act)) if len({y[i]for y in outputs})==2)
                layer=Counter(y[idx]for y in outputs)
                for _,y in rows:
                    sub={v for v in outputs if v[idx]==y[idx]}
                    if len(sub)==1:counts[1]+=1
                    else:
                        assert any(len({z[k]for z in sub})==2 for k in range(len(act)) if k!=idx)
                        counts[2]+=1
                exception.append({'step':d,'start':starts,'message':color,'active':act,'rows':rows})
    assert sorted(counts.items())==[(0,19174),(1,12056),(2,20)] and len(trip)==2
    return dict(status='PASS',scope='eleven messages, at most two endpoint reads, for a stated code; code-specific profile, no claim of a uniform single-read solution or of optimal total among 11-message codes',code_xyz=CODE,read_histogram=dict(sorted(counts.items())),scenarios=sum(counts.values()),ambiguous_receipt_types=dict(sorted(ob.items())),distinct_forbidden_monochromatic_triples=sorted(trip),exceptional_visible_world_groups=exception,total_reads=sum(k*v for k,v in counts.items()))
if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--out',type=Path,default=Path(__file__).with_name('hybrid_results.json'));opts=ap.parse_args();d=run();opts.out.write_text(json.dumps(d,indent=2)+'\n');print('PASS',d['read_histogram'])
