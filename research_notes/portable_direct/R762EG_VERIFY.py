#!/usr/bin/env python3
"""R762EG exact mod-3 coset-span checks; --smith uses SymPy for exact q=3 SNF."""
from collections import defaultdict
from itertools import product
import json
import sys


def forms(g, q):
    x, y, z = g
    return (x, y, z, (x-y+z) % q)


def f3_coset_rank(q):
    """Span of the 4q indicator functions 1_{ell_j=t} over F_3."""
    assert q >= 3 and q % 3 == 0
    pts = list(product(range(q), repeat=3))
    cosets = [[{} for _ in range(q)] for _ in range(4)]
    for i, g in enumerate(pts):
        ls = forms(g, q)
        for j in range(4):
            cosets[j][ls[j]][i] = 1
    pivots = {}
    for family in cosets:
        for column in family:
            w = dict(column)
            while w:
                k = min(w)
                if k not in pivots:
                    inv = 1 if w[k] == 1 else 2
                    pivots[k] = {i: (v*inv)%3 for i,v in w.items()}
                    break
                fac = w[k]
                for i,v in pivots[k].items():
                    u = (w.get(i,0)-fac*v)%3
                    if u: w[i]=u
                    else: w.pop(i,None)
    return len(pivots)


def q3_smith():
    """Independent integral group-ring check using exact HNF and SNF."""
    from sympy import Matrix, ZZ
    from sympy.matrices.normalforms import hermite_normal_form, smith_normal_form
    q=3
    G=list(product(range(q),repeat=3))
    indices={g:i for i,g in enumerate(G)}
    generators=[]
    for family in 'ABCD':
        d=defaultdict(int)
        for r in range(q):
            for s in range(q):
                if family == 'A': v=(0,r+s,-s)
                elif family == 'B': v=(r+s,0,s)
                elif family == 'C': v=(r+s,-s,0)
                else: v=(r+2*s,r+s,-s)
                d[tuple(t%q for t in v)] += (2 if r%3==0 else -1)
        generators.append(d)
    columns=[]
    for f in generators:
        for shift in G:
            col=[0]*len(G)
            for v,c in f.items():
                w=tuple((v[i]+shift[i])%q for i in range(3))
                col[indices[w]]+=c
            columns.append(Matrix(col))
    M=Matrix.hstack(*columns)
    H=hermite_normal_form(M)
    S=smith_normal_form(H,domain=ZZ)
    diag=[abs(int(S[i,i])) for i in range(min(S.shape)) if S[i,i]]
    assert H.shape==(27,12)
    assert diag == [1]*8+[3]*4
    return {'image_basis_shape':[27,12],'smith_diagonal':diag,
            'quotient_group':'(Z/3Z)^4','quotient_order':81}


def main():
    cases=[]
    for q in (3,9,27):
        rank=f3_coset_rank(q)
        assert rank == 4*q-4
        cases.append({'Q':q,'families':4,'coset_indicators':4*q,
                      'rank_mod3_I':rank,'rank_Q_K_from_R762ED':8*q-12,
                      'quotient_3_rank':4*q-8})
    data={'schema':'R762EG_NULL_LATTICE_THREE_RANK_EVIDENCE_V1',
          'method':'exact sparse finite-field elimination; optional integer SNF',
          'scope':'all-q symbolic proof; author finite q=3,9,27 checks',
          'status':'PASS','cases':cases}
    if '--smith' in sys.argv: data['q3_smith']=q3_smith()
    print(json.dumps(data,indent=2,sort_keys=True)+'\n',end='')


if __name__ == '__main__':
    main()
