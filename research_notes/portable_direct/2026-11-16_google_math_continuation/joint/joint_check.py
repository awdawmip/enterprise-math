"""Symbolic differentiation and exact finite cross-checks at scaled mixed errors."""
from fractions import Fraction as F
from itertools import product
import sympy as s
x,D,E=s.symbols('x D E')
f=(E*x**3-D*x**4)/(6*(x**5+D))
b=-4*(D**5-121*D**4+70*D**3*E+381*D**3-365*D**2*E-121*D**2+185*D*E+D-5*E)/(1+D)**5
assert s.factor(s.diff(f,x,4).subs(x,1)-b)==0
assert s.factor(s.diff(b,E)+4*(70*D**3-365*D**2+185*D-5)/(1+D)**5)==0
MAX=12012
cc=[1]+[0]*MAX
for w in [1,1,1,2,3,6]:
    for j in range(w,len(cc)):cc[j]+=cc[j-w]
C=[0]+cc
T=[0]*len(C)
for j in range(1,len(C)):T[j]=T[j-1]+C[j-1]
P=(20,20,20,-100,140,-100)
def obs(r,e,d):
    y=[]
    for q in range(r,r+7):
        poly=F(q**4,6)+F(q**3,2)-F(115*q*q,36)+F(115*q,6)-F(16315,108)
        y.append(F(q**3*(T[q]+e),C[q]+d)-poly)
    return [sum(w*x for w,x in zip((1,-4,6,-4,1),y[j:])) for j in range(3)]
def asym(r,e,d):
    uv=F(25920*e,r**6);v=F(4320*d,r**5)
    a=(1+uv)/(1+v)**2
    f=-4*(v**5-121*v**4+70*v**3*uv+381*v**3-365*v**2*uv-121*v**2+185*v*uv+v-5*uv)/(1+v)**5
    return [a*P[(r+j)%6]+f for j in range(3)]
for D0,E0 in [(F(-1,6),F(-1,3)),(F(1,4),F(1,5)),(F(0),F(-1,2)),(F(0),F(0))]:
    errors=[]
    for r0 in (120,1200,12000):
        largest=0
        for r in range(r0,r0+6):
            e=E0*r**6//25920;d=D0*r**5//4320
            real=obs(r,e,d)
            approx=asym(r,e,d)
            largest=max(largest,max(abs(v-u) for v,u in zip(real,approx)))
        errors.append(float(largest))
    print('scaled target D,E',D0,E0,'max actual 3-coordinate errors, all 6 phases:',errors)
    assert errors[2]<errors[1]/5<errors[0]/25
print('PASS symbolic derivative and finite convergence cross-checks')
