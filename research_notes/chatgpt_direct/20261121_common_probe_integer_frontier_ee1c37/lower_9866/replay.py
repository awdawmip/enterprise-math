"""Verify the complete cost9866 exclusion, or rerun all native profiles."""
import argparse
from hashlib import sha256
import json
from pathlib import Path
import subprocess
import sys

HERE=Path(__file__).resolve().parent


def digest(path):
    return sha256(path.read_bytes()).hexdigest()


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--mother',type=Path,default=HERE.parent/'integer_cuts/mother12')
    p.add_argument('--defect',type=Path,default=HERE.parent/'mother_sublevels_D')
    p.add_argument('--marginal',type=Path,default=HERE.parent/'marginal_bound')
    p.add_argument('--lower',type=Path,default=HERE.parent/'lower')
    p.add_argument('--previous',type=Path,default=HERE.parent/'previous')
    p.add_argument('--prior',type=Path,default=HERE.parent/'lower_9865')
    p.add_argument('--native-inputs',type=Path)
    p.add_argument('--mode',choices=['audit','full'],default='audit')
    p.add_argument('--output',type=Path,required=True)
    args=p.parse_args();args.output=args.output.resolve();args.output.mkdir(parents=True,exist_ok=True)
    roots={name:getattr(args,name).resolve() for name in ('mother','defect','marginal','lower','previous','prior')}
    bindings=json.loads((HERE/'bindings.json').read_text())
    for dep in bindings['dependencies']:
        assert digest(roots[dep['root']]/dep['path'])==dep['sha256'],dep
    assert digest(HERE/'original_driver.py')==bindings['driver_sha256']
    prior=json.loads((roots['prior']/'verification/result.json').read_text())
    assert prior['complete'] and prior['new_global_lower_bound']==9866
    start=json.loads((roots['marginal']/'verification.json').read_text())
    assert start['all_checks_passed'] and start['exact_two_embedded_global_lower_bound']>=9867
    three=json.loads((roots['defect']/'e3/core_three_dependency_result.json').read_text())
    assert three['scope']=='exactly 3 cores' and three['excluded_through']==9880
    assert len(three['cases'])==134 and all(r['solutions']==0 for r in three['cases'])
    four=json.loads((roots['previous']/'lower/four_result.json').read_text())
    assert four['all_excluded'] and 9866 in four['fully_excluded_costs']
    assert four['completed_by_cost']['9866']==525
    five=json.loads((roots['previous']/'previous/twelve_cores/result.json').read_text())['5/9995']
    assert len(five['cases'])==five['branches']==458 and all(r[-1]==0 for r in five['cases'])
    subprocess.run([sys.executable,'-B',HERE/'exact_price_frontier.py','--cost','9866',
                    '--mother-proof',roots['mother'],'--defect-catalog',roots['defect']/'cost_defect_catalog.json',
                    '--output',args.output/'typed_frontier.json'],check=True,stdout=subprocess.DEVNULL)
    frontier=json.loads((args.output/'typed_frontier.json').read_text())
    target={r['tag'] for r in frontier['survivors']}
    assert len(target)==117 and frontier['size_profiles']==102
    assert frontier['total_exact_price_patterns']==1454
    assert frontier['surviving_by_embedded_count']=={'3':10,'4':30,'5':61,'6':16}
    subprocess.run([sys.executable,'-B',HERE/'verify_price_dp.py','--mother',roots['mother'],
                    '--defect',roots['defect'],'--frontier',args.output/'typed_frontier.json',
                    '--output',args.output/'price_dp_result.json'],check=True,stdout=subprocess.DEVNULL)
    assert json.loads((args.output/'price_dp_result.json').read_text())['independent_price_dp_passed']
    rows=[json.loads(line) for line in (HERE/'receipts.jsonl').read_text().splitlines()]
    assert len(rows)==len({r['tag'] for r in rows})==117
    assert {r['tag'] for r in rows}==target==set((HERE/'profiles.txt').read_text().splitlines())
    for row in rows:
        assert row['cost']==9866 and row['found']==0
        for key in ('source_sha256','bank_sha256','driver_sha256'):
            assert row[key]==bindings[key]
    expected=json.loads((HERE/'expected.json').read_text())
    result={'cost':9866,'complete':True,'profiles':117,'missing_profiles':[],
            'new_global_lower_bound':9867,'upper_bound':9996,
            'prior_cost9865_audit_bound':9866,'solutions':0,
            'size_profiles':102,'typed_price_patterns':1454,
            'independent_price_dp_passed':True,
            'search_nodes':sum(r['search_nodes'] for r in rows),
            'geometric_nodes':sum(r['geometric_nodes'] for r in rows),
            'leaf_nodes':sum(r['leaf_nodes'] for r in rows),
            'search_rerun':args.mode=='full','review_status':'NOT_REVIEWED'}
    for key in ('search_nodes','geometric_nodes','leaf_nodes'):
        assert result[key]==expected[key]
    result['by_embedded_count']={}
    for e in range(3,7):
        group={r['tag'] for r in frontier['survivors'] if r['embedded_count']==e}
        actual=[r for r in rows if r['tag'] in group]
        result['by_embedded_count'][str(e)]={'profiles':len(group),
            **{k:sum(r[k] for r in actual) for k in ('search_nodes','geometric_nodes','leaf_nodes')}}
    assert result['by_embedded_count']==expected['by_embedded_count']
    if args.mode=='full':
        work=args.native_inputs.resolve() if args.native_inputs else args.output/'native_inputs'
        if args.native_inputs is None:
            subprocess.run([sys.executable,'-B',roots['lower']/'replay.py','--previous',roots['previous'],
                            '--work',work,'--first','9861','--last','9870','--cost','9866',
                            '--cores','0,1,2','--engine','orbit-min','--prepare-only'],check=True)
        for dep in bindings['native_inputs']:
            assert digest(work/dep['path'])==dep['sha256'],dep['path']
        types=list(map(tuple,json.loads((work/'manifest.json').read_text())['types']))
        execution=args.output/'execution_inputs';execution.mkdir(exist_ok=True)
        for dep in bindings['native_inputs']:
            q=execution/dep['path']
            if not q.exists():q.symlink_to(work/dep['path'])
        exe=args.output/'native_search'
        subprocess.run(['c++','-std=c++20','-O3','-mpopcnt',roots['lower']/'front_orbit_min_witness.cpp',
                        '-o',exe],check=True)
        query=''
        for r in rows:
            counts={(s,c):n for s,c,n in (map(int,item.split('-')) for item in r['tag'].split('_'))}
            assert set(counts)<=set(types)
            query+=' '.join(map(str,[9866,*[counts.get(t,0) for t in types]]))+'\n'
        native=subprocess.run([exe,work/'bank',work,execution],input=query,text=True,capture_output=True,check=True)
        values=[list(map(int,line.split())) for line in native.stdout.splitlines()]
        assert len(values)==len(rows)
        for r,actual in zip(rows,values):
            assert actual==[r[k] for k in ('cost','geometric_nodes','leaf_nodes','search_nodes','found')]
        result['execution_binary_sha256']=digest(exe)
    (args.output/'result.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,sort_keys=True))


if __name__=='__main__':
    main()
