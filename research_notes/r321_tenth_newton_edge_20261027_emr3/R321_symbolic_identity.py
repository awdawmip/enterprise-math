"""R321: exact rational-polynomial recurrence certificate, no interpolation.
Checks base moments and all-s induction identities for r=0..9, then Newton
q=9 recovery and shifted-polynomial positivity. Requires SymPy.
"""
from functools import lru_cache
from sympy import (S, Rational, symbols, binomial, factorial, diff, expand,
                   expand_func, together, Poly, simplify)

s, z, u = symbols('s z u')

def C(n, k):
    return binomial(n, k) if 0 <= k <= n else S.Zero

def n(i):
    return -C(3, i - 1)*z-C(6, i - 1)*z**2+C(8, i - 2)*z**3

def delta(i):
    return ((-C(4, i)+C(2, i - 1))*z
            +(C(5, i - 1)-C(5, i - 2))*z**2
            +C(7, i - 2)*z**3-C(9, i - 3)*z**4)

@lru_cache(None)
def M(i):
    if i == 0:
        return S.One
    return expand(n(i)*(1-z)**i - sum(
        delta(j)*M(i-j)*(1-z)**(j-1)
        for j in range(1, min(i, 12)+1)))

P = [S.One,
     3*(s+1)/4,
     (9*s**2+11*s-26)/16,
     3*(9*s**3+6*s**2-119*s+220)/64,
     3*(27*s**4-18*s**3-911*s**2+4070*s-6184)/256,
     3*(81*s**5-225*s**4-5295*s**3+43385*s**2-134746*s+162800)/1024,
     3*(243*s**6-1377*s**5-26055*s**4+348565*s**3
        -1709628*s**2+3668252*s-2031840)/4096,
     9*(243*s**7-2268*s**6-38052*s**5+780850*s**4
        -5472663*s**3+16271178*s**2-1634008*s-78016960)/16384,
     (6561*s**8-90396*s**7-1371006*s**6+41693400*s**5
      -395382351*s**4+1509433716*s**3+1771638636*s**2
      -36493134960*s+99723415680)/65536,
     (19683*s**9-373977*s**8-5078214*s**7+225467550*s**6
      -2791719189*s**5+13314869127*s**4+38834268264*s**3
      -860330966220*s**2+4551847454736*s-9191974659840)/262144]

assert M(0).subs(z, 1) == P[0]
for r in range(1, 10):
    assert simplify(diff(M(r), z, r).subs(z, 1)/2**r-P[r].subs(s, r)) == 0, r
    D = S.Zero
    for i in range(1, r+2):
        for a in range(r+2-i):
            if i == 1 and a == 0:
                continue
            lower = r+1-i-a
            D += ((-1)**i*factorial(r)/factorial(r+1-i)
                  *binomial(r+1-i, a)
                  *diff(delta(i), z, a).subs(z, 1)
                  *P[lower].subs(s, s-i) / S(2)**i)
    assert simplify(expand(D)-expand(P[r]-P[r].subs(s, s-1))) == 0, r

q = 9
Q9 = (390625*s**9-7734375*s**8+78168750*s**7
      -476358750*s**6+1425041625*s**5-3010947975*s**4
      +9059710376*s**3+13181542092*s**2-4890698640*s
      -67733293824)
DEN = 19025362944
recovered = sum((-1)**r*binomial(2*s+1-r, q-r)*P[r]/factorial(r)
                for r in range(q+1))
assert simplify(together(expand_func(recovered)-Q9/DEN)) == 0
shift = Poly(expand(Q9.subs(s, 9+u)), u)
shift_coeffs = [390625,23906250,660356250,10827022500,115842806625,
                830967262650,3922229318276,11404006965144,
                17815878242784,11071720783872]
assert shift.all_coeffs() == shift_coeffs
assert all(x > 0 for x in shift.all_coeffs())
assert Q9.subs(s, 9)/DEN == Rational(74489, 128)
assert 2**9*Q9.subs(s, 9)/DEN == 297956
print('PASS: exact base and all-s induction identities r=0..9; Newton q=9 recovery; shift positivity')
print('H9=', Poly(P[9]*262144,s).all_coeffs(), '/262144')
print('Q9=', Poly(Q9,s).all_coeffs(), '/', DEN)
print('Q9(9+u)=', shift.all_coeffs())
