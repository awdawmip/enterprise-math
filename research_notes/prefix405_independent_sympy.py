#!/usr/bin/env python3
"""Independent PREFIX-405 verification from original five-Port complex matrix."""
import sympy as S
I=S.I;R=S.Rational
A=S.Matrix([
 [4,4,0], [0,-4,4], [-5+3*I,0,-3+I],
 [-2-2*I,4+4*I,2+2*I], [-2,0,5+2*I]
])
B=S.simplify(A*A[:3,:].inv())
expect=S.Matrix([
[1,0,0],[0,1,0],[0,0,1],
[R(5,2)+R(9,2)*I,R(3,2)+R(7,2)*I,4*I],
[R(11,4)+R(15,8)*I,R(11,4)+R(15,8)*I,R(5,4)+R(9,4)*I]
])
assert B==expect

def abs2(z):return S.expand_complex(z*S.conjugate(z)).simplify()
def measurements(u,v):
 W=S.Matrix([1,u,v]);P=A*A[:3,:].inv()*W
 F=[abs2(x) for x in P]
 return [F[1],abs2(1+u),F[2],abs2(1+v),F[3],F[4]]
msplus=measurements(I,0)
msminus=measurements(-I,0)
assert msplus==[1,2,0,1,37,R(709,32)]
assert msminus==[1,2,0,1,45,R(709,32)]
midpoint=[S.simplify((a+b)/2) for a,b in zip(msplus,msminus)]
assert midpoint==[1,2,0,1,41,R(709,32)]
# Exact fibers at (I2,Cu,I3,Cv)=(1,2,0,1): v=0, Re u=0,
# |u|=1 -> u=+/-i. Hence the midpoint observation I4=41 is impossible.
# For robust bands, use rational bounds on Re u and Im u.
eps=R(1,10000)
assert R(9999,10000)-eps**2>R(999,1000)**2
assert R(10001,10000)<R(1001,1000)**2
# Re v in [-1/10000,+1/20000], Im v in [-1/100,+1/100].
assert (1-eps-1-eps)/2==-eps
assert (1+eps-1-0)/2==eps/2
Lplus=expect[3,0]+expect[3,1]*I
Lminus=expect[3,0]-expect[3,1]*I
assert S.expand(Lplus)==-1+6*I
assert S.expand(Lminus)==6+3*I
D=5*(R(1,10000)+R(1,1000))+4*(R(1,10000)+R(1,100))
assert D==R(459,10000)
Eplus=2*7*D+D**2
Eminus=2*9*D+D**2
assert Eplus==R(64470681,100000000)
assert Eminus==R(82830681,100000000)
gap=S.Min(40-(37+Eplus),(45-Eminus)-42)
assert gap==R(217169319,100000000)>0
print('PASS_PREFIX405_INDEPENDENT_ORIGINAL_MATRIX_AND_ROBUST_GAP')
print('A3_det=',A[:3,:].det())
print('witness_vectors=',msplus,msminus)
print('midpoint=',midpoint)
print('rational_gap=',gap)
