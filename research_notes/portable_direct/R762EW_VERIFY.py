#!/usr/bin/env python3
"""R762EW: exact finite-group-ring verification; six named positive BRC shifts."""
import json
from math import comb
from pathlib import Path
import numpy as np

BRANCHES = ((0,0,0),(1,0,0),(0,0,1),(1,1,0),(0,1,1),(1,1,1))

def apply_shifts(v, terms, modulus=27):
    out = np.zeros_like(v)
    for (x,y,z), coefficient in terms:
        out += coefficient * np.roll(v, (x,y,z), axis=(0,1,2))
    return out % modulus

def main():
    q, Q, N = 9, 27, 26
    pterms = tuple((step,1) for step in BRANCHES)
    aterms = tuple((tuple(3*t for t in step),1) for step in BRANCHES)
    zero = np.zeros((Q,Q,Q),dtype=np.int64)
    ident = zero.copy()
    ident[0,0,0] = 1

    # Compute P^3 before reduction, with all named path multiplicities.
    p3 = ident.copy()
    for _ in range(3):
        accum = np.zeros_like(p3)
        for step in BRANCHES:
            accum += np.roll(p3,step,axis=(0,1,2))
        p3 = accum
    aa = np.zeros_like(p3)
    for step in BRANCHES:
        aa[tuple(3*t for t in step)] += 1
    diff = p3-aa
    assert (diff%3==0).all()
    D = diff//3
    assert np.all(D>=0) and int(D.sum())==70 and int(D[1,0,0])==1
    dsupp = [(tuple(map(int,row)),int(D[tuple(row)])) for row in np.argwhere(D)]
    assert len(dsupp)==38

    # D^2 is an exact integer convolution, then reduced modulo 27.
    D2 = apply_shifts(D,dsupp,modulus=27)
    assert int(D2[2,0,0])==1

    p=[ident]
    for _ in range(N):
        p.append(apply_shifts(p[-1],pterms))
    a=[ident]
    for _ in range(q):
        a.append(apply_shifts(a[-1],aterms))
    ad=[D%27]
    ad2=[D2]
    for _ in range(q):
        ad.append(apply_shifts(ad[-1],aterms))
        ad2.append(apply_shifts(ad2[-1],aterms))

    checks=0
    first_order_iff=[]
    witness=[]
    for m in range(q):
        corrected=a[m].copy()
        first=corrected.copy()
        if m>=1:
            first=(first+3*m*ad[m-1])%27
            corrected=first.copy()
        if m>=2:
            corrected=(corrected+9*comb(m,2)*ad2[m-2])%27
        for r in range(3):
            t=corrected.copy()
            for _ in range(r):
                t=apply_shifts(t,pterms)
            assert np.array_equal(t,p[3*m+r]),(m,r)
            checks+=Q**3
        valid=bool(np.array_equal(first,p[3*m]))
        assert valid==(m%3!=2)
        first_order_iff.append({'m':m,'first_order_valid':valid,'predicted':m%3!=2})
        if 1<=m<q:
            assert int(p[3*m][2,0,0])==comb(3*m,2)%27
            first_x2=int(first[2,0,0])
            exact_x2=int(p[3*m][2,0,0])
            assert first_x2==(3*m)%27
            assert (exact_x2-first_x2)%27==9*comb(m,2)%27
            witness.append({'m':m,'exact_X2_mod27':exact_x2,
                            'first_order_X2_mod27':first_x2,
                            'difference_mod27':(exact_x2-first_x2)%27})

    # A second modulus checks m=9, v_3(9)+1=3, at Q=81.
    Q2,M2=81,81
    z=np.zeros((Q2,Q2,Q2),dtype=np.int64)
    e=z.copy()
    e[0,0,0]=1
    pw=e.copy()
    aw=e.copy()
    high=[]
    for m in range(1,10):
        for _ in range(3):
            pw=apply_shifts(pw,pterms,M2)
        aw=apply_shifts(aw,aterms,M2)
        d=(pw-aw)%M2
        expected=1
        k=m
        while k%3==0:
            expected*=3
            k//=3
        assert np.all(d%(3*expected)==0)
        assert int(d[1,0,0])==(3*m)%M2
        if 9*expected<=M2:
            assert (d%(9*expected)!=0).any()
        high.append({'m':m,'expected_v3':(1 if m%3 else (2 if m%9 else 3)),
                     'X_witness_mod81':int(d[1,0,0])})

    result={
        'result_id':'R762EW','date':'2026-11-18',
        'module':'numpy integer exact finite group ring',
        'q':q,'Q':Q,'terminal_positions':Q**3,
        'named_branches':list(map(list,BRANCHES)),
        'D_augmentation':int(D.sum()),'D_support_cells':len(dsupp),
        'D2_support_cells_mod27':int(np.count_nonzero(D2)),
        'P3_equals_A_plus_3D':True,'modulus':27,
        'm_domain':[0,8],'r_domain':[0,1,2],
        'full_vector_equalities':27,'terminal_coefficient_comparisons':checks,
        'first_order_if_and_only_if':first_order_iff,
        'X2_witnesses':witness,'q27_Q81_mod81_all_m_1_9':high,
        'author_side_result':'PASS','review':'NOT_REVIEWED',
        'general_theorem':'PROVED_SYMBOLICALLY;FINITE_CHECK_IS_IMPLEMENTATION_CROSSCHECK'
    }
    path=Path(__file__).with_name('R762EW_EVIDENCE.json')
    with path.open('w',encoding='utf-8') as f:
        json.dump(result,f,ensure_ascii=False,indent=2)
    print(json.dumps({'result_id':result['result_id'],
                      'full_vector_equalities':27,
                      'terminal_coefficient_comparisons':checks,
                      'q27_m9_X_witness_mod81':high[-1]['X_witness_mod81'],
                      'author_side_result':'PASS'},indent=2))

if __name__=='__main__':
    main()
