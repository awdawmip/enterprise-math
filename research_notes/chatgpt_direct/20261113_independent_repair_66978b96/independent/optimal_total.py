"""All four-message encodings up to first-row, row-order, column and color symmetries."""
import argparse,json
from collections import Counter
from itertools import product
from pathlib import Path
from independent_geometry import ACTIONS, evaluate
def run():
    rows=list(product(range(4),repeat=5));idx={r:i for i,r in enumerate(rows)}
    def canonical(r):
        parts=sorted((r.count(v) for v in set(r)),reverse=True)
        return tuple(i for i,n in enumerate(parts) for _ in range(n))
    roots=sorted({idx[canonical(r)] for r in rows})
    def compatible(a,b):return all(u!=v or (a.count(u)==b.count(v)==1) for u,v in zip(a,b))
    adj=[sum(1<<j for j,b in enumerate(rows) if compatible(a,b)) for a in rows]
    assert all(not (v>>i&1) for i,v in enumerate(adj))
    pairhist=Counter();tools=Counter();first_counts=[]
    def walk(path,can):
        if len(path)==5:
            C=[rows[i]for i in path]
            result=evaluate(C,ACTIONS)
            assert 'invalid_class' not in result
            pairhist[result['read_hist']['1']]+=1
            tools[tuple(sorted(Counter(x for row in C for x in row).values()))]+=1
            return 1
        ans=0
        while can:
            if can.bit_count()<5-len(path):break
            lo=can&-can;can-=lo;i=lo.bit_length()-1
            ans+=walk(path+[i],can&adj[i])
        return ans
    for i in roots:first_counts.append([list(rows[i]),walk([i],adj[i])])
    assert pairhist=={950:64} and tools=={(6,6,6,7):64}
    return dict(status='PASS',root_and_survivors=first_counts,number_of_representatives=sum(pairhist.values()),joint_inputs_per_candidate=2500,one_probe_minimum_total=950,one_probe_cases_per_solver_class=dict(pairhist),zero_probe_cases=1550,word_bits=2,scope='All valid deterministic four-message, one-worst-probe controllers; supplemental reads per history/menu/writer uniformly counted. No optimality assertion for the weighted native command max.')
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--out',type=Path,default=Path(__file__).with_name('optimal_total_results.json'))
    d=run();p.parse_args().out.write_text(json.dumps(d,indent=1,sort_keys=True)+'\n');print('PASS',d['number_of_representatives'],d['one_probe_minimum_total'])
