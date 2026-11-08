#!/usr/bin/env python3
"""Exact Fraction verifier for R5 two-chart full-p/q low-ratio prism.
The real-parameter proof is in RESEARCH.md; arithmetic checks its 64 vertices.
"""
from fractions import Fraction as F
from itertools import product

R=tuple(map(F,('1/10','1/2','3/4','1','5/4','3/2','19/10')))
T=F(1,50)
S={(0,0):F(3,4),(1,0):F(3,4),(0,1):F(9,10),(1,1):F(4,5)}
CERT="""G 0 0 0 0 613919/621645 0 613919/621645 613919/49731600 6057/1036075 519781/49731600 0
G 0 0 0 1 613919/621645 0 613919/621645 613919/49731600 5788629/33154400 519781/49731600 0
F 0 0 0 0 1518713/1726500 526133/6906000 1518713/1726500 658477/18416000 283891/1381200 1471251/18416000 526133/69060000
F 0 0 0 1 2646889/2649125 78937/5298250 2646889/2649125 37947/21193000 191839/847720 15391/21193000 78937/52982500
G 0 0 1 0 614413/621645 0 614413/621645 614413/49731600 35397/5180375 102079/9946320 0
G 0 0 1 1 614413/621645 0 614413/621645 614413/49731600 29106729/165772000 102079/9946320 0
F 0 0 1 0 7616237/8632500 2586017/34530000 7616237/8632500 3256713/92080000 1422643/6906000 7230359/92080000 2586017/345300000
F 0 0 1 1 1 1/50 1 0 227/1000 0 1/500
G 0 1 0 0 1 0 1 7/2000 1/125 21/80 0
G 0 1 0 1 1 0 1 7/2000 421/2000 21/80 0
F 0 1 0 0 587/590 0 587/590 0 5283/23600 3839/14750 0
F 0 1 0 1 1 2/125 1 7/10000 1133/5000 2637/10000 1/625
G 0 1 1 0 1 0 1 7/2000 1/100 21/80 0
G 0 1 1 1 1 0 1 7/2000 17/80 21/80 0
F 0 1 1 0 2939/2950 0 2939/2950 0 26451/118000 1917/7375 0
F 0 1 1 1 1 1/50 1 0 227/1000 33/125 1/500
G 1 0 0 0 1 0 452/475 113/9500 157/3800 0 0
G 1 0 0 1 1 0 452/475 113/9500 3193/15200 0 0
F 1 0 0 0 7509053/8632500 3843473/34530000 7509053/8632500 4332217/92080000 1428499/6906000 7680471/92080000 3843473/345300000
F 1 0 0 1 4657286/4664625 428399/18658500 4640369/4664625 186721/9951200 1054793/4664625 89743/49756000 428399/186585000
G 1 0 1 0 1 0 452/475 113/9500 823/19000 0 0
G 1 0 1 1 1 0 452/475 113/9500 16117/76000 0 0
F 1 0 1 0 100423/115100 50651/460400 100423/115100 859309/18416000 477229/2302000 302183/3683200 50651/4604000
F 1 0 1 1 1 1/50 1 19/1000 227/1000 0 1/500
G 1 1 0 0 1 0 1 1/80 7/250 101/400 0
G 1 1 0 1 1 0 1 1/80 26/125 101/400 0
F 1 1 0 0 1483/1500 0 1483/1500 1483/120000 4449/20000 30623/120000 0
F 1 1 0 1 164959/164975 6567/329950 164959/164975 59763/3299500 299553/1319800 1736281/6599000 6567/3299500
G 1 1 1 0 1 0 1 1/80 3/100 101/400 0
G 1 1 1 1 1 0 1 1/80 21/100 101/400 0
F 1 1 1 0 99/100 0 99/100 99/8000 891/4000 2039/8000 0
F 1 1 1 1 1 1/50 1 19/1000 227/1000 33/125 1/500"""
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
