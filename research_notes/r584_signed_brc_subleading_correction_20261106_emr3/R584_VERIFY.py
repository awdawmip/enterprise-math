"""R584: Exact Q-series certificate for the positive subleading b_m correction.
Independent paths: R583 rational binomial finite sum vs. derivative of
log(alpha)+3/2 log((2s+1)/3), using formal series for w=1-sqrt(1-2t).
No floating point is used in theorem acceptance assertions.
"""
from fractions import Fraction
from math import comb, pi, sqrt

N = 96
Q = Fraction

def mul(a, b, n):
    out = [Q(0) for _ in range(n)]
    for i, x in enumerate(a[:n]):
        for j, y in enumerate(b[:n - i]):
            out[i+j] += x * y
    return out

def inv(a, n):
    assert a[0] != 0
    v = [1 / a[0]]
    for i in range(1, n):
        v.append(-sum(a[j] * v[i-j] for j in range(1, i+1)) / a[0])
    return v

# Coefficients of w=1-sqrt(1-2t) are positive at all positive degrees.
w = [Q(0)] + [Q(comb(2*j,j), 2**j * (2*j-1)) for j in range(1, N)]
s = [Q(1)] + [-v for v in w[1:]]
alpha_denom = [Q(2)] + [-v for v in w[1:]]             # 1+s
other_denom = [Q(3)] + [-2*v for v in w[1:]]           # 1+2s
A = mul(inv(s, N), [x+3*y for x,y in zip(inv(alpha_denom,N), inv(other_denom,N))], N)

assert A[0] == Q(3,2)
assert A[1] == Q(29,12)
assert A[2] == Q(151,36)

for m in range(1, N+1):
    b_m = (Q(comb(2*m-1,m-1), 2**m)
            + Q(1,2) * sum((Q(comb(m+r-1,r),2**r) for r in range(m)), Q(0))
            - 3 * 2**(m-1) * sum((Q(comb(m+r-1,r),4**r) for r in range(m)), Q(0)))
    e_m = b_m + Q(3,2)*Q(8,3)**m - Q(2**m,4)
    assert e_m == A[m-1], (m, e_m, A[m-1])
    assert e_m > 0
    # Coefficientwise lower bound from j=0 of the two nonnegative w-series.
    assert e_m >= Q(3,2)*Q(comb(2*m-2,m-1),2**(m-1))
    if m in (1,2,3,12,24,48,96):
        print('m=',m,'b_m=',str(b_m) if m<=3 else '(exact verified)',
              'E_m=',str(e_m) if m<=3 else '(exact verified)')
        if m>=12:
            scaled = float(e_m / 2**m * sqrt(pi*m))
            print(' scaled E_m*sqrt(pi*m)/2^m=',format(scaled,'.12f'),
                  ' two-term=',format(2-2.5/m,'.12f'))
print('R584_POSITIVE_SUBLEADING_CORRECTION_EXACT_96_PASS')
