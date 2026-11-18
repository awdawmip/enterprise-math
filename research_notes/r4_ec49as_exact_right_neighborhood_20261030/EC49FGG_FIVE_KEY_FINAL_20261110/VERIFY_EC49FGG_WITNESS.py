#!/usr/bin/env python3
"""Independent signed-native X6 path/observer check of the 24-demand witness."""
import json,sys
OPS='acdefg'
T=((1,2,3,1,4,5),(1,6,7,1,1,1),(2,2,8,2,2,2),
   (3,8,3,3,3,3),(4,2,7,4,4,4),(5,6,3,5,5,5),
   (6,6,8,6,6,6),(7,8,7,7,7,7),(8,8,8,8,8,8))
SIG=(0,0,4,1,16,32,8,2,0)
STEPS={'a':(-1,-1),'c':(1,2,-1,-2),'d':(2,1,-2,-1),
       'e':(3,1,1,-3),'f':(1,-1),'g':(2,-2)}
REQ={2:(16,32),3:(16,32),4:(1,2,4,8),5:(16,32),
     6:(1,2,4,8),7:(1,2,4,8),8:(1,2,4,8),9:(16,32)}
data=json.load(open(sys.argv[1]))
seen={};P=set();K=set()
for row in data['rows']:
    h,s,w,key=row['window'],row['signature'],row['word'],tuple(row['key'])
    assert len(w)==h and (h,s) not in seen
    q=0;dis=[0]*6;prefix=[]
    for op in w:
        q=T[q][OPS.index(op)];assert q!=8
        for step in STEPS[op]:
            dis[abs(step)-1]+=1 if step>0 else -1
            prefix.append(step);P.add(tuple(prefix))
    assert SIG[q]==s and dis==[2,0,0,0,0,0]
    assert tuple(sum(step==j for step in prefix) for j in (1,2,3))==key
    K.add(key);seen[h,s]=w
assert set(seen)=={(h,s) for h,ss in REQ.items() for s in ss}
assert len(seen)==24 and len(K)==5 and len(P)==112
print(json.dumps({'verified':True,'demands':24,'keys':sorted(K),'native_edges':112},indent=2))
