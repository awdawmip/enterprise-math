#!/usr/bin/env python3
"""EC49FER: standard-library finite certificate for 98 native prefixes.
Original science freeze: fc0f038e7bfd12c886b4d37f900bfb770c0f61ab.
"""
import json
from collections import Counter
from functools import lru_cache

ORDER='acdefg'
OPS={'a':(-1,-1),'c':(1,2,-1,-2),'d':(2,1,-2,-1),
     'e':(3,1,1,-3),'f':(1,-1),'g':(2,-2)}
T=((1,2,3,1,4,5),(1,6,7,1,1,1),(2,2,8,2,2,2),
   (3,8,3,3,3,3),(4,2,7,4,4,4),(5,6,3,5,5,5),
   (6,6,8,6,6,6),(7,8,7,7,7,7),(8,8,8,8,8,8))
SIG=(0,0,4,1,16,32,8,2,0)
KEYS=((3,1,1),(3,2,1),(4,3,1),(4,4,1),(5,5,1))
HIGH={4,6,7,9}
W={
 2:{1:'de',2:'ed',4:'ce',8:'ec'},
 3:{1:'deg',8:'ecg',16:'feg'},
 4:{16:'fegg',32:'ggfe'},
 5:{1:'ggfed',2:'feggd',4:'feggc',8:'ggfec'},
 6:{16:'fegggf',32:'ggfegf'},
 7:{16:'fegggfg',32:'ggfegfg'},
 8:{1:'ggfegfgd',2:'fegggfgd',4:'fegggfgc',8:'ggfegfgc'},
 9:{16:'fegggfggf',32:'ggfegfggf'}
}
CERT={
 1:((2,1),(2,2),(2,4)),
 2:((2,1),(2,2),(2,4),(3,16),(4,32)),
 3:((2,1),(2,2),(2,4),(4,16),(9,32)),
 4:((2,1),(2,2),(2,4),(4,16),(9,32)),
 5:((2,1),(2,2),(2,4),(2,8),(3,16),(4,32)),
 6:((2,1),(2,2),(2,4),(2,8),(3,16),(4,32)),
 7:((2,1),(2,2),(2,4),(2,8),(3,16),(4,32)),
 8:((2,1),(2,2),(2,4),(2,8),(3,16),(4,32)),
 9:((3,1),(3,8),(4,16),(4,32)),
 10:((3,1),(3,8),(4,16),(4,32)),
 11:((5,1),(5,2),(5,4),(5,8)),
 12:((5,1),(5,2),(5,4),(5,8),(6,16),(6,32)),
 13:((5,1),(5,2),(5,4),(5,8),(6,16),(6,32)),
 14:((5,1),(5,2),(5,4),(5,8),(6,16),(6,32)),
 15:((7,16),(7,32)),
 16:((7,16),(7,32)),
 17:((8,1),(8,2),(8,4),(8,8)),
 18:((8,1),(8,2),(8,4),(8,8),(9,16),(9,32)),
 19:((8,1),(8,2),(8,4),(8,8),(9,16),(9,32)),
 20:((8,1),(8,2),(8,4),(8,8),(9,16),(9,32))
}
def native(w): return tuple(s for o in w for s in OPS[o])
def brc(w):
    counts=Counter(s for s in native(w) if s>0)
    return tuple(counts[i] for i in (1,2,3))
def signature(w):
    q=0
    for a in w:q=T[q][ORDER.index(a)]
    return SIG[q]
@lru_cache(None)
def group(h,target):
    found=set()
    for x,y,z in KEYS:
        a=z-1;cd=x+y-h-1;f=h+1-y-2*z;g=h+1-x
        if min(a,cd,f,g)<0:continue
        for c in range(cd+1):
            ct=[a,c,cd-c,z,f,g]
            def rec(prefix,q):
                if not any(ct):
                    if SIG[q]==target:found.add(prefix)
                    return
                for i,v in enumerate(ct):
                    if v:
                        ct[i]-=1
                        rec(prefix+ORDER[i],T[q][i])
                        ct[i]+=1
            rec('',0)
    return frozenset(found)
def verify():
    labels=[(h,s) for h in range(2,10)
            for s in ((1,8,16) if h==3 else ((16,32) if h in HIGH else (1,2,4,8)))]
    gs={q:group(*q) for q in labels}
    assert len(gs)==23 and all(gs.values()) and sum(map(len,gs.values()))==2471
    assert set(gs)=={(h,s) for h,row in W.items() for s in row}
    for (h,s),words in gs.items():
        assert W[h][s] in words
        for w in words:
            n=native(w);counts=Counter(n)
            assert len(w)==h and brc(w) in KEYS and signature(w)==s
            assert tuple(counts[i]-counts[-i] for i in range(1,7))==(2,0,0,0,0,0)
    assert max(len(native(w)) for words in gs.values() for w in words)==20
    packing=[]
    for d in range(1,21):
        seen=set()
        for q in CERT[d]:
            ws=gs[q]
            assert all(len(native(w))>=d for w in ws)
            ps={native(w)[:d] for w in ws}
            assert not seen.intersection(ps),(d,q)
            seen.update(ps)
        packing.append(len(CERT[d]))
    selected=[W[h][s] for h,s in labels]
    prefixes={native(w)[:d] for w in selected for d in range(1,len(native(w))+1)}
    assert len(selected)==23 and len({brc(w) for w in selected})==5
    assert sum(packing)==98==len(prefixes)
    return {'status':'PASS','frozen_science_pin':'fc0f038e7bfd12c886b4d37f900bfb770c0f61ab',
            'candidate_words':2471,'mandatory_groups':len(gs),'depth_bound':packing,
            'certified_lower':sum(packing),'witness_upper':len(prefixes),
            'exact_optimum':98,'witness_words':{str(h):{str(s):w for s,w in W[h].items()} for h in W}}
if __name__=='__main__':print(json.dumps(verify(),indent=2))
