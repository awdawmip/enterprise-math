"""Symbolic checks on the sharp near-stock proof, in physical positive coordinates."""
import json
from fractions import Fraction as F
import sympy as s

def check():
    # The physical spectrum as a function of A,D and independent y.
    # Under simultaneous x,y dilation A changes by u^(15/4), D is fixed.
    A,D,t,y=s.symbols("A D t y", positive=True)
    m=s.Rational(7,16)*A**4*D
    G=y**(-s.Rational(3,4))*A**4*D**5*(1-D)*t**4*(1-A*t)/(
       (1+m*t**4)*(1+m*A*t**5))
    ratio=s.factor((s.Rational(15,4)*A*s.diff(G,A)+y*s.diff(G,y)
                    +s.Rational(3,4)*G-s.Rational(15,4)*t*s.diff(G,t))/G)
    assert ratio==0
    # Check the physical census exponents, including b=1.
    sample=[]
    for c,b,L in [(16,1,2),(64,4,2),(81,9,3),(256,16,4),(1024,1024,8)]:
        z=F(b,c)
        rr=z/(L*L)
        # Here r^2=z/L^2, R0^2=1/(z L^2).
        R0_squared=rr/z**2
        assert R0_squared/c==F(1,b*L*L)
        assert rr/z==F(1,L*L)
        sample.append([c,b,L,str(R0_squared/c),str(rr/z)])
    return dict(euler_symbolic_ratio=str(ratio),
                scaled_square_identities=sample)

if __name__=="__main__":
    print(json.dumps(check(),indent=2))
