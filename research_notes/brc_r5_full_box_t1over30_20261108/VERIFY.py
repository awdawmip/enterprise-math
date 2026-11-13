#!/usr/bin/env python3
"""R5 full physical p/q/theta/kappa rational vertex verifier. Pure stdlib Fraction."""
from fractions import Fraction as F
from itertools import product

R=tuple(map(F,("1/10","1/2","3/4","1","5/4","3/2","19/10")))
T=F(1,30)
S={(0,0):F(3,4),(0,1):F(9,10),(1,0):F(1,2),(1,1):F(3,4)}
# Entries: chart,p,q,theta,lambda,g,a,b,u,v,w,z. All rational, independently checked.
CERT="""
G 0 0 0 0 731143/733759 0 731143/733759 731143/58700720 16677/3668795 882871/176102160 0
G 0 0 0 1 731143/733759 0 731143/733759 731143/58700720 20345157/117401440 882871/176102160 0
G 0 0 1 0 6586709/6603831 0 6586709/6603831 6586709/528306480 121787/18343975 505319/105661296 0
G 0 0 1 1 6586709/6603831 0 6586709/6603831 6586709/528306480 102954649/587007200 505319/105661296 0
G 0 1 0 0 1 0 1 7/1200 1/75 21/80 0
G 0 1 0 1 1 0 1 7/1200 259/1200 21/80 0
G 0 1 1 0 1 0 1 7/1200 1/60 21/80 0
G 0 1 1 1 1 0 1 7/1200 263/1200 21/80 0
G 1 0 0 0 1 0 262/285 131/11400 157/2280 0 0
G 1 0 0 1 1 0 262/285 131/11400 827/4560 0 0
G 1 0 1 0 1 0 262/285 131/11400 823/11400 0 0
G 1 0 1 1 1 0 262/285 131/11400 4211/22800 0 0
G 1 1 0 0 1 0 1 1/80 7/150 59/240 0
G 1 1 0 1 1 0 1 1/80 517/2400 59/240 0
G 1 1 1 0 1 0 1 1/80 1/20 59/240 0
G 1 1 1 1 1 0 1 1/80 7/32 59/240 0
F 0 0 0 0 925/948 0 925/948 43/18960 555/2528 0 0
F 0 0 0 1 1487983/1488435 75979/2976870 1487983/1488435 11173/5953740 2708761/11907480 0 75979/29768700
F 0 0 1 0 4633/4740 0 4633/4740 17/6320 13899/63200 0 0
F 0 0 1 1 1 1/30 1 0 137/600 0 1/300
F 0 1 0 0 1 1/340 1 0 383/1700 5251/20400 1/3400
F 0 1 0 1 1 1/34 1 0 31/136 2693/10200 1/340
F 0 1 1 0 1 7/1020 1 0 1151/5100 1757/6800 7/10200
F 0 1 1 1 1 1/30 1 0 137/600 53/200 1/300
F 1 0 0 0 55303/58500 1259/117000 55303/58500 2389/156000 100049/468000 0 1259/1170000
F 1 0 0 1 1 248/7725 7702/7725 283/12360 7031/30900 0 124/38625
F 1 0 1 0 1231/1300 89/7800 1231/1300 97/6240 6683/31200 0 89/78000
F 1 0 1 1 1 1/30 1 7/300 137/600 0 1/300
F 1 1 0 0 1 37/2040 1 0 4627/20400 647/2720 37/20400
F 1 1 0 1 1 7/225 1 407/18000 2053/9000 4747/18000 7/2250
F 1 1 1 0 1 3/136 1 0 309/1360 1949/8160 3/1360
F 1 1 1 1 1 1/30 1 7/300 137/600 53/200 1/300
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

def mass(f):
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

def hinge(f,k):
    return sum(max(ri-k,F(0))*mi for ri,mi in zip(R,mass(f)))

def lawful(f):
    g,a,b,u,v,w,z=f
    assert 0<=a<=g<=1 and 0<=b<=g
    assert 0<=u<=F(13,40)*a+b/80
    assert 0<=w<=F(3,40)*a+F(21,80)*b
    assert 0<=z<=a/10 and 0<=v-z<=F(9,40)*b
    m=mass(f)
    assert all(mi>=0 for mi in m)
    assert sum(m)==1 and sum(ri*mi for ri,mi in zip(R,m))==1

def check(x,y,chart):
    lawful(x);lawful(y)
    assert tp(x)==tp(y) and tq(x)==tq(y)
    assert all(hinge(y,rk)>=hinge(x,rk) for rk in R[1:-1])
    if chart=='G': assert y[1]==y[6]==0
    else: assert y[6]==y[1]/10 and y[4]-y[6]==F(9,40)*y[2]
    assert 9*y[2]*y[6]==4*y[1]*(y[4]-y[6])

def S_of(p,q):
    return sum(S[i,j]*(p if i else 1-p)*(q if j else 1-q)
               for i,j in product((0,1),repeat=2))

def seam(t,p,q):
    return 1-(t/T)*(1-S_of(p,q))

def target(t,p,q,theta,kappa):
    h=seam(t,p,q)
    assert F(1,2)<=h<=1
    if kappa<=h:
        ch='G';lam=kappa/h
    else:
        ch='F';lam=(kappa-h)/(1-h)
    zt=t/T
    yy=[F(0)]*7
    for tv,pv,qv,thv,lv in product((0,1),repeat=5):
        w=(zt if tv else 1-zt)*(p if pv else 1-p)*(q if qv else 1-q)*(
            theta if thv else 1-theta)*(lam if lv else 1-lam)
        if tv: v=Y[ch,pv,qv,thv,lv]
        else:
            kap0=F(lv) if ch=='G' else F(1)
            v=source(F(0),F(pv),F(qv),F(thv),kap0)
        for j in range(7): yy[j]+=w*v[j]
    y=tuple(yy)
    check(source(t,p,q,theta,kappa),y,ch)
    return ch,y

def main():
    count=0
    for ch,p,q,th,la in Y:
        k=F(la)*S[p,q] if ch=='G' else S[p,q]+F(la)*(1-S[p,q])
        check(source(T,F(p),F(q),F(th),k),Y[ch,p,q,th,la],ch);count+=1
        k0=F(la) if ch=='G' else F(1)
        x0=source(F(0),F(p),F(q),F(th),k0)
        check(x0,x0,ch);count+=1
    print('PASS_EXACT_ENDPOINT_VERTICES',count)
    for j in range(251):
        t=T*F((31*j+7)%251,251)
        p=F((19*j+5)%251,251)
        q=F((23*j+13)%251,251)
        theta=F((29*j+17)%251,251)
        h=seam(t,p,q)
        kap=h*F((37*j+11)%251,251) if j%2==0 else h+(1-h)*F((37*j+11)%251,251)
        target(t,p,q,theta,kap)
    for p,q,theta,k in product((F(0),F(1)),repeat=4):
        target(F(0),p,q,theta,k)
        target(T,p,q,theta,k)
    print('PASS_EXACT_INTERIOR',251)
    print('PASS_PHYSICAL_BOUNDARY',32)
    print('ALL_REAL_FIVE_PARAMETER_BOX_T_LE_1_OVER_30_AUTHOR_CERTIFICATE')

if __name__=='__main__': main()
