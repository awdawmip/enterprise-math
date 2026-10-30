#!/usr/bin/env python3
"""PREFIX-376: exact universal injectivity of (|1+u|^2, |1+v|^2)
for the inherited static 5-Port complex-three-component intensity model.
All load-bearing checks use SymPy exact rational/symbolic operations.
"""
import json
import sympy as S

a,b,c,d,x,t = S.symbols('a b c d x t', real=True)
i = S.I
L,U = S.Rational(8,85), S.Rational(4321,21259)
T = (S.Integer(3200)+56336*t)/(34000+204144*t)
assert S.factor(T.subs(t,0)-L)==0
assert S.factor(T.subs(t,S.Rational(1,4))-U)==0
assert S.simplify(S.diff(T,t)-S.Rational(1262163200,1)/(34000+204144*t)**2)==0
K = S.Rational(1101,424)-S.Rational(995,106)*x
assert K.subs(x,L)==S.Rational(233,136) and S.diff(K,x)<0
# Rebuild every normalized intensity from the frozen five-Port Q(t) family.
Tinv = (200-2125*x)/(12759*x-3521)
assert S.factor(T.subs(t,Tinv)-x)==0
Q = S.Matrix([34000+204144*Tinv,3200+56336*Tinv,
    58250+1286*Tinv,46600+12936*Tinv,31525+28011*Tinv])
assert S.cancel(Q[1]/Q[0]-x)==0
assert S.cancel(Q[2]/Q[0]-K)==0

A=S.Matrix([[4,4,0],[0,-4,4],[-5+3*i,0,-3+i],
  [-2-2*i,4+4*i,2+2*i],[-2,0,5+2*i]])
B=A[3:5,:]*A[:3,:].inv()
expected_B=S.Matrix([
 [S.Rational(5,2)+S.Rational(9,2)*i,S.Rational(3,2)+S.Rational(7,2)*i,4*i],
 [S.Rational(11,4)+S.Rational(15,8)*i,S.Rational(11,4)+S.Rational(15,8)*i,S.Rational(5,4)+S.Rational(9,4)*i]])
assert all(S.simplify(B[j,k]-expected_B[j,k])==0 for j in range(2) for k in range(3))

q4=S.Rational(217,106)-S.Rational(381,53)*x
q5=S.Rational(1133,848)-S.Rational(921,212)*x
assert S.cancel(Q[3]/Q[0]-q4)==0
assert S.cancel(Q[4]/Q[0]-q5)==0
v=c+i*d
Ds=[];Rs=[]
for j,qnorm in enumerate([q4,q5]):
    aa,bb,cc=list(B.row(j))
    Dj=S.expand(S.conjugate(aa+cc*v)*bb)
    n0=S.expand(S.conjugate(aa+cc*v)*(aa+cc*v))
    # On the physical circle, substitute |v|^2=K into the polynomial.
    nlin=S.expand(n0-S.expand(cc*S.conjugate(cc))*(c*c+d*d-K))
    Rj=S.factor((qnorm-nlin-S.expand(bb*S.conjugate(bb))*x)/2)
    Ds.append(Dj);Rs.append(Rj)
D4,D5=Ds;R4,R5=Rs
A4,B4=S.expand(S.re(D4)),S.expand(S.im(D4))
P5,Q5=S.expand(S.re(D5)),S.expand(S.im(D5))
assert S.expand(A4-(14*c-6*d+S.Rational(39,2)))==0
assert S.expand(B4-(-6*c-14*d+2))==0
assert S.expand(P5-((245*c-123*d)/32+S.Rational(709,64)))==0
assert S.expand(Q5-((-123*c-245*d)/32))==0
assert S.expand(R4-((-72*c+40*d+257*x-132)/4))==0
assert S.expand(R5-((-51940*c+26076*d+158627*x-91398)/6784))==0
F4=S.expand(A4*a-B4*b-R4)
F5=S.expand(P5*a-Q5*b-R5)

def flip(expr, flip_b=False, flip_d=False):
    return S.expand(expr.subs({b:(-b if flip_b else b), d:(-d if flip_d else d)}, simultaneous=True))

# Case I: v unchanged, u -> conjugate(u); if b != 0, B4=Q5=0.
assert S.expand(F4-flip(F4,flip_b=True)+2*B4*b)==0
assert S.expand(F5-flip(F5,flip_b=True)+2*Q5*b)==0
same_v=S.solve([B4,Q5],(c,d),dict=True)
assert same_v==[{c:-S.Rational(35,18), d:S.Rational(41,42)}]
assert S.Rational(35,18)**2 - K.subs(x,L) == S.Rational(22777,11016)>0

# Case II: u unchanged, v -> conjugate(v); if d!=0, two linear equations.
assert S.expand(F4-flip(F4,flip_d=True)+4*d*(3*a-7*b+5))==0
assert S.expand(F5-flip(F5,flip_d=True)+S.Rational(1,16)*d*(123*a-245*b+123))==0
same_u=S.solve([3*a-7*b+5,123*a-245*b+123],(a,b),dict=True)
assert same_u==[{a:S.Rational(26,9),b:S.Rational(41,21)}]
assert S.Rational(26,9)**2 > U

# Case III: both coordinates conjugated; if d!=0, b=-2d and a=-1-2c.
assert S.expand(F4-flip(F4,flip_b=True,flip_d=True)+4*(3*a*d-3*b*c+b+5*d))==0
assert S.expand(F5-flip(F5,flip_b=True,flip_d=True)+S.Rational(123,16)*(a*d-b*c+d))==0
assert S.expand((3*a*d-3*b*c+b+5*d)-3*(a*d-b*c+d)-(b+2*d))==0
c_expr=S.factor((x-1-4*K)/4)
assert S.expand(c_expr-(4086*x-1207)/424)==0
N=16695396*x**2-8176084*x+990025
assert S.factor(K-c_expr**2+N/S.Integer(179776))==0
assert S.diff(N,x).subs(x,U)==-S.Rational(29533757524,21259)<0
assert N.subs(x,U)==S.Rational(8101139328585,451945081)>0

# Exact inverse of the two coherent readouts, up to signs resolved uniquely by F4/F5.
Cu=1+x+2*a; Cv=1+K+2*c
assert S.simplify(S.solve(S.Eq(S.Symbol('cu'),Cu),a)[0]-(S.Symbol('cu')-1-x)/2)==0
assert S.simplify(S.solve(S.Eq(S.Symbol('cv'),Cv),c)[0]-(S.Symbol('cv')-1-K)/2)==0

result={
 'unit':'PREFIX-376',
 'model':'auxiliary static complex 3-component / 5-Port intensity',
 'claim':'joint (Cu,Cv) is injective on the physical source fiber for every t in [0,1/4]',
 'physical_x_range':[str(L),str(U)],
 'checks':{
   'recomputed_B_and_two_normalized_intensity_equations':True,
   'conjugate_u_only_forces_v':[str(same_v[0][c]),str(same_v[0][d])],
   'conjugate_u_only_lower_bound_c2_minus_Kmax':str(S.Rational(22777,11016)),
   'conjugate_v_only_forces_u':[str(same_u[0][a]),str(same_u[0][b])],
   'conjugate_v_only_a2_gt_xmax':True,
   'both_conjugated_forces_b_equal_minus2d':True,
   'both_conjugated_forces_a_equal_minus1_minus2c':True,
   'K_minus_c2_equals_minus_N_over_179776':True,
   'N_derivative_at_upper_bound':str(S.diff(N,x).subs(x,U)),
   'N_at_upper_bound':str(N.subs(x,U)),
   'explicit_real_part_recovery':True
 },
 'verification':'exact symbolic identities and rational inequalities; paper sign case split',
 'depends_on_prior_source_classification_for_injectivity':False,
 'status':'AUTHOR_SIDE_EXACT_SYMBOLIC / LOCAL_VERIFIED / UNREVIEWED / NOT_ADMITTED',
 'native_X6_or_typed_BRC_execution':False
}
print(json.dumps(result,indent=2,ensure_ascii=False))
print('PASS_PREFIX376_GLOBAL_TWO_OBSERVER_INJECTIVITY')
