"""R589: exact algebra audit of nonzero simple zeros of the auxiliary F.
No native BRC state evolution or physical residual calculation is performed.
"""
import sympy as sp
u, S, C, inv = sp.symbols('u S C inv')
f = sp.cos(u) - 1 + u**2/2
assert sp.simplify(sp.diff(f,u) - (u - sp.sin(u))) == 0
relations=[C-1+u**2/2,S-u,S**2+C**2-1,u*inv-1]
G=sp.groebner(relations,C,S,inv,u,order='lex',domain=sp.QQ)
assert G.contains(sp.Integer(1))
assert sp.factor(u**2+(1-u**2/2)**2-1) == u**4/4
assert sp.simplify((u-sp.sin(u))/u**5-(-u+sp.sin(u))/(-u)**5)==0
assert sp.simplify(sp.Rational(48)/(sp.Integer(8)**sp.Rational(3,2))-3/sp.sqrt(2))==0
assert sp.simplify(sp.sqrt(8)/4-1/sp.sqrt(2))==0
print("R589_EXACT_NONMULTIPLE_ROOT_GROEBNER_CERTIFICATE_PASS")
print("R589_CHAIN_RULE_BRANCH_INVARIANCE_PASS")
print("R589_ASYMPTOTIC_CONSTANTS_EXACT_PASS")
