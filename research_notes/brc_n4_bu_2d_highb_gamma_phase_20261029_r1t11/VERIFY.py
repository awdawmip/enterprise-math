"""Exact author-side verification of a high-b 2D BU-N4 minimax phase.
Uses the already published four-atom all-causal reduction and observable TV duals.
This verifies algebra and exact rational witnesses, not the independent 16-leaf reduction.
"""
import sympy as S

A,B,U,V,a,b,c=S.symbols('A B U V a b c', real=True)
lo,hi=S.Rational(97,100),S.Rational(99,100)
b0=S.Rational(307,2100)
bcut1,bcut2=S.Rational(3,20),S.Rational(4,25)
c0=(2*a-7*b)/(2*a+4*b)
cp=(7-a-21*b)/(4*a+12*b+2)
e0=b*c0/4
ep=cp*(a+3*b-1)/12
c1=3*b*c0/(a+3*b-1)
R=c*(a+3*b-1)/12
L0=(4*a-14*b-3*a*c-(a+3*b)*c**2)/(2*(23-2*c))
L3=c*(a-(a+3*b)*c)/(2*(7-2*c))
Q=a*a+38*a*b-7*a+105*b*b-14*b
G=5*a*a+8*a*b-21*b*b-2*b-5
D=7*a*a+29*a*b-7*a+63*b*b-14*b
zero=lambda expr: S.cancel(expr)==0
assert zero(L0.subs(c,c0)-e0)
assert zero(L3.subs(c,c0)-e0)
assert zero(L3.subs(c,cp)-ep)
assert zero(R.subs(c,cp)-ep)
assert zero(R.subs(c,c1)-e0)
assert zero((ep-e0)+(a-1)*Q/(24*(a+2*b)*(2*a+6*b+1)))
assert zero((cp-c0)+(a-1)*(5*a+21*b)/(2*(a+2*b)*(2*a+6*b+1)))
assert zero((L3.subs(c,c1)-e0)+b*(a-1)*(2*a-7*b)*Q/(8*(a+2*b)*(a+3*b-1)*D))
assert zero((ep-(1-a)/3)-G/(8*(2*a+6*b+1)))
assert Q.subs({a:hi,b:bcut1})==-S.Rational(111,2500)<0
assert Q.subs({a:lo,b:bcut2})==S.Rational(993,2000)>0
assert (S.diff(Q,a)).subs({a:lo,b:bcut1})>0
assert (S.diff(Q,b)).subs({a:lo,b:bcut1})>0
assert 61*b0-8*hi>0    # c0 <= 3/7 throughout the new strip
assert G.subs({a:lo,b:b0})==S.Rational(1283,13125)>0
assert G.subs({a:lo,b:bcut2})==S.Rational(177,2000)>0
assert S.diff(G,b,2)==-42 and S.diff(G,a)==10*a+8*b
assert S.Rational(15,14)*S.Rational(3,7)<1 # c1 <=45/98
# Exact signed four-atom observation vectors.
s=(A-a+B-b)/2
t=(A-a+3*(B-b))/4
H=B*c/4
rQ=a/6-A*c/6-U/3-V/4
rP=a/6-A*c/6-U/12-V/2
DQ=[s,H-s-rQ,rQ,-H]
DP=[t,H-t-rP,rP,-H]

cases=[('cap-97-150',lo,bcut1,'cap'),
       ('cap-99-150',hi,bcut1,'cap'),
       ('alt-99-151',hi,S.Rational(151,1000),'alt'),
       ('alt-97-200',lo,S.Rational(1,5),'alt'),
       ('alt-99-zeroedge',hi,2*hi/7,'alt'),
       ('zero-97-300',lo,S.Rational(3,10),'zero')]
for label,av,bv,kind in cases:
    if kind=='cap':
        cv=S.factor(cp.subs({a:av,b:bv})); Bv=(av+3*bv-1)/3
        subs={a:av,b:bv,A:S.Integer(1),B:Bv,c:cv,U:Bv*(1+cv),V:Bv}
        expected=S.factor(ep.subs({a:av,b:bv}))
    elif kind=='alt':
        cv=S.factor(c0.subs({a:av,b:bv}))
        subs={a:av,b:bv,A:av,B:bv,c:cv,U:bv*(1+cv),V:bv}
        expected=S.factor(e0.subs({a:av,b:bv}))
    else:
        cv=S.Integer(0)
        subs={a:av,b:bv,A:av,B:bv,c:cv,U:2*av/7,V:2*av/7}
        expected=S.Integer(0)
    values=[S.factor(subs[u]) for u in (A,B,c,U,V)]
    assert all(0<=u<=1 for u in values)
    assert subs[U]<=subs[A] and subs[V]<=subs[B]
    q=[S.factor(v.subs(subs)) for v in DQ]
    p=[S.factor(v.subs(subs)) for v in DP]
    assert sum(q)==sum(p)==0
    tvq=S.factor(sum(map(abs,q))/2)
    tvp=S.factor(sum(map(abs,p))/2)
    assert tvq==tvp==expected,(label,tvq,tvp,expected)
    print(label,'A,B,c,U,V=',values,'TV=',expected)
# Strict counterexample to extending the capacity expression above the gamma curve.
av=hi;bv=S.Rational(151,1000)
actual=S.factor(e0.subs({a:av,b:bv}))
proposal=S.factor(ep.subs({a:av,b:bv}))
assert 0 < proposal-actual
assert Q.subs({a:av,b:bv})>0
print('high-b strict capacity failure at (99/100,151/1000):',
      'e_alt=',actual,'e_cap=',proposal,'gap=',proposal-actual)
print('PASS_EXACT_BU_N4_TWO_DIMENSIONAL_HIGHB_SWITCH_20261029')
