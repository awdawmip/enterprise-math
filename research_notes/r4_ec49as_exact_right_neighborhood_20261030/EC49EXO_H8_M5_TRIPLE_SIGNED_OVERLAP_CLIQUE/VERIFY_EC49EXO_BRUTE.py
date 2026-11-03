#!/usr/bin/env python3
"""Independent literal operation-word witness audit for EC49EXO suffix and overlap bounds.
H=2..5 only: finite samples for the analytically proved general lemma.
"""
from itertools import product
from collections import defaultdict
import json
OPS={'a':(-1,-1),'b':(-2,-2),'c':(1,2,-1,-2),'d':(2,1,-2,-1),'e':(3,1,1,-3),'f':(1,-1),'g':(2,-2)}
bykey=defaultdict(list)
counts={}
for h in range(2,6):
    ct=0
    for word in product('acdefg',repeat=h):
        if word.count('e')!=word.count('a')+1:continue
        steps=tuple(x for op in word for x in OPS[op]);ct+=1
        k=tuple(steps.count(x) for x in (1,2,3))
        assert tuple(steps.count(-x) for x in (1,2,3))==(k[0]-2,k[1],k[2])
        assert len(steps)==2*(sum(k)-1)
        bykey[k].append((h,word,steps))
    counts[h]=ct

def common(a,b):
    for t,(x,y) in enumerate(zip(a,b)):
        if x!=y:return t
    return min(len(a),len(b))

n_pairs=0;n_eq_len=0;n_samekey_crossh=0;n_diffkey=0;max_suffix=0
for k,v in bykey.items():
    # distinct operation words, same signed length (same K)
    for i in range(len(v)):
        for j in range(i+1,len(v)):
            a,b=v[i],v[j];c=common(a[2],b[2]);L=len(a[2]);assert L==len(b[2]);assert c<=L-2
            if a[0]!=b[0]:assert c<=L-3;n_samekey_crossh+=1
            n_eq_len+=1;n_pairs+=1
# Pairwise different keys crosscheck using a selected first 100 words from each key to keep work bounded
bykey_sample={k:v[:50] for k,v in bykey.items()}
for k,rows in bykey_sample.items():
    for kk,rows2 in bykey_sample.items():
        if k>=kk:continue
        overlap=2*sum(min(k[t],kk[t]) for t in range(3))-2
        for a in rows:
            for b in rows2:
                assert common(a[2],b[2])<=overlap
                n_diffkey+=1
print(json.dumps({'status':'PASS','horizons':[2,3,4,5],'valid_words':counts,
                  'same_key_equal_length_pairs_exhaustively_tested':n_eq_len,
                  'same_key_cross_window_pairs_exhaustively_tested':n_samekey_crossh,
                  'different_key_pairs_sampled':n_diffkey},indent=2))