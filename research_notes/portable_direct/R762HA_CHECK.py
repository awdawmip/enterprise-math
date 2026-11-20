#!/usr/bin/env python3
"""Exact parity-support BRC verifier for frozen-X6 auxiliary K4-STAR Port candidate.

Positive endpoint-word multiplicities only; sign refinements are counted in the
separate terminal observer. The code uses integer arithmetic throughout.
"""
from itertools import product
import json


def mmul(X, Y):
    return [[sum(X[i][k]*Y[k][j] for k in range(2)) for j in range(2)] for i in range(2)]


def parity_transfer(signs):
    a,b,c,d=signs
    A=((a,b),(c,d))
    B=((a,c),(d,b))
    C=((a,d),(b,c))
    return mmul(mmul(A,B),C)


def parity_fourier(k):
    """Number of length-3k endpoint words returning Port 01, all vertex degrees even."""
    total=0
    for signs in product((1,-1),repeat=4):
        T=parity_transfer(signs)
        V=[[1,0],[0,1]]
        for _ in range(k):
            V=mmul(V,T)
        total+=V[0][0]
    assert total % 16 == 0
    return total // 16


def parity_dp(k):
    """Independent exact positive BRC parity-state automaton, 3k events."""
    # For the 3 matching-phase layers, rows/columns correspond to named Ports.
    # The source vertex on each transition is encoded by its bit number.
    layers=[((0,1),(2,3)),((0,2),(3,1)),((0,3),(1,2))]
    states={(0,0):1}
    for step in range(3*k):
        layer=layers[step%3]
        nxt={}
        for (port,mask),weight in states.items():
            for next_port,vertex in enumerate(layer[port]):
                key=(next_port,mask^(1<<vertex))
                nxt[key]=nxt.get(key,0)+weight
        states=nxt
    return states.get((0,0),0)


def formula(k):
    if k==0:
        return 1
    if k%2:
        return 0
    n=k//2
    return 2**(6*n-4)+2**(3*n-1)


def classification():
    out={'all_same':0,'two_two':0,'one_three':0}
    for e in product((1,-1),repeat=4):
        m=parity_transfer(e)
        plus=e.count(1)
        if plus in (0,4):
            out['all_same']+=1
            sign=e[0]
            assert m==[[4*sign,4*sign],[4*sign,4*sign]]
        elif plus==2:
            out['two_two']+=1
            assert m==[[0,0],[0,0]]
        else:
            out['one_three']+=1
            assert mmul(m,m)==[[8,0],[0,8]]
            assert abs(m[0][0])==2
    assert out=={'all_same':2,'two_two':6,'one_three':8}
    return out


def run():
    groups=classification()
    rows=[]
    for k in range(17):
        got1=parity_fourier(k)
        got2=parity_dp(k)
        want=formula(k)
        assert got1==got2==want,(k,got1,got2,want)
        m=3*k
        port_words=1 if k==0 else 2**(m-1)
        rows.append({'events':m,'three_blocks':k,'parity_compatible_port_return_endpoint_words':want,'total_port_return_endpoint_words':port_words})
    evidence={'research_id':'R762HA','model':'K4_STAR_SIGNED_PORT_CHIRALITY_PLUS_CANDIDATE','observation':'endpoint-word exists some signed refinement with full X6 Cell and Port return','classifications':groups,'verification':'PASS','method':'exact 16-character Fourier + independent positive parity DP','checked_three_blocks':list(range(17)),'rows':rows,'independent_review':'NOT_REVIEWED','native_tri_closure_permission':'OPEN'}
    print(json.dumps(evidence,ensure_ascii=False,indent=2))


if __name__=='__main__':
    run()
