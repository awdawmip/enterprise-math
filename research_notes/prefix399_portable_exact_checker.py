#!/usr/bin/env python3
"""PREFIX-399 exact singular two-source fiber; SymPy 1.14; not a CAD engine."""
import sympy as s
I=s.I
A=s.Matrix([[4,4,0],[0,-4,4],[-5+3*I,0,-3+I],
            [-2-2*I,4+4*I,2+2*I],[-2,0,5+2*I]])
A3=A[:3,:]
assert A3.det()==-32+32*I
B=s.simplify(A*A3.inv())
assert B[:3,:]==s.eye(3)
c,d=s.symbols('c d',real=True)
r=s.Rational(59,63)
v=c+I*d
W=s.Matrix([1,r,v])
def sq(t):
    z=s.expand_complex(t)
    return s.expand(s.re(z)**2+s.im(z)**2)
P=[sq(z) for z in B*W]
N=75154
T=245*c-123*d
S=123*c+245*d
K4=s.Rational(300616,3969)
K5=s.Rational(2638189,63504)
k=c*c+d*d
assert P[0]==1 and P[1]==s.Rational(3481,3969) and P[2]==k
assert s.expand(P[3]-K4-16*k-s.Rational(16,63)*T)==0
assert s.expand(P[4]-K5-s.Rational(53,8)*k-s.Rational(61,504)*T)==0
assert s.expand(T*T+S*S-N*k)==0
M=s.Matrix([[22448,-30135],[-30135,-22448]])/37577
assert M*M==s.eye(2) and M.det()==-1
vp=M*s.Matrix([c,d])
assert s.expand((245*vp[0]-123*vp[1])-T)==0
assert s.expand((123*vp[0]+245*vp[1])+S)==0
for a in P:
    assert s.expand(a.subs({c:vp[0],d:vp[1]}, simultaneous=True)-a)==0
v1=(s.Integer(1),s.Integer(1))
v2=tuple(s.factor(z.subs({c:1,d:1})) for z in vp)
assert v2==(-s.Rational(7687,37577),-s.Rational(52583,37577))
vals=tuple(s.factor(a.subs({c:1,d:1})) for a in P)
assert vals==(1,s.Rational(3481,3969),2,s.Rational(550600,3969),s.Rational(4417309,63504))
cv1=(1+v1[0])**2+v1[1]**2
cv2=(1+v2[0])**2+v2[1]**2
assert (cv1,cv2)==(5,s.Rational(97357,37577))
assert (cv1-cv2)/2==s.Rational(45264,37577)
print('PASS_PREFIX399_SINGULAR_TWO_SOURCE_COMPLETE_FIBER')
print('PASS_PREFIX399_EXACT_OBSERVER_REPAIR_GAP')
print('observations',list(map(str,vals))+[str((1+r)**2)])
print('v_plus',v1,'v_minus',v2,'Cv',cv1,cv2)
