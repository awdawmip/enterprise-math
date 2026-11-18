#!/usr/bin/env python3
"""Independent exact key-family enumeration and sound H7/S4 screen.
Frozen finite mathematical model of EC49EXI, no operation-word generation.
"""
from itertools import combinations, product
from collections import Counter
from pathlib import Path
import json

BASE=(3,1,1)
def families(h):
    out={}
    for w in range(1,(h+1)//2+1):
        for r in range(h-2*w+2):
            for f in range(h-2*w-r+2):
                g=h-(2*w-1)-r-f
                key=(r+2*w+f,r+g,w)
                # Every r>=1 key has one T4 full-rank family;
                # r=0 with f,g>=1 has a T2 full-rank family.
                typ=4 if r>=1 else (2 if f>=1 and g>=1 else 0)
                if typ:
                    assert key not in out or out[key]==typ
                    out[key]=typ
    return out

def main():
    fs={h:families(h) for h in range(2,9)}
    assert fs[2]=={BASE:4}
    ks=sorted(set().union(*(set(z) for z in fs.values())))
    assert len(ks)==84
    qsets=0
    all_schedules=0
    counts=Counter();examples={}
    for extras in combinations((k for k in ks if k!=BASE),3):
        q=(BASE,)+extras
        opts=[]
        for h in range(3,9):
            opts.append([(i,fs[h][p]) for i,p in enumerate(q) if p in fs[h]])
        if not all(opts):continue
        q_count=0
        for seq in product(*opts):
            prior=((0,4),)+seq[:-1]
            used={i for i,_ in prior}
            if len({0,*[i for i,_ in seq]})!=4:continue
            q_count+=1
            phase = 'four_keys_by_h7' if len(used)==4 else 'new_key_h8'
            if phase=='four_keys_by_h7':
                first4=next(h for h in range(3,8) if len({0,*[i for i,t in seq[:h-2]]})==4)
                h7_s4=all(t==4 for _,t in prior)
                h8typ=seq[-1][1]
                k=('phase',phase,'first4',first4,'h7_S4',h7_s4,'h8',h8typ)
                counts[k]+=1
                if k not in examples:examples[k]={'keys_by_horizon':[list(q[0])]+[list(q[i]) for i,t in seq], 'types':[4]+[t for i,t in seq]}
                counts[('first4',first4)]+=1
                counts[('h7_S4',h7_s4,'h8',h8typ)]+=1
            else:
                counts[('phase',phase,'h8',seq[-1][1])]+=1
        if q_count:qsets+=1;all_schedules+=q_count
    assert (qsets,all_schedules)==(14092,55493),(qsets,all_schedules)
    assert sum(v for k,v in counts.items() if k[:1]==('phase',) and 'first4' in k)==26933
    assert sum(v for k,v in counts.items() if k[:2]==('phase','new_key_h8'))==28560
    all_t4_h7=sum(v for k,v in counts.items() if len(k)==4 and k[:1]==('h7_S4',) and k[1] is True)
    out={
        'status':'PASS',
        'scope':'Exact key-family schedules H8/M4/S<=6, remaining fourth-key-by-h7 branch',
        'frozen_model_input':'EC49EXI 7-operation signed native X6, symbolic positive-count BRC, exact T4/T2 key-fiber criterion',
        'complete_key_sets':qsets,'complete_schedules':all_schedules,
        'residual_schedules':26933,
        'counts_by_first_fourth_key': {str(h):counts[('first4',h)] for h in range(3,8)},
        'h7_observer_S4_and_h8_type':{f'H7S4={t},H8T{typ}':counts[('h7_S4',t,'h8',typ)] for t in (True,False) for typ in (2,4)},
        'strong_H7S4_screened':all_t4_h7,
        'remaining_after_H7S4_screen':26933-all_t4_h7,
        'strict_lower_bound_by_H7S4_h8': {'h8_T2':96,'h8_T4':100},
        'other_prior_bound_h7_m4_s6':72,
        'notes':'H7 four-key S4 exact E7>=92 from EC49EW; terminal primitive prefix increments +4 (T2), +8 (T4) from EC49EXD/EXI; stronger bound valid if first 7 fibers are T4. For all other cases no E8>=90 conclusion is asserted.',
        'sample_key_family_by_group': {' / '.join(map(str,k)):v for k,v in examples.items()}
    }
    dst=Path(__file__).with_name('EC49EXJ_ANALYTIC_EXECUTED.json')
    dst.write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:out[k] for k in ['status','complete_key_sets','complete_schedules','counts_by_first_fourth_key','h7_observer_S4_and_h8_type','strong_H7S4_screened','remaining_after_H7S4_screen']},ensure_ascii=False,indent=2))
if __name__=='__main__':main()
