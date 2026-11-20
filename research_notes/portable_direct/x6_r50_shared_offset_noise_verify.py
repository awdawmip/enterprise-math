"""R50 exact observer-level shared-offset/noise feasibility verifier.

Consumes the R47 closed positive Weighted-BRC root mass expressions.
All Fraction arithmetic is restricted to the declared measurement layer and
exact polygon inequalities; it is not a native heartbeat/BRC propagation engine.
"""
from fractions import Fraction as F
from itertools import combinations


def poly_vertices(z, eta, q):
    z = tuple(F(v) for v in z)
    eta = F(eta)
    v = [(F(q), F(0)), (F(q - 1), F(0)),
         (F(0), F(2 * (q*q - 1))), (F(0), F(2 * q))]
    H = [(F(-1), F(0), F(0)), (F(0), F(-1), F(0))]
    for i, j in combinations(range(4), 2):
        a, b = v[i][0] - v[j][0], v[i][1] - v[j][1]
        d = z[i] - z[j]
        H.extend([(a, b, d + 2*eta), (-a, -b, -d + 2*eta)])
    vertices = set()
    for (a, b, c), (d, e, f) in combinations(H, 2):
        det = a*e - b*d
        if not det:
            continue
        S = (c*e - b*f) / det
        P = (a*f - c*d) / det
        if all(A*S + B*P <= C for A, B, C in H):
            vertices.add((S, P))
    return vertices


def feasible(z, eta, q):
    if q < 1 or eta < 0:
        raise ValueError("positive integer q and nonnegative eta required")
    V = poly_vertices(z, eta, q)
    if any(s > 0 and p > 0 and s*s >= 4*p for s, p in V):
        return True
    return (any(s > 0 and p == 0 for s, p in V)
            and any(p > 0 for s, p in V))


def port_cap(z, eta):
    s = F(z[0]) - F(z[1])
    k = F(z[0]) - F(z[3])
    e = F(z[2]) - F(z[3])
    eta = F(eta)
    if s <= 2*eta:
        return None
    E = e + 2*eta
    if E <= 0:
        return 2
    cap = (k + 2*eta + F(3, 5)*E) / (s - 2*eta)
    return max(2, cap.numerator // cap.denominator)


def feasible_ports(z, eta):
    cap = port_cap(z, eta)
    if cap is None:
        raise ValueError("R50 finite search cap hypothesis s>2eta is unmet")
    return [q for q in range(1, cap + 1) if feasible(z, eta, q)]


def root_masses(q, alpha, beta, b=F(0)):
    S, P = alpha + beta, alpha*beta
    return (q*S+b, (q-1)*S+b, 2*(q*q-1)*P+b, 2*q*P+b)


def main():
    examples = [
        ("exact", (9, 6, 32, 12), F(0), 3, [3]),
        ("bias", (16, 13, 39, 19), F(0), 3, [3]),
        ("quarter", (F(37,4), F(25,4), F(129,4), F(49,4)), F(1,4), 3, [3]),
        ("eta_one", (9, 6, 32, 12), F(1), 12, [3]),
    ]
    for label, z, eta, cap, expected in examples:
        assert port_cap(z, eta) == cap, label
        assert feasible_ports(z, eta) == expected, label
    for q, alpha, beta, b, eta in [
        (1, F(1), F(2), F(0), F(0)),
        (2, F(3,2), F(3,2), F(3), F(0)),
        (3, F(1), F(2), F(0), F(1,4)),
        (4, F(1,3), F(5,3), F(-2), F(1,8)),
    ]:
        assert feasible(root_masses(q, alpha, beta, b), eta, q)
    for q in range(1, 101):
        t = F(1, 8)
        alpha = beta = t/q
        masses = root_masses(q, alpha, beta)
        assert max(masses) <= F(1,2)
        assert feasible((0, 0, 0, 0), F(1,2), q)
    for q in range(1, 13):
        assert feasible((9, 6, 32, 12), F(1), q) == feasible(
            (16, 13, 39, 19), F(1), q)
    print("PASS: four rational parameter cases; four positive-weight self witnesses;")
    print("100 zero-readout aliases; twelve common-bias invariance checks")
    print("at eta=1 feasible Port set [3]; proven finite cap=12")


if __name__ == "__main__":
    main()
