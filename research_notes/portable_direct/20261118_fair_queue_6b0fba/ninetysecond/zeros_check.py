"""Exact Laguerre checks and rigorous finite raw-road Green integrals.

Install python-flint==0.9.0 in the interpreter, then run
    python zeros_check.py > zeros_checked.json
"""
from fractions import Fraction as F
from math import comb, factorial
import json
from flint import acb, arb, ctx, fmpq

ctx.prec = 192


def ball(x):
    x = F(x)
    return arb(fmpq(x.numerator, x.denominator))


def bracket(x, digits=15):
    scale = 10 ** digits
    ix = (x * scale).floor().unique_fmpz()
    if ix is None:
        raise ArithmeticError("interval wider than target grid")
    ix = int(ix)
    assert x >= ball(F(ix, scale)) and x <= ball(F(ix + 1, scale))
    return [str(F(ix, scale)), str(F(ix + 1, scale))]


def polynomial_rows():
    rows = []
    for m in range(1, 33):
        lag = [F((-1) ** j * comb(m, j + 1), factorial(j)) for j in range(m)]
        sq = [F(0)] * (2 * m - 1)
        for j, x in enumerate(lag):
            for k, y in enumerate(lag):
                sq[j+k] += x * y
        # e^(2v) times the tail integral solves (2 - d/dv)P = L^2.
        tail = [F(0)] * (len(sq) + 1)
        for j in reversed(range(len(sq))):
            tail[j] = (sq[j] + (j + 1) * tail[j+1]) / 2
        center = F(comb(2*m, m), 4**m)
        first = sum(v * F(factorial(j+1), 2 ** (j+2)) for j, v in enumerate(sq))
        expmass = sum(v * factorial(j) for j, v in enumerate(sq))
        gram = sum(F(comb(j+k, k), 2 ** (j+k+1))
                   for j in range(m) for k in range(m))
        assert tail[0] == gram == m * (1 - center)
        assert first == m * center / 2 and expmass == m
        assert tail[-2] == F(1, 2 * factorial(m-1) ** 2)
        if m <= 5:
            rows.append({"multiplicity": m, "tail_polynomial_ascending": list(map(str, tail[:-1])),
                         "mass": str(gram), "first_moment": str(first), "exponential_moment": int(expmass)})
    return {"all_rational_identities_for_m": [1, 32], "examples": rows}


def road_atoms(a, H):
    mu = [1] * H
    sieved = bytearray(H)
    product = [arb(1) for _ in range(H)]
    for p in range(2, H):
        if sieved[p]:
            continue
        factor = 1 - arb(p) ** (-a)
        for n in range(p, H, p):
            sieved[n] = 1
            mu[n] = -mu[n]
            product[n] *= factor
        for n in range(p*p, H, p*p):
            mu[n] = 0
    divisor = [arb(0) for _ in range(H)]
    for d in range(1, H):
        if mu[d]:
            term = mu[d] * arb(d) ** (-a)
            for n in range(d, H, d):
                divisor[n] += term
    eps = ball(F(1, 2**170))
    assert all(product[n].overlaps(divisor[n]) and product[n].rad() < eps
               and divisor[n].rad() < eps for n in range(1, H))
    return product, divisor


def raw_window(den, v, w):
    a = ball(F(1, den))
    L = int((ball(v)/a).exp().ceil().unique_fmpz())
    H = int((ball(w)/a).exp().ceil().unique_fmpz())
    c = 1 / (1+a).zeta()
    product, divisor = road_atoms(a, H)
    # First route uses a cellwise integral and prime product weights.
    subtotal = sum(product[2:L], arb(0))
    direct, midpoint, variance = arb(0), arb(0), arb(0)
    for n in range(L, H):
        subtotal += product[n]
        direct += subtotal ** 2 / (n*(n+1)) - 2*c*subtotal*(1+arb(1)/n).log() + c*c
        midpoint += ((subtotal-c*(n+ball(F(1,2)))) / n) ** 2
        variance += (c/n) ** 2 / 12
    # Independent route groups all Green pairs by max(m,n) and uses Möbius.
    prefix = sum(divisor[2:L], arb(0))
    pairs = prefix**2 * (arb(1)/L - arb(1)/H)
    cross = prefix * (arb(H)/L).log()
    for n in range(L, H):
        r = divisor[n]
        pairs += r*(2*prefix+r)*(arb(1)/n-arb(1)/H)
        cross += r*(arb(H)/n).log()
        prefix += r
    mix = 2*c*cross
    background = (H-L)*c*c
    green = pairs - mix + background
    assert direct.overlaps(green) and green > 0
    assert midpoint+variance > direct > ball(F(L*L, (L+1)**2))*(midpoint+variance)
    eps = ball(F(1, 2**170))
    assert c.rad() < eps
    rounding = ball(F(1, 2**130))
    assert all(x.rad() < rounding for x in [pairs, mix, background, direct, green, midpoint])
    return {"a": f"1/{den}", "scaled_window": [str(v), str(w)], "integer_cutoffs_half_open": [L,H],
            "c_a": bracket(c), "Green_positive_pairs": bracket(pairs), "Green_subtracted_cross": bracket(mix),
            "Green_background": bracket(background), "actual_Q": bracket(direct), "Q_over_a": bracket(green/a),
            "actual_midpoint_D_over_a": bracket(midpoint/a), "cancellation_condition_ratio":
            bracket((pairs+mix+background)/green, 6), "individual_weight_radius_upper": "2^-170",
            "background_constant_radius_upper": "2^-170", "total_Green_roundoff_radius_upper": "2^-130",
            "actual_Q_cell_radius_upper": "2^-130", "completion_used_in_finite_calculation": False}


def zero_fixture():
    root = acb.zeta_zero(1)
    assert root.real == ball(F(1,2)) and 14 < root.imag < 15
    assert arb(14).zeta_nzeros() == 0 and arb(15).zeta_nzeros() == 1
    errors = []
    for power in (8,16,24):
        a = ball(F(1, 2**power))
        for v in map(F, [-2, F(1,3), 1]):
            iv = acb(0, ball(v))
            s = root + a*iv
            field = (s.zeta()/(s+a).zeta()-1)/s
            limit = -1/(root*(1+iv))
            error = abs(field - limit)
            assert error < a
            errors.append({"a": f"2^-{power}", "v": str(v), "absolute_error_over_a": bracket(error/a)})
    T = arb(3 * 10**12)
    upper = 2*(T.log()+1)/(arb.pi()*T)
    lam = 1 + arb.const_euler()/2 - (4*arb.pi()).log()/2
    assert upper < ball(F(6309, 10**15))
    assert lam - upper/2 > ball(F(2309570896296,10**14))
    assert upper/lam < ball(F(2732,10**13))
    return {"first_zero_positive_ordinate": bracket(root.imag),
            "counts_with_multiplicity_at_14_and_15": [0,1], "fixed_local_Fourier_samples": errors,
            "verified_height_input": str(3*10**12), "signed_high_zero_sum_upper_expression": bracket(upper,21),
            "coefficient_lower_expression": bracket(lam-upper/2,18),
            "TV_upper_expression": bracket(upper/lam,20)}


def main():
    windows = [(8, F(1,8), F(1,4)), (16, F(1,8), F(1,4)), (32, F(1,8), F(1,4)),
               (16, F(1,4), F(1,2))]
    data = {"dependencies": {"python-flint": "0.9.0", "precision_bits": ctx.prec},
            "scope": "finite original-road intervals, rational profile identities, finite certified zero checks",
            "profiles": polynomial_rows(), "zero_and_constants": zero_fixture(),
            "finite_raw_windows": [raw_window(*case) for case in windows]}
    print(json.dumps(data, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
