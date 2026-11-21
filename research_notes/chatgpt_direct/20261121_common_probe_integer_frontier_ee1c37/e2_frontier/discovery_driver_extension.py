"""Extend the frozen E2>=9898 theorem without duplicating earlier discovery.

This driver stops at any missing native type or native superset cover. A found
cover is classified by its true embedded count before reporting its scope.
"""
from hashlib import sha256
import json
from pathlib import Path
import struct
import subprocess
import sys
import time

HERE=Path(__file__).resolve().parent
OLD=Path('/workspace/scratch/567706f31840')
WORK=OLD/'r10/lower/work'
EXE=HERE.parent/'structure9866/work/front_orbit_min_witness'


def main():
    types=list(map(tuple,json.loads((WORK/'manifest.json').read_text())['types']))
    rows_path=HERE/'completed.jsonl'
    done={r['tag']:r for r in map(json.loads,rows_path.read_text().splitlines())} if rows_path.exists() else {}
    state={'previous_E2_lower_bound':9898,'E2_lower_bound':9898,'completed_costs':[],
           'prior_package':'E2_complete_9898','scope':'Exactly two embedded classes among twelve labels.'}
    provenance={
        'source_sha256':sha256((OLD/'r10/lower/front_orbit_min_witness.cpp').read_bytes()).hexdigest(),
        'bank_sha256':sha256((WORK/'bank').read_bytes()).hexdigest(),
        'binary_sha256':sha256(EXE.read_bytes()).hexdigest(),
        'driver_sha256':sha256(Path(__file__).read_bytes()).hexdigest()}
    plans=HERE/'plans';plans.mkdir(exist_ok=True)
    with subprocess.Popen([EXE,WORK/'bank',WORK,HERE/'inputs'],stdin=subprocess.PIPE,
                          stdout=subprocess.PIPE,text=True) as native:
        for cost in range(9898,9996):
            if (HERE/'STOP_NEW_LAYERS').exists():
                state.update(next_cost=cost,stop='Requested checkpoint pause before a new cost layer.')
                break
            plan_file=plans/f'cost{cost}.json'
            subprocess.run([sys.executable,'-B',HERE/'exact_price_frontier.py','--cost',str(cost),
                            '--only-embedded-count','2','--mother-proof',OLD/'r10/integer_cuts/mother12',
                            '--defect-catalog',OLD/'r11/publication/artifact/mother_sublevels_D/cost_defect_catalog.json',
                            '--output',plan_file],check=True,stdout=subprocess.DEVNULL)
            plan=json.loads(plan_file.read_text());necessary={r['tag']:r for r in plan['survivors']}
            missing=sorted({(t['size'],t['cost']) for r in necessary.values() for t in r['types']}-set(types))
            if missing:
                state.update(next_cost=cost,missing_native_types=missing,
                             stop='The retained complete bank lacks a necessary size/price type.')
                break
            found=False
            for tag,row in necessary.items():
                if tag in done:
                    assert done[tag]['found']==0
                    continue
                counts={}
                for t in row['types']:
                    pair=t['size'],t['cost']
                    counts[pair]=counts.get(pair,0)+t['count']
                query=' '.join(map(str,[cost,*[counts.get(t,0) for t in types]]))+'\n'
                (HERE/'running.json').write_text(json.dumps({'cost':cost,'tag':tag,'started':time.time()})+'\n')
                started=time.monotonic();native.stdin.write(query);native.stdin.flush()
                values=list(map(int,native.stdout.readline().split()))
                assert len(values)==5 and values[0]==cost
                item=dict(zip(['cost','geometric_nodes','leaf_nodes','search_nodes','found'],values))
                item.update(tag=tag,seconds=time.monotonic()-started,**provenance)
                with rows_path.open('a') as out:out.write(json.dumps(item,sort_keys=True)+'\n')
                done[tag]=item
                if item['found']:
                    witness=HERE/'inputs'/f'found_{cost}.json'
                    table=json.loads(witness.read_text())
                    mothers=[lo|(hi<<64) for lo,hi,c,s in struct.iter_unpack('<QQII',(WORK/'bank').read_bytes()) if (s&255)==13]
                    masks=[sum(1<<i for i in c['points']) for c in table['classes']]
                    embedded=sum(any(m&M==m for M in mothers) for m in masks)
                    state.update(next_cost=cost,witness=str(witness),actual_embedded_count=embedded,
                                 stop='A native superset cover was found; original-menu witness verification is required.')
                    found=True
                    break
            if found:break
            actual=[done[tag] for tag in necessary]
            layer={'cost':cost,'size_profiles':plan['size_profiles'],
                   'price_patterns':plan['total_exact_price_patterns'],
                   'native_profiles':len(necessary),'search_nodes':sum(r['search_nodes'] for r in actual)}
            state['completed_costs'].append(layer);state['E2_lower_bound']=cost+1
            (HERE/'state.json').write_text(json.dumps(state,indent=2)+'\n')
            (HERE/'running.json').unlink(missing_ok=True)
            print(json.dumps(layer,sort_keys=True),flush=True)
        native.stdin.close();assert native.wait()==0
    (HERE/'running.json').unlink(missing_ok=True)
    (HERE/'state.json').write_text(json.dumps(state,indent=2)+'\n')
    print(json.dumps(state,sort_keys=True),flush=True)


if __name__=='__main__':
    main()
