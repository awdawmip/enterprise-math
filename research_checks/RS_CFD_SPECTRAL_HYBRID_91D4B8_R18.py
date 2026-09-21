from fractions import Fraction as F
from itertools import product


def rk4_R_minus(x):
    """Classical RK4 stability polynomial R(-x), x >= 0."""
    return F(1) - x + x**2 / 2 - x**3 / 6 + x**4 / 24


def stage_weights_minus(x):
    """Weights multiplying stage-local nonlinear terms for y'=-(x/h)y+N(y)."""
    return (
        (F(4) - 4 * x + 2 * x**2 - x**3) / 24,
        (F(4) - 2 * x + x**2) / 12,
        (F(2) - x) / 6,
        F(1, 6),
    )


def direct_rk4_semilinear(y, x, h, nonlinear_stage_values):
    """Exact scalar RK4 update, treating N_i as the values observed at its four stages."""
    linear = -x / h
    n1, n2, n3, n4 = nonlinear_stage_values
    k1 = linear * y + n1
    y2 = y + h * k1 / 2
    k2 = linear * y2 + n2
    y3 = y + h * k2 / 2
    k3 = linear * y3 + n3
    y4 = y + h * k3
    k4 = linear * y4 + n4
    return y + h * (k1 + 2 * k2 + 2 * k3 + k4) / 6


def decomposed_update(y, x, h, nonlinear_stage_values):
    return rk4_R_minus(x) * y + h * sum(
        b * n for b, n in zip(stage_weights_minus(x), nonlinear_stage_values)
    )


def l1(v):
    return sum(abs(a) for a in v)


def vadd(a, b):
    return tuple(x + y for x, y in zip(a, b))


def vscale(c, a):
    return tuple(c * x for x in a)


# 1) Exact positivity / uniform lower bound of the pure-viscous RK4 multiplier.
#    24 R(-x) = x^2(x-2)^2 + 8(x-3/2)^2 + 6 >= 6,
#    hence R(-x) >= 1/4 for every x >= 0.
sos_cases = 0
for denominator in range(1, 21):
    for numerator in range(0, 20 * denominator + 1):
        x = F(numerator, denominator)
        lhs = 24 * rk4_R_minus(x)
        rhs = x**2 * (x - 2) ** 2 + 8 * (x - F(3, 2)) ** 2 + 6
        assert lhs == rhs
        assert rk4_R_minus(x) >= F(1, 4) > 0
        sos_cases += 1

# 2) Exact semilinear decomposition of one RK4 mode update.
#    This is algebraic and does not assume the four N_i are independent in a real solver.
values = [F(-2), F(-1), F(0), F(1), F(2)]
xs = [F(0), F(1, 4), F(1, 2), F(1), F(2), F(3), F(5)]
hs = [F(1, 4), F(1, 2), F(1), F(2)]
decomposition_cases = 0
for x, h, y, n1, n2, n3, n4 in product(xs, hs, values, values, values, values, values):
    ns = (n1, n2, n3, n4)
    assert direct_rk4_semilinear(y, x, h, ns) == decomposed_update(y, x, h, ns)
    decomposition_cases += 1

# 3) Source=0, target-mode nonlinear term zero at every RK4 stage => exact support preservation.
#    A nonzero scalar/vector coefficient is multiplied by R(-x) >= 1/4.
pure_viscous_cases = 0
for x in xs:
    R = rk4_R_minus(x)
    for y in values:
        if y == 0:
            continue
        for h in hs:
            out = decomposed_update(y, x, h, (F(0),) * 4)
            assert out == R * y
            assert out != 0
            assert abs(out) >= abs(y) / 4
            pure_viscous_cases += 1

# 4) Exact sufficient no-shrink certificate in a vector norm:
#    C = h sum b_i N_i. If ||C||_1 < R(-x)||u_n||_1, then u_{n+1} != 0.
#    The weaker host-friendly condition ||C|| upper bound < ||u_n||/4 is also valid.
vec_states = [
    (F(1), F(0)),
    (F(0), F(1)),
    (F(1), F(1)),
    (F(2), F(-1)),
    (F(-1), F(2)),
]
vec_nonlinear = [
    (F(0), F(0)),
    (F(1), F(0)),
    (F(-1), F(0)),
    (F(0), F(1)),
    (F(1), F(-1)),
]
sharp_no_shrink_cases = 0
uniform_no_shrink_cases = 0
exact_cancellation_cases = 0
for x in xs:
    R = rk4_R_minus(x)
    bs = stage_weights_minus(x)
    for h in [F(1, 4), F(1, 2), F(1)]:
        for state in vec_states:
            for ns in product(vec_nonlinear, repeat=4):
                correction = (F(0), F(0))
                upper = F(0)
                for b, n in zip(bs, ns):
                    correction = vadd(correction, vscale(h * b, n))
                    upper += h * abs(b) * l1(n)
                out = vadd(vscale(R, state), correction)

                if upper < R * l1(state):
                    assert out != (F(0), F(0))
                    sharp_no_shrink_cases += 1
                if upper < l1(state) / 4:
                    assert out != (F(0), F(0))
                    uniform_no_shrink_cases += 1
                if out == (F(0), F(0)):
                    # Necessary exact cancellation identity for any disappearing mode.
                    assert correction == vscale(-R, state)
                    assert l1(correction) == R * l1(state)
                    assert upper >= R * l1(state) >= l1(state) / 4
                    exact_cancellation_cases += 1

assert exact_cancellation_cases > 0  # algebra allows cancellation once nonlinear stage terms are present

print(
    {
        "status": "PASS",
        "sos_cases": sos_cases,
        "decomposition_cases": decomposition_cases,
        "pure_viscous_cases": pure_viscous_cases,
        "sharp_no_shrink_cases": sharp_no_shrink_cases,
        "uniform_no_shrink_cases": uniform_no_shrink_cases,
        "algebraic_exact_cancellation_cases": exact_cancellation_cases,
        "uniform_R_lower_bound": "1/4",
        "boundary": "The cancellation cases use arbitrary stage-local nonlinear values; they do not claim Navier-Stokes realizability. The no-shrink theorem is exact for Source=0 whenever the target mode's projected nonlinear contribution is zero at all four RK4 stages.",
    }
)
