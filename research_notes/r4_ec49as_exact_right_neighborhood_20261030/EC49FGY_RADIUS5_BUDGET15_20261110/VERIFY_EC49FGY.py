#!/usr/bin/env python3
"""EC49FGY exact complete 5-way union test for budgets 11..15.
Dependencies: sibling EC49FGX/VERIFY_EC49FGX.py and its EC49FGW sibling.
Scientific pin and original 24-path witnesses are validated by EC49FGW.
"""
import collections, itertools, json, sys
from pathlib import Path
HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE.parent/'EC49FGX_RADIUS5_PAIR_FIVE_DP_20261110'))
from VERIFY_EC49FGX import W,PIN,all_words,raw_key,pref,validate_profile,candidates,pair_possible,five_possible

def audit(pr,all_legal):
    rows,sets=validate_profile(pr)
    labels=[(r['window'],r['signature']) for r in rows]
    keys=[raw_key(r['word']) for r in rows]
    known=set(keys)
    sup=collections.defaultdict(int)
    key_sup=collections.defaultdict(int)
    for i,(ps,key) in enumerate(zip(sets,keys)):
        key_sup[key]|=1<<i
        for p in ps:sup[p]|=1<<i
    assert len(known)==7 and len(sup)==94
    index=collections.defaultdict(list)
    for lab,w in all_legal:
        if raw_key(w) not in known:continue
        p=pref(w)
        index[lab].append((len(p),p[-1],[(len(t),sup[t]) for t in p if t in sup]))
    assert sum(map(len,index.values()))==9838
    tally=collections.Counter()
    budgets=collections.Counter()
    for Q in itertools.combinations(range(24),5):
        mask=sum(1<<i for i in Q)
        if any(s&mask==s for s in key_sup.values()):continue
        B=sum((s&mask)==s for s in sup.values())-1
        if not 11<=B<=15:continue
        tally['all_positions']+=1
        cs=[candidates(index[labels[i]],mask,B) for i in Q]
        if any(not a for a in cs):
            tally['singleton_rejected']+=1;continue
        if any(not pair_possible(cs[i],cs[j],B) for i,j in itertools.combinations(range(5),2)):
            tally['pair_rejected']+=1;continue
        tally['five_tested']+=1
        budgets[B]+=1
        if five_possible(cs,B):
            tally['feasible_93']+=1
        else:
            tally['five_rejected']+=1
    return {'witness':pr['profile_id'],'counts':dict(tally),'five_rejected_by_budget':dict(sorted(budgets.items()))}

if __name__=='__main__':
    all_legal=list(all_words());assert len(all_legal)==178850
    result={'schema':'EC49FGY_RADIUS5_EXACT_BUDGET11_TO15_V1','frozen_scientific_pin':PIN,
            'model':'original nine-state BRC / signed ordered X6 microstep prefixes',
            'domain':'all five-label replacement positions with no original-key release, budget B in 11..15',
            'profiles':[audit(pr,all_legal) for pr in W['profiles']]}
    assert [p['counts']['five_rejected'] for p in result['profiles']]==[2066,2040]
    assert all(p['counts'].get('feasible_93',0)==0 for p in result['profiles'])
    (HERE/'EXACT_REPORT_EC49FGY.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2));print('EC49FGY_EXACT_PASS')
