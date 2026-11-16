#!/usr/bin/env python3
"""R749SSP exact (8,9) collision at three reads and four-read no-go.

All symbolic assertions use exact rational arithmetic. Python 3 + SymPy.
"""
import json
from fractions import Fraction as F
from pathlib import Path
import sympy as sp

W = (1,1,2,3,6)
N=40
n=[0]*(N+1); n[0]=1
for w in W:
    for k in range(w,N+1):
        n[k]+=n[k-w]
C=[0]*(N+1); T=[0]*(N+1)
for q in range(1,N+1):
    C[q]=C[q-1]+n[q-1]
    T[q]=T[q-1]+C[q-1]
S=lambda q: 18*q**4+54*q**3-345*q**2+2070*q-16315
Y=lambda q,E,D: sp.Rational(q**3)*(T[q]+E)/(C[q]+D)-sp.Rational(S(q),108)
e,d,E,D=sp.symbols('e d E D')
q,p=8,9
rows=[]
for j in range(4):
    a,b=q+6*j,p+6*j
    V=b**3*(C[a]+d)
    U=a**3*(T[a]+e)+sp.Rational(S(b)-S(a),108)*(C[a]+d)
    rows.append((V,-U,C[b]*U-T[b]*V))

def det3(index):
    a,b,c=[rows[j] for j in index]
    return sp.expand(a[0]*(b[1]*c[2]-b[2]*c[1])
                    -a[1]*(b[0]*c[2]-b[2]*c[0])
                    +a[2]*(b[0]*c[1]-b[1]*c[0]))

f_raw=det3((0,1,2))
g_raw=det3((0,1,3))
D0=sp.ilcm(*[k.q for k in sp.Poly(f_raw,e,d).coeffs()
            +sp.Poly(g_raw,e,d).coeffs()])
f=sp.Poly(sp.expand(D0*f_raw),e).as_expr()
g=sp.Poly(sp.expand(D0*g_raw),e).as_expr()
a,b,c=[sp.Poly(f,e).nth(i) for i in (2,1,0)]
A,B,CC=[sp.Poly(g,e).nth(i) for i in (2,1,0)]
R=sp.Poly(sp.expand((a*CC-A*c)**2-(a*B-A*b)*(b*CC-B*c)),d)
Q=sp.Poly(
    26462686334042645429945701137787854*d**5
  + 2665724529495411954752877400836869271273*d**4
  + 225665575370900725811848376223012798253276*d**3
  + 259206111485804009334400947416274794358340*d**2
  -10607977574627059592249580049853570554088576*d
  +19042774742613941301134787391164065250594816,d)
core=sp.Poly((d+98)*(d+662)*(79435415*d+612671694)*Q.as_expr(),d)
quotient,remainder=sp.div(R,core)
assert remainder==0 and quotient.degree()==0 and quotient.all_coeffs()[0]!=0
resultant_constant=quotient.all_coeffs()[0]
assert D0==24

# Bernstein-basis positivity certificate on d=-2+4x, 0<=x<=1.
x=sp.symbols('x')
PX=sp.Poly(sp.expand(Q.as_expr().subs(d,-2+4*x)),x)
assert PX.degree()==5
coeff=PX.all_coeffs()[::-1]
bernstein=[sp.factor(sum(coeff[k]*sp.binomial(i,k)/sp.binomial(5,k)
                   for k in range(i+1))) for i in range(6)]
assert all(z>0 for z in bernstein)

# Three-read collision at cutoff 8 with denominator error d=-1.
Phi=sp.Poly(86485661024256*e**2-75908891607492816*e
            -24689030348714335,e)
f_at=sp.Poly(sp.expand(f.subs(d,-1)),e)
qu,rem=sp.div(f_at,Phi)
assert rem==0 and qu.degree()==0 and qu.all_coeffs()[0]!=0
lo,hi=F(-163,500),F(-13,40)
assert Phi.eval(sp.Rational(lo.numerator,lo.denominator))>0
assert Phi.eval(sp.Rational(hi.numerator,hi.denominator))<0
assert all(sp.diff(Phi.as_expr(),e).subs(
    e,sp.Rational(z.numerator,z.denominator))<0 for z in (lo,hi))
ys=[Y(q+6*j,e,-1) for j in range(3)]
xs=[sp.cancel((ys[j]+sp.Rational(S(p+6*j),108))/(p+6*j)**3)
    for j in range(2)]
assert sp.simplify(xs[1]-xs[0])!=0
Dofe=sp.cancel((T[p+6]-T[p]-xs[1]*C[p+6]+xs[0]*C[p])/(xs[1]-xs[0]))
Eofe=sp.cancel(xs[0]*(C[p]+Dofe)-T[p])
assert Dofe==sp.cancel((3161870784*e+155094721265)
                       /(2*(632114352*e-110882822705)))
assert Eofe==sp.cancel((143842148352*e**2
                       -23723179174944*e-29856214143065)
                       /(216*(632114352*e-110882822705)))
third=sp.cancel(ys[2]-Y(p+12,Eofe,Dofe))
num,den=sp.fraction(third)
assert sp.rem(sp.Poly(num,e),Phi)==0
assert sp.gcd(sp.Poly(num,e),sp.Poly(den,e)).degree()==0

# Rational interval enclosures establish both competing errors inside (-2,2).
def plus(a,b): return (a[0]+b[0],a[1]+b[1])
def times(a,b):
    vals=[u*v for u in a for v in b]
    return min(vals),max(vals)
def divide(a,b):
    assert b[0]*b[1]>0
    inv=(F(1,b[1]),F(1,b[0]))
    return times(a,(min(inv),max(inv)))
def evalpoly(coefs):
    y=(F(0),F(0))
    for c in coefs[::-1]:
        y=plus(times(y,(lo,hi)),(F(c),F(c)))
    return y
D_iv=divide(evalpoly([155094721265,3161870784]),
            evalpoly([-221765645410,1264228704]))
E_iv=divide(evalpoly([-29856214143065,-23723179174944,143842148352]),
            evalpoly([-23950689704280,136536700032]))
for interval in (D_iv,E_iv):
    assert -2<interval[0]<=interval[1]<2
assert lo>-2 and hi<2

out={
    'schema':'R749SSP_SHARP_HORIZON_8_9_CERT_V1',
    'author_status':'AUTHOR_EXACT_NOT_REVIEWED',
    'cutoffs':[8,9],
    'weights':list(W),
    'common_within_state_errors':'Each state uses its own real pair in [-2,2]^2',
    'three_read_collision':{
        'cutoff_8_denominator_error':'-1',
        'cutoff_8_numerator_error':'unique root in (-163/500,-13/40) of '+str(Phi.as_expr()),
        'cutoff_9_numerator_error_formula':str(Eofe),
        'cutoff_9_denominator_error_formula':str(Dofe),
        'cutoff_9_error_bounds_rational':{
            'eprime':[str(z) for z in E_iv],
            'dprime':[str(z) for z in D_iv]},
        'third_read_identity':'third difference numerator divisible by Phi'},
    'four_read_separation':{
        'scaled_determinant_factor':str(D0),
        'resultant_constant_multiplier':str(resultant_constant),
        'resultant_factorization':'K*(d+98)*(d+662)*(79435415*d+612671694)*Q(d)',
        'quintic_Q_coefficients_ascending':[str(z) for z in Q.all_coeffs()[::-1]],
        'Q_bernstein_coefficients_on_minus2_plus2':[str(z) for z in bernstein],
        'bernstein_all_positive':True},
    'minimal_consecutive_six_shift_reads':4,
    'status':'PASS'}
Path(__file__).with_name('R749SSP_EIGHT_NINE_RESULTS.json').write_text(
    json.dumps(out,indent=2,ensure_ascii=False,sort_keys=True)+'\n',encoding='utf-8')
print('PASS; q=8 vs q=9, three-read collision, four-read separation')
print('Bernstein signs:',[int(sp.sign(z)) for z in bernstein])
print('E interval:',E_iv,'D interval:',D_iv)
