import sympy as s
z=s.symbols('z'); I=s.I
class Jet:
    def __init__(self,v,d=0,e=0):self.v,self.d,self.e=map(s.sympify,(v,d,e))
    def __add__(self,o):
        o=j(o);return Jet(self.v+o.v,self.d+o.d,self.e+o.e)
    __radd__=__add__
    def __neg__(self):return Jet(-self.v,-self.d,-self.e)
    def __sub__(self,o):return self+-j(o)
    def __rsub__(self,o):return j(o)+-self
    def __mul__(self,o):
        o=j(o);return Jet(self.v*o.v,self.d*o.v+self.v*o.d,self.e*o.v+2*self.d*o.d+self.v*o.e)
    __rmul__=__mul__
    def inv(self):
        v,d,e=self.v,self.d,self.e
        return Jet(1/v,-d/v**2,2*d**2/v**3-e/v**2)
    def __truediv__(self,o):return self*j(o).inv()
    def __rtruediv__(self,o):return j(o)*self.inv()
    def __repr__(self):return str((self.v,self.d,self.e))
def j(x):return x if isinstance(x,Jet) else Jet(x)
def power(p):return Jet(I**p,p*I**p,p*p*I**p)
def P(a,b):return a*b
def M(a,b):return (1-a*b*z*z)/((1-a*z)*(1-b*z)*(1-a*b*z))
def T(a,b,c):return (1-a*b*c*z**3)/((1-a*b*c*z**2)*(1-a*z)*(1-b*z)*(1-c*z))
def S(a,b,c):return M(b,c)/(1-a*z)+M(a,c)/(1-b*z)+M(a,b)/(1-c*z)-T(a,b,c)
def event(S):
    out=Jet(z/(1-z))
    for p in S:out=out/(1-z*power(p))
    return out
F0,F1,F2=[event(S) for S in ([214,215,216,217,218],[214,216,217,218,219,220,221],[215,216,217,218,219,220,221])]
base=Jet(z/(1-z))
for p in range(216,219): base=base/(1-z*power(p))
hsum=Jet(0)
for r in (219,220,221):
    c=Jet(1)
    for ss in (219,220,221):
        if ss!=r:c=c/(1-power(ss-r))
    hsum=hsum+c*S(power(214),power(215),power(r))
Fh=base*hsum
b0=s.Integer(12780)-24*I;b1=s.Integer(12558)+s.Rational(169,2)*I;b2=s.Rational(25115,2)-23*I;bh=s.Rational(24901,2)-23*I
D=lambda f:-f.d
G=(F0.e-F0.d)/2+(b0+s.Rational(23,2))*D(F0)+220*(1-I)*((b1+s.Rational(23,2))*F1.v+D(F1))+220*((b2+s.Rational(23,2))*F2.v+D(F2))-440*((bh+s.Rational(23,2))*Fh.v+D(Fh))

# Author certificate: generating series restricted to even m via z -> -z.
R=(-110 + (8033772-41446*I)*z**2 + (10499950+4893440*I)*z**4
   +(-7284728+59598*I)*z**6 +(-12770418-6606800*I)*z**8
   +(-3019732-22442*I)*z**10 -110*z**12 -110*I*z**14)
D0=(1-z**2)**4*(1+z**2)**4
parts=[(F0.e-F0.d)/2+(b0+s.Rational(23,2))*D(F0),
       220*(1-I)*((b1+s.Rational(23,2))*F1.v+D(F1)),
       220*((b2+s.Rational(23,2))*F2.v+D(F2)),
       440*(Fh.d-(bh+s.Rational(23,2))*Fh.v)]
total=s.Poly(0,z,extension=I)
for part in parts:
    p=s.cancel(part,extension=I)
    ev=s.cancel((p+p.subs(z,-z))/2,extension=I)
    r=s.cancel((ev - 110/(1-I*z**2) if part is parts[-1] else ev)*D0,extension=I)
    total+=s.Poly(r,z,extension=I)
assert total==s.Poly(R,z,extension=I)
print('PASS symbolic rational-function identity for E_2k; exact Gaussian rational arithmetic')
