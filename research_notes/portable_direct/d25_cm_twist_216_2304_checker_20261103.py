#!/usr/bin/env python3
"""Exact source-labelled E3/E4 CM twist and F_(p^2) point-count checker.

AUTHOR-SIDE / EXACT ARITHMETIC / NO NATIVE H0-B0 EXPERIMENT.
The curves are the d=3,4 Chisholm--Deines--Long--Nebe--Swisher
hypergeometric elliptic families.  This checker does not assert a
p^3-level transfer of their truncated hypergeometric periods.
"""
from dataclasses import dataclass
from fractions import Fraction
import json

@dataclass(frozen=True)
class K2:
    a: Fraction
    b: Fraction = Fraction(0)

    def __add__(self, other):
        other = other if isinstance(other, K2) else K2(Fraction(other))
        return K2(self.a + other.a, self.b + other.b)
    __radd__ = __add__

    def __neg__(self):
        return K2(-self.a, -self.b)
    def __sub__(self, other):
        return self + (-other if isinstance(other, K2) else -Fraction(other))
    def __rsub__(self, other):
        return (-self) + other

    def __mul__(self, other):
        other = other if isinstance(other, K2) else K2(Fraction(other))
        return K2(self.a * other.a + 2 * self.b * other.b,
                  self.a * other.b + self.b * other.a)
    __rmul__ = __mul__

    def inverse(self):
        norm = self.a*self.a - 2*self.b*self.b
        assert norm
        return K2(self.a/norm, -self.b/norm)
    def __truediv__(self, other):
        other = other if isinstance(other, K2) else K2(Fraction(other))
        return self * other.inverse()
    def __rtruediv__(self, other):
        return self.inverse() * other
    def __pow__(self, exponent):
        if exponent < 0:
            return (self.inverse()) ** (-exponent)
        out, base = K2(Fraction(1)), self
        while exponent:
            if exponent & 1:
                out = out * base
            base *= base
            exponent >>= 1
        return out

S = K2(Fraction(0), Fraction(1))
t3 = (2-S)/4
t4 = (3-2*S)/6
d = 3*S
assert -4*t3*(t3-1) == K2(Fraction(1, 2))
assert -4*t4*(t4-1) == K2(Fraction(1, 9))

# E3: y^2 + x*y + (t3/27)*y = x^3,
# E4: y^2 = x^3+x^2+(t4/4)*x.
c4_3 = (5+2*S)/9
c6_3 = -(12+7*S)/27
c4_4 = 16-12*t4
c6_4 = -64+72*t4
assert c4_4 == d*d*c4_3
assert c6_4 == d**3*c6_3
# E3 and E4 have j = 2417472 + 1707264 sqrt(2).
# E3 discriminant is t3^3 (1-t3) / 27^3.
delta3 = t3**3 * (1-t3) / 27**3
delta4 = t4**2*(1-t4)
assert delta4 == d**6 * delta3
j3 = c4_3**3 / delta3
j4 = c4_4**3 / delta4
assert j3 == j4 == 2417472 + 1707264*S

# Change x4=d*x3 + e, y4=u^3*(y3 + (x3+t3/27)/2), u^2=d.
# In x3, the E3-square-completed RHS times d^3 must equal E4 RHS.
e = d/12 - K2(Fraction(1,3))
b = t3/27
coeff_left = (d**3 * b**2/4, d**3*b/2, d**3/4, d**3)
coeff_right = (e**3+e**2+(t4/4)*e,
               d*(3*e*e+2*e+t4/4), d*d*(3*e+1), d**3)
assert coeff_left == coeff_right

# Exact finite-field K/p = F_p[s]/(s^2-2), p in the two inert classes.
def field_ops(p):
    def mul(a,b):
        return ((a[0]*b[0]+2*a[1]*b[1])%p,
                (a[0]*b[1]+a[1]*b[0])%p)
    def power(a,n):
        res = (1,0)
        while n:
            if n&1:
                res = mul(res,a)
            a = mul(a,a)
            n >>= 1
        return res
    def character(a):
        if a == (0,0):
            return 0
        v = power(a,(p*p-1)//2)
        assert v in ((1,0),(p-1,0)),(p,a,v)
        return 1 if v==(1,0) else -1
    return mul, power, character

def get_trace(p):
    assert p%24 in (13,19)
    mul,power,chi=field_ops(p)
    inv=lambda v: pow(v,-1,p)
    s=(0,1)
    t3=((2*inv(4))%p,-inv(4)%p)
    t4=((3*inv(6))%p,(-2*inv(6))%p)
    b=mul(t3,(inv(27),0))
    c=mul(t4,(inv(4),0))
    trace3=trace4=0
    for a in range(p):
        for bb in range(p):
            x=(a,bb)
            x2=mul(x,x)
            x3=mul(x2,x)
            v=(x[0]+b[0],(x[1]+b[1])%p)
            v2=mul(v,v)
            # Four times completed square of E3.
            f3=((4*x3[0]+v2[0])%p,(4*x3[1]+v2[1])%p)
            cx=mul(c,x)
            f4=((x3[0]+x2[0]+cx[0])%p,(x3[1]+x2[1]+cx[1])%p)
            trace3 -= chi(f3)
            trace4 -= chi(f4)
    d=(0,3%p)
    norm_d=(-18)%p
    twist=chi(d)
    norm_char=pow(norm_d,(p-1)//2,p)
    assert norm_char == (1 if twist==1 else p-1)
    assert twist == (-1 if p%24==13 else 1)
    assert trace4 == twist*trace3
    return dict(p=p,q=p*p,p_mod_24=p%24,character_d_over_Fp2=twist,
                norm_d_mod_p=norm_d,trace_E3=trace3,trace_E4=trace4,
                curve_3="y^2+xy+(t3/27)y=x^3",
                curve_4="y^2=x(x^2+x+t4/4)")

if __name__ == '__main__':
    rows=[get_trace(p) for p in (13,19,37,43,109,373)]
    print(json.dumps({
        'status':'EXACT_SYMBOLIC_IDENTITIES_AND_EXACT_FINITE_FIELD_COUNTS_PASS',
        'model':'EXTERNAL_CM_ELLIPTIC_CURVES_NOT_NATIVE_H0_B0',
        'source_observers':'E3 lambda=1/2, E4 lambda=1/9; p^2-Frobenius trace',
        'symbolic_identity':'c4_4=d^2*c4_3,c6_4=d^3*c6_3,delta4=d^6*delta3',
        'shared_j':'2417472 + 1707264 sqrt(2)',
        'twist_parameter':'d=3 sqrt(2)',
        'exact_isomorphism':'x4=d*(x3+1/12)-1/3; y4=u^3*(y3+(x3+t3/27)/2), u^2=d',
        'theorem':'a_p^2(E4)=chi_Fp2(d)*a_p^2(E3)',
        'not_proved':'weighted truncated 216 p^3 supercongruence and native experiment',
        'results':rows
    },indent=2,ensure_ascii=False))
