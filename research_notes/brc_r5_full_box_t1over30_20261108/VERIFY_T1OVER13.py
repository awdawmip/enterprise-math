#!/usr/bin/env python3
"""Exact independent endpoint table for the enlarged R5 t<=1/13 prism.

Reuses only fixed seven-node calibrated mass/time/hinge/legality definitions
from VERIFY.py, which is in the same directory. No floating-point arithmetic.
"""
from fractions import Fraction as F
from itertools import product
import VERIFY as v

v.T=F(1,13)
v.S={(0,0):F(3,5),(0,1):F(7,10),(1,0):F(1,20),(1,1):F(2,5)}
CERT="""
G 0 0 0 0 1 0 240/247 3/247 10/247 0 0
G 0 0 0 1 1 0 240/247 3/247 8669/49400 0 0
G 0 0 1 0 1 0 240/247 3/247 119/2470 0 0
G 0 0 1 1 1 0 240/247 3/247 9049/49400 0 0
G 0 1 0 0 1 0 1 1/80 17/520 17/65 0
G 0 1 0 1 1 0 1 1/80 989/5200 17/65 0
G 0 1 1 0 1 0 1 1/80 21/520 17/65 0
G 0 1 1 1 1 0 1 1/80 1029/5200 17/65 0
G 1 0 0 0 1 0 201/247 201/19760 157/988 0 0
G 1 0 0 1 1 0 201/247 201/19760 33623/197600 0 0
G 1 0 1 0 1 0 201/247 201/19760 823/4940 0 0
G 1 0 1 1 1 0 201/247 201/19760 35143/197600 0 0
G 1 1 0 0 1 0 1 1/80 7/65 233/1040 0
G 1 1 0 1 1 0 1 1/80 257/1300 233/1040 0
G 1 1 1 0 1 0 1 1/80 3/26 233/1040 0
G 1 1 1 1 1 0 1 1/80 267/1300 233/1040 0
F 0 0 0 0 4951/5135 0 4951/5135 211/20540 44559/205400 0 0
F 0 0 0 1 1289073/1289977 75979/1289977 1289073/1289977 11173/2579954 11905573/51599080 0 75979/12899770
F 0 0 1 0 4971/5135 0 4971/5135 231/20540 44739/205400 0 0
F 0 0 1 1 1 1/13 1 0 121/520 0 1/130
F 0 1 0 0 7619/7670 0 7619/7670 0 68571/306800 15383/61360 0
F 0 1 0 1 1 15/221 1 0 2049/8840 4703/17680 3/442
F 0 1 1 0 7659/7670 0 7659/7670 0 68931/306800 15303/61360 0
F 0 1 1 1 1 1/13 1 0 121/520 279/1040 1/130
F 1 0 0 0 454031/507000 34243/1014000 454031/507000 29973/1352000 830953/4056000 0 34243/10140000
F 1 0 0 1 1 496/6695 6649/6695 3909/107120 2473/10712 0 248/33475
F 1 0 1 0 11689/13000 917/26000 11689/13000 2361/104000 21407/104000 0 917/260000
F 1 0 1 1 1 1/13 1 3/80 121/520 0 1/130
F 1 1 0 0 3829/3835 0 3829/3835 0 34461/153400 3251/15340 0
F 1 1 0 1 1 14/195 1 43/1200 1811/7800 4139/15600 7/975
F 1 1 1 0 1 7/1105 1 0 9973/44200 471/2210 7/11050
F 1 1 1 1 1 1/13 1 3/80 121/520 279/1040 1/130
"""
v.Y={}
for line in CERT.strip().splitlines():
    ch,p,q,th,lam,*coords=line.split()
    v.Y[ch,int(p),int(q),int(th),int(lam)]=tuple(map(F,coords))
assert len(v.Y)==32

def target(t,p,q,theta,kappa):
    h=v.seam(t,p,q)
    assert F(1,20)<=h<=1
    if kappa<=h:
        ch="G"; lam=kappa/h
    else:
        ch="F"; lam=(kappa-h)/(1-h)
    y=[F(0)]*7
    for tv,pv,qv,thv,lv in product((0,1),repeat=5):
        weight=(t/v.T if tv else 1-t/v.T)*(p if pv else 1-p)*(
            q if qv else 1-q)*(theta if thv else 1-theta)*(
            lam if lv else 1-lam)
        if tv:
            z=v.Y[ch,pv,qv,thv,lv]
        else:
            z=v.source(F(0),F(pv),F(qv),F(thv),
                       F(lv) if ch=="G" else F(1))
        for j in range(7): y[j]+=weight*z[j]
    y=tuple(y)
    v.check(v.source(t,p,q,theta,kappa),y,ch)
    return ch,y

def main():
    count=0
    for ch,p,q,th,lam in v.Y:
        k=F(lam)*v.S[p,q] if ch=="G" else v.S[p,q]+F(lam)*(1-v.S[p,q])
        v.check(v.source(v.T,F(p),F(q),F(th),k),v.Y[ch,p,q,th,lam],ch)
        count+=1
        x=v.source(F(0),F(p),F(q),F(th),F(lam) if ch=="G" else F(1))
        v.check(x,x,ch)
        count+=1
    print("PASS_EXACT_ENDPOINT_VERTICES",count)
    for j in range(251):
        t=v.T*F((31*j+7)%251,251)
        p=F((19*j+5)%251,251)
        q=F((23*j+13)%251,251)
        theta=F((29*j+17)%251,251)
        h=v.seam(t,p,q)
        k=h*F((37*j+11)%251,251) if j%2==0 else h+(1-h)*F((37*j+11)%251,251)
        target(t,p,q,theta,k)
    print("PASS_EXACT_INTERIOR",251)
    for p,q,theta,k in product((F(0),F(1)),repeat=4):
        target(F(0),p,q,theta,k)
        target(v.T,p,q,theta,k)
    print("PASS_PHYSICAL_BOUNDARY",32)
    print("ALL_REAL_FIVE_PARAMETER_BOX_T_LE_1_OVER_13_AUTHOR_CERTIFICATE")

if __name__=="__main__": main()
