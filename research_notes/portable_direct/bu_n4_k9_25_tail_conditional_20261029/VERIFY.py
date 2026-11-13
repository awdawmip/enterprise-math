"""Exact algebra verification for BU N4 k=9/25 capacity tail.

The inherited 16-leaf causal reduction and event-TV dual weights are
HYPOTHESES. This code does not independently validate them or claim admission.
"""
from sympy import Rational as Q, symbols, simplify, diff, factor

a, b, c = symbols('a b c', real=True)
lo, hi = Q(989,1000), Q(99,100)
bl, bh = Q(307,2100), Q(3,20)
k = Q(9,25)
D = 4*a+12*b+2
C = (7-a-21*b)/D
E = C*(a+3*b-1)/12
L0 = lambda z: (4*a-14*b-3*a*z-(a+3*b)*z*z)/(2*(23-2*z))
L3 = lambda z: z*(a-(a+3*b)*z)/(2*(7-2*z))
R = lambda z: z*(a+3*b-1)/12
N = 55781*a*a+243936*a*b-90472*a+229779*b*b-692766*b+97475
G = 5*a*a+8*a*b-21*b*b-2*b-5
F1,F2 = 61*a+633*b-157, 121*a+363*b-175
ev = lambda f,x,y: factor(f.subs({a:x,b:y}))

assert simplify(L0(k)-E-N/(334200*(2*a+6*b+1))) == 0
assert simplify(L3(k)-E-F1*F2/(94200*(2*a+6*b+1))) == 0
assert simplify(L3(C)-E) == simplify(R(C)-E) == 0
assert simplify(diff(C,a)-(72*b-30)/D**2) == 0
assert simplify(diff(C,b)+(72*a+126)/D**2) == 0
assert simplify(diff(L3(c),c,2)-7*(5*a+21*b)/(2*c-7)**3) == 0
assert simplify(diff(L0(c),c)
    -(a*(2*c*c-46*c-61)+b*(6*c*c-138*c-28))/(2*(2*c-23)**2)) == 0

assert ev(diff(N,a),lo,bl)==Q(27761969,500)>0
assert ev(diff(N,b),hi,bh)==-Q(19116783,50)<0
assert ev(N,lo,bh)==Q(1792601,1000000)>0
assert ev(F1,hi,bh)==-Q(83,50)<0
assert ev(F2,hi,bh)==-Q(19,25)<0
assert ev(C,hi,bh)==Q(143,388)>k
assert ev(C,lo,bl)==Q(20587,53972)<1
assert ev(a+3*b-1,lo,bl)==Q(2993,7000)>0

assert ev(G,lo,bl)==Q(183647,600000)>0
assert ev(G,lo,bh)==Q(60981,200000)>0
assert simplify(E-(1-a)/3-G/(8*(2*a+6*b+1)))==0
assert simplify(diff(G,a)-(10*a+8*b))==0
assert simplify(diff(G,b,2)+42)==0

for av in [lo,hi]:
    for bv in [bl,bh]:
        cv, e = ev(C,av,bv), ev(E,av,bv)
        B = ev((a+3*b-1)/3,av,bv)
        assert 0<B<=bv and 0<B*(1+cv)<1 and 0<cv<1
        dq = [(1-av)/3, e-(1-av)/3, Q(0), -e]
        dp = [Q(0),Q(0),e,-e]
        assert sum(dq)==0 and sum(dp)==0
        assert sum(abs(x) for x in dq)/2==e
        assert sum(abs(x) for x in dp)/2==e

assert (hi-lo)*(bh-bl) == Q(1,262500)
print("PASS_EXACT_BU_N4_FIXED_K9_25_TAIL_CONDITIONAL_20261029")
print("L0 lower-bound gap at minimizer:",ev(L0(k)-E,lo,bh))
print("C minimum / maximum:",ev(C,hi,bh),ev(C,lo,bl))
print("additional domain area:",(hi-lo)*(bh-bl))
