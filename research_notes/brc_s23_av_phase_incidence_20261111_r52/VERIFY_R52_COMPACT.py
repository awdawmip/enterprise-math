"""Independent integer reproduction of R52 complete labelled phase-event updates.
A deliberately separate cut-ranking oracle (sort / heapq.nlargest) checks R52
without importing the R51 rank/select implementation. Python stdlib only.
"""
from bisect import bisect_right
from heapq import nlargest, heappush, heappop, heapify
from math import isqrt

S23=(262204504569236716045286,262204504569236716045287,10**24)
D=10**32
q=isqrt(2*D*D)
assert q*q<2*D*D<(q+1)**2
QUAD=(q-D,q+1-D,D)

def verify(name,m,H,enclosure,depth):
    L,U,D=enclosure;B=L+U;Q=2*D;K=m+H-1
    historical=sorted(((z*B)%Q,z) for z in range(m))
    phase=[p for p,z in historical]
    prev={z:historical[i-1][1] for i,(_,z) in enumerate(historical)}
    if depth==K:
        cuts=sorted(range(1,K+1), key=lambda s:(s*B)%Q,reverse=True)
    else:
        cuts=nlargest(depth,range(1,K+1),key=lambda s:(s*B)%Q)
    def reconstruct(s):
        x=s*B%Q
        return tuple(historical[bisect_right(phase,(x-r*B)%Q)-1][1]
                     for r in range(1,H+1))
    owner=[-1]+list(reconstruct(cuts[0]));version=[0]*(H+1)
    heaps=[[] for _ in range(m)]
    for r in range(1,H+1):heaps[owner[r]].append((r,0))
    for h in heaps:heapify(h)
    def ages():
        out=[]
        for z,h in enumerate(heaps):
            while h and (owner[h[0][0]]!=z or version[h[0][0]]!=h[0][1]):heappop(h)
            out.append(h[0][0] if h else None)
        return tuple(out)
    state=ages();changes=0;events=0;equal_count_changed=0;same_prefix=1
    for j in range(1,len(cuts)):
        s=cuts[j-1]
        for z in range(max(0,s-H),min(m-1,s-1)+1):
            r=s-z;assert owner[r]==z,(name,j,s,r)
            owner[r]=prev[z];version[r]+=1
            heappush(heaps[prev[z]],(r,version[r]));events+=1
        assert tuple(owner[1:])==reconstruct(cuts[j]),(name,j,'owner')
        now=ages()
        direct=[None]*m
        for r in range(1,H+1):
            z=owner[r]
            if direct[z] is None:direct[z]=r
        assert now==tuple(direct),(name,j,'min')
        if now!=state:
            changes+=1
            if sum(x is not None for x in now)==sum(x is not None for x in state):equal_count_changed+=1
        elif changes==0:same_prefix+=1
        state=now
    print('PASS_R52_COMPACT',name,'K',K,'cells',len(cuts),
          'events',events,'vector_changes',changes,'same_prefix',same_prefix,
          'count_masked_changes',equal_count_changed,'top',cuts[:5])
    return events

if __name__=='__main__':
    assert verify('frozen_S23',128,225,S23,352)==28672
    assert verify('quadratic_m5_H8',5,8,QUAD,12)==35
    assert verify('quadratic_large',8,999993,QUAD,4)==24
    print('PASS_R52_COMPACT_3_FAMILIES')
