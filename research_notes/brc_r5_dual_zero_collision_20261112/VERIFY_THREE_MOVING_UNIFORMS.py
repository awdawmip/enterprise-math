#!/usr/bin/env python3
"""Exact endpoint proof checker for the three uniform moving words.

Runs the sibling standalone frozen-fixture dual-zero census first, to reuse
its complete local 28-coordinate setup without network or mutable imports.
"""
from pathlib import Path
from runpy import run_path
f = run_path(str(Path(__file__).with_name("VERIFY_DUAL_ZERO_COLLISIONS.py")))
Q,X,P,H,x,k0,k1,L,U,E,V = (f[k] for k in
    ("Q","X","P","H","x","k0","k1","L","U","E","V"))
assert U==Q(1,23)
WORD = {15:(6,1), 12:(1,), 3:(6,)}
GATE_MARGIN = {
    15:Q(13289444035517,14507005871120000000),
    12:Q(10649520956717,14507005871120000000),
    3:Q(2729751720317,14507005871120000000)
}
for q,word in WORD.items():
    gate=(1-q*E/x)/23
    assert L<gate<U
    for r in (gate,U):
        eps=x*(1-23*r)/q
        assert eps==(E if r==gate else 0)
        mask=0
        for atom in (0,)+word:
            if atom:
                mask|=1<<(atom-1)
            state=tuple(X[k]+r*x*H[k]+eps*P[mask][k]/36
                        for k in range(28))
            assert all(z>=0 for z in state)
            if r==U:
                assert [V[k] for k,z in enumerate(state) if z==0]==[(1,3)]
            if atom==word[-1] and r==gate:
                assert [V[k] for k,z in enumerate(state) if z==0]==[(1,3)]
                assert min(z for z in state if z>0)==GATE_MARGIN[q]
        if r==gate:
            assert P[mask][k1]==-36*q
            assert X[k1]+r*x*H[k1]+eps*P[mask][k1]/36==0
    print("UNIFORM_MOVING",q,"GATE",gate,"WORD",word,
          "MIN_POSITIVE_GATE_MARGIN",GATE_MARGIN[q],
          "AT_GATE_AND_U_ALL_PREFIXES_LEGAL",True)
print("PASS_R5_THREE_UNIFORM_MOVING_FIRST_ZERO_WORDS")
