"""Exact certificates for the two final placements of a 5 and the asymptotic scale."""
from fractions import Fraction as Q
from math import factorial
import json

LAMBDA = Q(42, 4225)

def coefficients(r):
    a = Q((9*r+4)*(9*r+5), 14*(6*r+1)*(6*r+5))
    beta = Q(3*(9*r+4)*(9*r+5), 56*(3*r+1)*(3*r+2)*(6*r+1)*(6*r+5))
    return 1+a, beta

def interval(k):
    x, y = Q(0), Q(1)
    for j in reversed(range(3, k)):
        alpha, beta = coefficients(j)
        x, y = 1/(alpha-beta*x), 1/(alpha-beta*y)
    return x, y

def l_b(u):
    return Q(76032, 65)*((62216-115*u)/(537448+12213*u))**2

def l_c(u):
    return Q(21676032, 25)*((62216-115*u)/(11696360+267237*u))**2

def outward(x, digits, upper=False):
    numerator = x.numerator * 10**digits
    if upper:
        numerator += x.denominator-1
    approx = numerator//x.denominator
    return f"{approx//10**digits}.{approx%10**digits:0{digits}d}"

def verify_symbolic():
    import sympy as s
    u, r, t = s.symbols("u r t")
    def f(r, c, m, x):
        K, h = 2*r+1, c-m
        rho = s.Rational(K+4*h, K+h)
        tau = s.Rational(28*(K+4*h)*(K+4*h-1), (4*K+h)*(K+h-1))
        for j in range(h+1, c+1):
            rho *= s.Rational(K+4*j, 4*(K+j))
            tau *= s.Rational(K+4*j, 4*(4*K+j))
        return s.factor(tau/(tau+1+(rho-1)*x))
    A = f(1,2,0, f(2,3,1,u))
    B = f(1,3,1, f(2,3,0,u))
    E = f(1,3,0, f(2,3,0,u))
    C = s.factor(128*(1-E)/(68-3*E))
    for expr in (s.diff(B,u)/s.diff(A,u)+l_b(u), s.diff(C,u)/s.diff(A,u)-l_c(u)):
        assert s.cancel(expr) == 0
    a = (9*r+4)*(9*r+5)/(14*(6*r+1)*(6*r+5))
    beta = 3*(9*r+4)*(9*r+5)/(56*(3*r+1)*(3*r+2)*(6*r+1)*(6*r+5))
    P = r*(r+1)*beta/((1+a)*(1+a-beta)*LAMBDA)
    assert s.limit(s.factor((1-P)*r*r), r,s.oo) == s.Rational(698,5265)
    assert s.limit(s.factor(r*r*beta/(1+a)),r,s.oo) == s.Rational(3,260)
    assert Q(698,5265)-Q(3,260)*Q(47,65) == Q(170059,1368900)
    for gap in (P-1+1/(6*r*r), 1-P-1/(63*(r-1)**2),
                s.Rational(1,4)-a, 1/(64*r*r)-beta):
        numerator, denominator = s.factor(s.cancel(gap.subs(r,t+3))).as_numer_denom()
        assert all(x>0 for poly in (numerator,denominator) for x in s.Poly(poly,t).all_coeffs())
    for h in (l_b(u),l_c(u)):
        d = s.cancel(-s.diff(h,u)/h)
        # On [0,1], combine monotone endpoint bounds on the two summands of -log L'.
        m, q = (12213,537448) if h==l_b(u) else (267237,11696360)
        assert s.cancel(d - 2*(115/(62216-115*u)+m/(q+m*u))) == 0
        assert Q(1,25)<2*(Q(115,62216)+Q(m,q+m))
        assert 2*(Q(115,62101)+Q(m,q))<Q(3,50)
    return {"A":str(A),"B":str(B),"8p2_C":str(C)}

def run():
    symbolic=verify_symbolic()
    x,y=interval(18)
    constants={name:[outward(h(y),50),outward(h(x),50,True)] for name,h in (("B",l_b),("C",l_c))}
    n=200
    xx,yy=interval(n)
    v=(yy-xx)*factorial(n-1)*factorial(n)/LAMBDA**(n-3)
    w_lower,w_upper=v*(1-Q(1,6*(n-1))), v
    a_lower=w_lower*127075/(8*(62216-115*x)**2)
    a_upper=w_upper*127075/(8*(62216-115*y)**2)
    return {"tail_functions":symbolic,"ratio_limits_from_k18":constants,
            "W_constant_from_k200":[outward(w_lower,10),outward(w_upper,10,True)],
            "A_constant_from_k200":[outward(a_lower,12),outward(a_upper,12,True)]}

if __name__=="__main__":
    print(json.dumps(run(), indent=2))
