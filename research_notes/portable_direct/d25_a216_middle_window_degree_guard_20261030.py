"""Exact A216 middle-band finite-window Gosper degree checks.

The general degree lower bound and no-rational-identity proof are in companion
research note. These exact checks are finite witnesses, not a universal proof.
"""
from fractions import Fraction as Q
from math import factorial


def d(m, s):
    assert m >= 1 and 0 <= s < m
    return Q((-1)**(s+1)*factorial(3*m)*factorial(2*m)*factorial(4*m)
             *factorial(s)*factorial(m+s),
             6*2**(3*m+1+s)*factorial(3*m+1+s)**3*factorial(m-1-s))


def a(m,s): return (s+1-m)*(s+1)*(s+m+1)
def b_prev(m,s): return 2*(s+3*m+1)**3
def weight(m,s): return 18*m+7+6*s


def exact_window(m):
    # A(m-1)=0 gives the terminal value. All B_prev(s) are nonzero.
    y=[Q(0)]*m
    y[m-1]=-Q(weight(m,m-1),b_prev(m,m-1))
    for s in range(m-2,-1,-1):
        y[s]=(a(m,s)*y[s+1]-weight(m,s))/b_prev(m,s)
    # Exact Newton forward differences yield the interpolation polynomial
    # Y(s)=sum_k Delta^k(y_0)*binom(s,k).
    row=y[:]; coefficients=[]
    while row:
        coefficients.append(row[0]);row=[row[i+1]-row[i] for i in range(len(row)-1)]
    degree=max(i for i,c in enumerate(coefficients) if c)
    for s in range(m):
        # Check source-faithful two-term operator, with A(m-1)=0.
        lhs=a(m,s)*(y[s+1] if s<m-1 else Q(0))-b_prev(m,s)*y[s]
        assert lhs==weight(m,s)
        if s<m-1:
            assert d(m,s+1)/d(m,s)==Q(a(m,s),2*(s+3*m+2)**3)
    assert degree>=m-3 and degree<=m-1
    assert min(m-1,-1,-m-1)>-3*m-2  # A vs B(s+h), all h>=0
    return degree


for m in range(1,17):
    degree=exact_window(m)
    print('EXACT_ORIGINAL_A216_WINDOW', 'm',m,'degree',degree,'bound',[max(0,m-3),m-1])
print('PASS_16_EXACT_FRACTION_WINDOWS; NO_GOSPER_RATIONAL_IDENTITY_PROOF_BY_POLE_AND_DEGREE')
print('NO_NATIVE_H0_B0_EXECUTION; NO_SOURCE_RESULT_ADMISSION')

# Source-typed endpoint re-evaluation, including fixed p=373 (m=62).
# This arithmetic is the A216 middle valuation-two scalar, NOT native H0/B0.
def endpoint_scalar(m):
    y=[Q(0)]*m
    y[-1]=-Q(weight(m,m-1),b_prev(m,m-1))
    for s in range(m-2,-1,-1):
        y[s]=(a(m,s)*y[s+1]-weight(m,s))/b_prev(m,s)
    boundary=-d(m,0)*b_prev(m,0)*y[0]
    direct=sum((weight(m,s)*d(m,s) for s in range(m)),Q(0))
    assert direct==boundary
    p=6*m+1
    assert boundary.denominator%p
    return (boundary.numerator*pow(boundary.denominator,-1,p))%p

for m,expected in ((2,10),(3,9),(62,266)):
    result=endpoint_scalar(m)
    assert result==expected
    print('EXACT_MIDDLE_SCALAR_ENDPOINT', 'p',6*m+1,'source',result)
assert exact_window(62)==61
print('PASS_P373_EXACT_FRACTION_WINDOW_DEGREE_61_AND_MIDDLE_SOURCE_266')
