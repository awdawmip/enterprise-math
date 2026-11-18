"""EC49FEQ 23-path H3 mixed support: self-contained exact signature census.
Frozen original science pin fc0f038e7bfd12c886b4d37f900bfb770c0f61ab.
"""
from itertools import combinations, product
from functools import lru_cache
import json

OPS = {'a':(-1,-1), 'c':(1,2,-1,-2), 'd':(2,1,-2,-1),
       'e':(3,1,1,-3), 'f':(1,-1), 'g':(2,-2)}
ORDER='acdefg'
T=((1,2,3,1,4,5),(1,6,7,1,1,1),(2,2,8,2,2,2),
   (3,8,3,3,3,3),(4,2,7,4,4,4),(5,6,3,5,5,5),
   (6,6,8,6,6,6),(7,8,7,7,7,7),(8,8,8,8,8,8))
SIG=(0,0,4,1,16,32,8,2,0)
@lru_cache(None)
def signatures(h,k):
    x,y,z=k
    a=z-1; r=x+y-h-1; f=h+1-y-2*z; g=h+1-x
    if min(a,r,f,g)<0: return frozenset()
    @lru_cache(None)
    def dp(q,counts):
        if not any(counts): return frozenset((SIG[q],)) if SIG[q] else frozenset()
        out=set()
        for j,n in enumerate(counts):
            if n:
                nxt=list(counts);nxt[j]-=1
                out.update(dp(T[q][j],tuple(nxt)))
        return frozenset(out)
    out=set()
    for nc in range(r+1): out.update(dp(0,(a,nc,r-nc,z,f,g)))
    return frozenset(out)

def high_keys(h):
    out=set()
    for z in range(1,(h+1)//2+1):
        for r in range(h-2*z+2):
            for f in range(h-2*z+2-r):
                g=h-2*z+1-r-f
                k=(r+2*z+f,r+g,z)
                if {16,32}<=signatures(h,k):out.add(k)
    return tuple(sorted(out))

def census():
    late=tuple(range(4,10)); hk={h:high_keys(h) for h in late}
    assert [len(hk[h]) for h in late]==[2,4,6,9,12,16]
    by_high={}; total=early=feasible=0
    for high in combinations(late,4):
        n=ne=nf=0; low=tuple(h for h in late if h not in high)
        for choice in product(*(hk[h] for h in high)):
            n+=1; K=((3,1,1),)+choice
            if not {1,8}<=set().union(*(signatures(3,k) for k in choice)):continue
            ne+=1
            if all({1,2,4,8}<=set().union(*(signatures(h,k) for k in K)) for h in low):nf+=1
        by_high[''.join(map(str,high))]=[n,ne,nf]
        total+=n;early+=ne;feasible+=nf
    assert (total,early,feasible)==(42048,18504,12276)
    return {'frozen_science':'fc0f038e7bfd12c886b4d37f900bfb770c0f61ab',
            'high_key_options':{str(h):len(hk[h]) for h in late},
            'columns':['inventories','H3_mixed_available','all_signatures_available'],
            'type_B_by_late_high':by_high,'type_B_total':total,
            'type_B_feasible':feasible,'type_C_feasible_by_involution':feasible,
            'two_type_total':2*total,'two_type_feasible':2*feasible}
if __name__=='__main__':print(json.dumps(census(),indent=2))
