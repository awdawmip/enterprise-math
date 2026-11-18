#!/usr/bin/env python3
"""Independent prefix parser and exact duplicate-only three-label obstruction verifier."""
import collections,itertools,json,os,sys
from pathlib import Path
BASE=Path(__file__).resolve().parent
D=Path(os.environ.get('EC49FKB_INPUT_DIR',BASE.parent/'EC49FJD_RELEASE_B11_COMPLETE_20261111'))
sys.path.insert(0,str(D))
import EC49FGW_RADIUS5_SCREEN as g
C=json.loads((BASE/'EXACT_TRIPLE_CERTS_EC49FKC.json').read_text())
assert C['frozen_pin']==g.PIN=='fc0f038e7bfd12c886b4d37f900bfb770c0f61ab'
STEP={'a':(-1,-1),'c':(1,2,-1,-2),'d':(2,1,-2,-1),'e':(3,1,1,-3),'f':(1,-1),'g':(2,-2)}
def prefix(w):
    path=();res=set()
    for op in w:
        for s in STEP[op]:
            path+=(s,);res.add(path)
    return frozenset(res)
def key(w):
    steps=[a for c in w for a in STEP[c]]
    return tuple(steps.count(j) for j in (1,2,3))
catalog=list(g.all_words());assert len(catalog)==178850
certs=collections.defaultdict(list)
for c in C['triples']:certs[c['profile']].append(c)
checked={}
for prof in g.W['profiles']:
    who=prof['profile_id'];rows=sorted(prof['demands'],key=lambda a:(a['window'],a['signature']))
    labels=[(d['window'],d['signature']) for d in rows]
    supports=collections.defaultdict(int);key_s=collections.defaultdict(int)
    keys={key(d['word']) for d in rows}
    assert len(keys)==7
    for i,d in enumerate(rows):
        key_s[key(d['word'])]|=1<<i
        for p in prefix(d['word']):supports[p]|=1<<i
    assert len(supports)==94
    bg=collections.defaultdict(list)
    for Q in itertools.combinations(range(24),7):
        bits=sum(1<<i for i in Q)
        if any((s&bits)==s for s in key_s.values()):continue
        removed=tuple(sorted(p for p,s in supports.items() if (s&bits)==s))
        if len(removed)==16:bg[removed].append(Q)
    assert len(bg)==67 and sum(map(len,bg.values()))==4336
    groups=sorted(bg.items())
    solved=0
    for cert in certs[who]:
        idx=cert['group_index'];rem,Qs=groups[idx-1];L=[tuple(v) for v in cert['obstruction_labels']]
        assert len(rem)==16 and len(Qs)==cert['contexts'] and len(L)==3
        assert all(set(L).issubset({labels[i] for i in Q}) for Q in Qs)
        fixed=set(supports)-set(rem)
        bylab={lab:[] for lab in L}
        for lab,word in catalog:
            if lab in bylab and key(word) in keys:
                delta=prefix(word)-fixed
                if len(delta)<=15:bylab[lab].append(delta)
        assert all(bylab.values())
        states={frozenset()};stage=[]
        for lab in L:
            states={u|v for u in states for v in bylab[lab] if len(u|v)<=15}
            stage.append(len(states))
            if not states:break
        assert not states,(who,idx,L,len(states))
        solved+=len(Qs)
        print('TRIPLE_PASS',who,idx,len(Qs),L,'states',stage,flush=True)
    checked[who]=solved
assert checked=={'A':303,'B':498},checked
print('EC49FKC_DIRECT_801_PASS',checked,flush=True)
