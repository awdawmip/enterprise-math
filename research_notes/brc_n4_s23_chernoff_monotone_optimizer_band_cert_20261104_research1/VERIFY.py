"""Audit analytic derivatives and exact rational enclosure constants.
Scientific domain: frozen S23, v=2h in (0,1/21].
SymPy checks are algebraic; mpmath diagnostics are illustrative, not universal proof.
"""
from fractions import Fraction as Q
import sympy as S
import mpmath as mp

x=S.symbols('x', positive=True)
psi=S.log(S.sqrt(1-x*x)*S.atanh(x)/x)
q=(S.atanh(x)-x)/(x*(1-x*x)*S.atanh(x))
assert S.simplify(S.diff(psi,x)+q)==0

# Exact rational Lipschitz and band loss coefficients at the maximal lawful contrast.
v=Q(1,21)
M=v*(3-2*v*v)/(3*(1-v*v)**3)
R=v**4*(3-2*v*v)**2/(72*(1-v*v)**8)
assert R==v*v*M*M/(8*(1-v*v)**2)
assert 0<M<Q(1,20)
assert 0<R<Q(1,1000000)
assert R*Q(1,10000)**2<Q(1,10**14)

mp.mp.dps=70
z=mp.mpf(1)/21
A=mp.atanh(z)
def ph(y):
    return mp.log(mp.sqrt(1-y*y)*mp.atanh(y)/y) if y else mp.mpf(0)
def delta(s):
    k=s/(2-s)
    return (ph(k*z)-ph(z))/(A+mp.atanh(k*z))
def deriv(s):
    k=s/(2-s);d=delta(s);D=A+mp.atanh(k*z)
    u=k*z
    qq=(mp.atanh(u)-u)/(u*(1-u*u)*mp.atanh(u)) if u else mp.mpf(0)
    return -2*z/(2-s)**2/D*(qq+d/(1-u*u))

for n in range(1,100):
    s=mp.mpf(n)/100
    d=delta(s)
    assert d>0 and d<mp.mpf(1)/125
    analytical=deriv(s)
    numeric=mp.diff(delta,s)
    assert analytical<0
    assert abs(analytical-numeric)<mp.mpf('1e-60')
    assert -analytical<mp.mpf(M.numerator)/M.denominator

# Envelope derivative: stationarity eliminates derivatives of the optimizer.
def c_B(s):
    k=s/(2-s);g=mp.atanh(k*z)
    X=s*mp.sqrt(1-z*z)/2
    Y=(2-s)*mp.sqrt(1-k*k*z*z)/2
    d=delta(s)
    return -mp.log(X*mp.exp(A*d)+Y*mp.exp(-g*d))
for n in range(1,100):
    s=mp.mpf(n)/100
    k=s/(2-s);g=mp.atanh(k*z);d=delta(s)
    kd=2/(2-s)**2
    predicted= -g/(A+g)/s + A/(A+g)*(1/(2-s)+(k*z*z+d*z)*kd/(1-k*k*z*z))
    assert abs(predicted-mp.diff(c_B,s))<mp.mpf('1e-60')

for s1,s2 in [(mp.mpf('0.1'),mp.mpf('0.11')),(mp.mpf('0.10243'),mp.mpf('0.10244'))]:
    mid=(delta(s1)+delta(s2))/2
    wid=delta(s1)-delta(s2)
    s=(s1+s2)/2;k=s/(2-s);c=mp.atanh(k*z)
    X=s*mp.sqrt(1-z*z)/2
    Y=(2-s)*mp.sqrt(1-k*k*z*z)/2
    Z=lambda d: X*mp.exp(A*d)+Y*mp.exp(-c*d)
    loss=mp.log(Z(mid)/Z(delta(s)))
    assert 0<=loss<=A*A*wid*wid/8
    bnd=mp.mpf(R.numerator)/R.denominator*(s2-s1)**2
    assert loss<=bnd

d0=-ph(z)/A
slope0=ph(z)*z/(2*A*A)
slope1=-(A-z)/((1-z*z)*A*A)
assert abs(mp.diff(delta,mp.mpf('0'))-slope0)<mp.mpf('1e-60')
assert abs(mp.diff(delta,mp.mpf('1'))-slope1)<mp.mpf('1e-60')
print('PASS_BRC_S23_CHERNOFF_OPTIMIZER_MONOTONE_BAND_CERT_20261104')
print('symbolic_identity=PASS, optimizer_derivative_grid=99, envelope_derivative_grid=99, band_examples=2')
print('rational_M=',M)
print('rational_R=',R)
print('one_1e-4_band_error_bound=',R*Q(1,10000)**2)
print('endpoint_slopes=',mp.nstr(slope0,20),mp.nstr(slope1,20))
