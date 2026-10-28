from fractions import Fraction as F
from itertools import product
Z=F(0); I=F(1)
def add(a,b): return tuple(x+y for x,y in zip(a,b))
def scale(s,a): return tuple(s*x for x in a)
def sub(a,b): return add(a,scale(-I,b))
def det(a,b,c):
    return a[0]*(b[1]*c[2]-b[2]*c[1])-b[0]*(a[1]*c[2]-a[2]*c[1])+c[0]*(a[1]*b[2]-a[2]*b[1])
def O(x,y,z=Z):
    # External P/Q branch carrier: (Q mass, LR, stop time, Pr[declare Q]).
    events=[(F(1,3),F(1,4),2,I-z),(F(1,4),F(2),2,Z),
       (F(1,6)*(I-x),I,2,Z),(F(1,6)*x*(I-y),I,3,Z),
       (F(1,12)*x*y,F(1,2),4,I),(F(1,12)*x*y,F(3,2),4,Z),
       (F(1,4)*(I-y),I,3,Z),(F(1,8)*y,F(1,4),4,I),
       (F(1,8)*y,F(7,4),4,Z)]
    assert all(Z<=t<=I for t in (x,y,z))
    assert sum(q for q,r,t,d in events)==I
    assert sum(q*r for q,r,t,d in events)==I
    return (sum(q*r*d for q,r,t,d in events),sum(q*(I-d) for q,r,t,d in events),
            sum(q*r*t for q,r,t,d in events),sum(q*t for q,r,t,d in events))
parents=[(F(1,2),F(1,2)),(F(1,2),F(3,2))]
children=[[(F(1,6),I),(F(1,3),F(1,4))],[(F(1,4),I),(F(1,4),F(2))]]
for (q,r),cs in zip(parents,children):
    assert sum(a for a,b in cs)==q
    assert sum(a*b for a,b in cs)==q*r
assert all(a>0 and b>0 for cs in children for a,b in cs)
B00,B01,B10,B11=[O(F(x),F(y)) for x,y in ((0,0),(0,1),(1,0),(1,1))]
u=sub(B10,B00);v=sub(B01,B00);w=sub(add(B11,B00),add(B10,B01))
B=lambda x,y:add(B00,add(scale(x,u),add(scale(y,v),scale(x*y,w))))
for x,y in product((Z,F(1,5),F(1,2),F(4,5),I),repeat=2):
    assert O(x,y)==B(x,y)
    assert B(x,y)[2]==B(x,y)[3]
cols=lambda t:(t[0],t[1],t[3])
assert det(cols(u),cols(v),cols(w))==F(1,2304)
qU,rU=parents[0];qV,rV=parents[1];pU=qU*rU;pV=qV*rV
plus=(pU+2*pV,qU+2*qV)
minus=(2*pU+pV,2*qU+qV)
assert plus==(F(7,4),F(3,2)) and minus==(F(5,4),F(3,2))
assert plus[0]-plus[1]==F(1,4) and minus[0]-minus[1]==-F(1,4)
t=(-F(1,12),F(1,3),Z,Z)
for x,y,z in product((Z,F(1,2),I),repeat=3):
    assert O(x,y,z)==add(B(x,y),scale(z,t))
L=O(Z,Z,F(1,2))
assert L==(F(1,24),F(5,6),F(9,4),F(9,4))
assert u[1]==Z and v[1]==-F(1,8) and w[1]==-F(1,12)
assert L[1]-B00[1]==F(1,6)
jac=det(cols(add(u,scale(F(1,2),w))),cols(add(v,scale(F(1,2),w))),cols(t))
assert jac==-F(1,3456)
print("model: external strictly-positive six-leaf rational P/Q")
print("rank3 minor =",F(1,2304))
print("two LR time-contrast witnesses = +1/4, -1/4")
print("support gap for c*(0,0,1,-1) >= |c|/4")
print("LR-feasible off-patch point =",L)
print("restricted-patch supnorm distance >= 1/6")
print("terminal-leakage Jacobian =",jac)
print("ALL EXACT NORMAL-GATE AND TERMINAL-LEAKAGE CHECKS PASSED")
