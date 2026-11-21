"""Independent integer reconstruction of the complete E=3 exact9865 split."""
from collections import Counter
from functools import lru_cache
from itertools import combinations_with_replacement
from pathlib import Path
import json

HERE=Path(__file__).resolve().parent


def verify(mother):
    expected=json.loads((HERE/'exact_cost_E3_9865.json').read_text())
    catalog={}
    for line in (mother/'catalog.txt').read_text().splitlines():
        n,e,c,d=map(int,line.split());catalog.setdefault((e,n),set()).add(c)
    minimum={key:min(value) for key,value in catalog.items()}
    @lru_cache(None)
    def proper_min(count,total,smallest):
        if not count:return 0 if total==0 else 10**9
        if total<count*smallest or total>12*count:return 10**9
        return min((minimum[0,n]+proper_min(count-1,total-n,n) for n in range(smallest,13) if (0,n) in minimum),default=10**9)
    profiles=[]
    def choose_proper(count,total,smallest,spent,chosen,embedded,embedded_min):
        if spent+proper_min(count,total,smallest)+embedded_min>9865:return
        if not count:
            assert total==0;profiles.append((tuple(embedded),tuple(chosen)));return
        for n in range(smallest,13):
            if (0,n) in minimum:choose_proper(count-1,total-n,n,spent+minimum[0,n],chosen+[n],embedded,embedded_min)
    for embedded in combinations_with_replacement(range(1,14),3):
        if all((1,n) in minimum for n in embedded):
            embedded_min=sum(minimum[1,n] for n in embedded)
            choose_proper(9,125-sum(embedded),2,0,[],embedded,embedded_min)
    assert len(profiles)==len(set(profiles))==9
    recorded={(tuple(r['profile']['embedded_sizes']),tuple(r['profile']['proper_sizes'])):r for r in expected['size_profiles']}
    assert set(profiles)==set(recorded)
    delta={(r['size'],r['cost']):r['maximum_defect_upper_bound'] for r in json.loads((HERE/'cost_defect_catalog.json').read_text())['rows']}
    all_survivors=set();enumerated=0;summary=[]
    for embedded,proper in sorted(profiles):
        slots=[(1,n) for n in embedded]+[(0,n) for n in proper]
        base=sum(minimum[key] for key in slots);extra=9865-base
        maxima=[];surviving=set();all_typed=set()
        def prices(at,left,defect,chosen):
            nonlocal enumerated
            if at==12:
                if left:return
                pattern=tuple(sorted(Counter(chosen).items()));assert pattern not in all_typed
                all_typed.add(pattern);maxima.append(defect);enumerated+=1
                if defect>=6:surviving.add(pattern)
                return
            key=slots[at];e,n=key
            lowest=chosen[-1][2] if at and slots[at-1]==key else -1
            for c in sorted(catalog[key]):
                increase=c-minimum[key]
                if c>=lowest and increase<=left:
                    prices(at+1,left-increase,defect+(0 if e else delta[n,c]),chosen+[(e,n,c)])
        prices(0,extra,0,[])
        maximum=max(maxima,default=None);saved=recorded[embedded,proper]
        assert maximum==saved['maximum_proper_defect_at_exact_price']
        assert len(surviving)==saved['surviving_typed_profiles']
        all_survivors.update(surviving)
        summary.append({'embedded':embedded,'proper':proper,'extra':extra,'max_defect':maximum,
                        'typed_price_patterns':len(all_typed),'surviving_patterns':len(surviving)})
    expected_patterns={tuple(sorted((((int(t['embedded']),t['size'],t['cost']),t['count']) for t in r['types']))) for r in expected['surviving_typed_profiles']}
    assert all_survivors==expected_patterns and len(all_survivors)==8
    core=[];residual=[]
    for pattern in sorted(all_survivors):
        is_core=all((n,c) in ((12,1104),(13,1296)) for (e,n,c),count in pattern if e)
        combined=Counter()
        for (e,n,c),count in pattern:combined[n,c]+=count
        tag='_'.join(f'{n}-{c}-{count}' for (n,c),count in sorted(combined.items()))
        (core if is_core else residual).append(tag)
    integer=json.loads((HERE/'e3/integer_receipts.json').read_text())
    assert set(residual)=={r['tag'] for r in integer} and len(residual)==2 and len(core)==6
    assert all(r['found']==0 and r['cost']==9865 for r in integer)
    inherited=json.loads((HERE/'e3/core_three_dependency_result.json').read_text())
    assert inherited['scope']=='exactly 3 cores' and inherited['excluded_through']==9880 and inherited['branches']==134
    assert len(inherited['cases'])==134 and all(r['solutions']==0 for r in inherited['cases'])
    assert sum(r['nodes'] for r in inherited['cases'])==inherited['nodes']==96050105
    return {'independently_enumerated_size_profiles':9,'exact_price_patterns_enumerated':enumerated,
            'capacity_survivors':8,'inherited_exact_three_core_exclusions':6,'native_residual_types':2,
            'size_profile_audit':summary,'exact_E3_cost9865_exclusion_closed':True,
            'scope':'The arithmetic split is independently recomputed. Six patterns inherit the published exactly-three-core theorem; the other two are replayed by replay.py. The96,050,105 inherited core-search nodes are not rerun.'}
