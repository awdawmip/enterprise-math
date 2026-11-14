#!/usr/bin/env python3
"""EC49FET native X6 signed-word and nine-state DFA independent enumeration.
Science frozen at fc0f038e7bfd12c886b4d37f900bfb770c0f61ab.
"""
import json,sys
from collections import defaultdict,Counter
from functools import lru_cache

OPERATIONS = {"a":(-1,-1),"c":(1,2,-1,-2),"d":(2,1,-2,-1),"e":(3,1,1,-3),"f":(1,-1),"g":(2,-2)}
ALPHABET = 'acdefg'
NEXT=((1,2,3,1,4,5),(1,6,7,1,1,1),(2,2,8,2,2,2),
      (3,8,3,3,3,3),(4,2,7,4,4,4),(5,6,3,5,5,5),
      (6,6,8,6,6,6),(7,8,7,7,7,7),(8,8,8,8,8,8))
OBS=(0,0,4,1,16,32,8,2,0)
@lru_cache(None)
def words_with_label(h,k):
    x,y,z=k
    A=z-1;CD=x+y-h-1; F=h+1-y-2*z;G=h+1-x
    if min(A,CD,F,G)<0:return ()
    all_word=set()
    for C in range(CD+1):
        counts=[A,C,CD-C,z,F,G]
        def walk(prefix,st):
            if sum(counts)==0:
                if OBS[st]:all_word.add((OBS[st],prefix))
                return
            for j in range(6):
                if counts[j]:
                    counts[j]-=1;walk(prefix+ALPHABET[j],NEXT[st][j]);counts[j]+=1
        walk('',0)
    return tuple(sorted(all_word))

def native_prefixes(w):
    current=()
    for ch in w:
        for step in OPERATIONS[ch]:
            current+= (step,)
            yield current

