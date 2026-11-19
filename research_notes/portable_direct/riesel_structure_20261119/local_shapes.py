"""Exact radius-two phase surgery around the original square Riesel cover.

Use u=(n-1)/2 for positive odd n. The domain is Z/3360 and each labelled
prime contributes one residue class modulo its effective u-period. This
script exhausts every one- and two-coordinate change from the original.
"""
from __future__ import annotations

from itertools import combinations
import json
from math import lcm
from pathlib import Path


def main():
    directory = Path(__file__).resolve().parent
    source = directory.with_name('riesel_mixed_20261119') / 'certificate.json'
    rows = json.loads(source.read_text())['original']['rows']
    periods = [r['order']//2 if r['order']%2==0 else r['order'] for r in rows]
    phases = [((r['exponent_phase']-1)//2)%e if r['order']%2==0
              else ((r['exponent_phase']-1)*pow(2,-1,e))%e
              for r,e in zip(rows,periods)]
    period=lcm(*periods)
    full=(1<<period)-1
    # One extra zero mask represents any root residue with no odd-index hit
    # in that prime channel (for example a=0 modulo p).
    masks=[[sum(1<<u for u in range(c,period,e)) for c in range(e)]+[0] for e in periods]
    old=[m[c] for m,c in zip(masks,phases)]
    def union(inds):
        result=0
        for i in inds: result |= old[i]
        return result
    assert union(range(len(rows)))==full
    single=[]; pair=[]; total_candidates=0
    for i in range(len(rows)):
        holes=full^union(j for j in range(len(rows)) if j!=i)
        assert holes
        for c,mask in enumerate(masks[i]):
            if c != phases[i] and mask&holes==holes:
                single.append({'i':i,'p':rows[i]['p'],'phase':c})
    for i,j in combinations(range(len(rows)),2):
        holes=full^union(k for k in range(len(rows)) if k not in (i,j))
        for ci,mi in enumerate(masks[i]):
            if ci==phases[i]:continue
            remaining=holes & ~mi
            for cj,mj in enumerate(masks[j]):
                if cj==phases[j]:continue
                total_candidates += 1
                if remaining & ~mj == 0:
                    # The complete enumeration establishes that no valid
                    # radius-two result makes an odd channel inactive.
                    assert ci<periods[i] and cj<periods[j]
                    new=list(phases);new[i]=ci;new[j]=cj
                    pair.append({'indices':[i,j],'primes':[rows[i]['p'],rows[j]['p']],
                                 'old_phases':[phases[i],phases[j]],'new_phases':[ci,cj],
                                 'u_phases':new})
    def canonical(vec):
        return min(tuple((c+t)%e for c,e in zip(vec,periods)) for t in range(period))
    candidates=[phases]+[x['u_phases'] for x in pair]
    canon={canonical(v) for v in candidates}
    result={'schema':'RIESEL_EXACT_LOCAL_PHASE_SURGERY_V1','researcher_id':'EM-DIRECT-970E1C',
            'period':period,'primes':[r['p'] for r in rows], 'effective_periods':periods,
            'original_u_phases':phases,
            'inactive_odd_channel_included':True,
            'single_change_population':sum(periods),'single_valid':single,
            'single_active_only_population':sum(e-1 for e in periods),
            'double_active_only_population':sum((periods[i]-1)*(periods[j]-1) for i,j in combinations(range(len(rows)),2)),
            'double_change_population':total_candidates,'double_valid_count':len(pair),
            'double_valid':pair,'translation_classes_in_radius2':len(canon),
            'canonical_representatives':[list(v) for v in sorted(canon)]}
    (directory / 'local_shapes_results.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k not in ('double_valid','canonical_representatives')},indent=2))
    for row in pair: print(row['primes'],row['old_phases'],'->',row['new_phases'])


if __name__=='__main__':main()
