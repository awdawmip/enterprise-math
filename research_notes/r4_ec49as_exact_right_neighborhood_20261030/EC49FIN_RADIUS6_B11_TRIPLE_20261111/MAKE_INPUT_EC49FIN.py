#!/usr/bin/env python3
"""Regenerate exact six-demand B=11 cases and signed-X6 native prefix tries."""
import collections,itertools,json,sys
from pathlib import Path
HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE.parent/'EC49FGW_RADIUS5_EXACT_SCREENS_20261110'))
from EC49FGW_RADIUS5_SCREEN import W,PIN,all_words,pref,raw_key,validate_profile
catalog=list(all_words());assert len(catalog)==178850
for p in W['profiles']:
    name=p['profile_id'];rows,paths=validate_profile(p)
    keys={raw_key(row['word']) for row in rows}
    labels={(r['window'],r['signature']):i for i,r in enumerate(rows)}
    supp=collections.defaultdict(int);ksupp=collections.defaultdict(int)
    for i,(row,ps) in enumerate(zip(rows,paths)):
        ksupp[raw_key(row['word'])]|=1<<i
        for edge in ps:supp[edge]|=1<<i
    assert len(supp)==94 and len(keys)==7
    qlist=[]
    for Q in itertools.combinations(range(24),6):
        mask=sum(1<<i for i in Q)
        removed=sum(s&mask==s for s in supp.values())
        if removed!=12:continue
        if any(s&mask==s for s in ksupp.values()):continue
        qlist.append(Q)
    assert len(qlist)==6284
    (HERE/f'QS_{name}_11.txt').write_text(''.join(' '.join(map(str,q))+'\n' for q in qlist))
    trie={b'':0};parents=[-1];edge_support=[0];terminal=[0]
    for lab,word in catalog:
        if raw_key(word) not in keys:continue
        u=0
        for edge in pref(word):
            if edge not in trie:
                trie[edge]=len(parents);parents.append(u)
                edge_support.append(supp.get(edge,0));terminal.append(0)
            u=trie[edge]
        assert terminal[u]==0
        terminal[u]=1<<labels[lab]
    assert len(parents)==42735 and sum(bool(t) for t in terminal)==9838
    (HERE/f'TRIE_{name}.txt').write_text(''.join(f'{a} {b} {c}\n' for a,b,c in zip(parents,edge_support,terminal)))
    print(name,'cases',len(qlist),'trie nodes',len(parents),'catalog',len(catalog))
print('EC49FIN_INPUT_PASS',PIN)
