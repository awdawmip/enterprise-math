#!/usr/bin/env python3
"""Independent symbolic check of PREFIX-401 from original five-Port complex matrix."""
import sympy as sp
I=sp.I
A=sp.Matrix([[4,4,0],[0,-4,4],[-5+3*I,0,-3+I],[-2-2*I,4+4*I,2+2*I],[-2,0,5+2*I]])
c,d=sp.symbols('c d',real=True)
w=sp.Matrix([1,sp.Rational(59,63),c+I*d]); Y=A[:3,:].inv()*w
ports=A*Y
sq=lambda x:sp.simplify(sp.expand_complex(x*sp.conjugate(x)))
T=245*c-123*d;S=123*c+245*d;N=75154
k=c*c+d*d
expected=[1,sp.Rational(3481,3969),k,sp.Rational(300616,3969)+16*k+sp.Rational(16,63)*T,sp.Rational(2638189,63504)+sp.Rational(53,8)*k+sp.Rational(61,504)*T]
assert all(sp.simplify(sq(ports[i])-expected[i])==0 for i in range(5))
assert sp.simplify(T*T+S*S-N*k)==0
C4=sp.Rational(37577,63); C5=sp.Rational(43249,63)
assert sp.simplify(expected[2]- (T*T+S*S)/N)==0
assert sp.simplify(expected[3]-sp.Rational(16,N)*((T+C4)**2+S*S))==0
assert sp.simplify(expected[4]-sp.Rational(53,8*N)*((T+C5)**2+S*S))==0
Cv=sp.simplify(sq(1+w[2])); assert sp.simplify(Cv-(1+k+sp.Rational(2,N)*(245*T+123*S)))==0
assert sp.simplify(Cv-((T+245)**2+(S+123)**2)/N)==0
for sig,ref in [(368,sp.Rational(5)),(-368,sp.Rational(97357,37577))]:
    cn=sp.Rational(245*122+123*sig,N)
    dn=sp.Rational(-123*122+245*sig,N)
    assert sp.simplify(Cv.subs({c:cn,d:dn})-ref)==0
    assert sp.simplify(k.subs({c:cn,d:dn})-2)==0
delta=sp.Rational(1,10);xi=delta
DT=sp.Rational(63,16)*xi+63*delta
minsigma2=N*(2-delta)-(122+DT)**2
assert minsigma2>355**2
DS=(N*delta+(244+DT)*DT)/(355+368)
H=delta+sp.Rational(2,N)*(245*DT+123*DS)
assert sp.Rational(90528,37577)-2-2*H==sp.Rational(4474780119,115917529600)>0
print('PASS_PREFIX401_INDEPENDENT_SYMPY_ORIGINAL_A_AND_BRANCHED_ANNULUS_BOUND')
