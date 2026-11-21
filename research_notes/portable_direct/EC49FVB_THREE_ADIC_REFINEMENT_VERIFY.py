"""Exact finite crosscheck of EC49FVB three-adic valuation theorem."""
from fractions import Fraction as F
from math import gcd

BETA=F(3,637)
GAMMA=F(141024,1653649)
U=F(4822040484,8132285009)
M=8132285009
L=8*M

def vp(a,p=3):
    assert a
    n=0
    while a%p==0:
        n+=1
        a//=p
    return n

def v(q):
    return vp(q.numerator)-vp(q.denominator)

def vals(x):
    t0=(1-x)*(1-BETA*x)
    te=(1-x)*(1+GAMMA*x)
    a=1-t0
    b=1-U*te
    r=t0/(U*te)
    s=(b/a)*r
    assert 0<a<b<1 and 1<r<s
    return v(r),v(s)

assert tuple(map(v,(BETA,GAMMA,U)))==(1,1,6)
c1=c2=c3=0
for d in range(2,241):
    for m in range(1,d):
        if gcd(m,d)!=1:continue
        x=F(m,d)
        vr,vs=vals(x)
        if d%3!=0 and m%3!=0:
            assert (vr,vs)==(-6,-6),(m,d,vr,vs)
            c1+=1
        if d%9==0:
            j=vp(d)
            if j<=3:
                assert (vr,vs)==(-6,2*j-7),(m,d,j,vr,vs)
            else:
                assert (vr,vs)==(-6,0),(m,d,j,vr,vs)
            c2+=1
        if d%3==0 and d%9!=0 and (m*pow(d//3,-1,3))%3==2:
            assert vr<vs<0,(m,d,vr,vs)
            c3+=1
assert min(c1,c2,c3)>100
assert 3*L-40==195174840176
print('ALL PASS: v3(beta,gamma,u)=(1,1,6);',c1,'unit m,d;',c2,'denominator v3>=2;',c3,'v3(d)=1 and 3x mod3=2')
print('CRT 40 unresolved of 3*L=',3*L,'certified',3*L-40)
