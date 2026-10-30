"""Exact symbolic certificate for the R5 nonterminal-route two-law parametric family.
Requires SymPy; it checks algebraic identities, not inequalities or scientific admission.
"""
from sympy import Matrix, Rational, factor, simplify, symbols

p, q, a, b, c = symbols("p q a b c")


def observer(x, y0, y1):
    yp = p*y0 + (1-p)*y1
    yq = q*y0 + (1-q)*y1
    return Matrix((c+a*x+b*x*yp, c+a*x+b*x*yq, 4-yp, 4-yq))


base = observer(0, 0, 0)
v10 = observer(0, 1, 0)-base
v01 = observer(0, 0, 1)-base
vroute = observer(1, 0, 0)-base
vr0 = observer(1, 1, 0)-base
vr1 = observer(1, 0, 1)-base

d1 = factor(Matrix.hstack(v10, v01, vroute, vr0).det())
d2 = factor(Matrix.hstack(v10, v01, vr0, vr1).det())
assert simplify(d1+a*b*(p-q)**2) == 0
assert simplify(d2-b*(2*a+b)*(p-q)**2) == 0

# FULL policy: x=1/2, Y=X at U=0, Y=1-X at U=1.
ep = c+a/2+b*p/2
eq = c+a/2+b*q/2
assert factor(ep-eq) == b*(p-q)/2
assert simplify(ep.subs({p:Rational(1,4),a:Rational(1,8),b:Rational(1,8),c:Rational(1,4)})-Rational(21,64)) == 0
assert simplify(eq.subs({q:Rational(1,2),a:Rational(1,8),b:Rational(1,8),c:Rational(1,4)})-Rational(11,32)) == 0
assert d1.subs({p:Rational(1,4),q:Rational(1,2),a:Rational(1,8),b:Rational(1,8)}) == -Rational(1,1024)
assert d2.subs({p:Rational(1,4),q:Rational(1,2),a:0,b:Rational(1,8)}) != 0

print("DET_ROUTE_BASE="+str(d1))
print("DET_TAIL_PAIR="+str(d2))
print("FULL_ERROR_DIFFERENCE="+str(factor(ep-eq)))
print("NONZERO_RANK4_IF_AND_ONLY_IF=(p!=q and b!=0) for 0<p,q<1")
print("REAL_IMAGE_GAP_IF=(p!=q and b!=0), legal error kernels")
print("RAW_LINFTY_LOWER_BOUND=abs(b)*abs(p-q)/(4*(1+abs(b)))")
print("PASS_EXACT_R5_ROUTE_MEMORY_PARAMETRIC_OPEN_FAMILY")