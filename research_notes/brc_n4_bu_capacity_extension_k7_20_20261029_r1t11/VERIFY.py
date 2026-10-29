"""Exact algebra check for the newly extended BU N=4 capacity rectangle.
External finite signed-measure model only; no native heartbeat/BRC execution.
"""
import sympy as S

a,b,c,A,B,U,V=S.symbols('a b c A B U V',real=True)
k=S.Rational(7,20)
a0,a1=S.Rational(97,100),S.Rational(99,100)
b0,b1=S.Rational(1,8),S.Rational(307,2100)
L0=(4*a-14*b-3*a*c-(a+3*b)*c**2)/(2*(23-2*c))
L3=c*(a-(a+3*b)*c)/(2*(7-2*c))
cc=(7-a-21*b)/(4*a+12*b+2)
ecap=cc*(a+3*b-1)/12
G=5*a*a+8*a*b-21*b*b-2*b-5
N=9016*a*a+39396*a*b-14447*a+37044*b*b-110901*b+15610
assert S.simplify((L0.subs(c,k)-ecap)-N/(53520*(2*a+6*b+1)))==0
assert S.simplify((L3.subs(c,k)-ecap)-(7*a+21*b-10)*(8*a+84*b-21)/(720*(2*a+6*b+1)))==0
assert S.simplify((ecap-(1-a)/3)-G/(8*(2*a+6*b+1)))==0
assert S.simplify(L3.subs(c,cc)-ecap)==0
assert cc.subs({a:a1,b:b1})==S.Rational(343,900)>k
assert (L0.subs(c,k)-ecap).subs({a:a0,b:b1})==S.Rational(89369,74482000)>0
assert (7*a+21*b-10).subs({a:a1,b:b1})==0
assert (8*a+84*b-21).subs({a:a1,b:b1})==-S.Rational(4,5)
assert N.diff(a).subs({a:a0,b:b0})>0
assert N.diff(b).subs({a:a1,b:b1})<0
assert (G.subs({a:a0,b:b0}),G.subs({a:a0,b:b1}))==(S.Rational(771,8000),S.Rational(1283,13125))
assert G.diff(a).subs({a:a0,b:b0})>0
# G is concave in b, so b-endpoint minima suffice after a-monotonicity.
assert S.diff(G,b,2)<0
N0=131*a*a+576*a*b-232*a+549*b*b-1746*b+245
assert N0.subs({a:a0,b:S.Rational(13,100)})==-S.Rational(2313,1250)<0
assert cc.subs({a:a0,b:S.Rational(13,100)})==S.Rational(55,124)
assert ecap.subs({a:a0,b:S.Rational(13,100)})==S.Rational(33,2480)
# Rebuild the exact signed 4-observation-atom marginal law for a fresh rational witness.
sv=(A-a+B-b)/2;tv=(A-a+3*(B-b))/4;H=B*c/4
rQ=a/6-A*c/6-U/3-V/4;rP=a/6-A*c/6-U/12-V/2
DQ=S.Matrix([sv,H-sv-rQ,rQ,-H]);DP=S.Matrix([tv,H-tv-rP,rP,-H])
for av,bv in ((a0,S.Rational(13,100)),(a0,b1),(a1,b1)):
 cv=cc.subs({a:av,b:bv});Bv=(av+3*bv-1)/3
 subs={a:av,b:bv,A:S.Integer(1),B:Bv,c:cv,U:Bv*(1+cv),V:Bv}
 assert all(S.Rational(0)<=v<=1 for v in (Bv,cv,Bv*(1+cv)))
 e=ecap.subs({a:av,b:bv});q=[S.factor(x.subs(subs)) for x in DQ];p=[S.factor(x.subs(subs)) for x in DP]
 assert sum(map(abs,q))/2==sum(map(abs,p))/2==e
 assert q[0]==(1-av)/3 and q[1]==e-(1-av)/3 and q[2]==0 and q[3]==-e
 assert p==[0,0,e,-e]
print('PASS_EXACT_BU_N4_EXTENDED_CAPACITY_2D_20261029')
