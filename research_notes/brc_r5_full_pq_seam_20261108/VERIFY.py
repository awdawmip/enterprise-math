#!/usr/bin/env python3
"""Exact Fraction verifier for R5 two-chart full-p/q low-ratio prism.
The real-parameter proof is in RESEARCH.md; arithmetic checks its 64 vertices.
"""
from fractions import Fraction as F
from itertools import product

R=tuple(map(F,('1/10','1/2','3/4','1','5/4','3/2','19/10')))
T=F(1,40)
S={(0,0):F(3,4),(1,0):F(1,2),(0,1):F(9,10),(1,1):F(3,4)}
CERT="""
G 0 0 0 0 492859/497316 0 492859/497316 492859/39785280 17163/3315440 333341/39785280 0
G 0 0 0 1 492859/497316 0 492859/497316 492859/39785280 1153287/6630880 333341/39785280 0
F 0 0 0 0 60761/69060 10843/138120 60761/69060 1681/46040 113707/552480 92/1151 10843/1381200
F 0 0 0 1 529266/529825 78937/4238600 529266/529825 37947/16954400 384229/1695440 15391/16954400 78937/42386000
G 0 0 1 0 164451/165772 0 164451/165772 164451/13261760 106263/16577200 21597/2652352 0
G 0 0 1 1 164451/165772 0 164451/165772 164451/13261760 5807331/33154400 21597/2652352 0
F 0 0 1 0 508231/575500 44249/575500 508231/575500 331741/9208000 190043/920800 720263/9208000 44249/5755000
F 0 0 1 1 1 1/40 1 0 91/400 0 1/400
G 0 1 0 0 1 0 1 7/1600 1/100 21/80 0
G 0 1 0 1 1 0 1 7/1600 17/80 21/80 0
F 0 1 0 0 1177/1180 0 1177/1180 0 10593/47200 24427/94400 0
F 0 1 0 1 1 1/50 1 7/8000 227/1000 33/125 1/500
G 0 1 1 0 1 0 1 7/1600 1/80 21/80 0
G 0 1 1 1 1 0 1 7/1600 43/200 21/80 0
F 0 1 1 0 1179/1180 0 1179/1180 0 10611/47200 24387/94400 0
F 0 1 1 1 1 1/40 1 0 91/400 423/1600 1/400
G 1 0 0 0 1 0 357/380 357/30400 157/3040 0 0
G 1 0 0 1 1 0 357/380 357/30400 499/3040 0 0
F 1 0 0 0 640261/863250 713551/3453000 640261/863250 703779/9208000 64759/345300 381663/2302000 713551/34530000
F 1 0 0 1 3724361/3731700 428399/14926800 926861/932925 161843/7960960 6759079/29853600 89743/39804800 428399/149268000
G 1 0 1 0 1 0 357/380 357/30400 823/15200 0 0
G 1 0 1 1 1 0 357/380 357/30400 2533/15200 0 0
F 1 0 1 0 42873/57550 23599/115100 42873/57550 17483/230200 86611/460400 302183/1841600 23599/1151000
F 1 0 1 1 1 1/40 1 33/1600 91/400 0 1/400
G 1 1 0 0 1 0 1 1/80 7/200 1/4 0
G 1 1 0 1 1 0 1 1/80 163/800 1/4 0
F 1 1 0 0 1183/1200 0 1183/1200 1183/96000 3549/16000 24323/96000 0
F 1 1 0 1 32991/32995 6567/263960 32991/32995 206057/10558400 120081/527920 2779667/10558400 6567/2639600
G 1 1 1 0 1 0 1 1/80 3/80 1/4 0
G 1 1 1 1 1 0 1 1/80 33/160 1/4 0
F 1 1 1 0 79/80 0 79/80 79/6400 711/3200 1619/6400 0
F 1 1 1 1 1 1/40 1 33/1600 91/400 423/1600 1/400
"""
Y={}
for line in CERT.strip().splitlines():
    ch,p,q,th,lam,*v=line.split()
    Y[ch,int(p),int(q),int(th),int(lam)]=tuple(map(F,v))
assert len(Y)==32

def source(t,p,q,theta,kappa):
    return (F(1),t,F(1),(F(13,40)*t+F(1,80))*p,
            F(9,40)*kappa+t*theta/10,
            (F(3,40)*t+F(21,80))*q,t*theta/10)

def masses(f):
    g,a,b,u,v,w,z=f
    return (F(509,900)*u+F(47,180)*z+F(67,162)*(v-z)+w/100,
            F(13,40)*a+b/80-u,(g-a)/2,
            1-g+a/10+F(9,40)*b-v+F(191,450)*(u+w)+F(43,90)*z+F(14,81)*(v-z),
            (g-b)/2,F(3,40)*a+F(21,80)*b-w,
            u/100+F(47,180)*z+F(67,162)*(v-z)+F(509,900)*w)

def tp(f):
    g,a,b,u,v,w,z=f
    return 1+g+F(3,8)*a+F(5,8)*b+u/2+v+F(3,2)*w

def tq(f):
    g,a,b,u,v,w,z=f
    return 1+g+(a+b)/2+u+v+w

def lawful(f):
    g,a,b,u,v,w,z=f
    assert 0<=a<=g<=1 and 0<=b<=g
    assert 0<=u<=F(13,40)*a+b/80
    assert 0<=w<=F(3,40)*a+F(21,80)*b
    assert 0<=z<=a/10 and 0<=v-z<=F(9,40)*b
    m=masses(f)
    assert all(v>=0 for v in m)
    assert sum(m)==1 and sum(a*b for a,b in zip(R,m))==1
    return m

def hinge(f,k):
    return sum(max(r-k,F(0))*m for r,m in zip(R,masses(f)))

def check(x,y,chart):
    lawful(x);lawful(y)
    assert (tp(x),tq(x))==(tp(y),tq(y))
    assert all(hinge(y,k)>=hinge(x,k) for k in R[1:-1])
    if chart=='G':
        assert y[1]==y[6]==0
    else:
        assert y[6]==y[1]/10 and y[4]-y[6]==F(9,40)*y[2]
    assert 9*y[2]*y[6]==4*y[1]*(y[4]-y[6])

def seam(t,p,q):
    s=sum(S[i,j]*(p if i else 1-p)*(q if j else 1-q)
          for i,j in product((0,1),repeat=2))
    return 1-(t/T)*(1-s)

def target(t,p,q,theta,kappa):
    h=seam(t,p,q)
    if kappa<=h:
        chart='G';lam=kappa/h
    else:
        chart='F';lam=(kappa-h)/(1-h)
    zt=t/T
    y=[F(0)]*7
    for tv,pv,qv,thv,lv in product((0,1),repeat=5):
        wt=(zt if tv else 1-zt)*(p if pv else 1-p)*(q if qv else 1-q)*(theta if thv else 1-theta)*(lam if lv else 1-lam)
        if tv:
            vertex=Y[chart,pv,qv,thv,lv]
        else:
            s0=seam(F(0),F(pv),F(qv))
            kapv=F(lv)*s0 if chart=='G' else s0+F(lv)*(1-s0)
            vertex=source(F(0),F(pv),F(qv),F(thv),kapv)
        for k in range(7):
            y[k]+=wt*vertex[k]
    yy=tuple(y)
    check(source(t,p,q,theta,kappa),yy,chart)
    return chart,yy

if __name__=='__main__':
    checked=0
    for ch,p,q,th,lam in Y:
        kap=F(lam)*S[p,q] if ch=='G' else S[p,q]+F(lam)*(1-S[p,q])
        check(source(T,F(p),F(q),F(th),kap),Y[ch,p,q,th,lam],ch)
        checked+=1
    for ch,p,q,th,lam in Y:
        kap=F(lam) if ch=='G' else F(1)
        x=source(F(0),F(p),F(q),F(th),kap)
        check(x,x,ch)
        checked+=1
    print('PASS_EXACT_VERTEX_HINGE_AND_SEEDLESS',checked)
    for j in range(151):
        t=T*F((31*j+7)%151,151)
        p=F((19*j+5)%151,151)
        q=F((23*j+13)%151,151)
        theta=F((29*j+17)%151,151)
        h=seam(t,p,q)
        kap=h*F((37*j+11)%151,151) if j%2==0 else h+(1-h)*F((37*j+11)%151,151)
        target(t,p,q,theta,kap)
    print('PASS_EXACT_INTERIOR_INTERPOLATION',151)
    print('THEOREM_ALL_REAL_FIVE_PARAMETER_LOW_RATIO_COMPLETE_PRISM')
