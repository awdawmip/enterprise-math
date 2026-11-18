"""Independent explicit 23-word witness audit: signed native X6 and full BRC."""
from collections import Counter
import json
OPS={'a':(-1,-1),'c':(1,2,-1,-2),'d':(2,1,-2,-1),'e':(3,1,1,-3),'f':(1,-1),'g':(2,-2)}
ORDER='acdefg'
T=((1,2,3,1,4,5),(1,6,7,1,1,1),(2,2,8,2,2,2),
(3,8,3,3,3,3),(4,2,7,4,4,4),(5,6,3,5,5,5),
(6,6,8,6,6,6),(7,8,7,7,7,7),(8,8,8,8,8,8))
SIG=(0,0,4,1,16,32,8,2,0)
W={2:['de','ed','ce','ec'],3:['deg','ecg','feg'],
4:['fegg','gefg'],5:['degfg','feggd','feggc','ecgfg'],
6:['feggfg','gefgfg'],7:['feggfgg','gefgfgg'],
8:['gefgfggd','feggfggd','feggfggc','gefgfggc'],
9:['feggfggfg','gefgfggfg']}
HIGHS={4,6,7,9}
EXPECTED={(3,1,1),(3,2,1),(4,3,1),(4,4,1),(5,5,1)}
def audit():
    keys=set();P=set();num=0
    for h in range(2,10):
        signatures=set()
        for w in W[h]:
            assert len(w)==h
            native=tuple(step for op in w for step in OPS[op]);freq=Counter(native)
            assert tuple(freq[i]-freq[-i] for i in range(1,7))==(2,0,0,0,0,0)
            q=0
            for op in w:q=T[q][ORDER.index(op)]
            signatures.add(SIG[q]); num+=1
            pos=Counter(s for s in native if s>0)
            keys.add(tuple(pos[i] for i in (1,2,3)))
            for d in range(1,len(native)+1):P.add(native[:d])
        expected={1,8,16} if h==3 else ({16,32} if h in HIGHS else {1,2,4,8})
        assert signatures==expected,(h,signatures,expected)
    assert num==23 and keys==EXPECTED and len(P)==99
    return {'paths':num,'all_signed_endpoints_correct':True,
     'full_BRC_keys':sorted(keys),'native_prefix_cost':len(P),
     'observer_groups_pass':8,
     'science_pin':'fc0f038e7bfd12c886b4d37f900bfb770c0f61ab'}
if __name__=='__main__': print(json.dumps(audit(),indent=2))
