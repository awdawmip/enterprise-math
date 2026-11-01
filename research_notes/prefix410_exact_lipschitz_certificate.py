"""PREFIX-410 author-side exact certificate (external static five-Port model).

Check exact two-branch remainders, rational all-source bounds for
0<=epsilon<=1e-6, and an all-six-observation noisy coherent witness.
Not a P000/native typed-BRC calculation or an accepted EM Result.
"""
from fractions import Fraction as F
import sympy as S

eta=F(1,10000)
beta=F(1,1000000)
eps=F(1,1000000)

# Polynomial identities derived in the manuscript; recompute independently
# from the reduced affine Port expressions for this author-side checker.
p,q,x,y=S.symbols('p q x y',real=True)
uc=p+S.I*q; vc=x+S.I*y
a=S.Rational(5,2)+S.Rational(9,2)*S.I
b=S.Rational(3,2)+S.Rational(7,2)*S.I
d=S.Rational(11,4)+S.Rational(15,8)*S.I
e=S.Rational(5,4)+S.Rational(9,4)*S.I

def squared(z):return S.expand_complex(z*S.conjugate(z)).expand()
four=squared(a+b*uc+4*S.I*vc)
five=squared(d*(1+uc)+e*vc)
h=squared(1+vc)-1
t=squared(vc)
k=five-S.Rational(709,32)
alpha,gamma=S.symbols('alpha gamma',real=True)

for sign,c,center,Ah,Bh,quadratic,ident in [
    (1,S.Rational(64,61),37,(728*x-240*y+961)/61,(240*x+728*y+107)/61,S.Rational(351,122), (728,64,-176,61)),
    (-1,S.Rational(48,23),45,-(182*x-186*y+333)/46,-(186*x+182*y-609)/46,-S.Rational(793,92),(93,48,-43,23)),
]:
    four0=squared(a+b*(sign*S.I)+4*S.I*vc)
    five0=squared(d*(1+sign*S.I)+e*vc)
    k0=five0-S.Rational(709,32)
    n1,n2,n3,denom=ident
    assert S.simplify(four0-(center+(n1*h+n2*k0+n3*t)/denom))==0
    remainder=S.expand(four-four0-c*(five-five0)).subs({p:alpha,q:sign+gamma}).expand()
    target=(alpha*Ah+gamma*Bh+quadratic*(alpha**2+gamma**2)).expand()
    assert S.simplify(remainder-target)==0
    print('PASS exact remainder for branch',sign)

# For |x|,|y|<=1/1000 and |p|<=eps, |gamma|<3 eps/5,
# rational maxima: quadratic piece uses (p^2+gamma^2) <=34 eps^2/25.
Cp=F(961*1000+968,61000)+F(3,5)*F(107*1000+968,61000)+F(351,122)*F(34,25)*eps
Cm=F(333*1000+368,46000)+F(3,5)*F(609*1000+368,46000)+F(793,92)*F(34,25)*eps
assert Cp<17 and Cm<16
k_lower=4-F(792,61)*eta-17*eps
k_minus=4-(141*eta+43*beta)/23-16*eps
assert k_minus>k_lower
print('PASS rational global remainder bounds: Cplus=',Cp,'Cminus=',Cm)
print('PROVED_NO_BELOW=',k_lower,'~',float(k_lower),'MINUS_BRANCH_NO_BELOW=',k_minus)

# Fraction-valued complex pairs; no binary floating-point arithmetic.
def plus(z,w):return(z[0]+w[0],z[1]+w[1])
def times(z,w):return(z[0]*w[0]-z[1]*w[1],z[0]*w[1]+z[1]*w[0])
def norm(z):return z[0]*z[0]+z[1]*z[1]
A=(F(5,2),F(9,2)); B=(F(3,2),F(7,2)); D=(F(11,4),F(15,8)); E=(F(5,4),F(9,4)); O=(F(1),F(0))
def obs(u,v):
    return {
      'I2':norm(u),'Cu':norm(plus(O,u)),'I3':norm(v),'Cv':norm(plus(O,v)),
      'I4':norm(plus(plus(A,times(B,u)),times((F(0),F(4)),v))),
      'I5':norm(plus(times(D,plus(O,u)),times(E,v))),
    }
u=(F(9,10000000),F(19999991,20000000))
v=(F(2499,50000000),-F(7,50000))
q=obs(u,v)
assert abs(q['I2']-1)<=eps and abs(q['Cu']-2)<=eps
assert 0<=q['I3']<=beta
assert abs(q['Cv']-1)<=eta and abs(q['I5']-F(709,32))<=eta
assert q['I4']<41
k_upper=F(41)-q['I4']
assert k_lower<k_upper
# Prior PREFIX-409 exact optimum: kappa_409=(4-792*eta/61)+(176*T*/61), T*>0.
old_lower=4-F(792,61)*eta
assert k_upper<old_lower
assert old_lower-k_upper==F(5962374915813,1220000000000000000)
print('PASS coherent rational witness, six noisy observations')
for name,center in [('I2',F(1)),('Cu',F(2)),('I3',F(0)),('Cv',F(1)),('I4',F(41)),('I5',F(709,32))]:
    print(name,'=',q[name],'difference=',q[name]-center)
print('WITNESS_KAPPA_UPPER=',k_upper,'~',float(k_upper))
print('NO_GO_TO_YES_CERTIFIED_WINDOW_WIDTH=',k_upper-k_lower,'~',float(k_upper-k_lower))
print('STRICT_IMPROVEMENT_BELOW_PREFIX409_BASELINE=',old_lower-k_upper)
print('PASS_PREFIX410_EXACT_TWO_SHEET_LIPSCHITZ_AND_FULL_NOISY_BRACKET')
