#!/usr/bin/env python3
"""Independent integer-only certificate replay for EC49FGL seven-key 98-edge case."""
import json
import sys

OPS='acdefg'
T=((1,2,3,1,4,5),(1,6,7,1,1,1),(2,2,8,2,2,2),
   (3,8,3,3,3,3),(4,2,7,4,4,4),(5,6,3,5,5,5),
   (6,6,8,6,6,6),(7,8,7,7,7,7),(8,8,8,8,8,8))
SIG=(0,0,4,1,16,32,8,2,0)
STEPS={'a':(-1,-1),'c':(1,2,-1,-2),'d':(2,1,-2,-1),
       'e':(3,1,1,-3),'f':(1,-1),'g':(2,-2)}
REQ={2:(16,32),3:(16,32),4:(1,2,4,8),5:(16,32),
     6:(1,2,4,8),7:(1,2,4,8),8:(1,2,4,8),9:(16,32)}

def check(data):
    assert data['frozen_science']=='fc0f038e7bfd12c886b4d37f900bfb770c0f61ab'
    edges=set(); seen=set(); used=set()
    for row in data['paths']:
        h,s,w=row['h'],row['s'],row['word'];k=tuple(row['key'])
        assert (h,s) not in seen and len(w)==h
        seen.add((h,s));q=0;pt=[0]*6;pos=[0]*3;p=[]
        for op in w:
            assert op in OPS
            q=T[q][OPS.index(op)]; assert q!=8
            for step in STEPS[op]:
                p.append(step);edges.add(tuple(p))
                pt[abs(step)-1]+=1 if step>0 else -1
                if 0<step<=3:pos[step-1]+=1
        assert SIG[q]==s and pt==[2,0,0,0,0,0] and tuple(pos)==k,(h,s,w)
        used.add(k)
    assert seen=={(h,s) for h,labels in REQ.items() for s in labels}
    assert used=={tuple(z) for z in data['fixed_inventory']}
    assert (len(seen),len(used),len(edges))==(24,7,98)
    print('PASS 24 frozen DFA labels; 7 complete raw keys; 98 literal native signed-X6 prefixes')

if __name__=='__main__':
    with open(sys.argv[1] if len(sys.argv)>1 else 'WITNESS_EC49FGL_98.json') as f:
        check(json.load(f))
