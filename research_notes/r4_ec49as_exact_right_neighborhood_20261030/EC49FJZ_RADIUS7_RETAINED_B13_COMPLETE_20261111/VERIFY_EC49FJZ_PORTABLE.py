#!/usr/bin/env python3
"""EC49FJZ exact B13 seven-replacement retained-key BRC finite proof.

Input: the frozen original EC49FGW_RADIUS5_SCREEN.py and
EC49FGJ_SEVEN_KEY_94_WITNESSES.json together inside sibling EC49FJR/.
No endpoint quotient, signed-step omission, random test, or antichain shortcut.
"""
import collections,itertools,json,sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).parent/'EC49FJR'))
import EC49FGW_RADIUS5_SCREEN as g
B=13
assert g.PIN=='fc0f038e7bfd12c886b4d37f900bfb770c0f61ab'

def impossible_raw_union(options):
    """Exact literal signed-prefix union DP: deduplicate identical unions only."""
    states={frozenset()}
    for words in options:
        states={a|b for a in states for b in words if len(a|b)<=B}
        if not states:return True
    return False

def analyze_profile(profile,whole):
    rows,ps=g.validate_profile(profile)
    labels=tuple((d['window'],d['signature']) for d in rows)
    keys={g.raw_key(d['word']) for d in rows}
    assert len(keys)==7 and len(set().union(*ps))==94
    words_by_label=collections.defaultdict(list)
    for lab,w in whole:
        if g.raw_key(w) in keys:
            words_by_label[lab].append(frozenset(g.pref(w)))
    assert sum(map(len,words_by_label.values()))==9838
    support=collections.defaultdict(int);key_support=collections.defaultdict(int)
    for i,d in enumerate(rows):
        key_support[g.raw_key(d['word'])]|=1<<i
        for p in ps[i]:support[p]|=1<<i
    backgrounds=collections.defaultdict(list)
    released=0
    for Q in itertools.combinations(range(24),7):
        mask=sum(1<<i for i in Q)
        if any(s&mask==s for s in key_support.values()):
            released+=1;continue
        removed=tuple(sorted(p for p,s in support.items() if s&mask==s))
        if len(removed)==B+1:backgrounds[removed].append(Q)
    assert released==192696 and len(backgrounds)==58
    assert sum(len(v) for v in backgrounds.values())==8564
    classified=collections.Counter(); details=[]
    for gid,(removed,Qs) in enumerate(sorted(backgrounds.items()),1):
        F=set(support).difference(removed)
        common=set.intersection(*({labels[i] for i in Q} for Q in Qs))
        selected=None
        eligible={}
        for lab in sorted(common):
            eligible[lab]=[p.difference(F) for p in words_by_label[lab]
                           if len(p.difference(F))<=B]
            assert eligible[lab]
        for r in (2,3,4):
            for labs in itertools.combinations(sorted(common),r):
                if impossible_raw_union([eligible[lab] for lab in labs]):
                    selected=labs;break
            if selected:break
        assert selected is not None,(profile['profile_id'],gid)
        assert all(set(selected)<={labels[i] for i in Q} for Q in Qs)
        classified[len(selected)]+=len(Qs)
        details.append({'group':gid,'contexts':len(Qs),
                        'obstructing_labels':[list(l) for l in selected],
                        'raw_words_per_label':[len(eligible[l]) for l in selected],
                        'certificate_arity':len(selected)})
        print(profile['profile_id'],gid,len(Qs),'arity',len(selected),flush=True)
    p=profile['profile_id']
    expectation={'A':{2:274,3:3442,4:4848},'B':{2:548,3:3168,4:4848}}[p]
    assert dict(classified)==expectation,(p,classified)
    return {'profile':p,'B13_contexts':8564,'groups':58,
            'pair_excluded':classified[2], 'triple_excluded':classified[3],
            'four_excluded':classified[4], 'unresolved':0,'details':details}

def main():
    whole=list(g.all_words())
    assert len(whole)==178850
    assert len({g.raw_key(w) for _,w in whole})==94
    profiles=[analyze_profile(p,whole) for p in g.W['profiles']]
    assert sum(p['B13_contexts'] for p in profiles)==17128
    report={'schema':'EC49FJZ_R7_B13_LITERAL_RAW_WORD_COMPLETE_EXACT_V1',
            'frozen_scientific_pin':g.PIN,'budget':B,
            'legal_native_words':len(whole),'raw_complete_keys':94,
            'profiles':profiles,'total_new_sharp_local_94_optima':17128}
    (Path(__file__).parent/'EXACT_REPORT_EC49FJZ.json').write_text(
        json.dumps(report,indent=2)+'\n')
    print('EC49FJZ_ALL_17128_EXACT_PASS',flush=True)
if __name__=='__main__':main()
