#!/usr/bin/env python3
"""Independent exact n=3 grid and bilinear continuum certificate.
Source kernel: S23 author's KERNEL.json, blob 564acd9574876059c505fd8a40d14f2f6e0e3736.
No floating point is used in assertions or certificate construction.
"""
from fractions import Fraction as Q
from itertools import product

M = 1_000_000
ROWS = [
    {13:1000000},
    {1:479665,12:520335},
    {9:296273,10:703727},
    {2:419643,15:48185,18:405725,21:112202,26:14245},
    {1:139862,4:683322,9:176816},
    {6:230562,9:106277,11:120245,12:56752,14:50073,15:71369,16:50073,17:25415,19:120245,22:50462,23:25415,24:70684,25:22428},
    {1:20822,3:400945,4:11265,5:119554,6:192951,7:125268,8:65023,20:64172},
    {0:747749,1:99382,3:52308,4:2315,6:2609,9:87375,10:3741,18:4521},
]
assert len(ROWS)==8 and all(sum(r.values())==M and all(0<=j<27 for j in r) for r in ROWS)
# Input y in lex order, Y=0 N=1. Group by the count of Y.
G = [[0]*4 for _ in range(27)]
for y,row in zip(product(range(2),repeat=3),ROWS):
    h=y.count(0)
    for x,v in row.items():
        G[x][h]+=v
assert [sum(G[x][h] for x in range(27)) for h in range(4)]==[M,3*M,3*M,M]
EXPS = [tuple(x.count(t) for t in range(3)) for x in product(range(3),repeat=3)]

def grid_max(N):
    D=8*N; den=2*M*D**6
    best=-1; bestij=None
    for i in range(N+1):
        A=4*N+3*i
        for j in range(N+1):
            C=4*N+3*j
            d=D*D
            p0=A*D
            p1=(D-A)*C
            p2=(D-A)*(D-C)
            w=d-p1
            pows=[[1,p0,p0*p0,p0*p0*p0],[1,p1,p1*p1,p1*p1*p1],[1,p2,p2*p2,p2*p2*p2]]
            zp=[1,p1,p1*p1,p1*p1*p1]
            wp=[1,w,w*w,w*w*w]
            q=[sum(G[x][h]*zp[h]*wp[3-h] for h in range(4)) for x in range(27)]
            num=sum(abs(M*pows[0][e[0]]*pows[1][e[1]]*pows[2][e[2]]-q[x]) for x,e in enumerate(EXPS))
            if num>best: best,bestij=num,(i,j)
    return Q(best,den), bestij, best,den

def exact_cert():
    assert Q(24)+Q(147,8)==Q(339,8)
    assert Q(339,8)+Q(12)==Q(435,8)
    def extension(N): return Q(3915,8192*N*N)
    N=256
    m,where,num,den=grid_max(N)
    expected=Q(35098787251437814650241024,147573952589676412928000000)
    assert m==expected and where==(141,256)
    bound=m+extension(N)
    assert bound==Q(1046057444764480007,4398046511104000000)
    assert bound<Q(237846,1000000)
    print('PASS_S23_N3_BILINEAR_SECOND_ORDER_CERTIFICATE')
    print('N256_points=',(N+1)**2,'max_i_j=',where, 'max_T=',num,'den=',den)
    print('N256_max_grid=',m)
    print('N256_extension=',extension(N))
    print('N256_all_real_bound=',bound, 'decimal=',format(float(bound),'.17f'))
    # The next exact 8192 maximum is an existing remote source certificate,
    # not independently re-enumerated in this invocation.
    remote=Q(21422604982162266373,90071992547409920000)
    updated=remote+extension(8192)
    assert updated==Q(21422605623595866373,90071992547409920000)
    assert updated<Q(237839,1000000)
    assert updated>Q(5211,21952)
    print('REUSED_SOURCE_GRID_N8192=',remote)
    print('N8192_extension=',extension(8192))
    print('N8192_all_real_bound=',updated,'decimal=',format(float(updated),'.17f'))
    print('N8192_gap_from_prior_lower=',updated-Q(5211,21952))
    print('CHECKS exact integer/rational; 8192 enumeration REUSED not rerun')

if __name__=='__main__': exact_cert()
