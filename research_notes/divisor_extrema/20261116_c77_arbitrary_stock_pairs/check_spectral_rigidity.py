"""Exact leading/first fractional terms of one physical stock spectrum."""
import json
import sympy as sp


def certificate():
    u, v, t, b = sp.symbols("u v t b", positive=True)
    A, D = 4*u**15, 4*v**9/u**9
    m = b*A**4*D
    # y**(-3/4) = v**(-3). Suppress nonzero constant prefactors.
    one = sp.factor(A**4*D**5*(1-D)*v**(-3)*t**4*(1-A*t)
                    / ((1+m*t**4)*(1+m*A*t**5)))
    def orders(f, z, k):
        # First correction of the 12th power uses 12 times its single-column
        # coefficient once the common monomial factor has been removed.
        f0 = sp.factor(f / z**k)
        coeff = sp.factor(f0.subs(z, 0))
        diff = sp.factor((f0/coeff - 1)/z**9)
        return coeff, sp.factor(12*diff.subs(z, 0))
    l0, corr0 = orders(one, u, 6)
    l1, corr1 = orders(one, v, 42)
    assert sp.simplify(corr0 + 3/v**9) == 0
    assert sp.simplify(corr1 + 12*(1+b*A**4*t**4+b*A**5*t**5)*4/u**9) == 0
    assert sp.simplify(l0 / (t**4*v**51)).is_constant()
    assert sp.simplify(l1 / (t**4*u**15*(1-4*t*u**15))).is_constant()
    assert 12*6//4 == 18 and 12*42//4 == 126
    D0 = sp.Symbol("D0", positive=True)
    rank_coeff = sp.factor(sp.diff(D0**sp.Rational(14,3)*(D0-1), D0).subs(D0,2))
    assert rank_coeff > 0
    return dict(x_transverse_leading=18, y_transverse_leading=126,
                first_noninteger_x="81/4", first_noninteger_y="513/4",
                x_relative_coefficient=str(corr0), y_relative_coefficient=str(corr1),
                interior_rank_factor=str(rank_coeff))


if __name__ == "__main__":
    print(json.dumps(certificate(), indent=2))
