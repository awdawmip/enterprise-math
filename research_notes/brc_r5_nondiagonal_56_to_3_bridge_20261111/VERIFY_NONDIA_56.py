#!/usr/bin/env python3
"""R5 frozen P/Q-BRC seven-LR auxiliary Blackwell observer.
Exact rational validation of non-diagonal minimal-5/6 families and 3-edge endpoint.
Frozen science GLOBAL a01383f825ef9d43b4b754254303298c64041568;
EM 86149263e38c22292c9def1e0f69092efa1be77e.
"""
from fractions import Fraction as F
r=tuple(F(t) for t in ('1/10','1/2','3/4','1','5/4','3/2','19/10'))
D=tuple((i,j) for j in (0,1,2,3,5,6) for i in range(7) if j not in (0,6) or i==j)

def mass(x):
    g,a,b,u,v,w,z=x
    return (F(509,900)*u+F(47,180)*z+F(67,162)*(v-z)+w/100,
            F(13,40)*a+b/80-u,(g-a)/2,
            1-g+a/10+F(9,40)*b-v+F(191,450)*(u+w)+F(43,90)*z+F(14,81)*(v-z),
            (g-b)/2,F(3,40)*a+F(21,80)*b-w,
            u/100+F(47,180)*z+F(67,162)*(v-z)+F(509,900)*w)

def times(x):
    g,a,b,u,v,w,z=x
    return (1+g+F(3,8)*a+F(5,8)*b+u/2+v+F(3,2)*w,
            1+g+(a+b)/2+u+v+w)

def slacks(x):
    g,a,b,u,v,w,z=x
    return (a,g-a,1-g,b,g-b,u,F(13,40)*a+b/80-u,
            w,F(3,40)*a+F(21,80)*b-w,z,a/10-z,v-z,z+F(9,40)*b-v)

def q21(x,y):
    m=mass(y);n=mass(x)
    return m+n+tuple(r[j]*n[j] for j in range(7))

def coupling21(E):
    out=[F(0)]*21
    for (i,j),weight in E.items():
        assert (i,j) in D and weight>=0
        out[i]+=weight;out[7+j]+=weight;out[14+j]+=r[i]*weight
    return tuple(out)

def state(s):
    c=F(247,4076)*s
    u=F(13,40)*s+F(1,80)
    w=F(3,40)*s+F(21,80)
    x=(F(1),s,F(1),u,F(0),w,F(0))
    y=(F(1),s,F(1),u-c,2*c,w-c,s/10)
    src,tar=mass(x),mass(y)
    E={(0,0):src[0],(1,3):c,(3,3):tar[3],(5,3):c,(6,6):src[6]}
    if s<1:E[(2,2)]=src[2]
    return x,y,E

def diagonal_endpoint():
    a=(F(1),F(1),F(1),F(27,80),F(1,10),F(27,80),F(1,10))
    m=mass(a)
    return a,a,{(0,0):m[0],(3,3):m[3],(6,6):m[6]}

def verify(x,y,E):
    assert x[0]==x[2] and y[0]==1 and y[6]==y[1]/10
    assert times(x)==times(y)
    assert all(q>=0 for q in slacks(x)+slacks(y))
    assert all(weight>0 for weight in E.values())
    assert coupling21(E)==q21(x,y)
    assert sum(E.values())==1
    assert len(D)==30

def blend(P,R,t):
    x,y,E=P; a,b,F0=R
    X=tuple((1-t)*v+t*w for v,w in zip(x,a))
    Y=tuple((1-t)*v+t*w for v,w in zip(y,b))
    arcs=set(E)|set(F0)
    W={arc:(1-t)*E.get(arc,F(0))+t*F0.get(arc,F(0)) for arc in arcs}
    return X,Y,{arc:value for arc,value in W.items() if value>0}

p3=diagonal_endpoint();verify(*p3)
print('P3_MASSES',tuple(str(x) for x in mass(p3[0])))
for s in (F(1,2),F(3,4),F(1)):
    p=state(s);verify(*p)
    x,y,E=p
    n=6 if s<1 else 5
    assert len(E)==n
    assert len([m for m in mass(y) if m>0])==n
    assert mass(x)[1]==mass(x)[5]==mass(x)[4]==0
    assert mass(y)[4]==0
    assert mass(x)[0]==mass(y)[0] and mass(x)[6]==mass(y)[6]
    assert mass(y)[1]==mass(y)[5]==F(247,4076)*s
    print('S',str(s),'SRC',','.join(map(str,x)),'TGT',','.join(map(str,y)))
    print('ARCS',','.join(f'{i}:{j}={v}' for (i,j),v in sorted(E.items())))
    print('TARGET_NONZERO',n,'MINIMAL_BY_TARGET_ROW_COUNT',n)
    for t in (F(0),F(1,4),F(1,2),F(3,4),F(1)):
        X,Y,W=blend(p,p3,t);verify(X,Y,W)
        expected=3 if t==1 else n
        assert len(W)==expected
        assert sum(v>0 for v in mass(Y))==expected
        print('BRIDGE',str(s),str(t),'NMIN',expected)
# Full 2D theorem uses exact affine/slack and bilinear interpolation identities;
# these endpoint/interior tests are not substituted for that proof.
print('PASS_EXACT_5_AND_6_NONDIA_MINIMA_AND_TWO_PARAMETER_3_EDGE_BRIDGES')
