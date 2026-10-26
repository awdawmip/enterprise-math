# R322 exact symbolic recurrence certificate; prior r0..r9 expressions traced to R321 immutable source.
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


# R322 extension: exact r=10 recurrence and Newton q=10 polynomial.
from sympy import cancel
r = 10
D = S.Zero
for i in range(1, r+2):
    for a in range(r+2-i):
        if i==1 and a==0:
            continue
        h=r+1-i-a
        D += ((-1)**i*factorial(r)/factorial(r+1-i)
              *binomial(r+1-i,a)*diff(delta(i),z,a).subs(z,1)
              *P[h].subs(s,s-i)/S(2)**i)
D=expand(D)
assert Poly(D,s).degree()==9
A=S.Zero
R=D
for d in reversed(range(10)):
    c=Poly(R,s).coeff_monomial(s**d)
    term=c*s**(d+1)/(d+1)
    A+=term
    R=expand(R-(term-term.subs(s,s-1)))
assert R==0
m10_base=diff(M(10),z,10).subs(z,1)
assert m10_base==1215648000
A=expand(A+(m10_base/S(2)**10-A.subs(s,10)))
assert expand(A-A.subs(s,s-1)-D)==0
assert A.subs(s,10)==m10_base/S(2)**10
P.append(A)
P10_NUM=[59049,-1476225,-17452260,1134666630,-17876052243,105293849535,500912600310,-13511047863780,105842210675544,-414136077320160,691268379379200]
D10_NUM=[295245,-7971615,-39694050,4147463250,-65930377275,417673308465,276315645600,-21096639526500,126789710687280,-266932963987200]
Q10_NUM=[390625,-9765625,126937500,-997406250,4369693125,-13510205625,36487366310,14180963260,21073172760,-511748665056,-691481774592]
SHIFTQ10_NUM=[390625,29296875,1005843750,20876343750,289976255625,2801680756875,18846923022560,85552644990660,244575209356560,386762812758144,254338037710848]
pden,pnum=Poly(P[10],s).clear_denoms(convert=True)
assert pden==1048576 and list(map(int,pnum.all_coeffs()))==P10_NUM
dden,dnum=Poly(D,s).clear_denoms(convert=True)
assert dden==524288 and list(map(int,dnum.all_coeffs()))==D10_NUM
q=10
recovered=sum((-1)**r*binomial(2*s+1-r,q-r)*P[r]/factorial(r) for r in range(q+1))
recovered=cancel(expand(expand_func(recovered)))
qden,qnum=Poly(recovered,s).clear_denoms(convert=True)
assert qden==152202903552 and list(map(int,qnum.all_coeffs()))==Q10_NUM
shift=Poly(expand(qnum.as_expr().subs(s,10+u)),u)
assert list(map(int,shift.all_coeffs()))==SHIFTQ10_NUM
assert all(c>0 for c in shift.all_coeffs())
assert 2**10*recovered.subs(s,10)==1711151
assert recovered.subs(s,10)==Rational(1711151,1024)
print('PASS: exact r=0..10 induction polynomial, q=10 Newton recovery and all-positive shift')
print('P10=',P10_NUM,'/1048576')
print('D10=',D10_NUM,'/524288')
print('Q10=',Q10_NUM,'/152202903552')
print('SHIFT=',SHIFTQ10_NUM)
