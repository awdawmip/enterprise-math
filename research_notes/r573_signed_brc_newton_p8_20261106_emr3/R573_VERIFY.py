#!/usr/bin/env python3
"""R573: exact p8 certificate for the frozen R462 signed-BRC auxiliary scalar.
No floating-point approximations enter any accepting condition.
Run: python R573_VERIFY.py > R573_EVIDENCE.txt
Python 3 + SymPy required.
"""
from math import comb, factorial
from fractions import Fraction
import sympy as S

k, t = S.symbols('k t', integer=True)
D = S.Integer(400187433595950000000)
P8_DESC = (
    7554138112,11588835377152,159172974950400,642392216322048,
    -894589534093904,-17384871298837376,-53603602043693368,
    86624147718232760,1320958222567876483,5659350297985381846,
    14848049781867842558,26798213772663506696,34024366657433013195,
    29620698220815642474,16560775327536222788,4547844671358118136,
)
P8 = S.Poly.from_list(P8_DESC,k).as_expr()

def catalan(n):
    return comb(2*n,n)//(n+1)

def H(n,j):
    r=2*n+1
    if j<2 or j>r: return 0
    return comb(r+j,2*j)*sum(comb(j-1,2*q)*4**q*catalan(n-q)
        for q in range(min(n,(j-1)//2)+1))

def A_symbolic(j):
    """A_j=H_k(j+2)/H_k(2), closed form via Catalan quotient.
    Derivation for k >= 5: C_(k-q)/C_k = prod_{v=0}^{q-1}
      (k-v+1)/(2*(2*(k-v)-1)), then cancellation. The resulting
    polynomial extends to 2 <= k <= 4 with missing A_j=0.
    """
    binomial_quotient = S.Rational(24, factorial(2*j+4)) * (
        S.prod(2*k+a for a in range(4,j+4)) *
        S.prod(2*k-1-b for b in range(j)))
    def cquot(q):
        return S.prod((k-v+1)/(2*(2*(k-v)-1)) for v in range(q))
    branching = sum(comb(j+1,2*q)*4**q*cquot(q)
                    for q in range((j+1)//2+1))
    return S.factor(S.cancel(binomial_quotient*branching))

A = {j:A_symbolic(j) for j in range(1,9)}
p = {}
for m in range(1,9):
    p[m]=S.factor(-sum((-1)**j*A[j]*p[m-j] for j in range(1,m))
                 -m*(-1)**m*A[m])
assert S.cancel(p[8]-(k+2)*P8/D)==0
assert S.degree(p[8], k) == 16

# Exact global positivity proof, not extrapolation from finite tests:
shift = list(reversed(S.Poly(S.expand(P8.subs(k,t+2)),t).all_coeffs()))
assert len(shift)==16 and all(x.is_Integer and x > 0 for x in shift)
# Independent literal Catalan / binomial computation for every k=2,...,1000:
for n in range(2,1001):
    den=H(n,2)
    coeff=[Fraction(H(n,j+2),den) for j in range(1,9)]
    for j in range(1,9):
        assert coeff[j-1] == Fraction(A[j].subs(k,n))
    power={}
    for m in range(1,9):
        power[m]=-sum((-1)**j*coeff[j-1]*power[m-j]
                  for j in range(1,m)) - m*(-1)**m*coeff[m-1]
    assert power[8]==Fraction(p[8].subs(k,n))
    assert power[8]>0

print('FROZEN_SOURCE R462@18783e01e3646c72b7aab3b16d3f565e83e6446f')
print('MODEL signed-BRC auxiliary scalar Toeplitz-Hessenberg Q_k degree=2k-1')
print('P8_DESC',list(P8_DESC))
print('DEN',D)
print('P8_SHIFT_K2_ASC',list(map(int,shift)))
print('P8_LEADING_COEFFICIENT',S.LC(S.Poly(p[8],k)))
print('RHO8_LIMINF_FACTOR_POWER8',S.factor(S.LC(S.Poly(p[8],k))/2))
for n in [2,3,5,9,29,30,100,1000]:
    pn=Fraction(p[8].subs(k,n))
    print('K',n,'P8',pn,'RHO8_POWER8',pn/Fraction(2*n-1))
print('R573_NEWTON_P8_EXACT_PASS k=2..1000 n=999')
