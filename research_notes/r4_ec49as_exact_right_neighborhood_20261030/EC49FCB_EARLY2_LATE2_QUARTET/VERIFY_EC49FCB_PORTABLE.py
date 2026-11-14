"""Exact 158-edge four-slot certificate (five non-H7/H8 late-pair families).
Run with e.g. python VERIFY_EC49FCB_PORTABLE.py H9H9; all five phase outputs
regenerate the 1305-group finite certificate. Python standard library only.
"""
import json, math, sys
from itertools import combinations, product
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'EC49FBY_COMPLETE_TRIPLE_RIGIDITY'))
from VERIFY_EC49FBY import build

PHASES=('H7H7','H7H9','H8H8','H8H9','H9H9')
PIN='fc0f038e7bfd12c886b4d37f900bfb770c0f61ab'

def run(phase):
    assert phase in PHASES
    chosen,early,late,pools,single=build()
    assert len(single)==24 and len(early)==len(late)==10
    A=int(phase[1]); B=int(phase[3])
    l1=[k for k in late if k.startswith(f'{A}:')]
    l2=[k for k in late if k.startswith(f'{B}:')]
    late_pairs=combinations(l1,2) if A==B else product(l1,l2)
    result=[]
    # Materialize only this small combinatorial slot-pair list; reuse across E.
    late_pairs=list(combinations(l1,2) if A==B else product(l1,l2))
    for E in combinations(early,2):
        for L in late_pairs:
            slots=E+L
            rest=0
            for key,mask in single.items():
                if key not in slots:rest |= mask
            base=rest.bit_count(); limit=158-base
            arrays=[]; raw=1
            for key in slots:
                residual={mask & ~rest for mask in pools[key] if (mask & ~rest).bit_count()<limit}
                arrays.append((key,tuple(residual)))
                raw*=len(pools[key])
            arrays.sort(key=lambda pair:len(pair[1]))
            a,b,c,d=(r for _,r in arrays)
            pairprune=tripleprune=checks=0; best=158
            for x in a:
                for y in b:
                    xy=x|y
                    if xy.bit_count()>=limit:
                        pairprune+=1;continue
                    for z in c:
                        xyz=xy|z
                        if xyz.bit_count()>=limit:
                            tripleprune+=1;continue
                        for w in d:
                            checks+=1
                            best=min(best,base+(xyz|w).bit_count())
            result.append({'slots':slots,'rest_edges':base,'raw':raw,
                           'eligible_product':math.prod(len(r) for r in (a,b,c,d)),
                           'pair_pruned':pairprune,'triple_pruned':tripleprune,
                           'fourth_evaluations':checks,'minimum':best})
    expected=45*(6 if A==B and A!=9 else 1 if A==B else len(l1)*len(l2))
    assert len(result)==expected and all(x['minimum']==158 for x in result)
    keys=('raw','eligible_product','pair_pruned','triple_pruned','fourth_evaluations')
    sums={k:sum(row[k] for row in result) for k in keys}
    out={'schema':'EC49FCB_EXACT_PHASE_V1','pin':PIN,'phase':phase,
         'groups':len(result),'minimum':158,'sums':sums,'per_group':result}
    Path(__file__).with_name(f'EC49FCB_REPORT_{phase}.json').write_text(json.dumps(out,indent=2)+'\n')
    print('PASS',phase,len(result),sums,flush=True)
    return out
if __name__=='__main__':
    if len(sys.argv)!=2:raise SystemExit('phase required: '+', '.join(PHASES))
    run(sys.argv[1])
