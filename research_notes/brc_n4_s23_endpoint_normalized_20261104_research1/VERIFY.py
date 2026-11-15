"""Independent exact-rational audit for normalized BRC S23 cubic Chernoff proxy."""
from fractions import Fraction as Q
from math import isqrt

V = Q(1, 21)
R = 1 - V * V
# Explicit envelope of |e'(x)| / x^5 for x in [0,V].
K = Q(37, 15)/R + V*V/(5*R*R) + Q(1, 9)/(R*R*R)
assert K < 3
# Ratio |D*d3 - N| / ((1-k)*v^6); all component bounds are exact.
A = 3 + Q(14, 135) + 1/(15*R) + Q(14, 225)*V*V/R
assert A < Q(16, 5)
# Probability weight w<=s on interpolation: (21/40)/(1-21/(440*125)) <1.
W = Q(21, 40)/(1-Q(21, 440*125))
assert W < 1
# Maximum normalized information error, with its rational value.
ERR = 32*V**12/R**2
assert ERR < Q(1, 10**14)
assert Q(16,5) < 4
# Universal algebraic factor t/(1+t)^2 <=1/4, t in [0,1]
# equivalently 4t <= (1+t)^2, whose difference is (1-t)^2.
for j in range(1001):
    t=Q(j,1000)
    assert (1+t)**2-4*t == (1-t)**2

print('EXACT_K=',K)
print('EXACT_A=',A)
print('EXACT_W=',W)
print('EXACT_ERR=',ERR)
print('ERR_UPPER_1e-14=',ERR<Q(1,10**14))

# Independent high-precision examples: only audits computational behavior,
# and is not the proof of the universal bound.
try:
    import mpmath as mp
    mp.mp.dps = 100
    grid=[Q(j,1000) for j in (1,5,50,102,103,200,500,900,990,999)]
    vm=mp.mpf(1)/21
    def psi(x):
        if x == 0: return mp.mpf(0)
        return mp.log(mp.sqrt(1-x*x)*mp.atanh(x)/x)
    max_ratio=mp.mpf(0)
    for s in grid:
        sm=mp.mpf(s.numerator)/s.denominator
        k=sm/(2-sm)
        alpha=mp.atanh(vm); gamma=mp.atanh(k*vm)
        delta=(psi(k*vm)-psi(vm))/(alpha+gamma)
        d3=(1-k)*vm/6+(1-k)*(9*k*k+10*k+9)*vm**3/180
        X=sm*mp.sqrt(1-vm*vm)/2
        Y=(2-sm)*mp.sqrt(1-k*k*vm*vm)/2
        z=lambda d: X*mp.exp(alpha*d)+Y*mp.exp(-gamma*d)
        # minimize log Z; error is log Z(d3)-log Z(delta)
        gap=mp.log(z(d3)/z(delta))
        bound=mp.mpf(128)*sm*(1-sm)**2/(2-sm)**2*vm**12/(1-vm*vm)**2
        assert gap > -mp.mpf('1e-95') and gap <= bound
        assert abs(delta-d3) <= 4*(1-k)*vm**5
        norm=gap/(sm*(1-sm))
        max_ratio=max(norm,max_ratio)
    print('MPMATH_SAMPLE_COUNT=',len(grid))
    print('MPMATH_MAX_NORMALIZED_GAP=',mp.nstr(max_ratio,24))
except ImportError:
    print('MPMATH_SAMPLE_COUNT=UNAVAILABLE')
print('PASS_BRC_S23_ENDPOINT_NORMALIZED_V12_ERROR_20261104')
