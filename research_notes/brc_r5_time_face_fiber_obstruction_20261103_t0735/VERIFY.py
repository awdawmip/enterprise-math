"""R5: exact P/Q time-face fiber obstruction, source-preserving two-law model.

Author-side evidence. Standard library only; rational enumeration is a crosscheck
for the analytic all-real theorem in RESEARCH.md.
"""
from fractions import Fraction as F
from itertools import product

C = F(2, 3)
ALPHA = (F(1, 2), F(2, 3), F(1, 2), F(3, 4))
W = (F(1, 8), F(1, 6), F(1, 16), F(3, 32))
N_FULL = 0
N_LR = 0
CHECKS = 0


def check(test, detail):
    global CHECKS
    CHECKS += 1
    if not test:
        raise AssertionError(detail)


def observer(x, y, j, z, t, a, b, p, q):
    """Exact true four-observer from the established physical P/Q path sums."""
    i = (1 - x) * j
    w = (F(1, 4), (1 - x) * F(1, 4), y * F(1, 8), i * F(1, 8))
    Q = tuple(w[s] * ALPHA[s] * z[s] for s in range(4))
    S = tuple(C * Q[s] * t[s] for s in range(4))
    d = y * F(1, 16) + i * F(3, 32)
    return (
        F(107, 128) - F(21, 128) * x + d / 4 - sum(p[s] * S[s] for s in range(4)),
        F(13, 64) + F(3, 64) * x - d / 2 + sum(q[s] * S[s] for s in range(4)) / 4,
        3 + sum(Q) + sum((1 + a[s]) * S[s] for s in range(4)),
        3 + sum(Q) / 2 + sum((1 + b[s]) * S[s] for s in range(4)) / 4,
    )


def normal_and_margin(a, rho):
    tau = (a[1] + a[2]) / 2
    h = -C * (1 + tau)
    n3 = (h - 1) / (F(1, 2) - rho / 4)
    n2 = 1 - rho * n3 / 4
    g = min(C * (a[1] - tau) / 6, C * F(5, 32) * (tau - a[2]))
    return tau, n2, n3, g


def dot(normal, value):
    return sum(normal[k] * value[k] for k in range(4))


def bellman_full(normal, a, b, p, q):
    n0, n1, n2, n3 = normal
    base = F(107, 128) * n0 + F(13, 64) * n1 + 3 * (n2 + n3)
    hx = -F(21, 128) * n0 + F(3, 64) * n1
    hd = n0 / 4 - n1 / 2
    h = n2 + n3 / 2
    k = tuple(-n0 * p[s] + n1 * q[s] / 4
              + n2 * (1 + a[s]) + n3 * (1 + b[s]) / 4 for s in range(4))
    L = tuple(max(F(0), h + C * max(F(0), k[s])) for s in range(4))
    return (base + L[0] / 8 + max(F(0), (hd + L[2]) / 16)
            + max(hx, L[1] / 6 + max(F(0), 3 * (hd + L[3]) / 32)))


def suite(label, rho, a, p, q, special_delta=None):
    global N_FULL, N_LR
    b = tuple(rho * (1 + v) - 1 for v in a)
    check(0 < a[2] < a[1] <= a[0] < 1 and a[2] == a[3], label + ': ordered a')
    check(all(0 < v < 1 for v in a + b + p + q), label + ': positivity')
    check(all((1 + b[s]) / (1 + a[s]) == rho for s in range(4)), label + ': rho')
    tau, n2, n3, g = normal_and_margin(a, rho)
    delta = special_delta if special_delta is not None else g / 4
    check(0 < delta < g and g > 0, label + ': perturbation margin')
    check(n2 + n3 / 2 == -C * (1 + tau), label + ': h')
    check(n2 + rho * n3 / 4 == 1, label + ': f')
    n = (delta, F(0), n2, n3)
    lr_w = observer(0, 0, 0, (1, 1, 1, 1), (1, 1, 1, 1), a, b, p, q)
    full_w = observer(0, 1, 1, (1, 1, 0, 0), (1, 1, 0, 0), a, b, p, q)
    check(tuple(full_w[k] - lr_w[k] for k in range(4)) ==
          (F(5, 128), -F(5, 64), F(0), F(0)), label + ': face fiber')
    check(dot(n, full_w) - dot(n, lr_w) == delta * F(5, 128), label + ': witness gap')

    full_max = None
    for x, y, j in product((0, 1), repeat=3):
        for tail in product((0, 1), repeat=8):
            val = dot(n, observer(x, y, j, tail[:4], tail[4:], a, b, p, q))
            check(val <= dot(n, full_w), label + ': full binary domination')
            full_max = val if full_max is None else max(val, full_max)
            N_FULL += 1
    lr_max = None
    time_losses = []
    tn = (F(0), F(0), n2, n3)
    for x, y, z, t in product((0, 1), repeat=4):
        val = observer(x, y, y, (z,) * 4, (t,) * 4, a, b, p, q)
        check(dot(n, val) <= dot(n, lr_w), label + ': LR binary domination')
        if (x,y,z,t) != (0,0,1,1):
            time_losses.append(dot(tn, lr_w) - dot(tn, val))
        lr_max = dot(n, val) if lr_max is None else max(lr_max, dot(n, val))
        N_LR += 1
    check(min(time_losses) == g, label + ': exact LR time margin')
    check(full_max == dot(n, full_w), label + ': full attained')
    check(lr_max == dot(n, lr_w), label + ': LR attained')
    check(bellman_full(n, a, b, p, q) == full_max, label + ': analytic FULL oracle')
    check(full_max - lr_max == delta * F(5, 128), label + ': exact support gap')
    print('CASE', label, 'rho', rho, 'tau', tau, 'margin', g,
          'delta', delta, 'support_gap', full_max-lr_max,
          'Linf_lower', (full_max-lr_max)/sum(abs(v) for v in n))
    return full_w, lr_w


half = (F(1, 2),) * 4
near_edges = (F(1, 1000), F(999, 1000), F(1, 999), F(998, 999))
cases = (
    ('fixed_uniform', F(1), (F(3,4),F(1,2),F(1,4),F(1,4)), half, half, F(1,1000)),
    ('fixed_heterogeneous',F(1), (F(3,4),F(1,2),F(1,4),F(1,4)),
     (F(1,4),F(1,2),F(3,4),F(1,3)),(F(1,3),F(3,4),F(1,2),F(1,4)),None),
    ('fixed_near_edges',F(1),(F(3,4),F(1,2),F(1,4),F(1,4)),near_edges,near_edges[::-1],None),
    ('rho_four_fifths',F(4,5),(F(3,4),F(1,2),F(3,8),F(3,8)),half,near_edges,None),
    ('rho_six_fifths',F(6,5),(F(3,5),F(2,5),F(1,4),F(1,4)),near_edges,half,None),
    ('high_tie',F(1),(F(1,2),F(1,2),F(1,4),F(1,4)),half,near_edges,None),
    ('broad_interval',F(1),(F(9,10),F(3,4),F(1,16),F(1,16)),near_edges,half,None),
)
for args in cases:
    witness, lrvertex = suite(*args)
    if args[0] == 'fixed_uniform':
        check(witness == (F(7,9), F(43,288), F(173,48), F(619,192)),
              'fixed witness coordinates')
        check(witness[2:] == lrvertex[2:], 'fixed time fiber')
        check(F(1,1000)*F(5,128) == F(1,25600), 'fixed support value')

print('PASS_EXACT_R5_NONUNIFORM_TIME_FACE_FIBER_OBSTRUCTION')
print('TOTAL_EXACT_ASSERTIONS', CHECKS, 'PARAMETER_CASES', len(cases),
      'FULL_CONFIGS', N_FULL, 'LR_CONFIGS', N_LR)
