#!/usr/bin/env python3
"""Independent exact R5 triangular-p/q Blackwell certificate. Python stdlib only."""
from fractions import Fraction as F
from itertools import product

T=F(3,20)
R=tuple(map(F,("1/10","1/2","3/4","1","5/4","3/2","19/10")))
CORNER=((0,0),(0,1),(1,1))
S={(0,0):F(1,4),(0,1):F(1,3),(1,1):F(0)}
CERT = """G 0 0 0 0 767/800 0 17/20 0 153/800 0 0
G 0 0 0 1 1 0 45/52 1/260 81/416 0 0
G 0 0 1 0 779/800 0 17/20 0 153/800 0 0
G 0 0 1 1 1 0 229/260 1/130 2061/10400 0 0
G 0 1 0 0 1 0 1 0 9/80 189/800 0
G 0 1 0 1 1 0 1 0 3/16 189/800 0
G 0 1 1 0 1 0 1 0 51/400 189/800 0
G 0 1 1 1 1 0 1 0 81/400 189/800 0
G 1 1 0 0 1 0 1 1/200 9/40 9/50 0
G 1 1 0 1 1 0 1 1/200 9/40 9/50 0
G 1 1 1 0 1 0 1 1/80 9/40 3/16 0
G 1 1 1 1 1 0 1 1/80 9/40 3/16 0
F 0 0 0 0 1 33/320 169/320 1027/25600 1653/12800 3747/25600 33/3200
F 0 0 0 1 526471/529825 236811/2119300 526471/529825 113841/8477200 99501/423860 46173/8477200 236811/21193000
F 0 0 1 0 1 177/1600 857/1600 5459/128000 8421/64000 19059/128000 177/16000
F 0 0 1 1 1 3/20 1 0 6/25 0 3/200
F 0 1 0 0 241/250 0 241/250 39/5000 2169/10000 5061/20000 0
F 0 1 0 1 1 3/25 1 21/4000 237/1000 543/2000 3/250
F 0 1 1 0 97/100 0 97/100 87/8000 873/4000 2037/8000 0
F 0 1 1 1 1 3/20 1 0 6/25 219/800 3/200
F 1 1 0 0 99/100 0 99/100 99/8000 891/4000 1519/8000 0
F 1 1 0 1 1 57/400 397/400 1879/32000 3801/16000 8679/32000 57/4000
F 1 1 1 0 1 0 1 1/80 9/40 3/16 0
F 1 1 1 1 1 3/20 1 49/800 6/25 219/800 3/200"""

Y={}
for row in CERT.strip().splitlines():
    chart,p,q,theta,lam,*nums=row.split()
    Y[chart,int(p),int(q),int(theta),int(lam)]=tuple(map(F,nums))
assert len(Y)==24

def src(t,p,q,theta,kappa):
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

def lawful(f):
    g,a,b,u,v,w,z=f
    assert 0<=a<=g<=1 and 0<=b<=g
    assert 0<=u<=F(13,40)*a+b/80
    assert 0<=w<=F(3,40)*a+F(21,80)*b
    assert 0<=z<=a/10 and 0<=v-z<=F(9,40)*b
    m=mass(f)
    assert len(m)==7 and all(mi>=0 for mi in m)
    assert sum(m)==1 and sum(ri*mi for ri,mi in zip(R,m))==1

def hng(f,k):
    return sum(max(ri-k,F(0))*mi for ri,mi in zip(R,mass(f)))

def check(x,y,chart):
    lawful(x); lawful(y)
    assert tp(x)==tp(y) and tq(x)==tq(y)
    assert all(hng(y,k)>=hng(x,k) for k in R[1:-1])
    if chart=="G": assert y[1]==y[6]==0
    elif chart=="F": assert y[6]==y[1]/10 and y[4]-y[6]==F(9,40)*y[2]
    else: raise ValueError(chart)
    assert 9*y[2]*y[6]==4*y[1]*(y[4]-y[6])

def tw(p,q):
    assert 0<=p<=q<=1
    return {(0,0):1-q,(0,1):q-p,(1,1):p}

def seam(t,p,q):
    return 1-(t/T)*(1-sum(w*S[k] for k,w in tw(p,q).items()))

def target(t,p,q,theta,kappa):
    assert 0<=t<=T and 0<=theta<=1 and 0<=kappa<=1
    h=seam(t,p,q)
    assert F(0)<=h<=1
    if h>0 and kappa<=h:
        chart="G"; lam=kappa/h
    else:
        chart="F"; lam=(kappa-h)/(1-h)
    v=[F(0)]*7
    weights=tw(p,q)
    for tv,(pv,qv),th,lv in product((0,1),CORNER,(0,1),(0,1)):
        weight=(t/T if tv else 1-t/T)*weights[pv,qv]*(
            theta if th else 1-theta)*(lam if lv else 1-lam)
        if tv:
            row=Y[chart,pv,qv,th,lv]
        else:
            row=src(F(0),F(pv),F(qv),F(th),F(lv) if chart=="G" else F(1))
        for j in range(7): v[j]+=weight*row[j]
    y=tuple(v)
    check(src(t,p,q,theta,kappa),y,chart)
    return chart,y

def main():
    n=0
    for chart,p,q,theta,lam in Y:
        s=S[p,q]
        k=F(lam)*s if chart=="G" else s+F(lam)*(1-s)
        check(src(T,F(p),F(q),F(theta),k),Y[chart,p,q,theta,lam],chart)
        n+=1
        x=src(F(0),F(p),F(q),F(theta),F(lam) if chart=="G" else F(1))
        check(x,x,chart);n+=1
    print("PASS_EXACT_24_NONTRIVIAL_PLUS_24_ZERO_ENDPOINTS",n)
    for i in range(201):
        t=T*F((17*i+3)%201,201)
        q=F((23*i+7)%201,201)
        p=q*F((29*i+11)%201,201)
        theta=F((31*i+13)%201,201)
        h=seam(t,p,q)
        k=h*F((37*i+17)%201,201) if i%2==0 else h+(1-h)*F((37*i+17)%201,201)
        target(t,p,q,theta,k)
    print("PASS_EXACT_201_INTERIOR_REGRESSIONS")
    for t in (F(0),T):
        for p,q in CORNER:
            for theta,kappa in product((F(0),F(1)),repeat=2):
                target(t,F(p),F(q),theta,kappa)
    print("PASS_EXACT_24_BOUNDARY_REGRESSIONS")
    print("THEOREM_ALL_REAL_T_LE_3_OVER_20_P_LE_Q_FULL_THETA_KAPPA")

if __name__=="__main__": main()
