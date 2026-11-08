#!/usr/bin/env python3
"""Exact all-real R5 F-face gap-prism certificate and sharp single-corner dual.
No nonstdlib runtime dependencies. CERT rows are independent rational targets.
"""
from fractions import Fraction as F
from itertools import product

R = tuple(map(F, ("1/10","1/2","3/4","1","5/4","3/2","19/10")))
PSTAR=F(303,2450)
T0,T1=F(3,20),F(7,39)
CERT = """\
0 0 0 0 0 1 6909/80000 39697/80000 219331/6400000 384909/3200000 875091/6400000 6909/800000
0 0 0 0 1 526471/529825 236811/2119300 526471/529825 17805579/847720000 99501/423860 46173/8477200 236811/21193000
0 0 0 1 0 1 7509/80000 40297/80000 235531/6400000 392709/3200000 891291/6400000 7509/800000
0 0 0 1 1 1 3/20 1 303/40000 6/25 0 3/200
0 0 1 0 0 467/500 0 467/500 0 4203/20000 9807/40000 0
0 0 1 0 1 1 3/25 1 513/40000 237/1000 543/2000 3/250
0 0 1 1 0 47/50 0 47/50 123/40000 423/2000 987/4000 0
0 0 1 1 1 1 3/20 1 303/40000 6/25 219/800 3/200
0 1 0 0 0 1 267/1600 751/1600 7693/128000 7827/64000 17373/128000 267/16000
0 1 0 0 1 1 1007847/6815450 3327199/3407725 1642921/27261800 6392097/27261800 478869/109047200 1007847/68154500
0 1 0 1 0 1 279/1600 763/1600 8017/128000 7983/64000 17697/128000 279/16000
0 1 0 1 1 1 3/20 1 49/800 6/25 0 3/200
0 1 1 0 0 99/100 0 99/100 99/8000 891/4000 1519/8000 0
0 1 1 0 1 1 57/400 397/400 1879/32000 3801/16000 8679/32000 57/4000
0 1 1 1 0 1 0 1 1/80 9/40 3/16 0
0 1 1 1 1 1 3/20 1 49/800 6/25 219/800 3/200
1 0 0 0 0 1 1572889/15288000 194283/392000 532661/13440000 74484889/611520000 56185037/407680000 1572889/152880000
1 0 0 0 1 315487/317895 552559/4132635 315487/317895 103136181/4153828000 7824443/33061080 107737/16530540 552559/41326350
1 0 0 1 0 1 1710089/15288000 7714237/15288000 7453793/174720000 76268489/611520000 57419837/407680000 1710089/152880000
1 0 0 1 1 1 7/39 1 1717/196000 379/1560 0 7/390
1 0 1 0 0 3661/3900 0 3661/3900 5359/611520 10983/52000 25627/104000 0
1 0 1 0 1 1 28/195 1 114983/7644000 1867/7800 1421/5200 14/975
1 0 1 1 0 5427563/5733000 0 5427563/5733000 5427563/458640000 5427563/25480000 113505523/458640000 0
1 0 1 1 1 1 7/39 1 1717/196000 379/1560 287/1040 7/390
1 1 0 0 0 1 1223/6240 223/480 2669/38400 30983/249600 22739/166400 1223/62400
1 1 0 0 1 1 1567762/8860085 25828679/26580255 29622823/425284080 16751417/70880680 1117361/212642040 783881/44300425
1 1 0 1 0 1 1279/6240 197/416 36209/499200 31711/249600 23243/166400 1279/62400
1 1 0 1 1 1 7/39 1 17/240 379/1560 0 7/390
1 1 1 0 0 1 41/2340 1 131/7200 2653/11700 17113/93600 41/23400
1 1 1 0 1 1 133/780 773/780 4231/62400 7489/31200 5677/20800 133/7800
1 1 1 1 0 1 23/780 1 53/2400 889/3900 1973/10400 23/7800
1 1 1 1 1 1 7/39 1 17/240 379/1560 287/1040 7/390
"""
Y={}
for line in CERT.splitlines():
    ti,pi,qi,thi,ki,*coords=line.split()
    key=tuple(map(int,(ti,pi,qi,thi,ki)))
    assert key not in Y and len(coords)==7
    Y[key]=tuple(map(F,coords))
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

def verify(x,y):
    lawful(x); lawful(y)
    assert y[6]==y[1]/10 and y[4]-y[6]==F(9,40)*y[2]
    assert 9*y[2]*y[6]==4*y[1]*(y[4]-y[6])
    assert tp(x)==tp(y) and tq(x)==tq(y)
    assert all(hinge(y,k)>=hinge(x,k) for k in R[1:-1])

def target(t,p,q,theta,kappa):
    assert T0<=t<=T1 and PSTAR<=p<=1
    assert all(0<=v<=1 for v in (q,theta,kappa))
    axes=((t-T0)/(T1-T0),(p-PSTAR)/(1-PSTAR),q,theta,kappa)
    ans=[F(0)]*7
    for bits,y in Y.items():
        weight=F(1)
        for bit,param in zip(bits,axes):
            weight*= param if bit else 1-param
        for j in range(7): ans[j]+=weight*y[j]
    y=tuple(ans)
    verify(source(t,p,q,theta,kappa),y)
    return y

def dual_identity(p,y):
    """Affine identity valid on F face, no feasibility assumptions."""
    g,a,b,u,v,w,z=y
    assert z==a/10 and v-z==F(9,40)*b
    x=source(T0,p,F(1),F(0),F(0))
    rhs=(F(222,49)*a+F(164,49)*(g-b)+F(800,49)*u
         +F(472,49)*(F(3,40)*a+F(21,80)*b-w)
         +F(1272,49)*(tp(y)-tp(x))-F(1436,49)*(tq(y)-tq(x)))
    assert rhs==p-PSTAR
def F_lift(g,a,b,u,w):
    return (g,a,b,u,a/10+F(9,40)*b,w,a/10)

def main():
    for bits,y in Y.items():
        ti,pi,q,theta,kappa=bits
        t=(T0,T1)[ti]; p=(PSTAR,F(1))[pi]
        verify(source(t,p,F(q),F(theta),F(kappa)),y)
    print("PASS_EXACT_F_FACE_32_CORNERS",len(Y))

    # Exact affine coefficient identity: constant term plus 6 basis vectors.
    dual_identity(F(0),F_lift(*(F(0),)*5))
    for i in range(6):
        args=[F(0)]*6;args[i]=F(1)
        dual_identity(args[0],F_lift(*args[1:]))
    print("PASS_EXACT_DUAL_AFFINE_BASIS",7)

    verify(source(T0,PSTAR,F(1),F(0),F(0)),
           Y[(0,0,1,0,0)])
    for j in range(201):
        t=T0+(T1-T0)*F((31*j+7)%201,201)
        p=PSTAR+(1-PSTAR)*F((19*j+5)%201,201)
        q=F((23*j+13)%201,201)
        th=F((29*j+17)%201,201)
        k=F((37*j+11)%201,201)
        target(t,p,q,th,k)
    print("PASS_EXACT_201_INTERIOR_REGRESSIONS")
    for t in (T0,T1):
        for p in (PSTAR,F(1)):
            for q,th,k in product((F(0),F(1)),repeat=3):
                target(t,p,q,th,k)
    print("PASS_EXACT_32_BOUNDARY_REGRESSIONS")
    print("THEOREM_ALL_REAL_T_3_20_TO_7_39_P_GE_303_2450_ALL_Q_THETA_KAPPA")
    print("SHARP_F_FACE_PSTAR_303_2450_AT_T_3_20_Q_1_THETA_KAPPA_0")

if __name__=="__main__":
    main()
