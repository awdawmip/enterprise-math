#!/usr/bin/env python3
"""EC49FGH independent original-DFA and ordered signed X6 six-key witness verifier."""
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
def verify(path):
    rows=json.load(open(path))['demands']
    seen={};K=set();P=set()
    for r in rows:
        h,s,w,key=r['window'],r['signature'],r['word'],tuple(r['key'])
        assert len(w)==h and (h,s) not in seen
        q=0;dis=[0]*6;pos=[0]*3;steps=[]
        for op in w:
            q=T[q][OPS.index(op)]; assert q!=8
            for step in STEPS[op]:
                ax=abs(step)-1
                dis[ax]+=1 if step>0 else -1
                if step>0:pos[ax]+=1
                steps.append(step);P.add(tuple(steps))
        assert SIG[q]==s and dis==[2,0,0,0,0,0] and tuple(pos)==key
        K.add(key);seen[h,s]=w
    assert set(seen)=={(h,s) for h,ss in REQ.items() for s in ss}
    assert len(seen)==24 and len(K)==6 and len(P)==100
    return {'schema':'EC49FGH_NATIVE_CERTIFICATE_V1','demands':len(seen),
            'raw_keys':sorted(K),'raw_key_count':len(K),
            'native_ordered_prefix_edges':len(P),'verified':True,
            'claim_scope':'exact six-key 100-edge upper witness only'}
if __name__=='__main__':
    print(json.dumps(verify(sys.argv[1]),indent=2))
