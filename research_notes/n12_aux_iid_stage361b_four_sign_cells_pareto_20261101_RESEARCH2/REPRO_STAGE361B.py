#!/usr/bin/env python3
from fractions import Fraction as F
W=(1,3,3,1); M=(61,21,9,9)
XL=F(229,1000); XH=F(233,1000); XT=F(234,1000)
YL=F(27,50); YH=F(14,25); YT=F(561,1000); CAP=F(299,50000)
P=((1,-3,3,-1),(0,1,-2,1),(0,0,1,-1),(0,0,0,1))
def B(k,z):return z**k*(1-z)**(3-k)
def r(k,x,y):return (4*B(k,x)+B(k,y))/5-F(M[k],160)
def b(x,y):return F(5,32)*sum((W[k]*abs(r(k,x,y)) for k in range(4)),F())
def D(a,z):return sum((W[k]*abs(B(k,a)-B(k,z)) for k in range(4)),F())/2
def c(x,y):return (63*D(F(1,4),x)+D(F(3,4),x)+9*D(F(1,4),y)+7*D(F(3,4),y))/256
def comb(v):
    a=[sum(F(v[k]*i*P[k][i]) if i<len(P[k]) else F() for k in range(4)) for i in (1,2,3)]
    while len(a)>1 and a[-1]==0:a.pop()
    return tuple(a)
def db(sign,div):return comb([F(W[k]*sign[k],div) for k in range(4)])
def dc(s,t,weights):return comb([-F(W[k]*(weights[0]*s[k]+weights[1]*t[k]),512) for k in range(4)])
def verify():
    sx=(-1,1,1,1);tx=(-1,-1,1,1);sy=(1,1,-1,-1);ty=(-1,-1,1,1)
    for a,L,H,S in ((F(1,4),XL,XT,sx),(F(3,4),XL,XT,tx),(F(1,4),YL,YT,sy),(F(3,4),YL,YT,ty)):
        for k in range(4):
            assert all(S[k]*(B(k,a)-B(k,z))>0 for z in (L,H))
    assert r(2,XL,YL)==F(3653511,1250000000)>0
    assert r(3,XT,YT)==-F(53439903,5000000000)<0
    assert r(1,XL,YL)>0
    assert db((1,1,1,-1),8)==(0,0,-F(3,4))
    assert db((1,-1,1,-1),8)==(-F(3,4),3,-3)
    assert db((-1,1,1,-1),8)==(F(3,4),-F(3,2))
    assert db((-1,1,1,-1),32)==(F(3,16),-F(3,8))
    assert db((-1,-1,1,-1),32)==(0,F(3,8),-F(9,16))
    assert dc(sx,tx,(63,1))==(-F(189,256),F(372,256),-F(183,256))
    assert dc(sy,ty,(9,7))==(0,F(3,64),-F(3,64))
    assert F(3,4)*XL**2>F(39,1000)
    assert F(3,4)*(1-2*XT)**2>F(1,5)
    assert F(3,256)*(1-XT)*(63-61*XT)>F(2,5)
    assert F(3,4)*(1-2*XL)-30*F(3,16)*(2*YL-1)==-F(87,2000)
    assert -F(2,5)+30*F(3,256)==-F(31,640)
    assert F(3,16)*YH*(2-3*YH)>F(3,100)
    assert F(3,64)*YH*(1-YH)>F(1,100)
    assert all(a-F(3,800)>limit for a,limit in
         ((F(39,1000),F(7,200)),(F(1,5),F(19,100)),(F(2,5),F(39,100)),
          (F(87,2000),F(39,1000)),(F(31,640),F(11,250)),
          (F(3,100),F(1,40)),(F(1,100),F(1,200))))
    U=(-F(5,16)*r(3,XL,YL),F(5,16)*(r(0,XL,YL)+3*r(2,XH,YH)),
       -F(5,16)*(r(0,XH,YL)+r(3,XH,YL)),F(15,16)*r(2,XH,YH))
    assert U==(F(18937511,4000000000),F(4711,800000),F(4827,1000000),F(17469489,4000000000))
    assert all(u<CAP for u in U)
    for label,p,q,sign in (
        ('++', (F(231,1000),F(27,50)),(F(23101,100000),F(27,50)),(1,1,1,-1)),
        ('+-', (F(229,1000),F(11,20)),(F(22901,100000),F(11,20)),(1,-1,1,-1)),
        ('-+', (F(233,1000),F(11,20)),(F(23301,100000),F(5503,10000)),(-1,1,1,-1)),
        ('--', (F(231,1000),F(14,25)),(F(231,1000),F(5599,10000)),(-1,-1,1,-1))):
        assert all(sign[k]*r(k,*p)>0 and sign[k]*r(k,*q)>0 for k in range(4))
        assert b(*p)>b(*q) and c(*p)>c(*q) and b(*p)<CAP
        print(label,'b_gain',b(*p)-b(*q),'c_gain',c(*p)-c(*q))
    print('STAGE361B_FOUR_OPEN_SIGN_CELLS_EXACT_PASS')
if __name__=='__main__':verify()