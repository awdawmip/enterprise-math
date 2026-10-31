#!/usr/bin/env python3
"""PREFIX-402: exact author-side certificate for a noisy-u six-observer slice.

All decisive inequalities are rational.  SymPy is used to cross-check the
original complex Port matrix; the derived interval inequalities are algebraic.
"""
from fractions import Fraction as F
import json
import sympy as s

j=s.I
A=s.Matrix([[4,4,0],[0,-4,4],[-5+3*j,0,-3+j],[-2-2*j,4+4*j,2+2*j],[-2,0,5+2*j]])
A3=A[:3,:]
assert s.simplify(A3.det()-(-32+32*j))==0
B=s.simplify(A*A3.inv())
expected=s.Matrix([[1,0,0],[0,1,0],[0,0,1],
  [s.Rational(5,2)+s.Rational(9,2)*j,s.Rational(3,2)+s.Rational(7,2)*j,4*j],
  [s.Rational(11,4)+s.Rational(15,8)*j,s.Rational(11,4)+s.Rational(15,8)*j,s.Rational(5,4)+s.Rational(9,4)*j]])
assert B==expected

def sq(w):return s.simplify(s.expand_complex(w*s.conjugate(w)))
u0=s.Rational(59,63); N=s.Integer(75154)
c,d=s.symbols('c d',real=True)
v=c+j*d
T=245*c-123*d; S=123*c+245*d
I3=c*c+d*d
L4=B[3,0]+B[3,1]*u0+B[3,2]*v
L5=B[4,0]+B[4,1]*u0+B[4,2]*v
assert s.simplify(s.expand(sq(L4)-s.Rational(16,1)/N*((T+s.Rational(37577,63))**2+S**2)))==0
assert s.simplify(s.expand(sq(L5)-s.Rational(53,8)/N*((T+s.Rational(43249,63))**2+S**2)))==0
assert s.simplify(s.expand(sq(L4)-(16*I3+s.Rational(16,63)*T+s.Rational(300616,3969))))==0
assert s.simplify(s.expand(sq(1+v)-(1+I3+2*(245*T+123*S)/N)))==0

vp=1+j
vm=-s.Rational(7687,37577)-j*s.Rational(52583,37577)
assert (T.subs({c:1,d:1}),S.subs({c:1,d:1}))==(122,368)
assert (s.simplify(T.subs({c:s.re(vm),d:s.im(vm)})),s.simplify(S.subs({c:s.re(vm),d:s.im(vm)})))==(122,-368)
J4=s.Rational(550600,3969); J5=s.Rational(4417309,63504)
assert sq(L4.subs({c:1,d:1}))==sq(L4.subs({c:s.re(vm),d:s.im(vm)}))==J4
assert sq(L5.subs({c:1,d:1}))==sq(L5.subs({c:s.re(vm),d:s.im(vm)}))==J5
assert sq(1+vp)==5 and sq(1+vm)==s.Rational(97357,37577)

def f(z):return F(int(s.numer(z)),int(s.denom(z)))
EPS=F(1,10**8); RHO=F(1,5000)
assert (1+2*f(u0))*EPS < RHO**2
assert sq(B[3,0]+B[3,1]*u0)<81 and sq(B[3,1])<16 and sq(B[3,2])==16
assert sq(B[4,0]+B[4,1]*u0)<49 and sq(B[4,1])<16 and sq(B[4,2])<9
assert 120*RHO+16*RHO**2 < F(1,40)
assert 96*RHO+16*RHO**2 < F(1,50)

DELTA=F(1,10); XI4_EFF=F(1,8); ETA=F(1,1)
DT=F(63,16)*XI4_EFF+63*DELTA
S2_LOWER=F(75154)*(2-DELTA)-(122+DT)**2
assert S2_LOWER>355**2
DS=(F(75154)*DELTA+(244+DT)*DT)/(355+368)
H=DELTA+F(2,75154)*(245*DT+123*DS)
NOMINAL_CV_GAP=F(90528,37577)
SEPARATION=NOMINAL_CV_GAP-2*(H+ETA)
assert SEPARATION>0

# Exact false-negative example: genuine u is not the frozen nominal real u0.
h=s.Rational(1,10000); uh=u0+j*h
assert sq(uh)-sq(u0)==h*h and sq(1+uh)-sq(1+u0)==h*h
Y=A3.inv()*s.Matrix([1,uh,vp])
ports=[sq((A*Y)[i]) for i in range(5)]
assert ports[:3]==[1,sq(uh),2]
assert ports[3]==sq(B[3,0]+B[3,1]*uh+B[3,2]*vp)
assert ports[4]==sq(B[4,0]+B[4,1]*uh+B[4,2]*vp)
i4h=ports[3]
i4plus=sq(B[3,0]+B[3,1]*u0+B[3,2]*vp)
i4minus=sq(B[3,0]+B[3,1]*u0+B[3,2]*(1-j))
assert i4h!=i4plus and i4h!=i4minus
assert sq(1+vp)==5
assert s.simplify(i4h-i4plus)==s.Rational(720029,200000000)
assert s.simplify(i4h-i4minus)==-s.Rational(262384879391,4200000000)

out={
 'status':'PASS_PREFIX402_TWO_NOISY_U_OBSERVERS_SHARP_SQRT_AND_BRANCH_SEPARATION',
 'source':'original A, six scalar outputs, exact I1=1',
 'epsilon_I2_Cu':str(EPS), 'rho_u':str(RHO),
 'additional_I4':str(F(1,40)), 'additional_I5':str(F(1,50)),
 'DT':str(DT),'S_squared_lower':str(S2_LOWER),
 'DS':str(DS),'H_Cv_true':str(H),'nominal_Cv_gap':str(NOMINAL_CV_GAP),
 'joint_observed_branch_separation':str(SEPARATION),
 'frozen_u_false_negative':{'h':str(h),'I4_actual':str(i4h),'difference_from_u0_vplus':str(i4h-i4plus),'difference_from_u0_vminus':str(i4h-i4minus)},
 'symbolic_original_A_crosscheck':True,
 'scope':'I1 exact; independent I2,Cu errors 1e-8; I3,I4,I5 errors 0.1; Cv error 1; auxiliary static model only'
}
print(json.dumps(out,ensure_ascii=False,indent=2))
