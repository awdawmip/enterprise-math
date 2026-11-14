#!/usr/bin/env python3
"""Standalone standard-library verifier: all-low U=9 four-key native-prefix packing.
Proves C_native>=150 for this FIXED key inventory and 32 specified groups.
Also verifies an explicit 239-edge feasible construction.
Frozen source: fc0f038e7bfd12c886b4d37f900bfb770c0f61ab.
"""
from collections import Counter, defaultdict

ORDER='acdefg'
OPS={'a':(-1,-1),'c':(1,2,-1,-2),'d':(2,1,-2,-1),
     'e':(3,1,1,-3),'f':(1,-1),'g':(2,-2)}
T=((1,2,3,1,4,5),(1,6,7,1,1,1),(2,2,8,2,2,2),
   (3,8,3,3,3,3),(4,2,7,4,4,4),(5,6,3,5,5,5),
   (6,6,8,6,6,6),(7,8,7,7,7,7),(8,8,8,8,8,8))
SIG=(0,0,4,1,16,32,8,2,0)
K={3:(3,1,1),4:(3,2,1),6:(4,3,1),10:(6,5,1)}
ASSIGN={2:3,3:4,4:6,5:6,6:10,7:10,8:10,9:10}

# One candidate-independent disjointness certificate per native-prefix depth.
# Three digits: 1-digit horizon, 2-digit (zero-padded) signature.
PACK='''
404 602 701
404 602 701
404 602 701
404 602 701
208 404 602 701
208 404 602 701
301 308 404 602
308 404 602 701
308 404 602 701
308 404 602 701
404 602 608 701
404 504 508 601 602 608 901 902
404 504 508 601 602 608 901 902
404 504 508 601 602 608 901 902
601 602 608 704 901 902
601 602 608 704 802 808 901 904
601 602 608 704 802 808 901 904
601 602 608 704 802 808 901 904
601 602 608 704 802 808 901 904
601 602 604 608 701 702 704 708 801 802 804 808 901 902 904 908
601 602 604 608 701 702 704 708 801 802 804 808 901 902 904 908
601 602 604 608 701 702 704 708 801 802 804 808 901 902 904 908
'''

# Explicit one-word-per-group witness. Each row is h,signature,operation-word.
WITNESS='''
9,1,defffgggg
9,2,edfffgggg
9,4,cefffgggg
9,8,egcfffggg
8,1,deffdggg
8,2,edffdggg
8,4,ceffcggg
8,8,egcffcgg
7,1,defddgg
7,2,edfddgg
7,4,cefccgg
7,8,egcfccg
6,1,dedddg
6,2,eddddg
6,4,cecccg
6,8,egcccc
5,1,defgg
5,2,edfgg
5,4,cefgg
5,8,egcfg
4,1,dedg
4,2,eddg
4,4,cecg
4,8,egcc
3,1,deg
3,2,edg
3,4,ceg
3,8,egc
2,1,de
2,2,ed
2,4,ce
2,8,ec
'''

def native(word):
    return tuple(t for op in word for t in OPS[op])

def observed(word):
    state=0
    for op in word:state=T[state][ORDER.index(op)]
    return SIG[state]

def candidates(h,key):
    x,y,z=key
    a=z-1; cd=x+y-h-1; f=h+1-y-2*z; g=h+1-x
    assert min(a,cd,f,g)>=0
    for c in range(cd+1):
        ct=[a,c,cd-c,z,f,g]
        def rec(prefix,state):
            if not any(ct):
                yield prefix,SIG[state]
                return
            for i,num in enumerate(ct):
                if num:
                    ct[i]-=1
                    yield from rec(prefix+ORDER[i],T[state][i])
                    ct[i]+=1
        yield from rec('',0)

def verify():
    groups=defaultdict(list)
    n_words=0
    for h in range(2,10):
        key=K[ASSIGN[h]]
        for word,signature in candidates(h,key):
            assert len(word)==h
            if signature not in (1,2,4,8):continue
            n=native(word)
            assert len(n)==2*(key[0]+key[1]+key[2]-1)
            count=Counter(n)
            assert tuple(count[i]-count[-i] for i in range(1,7))==(2,0,0,0,0,0)
            assert tuple(count[i] for i in (1,2,3))==key
            assert observed(word)==signature
            groups[(h,signature)].append(n)
            n_words+=1
    assert len(groups)==32 and n_words==9460,(len(groups),n_words)
    pack_rows=[r.strip().split() for r in PACK.strip().splitlines()]
    assert len(pack_rows)==22
    costs=[]
    for depth,row in enumerate(pack_rows,start=1):
        seen=set()
        for item in row:
            assert len(item)==3 and item[0].isdigit() and item[1:].isdigit()
            group=(int(item[0]),int(item[1:]))
            assert group in groups and all(len(n)>=depth for n in groups[group])
            prefixes={n[:depth] for n in groups[group]}
            assert not prefixes.intersection(seen),(depth,group)
            seen.update(prefixes)
        assert len(set(row))==len(row)
        costs.append(len(row))
    lower=sum(costs)
    assert lower==150,(lower,costs)
    witness={};prefix_union=set()
    for row in WITNESS.strip().splitlines():
        h,s,w=row.split(',');h=int(h);s=int(s)
        n=native(w)
        assert (h,s) not in witness and n in groups[(h,s)]
        witness[(h,s)]=w
        prefix_union.update(n[:depth] for depth in range(1,len(n)+1))
    assert len(witness)==32
    upper=len(prefix_union)
    assert upper==239,upper
    return {'status':'EXACT_INTEGER_PASS','frozen_pin':'fc0f038e7bfd12c886b4d37f900bfb770c0f61ab',
            'fixed_keys':K,'groups':len(groups),'candidate_words':n_words,
            'per_depth_lower':costs,'certified_lower':lower,'explicit_upper':upper}

if __name__=='__main__':
    import json
    print(json.dumps(verify(),indent=2))
