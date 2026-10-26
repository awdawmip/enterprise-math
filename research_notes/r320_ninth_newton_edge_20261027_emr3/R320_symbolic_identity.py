"""R320: exact rational-polynomial certificate. Requires SymPy; no interpolation."""
from functools import lru_cache
from sympy import symbols, binomial, factorial, diff, expand, Rational, Poly, solve, simplify
s, z, u = symbols('s z u')
def C(n, k):
    return binomial(n,k) if 0<=k<=n else 0
def n(i):
    return -C(3,i-1)*z-C(6,i-1)*z**2+C(8,i-2)*z**3
def delta(i):
    return (-C(4,i)+C(2,i-1))*z+(C(5,i-1)-C(5,i-2))*z**2+C(7,i-2)*z**3-C(9,i-3)*z**4
@lru_cache(None)
def M(i):
    if i==0: return Rational(1)
    return expand(n(i)*(1-z)**i-sum(delta(j)*M(i-j)*(1-z)**(j-1) for j in range(1,min(i,12)+1)))
P=[Rational(1),3*(s+1)/4,(9*s**2+11*s-26)/16,
   3*(9*s**3+6*s**2-119*s+220)/64,
   3*(27*s**4-18*s**3-911*s**2+4070*s-6184)/256,
   3*(81*s**5-225*s**4-5295*s**3+43385*s**2-134746*s+162800)/1024,
   3*(243*s**6-1377*s**5-26055*s**4+348565*s**3-1709628*s**2+3668252*s-2031840)/4096,
   9*(243*s**7-2268*s**6-38052*s**5+780850*s**4-5472663*s**3+16271178*s**2-1634008*s-78016960)/16384]
d8=6561*s**7-102060*s**6-745038*s**5+28176120*s**4-252794031*s**3+917001540*s**2-347820132*s-4539623760
h8=6561*s**8-90396*s**7-1371006*s**6+41693400*s**5-395382351*s**4+1509433716*s**3+1771638636*s**2-36493134960*s+99723415680
q8=78125*s**8-1187500*s**7+8916250*s**6-41125000*s**5+72310525*s**4-81437020*s**3+509008124*s**2+808645200*s-308472192
D=Rational(0)
for i in range(1,10):
    for a in range(10-i):
        if i==1 and a==0: continue
        r=9-i-a
        D+=(-1)**i*factorial(8)/factorial(9-i)*binomial(9-i,a)*diff(delta(i),z,a).subs(z,1)*P[r].subs(s,s-i)/2**i
D=expand(D)
assert simplify(D-d8/8192)==0
H=h8/65536
assert simplify(H-H.subs(s,s-1)-d8/8192)==0
assert diff(M(8),z,8).subs(z,1)==7096320
assert H.subs(s,8)==27720
recovered=sum((-1)**r*binomial(2*s+1-r,8-r)*P[r]/factorial(r) for r in range(8))+H/factorial(8)
assert simplify(expand(recovered)-q8/528482304)==0
shift=Poly(expand(q8.subs(s,8+u)),u)
expected=[78125,3812500,82416250,1030855000,8106910525,40334899780,119864161244,183822902544,103334805504]
assert shift.all_coeffs()==expected
assert q8.subs(s,8)/528482304==Rational(6257,32)
print('PASS: exact R8 recurrence, initial moment, ant difference, N8 recovery, shift positivity')
print('D8_coeffs:', Poly(d8,s).all_coeffs())
print('H8_coeffs:', Poly(h8,s).all_coeffs())
print('Q8_shift_coeffs:', shift.all_coeffs())
