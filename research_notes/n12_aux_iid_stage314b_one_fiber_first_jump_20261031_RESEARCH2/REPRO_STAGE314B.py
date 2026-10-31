#!/usr/bin/env python3
"""Stage314-B: exact one-fiber first-order Pareto transition.

Fraction arithmetic checks 128 atom probabilities at rational rates;
Q(sqrt(13)) checks algebraic witness and strict endpoint bounds.
SymPy checks the exact residual/derivative polynomial identities.
The universal minimization is proved in PROOF_STAGE314B.md, not by sampling.
"""
from collections import defaultdict
from dataclasses import dataclass
from fractions import Fraction as F
from itertools import product
import sympy as sp

@dataclass(frozen=True)
class Q13:
    a: F = F(0)
    b: F = F(0)
    def __init__(self, a=0, b=0):
        object.__setattr__(self, "a", F(a)); object.__setattr__(self, "b", F(b))
    @staticmethod
    def cv(x): return x if isinstance(x, Q13) else Q13(x)
    def __add__(self,o):
        o=self.cv(o); return Q13(self.a+o.a,self.b+o.b)
    __radd__=__add__
    def __neg__(self): return Q13(-self.a,-self.b)
    def __sub__(self,o): return self+(-self.cv(o))
    def __rsub__(self,o): return self.cv(o)-self
    def __mul__(self,o):
        o=self.cv(o); return Q13(self.a*o.a+13*self.b*o.b,self.a*o.b+self.b*o.a)
    __rmul__=__mul__
    def __truediv__(self,o):
        o=self.cv(o); den=o.a*o.a-13*o.b*o.b
        assert den; return self*Q13(o.a/den,-o.b/den)
    def __pow__(self,k):
        assert isinstance(k,int) and k>=0
        out=Q13(1)
        for _ in range(k):out=out*self
        return out
    def sign(self):
        a,b=self.a,self.b
        if not b: return (a>0)-(a<0)
        if not a: return (b>0)-(b<0)
        if (a>0)==(b>0):return (a>0)-(a<0)
        lhs=a*a;rhs=13*b*b
        assert lhs!=rhs
        return ((a>0)-(a<0)) if lhs>rhs else ((b>0)-(b<0))
    def __abs__(self):return self if self.sign()>=0 else -self
    def __lt__(self,o):return (self-self.cv(o)).sign()<0
    def __le__(self,o):return (self-self.cv(o)).sign()<=0
    def __eq__(self,o):
        o=self.cv(o);return self.a==o.a and self.b==o.b
    def __str__(self):return str(self.a) if not self.b else f"({self.a})+({self.b})*sqrt(13)"

H=("000","001","010","011","100","101","110","111")
AB=((63,1),(21,3),(21,3),(7,9),(9,7),(3,21),(3,21),(1,63))
WORDS=tuple(product((0,1),repeat=3))
MAP=tuple(Q13(F(1,4)) if a>b else Q13(F(3,4)) for a,b in AB)


def prob_word(p,word):
    k=sum(word);return p**k*(Q13(1)-p)**(3-k)

def totalvariation(d1,d2):
    return sum((abs(d1.get(k,Q13())-d2.get(k,Q13())) for k in d1.keys()|d2.keys()),Q13())/2

def risk(rate):
    assert len(rate)==8
    tc=defaultdict(Q13);tt=defaultdict(Q13)
    pc=defaultdict(Q13);pt=defaultdict(Q13)
    for idx,h in enumerate(H):
        j,w,y=(int(z) for z in h)
        for s,m in enumerate(AB[idx]):
            p=Q13(F(1,4) if s==0 else F(3,4))
            for word in WORDS:
                a=Q13(m)/256*prob_word(p,word)
                b=Q13(m)/256*prob_word(rate[idx],word)
                ka=(s,j,w,y,word); kb=(w,y,word)
                tt[ka]+=a;tc[ka]+=b;pt[kb]+=a;pc[kb]+=b
    assert sum(tt.values(),Q13())==Q13(1)
    assert sum(tc.values(),Q13())==Q13(1)
    return totalvariation(pc,pt),totalvariation(tc,tt)

def one(t):
    rates=list(MAP);rates[4]=Q13.cv(t)
    return risk(rates)

def q(u):
    u=Q13.cv(u);return Q13(F(9,128))*u+Q13(F(3,32))*u*u-u**3/8

def g(u):
    u=Q13.cv(u);return Q13(F(117,4096))*u-Q13(F(123,1024))*u*u+Q13(F(23,256))*u**3

P0,T0=risk(MAP)
assert P0==Q13(F(11,256)) and T0==Q13(F(77,1024))
assert sum(a+b for a,b in AB)==256

# Path-resolved MAP public residuals in G=00, k=0..3.
t=sp.symbols('t',real=True);u=sp.symbols('u',real=True)
Bk=lambda k,p:p**k*(1-p)**(3-k)
R=[sp.factor(sp.Rational(v,1024)+(Bk(k,t)-Bk(k,sp.Rational(1,4)))/16) for k,v in enumerate((13,3,-3,-13))]
assert [sp.factor(512*r) for r in R]==[
    -32*t**3+96*t*t-96*t+25,
    32*t**3-64*t*t+32*t-3,
    -32*t**3+32*t*t-3,
    32*t**3-7]

Q=sp.Rational(9,128)*u+sp.Rational(3,32)*u*u-u**3/8
G=sp.Rational(117,4096)*u-sp.Rational(123,1024)*u*u+sp.Rational(23,256)*u**3
assert sp.simplify(sp.diff(Q,u)+3*(4*u-3)*(4*u+1)/128)==0
assert sp.simplify(sp.diff(G,u)-3*(4*u-3)*(92*u-13)/4096)==0
# First public-chamber flip is k=2. Rational root isolation and strict ordering:
f2=lambda z:32*z*z*(1-z)-3
assert f2(F(392,1000))<0<f2(F(393,1000))
assert f2(F(1,4)+F(13,92))<0
# k=0 follows; its cubic root in (397/1000,398/1000).
f0=lambda z:32*(1-z)**3-7
assert f0(F(397,1000))>0>f0(F(398,1000))
assert F(393,1000)<F(397,1000)

s13=Q13(0,1)
tdag=(Q13(7)-s13)/8
udag=tdag-Q13(F(1,4))
Pdag,Tdag=one(tdag)
Edag=P0-Pdag
assert Q13(F(424,1000))<tdag<Q13(F(425,1000))
assert Pdag==Q13(F(-1,32),F(9,512))
assert Tdag==Q13(F(319,4096),F(-1,4096))
assert Edag==Q13(F(19,256),F(-9,512))
assert Edag<q(F(7,50)) and F(7,50)<F(13,92)
assert q(F(11,100))<Edag
assert g(F(109,1000))<Tdag-T0<g(F(11,100))
assert F(13,92)<F(142,1000)<F(143,1000) and Q13(F(143,1000))<udag
assert g(udag)==Tdag-T0
# For t>=3/4, the source-tagged risk exceeds the dagger risk by the simple D3 lower bound.
assert Q13(F(11,2048))>Tdag-T0

# Literal 128-atom exact recomputations in multiple sign chambers.
samples=(F(1,5),F(1,4),F(35,100),F(392,1000),F(393,1000),F(2,5),F(42,100),F(1,2),F(3,4),F(1))
for z in samples:
    pp,tt=one(z)
    assert Q13(0)<=pp<=Q13(1) and Q13(0)<=tt<=Q13(1)
    if z<F(1,4): assert pp>P0
    if F(1,4)<=z<=F(392,1000):
        eps=z-F(1,4)
        assert pp==P0-q(eps) and tt==T0+g(eps)
    if z>=F(1,2): assert tt>Tdag

# The first switch is a unique algebraic root in (109/1000, 11/100).
# Its epsilon interval is q at the two exact rational endpoints.
print('MODEL_POSITIVE_MASS: 256/256; TAGGED_ATOMS: 128; PUBLIC_ATOMS: 32')
print('MAP_PUBLIC:',P0,'MAP_TAGGED:',T0)
print('FIRST_PUBLIC_SIGN_FLIP: k=2, root 32*t^2*(1-t)-3=0, t in (392/1000,393/1000)')
print('SECOND_PUBLIC_SIGN_FLIP: k=0, t in (397/1000,398/1000)')
print('TAGGED_COST_LOCAL_MAX_U: 13/92 (BEFORE FIRST PUBLIC FLIP)')
print('DAGGER_RATE:',tdag)
print('DAGGER_PUBLIC:',Pdag,'DAGGER_TAGGED:',Tdag)
print('DAGGER_PUBLIC_GAIN_E:',Edag)
print('ONE_FIBER_TRANSITION_U_BRACKET:',F(109,1000),F(11,100))
print('ONE_FIBER_TRANSITION_E_BRACKET:',q(F(109,1000)),q(F(11,100)))
print('ONE_FIBER_ENVELOPE: min(T0+g(q^-1(epsilon)),Tdag), 0<=epsilon<=Edag')
print('ACTUAL_RATIONAL_ATOM_RECOMPUTATIONS:',len(samples))
print('STAGE314B_ONE_FIBER_FIRST_ORDER_TRANSITION_EXACT_PASS')
