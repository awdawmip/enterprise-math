"""Independent multiset polynomial check of the exact9866 price frontier.

This replaces slot-by-slot price recursion by one generating function per
size/embedding multiplicity, then convolves those functions. Geometry remains
the responsibility of the separate native-cover receipts.
"""
import argparse
from collections import Counter,defaultdict
from hashlib import sha256
import importlib.util
import json
from pathlib import Path

HERE=Path(__file__).resolve().parent


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--mother',type=Path,default=HERE.parent/'integer_cuts/mother12')
    p.add_argument('--defect',type=Path,default=HERE.parent/'mother_sublevels_D')
    p.add_argument('--frontier',type=Path,default=HERE/'typed_frontier.json')
    p.add_argument('--output',type=Path,required=True)
    args=p.parse_args()
    expected=json.loads(args.frontier.read_text())
    hashes={Path(r['path']).name:r['sha256'] for r in expected['dependencies']}
    for source in (args.mother/'plan.py',args.mother/'catalog.txt',args.defect/'cost_defect_catalog.json'):
        assert sha256(source.read_bytes()).hexdigest()==hashes[source.name],source
    spec=importlib.util.spec_from_file_location('plan_dp',args.mother/'plan.py')
    plan=importlib.util.module_from_spec(spec);spec.loader.exec_module(plan)
    data=plan.catalogue();minimum={k:min(v) for k,v in data.items()}
    defs={(r['size'],r['cost']):r['maximum_defect_upper_bound']
          for r in json.loads((args.defect/'cost_defect_catalog.json').read_text())['rows']}
    constants={8:419,9:557,10:744,11:993,12:1226}
    by_sizes={(tuple(r['embedded_sizes']),tuple(r['proper_sizes'])):r for r in expected['size_summary']}
    rows=plan.make_rows(9866,minimum);assert len(rows)==102
    checked=[];cache={}
    def group(size,embedded,count,budget,required):
        key=size,embedded,count,budget,required
        if key in cache:return cache[key]
        state={(0,0,0,0):1}
        for price in sorted(data[size,embedded]):
            extra=price-minimum[size,embedded]
            if extra>budget:break
            delta=0 if embedded else defs.get((size,price),min(3*(size-2),(price-constants[size])//3))
            core=int((size,price) in ((12,1104),(13,1296)))
            nxt=defaultdict(int)
            for (n,c,d,k),ways in state.items():
                for copies in range(count-n+1):
                    nc=c+copies*extra
                    if nc>budget:break
                    nxt[n+copies,nc,min(required,d+copies*delta),k+copies*core]+=ways
            state=nxt
        answer={(c,d,k):ways for (n,c,d,k),ways in state.items() if n==count}
        cache[key]=answer;return answer
    for row in rows:
        e=row['embedded_count']
        if not row['unrestricted_union_bound_passes'] or e==2:continue
        key=tuple(row['embedded_sizes']),tuple(row['proper_sizes'])
        budget=9866-row['minimum_total_cost'];required=3*max(5-e,0)
        groups=Counter((s,1) for s in row['embedded_sizes'])+Counter((s,0) for s in row['proper_sizes'])
        state={(0,0,0):1}
        for (size,embedded),multiplicity in sorted(groups.items()):
            option=group(size,embedded,multiplicity,budget,required)
            nxt=defaultdict(int)
            for (c,d,k),ways in state.items():
                for (cc,dd,kk),count in option.items():
                    if c+cc<=budget:nxt[c+cc,min(required,d+dd),k+kk]+=ways*count
            state=nxt
        totals=Counter()
        for (c,d,k),ways in state.items():
            if c!=budget:continue
            totals['all']+=ways
            if d<required:totals['centre_defect']+=ways
            elif k>=3:totals['inherited_core_bound']+=ways
            else:totals['survivors']+=ways
        original=by_sizes[key]
        for name in ('all','centre_defect','inherited_core_bound'):
            assert totals[name]==original['counts'].get(name,0),(key,name,totals,original)
        assert totals['survivors']==original['surviving_typed_patterns'],key
        checked.append({'embedded_count':e,'embedded_sizes':key[0],'proper_sizes':key[1],'counts':dict(totals)})
    result={'independent_price_dp_passed':True,'cost':9866,'full_size_profiles':len(rows),
            'price_checked_size_profiles':len(checked),
            'exact_typed_price_patterns':sum(r['counts'].get('all',0) for r in checked),
            'surviving_typed_patterns':sum(r['counts'].get('survivors',0) for r in checked),
            'by_embedded_count':{},'rows':checked,
            'scope':'Price arithmetic only; no claim of native geometric exclusion.'}
    for e in range(3,8):
        result['by_embedded_count'][str(e)]={name:sum(r['counts'].get(name,0) for r in checked if r['embedded_count']==e)
            for name in ('all','centre_defect','inherited_core_bound','survivors')}
    assert result['exact_typed_price_patterns']==1454 and result['surviving_typed_patterns']==117
    args.output.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k!='rows'},sort_keys=True))


if __name__=='__main__':
    main()
