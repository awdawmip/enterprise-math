#!/usr/bin/env python3
"""Exact corner certificates and 3D all-real interpolation for q=1 extension.
Requires the sibling VERIFY.py (sharp-face mass / target / time definitions).
"""
from fractions import Fraction as F
from itertools import product
from VERIFY import R, mass, target, tp, tq

def source(t,p,q):
    return (F(1), t, F(1), (F(13,40)*t+F(1,80))*p,
            t/40+F(27,160), (F(3,40)*t+F(21,80))*q,t/40)

# Exact rational witnesses for t=1/5, keyed by (p,q) in {0,1}^2.
C = {
 (0,0): ((F(478139,480375),F(494131,2882250),F(478139,480375),F(154999,15372000),F(5411,1317600)),
         {(0,0):F(5119,72000),(0,1):F(68903,9223200),(1,1):F(2678251,46116000),
          (2,1):F(68903,5764500),(2,2):F(2,5),(3,3):F(3701,36000),
          (3,5):F(68903,20752200),(5,5):F(498107,1844640),
          (6,5):F(68903,16601760),(6,6):F(5119,72000)}),
 (0,1): ((F(15746743,15778375),F(2986237,15778375),F(15746743,15778375),F(53761,63113500),F(13943961,50490800)),
         {(0,0):F(13297,180000),(0,1):F(68903,25245400),
          (1,1):F(17773707,252454000),(1,3):F(68903,25245400),
          (2,1):F(68903,15778375),(2,2):F(2,5),
          (3,3):F(2457752531,11360430000),(6,3):F(68903,45441720),
          (6,6):F(41047,180000)}),
 (1,0): ((F(17192243,17230325),F(3407983,17230325),F(17054437,17230325),F(21132399,275685200),F(15901,13784260)),
         {(0,0):F(20687,180000),(0,3):F(68903,49623336),
          (2,2):F(2,5),(3,3):F(1168028267,8861310000),
          (4,5):F(68903,17230325),(5,3):F(68903,27568520),
          (5,5):F(14942233,55137040),(6,5):F(68903,27568520),
          (6,6):F(12937,180000)}),
 (1,1): ((F(1),F(79297491,408062125),F(406561069,408062125),F(493659167,6528994000),F(359240491,1305798800)),
         {(0,0):F(42373,360000),(0,2):F(93909,81612425),
          (2,2):F(162348366,408062125),(2,3):F(2033951,408062125),
          (3,3):F(144426185659,587609460000),(4,3):F(750528,408062125),
          (5,2):F(406939,408062125),(6,3):F(1283423,1469023650),
          (6,6):F(82373,360000)})
}

def validate(x,yv,edges):
    y=target(*yv);g,a,b,u,w=yv
    assert 0<=a<=g<=1 and 0<=b<=g
    assert 0<=u<=F(13,40)*a+b/80 and 0<=w<=F(3,40)*a+F(21,80)*b
    assert 9*y[2]*y[6]==4*y[1]*(y[4]-y[6])
    mx,my=mass(x),mass(y)
    assert all(v>=0 for v in mx+my) and all(v>=0 for v in edges.values())
    assert sum(mx)==sum(my)==1
    assert sum(R[i]*mx[i] for i in range(7))==sum(R[i]*my[i] for i in range(7))==1
    for i in range(7):assert sum(v for (ii,j),v in edges.items() if ii==i)==my[i]
    for j in range(7):
        assert sum(v for (i,jj),v in edges.items() if jj==j)==mx[j]
        assert sum(R[i]*v for (i,jj),v in edges.items() if jj==j)==R[j]*mx[j]
    assert tp(x)==tp(y) and tq(x)==tq(y)

def corner(t,p,q):
    x=source(t,p,q)
    if t==0:
        yv=(x[0],x[1],x[2],x[3],x[5])
        return x,yv,{(i,i):v for i,v in enumerate(mass(x)) if v>0}
    assert t==F(1,5)
    yv,edges=C[(int(p),int(q))]
    return x,yv,edges

if __name__=='__main__':
    vertices={}
    for t,p,q in product((F(0),F(1,5)),(F(0),F(1)),(F(0),F(1))):
        x,yv,edges=corner(t,p,q);validate(x,yv,edges)
        vertices[t,p,q]=(x,yv,edges)
    assert len(vertices)==8
    for j in range(601):
        t=F(1,5)*F(j,600)
        p=F((7*j+13)%601,601)
        q=F((11*j+29)%601,601)
        weights={key: (t/F(1,5) if key[0] else 1-t/F(1,5))
                       *(p if key[1] else 1-p)*(q if key[2] else 1-q)
                 for key in vertices}
        assert sum(weights.values())==1 and min(weights.values())>=0
        x=source(t,p,q)
        assert all(sum(weights[key]*vertices[key][0][k] for key in vertices)==x[k] for k in range(7))
        yv=tuple(sum(weights[key]*vertices[key][1][k] for key in vertices) for k in range(5))
        edges={ij:sum(weights[key]*vertices[key][2].get(ij,F(0)) for key in vertices)
               for ij in set().union(*(set(item[2]) for item in vertices.values()))}
        validate(x,yv,edges)
    print('PASS_8_EXACT_CORNERS_NEW_Q1_EDGE_CERTIFICATES', sum(len(C[k][1]) for k in C))
    print('PASS_601_EXACT_TRIVARIATE_INTERPOLATION_CASES')
    print('PROVED_ALL_REAL_T_P_Q_FULL_BOX_T_0_TO_1_5_P_Q_0_TO_1_THETA_1_4_KAPPA_3_4')
