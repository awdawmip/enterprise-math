#!/usr/bin/env python3
"""EC49FGO complete H7/H8 fixed-16 one-incoherence finite certificate.
Uses literal EC49FCZ nine-state BRC and ordered signed-X6 microsteps; stdlib.
"""
import argparse, itertools, json
from collections import defaultdict, Counter
from pathlib import Path
O='acdefg'
T=((1,2,3,1,4,5),(1,6,7,1,1,1),(2,2,8,2,2,2),(3,8,3,3,3,3),
   (4,2,7,4,4,4),(5,6,3,5,5,5),(6,6,8,6,6,6),(7,8,7,7,7,7),(8,8,8,8,8,8))
S=(0,0,4,1,16,32,8,2,0)
X={'a':(-1,-1),'c':(1,2,-1,-2),'d':(2,1,-2,-1),'e':(3,1,1,-3),'f':(1,-1),'g':(2,-2)}
SIG=(1,2,4,8)
PIN='fc0f038e7bfd12c886b4d37f900bfb770c0f61ab'

def pref(w):
    p=()
    for a in w:
        for v in X[a]:
            p=p+(v,)
            yield p

def words(h):
    out=defaultdict(list)
    for a in range((h-1)//2+1):
        for c in range(h-2*a):
            for d in range(h-2*a-c):
                for f in range(h-2*a-c-d):
                    g=h-2*a-1-c-d-f
                    counts=[a,c,d,a+1,f,g]
                    def walk(w,q):
                        if len(w)==h:
                            if S[q] in SIG:out[S[q]].append(w)
                            return
                        for j,op in enumerate(O):
                            if counts[j] and T[q][j]!=8:
                                counts[j]-=1
                                walk(w+op,T[q][j]);counts[j]+=1
                    walk('',0)
    return out

def check(profile,raw):
    F=set(itertools.chain.from_iterable(pref(d['word']) for d in profile['demands'] if d['window'] not in (7,8)))
    assert len(F)==78
    ids={};keep={};exists=set()
    for h in (7,8):
        for s in SIG:
            tmp=[]
            for w in raw[h][s]:
                extra=set(pref(w))-F
                if len(extra)>15:continue
                mask=0
                for node in extra:
                    if node not in ids:ids[node]=len(ids)
                    mask|=1<<ids[node]
                tmp.append((mask,w));exists.add((h,s,w))
            keep[h,s]=tmp
    coherent={s:{a for a,w in keep[8,s] if (7,s,w[:7]) in exists} for s in SIG}
    answer={'profile':profile['profile_id'],'fixed_prefixes':78,'masks':len(ids),
            'retained':{f'{h}:{s}':len(keep[h,s]) for h in (7,8) for s in SIG},
            'coherent':{str(s):len(coherent[s]) for s in SIG},'cases':[]}
    for exceptional in SIG:
        other=[s for s in SIG if s!=exceptional]
        two={a|b for a in coherent[other[0]] for b in coherent[other[1]] if (a|b).bit_count()<=15}
        triple={a|b for a in two for b in coherent[other[2]] if (a|b).bit_count()<=15}
        minimal=[]
        for x in sorted(triple,key=lambda x:(x.bit_count(),x)):
            if not any((y&x)==y for y in minimal): minimal.append(x)
        checks=0
        for x in minimal:
            allowance=15-x.bit_count()
            uu=[a for a,w in keep[7,exceptional] if (a&~x).bit_count()<=allowance]
            vv=[b for b,w in keep[8,exceptional] if (b&~x).bit_count()<=allowance]
            for a in uu:
                used=x|a
                for b in vv:
                    checks+=1
                    assert (used|b).bit_count()>15, (profile['profile_id'],exceptional)
        answer['cases'].append({'exceptional_signature':exceptional,'two_masks':len(two),
                                'triple_masks':len(triple),'minimal_triples':len(minimal),
                                'pair_checks':checks,'no_93':True})
    return answer

if __name__=='__main__':
    ap=argparse.ArgumentParser()
    ap.add_argument('--witness',type=Path,default=Path(__file__).resolve().parent.parent/'EC49FGJ_SEVEN_KEY_94_20261110'/'WITNESSES_EC49FGJ.json')
    ap.add_argument('--profile',choices=('A','B'),required=True)
    args=ap.parse_args()
    j=json.loads(args.witness.read_text());assert j['frozen_scientific_pin']==PIN
    raw={h:words(h) for h in (7,8)}
    assert [len(raw[7][s]) for s in SIG]==[5724,6806,5724,6806]
    assert [len(raw[8][s]) for s in SIG]==[28063,34777,28063,34777]
    profile=next(p for p in j['profiles'] if p['profile_id']==args.profile)
    report=check(profile,raw)
    print(json.dumps(report,indent=2,sort_keys=True))
