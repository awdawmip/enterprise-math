#!/usr/bin/env python3
"""Independently enumerate literal six-letter BRC words and tuple prefix sets, exact radius 3."""
import sys,pathlib,json,itertools,collections
P=pathlib.Path(__file__).parent
sys.path.insert(0,str(P))
import EC49FGQ_DIRECT_CROSSCHECK as D
src=json.loads((P/'EC49FGJ_SEVEN_KEY_94_WITNESSES.json').read_text())
sets={p['profile_id']:set(map(tuple,p['allowed_keys'])) for p in src['profiles']}
allwords={p['profile_id']:collections.defaultdict(set) for p in src['profiles']}
for h in D.REQUIRED:
    for s,w in D.full_alphabet_paths(h):
        k=D.key(w)
        for pid,allow in sets.items():
            if k in allow:allwords[pid][(h,s)].add(D.signed_prefix_set(w))
for profile in src['profiles']:
    pid=profile['profile_id'];base={(r['window'],r['signature']):r['word'] for r in profile['demands']}
    basesp={l:D.signed_prefix_set(w) for l,w in base.items()}
    assert len(set().union(*basesp.values()))==94
    stats=collections.Counter();pairtests=0;tripletests=0
    for triple in itertools.combinations(D.LABELS,3):
        fixed=set().union(*(basesp[l] for l in D.LABELS if l not in triple))
        bound=93-len(fixed)
        if bound<0:stats['fixed_reject']+=1;continue
        stats['screened']+=1
        eligible=[]
        for l in triple:
            eligible.append({frozenset(x.difference(fixed)) for x in allwords[pid][l] if len(x.difference(fixed))<=bound})
        if any(not x for x in eligible):stats['empty_label']+=1;continue
        eligible.sort(key=len)
        pairset=set()
        for a in eligible[0]:
            for b in eligible[1]:
                pairtests+=1
                joined=a.union(b)
                if len(joined)<=bound:pairset.add(joined)
        if not pairset:stats['empty_pair']+=1;continue
        for u in pairset:
            for v in eligible[2]:
                tripletests+=1
                assert len(u.union(v))>bound, ('found 93',pid,triple,bound)
        stats['final_reject']+=1
    print(pid,dict(stats),'pair_tests',pairtests,'triple_tests',tripletests,flush=True)
    assert stats['fixed_reject']==816 and stats['screened']==1208
    assert stats['empty_label']==914
    (P/f'RADIUS3_INDEPENDENT_{pid}.json').write_text(json.dumps({'profile':pid,'stats':dict(stats),'pair_tests':pairtests,'triple_tests':tripletests,'scope':'all unordered triple-labelled local substitutions under fixed 7-key allowlist; separate key-forcing lemma covers all 7-key completions'},indent=2)+'\n')
