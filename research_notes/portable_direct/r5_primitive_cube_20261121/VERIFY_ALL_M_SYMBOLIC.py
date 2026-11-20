"""Exact primitive cubic R5 threshold generating functions; requires SymPy.

All arithmetic is exact in Q(sqrt(-3)); no floats or finite-fitting proofs.
"""
import json
from pathlib import Path
import sympy as sp

z = sp.symbols('z')
t = sp.symbols('t')
I3 = sp.sqrt(-3)
omega = (-1+I3)/2
one = sp.Integer(1)

def phase(p):
    return (one, omega, omega**2)[p%3]

def M(a,b):
    return (1-a*b*z**2)/((1-a*z)*(1-b*z)*(1-a*b*z))

def V(a,b,c):
    return (1-a*b*c*z**3)/((1-a*b*c*z**2)*(1-a*z)*(1-b*z)*(1-c*z))

def S(a,b,c):
    return M(b,c)/(1-a*z)+M(a,c)/(1-b*z)+M(a,b)/(1-c*z)-V(a,b,c)

def reduce(e):
    return sp.cancel(e,extension=I3)

Hh = z/(3*(1-z)*(1-z**3))*sum(S(omega,omega**2,c) for c in (one,omega,omega**2))
H0 = z/(1-z**3)**2
H1 = z/((1-z**3)**2*(1-z)*(1-omega*z))
H2 = z/((1-z**3)**2*(1-z)*(1-omega**2*z))
H01 = -H0*sum(p*z*phase(p)/(1-z*phase(p)) for p in range(214,219))
Q = H01+219*(1-omega)*H1+219*(2+omega)*H2-657*Hh

D = (1-z**3)**3*(1+z**3)
Hh_closed = z*(2+z+2*z**3)/D
Q_closed = z*(-657+(216+I3)*z+(216-I3)*z**2-1737*z**3+(873+I3)*z**4+(216-I3)*z**5-1080*z**6)/D
assert reduce(Hh-Hh_closed)==0
assert reduce(Q-Q_closed)==0

b=lambda k: ((k+2)**2//4) if k>=0 else 0
Q_2=lambda k: sp.expand((216+I3)*b(k)+(873+I3)*b(k-1))
Q_0=lambda k: sp.expand((216-I3)*sp.binomial(k+2,2))
Q_2_gen=((216+I3)+(873+I3)*t)/((1-t)**3*(1+t))
Q_0_gen=(216-I3)/(1-t)**3
coeffs2=sp.Poly(sp.series(Q_2_gen,t,0,13).removeO().expand(),t)
coeffs0=sp.Poly(sp.series(Q_0_gen,t,0,13).removeO().expand(),t)
for k in range(12):
    assert sp.simplify(coeffs2.nth(k)-Q_2(k))==0
    assert sp.simplify(coeffs0.nth(k)-Q_0(k))==0
assert reduce(((216+I3)+(873+I3)*t).subs(t,-1))==-657
assert all(sp.re(sp.expand_complex(Q_2(k)))>0 for k in range(30))
assert all(sp.re(sp.expand_complex(Q_0(k)))>0 for k in range(30))
assert Q_2(0)==216+I3
assert Q_0(0)==216-I3

result={
 'schema':'R5_PRIMITIVE_CUBE_ALL_FIXED_M_V1',
 'model':'Frozen R5; m fixed positive; omega^3=1 omega!=1',
 'Q_m_generating_function':str(Q_closed),
 'overlap_Hh_generating_function':str(Hh_closed),
 'm_mod3_eq1':{'pole_order':32,'cost_N_degree':31,'leading_ratio_to_A3':'(k+1), m=3k+1'},
 'm_mod3_eq2':{'pole_order':31,'cost_N_degree':30,'Q_over_A3':'(216+i*sqrt(3))*b(k)+(873+i*sqrt(3))*b(k-1), b(k)=floor((k+2)^2/4), b(-1)=0'},
 'm_mod3_eq0':{'pole_order':31,'cost_N_degree':30,'Q_over_A3':'(216-i*sqrt(3))*binomial(k+2,2), m=3k+3'},
 'threshold_subperiod':'m=3k+2 coefficient has irreducible pole at t=-1, minimal k quasiperiod 2',
 'tests':{'symbolic_rational_identity':'PASS','finite_coefficients_per_subsequence':12,'previous_m2_m3_exact_values':'PASS','algebra':'Q(sqrt(-3)) exact'},
 'scope':'Only two primitive cubic-root contributions, not full F_m(N)',
 'review':'NOT_REVIEWED'
}
Path(__file__).with_name('RESULT_ALL_M.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print('PASS: exact rational Hh and Q identities; all m mod3 classes; 12 coefficients each')
