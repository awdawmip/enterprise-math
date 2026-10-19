"""Exact, small-domain algebra audit; inputs p,q are explicitly supplied.

This is a task-local certificate, not an N-only moment extractor.
Run with the standard Python library and the existing Enterprise Math source.
"""
from fractions import Fraction as F
from math import comb, gcd
from pathlib import Path
import argparse
import hashlib
import json
import sys

ROOT = Path(__file__).resolve().parent
parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument("--enterprise-root", type=Path, default=ROOT.parent)
parser.add_argument("--output-dir", type=Path, default=ROOT)
args = parser.parse_args()
REUSED_ROOT = args.enterprise_root.resolve()
sys.path.insert(0, str(REUSED_ROOT / "src"))
from enterprise_math.brc_moment_transfer import moment_transition_matrix


def carrier(k):
    return [(r, s) for r in range((k - 1) // 2 + 1)
            for s in range((k // (2 * r + 1) - 1) // 2 + 1)]


def central_polynomial(points, degree):
    n = len(points)
    t = F(sum(r for r, _ in points), n)
    assert sum(s for _, s in points) == n * t
    # Entry j is the coefficient of p**(degree-j) * q**j.
    return [comb(degree, j) * sum((F(r) - t) ** (degree-j)
            * (F(s) - t) ** j for r, s in points)
            for j in range(degree + 1)]


def symmetric_basis(coeff):
    degree = len(coeff) - 1
    assert coeff == coeff[::-1]
    residual = coeff[:]
    result = []
    for j in range(degree // 2 + 1):
        c = residual[j]
        result.append(c)
        for h in range(degree - 2 * j + 1):
            residual[j+h] -= c * comb(degree-2*j, h)
    assert all(c == 0 for c in residual)
    return result


def direct_moment(points, p, q, degree):
    ys = [r*p + s*q for r, s in points]
    mean = F(sum(ys), len(ys))
    return sum((F(y)-mean)**degree for y in ys)


def cubic_coefficients(points):
    n = len(points)
    r1 = sum(r for r, s in points)
    r2 = sum(r*r for r, s in points)
    rs = sum(r*s for r, s in points)
    r3 = sum(r**3 for r, s in points)
    r2s = sum(r*r*s for r, s in points)
    a = F(n*n*r3 - 3*n*r1*r2 + 2*r1**3, n*n)
    b = F(3*n*n*(r2s-r3) + 6*n*r1*(r2-rs), n*n)
    return a, b


def h3(p, q):
    s, n = p+q, p*q
    return 2*s**3 - 9*n*s


def module_moment(points, p, q, degree):
    # Shift by 1 so the existing positive-weight API accepts the zero branch.
    # Central moments are invariant under this common translation.
    edges = [(0, 0, 1+r*p+s*q) for r, s in points]
    raw = [moment_transition_matrix(1, edges, j)[0][0]
           for j in range(degree + 1)]
    mean = raw[1]/raw[0]
    return sum(comb(degree, j)*(-mean)**(degree-j)*raw[j]
               for j in range(degree+1))


def main():
    result = {
        "researcher_id": "EM-HME-0CE4FD",
        "scope": "direct mathematical audit; explicit p,q; no N-only extractor",
        "global_snapshot": "dde41a0cf844b545f7490995264aff6d4980adc0",
        "module_source_snapshot": "ef1893382eb1dcfcd773e19882569e9ff072a8ee",
        "module_path": "src/enterprise_math/brc_moment_transfer.py",
        "module_sha256": hashlib.sha256((REUSED_ROOT / "src/enterprise_math/brc_moment_transfer.py").read_bytes()).hexdigest(),
        "polynomials": {},
    }
    checks = 0
    for k in (3, 5, 7, 9):
        points = carrier(k)
        assert set(points) == {(s, r) for r, s in points}
        a, b = cubic_coefficients(points)
        assert [a, b] == symmetric_basis(central_polynomial(points, 3))
        entry = {"n": len(points), "points": points,
                 "M3_S3_NS": [str(a), str(b)], "central_S_N_basis": {}}
        for degree in range(2, 9):
            coeff = symmetric_basis(central_polynomial(points, degree))
            entry["central_S_N_basis"][str(degree)] = [str(c) for c in coeff]
            for p in range(1, 17):
                for q in range(1, 17):
                    s, n = p+q, p*q
                    predicted = sum(c*s**(degree-2*j)*n**j
                                    for j, c in enumerate(coeff))
                    assert predicted == direct_moment(points, p, q, degree)
                    checks += 1
        result["polynomials"][str(k)] = entry
    assert result["polynomials"]["3"]["M3_S3_NS"] == ["2/9", "-1"]
    assert result["polynomials"]["5"]["M3_S3_NS"] == ["54/25", "-9"]
    assert result["polynomials"]["7"]["M3_S3_NS"] == ["432/49", "-36"]

    module_checks = 0
    for k in (3, 5, 7, 9):
        for p, q in ((3, 5), (5, 7), (2, 13)):
            for degree in (2, 3, 4):
                assert module_moment(carrier(k), p, q, degree) == direct_moment(carrier(k), p, q, degree)
                module_checks += 1

    triple_checks = 0
    for p in range(1, 17):
        for q in range(1, 17):
            points = carrier(3)
            m2, m3, m4 = [direct_moment(points, p, q, j) for j in (2, 3, 4)]
            e = 2*(p+q)**2 - 6*p*q
            assert 9*m3 == h3(p, q)
            assert h3(p, q) == (p+q)*(2*p-q)*(p-2*q)
            assert m2 == F(e, 3)
            assert m4 == m2*m2/2 == F(e*e, 18)
            ys = [0, p, q]
            assert sum((a-b)*(b-c)*(c-a) for a in ys for b in ys for c in ys) == 0
            # Newton recurrence of the three centered points.
            ms = [F(3), F(0), m2, m3]
            for degree in range(4, 11):
                ms.append(m2*ms[degree-2]/2 + m3*ms[degree-3]/3)
                assert ms[-1] == direct_moment(points, p, q, degree)
            triple_checks += 1

    local_moduli = []
    for modulus in range(2, 33):
        fibers = {}
        for a in range(modulus):
            for b in range(modulus):
                if gcd(a*b, modulus) != 1:
                    continue
                fibers.setdefault(a*b % modulus, set()).add(h3(a, b) % modulus)
        constant = all(len(v) == 1 for v in fibers.values())
        assert constant == (4 % modulus == 0)
        fiber_sums = {
            n: sum(h3(a, b) for a in range(modulus) for b in range(modulus)
                   if a*b % modulus == n) % modulus
            for n in fibers
        }
        assert all(total == 0 for total in fiber_sums.values())
        local_moduli.append({"modulus": modulus,
                             "product_only_on_all_unit_fibers": constant,
                             "sum_over_each_unit_product_fiber_is_zero": True})
    result["unit_fiber_checks"] = local_moduli

    # Distinct odd prime pairs, using a small modulus only.
    examples = []
    for p, q in ((3, 13), (7, 17)):
        n, s = p*q, p+q
        examples.append({"p": p, "q": q, "N": n, "S": s,
                         "N_mod5": n % 5, "S2_mod5": s*s % 5,
                         "E3_mod5": (2*s*s-6*n) % 5,
                         "H3": h3(p, q), "H3_mod5": h3(p,q) % 5})
    assert examples[0]["N_mod5"] == examples[1]["N_mod5"]
    assert examples[0]["S2_mod5"] == examples[1]["S2_mod5"]
    assert examples[0]["E3_mod5"] == examples[1]["E3_mod5"]
    assert examples[0]["H3_mod5"] != examples[1]["H3_mod5"]
    result["same_even_observer_distinct_odd_residue"] = examples
    result["checks"] = {"polynomial_evaluations": checks,
                        "existing_module_reuse": module_checks,
                        "K3_recurrence_and_cancellation_cases": triple_checks,
                        "unit_ring_moduli": len(local_moduli)}
    result["verdict"] = "PASS_EXACT_ALGEBRA_AND_FINITE_CHECKS; NONLY_EXTRACTION_NOT_ESTABLISHED"
    args.output_dir.mkdir(parents=True, exist_ok=True)
    (args.output_dir / "certificate.json").write_text(json.dumps(result, indent=2), encoding="utf-8")
    print(json.dumps({"checks": result["checks"],
                      "cubic": {k: v["M3_S3_NS"] for k,v in result["polynomials"].items()},
                      "examples": examples,
                      "verdict": result["verdict"]}, indent=2))


if __name__ == "__main__":
    main()

