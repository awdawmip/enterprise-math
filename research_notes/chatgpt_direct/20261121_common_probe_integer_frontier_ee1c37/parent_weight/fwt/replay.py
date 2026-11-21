"""Audit saved exact FWT receipts, or repeat all six complete transforms."""
from pathlib import Path
from fractions import Fraction
from hashlib import sha256
import argparse
import json
import subprocess
import sys

TYPES = ((9,557),(10,744),(11,936),(11,944))
COUNTS = (2,5,2,1)
COORDS = [(i//25,i//5%5,i%5) for i in range(125)]
SCALE = 1 << 40


def audit(check, witness, engine_source):
    data = witness.read_bytes(); point = json.loads(data)
    result = json.loads((check/'result.json').read_text())
    assert result['witness_sha256'] == sha256(data).hexdigest()
    assert result['engine_source_sha256'] == sha256(engine_source.read_bytes()).hexdigest()
    assert result['global_family_verified_exactly'] and result['indexed_cuts'] == 1 << 27
    free = int(point['free_mask']); rows = point['weights']; pair = result['pair']
    weights = [Fraction(row['numerator'],row['denominator']) for row in rows]
    assert sum(weights) == 10 and all(w > 0 for w in weights)
    fibers = [sum(1<<p for p,x in enumerate(COORDS) if free>>p&1 and 5*x[pair[0]]+x[pair[1]] == value) for value in range(1,25)]
    rhs = [f.bit_count()%2 for f in fibers]+[n%2 for n in COUNTS]
    rhs_mask = sum(bit<<i for i,bit in enumerate(rhs[:-1])); encoded = []
    for row,w in zip(rows,weights):
        mask = int(row['mask']); typ = TYPES.index((row['size'],row['cost']))
        column = sum(((mask&f).bit_count()%2)<<i for i,f in enumerate(fibers)) | (1<<(24+typ))
        constant = column>>27; key = (column&((1<<27)-1))^(rhs_mask if constant else 0)
        value = w.numerator*SCALE//w.denominator
        encoded.append((key,-value if constant else value))
    expected_input = f'27 {len(rows)} {SCALE}\n'+''.join(f'{key} {value}\n' for key,value in encoded)
    assert (check/'fwt_input.txt').read_text() == expected_input
    assert sha256(expected_input.encode()).hexdigest() == result['input_sha256']
    evaluated = []; seen = set()
    for line in (check/'fwt.stdout').read_text().splitlines():
        bits,score = map(int,line.split()); assert bits not in seen and 0 <= bits < 1<<27; seen.add(bits)
        assert score >= 8*SCALE-len(rows)
        assert score == sum(-value if (key&bits).bit_count()%2 else value for key,value in encoded)
        last = 1^((bits&rhs_mask).bit_count()%2); full = bits|(last<<27)
        subset = sum(f for j,f in enumerate(fibers) if full>>j&1)
        parities = [(full>>(24+j))&1 for j in range(4)]
        assert (subset.bit_count()+sum(a*n for a,n in zip(parities,COUNTS)))%2 == 1
        lhs = sum((w for row,w in zip(rows,weights) if ((int(row['mask'])&subset).bit_count()+parities[TYPES.index((row['size'],row['cost']))])%2),Fraction())
        evaluated.append((lhs,str(subset),parities))
    assert len(evaluated) == result['exact_threshold_candidates']
    assert sum(v[0] < 1 for v in evaluated) == result['violated_indexed_cuts']
    assert min(v[0] for v in evaluated) == Fraction(result['minimum']['lhs'])
    for cut in result['violations']:
        assert (Fraction(cut['lhs']),cut['subset_mask'],cut['type_parities']) in evaluated
    log = (check/'fwt.stderr').read_text()
    assert f'indexed {1<<27} retained {len(evaluated)} ' in log
    return {'frame':point['frame'],'pair':pair,'indexed_cuts':1<<27,
            'threshold_candidates':len(evaluated),'violations':result['violated_indexed_cuts'],
            'minimum':result['minimum']['lhs'],'witness_sha256':result['witness_sha256']}


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--integer-cuts',type=Path,required=True)
    ap.add_argument('--joint3',type=Path,required=True)
    ap.add_argument('--work',type=Path,required=True)
    ap.add_argument('--mode',choices=['audit','full'],default='audit')
    a = ap.parse_args(); a.work.mkdir(parents=True,exist_ok=True)
    here = Path(__file__).resolve().parent; source = here/'pair_boolean_exact.cpp'
    binary = a.work/'pair_boolean_exact'
    if a.mode == 'full': subprocess.run(['c++','-O3','-std=c++20',source,'-o',binary],check=True)
    checks = []
    for frame in (1,2):
        witness = a.integer_cuts/'all_joint_exact/cover_1.json' if frame == 1 else a.joint3/'cover_2.json'
        for pair in ((0,1),(0,2),(1,2)):
            name = f'frame{frame}_pair{pair[0]}{pair[1]}'
            saved = here/'checks'/name
            baseline = audit(saved,witness,source)
            if a.mode == 'full':
                output = a.work/name
                subprocess.run([sys.executable,'-B',here/'pair_boolean_exact.py','--witness',witness,
                                '--output',output,'--pair',str(pair[0]),str(pair[1]),'--binary',binary],check=True)
                assert audit(output,witness,source) == baseline
            checks.append(baseline)
    result = {'status':'PASS','mode':a.mode,'complete_family_reexecuted':a.mode=='full',
              'saved_complete_results_audited':True,'checks':checks,
              'indexed_applications':sum(c['indexed_cuts'] for c in checks),
              'exact_threshold_candidates':sum(c['threshold_candidates'] for c in checks),
              'full_candidate_lp_infeasibility_claimed_by_this_family':False,'review_status':'NOT_REVIEWED'}
    (a.work/'result.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))


if __name__ == '__main__': main()
