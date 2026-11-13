#!/usr/bin/env python3
"""Exact F-face certificate, triangular p<=q, t in [7/39,1/5]."""
from fractions import Fraction as F
from itertools import product
import VERIFY_TRIANGLE_T3OVER20 as v
START=F(7,39)
STOP=F(1,5)
CORNER=((0,0),(0,1),(1,1))
CERT="""
0 0 0 0 0 2/3 10/39 2/3 11/120 137/780 101/520 1/39
0 0 0 0 1 315487/317895 552559/4132635 315487/317895 6811/423860 7824443/33061080 107737/16530540 552559/41326350
0 0 0 1 0 787/1170 307/1170 787/1170 2923/31200 8311/46800 157/800 307/11700
0 0 0 1 1 1 7/39 1 0 379/1560 0 7/390
0 0 1 0 0 3661/3900 0 3661/3900 1/312000 10983/52000 25627/104000 0
0 0 1 0 1 1 28/195 1 49/7800 1867/7800 1421/5200 14/975
0 0 1 1 0 3689/3900 0 3689/3900 383/104000 11067/52000 25823/104000 0
0 0 1 1 1 1 7/39 1 0 379/1560 287/1040 7/390
0 1 1 0 0 1 41/2340 1 131/7200 2653/11700 17113/93600 41/23400
0 1 1 0 1 1 98/585 1 241/3600 5657/23400 12593/46800 49/2925
0 1 1 1 0 1 23/780 1 53/2400 889/3900 1973/10400 23/7800
0 1 1 1 1 1 7/39 1 17/240 379/1560 287/1040 7/390
1 0 0 0 0 2/3 4/15 2/3 19/200 53/300 39/200 2/75
1 0 0 0 1 525353/529825 78937/529825 525353/529825 37947/2119300 201757/847720 15391/2119300 78937/5298250
1 0 0 1 0 101/150 41/150 101/150 389/4000 1073/6000 789/4000 41/1500
1 0 0 1 1 1 1/5 1 0 49/200 0 1/50
1 0 1 0 0 471/500 0 471/500 211/40000 4239/20000 9891/40000 0
1 0 1 0 1 1 4/25 1 7/1000 241/1000 549/2000 2/125
1 0 1 1 0 19/20 0 19/20 3/320 171/800 399/1600 0
1 0 1 1 1 1 1/5 1 0 49/200 111/400 1/50
1 1 1 0 0 1 11/300 1 293/12000 343/1500 2203/12000 11/3000
1 1 1 0 1 1 14/75 1 439/6000 731/3000 1619/6000 7/375
1 1 1 1 0 1 1/20 1 23/800 23/100 153/800 1/200
1 1 1 1 1 1 1/5 1 31/400 49/200 111/400 1/50
"""
Y={}
for row in CERT.strip().splitlines():
    te,p,q,th,k,*y=row.split()
    Y[int(te),int(p),int(q),int(th),int(k)]=tuple(map(F,y))
assert len(Y)==24

def target(t,p,q,th,k):
    assert START<=t<=STOP and 0<=th<=1 and 0<=k<=1
    s=(t-START)/(STOP-START)
    yy=[F(0)]*7
    for te,(pv,qv),the,kk in product((0,1),CORNER,(0,1),(0,1)):
        weight=(s if te else 1-s)*v.tw(p,q)[pv,qv]*(th if the else 1-th)*(k if kk else 1-k)
        for j in range(7): yy[j]+=weight*Y[te,pv,qv,the,kk][j]
    y=tuple(yy)
    v.check(v.src(t,p,q,th,k),y,'F')
    return y

def main():
    for te,p,q,th,k in Y:
        t=START if te==0 else STOP
        v.check(v.src(t,F(p),F(q),F(th),F(k)),Y[te,p,q,th,k],'F')
    print('PASS_24_F_FACE_EXACT_CORNERS')
    for i in range(201):
        t=START+(STOP-START)*F((17*i+3)%201,201)
        q=F((23*i+7)%201,201)
        p=q*F((29*i+11)%201,201)
        th=F((31*i+13)%201,201)
        k=F((37*i+17)%201,201)
        target(t,p,q,th,k)
    print('PASS_201_EXACT_INTERIORS')
    for t in (START,STOP):
        for p,q in CORNER:
            for th,k in product((F(0),F(1)),repeat=2):
                target(t,F(p),F(q),th,k)
    print('PASS_24_EXACT_BOUNDARIES')
    print('THEOREM_ALL_REAL_T_7_OVER_39_TO_1_OVER_5_P_LE_Q_ALL_THETA_KAPPA')
if __name__=='__main__':main()
