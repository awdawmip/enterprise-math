"""EC49FBZ: exact early-four-slot native-X6 BRC prefix-union computation.
Imports the immutable EC49FBY generator at the adjacent directory; standard-library only.
"""
from pathlib import Path
from itertools import combinations
import sys, json
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'EC49FBY_COMPLETE_TRIPLE_RIGIDITY'))
from VERIFY_EC49FBY import build

BASELINE = 158
PIN = 'fc0f038e7bfd12c886b4d37f900bfb770c0f61ab'

def run():
    chosen, early, late, pools, single = build()
    assert len(early) == 10 and len(single) == 24
    report = []
    all_raw = all_eval = pair_pruned = triple_pruned = 0
    for slots in combinations(early,4):
        remaining = 0
        for key,v in single.items():
            if key not in slots:
                remaining |= v
        base = remaining.bit_count()
        limit = BASELINE - base
        filtered = [[v & ~remaining for v in pools[k] if (v & ~remaining).bit_count()<limit] for k in slots]
        order = sorted(range(4), key=lambda j:len(filtered[j]))
        a,b,c,d = [filtered[j] for j in order]
        raw = 1
        for k in slots:raw *= len(pools[k])
        all_raw += raw
        checked = pairs = triples = 0
        optimum = BASELINE
        for x in a:
            for y in b:
                xy = x|y
                if xy.bit_count()>=limit:
                    pairs += 1
                    continue
                for z in c:
                    xyz = xy|z
                    if xyz.bit_count()>=limit:
                        triples += 1
                        continue
                    for w in d:
                        checked += 1
                        optimum = min(optimum,base+(xyz|w).bit_count())
        all_eval += checked
        pair_pruned += pairs
        triple_pruned += triples
        report.append({'slots':slots,'rest_edges':base,'raw':raw,
                       'strict_candidates':[len(z) for z in filtered],
                       'pair_pruned':pairs,'triple_pruned':triples,
                       'fourth_evaluations':checked,'minimum':optimum})
    result = {'schema':'EC49FBZ_EARLY_FOUR_EXCHANGE_EXACT_V1','pin':PIN,
              'source':'EC49FBY@5b10f1c296cb8826d4b69f6fd83dba89d765df1c',
              'baseline':BASELINE,'groups':len(report),
              'unpruned_four_tuples':all_raw,'exact_fourth_evals':all_eval,
              'pair_pruned':pair_pruned,'triple_pruned':triple_pruned,
              'minimum':min(z['minimum'] for z in report), 'per_group':report}
    assert (result['groups'],all_raw,all_eval,pair_pruned,triple_pruned,result['minimum']) == (210,24708240,3001,792,1577,158)
    destination = Path(__file__).with_name('EXACT_REPORT_EC49FBZ.json')
    destination.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print('PASS EC49FBZ',len(report),'quartets',result['minimum'],'edges',all_eval,'fourth evaluations')
    return result
if __name__=='__main__':run()
