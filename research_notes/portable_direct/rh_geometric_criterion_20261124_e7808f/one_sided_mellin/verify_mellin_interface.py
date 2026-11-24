#!/usr/bin/env python3
"""Finite author checks for PROOF.md, never a zero search or RH verification.

Checks the exact algebra used to identify the smoothed Mellin transform, and
certifies selected integer-cell curvature gaps using outward integer intervals.
No D, c, or q cache is generated or read.  The interval helper is a retained,
audited dependency from the previous finite certificate.
"""
from fractions import Fraction as F
from pathlib import Path
import hashlib
import importlib.util
import json
import sympy as sp

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
HELPER = ROOT / "prior/extracted/riemann_cumulative_haar_20261123/dependencies/certify_fast_harmonic_energy.py"
spec = importlib.util.spec_from_file_location("retained_interval_helper", HELPER)
iv = importlib.util.module_from_spec(spec)
spec.loader.exec_module(iv)


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def log_rat(x):
    x = F(x)
    return iv.sub(iv.log_int(x.numerator), iv.log_int(x.denominator))


def main():
    s, rho, a = sp.symbols("s rho a")
    gam, ell2, ellpi, dig, zlog = sp.symbols("gamma log2 logpi digamma zeta_log_derivative")
    exact = {}

    zero_left = s*(s-1)/(rho*(1-rho)*(s-rho))
    zero_right = s/(rho*(1-rho)) - (1/(s-rho) + 1/rho)
    exact["zero_partial_fraction_5_6"] = sp.cancel(zero_left-zero_right) == 0

    trivial_left = -s*(s-1)/(a*(a+1)*(s+a))
    trivial_right = -s/(a*(a+1)) + 1/a - 1/(s+a)
    exact["trivial_partial_fraction_5_7"] = sp.cancel(trivial_left-trivial_right) == 0

    C = ell2 + ellpi
    C0 = 2 + gam - 2*ell2 - ellpi
    b = -1 - gam/2 + ell2 + ellpi/2
    T0 = 1-ell2
    H = 1/s + 1/(s-1) - ellpi/2 + dig/2 + zlog
    transformed = C*(s-1) + s*C0-H+b-s*T0+(dig+2/s+gam)/2
    desired = s*(1+gam)-1-1/(s-1)-zlog
    exact["aggregate_mellin_identity_5_8"] = sp.cancel(transformed-desired) == 0
    exact["x_equals_one_5_9"] = sp.expand(C+C0-T0-(1+gam)) == 0

    t, z1 = sp.symbols("t z1")
    Laurent = (1+gam)/t - 1/t**2 - (-1/t+gam+z1*t)/((1+t)*t)
    expanded = sp.series(Laurent, t, 0, 1).removeO().expand()
    exact["double_pole_cancelled_at_one"] = expanded.coeff(t, -2) == 0
    exact["simple_pole_cancelled_at_one"] = expanded.coeff(t, -1) == 0
    assert all(exact.values()), exact

    ns = list(range(1,65)) + [127,128,255,256,1023,1024,32767,32768,2**20,2**30]
    grid = [F(j,8) for j in range(1,8)]
    cells = []
    for n in ns:
        for u in grid:
            x = F(n)+u
            gap = iv.sub(
                iv.add(iv.qmul(iv.log_int(n), (1-u)*n),
                       iv.qmul(iv.log_int(n+1), u*(n+1))),
                iv.qmul(log_rat(x), x))
            bound = u*(1-u)/(2*n)
            # These are rigorous comparisons of the entire interval to 0 and
            # to the exact rational upper bound, not floating tolerances.
            assert gap[0] >= 0
            assert F(gap[1],iv.S) <= bound
            assert bound <= F(1,8*n)
            cells.append({"n":n, "u":str(u), "gap":iv.record(gap),
                          "analytic_upper_bound":str(bound)})

    certificate = {
        "researcher_id":"EM-DIRECT-E7808F",
        "activity_id":"RA-0B92AAF774CA466C1C1BC38B",
        "status":"finite author verification; not independent Review or RH verification",
        "scope":["six exact symbolic algebra checks", "518 outward-interval curvature checks"],
        "exact_algebra":exact,
        "curvature_check_count":len(cells),
        "curvature_checks":cells,
        "dependencies":{"interval_helper":str(HELPER.relative_to(ROOT)),
                        "interval_helper_sha256":digest(HELPER),
                        "script_sha256":digest(Path(__file__)),
                        "proof_sha256":digest(HERE/"PROOF.md")},
        "no_full_road_cache_used":True,
        "no_zero_truncation_used":True,
    }
    target = HERE/"mellin_interface_certificate.json"
    target.write_text(json.dumps(certificate,ensure_ascii=False,indent=2)+"\n")
    print(json.dumps({"output":str(target),"exact_checks":len(exact),
                      "curvature_checks":len(cells),"all_passed":True},ensure_ascii=False))


if __name__ == "__main__":
    main()
