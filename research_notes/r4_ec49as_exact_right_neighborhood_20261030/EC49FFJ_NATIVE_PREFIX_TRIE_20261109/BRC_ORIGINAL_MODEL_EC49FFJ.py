#!/usr/bin/env python3
"""Pin fc0f038e7bfd12c886b4d37f900bfb770c0f61ab.
Original BRC six-operation ordered signed X6 expansion and nine-state DFA,
transcribed from the source research verifier EC49FFH.
"""
ORDER='acdefg'
OPS={'a':(-1,-1),'c':(1,2,-1,-2),'d':(2,1,-2,-1),
     'e':(3,1,1,-3),'f':(1,-1),'g':(2,-2)}
T=((1,2,3,1,4,5),(1,6,7,1,1,1),(2,2,8,2,2,2),
   (3,8,3,3,3,3),(4,2,7,4,4,4),(5,6,3,5,5,5),
   (6,6,8,6,6,6),(7,8,7,7,7,7),(8,8,8,8,8,8))
SIGNATURE=(0,0,4,1,16,32,8,2,0)

def native(word):
    return tuple(step for op in word for step in OPS[op])

def observed(word):
    state=0
    for op in word:state=T[state][ORDER.index(op)]
    return SIGNATURE[state]

def candidates(h,key):
    x,y,z=key
    a=z-1; cd=x+y-h-1; f=h+1-y-2*z;g=h+1-x
    assert min(a,cd,f,g)>=0
    for c in range(cd+1):
        ct=[a,c,cd-c,z,f,g]
        def rec(prefix,state):
            if not any(ct):
                yield prefix,SIGNATURE[state]
                return
            for i,num in enumerate(ct):
                if num:
                    ct[i]-=1
                    yield from rec(prefix+ORDER[i],T[state][i])
                    ct[i]+=1
        yield from rec('',0)
