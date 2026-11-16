"""Exact resonance, gradient coprimality and asymmetric-center secant checks.

Run with Python 3 and SymPy. The resultant and both gcds are over Q.
"""
from fractions import Fraction
import json
import sympy as sp


def resonance_certificate():
    k, d, j = sp.symbols("k d j")
    rat = sp.Rational
    a = rat(1, 112)
    t = a / 4
    slope = (-rat(5, 4) - 15*a/(1+a) - rat(75, 4)*t/(1+t)
             + 15*k*a/(1+k*a))
    assert sp.factor(slope - 20*(34439*k-404740)/(50737*(k+112))) == 0
    K = rat(404740, 34439)
    assert K < 256
    # H = x^-3 (1+112 x^15/K)^-1 d^-16/3 (1-1/d)^eta.
    # Along its level set beta = d log d / d log x.
    def beta(eta):
        return (3+1680/(K+112))/(-rat(16, 3)+eta/(d-1))

    def log_width(A, B, vel, with_inner=True):
        together = rat(75, 4) + vel
        outer = (-rat(3, 4)+rat(75, 4)+rat(15, 4)*A/(A-1)
                 -B*d*together/(1+B*d)
                 -(rat(15,4)*A+B*d*together)/(A+B*d))
        if with_inner:
            outer += (rat(14, 3)+d/(d-1))*vel
        return sp.factor(outer)

    b = beta(0)
    low = log_width(4, 448, b)
    diff = sp.factor(log_width(4/j, 448/(K*j), b, False)
                     -log_width(4, 448, b, False))
    low_num = sp.fraction(low)[0]
    diff_num = sp.fraction(diff)[0]
    proj = sp.resultant(diff_num, j**4-K, j)
    assert sp.Poly(sp.gcd(low_num, proj), d).degree() == 0
    assert sp.Poly(sp.gcd(diff_num.subs(d, 1), j**4-K), j).degree() == 0
    edge = log_width(4,448,beta(1)).subs(d,4)
    assert edge == -rat(4529966025803, 163384708036)
    threshold = sp.solve((1+a)*(1+t) - (1+k*a), k)
    assert threshold == [rat(561,448)]
    return dict(resonant_K=str(K),log_gradient=sp.sstr(sp.factor(slope)),
                short_middle_corner_log_gradient=str(edge),
                positive_zero_tail_K=str(threshold[0]),
                first_numerator_degree=int(sp.degree(low_num,d)),
                ratio_numerator_degrees=[int(sp.degree(diff_num,v)) for v in (d,j)],
                resultant_degree=int(sp.degree(proj,d)), result_gcd_degree=0,
                sync_ratio_numerator_gcd_degree=0)


def exact_secants():
    F=Fraction
    count=0
    for a in (F(1,112),F(5,649),F(11,767)):
        for t in (a/4,2*a/7):
            for lo,hi in ((F(1,530),F(5,74)),(F(63,64),F(127,128))):
                for k in (F(2),F(9,4),F(404740,34439)):
                    def value(aa,tt,p):
                        return (1+tt*p)/(1+aa*p)
                    old=value(a,t,lo)/value(a,t,hi)-1
                    new=value(k*a,0,lo)/value(k*a,0,hi)-1
                    assert new/old == k*a/(a-t)*(1+a*lo)*(1+t*hi)/(1+k*a*lo)
                    count+=1
    return count


if __name__ == "__main__":
    result=resonance_certificate()
    result["exact_asymmetric_secants"]=exact_secants()
    print(json.dumps(result,indent=2))
