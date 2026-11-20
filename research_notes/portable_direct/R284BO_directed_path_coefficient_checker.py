#!/usr/bin/env python3
"""Exact verification for directed-path coefficient extraction and injective signatures.
Reuses R284BM exact polynomial dictionary implementation.
"""
from itertools import product
from random import Random
import json
from R284BM_connected_port_graph_checker import polynomial


def coeff(P,n,edge_count,vertices,edge_positions):
    exp=[0]*(n+edge_count)
    for i in range(n):
        if i not in vertices:exp[i]=1
    for k in edge_positions:exp[n+k]=1
    return P.get(tuple(exp),0)


def run():
    rng=Random(28420261120)
    cases={}
    # n=2,3: whole bounded population at H=2; larger n: seeded, exact polynomial.
    for n in (2,3,4,5):
        E=tuple((i,i+1) for i in range(n-1))
        inputs=list(product((1,2),repeat=n*n)) if n<=3 else [tuple(rng.randint(1,4) for _ in range(n*n)) for _ in range(72 if n==4 else 12)]
        path_checks=0
        for flat in inputs:
            C=[flat[i*n:(i+1)*n] for i in range(n)]
            P=polynomial(C,E)
            for i in range(n):
                for j in range(i+1,n):
                    val=coeff(P,n,n-1,set(range(i,j+1)),range(i,j))
                    assert val == -C[j][i],(n,i,j,flat,val)
                    path_checks+=1
        cases[str(n)]={'matrices_tested':len(inputs),'path_coefficients_checked':path_checks,'all_match':True}
    n=4;seen=set()
    for flat in product((1,2),repeat=n*n):
        C=[flat[i*n:(i+1)*n] for i in range(n)]
        signature=tuple(C[i][i] for i in range(n)) + tuple(C[j][i] for i in range(n) for j in range(i+1,n)) + tuple(C[i][j]*C[j][i] for i in range(n) for j in range(i+1,n))
        assert signature not in seen
        seen.add(signature)
    assert len(seen)==65536
    return {'coefficient_checks':cases,
            'n4_H2_recovery_signatures':len(seen),
            'exact_arithmetic':'integer polynomial coefficients / integer product signatures',
            'status':'PASS',
            'scope':'Path monomial identity checked exhaustively for n=2,3 H=2 and on declared seeded n=4,5 samples; n=4 H=2 all recovery signatures checked'}

if __name__ == '__main__':
    print(json.dumps(run(),indent=2,sort_keys=True))
