#!/usr/bin/env python3
"""Independent symbolic expansion from raw z4/z5 expressions (external auxiliary model)."""
import sympy as S
x,y=S.symbols('x y',real=True)
v=x+S.I*y

def obs(u):
    H=(5+9*S.I)/2+(3+7*S.I)*u/2
    z4=H+4*S.I*v
    z5=(22+15*S.I)*(1+u)/8+(5+9*S.I)*v/4
    return S.expand_complex(z4*S.conjugate(z4)).expand(),S.expand_complex(z5*S.conjugate(z5)).expand()
fp,gp=obs(S.I)
fm,gm=obs(-S.I)
assert S.simplify(gp-gm-(123*x+245*y)/8)==0
assert S.simplify(fp-fm-(-8+24*x+56*y))==0
assert S.simplify(fp+fm-82-(72*x-40*y+32*(x*x+y*y)))==0
xs=S.Rational(1,2000)
ys=-S.Rational(123,245)*xs
assert S.simplify((gp-gm).subs({x:xs,y:ys}))==0
assert S.simplify((fp-fm).subs({x:xs,y:ys}))!=0
assert S.simplify(fp.subs({x:xs,y:ys}))<41<S.simplify(fm.subs({x:xs,y:ys}))
difference=S.simplify((fp+fm-82).subs({x:xs,y:ys}))
assert difference==S.Rational(172762577,3751562500)
print('z5_phase_branch_difference:',S.factor(gp-gm))
print('z4_phase_branch_difference:',S.factor(fp-fm))
print('objective_difference_closed_form:',S.factor(fp+fm-82))
print('objective_difference_exact:',difference)
print('PASS_PREFIX434_INDEPENDENT_SYMBOLIC_ORIGINAL_PORT_EXPANSIONS')
