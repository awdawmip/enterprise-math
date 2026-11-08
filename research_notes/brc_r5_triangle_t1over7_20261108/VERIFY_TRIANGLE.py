#!/usr/bin/env python3
"""Independent exact R5 triangular-p/q Blackwell certificate. Python stdlib only."""
from fractions import Fraction as F
from itertools import product

T=F(1,7)
R=tuple(map(F,("1/10","1/2","3/4","1","5/4","3/2","19/10")))
CORNER=((0,0),(0,1),(1,1))
S={(0,0):F(1,4),(0,1):F(1,3),(1,1):F(1,50)}
CERT = """G 0 0 0 0 19/20 0 6/7 0 27/140 0 0
G 0 0 0 1 1 0 943/1092 1/624 2829/14560 0 0
G 0 0 1 0 27/28 0 6/7 0 27/140 0 0
G 0 0 1 1 1 0 137/156 23/4368 411/2080 0 0
G 0 1 0 0 39/41 0 39/41 0 193/1148 819/3280 0
G 0 1 0 1 401/413 0 401/413 0 3609/16520 8087/33040 0
G 0 1 1 0 1 0 1 0 17/140 19/80 0
G 0 1 1 1 1 0 1 0 11/56 19/80 0
G 1 1 0 0 1 0 1 0 9/40 5/28 0
G 1 1 0 1 1 0 1 9/4000 9/40 5063/28000 0
G 1 1 1 0 1 0 1 1/140 9/40 13/70 0
G 1 1 1 1 1 0 1 263/28000 9/40 5263/28000 0
F 0 0 0 0 1 223/2240 169/320 6981/179200 11539/89600 26181/179200 223/22400
F 0 0 0 1 737283/741755 78937/741755 737283/741755 5421/423860 1390259/5934040 15391/2967020 78937/7417550
F 0 0 1 0 1 239/2240 1199/2240 1059/25600 11747/89600 26613/179200 239/22400
F 0 0 1 1 1 1/7 1 0 67/280 0 1/70
F 0 1 0 0 337/350 0 337/350 167/28000 3033/14000 1011/4000 0
F 0 1 0 1 1 4/35 1 1/200 331/1400 759/2800 2/175
F 0 1 1 0 339/350 0 339/350 249/28000 3051/14000 1017/4000 0
F 0 1 1 1 1 1/7 1 0 67/280 153/560 1/70
F 1 1 0 0 2959/3000 0 2959/3000 2959/240000 8877/40000 326453/1680000 0
F 1 1 0 1 1 19/140 139/140 633/11200 1327/5600 3033/11200 19/1400
F 1 1 1 0 6971/7000 0 6971/7000 6971/560000 62739/280000 107551/560000 0
F 1 1 1 1 1 1/7 1 33/560 67/280 153/560 1/70"""

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
    assert S[(1,1)]<=h<=1
    if kappa<=h:
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
    print("THEOREM_ALL_REAL_T_LE_1_OVER_7_P_LE_Q_FULL_THETA_KAPPA")

if __name__=="__main__": main()
