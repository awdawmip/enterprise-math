"""Algorithmically independent fixed-carrier checker, NOT ADMITTED.

It imports no producer or producer polynomial routines. It rebuilds cleared
kernel numerators by monic long division and the triangular shift equation,
then checks interval coefficients by direct affine/binomial conversion.
Both files have the SAME author; this is not a nonauthor review or Native vote.
"""
from __future__ import annotations


def verify(spec, certificate, meter):
    required_math = {"m": 7, "n": 6, "a": [1, 1], "c": [1, 1],
                     "r_interval": [[7, 1], [8, 1]], "degree_bound": 56,
                     "dyadic_depth": 4}
    if spec.get("math") != required_math or certificate.get("math") != required_math:
        raise ValueError("fixed carrier mismatch")
    if certificate.get("schema") != "PARITY_M7_FIXED_INTERVAL_BERNSTEIN_CERTIFICATE_V1":
        raise ValueError("certificate schema")
    if certificate.get("source_binding") != spec.get("source_binding"):
        raise ValueError("source pin mismatch")
    expected_fields = {"schema", "math", "source_binding", "status", "polynomial",
                       "positive_trace_denominator", "bernstein", "producer_operations_so_far"}
    if set(certificate) != expected_fields:
        raise ValueError("unknown/missing certificate fields")
    zero, unity = meter.q(0), meter.q(1)

    # Dense r-polynomials, with [] the exact zero. This representation is not
    # shared with the producer's sparse three-variable representation.
    def trim(a):
        a = list(a)
        while a and a[-1] == 0:
            a.pop()
        return a
    def plus(a, c):
        return trim([meter.add(a[i] if i < len(a) else zero,
                               c[i] if i < len(c) else zero)
                     for i in range(max(len(a), len(c)))])
    def times(a, c):
        if not a or not c:
            return []
        if len(a) + len(c) - 2 > 56:
            raise ValueError("r degree outside carrier")
        out = [zero] * (len(a) + len(c) - 1)
        for i, av in enumerate(a):
            for j, cv in enumerate(c):
                out[i + j] = meter.add(out[i + j], meter.mul(av, cv))
        return trim(out)
    def scalar(a, c):
        return trim([meter.mul(v, c) for v in a])
    def opposite(a):
        return scalar(a, meter.q(-1))

    # A bivariate x,y polynomial whose coefficients are dense r-polynomials.
    def bplus(a, c):
        out = {k: list(v) for k, v in a.items()}
        for k, v in c.items():
            out[k] = plus(out.get(k, []), v)
        return {k: v for k, v in out.items() if v}
    def bnegative(a):
        return {k: opposite(v) for k, v in a.items()}
    def btimes(a, c):
        out = {}
        for (ax, ay), av in a.items():
            for (cx, cy), cv in c.items():
                k = (ax + cx, ay + cy)
                out[k] = plus(out.get(k, []), times(av, cv))
        return {k: v for k, v in out.items() if v}
    def flip(a):
        return {(j, i): list(v) for (i, j), v in a.items()}
    def monic_divide_x_minus_y(numerator):
        pending = {k: list(v) for k, v in numerator.items()}
        quotient = {}
        while pending and max(k[0] for k in pending) >= 1:
            top = max(k[0] for k in pending)
            for key in sorted(k for k in pending if k[0] == top):
                coeff = pending.pop(key)
                qkey = (top - 1, key[1])
                quotient[qkey] = plus(quotient.get(qkey, []), coeff)
                tail = (top - 1, key[1] + 1)
                pending[tail] = plus(pending.get(tail, []), coeff)
                if not pending[tail]:
                    del pending[tail]
        if pending:
            raise ValueError("Bezout polynomial division had nonzero remainder")
        return {k: v for k, v in quotient.items() if v}
    def inverse_shift_equation(f, axis):
        degree = max((key[axis] for key in f), default=0)
        if degree > 6:
            raise ValueError("shift inversion outside degree six")
        answer = {}
        for i in range(degree, -1, -1):
            row = {key[1 - axis]: list(v) for key, v in f.items() if key[axis] == i}
            for key, value in answer.items():
                j = key[axis]
                if j > i:
                    multiplier = meter.div(
                        meter.mul(meter.q(meter.comb(j, i)), meter.power(meter.q(7), j - i)),
                        meter.q(2))
                    other = key[1 - axis]
                    row[other] = plus(row.get(other, []), opposite(scalar(value, multiplier)))
            for other, value in row.items():
                if value:
                    answer[(i, other) if axis == 0 else (other, i)] = value
        return answer

    vx = {(0, 0): [unity]}
    for i in range(1, 8):
        vx = btimes(vx, {(1, 0): [unity], (0, 0): [meter.q(-i, 7)]})
    def cleared_kernel(shift):
        px = {(0, 0): [unity]}
        for j in range(7):
            px = btimes(px, {(1, 0): [unity], (0, 0): [meter.q(shift + j), unity]})
        rem = bplus(px, bnegative(vx))
        antisymmetric = bplus(btimes(vx, flip(px)), bnegative(btimes(px, flip(vx))))
        bezout = monic_divide_x_minus_y(antisymmetric)
        linear = {(0, 0): [meter.q(25 + 7 * shift), meter.q(7)]}
        return bplus(btimes(linear, bezout), bnegative(btimes(rem, flip(rem))))
    early, late = cleared_kernel(0), cleared_kernel(7)
    transformed = inverse_shift_equation(inverse_shift_equation(late, 0), 1)
    xi = bplus(btimes({(0, 0): [meter.q(25), meter.q(7)]}, transformed),
               bnegative(btimes({(0, 0): [meter.q(74), meter.q(7)]}, early)))
    for (xp, yp), row in xi.items():
        if row and xp + yp + len(row) - 1 > 14:
            raise ValueError("rebuilt Xi total degree exceeds fourteen")
    def grid_value(k):
        result = []
        base = [meter.q(-k), meter.q(-1)]
        cache = {0: [unity]}
        for n in range(1, 13):
            cache[n] = times(cache[n - 1], base)
        for (xp, yp), row in xi.items():
            result = plus(result, times(row, cache[xp + yp]))
        return result
    q_polys = []
    for k in range(7):
        p = [unity]
        for a in range(1, 8):
            p = times(p, [meter.add(meter.q(k), meter.q(a, 7)), unity])
        q_polys.append(p)
    p_actual = []
    for k in range(7):
        term = grid_value(k)
        for ell, q in enumerate(q_polys):
            if ell != k:
                term = times(term, q)
        weight = meter.q((-1) ** k, meter.integer_product(meter.factorial(k), meter.factorial(6 - k)))
        p_actual = plus(p_actual, scalar(term, weight))
    p_actual += [zero] * (57 - len(p_actual))
    if len(p_actual) != 57:
        raise ValueError("rebuilt numerator degree exceeds 56")

    def integer_hex(s):
        if not isinstance(s, str) or len(s) > meter.BITS // 4 + 4:
            raise ValueError("integer hex size")
        value = meter.integer(int(s, 16))
        if hex(value) != s:
            raise ValueError("noncanonical integer hex")
        return value
    table = certificate["polynomial"]
    if set(table) != {"positive_denominator_hex", "power_coeff_integer_hex"}:
        raise ValueError("power table shape")
    denominator = integer_hex(table["positive_denominator_hex"])
    integers = table["power_coeff_integer_hex"]
    if denominator <= 0 or not isinstance(integers, list) or len(integers) != 57:
        raise ValueError("power table dimension/positive denominator")
    p_claimed = [meter.q(integer_hex(s), denominator) for s in integers]
    if p_claimed != p_actual:
        raise ValueError("original residue/kernel polynomial identity mismatch")
    expected_d = {"L": [[7, 25], [7, 74]],
                  "q_factors": [[k, a, 7] for k in range(7) for a in range(1, 8)]}
    if certificate["positive_trace_denominator"] != expected_d:
        raise ValueError("positive original-trace denominator changed")

    rows = certificate["bernstein"]
    if not isinstance(rows, list) or len(rows) != 16:
        raise ValueError("exact fixed subdivision count")
    all_positive = True
    for i, claimed in enumerate(rows):
        if set(claimed) != {"i", "left", "right", "coefficients"}:
            raise ValueError("Bernstein row fields")
        if claimed["i"] != i or claimed["left"] != [112 + i, 16] or claimed["right"] != [113 + i, 16]:
            raise ValueError("fixed interval changed")
        vals = claimed["coefficients"]
        if not isinstance(vals, list) or len(vals) != 57:
            raise ValueError("Bernstein degree elevation dimension")
        left, width = meter.q(112 + i, 16), meter.q(1, 16)
        ap, wp = [unity], [unity]
        for _ in range(56):
            ap.append(meter.mul(ap[-1], left))
            wp.append(meter.mul(wp[-1], width))
        translated = [zero] * 57
        for degree, coefficient in enumerate(p_actual):
            for power in range(degree + 1):
                v = meter.mul(coefficient, meter.q(meter.comb(degree, power)))
                v = meter.mul(v, ap[degree - power])
                v = meter.mul(v, wp[power])
                translated[power] = meter.add(translated[power], v)
        for k in range(57):
            exact = zero
            for j in range(k + 1):
                exact = meter.add(exact, meter.mul(translated[j],
                       meter.q(meter.comb(k, j), meter.comb(56, j))))
            if meter.decoded(vals[k]) != exact:
                raise ValueError("independent Bernstein conversion mismatch")
            all_positive = all_positive and exact > 0
    expected_status = "POSITIVE_CANDIDATE" if all_positive else "CANNOT_CERTIFY_THIS_FIXED_PLAN"
    if certificate["status"] != expected_status:
        raise ValueError("certificate status disagrees with exact coefficients")
    count = certificate["producer_operations_so_far"]
    if type(count) is not int or not 0 <= count <= meter.operations <= meter.OPS:
        raise ValueError("producer operation count outside shared budget")
    return {"schema": "PARITY_M7_FIXED_INTERVAL_COLD_CHECK_V1",
            "polynomial_identity_verified": True, "bernstein_coefficients_verified": 912,
            "complete_interval": [[7, 1], [8, 1]], "all_strictly_positive": all_positive,
            "mathematical_conclusion": "ORIGINAL_TRACE_GT_6_ON_ENTIRE_INTERVAL" if all_positive
                 else "NO_TRACE_SIGN_CONCLUSION_FROM_THIS_FIXED_PLAN",
            "Native_acceptance_or_Task_completion": False}
