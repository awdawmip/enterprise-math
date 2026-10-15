#!/usr/bin/env python3
"""Independent symmetric policy-value recursion for the unreviewed T=3 pairs.
Retains Boolean positive support and both feedback branches; not a native X6 tool.
"""
from functools import lru_cache

def first_depth(n,Q):
    X=(1,)*n if Q==1 else (1,)*(n-1)+(3,)
    Y=(1,)*(n-1)+(2,)
    T=3
    lim=1<<n
    actions=[(lim-1)^(1<<j) for j in range(n)]
    def mass(d):
        return tuple(sum(d[i] for i in range(n) if not r>>i&1) for r in range(lim))
    mx,my=mass(X),mass(Y)
    @lru_cache(None)
    def successor(B,action,side,bit):
        masses=(mx,my)[side]
        out=0
        for r in range(lim):
            if B>>r&1:
                for i in range(n):
                    if action>>i&1:
                        nr=r|(1<<i)
                        if (masses[nr]>=T)==bit:
                            out|=1<<nr
        return out
    @lru_cache(None)
    def outputs(BX,BY,h):
        is_x_safe=all(mx[r]>=Q for r in range(lim) if BX>>r&1)
        is_y_safe=all(my[r]>=Q for r in range(lim) if BY>>r&1)
        answers={(is_x_safe,is_y_safe)}
        if h:
            for a in actions:
                left=outputs(successor(BX,a,0,False),
                             successor(BY,a,1,False),h-1)
                right=outputs(successor(BX,a,0,True),
                              successor(BY,a,1,True),h-1)
                answers.update((p[0] and q[0],p[1] and q[1])
                               for p in left for q in right)
        return frozenset(answers)
    for h in range(n+1):
        possible=outputs(1,1,h)
        if any(a!=b for a,b in possible):
            return h,outputs.cache_info().currsize
    return None,outputs.cache_info().currsize

if __name__=="__main__":
    for n in (5,6):
        for Q in (1,2):
            first,states=first_depth(n,Q)
            print(n,Q,first,states,flush=True)
            assert first==n
    print("EXACT_PUBLIC_POLICY_DP_PASS")
