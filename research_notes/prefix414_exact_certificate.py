#!/usr/bin/env python3
"""PREFIX-414 exact independent author-side certificate, Python Fraction + SymPy.
All positivity assertions are exact rational / symbolic checks.
"""
from fractions import Fraction as F
from math import isqrt

B=F(37577,64)
E=F(53,8)
beta=F(1,10**6)
r=F(1,1000)
eta0=F(97,50000)
eta1=F(1,500)
eta2=F(239,10000)
assert eta0<eta1<eta2

# Regime I: fixed rational minus-source witness, valid already at eta0.
x=F(-97,100000); y=F(-119,500000)
t=x*x+y*y
h=2*x+t
k=F(61,8)*x-23*y+E*t
q_minus=-24*x+48*y-16*t
assert t<=beta and abs(h)<=eta0 and abs(k)<=eta0
assert B>F(24**2)
upper_plus_small=F(1165,576)*eta1+F(182,24)*r+16*beta
small_gap=q_minus-upper_plus_small
assert small_gap>0

# Regime II: Cauchy support of disk cut by one halfspace; eta up to eta2.
assert F(1165**2)*beta-F(2368)*eta2**2==F(114993,25000000)>0
assert eta2+E*beta<F(3,125) # .024
assert B*beta-F(3,125)**2>F(3,1000)**2
# S0=sqrt(B beta - eta**2), Sminus=sqrt(B beta-(eta+E beta)**2): both >.003.
# Exact uniform lower bound for B * (q_minus_candidate - q_plus_halfspace_upper)
regime2_numer=122*eta1+1287*E*beta-182*(2*eta2*E*beta+(E*beta)**2)/F(6,1000)-32*B*beta
assert regime2_numer>0
# Dropping positive 1287 E beta gives an even simpler certificate.
conservative=122*eta1-182*(2*eta2*E*beta+(E*beta)**2)/F(6,1000)-32*B*beta
assert conservative==F(41396037181,192000000000)>F(1,5)

# Regime III: one fixed rational minus witness dominates global plus maximum.
x2=F(-1,2500); y2=F(9,10000)
t2=x2*x2+y2*y2
h2=2*x2+t2
k2=F(61,8)*x2-23*y2+E*t2
q_minus2=-24*x2+48*y2-16*t2
assert t2==F(97,10**8)<beta
assert abs(h2)<eta2 and abs(k2)<eta2
assert 49**2>2368
upper_plus_global=F(49,1000)+16*beta
large_gap=q_minus2-upper_plus_global
assert large_gap>0

# Independent original Port matrix check: no reliance on the flattened coefficient source.
import sympy as s
I=s.I
A=s.Matrix([[4,4,0],[0,-4,4],[-5+3*I,0,-3+I],
            [-2-2*I,4+4*I,2+2*I],[-2,0,5+2*I]])
P=A[:3,:]
assert P.det()!=0
T=s.simplify(A*P.inv())
assert T[3,0]==s.Rational(5,2)+s.Rational(9,2)*I
assert T[3,1]==s.Rational(3,2)+s.Rational(7,2)*I
assert T[3,2]==4*I
assert T[4,0]==T[4,1]==s.Rational(22,8)+s.Rational(15,8)*I
assert T[4,2]==s.Rational(5,4)+s.Rational(9,4)*I

X,Y=s.symbols('X Y',real=True)
def I4_I5(sigma):
    vv=X+I*Y
    W=s.Matrix([1,sigma*I,vv]); Z=P.inv()*W; obs=A*Z
    squared=lambda a:s.expand_complex(a*s.conjugate(a)).expand().simplify()
    return squared(obs[3]),squared(obs[4])
for sig in [1,-1]:
    i4,i5=I4_I5(sig)
    tt=X*X+Y*Y
    if sig==1:
        expect_i4=37+48*X+8*Y+16*tt
        expect_i5=s.Rational(709,32)+23*X+s.Rational(61,8)*Y+s.Rational(53,8)*tt
    else:
        expect_i4=45+24*X-48*Y+16*tt
        expect_i5=s.Rational(709,32)+s.Rational(61,8)*X-23*Y+s.Rational(53,8)*tt
    assert s.simplify(i4-expect_i4)==0
    assert s.simplify(i5-expect_i5)==0

print('PASS_PREFIX414_NO_SECOND_CROSSING_EXACT_CERTIFICATE')
print('regime1_minus_source_t_h_k_q=',*(str(v) for v in (t,h,k,q_minus)))
print('regime1_positive_margin_gt=',small_gap)
print('regime2_B_times_positive_margin_gt=',conservative)
print('regime3_minus_source_t_h_k_q=',*(str(v) for v in (t2,h2,k2,q_minus2)))
print('regime3_positive_margin_gt=',large_gap)
print('matrix_check=exact_original_5x3_port_inversion')
