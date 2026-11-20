#!/usr/bin/env python3
"""R284BM: symbolic exact checker for disconnected editable-Port graphs.
No external dependencies. Uses the Leibniz determinant in Z[d_*,z_*].
"""
from itertools import combinations, product, permutations
from collections import Counter
import json


def polynomial(C, edges):
    n = len(C)
    edge_index = {edge: n + k for k, edge in enumerate(edges)}
    m = n + len(edges)
    zero = (0,) * m
    out = Counter()
    for perm in permutations(range(n)):
        parity = (-1) ** sum(perm[i] > perm[j] for i in range(n) for j in range(i+1, n))
        terms = {zero: parity}
        for i,j in enumerate(perm):
            opts = [(zero, -C[i][j])]
            if i == j:
                v = list(zero); v[i] = 1
                opts.append((tuple(v), 1))
            if (i,j) in edge_index:
                v = list(zero); v[edge_index[(i,j)]] = 1
                opts.append((tuple(v), -1))
            nxt = Counter()
            for a, coefficient in terms.items():
                for b, value in opts:
                    nxt[tuple(x+y for x,y in zip(a,b))] += coefficient*value
            terms = {key: val for key,val in nxt.items() if val}
        out.update(terms)
    return {key: value for key, value in out.items() if value}


def witnesses(n, edges):
    # Component partition in the undirected support of editable edges.
    parent = list(range(n))
    def root(x):
        while x != parent[x]:
            x = parent[x]
        return x
    for a,b in edges:
        a=root(a); b=root(b)
        parent[a]=b
    first=root(0)
    group = [root(i)==first for i in range(n)]
    assert not all(group)  # disconnected
    C = [[1 if group[i]==group[j] or group[i] else 2 for j in range(n)] for i in range(n)]
    Cp = [[1 if group[i]==group[j] or group[j] else 2 for j in range(n)] for i in range(n)]
    assert C != Cp
    return C,Cp


def full_star_uniqueness(n, H):
    edges = tuple((0,j) for j in range(1,n))
    signatures=set()
    for flat in product(range(1,H+1),repeat=n*n):
        C=[flat[i*n:(i+1)*n] for i in range(n)]
        signature=tuple(sorted(polynomial(C,edges).items()))
        if signature in signatures:
            return False,len(signatures)
        signatures.add(signature)
    return True,len(signatures)


def run():
    counts={}
    for n in (2,3,4):
        all_edges=[(i,j) for i in range(n) for j in range(n) if i!=j]
        tested=0
        for k in range(n-1):
            for edges in combinations(all_edges,k):
                C,Cp=witnesses(n,edges)
                assert polynomial(C,edges)==polynomial(Cp,edges), (n,edges)
                tested+=1
        counts[str(n)]=tested
    for n in (2,3):
        good,num=full_star_uniqueness(n,2)
        assert good
        counts[f'full_star_n{n}_H2']=num
    return {'graph_families_symbolically_checked':counts,
            'arithmetic':'exact integer polynomial coefficients',
            'claims':'all directed port subsets of size < n-1 for n=2,3,4; all matrices for full star n=2,3 and H=2',
            'status':'PASS'}

if __name__ == '__main__':
    print(json.dumps(run(),indent=2,sort_keys=True))
