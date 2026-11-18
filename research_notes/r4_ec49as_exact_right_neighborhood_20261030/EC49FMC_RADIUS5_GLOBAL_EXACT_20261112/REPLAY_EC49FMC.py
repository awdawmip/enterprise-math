#!/usr/bin/env python3
"""Rebuild exactly the 1,137 radius-five signed-X6 BRC scanner cases; writes complete input on stdout."""
from functools import lru_cache,reduce
import collections,json,sys
from pathlib import Path
P=Path(__file__).resolve().parent
sys.path.insert(0,str(P.parent/'EC49FJD_RELEASE_B11_COMPLETE_20261111'))
from EC49FGW_RADIUS5_SCREEN import PIN,all_words,raw_key,pref
assert PIN=='fc0f038e7bfd12c886b4d37f900bfb770c0f61ab'
REQ={2:(16,32),3:(16,32),4:(1,2,4,8),5:(16,32),6:(1,2,4,8),7:(1,2,4,8),8:(1,2,4,8),9:(16,32)}
labels=sorted((h,s) for h,ss in REQ.items() for s in ss)
assert len(labels)==24
li={lab:i for i,lab in enumerate(labels)}
forced=((2,1,1),(3,0,1))
seed={(3,1,1),(4,2,1),(5,3,1),(5,4,1),(6,4,1)}
support=collections.defaultdict(int)
bykey=collections.defaultdict(list)
nword=0
for lab,w in all_words():
    k=raw_key(w)
    support[k]|=1<<li[lab]
    bykey[k].append((li[lab],pref(w)[-1].hex()))
    nword+=1
assert nword==178850 and len(support)==94
assert {k for k in support if support[k] & (1<<li[(2,16)])}=={forced[1]}
assert {k for k in support if support[k] & (1<<li[(2,32)])}=={forced[0]}
other=sorted(set(support)-set(forced))
assert len(other)==92
required=((1<<24)-1) & ~(support[forced[0]]|support[forced[1]])
assert required==16777212
masks=[support[k]&required for k in other]
original=[int(k in seed) for k in other]
@lru_cache(None)
def ways(i,k,mask):
    if not k:return int(mask==required)
    if len(other)-i<k:return 0
    return ways(i+1,k,mask)+ways(i+1,k-1,mask|masks[i])
assert ways(0,5,0)==108434
selected=[]
def walk(i,k,mask,chosen):
    if not k:
        if mask==required and not any(original[t] for t in chosen):selected.append(chosen)
        return
    if len(other)-i<k:return
    if ways(i+1,k-1,mask|masks[i]):walk(i+1,k-1,mask|masks[i],chosen+(i,))
    if ways(i+1,k,mask):walk(i+1,k,mask,chosen)
walk(0,5,0,())
assert len(selected)==1137
cases=[]
for chosen in selected:
    keys=forced+tuple(other[i] for i in chosen)
    first=collections.defaultdict(set)
    rows=[]
    for key in keys:
        words=bykey[key]
        rows.extend(words)
        for lab,hexword in words:first[lab].add(hexword[:2])
    ambiguity=sum(len(v)-1 for v in first.values())
    essential=sum(int(reduce(int.__or__,(masks[j] for j in chosen if j!=i),0)!=required) for i in chosen)
    cases.append((ambiguity,len(rows),chosen,essential,rows,keys))
cases.sort(key=lambda x:(x[0],x[1],x[2],x[3]))
manifest=[{'id':i,'optional_indices':chosen,'keys':keys,'root_ambiguity':amb,'word_count':nr,'essential_nonforced_keys':e} for i,(amb,nr,chosen,e,rows,keys) in enumerate(cases)]
(P/'EC49FMC_RADIUS5_MANIFEST.json').write_text(json.dumps(manifest,separators=(',',':'))+'\n')
print(len(cases))
for _,_,_,_,rows,_ in cases:
    print(len(rows))
    for label,hexword in rows:print(label,hexword)
print('EC49FMC_PREPARE_PASS 1137',file=sys.stderr)
