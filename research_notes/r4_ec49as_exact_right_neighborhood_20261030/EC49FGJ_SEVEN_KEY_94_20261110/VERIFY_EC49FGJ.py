#!/usr/bin/env python3
"""Independent exact signed-X6 and original 9-state DFA audit for EC49FGJ."""
import json,sys
OPS="acdefg"
T=((1,2,3,1,4,5),(1,6,7,1,1,1),(2,2,8,2,2,2),(3,8,3,3,3,3),(4,2,7,4,4,4),(5,6,3,5,5,5),(6,6,8,6,6,6),(7,8,7,7,7,7),(8,8,8,8,8,8))
SIG=(0,0,4,1,16,32,8,2,0)
STEPS={'a':(-1,-1),'c':(1,2,-1,-2),'d':(2,1,-2,-1),'e':(3,1,1,-3),'f':(1,-1),'g':(2,-2)}
REQ={2:(16,32),3:(16,32),4:(1,2,4,8),5:(16,32),6:(1,2,4,8),7:(1,2,4,8),8:(1,2,4,8),9:(16,32)}
def audit(rows):
    edges=set();keys=set();seen=set()
    for row in rows:
        h,s,w=row['window'],row['signature'],row['word']
        assert len(w)==h and (h,s) not in seen
        seen.add((h,s));state=0;point=[0]*6;plus=[0]*3;steps=[]
        for ch in w:
            state=T[state][OPS.index(ch)];assert state!=8
            for a in STEPS[ch]:
                steps.append(a);edges.add(tuple(steps))
                point[abs(a)-1]+=(a>0)-(a<0)
                if 0<a<=3:plus[a-1]+=1
        assert SIG[state]==s and point==[2,0,0,0,0,0],(h,s,w)
        keys.add(tuple(plus))
    assert seen=={(h,s) for h,ss in REQ.items() for s in ss}
    return len(seen),len(keys),len(edges),sorted(keys)
def main(path):
    data=json.load(open(path,encoding='utf-8'))
    assert data['frozen_scientific_pin']=='fc0f038e7bfd12c886b4d37f900bfb770c0f61ab'
    for p in data['profiles']:
        n,k,edges,keys=audit(p['demands'])
        assert (n,k,edges)==(24,7,94)
        assert [list(t) for t in keys]==p['claimed_keys']
        print('PASS',p['profile_id'],'demands',n,'raw_keys',k,'signed_microstep_prefix_edges',edges)
if __name__=='__main__':main(sys.argv[1])
