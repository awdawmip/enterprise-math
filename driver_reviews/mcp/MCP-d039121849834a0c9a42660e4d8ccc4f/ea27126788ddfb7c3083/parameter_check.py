from sympy import Rational, sqrt, simplify, legendre_symbol

# Exact specialization from the displayed Weierstrass curve invariants.
# This is not a numerical proof of the finite-sum congruence.
r = sqrt(2)
t = (2-r)/4
tbar = (2+r)/4
assert simplify(t+tbar) == 1

def displayed_invariants(u):
    a1, a2, a3, a4, a6 = 1, 0, u/27, 0, 0
    b2 = a1*a1 + 4*a2
    b4 = 2*a4 + a1*a3
    b6 = a3*a3 + 4*a6
    b8 = a1*a1*a6 + 4*a2*a6 - a1*a3*a4 + a2*a3*a3 - a4*a4
    c4 = simplify(b2*b2 - 24*b4)
    delta = simplify(-b2*b2*b8 - 8*b4**3 - 27*b6**2 + 9*b2*b4*b6)
    j = simplify(c4**3/delta)
    assert simplify(c4-(1-8*u/9)) == 0
    assert simplify(delta-(u/27)**3*(1-u)) == 0
    assert simplify(j-27*(9-8*u)**3/(u**3*(1-u))) == 0
    return c4, delta, j

c4, delta, j = displayed_invariants(t)
c4bar, deltabar, jbar = displayed_invariants(tbar)
assert j == 2417472+1707264*r
assert jbar == 2417472-1707264*r
assert simplify(j.xreplace({r: -r})-jbar) == 0
old_formula = simplify(27*(1+8*t)**3/(t*(1-t)**3))
assert old_formula == jbar
for value in (j, jbar):
    assert simplify(value*value-4834944*value+14670139392) == 0
norm = simplify(delta*deltabar)
assert norm == Rational(1,2**12*3**18)

print('displayed E3(t): y^2+xy+(t/27)y=x^3')
print('t =', t)
print('tbar = 1-t =', tbar)
print('c4(t) =', c4)
print('j(t) =', j)
print('j(tbar) =', jbar)
print('old formula equals j(tbar): PASS')
print('H_-24(j(t)) = H_-24(j(tbar)) = 0: PASS')
print('Norm(delta) =', norm)
for residue in (13,19):
    # These characters depend only on the unit residue class modulo 24.
    cm = legendre_symbol(-6, residue)
    sign_factor = legendre_symbol(2, residue)
    sgn = -1  # Standard Deuring criterion: inert CM reduction is supersingular.
    assert cm == -1 and sign_factor == -1 and sgn*sign_factor == 1
    print('p mod24 =', residue, '(−6/p) =', cm, '(2/p) =', sign_factor, 'sgn =', sgn, 'T1 product = +1')
