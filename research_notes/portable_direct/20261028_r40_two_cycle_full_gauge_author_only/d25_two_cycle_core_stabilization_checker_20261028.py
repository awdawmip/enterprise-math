#!/usr/bin/env python3
"""Exact author check of the two-cycle core decomposition over prime fields.

All enumeration and Gaussian linear algebra use integer residue arithmetic. This
checks finite instances of the proved theorem; it does not prove arbitrary q,n.
"""
from __future__ import annotations

import itertools
import json
import random
from pathlib import Path


def rank(rows, q):
    if not rows:
        return 0
    a = [[v % q for v in row] for row in rows]
    nrows, ncols = len(a), len(a[0])
    pivot_row = 0
    for col in range(ncols):
        pivot = next((i for i in range(pivot_row, nrows) if a[i][col]), None)
        if pivot is None:
            continue
        a[pivot_row], a[pivot] = a[pivot], a[pivot_row]
        inv = pow(a[pivot_row][col], -1, q)
        a[pivot_row] = [(v * inv) % q for v in a[pivot_row]]
        for i in range(nrows):
            if i != pivot_row and a[i][col]:
                c = a[i][col]
                a[i] = [(x - c*y) % q for x, y in zip(a[i], a[pivot_row])]
        pivot_row += 1
        if pivot_row == nrows:
            break
    return pivot_row


def span_rank(cols, q):
    if not cols:
        return 0
    return rank(list(map(list, zip(*cols))), q)


def nullspace(rows, dim, q):
    if not rows:
        return [tuple(int(i == j) for i in range(dim)) for j in range(dim)]
    a = [[v % q for v in row] for row in rows]
    i, pivots = 0, []
    for j in range(dim):
        k = next((h for h in range(i, len(a)) if a[h][j]), None)
        if k is None:
            continue
        a[i], a[k] = a[k], a[i]
        inv = pow(a[i][j], -1, q)
        a[i] = [v * inv % q for v in a[i]]
        for h in range(len(a)):
            if h != i and a[h][j]:
                coef = a[h][j]
                a[h] = [(x - coef*y) % q for x, y in zip(a[h], a[i])]
        pivots.append(j)
        i += 1
        if i == len(a):
            break
    out = []
    for j in range(dim):
        if j in pivots:
            continue
        v = [0] * dim
        v[j] = 1
        for h, p in enumerate(pivots):
            v[p] = (-a[h][j]) % q
        out.append(tuple(v))
    return out


def matmul(a, b, q):
    if not a:
        return []
    if not b:
        return [[0]*0 for _ in a]
    return [[sum(x*y for x, y in zip(row, col)) % q for col in zip(*b)] for row in a]


def examine(m, n, q, xflat, yflat):
    X = [list(xflat[i*n:(i+1)*n]) for i in range(m)]
    Y = [list(yflat[i*m:(i+1)*m]) for i in range(n)]
    r, s = rank(X, q), rank(Y, q)
    t = rank(matmul(Y, X, q), q)
    d = r+s-t
    assert 0 <= d <= min(m, 2*n), (m,n,q,r,s,t)
    image = []
    for j in range(n):
        col = tuple(X[i][j] for i in range(m))
        if span_rank(image+[col], q) > len(image):
            image.append(col)
    assert len(image) == r
    kernel = nullspace(Y, m, q)
    assert len(kernel) == m-s
    U = []
    for v in kernel:
        if span_rank(image+U+[v], q) > len(image)+len(U):
            U.append(v)
    assert len(U) == m-d
    V0 = image[:]
    for j in range(m):
        e = tuple(int(i == j) for i in range(m))
        if span_rank(V0+U+[e], q) > len(V0)+len(U):
            V0.append(e)
    assert len(V0) == d and span_rank(V0+U, q) == m
    assert all(all(sum(Y[i][j]*u[j] for j in range(m)) % q == 0 for i in range(n)) for u in U)
    # In the selected active core V0, every vector in ker(Y) belongs to im(X).
    assert len(nullspace([[sum(Y[i][j]*v[j] for j in range(m)) % q for v in V0] for i in range(n)], d, q)) == r-t
    return d


def test_exhaustive(q,n,m):
    states = 0
    hist = [0]*(min(m,2*n)+1)
    for bits in itertools.product(range(q),repeat=2*m*n):
        d = examine(m,n,q,bits[:m*n],bits[m*n:])
        hist[d] += 1
        states += 1
    assert states == q**(2*m*n)
    return {"q":q,"n":n,"m":m,"states":states,"core_dimension_counts":hist}


def test_sharpness(q,n):
    for d in range(1, 2*n+1):
        r = min(n,d)
        s = d-r
        # Construct an X of rank r, with image in first r columns of V,
        # and Y supported on last s coordinates. Then YX=0.
        X = [[int(i == j) for j in range(n)] for i in range(d)]
        Y = [[int(j==r+i) if i < s else 0 for j in range(d)] for i in range(n)]
        assert examine(d,n,q,tuple(v for row in X for v in row),tuple(v for row in Y for v in row)) == d
    return 2*n


def test_sample(q,n,m,samples,seed):
    rng = random.Random(seed)
    hist = [0]*(min(m,2*n)+1)
    for _ in range(samples):
        x = tuple(rng.randrange(q) for i in range(m*n))
        y = tuple(rng.randrange(q) for i in range(m*n))
        d=examine(m,n,q,x,y)
        hist[d]+=1
        assert d <= 2*n
    return {"q":q,"n":n,"m":m,"samples":samples,"seed":seed,"core_dimension_counts":hist}



def invert_square(a, q):
    n = len(a)
    t = [list(row)+[int(i==j) for j in range(n)] for i,row in enumerate(a)]
    for c in range(n):
        k = next((j for j in range(c,n) if t[j][c] % q),None)
        if k is None:
            return None
        t[c],t[k]=t[k],t[c]
        inv=pow(t[c][c],-1,q)
        t[c]=[(x*inv)%q for x in t[c]]
        for j in range(n):
            if j!=c and t[j][c]:
                v=t[j][c]
                t[j]=[(x-v*y)%q for x,y in zip(t[j],t[c])]
    return [row[n:] for row in t]


def complete_triple_orbit_test(q,n,m,expected):
    assert n<=2 and q<=3
    points=list(itertools.product(range(q),repeat=n))
    point_index={v:i for i,v in enumerate(points)}
    group=[]
    for data in itertools.product(range(q), repeat=n*n):
        h=[list(data[i*n:(i+1)*n]) for i in range(n)]
        hi=invert_square(h,q)
        if hi is not None:
            group.append((h,hi))
    def matvec(a,v):
        return tuple(sum(x*y for x,y in zip(row,v))%q for row in a)
    def mask_of(vectors):
        return sum(1<<point_index[v] for v in vectors)
    def all_span(columns):
        return {tuple(sum(coef*col[i] for coef,col in zip(coeffs,columns))%q for i in range(n))
                for coeffs in itertools.product(range(q),repeat=len(columns))}
    seen_keys=set()
    canon_cache={}
    class_hist={}
    for data in itertools.product(range(q),repeat=2*m*n):
        xx=data[:m*n]
        yy=data[m*n:]
        X=[list(xx[i*n:(i+1)*n]) for i in range(m)]
        Y=[list(yy[i*m:(i+1)*m]) for i in range(n)]
        T=matmul(Y,X,q)
        S={v for v in points if all(x==0 for x in matvec(X,v))}
        D=all_span([tuple(Y[i][j] for i in range(n)) for j in range(m)])
        raw=(mask_of(S),mask_of(D),tuple(v for row in T for v in row))
        if raw in canon_cache:
            key=canon_cache[raw]
        else:
            options=[]
            for h,hi in group:
                hs=mask_of({matvec(h,v) for v in S})
                hd=mask_of({matvec(h,v) for v in D})
                transformed=matmul(matmul(h,T,q),hi,q)
                options.append((hs,hd,tuple(v for row in transformed for v in row)))
            key=min(options)
            canon_cache[raw]=key
        seen_keys.add(key)
        d=rank(X,q)+rank(Y,q)-rank(T,q)
        if key in class_hist:
            assert class_hist[key]==d
        else:
            class_hist[key]=d
    got=len(seen_keys)
    assert got==expected, (q,n,m,got,expected)
    return {"q":q,"n":n,"m":m,"states":q**(2*m*n),"orbits_from_triple":got,
            "expected_earlier_group_orbit_result":expected,
            "orbits_by_core_dim":{str(d):sum(v==d for v in class_hist.values()) for d in range(min(m,2*n)+1)}}



def exhaustive_binary_three_axis_triples():
    """All GL_3(F_2)-orbits of (S,D,T), using actual 3x3 maps.

    Unlike an infeasible q^(2*m*n) enumeration at m=6,n=3, this enumerates
    every admissible stable triple exactly once and acts by all 168 bases.
    """
    n=3
    maps=[]
    group=[]
    for cols in itertools.product(range(8),repeat=3):
        vmap=tuple((cols[0] if v&1 else 0) ^ (cols[1] if v&2 else 0) ^ (cols[2] if v&4 else 0) for v in range(8))
        maps.append((cols,vmap))
        if len(set(vmap))==8:
            invmap=tuple(vmap.index(v) for v in range(8))
            group.append((vmap,invmap))
    assert len(group)==168 and len(maps)==512
    subspaces=[]
    for mask in range(256):
        if not (mask&1):
            continue
        vec=[v for v in range(8) if (mask>>v)&1]
        if all(((mask>>(u^v))&1) for u in vec for v in vec):
            dim=(len(vec).bit_length()-1)
            assert 2**dim==len(vec)
            subspaces.append((mask,dim))
    assert len(subspaces)==16
    triples=[]
    for smask,sdim in subspaces:
        S=[v for v in range(8) if (smask>>v)&1]
        for dmask,ddim in subspaces:
            for cols,vmap in maps:
                if any(vmap[v] for v in S):
                    continue
                if any(not ((dmask>>vmap[e])&1) for e in (1,2,4)):
                    continue
                image_size=len(set(vmap))
                t_rank=image_size.bit_length()-1
                core=n-sdim+ddim-t_rank
                assert 0<=core<=6
                triples.append(((smask,dmask,cols),core))
    assert len(triples)==2825
    orbits={}
    burnside_fixed=0
    maps_by_group=[]
    for vmap,invmap in group:
        masks={mask:sum(1<<vmap[v] for v in range(8) if (mask>>v)&1)
               for mask,_ in subspaces}
        maps_by_group.append((vmap,invmap,masks))
    for key,core in triples:
        smask,dmask,cols=key
        canonical=None
        orig=maps[cols[0]*64+cols[1]*8+cols[2]][1]
        for vmap,invmap,maskmap in maps_by_group:
            outcols=tuple(vmap[orig[invmap[e]]] for e in (1,2,4))
            new_key=(maskmap[smask],maskmap[dmask],outcols)
            if new_key==key:
                burnside_fixed+=1
            if canonical is None or new_key<canonical:
                canonical=new_key
        if canonical in orbits:
            assert orbits[canonical]==core
        else:
            orbits[canonical]=core
    assert burnside_fixed%len(group)==0
    assert burnside_fixed//len(group)==len(orbits)
    counts=[sum(v==d for v in orbits.values()) for d in range(7)]
    assert counts[:3]==[1,4,15]
    assert all(v>0 for v in counts)
    return {"field":"F_2","n":3,"triple_states":len(triples),
            "full_group_order":len(group),"orbits_by_minimal_core_dim":counts,
            "stabilized_orbit_count_m_ge_6":len(orbits),
            "burnside_sum_fixed":burnside_fixed,
            "N_m_sequence_m_0_to_7":[sum(counts[:min(m,6)+1]) for m in range(8)]}


def main():
    full=[]
    for q,n,ms in [(2,1,(0,1,2,3)),(2,2,(0,1,2,3,4)),(3,1,(0,1,2)),(3,2,(0,1,2))]:
        for m in ms:
            full.append(test_exhaustive(q,n,m))
    samples=[]
    for q,n,m,count in [(2,3,6,300),(3,3,7,300),(5,4,9,200),(373,3,7,100)]:
        samples.append(test_sample(q,n,m,count,seed=20261028+n*17+m*13+q))
    triple=[]
    for q,n,m,expected in [(2,1,0,1),(2,1,1,4),(2,1,2,5),
                           (2,2,0,1),(2,2,1,5),(2,2,2,16),(2,2,3,20),(2,2,4,21),
                           (3,2,0,1),(3,2,1,6),(3,2,2,24)]:
        triple.append(complete_triple_orbit_test(q,n,m,expected))
    three=exhaustive_binary_three_axis_triples()
    sharp = [{"q":q,"n":n,"max_core":test_sharpness(q,n)} for q in (2,3,373) for n in range(1,5)]
    result={"schema":"D25_TWO_CYCLE_CORE_STABILIZATION_AUTHOR_CHECK_V1","status":"PASS","scope":"finite exact prime-field checks, not universal proof", "exhaustive":full,"exhaustive_total_states":sum(x["states"] for x in full),"binary_n3_stable_triple_orbits":three,"triple_orbit_tests":triple,"triple_orbit_total_states":sum(x["states"] for x in triple),"sampled":samples,"sampled_total":sum(x["samples"] for x in samples),"sharpness_examples":sharp}
    filename=Path(__file__).with_name('d25_two_cycle_core_stabilization_author_check_20261028.json')
    filename.write_text(json.dumps(result,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
    print(json.dumps({"status":result["status"],"exhaustive_total_states":result["exhaustive_total_states"],"sampled_total":result["sampled_total"],"cases_exhaustive":len(full),"sharpness_instances":len(sharp),"triple_orbit_cases":len(triple),"binary_n3_stable_orbits":three["stabilized_orbit_count_m_ge_6"]},ensure_ascii=False))


if __name__ == '__main__':
    main()
