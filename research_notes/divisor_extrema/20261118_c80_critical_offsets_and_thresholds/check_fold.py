"""Exact leading spectrum identities and exhaustive small periodic-window checks."""
from fractions import Fraction
import json
import sympy as sp


def check_spectrum():
    A, D, s = sp.symbols("A D s")
    m = 7 * A**4 * D / 16
    ratio = s**4 * (1 - s*A) * (1+m) * (1+A*m) / ((1-A)*(1+s**4*m)*(1+s**5*A*m))
    assert sp.factor(ratio.subs(A, 0)) == s**4
    assert sp.factor(sp.diff(ratio, A).subs(A, 0) - s**4*(1-s)) == 0
    d_response_numerator = sp.factor(sp.together(sp.diff(ratio, D))).as_numer_denom()[0]
    assert sp.rem(d_response_numerator, A**4, A) == 0
    assert sp.rem(d_response_numerator, 1-s, s) == 0
    d_fold = sp.Rational(14,17)
    log_phi = sp.Rational(14,3)/D - 1/(1-D)
    assert log_phi.subs(D,d_fold) == 0
    curvature = sp.diff(log_phi,D).subs(D,d_fold)
    assert curvature < 0
    beta = sp.Rational(15,4)*sp.Rational(19,5)
    assert beta == sp.Rational(57,4)
    return {"D_fold":str(d_fold),"log_phi_second":str(curvature),"beta":str(beta)}


def check_windows():
    cases = 0
    for count in range(2,8):
        for groups in range(1,9):
            total = groups*(count-1)
            points = [Fraction(i, 2*total) for i in range(-2*total, 4*total)]
            for group in range(groups):
                cuts = [Fraction(k,total) for k in range(group*(count-1),(group+1)*(count-1)+1)]
                lookup = {}
                for x in points:
                    coarse = tuple((x-cut).__floor__() for cut in cuts)
                    fine = (x*total).__floor__()
                    lookup.setdefault(coarse, set()).add(fine)
                for fine_values in lookup.values():
                    kept = [v for v in fine_values if (v % total)//(count-1) == group]
                    if kept:
                        assert len(fine_values) == 1
                cases += 1
    return cases


if __name__ == "__main__":
    print(json.dumps({"symbolic":check_spectrum(),"periodic_window_designs_checked":check_windows()},indent=2))
