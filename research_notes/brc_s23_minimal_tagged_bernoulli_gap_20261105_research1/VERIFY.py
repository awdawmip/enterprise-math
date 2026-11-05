#!/usr/bin/env python3
"""Exact standalone certificate: minimal tagged Bernoulli witness for S23 box.
Uses only Fraction and integer comparisons in Q(sqrt(43)); no floating point.
"""
from dataclasses import dataclass
from fractions import Fraction as F
from itertools import combinations, product

@dataclass(frozen=True)
class R:
    # p+q*sqrt(43)
    p: F
    q: F=F(0)
    def __init__(self, p=0, q=0):
        object.__setattr__(self, 'p', F(p))
        object.__setattr__(self, 'q', F(q))
    def __add__(self, other):
        z=cast(other)
        return R(self.p+z.p, self.q+z.q)
    __radd__=__add__
    def __neg__(self): return R(-self.p,-self.q)
    def __sub__(self, other): return self+(-cast(other))
    def __rsub__(self, other): return cast(other)-self
    def __mul__(self, other):
        z=cast(other)
        return R(self.p*z.p+43*self.q*z.q, self.p*z.q+self.q*z.p)
    __rmul__=__mul__
    def __truediv__(self, other):
        z=cast(other)
        den=z.p*z.p-43*z.q*z.q
        assert den != 0
        return R((self.p*z.p-43*self.q*z.q)/den, (self.q*z.p-self.p*z.q)/den)
    def sign(self):
        if self.q==0: return (self.p>0)-(self.p<0)
        if self.p==0: return (self.q>0)-(self.q<0)
        if self.p>0 and self.q>0: return 1
        if self.p<0 and self.q<0: return -1
        cmp=(self.p*self.p>43*self.q*self.q)-(self.p*self.p<43*self.q*self.q)
        return cmp if self.p>0 else -cmp
    def __lt__(self, other): return (self-cast(other)).sign()<0
    def __le__(self, other): return (self-cast(other)).sign()<=0
    def __gt__(self, other): return (self-cast(other)).sign()>0
    def __ge__(self, other): return (self-cast(other)).sign()>=0
    def __eq__(self, other):
        try: z=cast(other)
        except (TypeError, ValueError): return False
        return self.p==z.p and self.q==z.q
    def __repr__(self): return f'({self.p})+({self.q})sqrt(43)'

def cast(x): return x if isinstance(x,R) else R(x)
def absolute(x): return -x if x<0 else x

def F4(a,b,c):
    return (a,(1-a)*b,(1-a)*(1-b)*c,(1-a)*(1-b)*(1-c))

def tagged(a,b):
    # Bernoulli event probabilities for (AV,stop1); (AU0,stops3+4); (BU0,stop2).
    return (a,(1-a)*(1-b),F(3,4)*b)

aval=(F(1,2),F(7,8))
bval=(F(1,8),F(1,2))
cval=(F(1,2),F(7,8))
vertices=[(a,b,c) for a,b,c in product(aval,bval,cval)]

# The original four-stop laws must project to precisely these event coordinates.
for a,b,c in vertices:
    au=F4(a,b,F(1,2)); av=F4(a,F(0),c); bu=F4(F(1,4),b,F(1,2))
    assert tuple(map(sum,[(av[0],),(au[2],au[3]),(bu[1],)]))==tagged(a,b)
    assert all(sum(row)==1 for row in (au,av,bu))
print('PASS_SOURCE_EVENT_IDENTITIES: eight complete-parameter vertices, source labels retained')

# Exact radical root and permitted lawful witness.
s=R(0,1)
r=(s-5)/8
assert 32*r*r+40*r-9==0
assert R(F(3,16))<r<R(F(1,5))
x=R(F(7,8))-r
y=R(F(1,2))-F(4,3)*r
assert R(aval[0])<=x<=R(aval[1])
assert R(bval[0])<=y<=R(bval[1])
assert (1-x)*(1-y)==R(F(7,16))-r
assert F(3,4)*y==R(F(3,8))-r

# For each Bernoulli coordinate TV(Bern(u),Bern(v))=|u-v|.
q_center=tagged(x,y)
errs=[absolute(cast(tagged(a,b)[j])-q_center[j]) for (a,b,_) in vertices for j in range(3)]
assert max(errs)==r
print('PASS_TRIPLE_LAWFUL_UPPER: center (7/8-r,1/2-4r/3), exact radius r')

# A 3-event lower certificate: r0>=7/8-x, 7/16-(1-x)(1-y), (3/4)(1/2-y)
# thus 32*r0^2+40*r0-9>=0 and r0>=r.  Polynomial increasing for r0>=0.
assert R(F(1,8))+r == 1-x
assert R(F(1,2))+F(4,3)*r == 1-y
assert (R(F(1,8))+r)*(R(F(1,2))+F(4,3)*r) == R(F(7,16))-r
print('PASS_TRIPLE_LAWFUL_LOWER: exact root and saturated three-event inequalities')

# Same weights mix COMPLETE joint strategies, not independently chosen row centers.
vertices4=[(F(1,2),F(1,8)),(F(1,2),F(1,2)),(F(7,8),F(1,8)),(F(7,8),F(1,2))]
weights=(F(4,9),F(1,18),F(2,9),F(5,18))
assert sum(weights)==1
hull_center=tuple(sum(w*tagged(a,b)[j] for w,(a,b) in zip(weights,vertices4)) for j in range(3))
assert hull_center==(F(11,16),F(1,4),F(3,16))
assert max(abs(tagged(a,b)[j]-hull_center[j]) for a,b,_ in vertices for j in range(3))==F(3,16)
# Feature 1 alone has extrema 1/2 and 7/8, so every possible hull center radius>=3/16.
assert (aval[1]-aval[0])/2==F(3,16)
assert r>R(F(3,16))
print('PASS_TRIPLE_CONVEX_HULL: exact joint mixture, radius 3/16, gap (2sqrt43-13)/16')

# Every proper subset of these exact 3 tagged binary observers has zero gap.
# Each center is a lawful TWO-parameter strategy. The last coordinate c is arbitrary.
subset_witnesses={
 (0,):(F(11,16),F(1,5)),
 (1,):(F(11,16),F(1,5)),
 (2,):(F(11,16),F(5,16)),
 (0,1):(F(11,16),F(1,5)),
 (0,2):(F(11,16),F(5,16)),
 (1,2):(F(7,11),F(5,16)),
}
for subset,center in sorted(subset_witnesses.items()):
    a0,b0=center
    assert aval[0]<=a0<=aval[1] and bval[0]<=b0<=bval[1]
    q0=tagged(a0,b0)
    actual=max(abs(tagged(a,b)[i]-q0[i]) for a,b,_ in vertices for i in subset)
    lower=max((max(tagged(a,b)[i] for a,b,_ in vertices)-min(tagged(a,b)[i] for a,b,_ in vertices))/2 for i in subset)
    assert actual==lower
    assert lower==(F(9,64) if subset==(2,) else F(3,16))
    print('PASS_PROPER_SUBSET',subset,'lawful=hull=',actual)

print('PASS_EXACT_S23_TAGGED_TRIPLE_MINIMAL_GAP_20261105')
