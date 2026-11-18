"""EC49FCD: exact all-late quartet BRC prefix-union test.
Usage: python VERIFY_EC49FCD.py START STOP (0<=START<STOP<=210),
then python VERIFY_EC49FCD.py merge after disjoint chunks cover all 210.
Imports frozen EC49FBY generator; integer bitsets preserve all ordered signed X6 prefixes.
"""
from pathlib import Path
from itertools import combinations
import json,sys,math
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'EC49FBY_COMPLETE_TRIPLE_RIGIDITY'))
from VERIFY_EC49FBY import build
HERE=Path(__file__).resolve().parent
PIN='fc0f038e7bfd12c886b4d37f900bfb770c0f61ab'
BASELINE=158
EXPECTED={'raw':1069546816890000,'eligible_product':23804059817376,
          'pair_pruned':8327983,'triple_pruned':10223623,'fourth_checks':670296}

def search(slots,pools,single):
    fixed=0
    for key,mask in single.items():
        if key not in slots:fixed|=mask
    base=fixed.bit_count();cut=BASELINE-base
    arrays=[];raw=1
    for key in slots:
        raw*=len(pools[key])
        residuals={mask&~fixed for mask in pools[key]
                   if (mask&~fixed).bit_count()<cut}
        arrays.append((key,tuple(sorted(residuals))))
    arrays.sort(key=lambda item:len(item[1]))
    a,b,c,d=(v for _,v in arrays)
    pair=triple=checks=0; minimum=BASELINE
    for x in a:
        for y in b:
            xy=x|y
            if xy.bit_count()>=cut:
                pair+=1;continue
            for z in c:
                xyz=xy|z
                if xyz.bit_count()>=cut:
                    triple+=1;continue
                for w in d:
                    checks+=1
                    minimum=min(minimum,base+(xyz|w).bit_count())
    return {'slots':list(slots),'base':base,'cut':cut,
            'raw':raw,'counts':[len(v) for _,v in arrays],
            'eligible_product':math.prod(len(v) for _,v in arrays),
            'pair_pruned':pair,'triple_pruned':triple,
            'fourth_checks':checks,'minimum':minimum}

def run(start,stop):
    assert 0<=start<stop<=210
    chosen,early,late,pools,single=build()
    assert len(chosen)==24 and len(early)==10 and len(late)==10
    sets=list(combinations(late,4))
    assert len(sets)==210
    rows=[]
    for index in range(start,stop):
        row=search(sets[index],pools,single)
        assert row['minimum']==BASELINE,(index,row)
        row['index']=index
        rows.append(row)
    out={'schema':'EC49FCD_EXACT_CHUNK_V1','pin':PIN,
         'range':[start,stop],'per_group':rows}
    (HERE/f'EC49FCD_CHUNK_{start:03d}_{stop:03d}.json').write_text(
        json.dumps(out,indent=2)+'\n',encoding='utf-8')
    print('PASS',start,stop,'groups',len(rows),'fourth',
          sum(x['fourth_checks'] for x in rows),flush=True)

def merge():
    rows=[]
    for p in HERE.glob('EC49FCD_CHUNK_*.json'):
        v=json.loads(p.read_text(encoding='utf-8'))
        assert v['pin']==PIN and len(v['per_group'])==v['range'][1]-v['range'][0]
        rows.extend(v['per_group'])
    rows.sort(key=lambda x:x['index'])
    assert [x['index'] for x in rows]==list(range(210))
    assert len({tuple(x['slots']) for x in rows})==210
    assert all(x['minimum']==BASELINE for x in rows)
    sums={key:sum(row[key] for row in rows) for key in EXPECTED}
    assert sums==EXPECTED,(sums,EXPECTED)
    full={'schema':'EC49FCD_ALL_LATE_QUARTET_CERTIFICATE_V1',
          'scientific_pin':PIN,'groups':210,'minimum':BASELINE,
          'aggregate':sums,'per_group':rows}
    (HERE/'EC49FCD_FULL_210.json').write_text(json.dumps(full,indent=2)+'\n')
    print('PASS_ALL_210',sums)
if __name__=='__main__':
    if sys.argv[1:]==['merge']:merge()
    elif len(sys.argv)==3:run(int(sys.argv[1]),int(sys.argv[2]))
    else:raise SystemExit('Use START STOP or merge')
