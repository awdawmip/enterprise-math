from fractions import Fraction as F
import json


def p(x):
    x = F(x)
    return F(1) - x + x*x/F(2) - x**3/F(6) + x**4/F(24)


def q(x):
    x = F(x)
    return x**3 - F(3)*x**2 + F(6)*x - F(6)


def qp(x):
    x = F(x)
    return F(3)*x**2 - F(6)*x + F(6)


def r(mu):
    mu = F(mu)
    return F(32)*mu**3 - F(12)*mu**2 + F(12)*mu - F(3)


def rp(mu):
    mu = F(mu)
    return F(96)*mu**2 - F(24)*mu + F(12)


def padd(a, b):
    n = max(len(a), len(b))
    out = [F(0)] * n
    for i in range(n):
        if i < len(a):
            out[i] += a[i]
        if i < len(b):
            out[i] += b[i]
    while len(out) > 1 and out[-1] == 0:
        out.pop()
    return out


def pscale(a, c):
    return [F(c) * v for v in a]


def pmul(a, b):
    out = [F(0)] * (len(a) + len(b) - 1)
    for i, ai in enumerate(a):
        for j, bj in enumerate(b):
            out[i+j] += ai*bj
    while len(out) > 1 and out[-1] == 0:
        out.pop()
    return out


# Polynomial coefficient identities (ascending powers).
Q = [F(-6), F(6), F(-3), F(1)]
QP = [F(6), F(-6), F(3)]
QP_SOS = [F(6), F(-6), F(3)]  # 3((x-1)^2+1)
P24 = [F(24), F(-24), F(12), F(-4), F(1)]
X4 = [F(0), F(0), F(0), F(0), F(1)]
assert QP == QP_SOS
assert padd(P24, pscale(X4, -1)) == pscale(Q, -4)

# Elimination identity:
# r(x^4/24)=q(x)*(x^6-3x^4+36)*(x^3+3x^2+6x+6)/432.
A = [F(36), F(0), F(0), F(0), F(-3), F(0), F(1)]
B = [F(6), F(6), F(3), F(1)]
rhs = pscale(pmul(pmul(Q, A), B), F(1, 432))
lhs = [F(0)] * 13
lhs[0] = F(-3)
lhs[4] = F(1, 2)
lhs[8] = F(-1, 48)
lhs[12] = F(1, 432)
assert lhs == rhs

# Exact isolating intervals.
x_lo = F(1596071, 10**6)
x_hi = F(1596072, 10**6)
mu_lo = F(54078953, 200000000)       # 0.270394765
mu_hi = F(135197383, 500000000)      # 0.270394766
assert q(x_lo) < 0 < q(x_hi)
assert r(mu_lo) < 0 < r(mu_hi)

# Monotonicity certificates.
for t in [F(-10), F(-1), F(0), F(1), F(2), F(10), x_lo, x_hi]:
    assert qp(t) == F(3)*((t-F(1))**2 + F(1))
    assert qp(t) > 0
for t in [F(-10), F(0), F(1, 8), F(1, 4), mu_lo, mu_hi, F(1), F(10)]:
    assert rp(t) == F(96)*(t-F(1, 8))**2 + F(21, 2)
    assert rp(t) > 0

# Strict improvement over R18's simple 1/4 uniform lower bound.
assert mu_lo > F(1, 4)
improvement_lower = (mu_lo-F(1, 4))/F(1, 4)

# Sanity grid; the continuum proof is the exact derivative/root-isolation certificate above.
grid_checks = 0
for i in range(0, 12001):
    xx = F(i, 1000)
    assert p(xx) > mu_lo
    grid_checks += 1

# Finite no-loss witnesses safely inside the stronger rational gate:
# |C| < mu_lo |u| and R(-x)>=mu>mu_lo imply R(-x)u+C != 0.
no_loss_checks = 0
xs = [F(i, 20) for i in range(0, 161)]  # [0,8]
us = [F(i, 7) for i in range(-12, 13) if i]
ratios = [F(j, 20) for j in range(-5, 6)]
for xx in xs:
    R = p(xx)
    assert R > mu_lo
    for u in us:
        for z in ratios:
            C = z*mu_lo*abs(u)/F(2)
            if abs(C) < mu_lo*abs(u):
                assert R*u+C != 0
                no_loss_checks += 1

out = {
    "schema": "CFD_RK4_SHARP_MIN_CERTIFICATE_V1",
    "exact_statement": {
        "stability_factor": "R(-x)=1-x+x^2/2-x^3/6+x^4/24",
        "stationary_polynomial": "q(x)=x^3-3x^2+6x-6",
        "unique_minimizer": "the unique x_*>0 with q(x_*)=0",
        "sharp_minimum": "mu=x_*^4/24",
        "mu_polynomial": "32 mu^3-12 mu^2+12 mu-3=0 (unique real root)",
    },
    "x_star_isolation": [str(x_lo), str(x_hi)],
    "mu_isolation": [str(mu_lo), str(mu_hi)],
    "mu_decimal_bracket": [0.270394765, 0.270394766],
    "r18_uniform_bound": "1/4",
    "certified_uniform_lower_bound": str(mu_lo),
    "certified_improvement_lower_fraction": str(improvement_lower),
    "certified_improvement_lower_percent": float(improvement_lower*100),
    "proof_obligations": {
        "q_prime": "3((x-1)^2+1)>0",
        "stationary_reduction": "24R(-x)-x^4=-4q(x)",
        "elimination": "r(x^4/24)=q(x)(x^6-3x^4+36)(x^3+3x^2+6x+6)/432",
        "r_prime": "96(mu-1/8)^2+21/2>0",
    },
    "finite_checks": {"grid_checks": grid_checks, "no_loss_checks": no_loss_checks},
}
print(json.dumps(out, indent=2, sort_keys=True))
