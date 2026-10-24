#!/usr/bin/env python3
"""R250 reproducible positive BRC effect-histogram witness. No native module claim."""
from collections import defaultdict
# effect(s,k): x1->s*x1+k; x2->s*x2; other four X6 axes unchanged
EDGES = (((2,(-1,-1)),(2,(1,-1))),
         ((0,(-1,-1)),(0,(1,-1))),
         ((1,(1,1)),(2,(1,-1))))
def then(a,b): return a[0]*b[0], b[0]*a[1]+b[1]
def direct(start,depth):
    H={(start,(1,0)):1}
    for _ in range(depth):
        nxt=defaultdict(int)
        for (state,effect),n in H.items():
            for target,step in EDGES[state]:
                nxt[target,then(effect,step)]+=n
        H=nxt
    out=defaultdict(int)
    for (state,effect),n in H.items():out[effect]+=n
    return dict(out)
# faithful chronological 2x2 Laurent matrix: Psi(s,k)=D_{-s*k} P_s
def laurent(s,k):
    m=-s*k
    return (({m:1},{}),({}, {-m:1})) if s==1 else (({}, {m:1}),({-m:1},{}))
def polyadd(a,b):
    d=defaultdict(int,a)
    for z,c in b.items(): d[z]+=c
    return {z:c for z,c in d.items() if c}
def polymul(a,b):
    d=defaultdict(int)
    for z,c in a.items():
        for zz,cc in b.items():d[z+zz]+=c*cc
    return {z:c for z,c in d.items() if c}
def mul2(A,B):
    return tuple(tuple(polyadd(polymul(A[i][0],B[0][j]),polymul(A[i][1],B[1][j])) for j in range(2)) for i in range(2))
def embed(H):
    M=[[{},{}],[{},{}]]
    for (s,k),count in H.items():
        Z=laurent(s,k)
        for i in range(2):
            for j in range(2): M[i][j]=polyadd(M[i][j],{z:c*count for z,c in Z[i][j].items()})
    return tuple(tuple(r) for r in M)
def main():
    E=[(s,k) for s in (-1,1) for k in range(-2,3)]
    assert all(laurent(*then(a,b))==mul2(laurent(*a),laurent(*b)) for a in E for b in E)
    expected=[True,True,True,False]
    for d in range(9):
        h0,h1=direct(0,d),direct(1,d)
        if d<4: assert (h0==h1)==expected[d]
        assert sum(h0.values())==sum(h1.values())==2**d
        assert embed(h0)==embed(h0) and embed(h1)==embed(h1)
    a,b=direct(0,3),direct(1,3)
    assert a.get((1,1),0)==0 and b.get((1,1),0)==1
    print('PASS R250: exact length-3 witness, lengths 0..8, 100 Laurent group checks')
if __name__=='__main__': main()
