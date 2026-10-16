"""Fixed m7 certificate producer, NOT ADMITTED; definitions only at import.

No CLI or permission switch is provided. A legitimately admitted launcher must
call produce with the exact frozen input and the shared resource Budget.
"""
from __future__ import annotations


def produce(spec, b):
    expected = {"m": 7, "n": 6, "a": [1, 1], "c": [1, 1],
                "r_interval": [[7, 1], [8, 1]], "degree_bound": 56,
                "dyadic_depth": 4}
    if spec.get("math") != expected:
        raise ValueError("input differs from the fixed m7 carrier")
    z, one = b.q(0), b.q(1)
    def clean(p):
        return {k: v for k, v in p.items() if v}
    def const(v):
        return {} if not v else {(0, 0, 0): v}
    def add(p, q):
        out = dict(p)
        for k, v in q.items():
            out[k] = b.add(out.get(k, z), v)
        return clean(out)
    def scale(p, v):
        return clean({k: b.mul(c, v) for k, c in p.items()})
    def sub(p, q):
        return add(p, scale(q, b.q(-1)))
    def mul(p, q):
        out = {}
        for a, u in p.items():
            for c, v in q.items():
                k = tuple(a[i] + c[i] for i in range(3))
                if sum(k) > 15:
                    raise ValueError("intermediate polynomial degree")
                out[k] = b.add(out.get(k, z), b.mul(u, v))
        return clean(out)
    def swap(p):
        return {(r, y, x): v for (r, x, y), v in p.items()}
    def deriv(p, axis, order):
        out = {}
        for k, v in p.items():
            if k[axis] >= order:
                factor = one
                for a in range(order):
                    factor = b.mul(factor, b.q(k[axis] - a))
                kk = list(k)
                kk[axis] -= order
                out[tuple(kk)] = b.mul(v, factor)
        return clean(out)
    def transfer(p, axis):
        if any(k[axis] > 6 for k in p):
            raise ValueError("transfer degree exceeds six")
        out = dict(p)
        for order, coeff in [(1, b.q(-7, 2)), (3, b.q(343, 24)), (5, b.q(-16807, 240))]:
            out = add(out, scale(deriv(p, axis, order), coeff))
        return out
    r, x = {(1, 0, 0): one}, {(0, 1, 0): one}
    vx = const(one)
    for a in range(1, 8):
        vx = mul(vx, add(x, const(b.q(-a, 7))))
    def pdata(shift):
        p = const(one)
        for j in range(7):
            p = mul(p, add(add(r, x), const(b.q(shift + j))))
        return p
    def bezout(p):
        # (x^a y^d - x^d y^a)/(x-y), with no diagonal division.
        out = {}
        for (_, a, _), u in vx.items():
            for (rp, d, _), v in p.items():
                c = b.mul(u, v)
                sign = one if a > d else b.q(-1)
                for j in range(abs(a - d)):
                    k = (rp, max(a, d) - 1 - j, min(a, d) + j)
                    out[k] = b.add(out.get(k, z), b.mul(c, sign))
        return clean(out)
    pr, ps = pdata(0), pdata(7)
    rr, rs = sub(pr, vx), sub(ps, vx)
    fr, fs = bezout(pr), bezout(ps)
    lr, ls = add(scale(r, b.q(7)), const(b.q(25))), add(scale(r, b.q(7)), const(b.q(74)))
    tr = transfer(rs, 1)
    xi = add(mul(mul(lr, ls), sub(transfer(transfer(fs, 1), 2), fr)),
             sub(mul(ls, mul(rr, swap(rr))), mul(lr, mul(tr, swap(tr)))))
    if any(sum(k) > 14 for k in xi):
        raise ValueError("Xi total degree certificate failed")

    def ua(p, q):
        out = dict(p)
        for k, v in q.items():
            out[k] = b.add(out.get(k, z), v)
        return clean(out)
    def um(p, q):
        out = {}
        for i, u in p.items():
            for j, v in q.items():
                if i + j > 56:
                    raise ValueError("univariate degree exceeds 56")
                out[i + j] = b.add(out.get(i + j, z), b.mul(u, v))
        return clean(out)
    def us(p, c):
        return clean({k: b.mul(v, c) for k, v in p.items()})
    def evaluate_grid(k):
        out = {}
        powers = {}
        for (_, a, d) in xi:
            h = a + d
            if h not in powers:
                powers[h] = {j: b.mul(b.q((-1) ** h * b.comb(h, j)),
                                     b.power(b.q(k), h - j)) for j in range(h + 1)}
        for (rp, a, d), c in xi.items():
            for j, v in powers[a + d].items():
                out[rp + j] = b.add(out.get(rp + j, z), b.mul(c, v))
        return clean(out)
    qk = []
    for k in range(7):
        q = {0: one}
        for a in range(1, 8):
            q = um(q, {1: one, 0: b.q(7 * k + a, 7)})
        qk.append(q)
    numerator = {}
    for k in range(7):
        omitted = {0: one}
        for ell in range(7):
            if ell != k:
                omitted = um(omitted, qk[ell])
        denom = b.integer_product(b.factorial(k), b.factorial(6 - k))
        numerator = ua(numerator, us(um(evaluate_grid(k), omitted), b.q((-1) ** k, denom)))
    coefficients = [numerator.get(i, z) for i in range(57)]
    common = 1
    for v in coefficients:
        common = b.lcm(common, v.denominator)
    integers = [b.integer_product(v.numerator, b.exact_integer_quotient(common, v.denominator))
                for v in coefficients]

    # Produce Bernstein rows by one global basis change then exact de Casteljau.
    power = [z for _ in range(57)]
    for i, v in enumerate(coefficients):
        for j in range(i + 1):
            term = b.mul(v, b.q(b.comb(i, j)))
            term = b.mul(term, b.power(b.q(7), i - j))
            power[j] = b.add(power[j], term)
    bern = []
    for i in range(57):
        value = z
        for j in range(i + 1):
            value = b.add(value, b.mul(power[j], b.q(b.comb(i, j), b.comb(56, j))))
        bern.append(value)
    def split(row):
        left, right = [row[0]], [row[-1]]
        current = list(row)
        while len(current) > 1:
            current = [b.div(b.add(current[i], current[i + 1]), b.q(2))
                       for i in range(len(current) - 1)]
            left.append(current[0])
            right.append(current[-1])
        return left, list(reversed(right))
    rows = [bern]
    for _ in range(4):
        next_rows = []
        for row in rows:
            next_rows.extend(split(row))
        rows = next_rows
    all_positive = all(v > 0 for row in rows for v in row)
    return {"schema": "PARITY_M7_FIXED_INTERVAL_BERNSTEIN_CERTIFICATE_V1",
            "math": expected, "source_binding": spec["source_binding"],
            "status": "POSITIVE_CANDIDATE" if all_positive else "CANNOT_CERTIFY_THIS_FIXED_PLAN",
            "polynomial": {"positive_denominator_hex": hex(common),
                           "power_coeff_integer_hex": [hex(v) for v in integers]},
            "positive_trace_denominator": {"L": [[7, 25], [7, 74]],
                         "q_factors": [[k, a, 7] for k in range(7) for a in range(1, 8)]},
            "bernstein": [{"i": i, "left": [112 + i, 16], "right": [113 + i, 16],
                           "coefficients": [b.encoded(v) for v in row]} for i, row in enumerate(rows)],
            "producer_operations_so_far": b.operations}
