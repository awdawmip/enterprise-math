#!/usr/bin/env python3
"""Independent symbolic path-sum reconstruction of five LR policy observations."""
import itertools
import sympy as sp
from fractions import Fraction as F
qx={(0,0):F(3,8),(0,1):F(1,8),(1,0):F(1,8),(1,1):F(3,8)}
w={0:F(3,4),1:F(1,4)}
R={0:F(1,2),1:F(3,2)}
q={(x,u,v):z*(w[u] if v==0 else 1-w[u]) for (x,u),z in qx.items() for v in (0,1)}
p={k:q[k]*R[k[2]] for k in q}
a,b,d=sp.symbols("a b d",real=True)
c={(x,u,v):(a if (x,u,v)==(0,0,0) else -b if (x,u,v)==(1,0,0) else d if v==1 else 0) for x,u,v in q}
def rat(z): return sp.Rational(z.numerator,z.denominator)
def obs(bits):
    ep=eq=sp.Rational(1,2);tp=tq=0
    for x,u,v in q:
        s,h,z=bits[x],bits[2+u],bits[4+v]
        tm=2+s*(1+h*(2-z))
        ep+=rat(p[x,u,v])*s*h*z*c[x,u,v]
        eq+=rat(q[x,u,v])*s*h*z*c[x,u,v]
        tp+=rat(p[x,u,v])*tm
        tq+=rat(q[x,u,v])*tm
    return sp.Matrix([ep,eq,tp,tq])
bs=list(itertools.product((0,1),repeat=6))
vec=[obs(bs[i]) for i in (0,16,20,21,26)]
mat=sp.Matrix.hstack(*(z-vec[0] for z in vec[1:]))
det=sp.factor(mat.det())
print("matrix=",mat)
print("det symbolic=",det)
assert sp.simplify(det-sp.Rational(81,65536)*b*d)==0
print("at a=b=1/4,d=1/8",det.subs({a:sp.Rational(1,4),b:sp.Rational(1,4),d:sp.Rational(1,8)}))
print("PASS_SYMBOLIC_CROSSING_THREE_STOP_RANK4_DET")
