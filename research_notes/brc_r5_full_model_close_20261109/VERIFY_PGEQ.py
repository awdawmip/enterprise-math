#!/usr/bin/env python3
"""Exact author certificate for the R5 F-face p>=q triangular bridge.
Standard library only. Frozen 7-node P/Q-BRC model, pins stated in RESEARCH.md.
The two time equalities reconstruct (u,w) from the three stored (g,a,b).
No floating-point arithmetic, optimization solver, or numerical tolerance is used.
"""
from fractions import Fraction as F
from itertools import product

R = tuple(map(F, ("1/10","1/2","3/4","1","5/4","3/2","19/10")))
T0,T1=F(1,13),F(1,5)
VERTICES=((F(0),F(0)),(F(1),F(0)),(F(1),F(1)))
DATA = """\
1/13 000 2/3 8/39 2/3
1/13 001 105621/105965 78937/1377545 105621/105965
1/13 010 87/130 27/130 87/130
1/13 011 1 1/13 1
1/13 100 157/240 167/624 157/240
1/13 101 2410927/2425605 428399/4851210 2377093/2425605
1/13 110 683/1040 281/1040 683/1040
1/13 111 1 1/13 1
1/13 200 1199/1300 0 1199/1300
1/13 201 85755/85787 6567/85787 85755/85787
1/13 210 241/260 0 241/260
1/13 211 1 1/13 1
1/5 000 2/3 4/15 2/3
1/5 001 525353/529825 78937/529825 525353/529825
1/5 010 101/150 41/150 101/150
1/5 011 1 1/5 1
1/5 100 769/1200 19/48 769/1200
1/5 101 1359031/1374775 287406/1374775 1313919/1374775
1/5 110 259/400 161/400 259/400
1/5 111 1 1/5 1
1/5 200 1 11/300 1
1/5 201 1 14/75 1
1/5 210 1 1/20 1
1/5 211 1 1/5 1
"""
CERT={}
for line in DATA.strip().splitlines():
    t,bits,*vals=line.split()
    key=(F(t),int(bits[0]),int(bits[1]),int(bits[2]))
    assert key not in CERT and len(vals)==3
    CERT[key]=tuple(map(F,vals))
assert len(CERT)==24

def source(t,p,q,th,ka):
    return (F(1),t,F(1),(F(13,40)*t+F(1,80))*p,
            F(9,40)*ka+t*th/10,(F(3,40)*t+F(21,80))*q,t*th/10)

def mass(x):
    g,a,b,u,v,w,z=x
    return (F(509,900)*u+F(47,180)*z+F(67,162)*(v-z)+w/100,
            F(13,40)*a+b/80-u,(g-a)/2,
            1-g+a/10+F(9,40)*b-v+F(191,450)*(u+w)+F(43,90)*z+F(14,81)*(v-z),
            (g-b)/2,F(3,40)*a+F(21,80)*b-w,
            u/100+F(47,180)*z+F(67,162)*(v-z)+F(509,900)*w)

def tp(x):
    g,a,b,u,v,w,z=x
    return 1+g+F(3,8)*a+F(5,8)*b+u/2+v+F(3,2)*w

def tq(x):
    g,a,b,u,v,w,z=x
    return 1+g+(a+b)/2+u+v+w

def hinges(x):
    m=mass(x)
    return tuple(sum(max(F(0),ri-rk)*mi for ri,mi in zip(R,m)) for rk in R[1:-1])

def lawful(x):
    g,a,b,u,v,w,z=x
    assert 0<=a<=g<=1 and 0<=b<=g
    assert 0<=u<=F(13,40)*a+b/80
    assert 0<=w<=F(3,40)*a+F(21,80)*b
    assert 0<=z<=a/10 and 0<=v-z<=F(9,40)*b
    m=mass(x)
    assert all(z>=0 for z in m)
    assert sum(m)==1 and sum(ri*mi for ri,mi in zip(R,m))==1

def calibrated_target(src,g,a,b):
    P,Q=tp(src),tq(src)
    u=-F(17,40)*a-F(19,80)*b-g/2-P+F(3,2)*Q-F(1,2)
    w=-F(7,40)*a-F(39,80)*b-g/2+P-Q/2-F(1,2)
    return (g,a,b,u,a/10+F(9,40)*b,w,a/10)

def verify(x,y):
    lawful(x);lawful(y)
    g,a,b,u,v,w,z=y
    assert z==a/10 and v-z==F(9,40)*b
    assert 9*b*z==4*a*(v-z)
    assert tp(x)==tp(y) and tq(x)==tq(y)
    gaps=tuple(i-j for i,j in zip(hinges(y),hinges(x)))
    assert all(h>=0 for h in gaps)
    return gaps

def target(t,p,q,th,ka):
    assert T0<=t<=T1 and 0<=q<=p<=1 and 0<=th<=1 and 0<=ka<=1
    wt=(t-T0)/(T1-T0)
    tw=(1-wt,wt)
    beta=(1-p,p-q,q) # vertices (0,0),(1,0),(1,1)
    ys=[F(0)]*7
    for it,tv in enumerate((T0,T1)):
        for j,(pv,qv) in enumerate(VERTICES):
            for ith,thv in enumerate((F(0),F(1))):
                for ika,kav in enumerate((F(0),F(1))):
                    ww=tw[it]*beta[j]*(th if ith else 1-th)*(ka if ika else 1-ka)
                    if ww==0: continue
                    xx=source(tv,pv,qv,thv,kav)
                    yy=calibrated_target(xx,*CERT[(tv,j,ith,ika)])
                    for d in range(7):ys[d]+=ww*yy[d]
    y=tuple(ys)
    verify(source(t,p,q,th,ka),y)
    return y

def normalized_to_physical(x,g,b):
    assert 0<=b<=g<=1
    E1=(F(1),)+ (F(0),)*6
    E0=(F(0),)*7
    return tuple(b*x[i]+(g-b)*E1[i]+(1-g)*E0[i] for i in range(7))

def main():
    hinge_min=[None]*5
    for tv in (T0,T1):
        for j,(p,q) in enumerate(VERTICES):
            for th,ka in product((F(0),F(1)),repeat=2):
                xx=source(tv,p,q,th,ka)
                yy=calibrated_target(xx,*CERT[(tv,j,int(th),int(ka))])
                gaps=verify(xx,yy)
                for i,gap in enumerate(gaps):
                    hinge_min[i]=gap if hinge_min[i] is None else min(hinge_min[i],gap)
    print("PASS_EXACT_24_F_FACE_TRIANGLE_CORNERS")
    print("MIN_HINGE_GAPS",*map(str,hinge_min))
    for j in range(251):
        den=257
        t=T0+(T1-T0)*F((17*j+11)%den,den)
        p=F((23*j+13)%den,den)
        q=p*F((29*j+19)%den,den)
        th=F((31*j+23)%den,den)
        ka=F((37*j+29)%den,den)
        y=target(t,p,q,th,ka)
        g=F((41*j+31)%den,den)
        b=g*F((43*j+37)%den,den)
        verify(normalized_to_physical(source(t,p,q,th,ka),g,b),
               normalized_to_physical(y,g,b))
    print("PASS_EXACT_251_NORMALIZED_AND_SCALED_REGRESSIONS")
    print("THEOREM_ALL_REAL_T_1_13_TO_1_5_P_GE_Q_F_FACE_STRASSEN")
if __name__=="__main__":
    main()
