#!/usr/bin/env python3
"""Exact R5 q-face threshold witness, independent Fraction checker.
Scientific inputs: frozen P/Q seven-node observer; does not use floating point.
"""
from fractions import Fraction as F
R = (F(1,10), F(1,2), F(3,4), F(1), F(5,4), F(3,2), F(19,10))
QSTAR = F(1343,1589)

def source(q):
    return (F(1), F(0), F(1), F(0), F(9,160), F(21,80)*q, F(0))

def target(g,a,b,u,w):
    z = F(3,40)*a
    return (g,a,b,u,z+F(27,160)*b,w,z)

def mass(f):
    g,a,b,u,v,w,z=f
    return (F(509,900)*u+F(47,180)*z+F(67,162)*(v-z)+w/100,
            F(13,40)*a+b/80-u, (g-a)/2,
            1-g+a/10+F(9,40)*b-v+F(191,450)*(u+w)
            +F(43,90)*z+F(14,81)*(v-z),
            (g-b)/2, F(3,40)*a+F(21,80)*b-w,
            u/100+F(47,180)*z+F(67,162)*(v-z)+F(509,900)*w)

def tp(f):
    g,a,b,u,v,w,z=f
    return 1+g+F(3,8)*a+F(5,8)*b+u/2+v+F(3,2)*w

def tq(f):
    g,a,b,u,v,w,z=f
    return 1+g+(a+b)/2+u+v+w

Y0 = (F(41738387,42475680),F(28151,530946),F(146812,265473),
      F(11395,471952),F(70389,471952))
Y1 = (F(209,227),F(0),F(209,227),F(0),F(4389,18160))
E0 = { (0,0):F(67,2880),(0,1):F(1,144),(0,2):F(23,936),
       (2,2):F(107,260),(2,3):F(905111,16990272),
       (3,1):F(1,180),(3,2):F(23,360),(3,3):F(1527587,21237840),
       (4,3):F(905111,16990272),(4,5):F(21,130),
       (6,5):F(21,208),(6,6):F(67,2880) }
E1 = { (0,0):F(208243,8172000),(0,1):F(7,720),(0,2):F(25717,817200),
       (1,3):F(209,18160),(2,2):F(87783,227000),
       (2,3):F(310691,5221000),(2,5):F(369,26105),
       (3,2):F(334321,4086000),(3,3):F(365083,2043000),
       (6,1):F(1,360),(6,3):F(23937,1044200),
       (6,5):F(1107,41768),(6,6):F(1215493,8172000) }

def verify(q, yvars, edges):
    x=source(q);y=target(*yvars)
    g,a,b,u,w=yvars
    assert 0<=a<=g<=1 and 0<=b<=g
    assert 0<=u<=F(13,40)*a+b/80 and 0<=w<=F(3,40)*a+F(21,80)*b
    assert 9*y[2]*y[6]==4*y[1]*(y[4]-y[6])
    mx,my=mass(x),mass(y)
    assert all(t>=0 for t in mx+my)
    assert sum(mx)==sum(my)==1
    assert sum(R[i]*mx[i] for i in range(7))==sum(R[i]*my[i] for i in range(7))==1
    assert all(v>=0 for v in edges.values())
    for i in range(7):
        assert sum(v for (k,j),v in edges.items() if k==i)==my[i]
    for j in range(7):
        assert sum(v for (i,k),v in edges.items() if k==j)==mx[j]
        assert sum(R[i]*v for (i,k),v in edges.items() if k==j)==R[j]*mx[j]
    assert tp(x)==tp(y) and tq(x)==tq(y)
    # Analytic stopping-time separator identity for every legal face target.
    L=350*(tq(y)-1)-309*(tp(y)-1)
    rhs=F(859,16)*a+F(391,2)*u+82*my[4]+F(227,2)*my[5]
    assert L==rhs>=0
    return (tp(x),tq(x),len(edges),L)

if __name__=='__main__':
    r0=verify(F(0),Y0,E0)
    r1=verify(QSTAR,Y1,E1)
    assert 350*(tq(source(QSTAR))-1)-309*(tp(source(QSTAR))-1)==0
    assert F(4029,4767)==QSTAR
    assert r1[3]==0
    for i in range(1001):
        q=QSTAR*F(i,1000)
        t=q/QSTAR
        v=tuple((1-t)*Y0[j]+t*Y1[j] for j in range(5))
        e={ij:(1-t)*E0.get(ij,F(0))+t*E1.get(ij,F(0)) for ij in E0.keys()|E1.keys()}
        verify(q,v,e)
    print('PASS_EXACT_ENDPOINTS',str(QSTAR),'Q0_EDGES',r0[2],'QSTAR_EDGES',r1[2])
    print('PASS_1001_EXACT_SEGMENT_CASES')
    print('PROVED_SHARP_FIXED_FACE_BOUND_q_LE_1343_1589_BY_SYMBOLIC_IDENTITY')
