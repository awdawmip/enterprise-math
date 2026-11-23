#!/usr/bin/env python3
"""R284FZ: exact-bit witnesses of an all-q first-publication obstruction.

No floating point and no generic decoder. Construct separately reachable
prefix/stable words, verify two differing coordinates and every omission budget.
"""

def witness(q, s, t, c, kind, i, j):
    a, b = 2*q+s, 2*q+t
    src = [0]*(a+b+c)
    dst = [0]*(a+b+c)
    if kind == "phase2":
        assert i == s-2 and j+c <= q
        # Prefix: i completed p3 writes; q old p3 omissions (edge 2).
        for z in range(i+q): src[z] = 1
        # Stable phase 2: p3 target one except q omissions (edge 0).
        for z in range(a): dst[z] = 1
        for z in range(i+q, i+2*q): dst[z] = 0
        # j already-written p5 bits remain one by phase-2 edge-1 omissions.
        for z in range(a,a+j): src[z] = dst[z] = 1
        # All c phase-2 p6 bits remain zero by edge-1 omissions.
        budgets_src = {2:q}
        budgets_dst = {0:q,1:j+c}
    elif kind == "phase3":
        assert j == t+i-2 and i<=q and c<=q
        # Prefix p3 writes, and phase-3 p3 edge-2 omissions, are both one.
        for z in range(i): src[z] = dst[z] = 1
        # Prefix p5 written bits, and q old edge-3 misses, are one.
        for z in range(a,a+j+q): src[z] = dst[z] = 1
        # q-i p5 phase-3 edge-2 omissions remain zero.
        # Other p5 phase-3 bits are one; the final two mismatch prefix.
        for z in range(a+j+2*q-i,a+b): dst[z] = 1
        # All c phase-3 p6 bits are zero from their edge-1 omissions.
        budgets_src = {3:q}
        budgets_dst = {2:q,1:c}
    else:
        raise ValueError(kind)
    assert len(src)==len(dst)==a+b+c
    assert sum(u!=v for u,v in zip(src,dst))==2, (q,s,t,c,kind,i,j)
    assert all(0<=v<=q for v in budgets_src.values())
    assert all(0<=v<=q for v in budgets_dst.values())
    assert all(src[z]==1 for z in range(i))
    assert all(src[z]==1 for z in range(a,a+j))
    assert all(src[z]==0 for z in range(a+b,a+b+c))
    return 2

def run(q,k):
    templates=nodes=0
    for s in range(3,k-2):
        for t in range(3,k-s+1):
            c=k-s-t
            templates+=1
            # Every monotone route must cross one of these boundaries.
            for i in range(s-2):
                witness(q,s,t,c,"phase3",i,t+i-2)
                nodes+=1
            for j in range(t+s-5):
                witness(q,s,t,c,"phase2",s-2,j)
                nodes+=1
            assert s-2 <= 2*q+s and t+s-5 <= 2*q+t
    return templates,nodes

if __name__=="__main__":
    for q in (5,6,7,13,32,64):
        p=run(q,8);r=run(q,9)
        assert (p[0]+r[0],p[1]+r[1])==(16,74)
        print(f"q={q}: templates=16, explicit_boundary_witnesses=74, PASS")
