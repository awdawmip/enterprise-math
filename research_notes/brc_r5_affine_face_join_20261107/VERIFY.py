#!/usr/bin/env python3
"""R5: exact Blackwell lifting for a two-parameter FULL_HIST side-flow rectangle."""
from fractions import Fraction as F
from itertools import product
R=(F(1,10),F(1,2),F(3,4),F(1),F(5,4),F(3,2),F(19,10))
Z=F(0); O=F(1); U=F(27,80)

def masses(x):
    g,a,b,u,v,w,z=x
    c0=F(13,40)*a+b/80
    c1=a/10+F(9,40)*b
    c2=F(3,40)*a+F(21,80)*b
    return (F(509,900)*u+F(47,180)*z+F(67,162)*(v-z)+w/100,
            c0-u,(g-a)/2,
            1-g+c1-v+F(191,450)*(u+w)+F(43,90)*z+F(14,81)*(v-z),
            (g-b)/2,c2-w,
            u/100+F(47,180)*z+F(67,162)*(v-z)+F(509,900)*w)

def times(x):
    g,a,b,u,v,w,z=x
    return (1+g+F(3,8)*a+F(5,8)*b+u/2+v+F(3,2)*w,
            1+g+(a+b)/2+u+v+w)

def legal(x):
    g,a,b,u,v,w,z=x
    return (0<=a<=g<=1 and 0<=b<=g and
            0<=u<=F(13,40)*a+b/80 and
            0<=w<=F(3,40)*a+F(21,80)*b and
            0<=z<=a/10 and 0<=v-z<=F(9,40)*b)

def seedless(x):
    g,a,b,u,v,w,z=x
    return 9*b*z==4*a*(v-z)

def qmatrix(entries):
    q=[[Z for _ in R] for _ in R]
    for i,j,num,den in entries:
        q[i][j]=F(num,den)
    return q

# Corners ordered (u/U,w/U)=(0,0),(1,0),(0,1),(1,1).
XS=[(O,O,O,p*U,F(9,40),q*U,Z) for p,q in [(0,0),(1,0),(0,1),(1,1)]]
YS=[
 (O,F(9,10),F(9,10),F(13,800),F(117,400),F(13,800),F(9,100)),
 (F(686,705),F(686,705),F(659,705),F(1233,3760),F(347,1128),Z,F(343,3525)),
 (O,F(4,5),O,F(7,200),F(61,200),F(129,400),F(2,25)),
 (O,F(14,15),O,F(379,1200),F(191,600),F(359,1200),F(7,75))]
QS=[
 qmatrix([(0,0,67,720),(0,1,8477,360000),(1,1,23,80),
          (2,1,1523,100000),(2,3,3477,100000),(3,1,20201,1800000),
          (3,3,31207,450000),(3,5,20201,1800000),
          (4,3,3477,100000),(4,5,1523,100000),(5,5,23,80),
          (6,5,8477,360000),(6,6,67,720)]),
 qmatrix([(0,0,20443,72000),(0,3,9977,1184400),(0,5,16277,2961000),
          (3,3,421271,1692000),(4,3,9,470),(5,3,3677,658000),
          (5,5,102899,329000),(6,5,16277,846000),(6,6,6943,72000)]),
 qmatrix([(0,0,6943,72000),(0,1,76,1875),(1,1,19,80),
          (2,1,169,3125),(2,3,287,6250),(3,1,101,18750),
          (3,3,67039,300000),(6,3,287,22500),(6,6,20443,72000)]),
 qmatrix([(0,0,10343,36000),(0,3,22,1875),(2,3,1,30),
          (3,3,93019,270000),(5,3,1,30),
          (6,3,167,67500),(6,6,10343,36000)])]

def check(x,y,Q):
    assert legal(x) and legal(y) and seedless(y)
    assert times(x)==times(y)
    mx,my=masses(x),masses(y)
    assert sum(mx)==sum(my)==O
    assert sum(r*m for r,m in zip(R,mx))==sum(r*m for r,m in zip(R,my))==O
    assert all(v>=0 for row in Q for v in row)
    for i in range(7):assert sum(Q[i])==my[i]
    for j in range(7):
        assert sum(Q[i][j] for i in range(7))==mx[j]
        assert sum(R[i]*Q[i][j] for i in range(7))==R[j]*mx[j]
    return [[Q[i][j]/my[i] if my[i] else (O if i==j else Z)
             for j in range(7)] for i in range(7)]

for index,(x,y,Q) in enumerate(zip(XS,YS,QS)):
    K=check(x,y,Q)
    for d in product((Z,O),repeat=7):
        e=[sum(K[i][j]*d[j] for j in range(7)) for i in range(7)]
        assert all(0<=v<=1 for v in e)
        assert sum(masses(y)[i]*e[i] for i in range(7))==sum(masses(x)[i]*d[i] for i in range(7))
        assert sum(R[i]*masses(y)[i]*e[i] for i in range(7))==sum(R[i]*masses(x)[i]*d[i] for i in range(7))
    print('CORNER',index,'SOURCE_TIMES',times(x),'SEEDLESS',y,'TRANSPORT_EDGES',sum(bool(v) for row in Q for v in row),'PASS')

def interpolate(p,q):
    assert 0<=p<=1 and 0<=q<=1
    W=((1-p)*(1-q),p*(1-q),(1-p)*q,p*q)
    x=tuple(sum(W[k]*XS[k][j] for k in range(4)) for j in range(7))
    y=tuple(sum(W[k]*YS[k][j] for k in range(4)) for j in range(7))
    Q=[[sum(W[k]*QS[k][i][j] for k in range(4)) for j in range(7)] for i in range(7)]
    return x,y,Q

for p,q in product((Z,F(1,7),F(1,2),F(5,7),O),repeat=2):
    x,y,Q=interpolate(p,q)
    assert x==(O,O,O,p*U,F(9,40),q*U,Z)
    check(x,y,Q)
print('PASS_R5_FULL_TWO_PARAMETER_U_W_RECTANGLE_25_EXACT_RATIONAL_INTERPOLATIONS')
print('THEOREM: all real p,q in [0,1], all real d in [0,1]^7, by bilinear convex interpolation.')


# === NEW R5 AFFINE-FACE CONVEX JOIN (2026-11-07) ===
def _diag(stops):
    return [[stops[i] if i==j else Z for j in range(7)] for i in range(7)]

def _flow_mix(weights,flows):
    return tuple(sum(weights[k]*flows[k][j] for k in range(len(weights)))
                 for j in range(7))

def _q_mix(weights,matrices):
    return [[sum(weights[k]*matrices[k][i][j] for k in range(len(weights)))
             for j in range(7)] for i in range(7)]

def _in_face(f):
    g,a,b,u,v,w,z=f
    return legal(f) and z==a/10 and v-z==F(9,40)*b and seedless(f)

def _cone(g,s,p,q):
    weights=((1-g),(g-s),s*(1-p)*(1-q),s*p*(1-q),s*(1-p)*q,s*p*q)
    e0=(Z,)*7
    e1=(O,Z,Z,Z,Z,Z,Z)
    x=_flow_mix(weights,[e0,e1]+XS)
    y=_flow_mix(weights,[e0,e1]+YS)
    m=_q_mix(weights,[_diag(masses(e0)),_diag(masses(e1))]+QS)
    assert x==(g,s,s,U*s*p,F(9,40)*s,U*s*q,Z)
    assert _in_face(y)
    check(x,y,m)
    return x,y,m

def _face(g,a,b,ur,wr):
    return (g,a,b,ur*(F(13,40)*a+b/80),a/10+F(9,40)*b,
            wr*(F(3,40)*a+F(21,80)*b),a/10)

Gs=((Z,Z),(O,Z),(O,O),(F(2,3),F(1,3)),(O,F(3,5)),(O,F(1,2)))
Bs=(_face(O,Z,Z,Z,Z),_face(O,Z,Z,O,O),
    _face(O,F(1,2),F(3,4),F(1,3),F(2,3)),
    _face(F(4,5),F(3,5),F(1,5),Z,Z),
    _face(O,Z,Z,F(1,7),F(3,7)))
tests=0
for (g,s),p,q,t,f in product(Gs,(Z,F(1,3),O),(Z,F(2,5),O),
                            (Z,F(1,7),F(1,2),F(5,7),O),Bs):
    assert _in_face(f)
    x0,y0,q0=_cone(g,s,p,q)
    x=_flow_mix((1-t,t),(x0,f))
    y=_flow_mix((1-t,t),(y0,f))
    mat=_q_mix((1-t,t),(q0,_diag(masses(f))))
    assert _in_face(y)
    check(x,y,mat)
    tests+=1
assert tests==1350
print("CONVEX_JOIN_CERTIFICATES_PASS",tests)
x0,y0,q0=_cone(O,F(1,2),F(2,3),F(3,4))
f=_face(O,F(1,2),F(3,4),F(1,3),F(2,3))
t=F(2,5)
x=_flow_mix((1-t,t),(x0,f))
y=_flow_mix((1-t,t),(y0,f))
mat=_q_mix((1-t,t),(q0,_diag(masses(f))))
check(x,y,mat)
assert x[1]!=x[2] and x[6]>0 and x[3]>0 and x[5]>0
print("STRICT_OUTSIDE_OLD_CONE_SOURCE",list(map(str,x)))
print("MATCHED_STOP_TIMES",list(map(str,times(x))))
print("HISTORICAL_RESIDUAL",str(9*x[2]*x[6]-4*x[1]*(x[4]-x[6])))
print("PASS_R5_ALL_REAL_AFFINE_FACE_JOIN_THEOREM")
