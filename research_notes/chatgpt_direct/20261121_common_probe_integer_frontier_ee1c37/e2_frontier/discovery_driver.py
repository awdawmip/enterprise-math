"""Continue exact E=2 layers while the retained complete native bank covers them."""
from pathlib import Path
from hashlib import sha256
import json
import subprocess
import sys
import time

HERE = Path(__file__).resolve().parent
OLD = Path('/workspace/scratch/567706f31840')
WORK = OLD/'r10/lower/work'
EXE = HERE.parent/'structure9866/work/front_orbit_min_witness'


def main():
    types = list(map(tuple, json.loads((WORK/'manifest.json').read_text())['types']))
    plan_dir = HERE/'plans'
    plan_dir.mkdir(exist_ok=True)
    receipts = HERE/'new_completed.jsonl'
    completed = {row['tag']: row for row in map(json.loads, receipts.read_text().splitlines())} if receipts.exists() else {}
    provenance = {'source_sha256': sha256((OLD/'r10/lower/front_orbit_min_witness.cpp').read_bytes()).hexdigest(),
                  'bank_sha256': sha256((WORK/'bank').read_bytes()).hexdigest(),
                  'binary_sha256': sha256(EXE.read_bytes()).hexdigest()}
    state = {'previous_E2_lower_bound': 9871, 'E2_lower_bound': 9871, 'completed_costs': [],
             'scope': 'Exactly two embedded classes; known E2 lower bound9871 supplied by preceding completed work.'}
    with subprocess.Popen([EXE, WORK/'bank', WORK, HERE/'inputs'], stdin=subprocess.PIPE,
                          stdout=subprocess.PIPE, text=True) as native:
        for cost in range(9871, 9996):
            target = plan_dir/f'cost{cost}.json'
            subprocess.run([sys.executable, '-B', HERE/'exact_price_frontier.py', '--cost', str(cost),
                            '--only-embedded-count', '2', '--mother-proof', OLD/'r10/integer_cuts/mother12',
                            '--defect-catalog', OLD/'r11/publication/artifact/mother_sublevels_D/cost_defect_catalog.json',
                            '--output', target], check=True, stdout=subprocess.DEVNULL)
            plan = json.loads(target.read_text())
            rows = plan['survivors']
            missing = sorted({(t['size'], t['cost']) for row in rows for t in row['types']} - set(types))
            if missing:
                state.update(next_cost=cost, missing_native_types=missing,
                             stop='The retained bank does not cover the next necessary class types.')
                break
            for row in rows:
                if row['tag'] in completed:
                    continue
                counts = {(t['size'],t['cost']):t['count'] for t in row['types']}
                query = ' '.join(map(str, [cost,*[counts.get(t,0) for t in types]]))+'\n'
                start = time.monotonic()
                (HERE/'running.json').write_text(json.dumps({'cost':cost,'tag':row['tag'],'started':time.time()})+'\n')
                native.stdin.write(query)
                native.stdin.flush()
                values = list(map(int, native.stdout.readline().split()))
                assert len(values)==5 and values[0]==cost
                item = dict(zip(['cost','geometric_nodes','leaf_nodes','search_nodes','found'],values))
                item.update(tag=row['tag'], seconds=time.monotonic()-start, **provenance)
                with receipts.open('a') as out:
                    out.write(json.dumps(item,sort_keys=True)+'\n')
                completed[item['tag']]=item
                if item['found']:
                    state.update(next_cost=cost, witness=HERE/'inputs'/f'found_{cost}.json')
                    state['witness']=str(state['witness'])
                    (HERE/'state.json').write_text(json.dumps(state,indent=2)+'\n')
                    return
            state['completed_costs'].append({'cost':cost,'size_profiles':plan['size_profiles'],
                                            'price_patterns':plan['total_exact_price_patterns'],
                                            'native_profiles':len(rows),
                                            'search_nodes':sum(completed[row['tag']]['search_nodes'] for row in rows)})
            state['E2_lower_bound']=cost+1
            (HERE/'state.json').write_text(json.dumps(state,indent=2)+'\n')
            (HERE/'running.json').unlink(missing_ok=True)
            print(json.dumps(state['completed_costs'][-1],sort_keys=True),flush=True)
        native.stdin.close()
        assert native.wait()==0
    (HERE/'state.json').write_text(json.dumps(state,indent=2)+'\n')
    print(json.dumps(state,sort_keys=True),flush=True)


if __name__=='__main__':
    main()
