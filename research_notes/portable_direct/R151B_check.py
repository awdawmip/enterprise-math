#!/usr/bin/env python3
"""R151B exact finite check of the CRT covariance gauge normal form."""
from fractions import Fraction
from math import gcd, lcm
from json import dump

def units(g):
    return [x for x in range(g) if gcd(x, g) == 1] if g > 1 else [0]

def wave(g, s, t, u, v, n, m):
    q = Fraction(g-1, 2)
    a = [(s*j + u) % g - q for j in range(g)]
    b = [(t*j + v) % g - q for j in range(g)]
    return tuple(sum(a[j]*b[(j+h) % g] for j in range(g)) / (g*n*m)
                 for h in range(g))

def run():
    case_count = waveform_checks = class_checks = 0
    for g in range(1, 11):
        for s in units(g):
            for t in units(g):
                ell = pow(s, -1, g) if g > 1 else 0
                signature_by_rho = {}
                for u in range(g):
                    for v in range(g):
                        rho = (v - t*ell*u) % g if g > 1 else 0
                        f = wave(g, s, t, u, v, g, g)
                        for h in range(g):
                            expected = (Fraction((t*h + rho) % g, 1) -
                                        Fraction(g-1, 2)) / g**2 if g > 1 else Fraction(0)
                            assert f[(h+ell) % g] - f[h] == expected
                            waveform_checks += 1
                        if rho in signature_by_rho:
                            assert signature_by_rho[rho] == f
                        else:
                            signature_by_rho[rho] = f
                        case_count += 1
                assert len(signature_by_rho) == len(set(signature_by_rho.values())) == g
                class_checks += 1

    n, m, s, t, u, v = 4, 6, 3, 5, 1, -2
    g = gcd(n, m)
    ell = pow(s, -1, g)
    rho = (v - t*ell*u) % g
    f = wave(g, s, t, u, v, n, m)
    assert all(f[(h+ell) % g] - f[h] ==
               Fraction((t*h + rho) % g, n*m) - Fraction(g-1, 2*n*m)
               for h in range(g))
    P = lcm(n, m)
    x = [Fraction((s*j+u) % n, n)-Fraction(n-1, 2*n) for j in range(P)]
    y = [Fraction((t*j+v) % m, m)-Fraction(m-1, 2*m) for j in range(P)]
    assert f == tuple(sum(x[j]*y[(j+h) % P] for j in range(P))/P for h in range(g))
    out = {
        "marker": "R151B_CRT_GAUGE_NORMAL_FORM_PASS",
        "g_range": "1..10", "cases": case_count,
        "lag_differences": waveform_checks,
        "complete_waveform_class_checks": class_checks,
        "independent_full_lcm_example": {"g": g, "rho": rho, "wave": [str(z) for z in f]},
        "arithmetic": "Exact arbitrary precision integers and fractions",
        "review": "NOT_REVIEWED"
    }
    with open("R151B_verification.json", "w", encoding="utf-8") as handle:
        dump(out, handle, indent=2)
    print(out)

if __name__ == "__main__":
    run()
