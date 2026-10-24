#!/usr/bin/env python3
"""Integer ordered-prefix descendant stop counts at new 73rd site."""
from collections import defaultdict
import verify_n14_73 as m

def routed_stop():
    current={(0,0,0):1}
    stopby=defaultdict(lambda:[0,0]); total_firsthit=0
    for n in range(m.N+1):
        nxt=defaultdict(int)
        for (a,b,via),k in current.items():
            st=(n,a,b)
            if st==m.A:
                assert via==0
                via=1; total_firsthit+=k
            z=m.act(st)
            if z!='C':
                stopby[(st,z)][via]+=k
                continue
            for i in range(3):
                nxt[(a+(i==0),b+(i==1),via)]+=k
        current=nxt
    assert not current
    return stopby,total_firsthit

if __name__=='__main__':
    stops,hit=routed_stop()
    assert hit==40
    via={str(st):{'decision':z,'others':v[0],'through_A73':v[1]}
         for (st,z),v in sorted(stops.items()) if v[1]}
    assert len(via)==22
    assert sum(r['through_A73'] for r in via.values())==4280
    print('PASS first-hit=40, descendant states=22, terminal words through A73=4280')
    for k,v in via.items():print(k,v)
