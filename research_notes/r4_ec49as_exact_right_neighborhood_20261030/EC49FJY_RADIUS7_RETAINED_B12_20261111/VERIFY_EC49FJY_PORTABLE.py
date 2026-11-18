#!/usr/bin/env python3
"""EC49FJY: direct finite certificate for radius-seven retained-key B=12.

Place the exact original EC49FGW_RADIUS5_SCREEN.py and
EC49FGJ_SEVEN_KEY_94_WITNESSES.json inside an EC49FJR subdirectory next to
this script. Every eligible raw word is enumerated literally; no antichain
pruning or endpoint quotient is used. This checker proves that no 93-prefix
completion exists in this specified finite class.
"""
import collections,itertools,json,sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).parent/'EC49FJR'))
import EC49FGW_RADIUS5_SCREEN as g
assert g.PIN=='fc0f038e7bfd12c886b4d37f900bfb770c0f61ab'
B=12
# Each certificate is an obstructing pair or triple of (window, signature)
# labels for the corresponding sorted deleted-prefix background class.
CERT={
 'A': [((8,4),(9,16)), ((8,2),(9,16)), ((8,8),(9,16)),
       ((8,1),(9,16)), ((6,4),(8,4)), ((8,4),(9,32)),
       ((8,2),(9,32)), ((8,8),(9,32)), ((8,1),(9,32)),
       ((4,1),(6,1),(8,1))],
 'B': [((8,4),(9,16)), ((8,2),(9,16)), ((8,8),(9,16)),
       ((8,1),(9,16)), ((6,4),(8,4)), ((8,4),(9,32)),
       ((8,2),(9,32)), ((8,8),(9,32)), ((8,1),(9,32)),
       ((6,8),(8,8))]}

def impossible_direct_word_union(options):
    """Exhaustive literal union test for one pair/triple, at total budget B."""
    if len(options)==2:
        return not any(len(a|b)<=B for a in options[0] for b in options[1])
    assert len(options)==3
    return not any(len(a|b|c)<=B for a in options[0] for b in options[1]
                   if len(a|b)<=B for c in options[2])

def examine(profile, catalog):
    rows,ps=g.validate_profile(profile)
    keys={g.raw_key(d['word']) for d in rows}
    assert len(keys)==7 and len(set().union(*ps))==94
    bylabel=collections.defaultdict(list)
    for lab,word in catalog:
        if g.raw_key(word) in keys:bylabel[lab].append(frozenset(g.pref(word)))
    assert sum(len(v) for v in bylabel.values())==9838
    key_support=collections.defaultdict(int); support=collections.defaultdict(int)
    for i,row in enumerate(rows):
        key_support[g.raw_key(row['word'])]|=1<<i
        for p in ps[i]:support[p]|=1<<i
    groups=collections.defaultdict(list)
    released=0
    for Q in itertools.combinations(range(24),7):
        m=sum(1<<i for i in Q)
        if any(s&m==s for s in key_support.values()):released+=1;continue
        deleted=tuple(sorted(p for p,s in support.items() if s&m==s))
        if len(deleted)==B+1:groups[deleted].append(Q)
    assert released==192696 and len(groups)==10
    assert sum(map(len,groups.values()))==8020
    result=[]
    for idx,(deleted,Qs) in enumerate(sorted(groups.items()),1):
        labels=CERT[profile['profile_id']][idx-1]
        assert all(set(labels)<={(rows[i]['window'],rows[i]['signature']) for i in Q}
                   for Q in Qs),(profile['profile_id'],idx,'certificate labels do not occur in every Q')
        F=set(support)-set(deleted)
        opts=[]
        for lab in labels:
            xs=[p-F for p in bylabel[lab] if len(p-F)<=B]
            assert xs
            opts.append(xs)
        assert impossible_direct_word_union(opts),(profile['profile_id'],idx)
        result.append({'group':idx,'contexts':len(Qs),
                       'obstructing_labels':[list(l) for l in labels],
                       'legal_word_counts':[len(a) for a in opts],
                       'certified_no_union_leq12':True})
        print(profile['profile_id'],idx,len(Qs),labels,flush=True)
    return result

def main():
    catalog=list(g.all_words())
    assert len(catalog)==178850
    assert len({g.raw_key(w) for _,w in catalog})==94
    r={p['profile_id']:examine(p,catalog) for p in g.W['profiles']}
    assert all(sum(q['contexts'] for q in v)==8020 for v in r.values())
    assert sum(len(x['obstructing_labels'])==3 for v in r.values() for x in v)==1
    report={'schema':'EC49FJY_R7_B12_DIRECT_FULL_CATALOG_EXACT_V1',
            'frozen_scientific_pin':g.PIN,'B':B,'total_certified':16040,
            'source':'EC49FGW pinned native BRC generator and EC49FGJ A/B witnesses',
            'groups_by_profile':r}
    Path(__file__).with_name('EXACT_REPORT_EC49FJY.json').write_text(json.dumps(report,indent=2)+'\n')
    print('EC49FJY_ALL_16040_EXACT_PASS',flush=True)
if __name__=='__main__':main()
