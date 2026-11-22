#!/usr/bin/env python3
"""EC49FWO: exact integer-only validation of product CRT inverse with mass."""
import json


def mask_set(mask, size):
    return frozenset(i for i in range(size) if mask & (1 << i))


def conv(S, size):
    out = [0] * size
    for x in S:
        for y in S:
            out[(x + y) % size] += 1
    return tuple(out)


def divisors(x):
    return [i for i in range(1, x+1) if x % i == 0]


def recover_from_spectrum(n, q, N, defect):
    assert q % 2 == 1 and len(defect) == n*q and N > 0
    K = [[0] * q for _ in range(n)]
    for a in range(n):
        for b in range(q):
            d = defect[a*q + b]
            assert d % 2 == 0
            K[a][b] = N - d//2
    B = [sum(K[a][b] for a in range(n)) for b in range(q)]
    matches = []
    for w in divisors(N):
        v = N//w
        if w > n or v > q:
            continue
        if any(t % (w*w) for t in B):
            continue
        KV = tuple(t//(w*w) for t in B)
        V = frozenset(x for x in range(q) if KV[(2*x) % q] % 2)
        if len(V) != v or conv(V, q) != KV:
            continue
        if any(sum(K[a][b] for b in range(q)) % (v*v) for a in range(n)):
            continue
        KU = tuple(sum(K[a][b] for b in range(q))//(v*v) for a in range(n))
        if any(K[a][b] != KU[a]*KV[b] for a in range(n) for b in range(q)):
            continue
        matches.append((w, V, KU))
    assert len(matches) == 1, (n,q,N,defect,matches)
    return matches[0]


def defect_from_product(U,V,n,q):
    w,v = len(U),len(V)
    KU, KV = conv(U,n),conv(V,q)
    return tuple(2*(w*v - KU[a]*KV[b]) for a in range(n) for b in range(q))


def exhaustive(n, q):
    seen = {}
    checked = 0
    collisions_same_spectrum = 0
    ambiguity_in_U = 0
    for umask in range(1, 1<<n):
        U=mask_set(umask,n)
        KU=conv(U,n)
        for vmask in range(1, 1<<q):
            V=mask_set(vmask,q)
            N=len(U)*len(V)
            defect=defect_from_product(U,V,n,q)
            rec=recover_from_spectrum(n,q,N,defect)
            assert rec == (len(U),V,KU)
            key=(N,defect)
            if key in seen:
                collisions_same_spectrum += 1
                prev=seen[key]
                assert prev[0] == len(U) and prev[1] == V and prev[2] == KU
                if prev[3] != U:
                    ambiguity_in_U += 1
            else:
                seen[key]=(len(U),V,KU,U)
            checked += 1
    return dict(n=n,q=q,pairs=checked,unique_observations=len(seen),
                collisions_with_same_mass=collisions_same_spectrum,
                collisions_with_different_U=ambiguity_in_U,
                different_hole_counts_with_same_observation=0)


def selected_cases():
    n,q=10,11
    U=frozenset([0,1,2,3,4])
    sets={
        'single_hole':frozenset(set(range(q))-{3}),
        'two_holes':frozenset(set(range(q))-{2,7}),
        'three_holes_AP':frozenset(set(range(q))-{1,2,3}),
        'nine_holes':frozenset({2,7}),
    }
    rows=[]
    for name,V in sets.items():
        N=len(U)*len(V)
        D=defect_from_product(U,V,n,q)
        assert recover_from_spectrum(n,q,N,D)==(len(U),V,conv(U,n))
        rows.append(dict(case=name,N=N,hole_count=q-len(V),recovered_holes=sorted(set(range(q))-V)))
    allU=frozenset(range(n)); V=frozenset({2,7}); Vc=frozenset(set(range(q))-V)
    assert defect_from_product(allU,V,n,q)==defect_from_product(allU,Vc,n,q)
    assert len(allU)*len(V)!=len(allU)*len(Vc)
    A=frozenset([0,2,3,4,7]); B=frozenset([0,1,3,4,6]); Q=frozenset(set(range(q))-{0})
    assert A!=B and conv(A,n)==conv(B,n)
    assert defect_from_product(A,Q,n,q)==defect_from_product(B,Q,n,q)
    assert len(A)*len(Q)==len(B)*len(Q)
    assert recover_from_spectrum(n,q,len(A)*len(Q),defect_from_product(A,Q,n,q))==(5,Q,conv(A,n))
    return rows


if __name__=='__main__':
    results={"status":"ALL PASS", "scope":"exact integer-only", "exhaustive":[exhaustive(4,5),exhaustive(4,7)],
             "selected_n10_q11":selected_cases(),"remaining_ambiguity":"U remains non-unique for even n; V, both cardinalities and K_U are unique"}
    print(json.dumps(results,indent=2,ensure_ascii=False,sort_keys=True))
