#!/usr/bin/env python3
"""C292 exact author certificate: full-box strong convexity and chart concavity.
Run beside frozen C275/C284/C288/C290 and C291_HESSIAN_EXACT.py from C291.
No native GF(2)-BRC/X6 transfer or Source/Driver acceptance is claimed.
"""
from fractions import Fraction as F
import C291_HESSIAN_EXACT as c

C=((3300,8,8,10),(8,1000,40,30),(8,40,850,310),(10,30,310,920))
D=(2700,700,670,770)
G=tuple(D[i]-sum(C[i][j] for j in range(4) if j!=i) for i in range(4))
assert G==(2674,622,312,420)
assert max(map(sum,C))==3326
A=((F(1),F(0),F(0),F(0)),
   (F(0),F(1),F(0),F(0)),
   (F(5,2),F(5,3),F(4,3),F(5,6)),
   (F(0),F(0),F(1),F(0)))
K=tuple(tuple(F(5,6)*sum(A[a][i]*C[a][b]*A[b][j]
                           for a in range(4) for b in range(4))
              for j in range(4)) for i in range(4))
assert max(max(r) for r in K)==F(86525,12)
assert max(sum(r) for r in K)==F(44305,3)
assert F(312)/(F(21,10)*F(2297,100))>6

def verify():
    paths,_=c.c.c288.build_paths()
    W,_=c.c.s.floor_fixed_masses()
    assert len(paths)==125
    for i,p in enumerate(paths):
        B=tuple((lo-c.c.PAD,hi+c.c.PAD) for lo,hi in p['box'])
        H,rho=c.Hessian_interval(B,W)
        assert rho<F(1,1000)
        for a in range(4):
            assert H[a][a][0]>D[a]
            assert H[a][a][0]-sum(max(map(abs,H[a][b])) for b in range(4) if b!=a)>312
            for b in range(4):
                lo,hi=H[a][b]
                assert -C[a][b]<lo<=hi<C[a][b]
        if (i+1)%25==0: print('VERIFIED',i+1,'/',len(paths),flush=True)
    print('C292_AUTHOR_EXACT_PASS: 125 continuous 4D boxes, H_(F/Q) > 312 I,')
    print('H_(F/Q) operator norm < 3326; H_Phi < -6 I on C290 parameter rectangles')
    print('chart Hessian max entry <',F(86525,12),'; chart gradient Lipschitz <',F(44305,3))
if __name__=='__main__':verify()
