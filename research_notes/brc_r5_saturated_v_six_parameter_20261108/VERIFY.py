#!/usr/bin/env python3
"""R5 exact checker: six-parameter saturated-v Blackwell lift; no floats."""
from fractions import Fraction as F
from itertools import product
import BASE_CERTIFICATES as b

Z, ONE, R, U, W = b.Z, b.ONE, b.R, b.U, b.W
E0=(Z,)*7
E1=(ONE,Z,Z,Z,Z,Z,Z)

def diag(m):
    return tuple(tuple(m[i] if i==j else Z for j in range(7)) for i in range(7))

def mix(items):
    return tuple(sum(weight*value[k] for weight,value in items) for k in range(7))

def mix_matrix(items):
    return tuple(tuple(sum(weight*value[i][j] for weight,value in items)
                       for j in range(7)) for i in range(7))

def lift(g,s,p,q,theta,h):
    assert Z<=s<=g<=ONE and all(Z<=v<=ONE for v in (p,q,theta,h))
    weights={(0,0):(ONE-p)*(ONE-q),(1,0):p*(ONE-q),
             (0,1):(ONE-p)*q,(1,1):p*q}
    src=[(ONE-g,E0),(g-s,E1)]
    tgt=[(ONE-g,E0),(g-s,E1)]
    transfers=[(ONE-g,diag(b.mass(E0))),(g-s,diag(b.mass(E1)))]
    for ij,weight in weights.items():
        corner=b.source(U*ij[0],W*ij[1])
        positive=list(corner);positive[4]+=F(1,10);positive[6]+=F(1,10)
        positive=tuple(positive)
        assert b.legal(positive) and b.residual(positive)==Z
        src.extend(((s*weight*(ONE-theta),corner),(s*weight*theta,positive)))
        tgt.extend(((s*weight*(ONE-theta),b.TARGET[ij]),(s*weight*theta,positive)))
        transfers.extend(((s*weight*(ONE-theta),b.Q[ij]),
                          (s*weight*theta,diag(b.mass(positive)))))
    x=mix(src); y=mix(tgt); qq=mix_matrix(transfers)
    u=s*U*p; w=s*W*q; z=s*theta/10
    assert x==(g,s,s/2,u,F(9,80)*s+z,w,z)
    assert b.legal(x) and b.legal(y)
    assert b.residual(x)==F(9,2)*s*(z-s/10)
    assert y[6]==y[1]/10 and y[4]-y[6]==F(9,40)*y[2]
    assert b.residual(y)==Z
    assert b.times(x)==(ONE+g+F(4,5)*s+u/2+F(3,2)*w+z,
                       ONE+g+F(69,80)*s+u+w+z)
    b.check_transport(x,y,qq)
    xh=mix(((ONE-h,x),(h,y)))
    qh=mix_matrix(((ONE-h,qq),(h,diag(b.mass(y)))))
    b.check_transport(xh,y,qh)
    for d in ((Z,)*7,(ONE,)*7,(Z,F(1,7),F(2,7),F(1,2),F(5,7),F(6,7),ONE)):
        my=b.mass(y); mh=b.mass(xh)
        transformed=tuple(sum(qh[i][j]*d[j] for j in range(7))/my[i] if my[i] else Z
                          for i in range(7))
        assert all(Z<=v<=ONE for v in transformed)
        assert sum(my[i]*transformed[i] for i in range(7))==sum(mh[j]*d[j] for j in range(7))
        assert sum(R[i]*my[i]*transformed[i] for i in range(7))==sum(R[j]*mh[j]*d[j] for j in range(7))
    return x,y

N=0
for g in (Z,F(1,2),ONE):
    for s in (Z,g/2,g):
        for p,q,theta,h in product((Z,F(1,2),ONE),repeat=4):
            lift(g,s,p,q,theta,h)
            N+=1
assert N==729
print('PASS_729_EXACT_G_S_P_Q_THETA_H_GRID_CASES',N)
x,y=lift(ONE,ONE,ONE,ONE,F(1,2),Z)
print('WITNESS_SOURCE',','.join(map(str,x)))
print('WITNESS_TARGET',','.join(map(str,y)))
print('WITNESS_TIMES',','.join(map(str,b.times(x))))
print('WITNESS_RESIDUAL',b.residual(x))
print('FROZEN_SCIENCE_PINS global=a01383f825ef9d43b4b754254303298c64041568 EM=86149263e38c22292c9def1e0f69092efa1be77e')
print('PASS_R5_SATURATED_V_SIX_PARAMETER_ALL_REAL_AFFINE_FACE_LIFT')
