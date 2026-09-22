"""Task-local exact p19 order-9 recovery and bounded (4,5) census.

FLINT LLL only proposes an integer change of basis; native integer checks verify
its product and unimodularity. All materialized divisions/remainders in this
consumer enter the existing BRC facade. No Fraction or floating proof state.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import time
from pathlib import Path

from enterprise_math.exact_arithmetic import division, brc_evaluate_division

TRACE_COUNT = 0
TRACE_SAMPLES = []
P = 19
BUDGET = 2331
WEIGHTS = [19 * r - 1 for r in range(1, 19)]


def qr(n, d):
    global TRACE_COUNT
    if d <= 0:
        raise ValueError("positive divisor required")
    t = brc_evaluate_division(division(abs(n), d))
    TRACE_COUNT += 1
    if len(TRACE_SAMPLES) < 12:
        TRACE_SAMPLES.append(vars(t))
    q, r = t.quotient, t.remainder
    if n < 0:
        q, r = (-q, 0) if r == 0 else (-q - 1, d - r)
    assert n == q * d + r and 0 <= r < d
    return q, r


def exact(n, d):
    q, r = qr(n, d)
    assert r == 0
    return q


def rem(n, d):
    return qr(n, d)[1]


def gcd(a, b):
    a, b = abs(a), abs(b)
    while b:
        a, b = b, rem(a, b)
    return a


def inv(a, modulus):
    r0, r1, t0, t1 = modulus, rem(a, modulus), 0, 1
    while r1:
        q, r = qr(r0, r1)
        r0, r1, t0, t1 = r1, r, t1, t0 - q * t1
    assert r0 == 1
    answer = rem(t0, modulus)
    assert rem(a * answer, modulus) == 1
    return answer


class Rat:
    def __init__(self, n=0, d=1):
        if d < 0:
            n, d = -n, -d
        if d == 0:
            raise ZeroDivisionError
        g = gcd(n, d)
        self.n, self.d = exact(n, g), exact(d, g)

    def __add__(self, other):
        if isinstance(other, int):
            other = Rat(other)
        return Rat(self.n * other.d + other.n * self.d, self.d * other.d)

    __radd__ = __add__

    def __neg__(self):
        return Rat(-self.n, self.d)

    def __sub__(self, other):
        return self + (-other)

    def __mul__(self, other):
        if isinstance(other, int):
            other = Rat(other)
        return Rat(self.n * other.n, self.d * other.d)

    __rmul__ = __mul__

    def ratio(self, other):
        return Rat(self.n * other.d, self.d * other.n)

    def pair(self):
        return [self.n, self.d]


def dot(x, y):
    return sum(a * b for a, b in zip(x, y))


def determinant(matrix):
    a = [list(row) for row in matrix]
    last, sign = 1, 1
    for k in range(len(a) - 1):
        if a[k][k] == 0:
            j = next(j for j in range(k + 1, len(a)) if a[j][k])
            a[k], a[j] = a[j], a[k]
            sign = -sign
        pivot = a[k][k]
        for i in range(k + 1, len(a)):
            for j in range(k + 1, len(a)):
                numerator = a[i][j] * pivot - a[i][k] * a[k][j]
                a[i][j] = exact(numerator, abs(last)) * (1 if last > 0 else -1)
            a[i][k] = 0
        last = pivot
    return sign * a[-1][-1]


def matrix_product(a, b):
    return [[sum(a[i][k] * b[k][j] for k in range(len(b)))
             for j in range(len(b[0]))] for i in range(len(a))]


def gram_schmidt(rows):
    stars, norms, projections = [], [], []
    for row in rows:
        v = [Rat(x) for x in row]
        for star, norm in zip(stars, norms):
            coefficient = sum(x * y for x, y in zip(row, star)).ratio(norm)
            v = [x - coefficient * y for x, y in zip(v, star)]
        norm = sum(x * x for x in v)
        assert norm.n > 0
        stars.append(v)
        norms.append(norm)
        projections.append([x.ratio(norm) for x in v])
    return norms, projections


def build_input():
    from flint import fmpz_mat

    basis = [[int(i == j) for j in range(18)] for i in range(18)]
    stages = []
    for k in range(1, 7):
        modulus = 19 ** k
        coefficients = [inv(r ** k, modulus) for r in range(1, 19)]
        c = [rem(dot(row, coefficients), modulus) for row in basis]
        pivot = next(j for j in range(18) if rem(c[j], 19))
        pivot_inv = inv(c[pivot], modulus)
        saved = list(basis[pivot])
        stages.append({"k": k, "modulus": modulus, "coefficients": coefficients,
                       "pivot_inverse": pivot_inv, "pivot_row": saved})
        next_basis = []
        for i, row in enumerate(basis):
            if i == pivot:
                next_basis.append([modulus * x for x in row])
            else:
                t = rem(c[i] * pivot_inv, modulus)
                next_basis.append([x - t * y for x, y in zip(row, saved)])
        basis = next_basis
    weighted = [[a * w for a, w in zip(row, WEIGHTS)] for row in basis]
    proposal, transform = fmpz_mat(weighted).lll(transform=True, gram="exact")
    reduced = [[int(proposal[i, j]) for j in range(18)] for i in range(18)]
    transform = [[int(transform[i, j]) for j in range(18)] for i in range(18)]
    assert matrix_product(transform, weighted) == reduced
    assert abs(determinant(transform)) == 1
    unweighted = [[exact(x, w) for x, w in zip(row, WEIGHTS)] for row in reduced]
    assert abs(determinant(unweighted)) == 19 ** 21
    for row in unweighted:
        for stage in stages:
            assert rem(dot(row, stage["coefficients"]), stage["modulus"]) == 0
    norms, projectors = gram_schmidt(reduced)
    scaled, denominators = [], []
    for projector in projectors:
        denominator = 1
        for x in projector:
            denominator = exact(denominator, gcd(denominator, x.d)) * x.d
        denominators.append(denominator)
        scaled.append([x.n * exact(denominator, x.d) for x in projector])
    mu_scaled = [[dot(row, projector) for projector in scaled] for row in reduced]
    # In split (4,5), maximal residual side budgets are 869 and 508.
    radius_squared_max = 869 ** 2 + 508 ** 2
    assert all(d.n > 4 * radius_squared_max * d.d for d in norms)
    atoms = [(q, r, 361 * q + 19 * r - 1)
             for q in range(1, 7) for r in range(1, 19)
             if 361 * q + 19 * r - 1 <= BUDGET]
    atom_representatives = []
    for q, r, _ in atoms:
        u = [0] * 18
        for stage in stages:
            target = -inv((r + 19 * q) ** stage["k"], stage["modulus"])
            residual = rem(target - dot(u, stage["coefficients"]), stage["modulus"])
            t = rem(residual * stage["pivot_inverse"], stage["modulus"])
            u = [x + t * y for x, y in zip(u, stage["pivot_row"])]
        atom_representatives.append(u)
    result = {"schema": "T6_P19_ORDER9_NATIVE_INPUT_V1", "prime": 19,
              "side_budget": BUDGET, "lattice_index": 19 ** 21,
              "stages": stages, "weighted_basis": reduced,
              "unweighted_basis": unweighted, "proposal_transform": transform,
              "saturated_basis": basis, "gram_schmidt_norms": [x.pair() for x in norms],
              "projector_numerators": scaled, "projector_denominators": denominators,
              "mu_scaled": mu_scaled, "atoms": atoms,
              "atom_representatives": atom_representatives,
              "max_radius_squared_4_5": radius_squared_max,
              "flatness_verified": True, "basis_proposal_only": "python-flint LLL",
              "brc_evaluations": TRACE_COUNT, "trace_samples": TRACE_SAMPLES}
    return result


def verify_input(data):
    assert data["prime"] == 19 and data["side_budget"] == BUDGET
    basis = data["weighted_basis"]
    u = [[exact(x, w) for x, w in zip(row, WEIGHTS)] for row in basis]
    assert u == data["unweighted_basis"]
    assert abs(determinant(u)) == 19 ** 21
    # Six reciprocal checks have full rank mod19, hence jointly surject onto
    # the mixed moduli. Inclusion plus equal index proves saturation.
    small = [[inv(r ** k, 19) for r in range(1, 7)] for k in range(1, 7)]
    assert rem(determinant(small), 19) != 0
    for row in u:
        for k in range(1, 7):
            modulus = 19 ** k
            assert rem(sum(a * inv(r ** k, modulus) for r, a in enumerate(row, 1)), modulus) == 0
    norms, projectors = gram_schmidt(basis)
    assert [x.pair() for x in norms] == data["gram_schmidt_norms"]
    for i, row in enumerate(projectors):
        d = data["projector_denominators"][i]
        assert d > 0
        for j, x in enumerate(row):
            assert x.n * d == x.d * data["projector_numerators"][i][j]
        assert norms[i].n > 4 * data["max_radius_squared_4_5"] * norms[i].d
    assert data["max_radius_squared_4_5"] == 869 ** 2 + 508 ** 2
    assert data["mu_scaled"] == [[dot(row, p) for p in data["projector_numerators"]] for row in basis]
    assert data["atoms"] == [[q, r, 361 * q + 19 * r - 1]
                             for q in range(1, 7) for r in range(1, 19)
                             if 361 * q + 19 * r - 1 <= BUDGET]
    assert len(data["atom_representatives"]) == len(data["atoms"])
    for (q, r, cost), u in zip(data["atoms"], data["atom_representatives"]):
        assert cost == 361 * q + 19 * r - 1
        for k in range(1, 7):
            modulus = 19 ** k
            value = sum(a * inv(s ** k, modulus) for s, a in enumerate(u, 1))
            assert rem(value + inv((r + 19 * q) ** k, modulus), modulus) == 0


def states(order, data):
    atoms = data["atoms"]
    out = []
    def visit(start, left, cost, chosen):
        if left == 0:
            u = [sum(data["atom_representatives"][a][r] for a in chosen) for r in range(18)]
            weighted = [a * w for a, w in zip(u, WEIGHTS)]
            # A coset-equivalent small representative; not a mass-budget test.
            for i in range(17, -1, -1):
                d = data["projector_denominators"][i]
                n = dot(weighted, data["projector_numerators"][i])
                nearest = qr(2 * n + d, 2 * d)[0]
                weighted = [a - nearest * b for a, b in zip(weighted, data["weighted_basis"][i])]
            centers = [dot(weighted, p) for p in data["projector_numerators"]]
            mask = 0
            for a in chosen:
                mask |= 1 << a
            out.append({"atoms": list(chosen), "mask": mask, "cost": cost,
                        "weighted_representative": weighted, "centers": centers})
            return
        for a in range(start, len(atoms)):
            q, _, c = atoms[a]
            if q > left or cost + c > BUDGET:
                continue
            visit(a, left - q, cost + c, chosen + [a])
    visit(0, order, 0, [])
    return out


def check_pair(positive, negative, data):
    remaining_positive = BUDGET - positive["cost"]
    remaining_negative = BUDGET - negative["cost"]
    radius_squared = remaining_positive ** 2 + remaining_negative ** 2
    chosen = [0] * 18
    lower = 0
    for i in range(17, -1, -1):
        d = data["projector_denominators"][i]
        n = positive["centers"][i] - negative["centers"][i]
        n += sum(chosen[j] * data["mu_scaled"][j][i] for j in range(i + 1, 18))
        nearest = qr(2 * n + d, 2 * d)[0]
        chosen[i] = -nearest
        error = n - nearest * d
        dn, dd = data["gram_schmidt_norms"][i]
        # Sum of floors is an exact integer lower bound on the partial norm.
        lower += qr(error * error * dn, d * d * dd)[0]
        if lower > radius_squared:
            return None, 18 - i
    weighted = [a - b for a, b in zip(positive["weighted_representative"], negative["weighted_representative"])]
    for i, n in enumerate(chosen):
        weighted = [a + n * b for a, b in zip(weighted, data["weighted_basis"][i])]
    if sum(x * x for x in weighted) > radius_squared:
        return None, 19
    pos = sum(max(0, x) for x in weighted)
    neg = sum(max(0, -x) for x in weighted)
    if pos > remaining_positive or neg > remaining_negative:
        return None, 20
    u = [exact(x, w) for x, w in zip(weighted, WEIGHTS)]
    return {"q0": u, "positive_vertical": positive["atoms"],
            "negative_vertical": negative["atoms"],
            "positive_mass": pos + positive["cost"], "negative_mass": neg + negative["cost"]}, 21


def census(data, start, stop, max_seconds):
    started = time.monotonic()
    positive, negative = states(4, data), states(5, data)
    assert len(positive) == 8124 and len(negative) == 8506
    if not 0 <= start < stop <= len(positive):
        raise ValueError("invalid exact order-4 row interval")
    counters = [0] * 22
    primitive, cancelled, complete_stop = 0, 0, start
    hit = None
    for i in range(start, stop):
        if time.monotonic() - started >= max_seconds:
            break
        for j, state in enumerate(negative):
            if positive[i]["mask"] & state["mask"]:
                cancelled += 1
                continue
            primitive += 1
            hit, stage = check_pair(positive[i], state, data)
            counters[stage] += 1
            if hit is not None:
                hit.update(positive_index=i, negative_index=j)
                break
        if hit is not None:
            break
        complete_stop = i + 1
        if i == start or rem(i + 1 - start, 25) == 0:
            print(json.dumps({"completed_stop": complete_stop, "primitive": primitive,
                              "elapsed_seconds": time.monotonic() - started}), flush=True)
    return {"schema": "T6_P19_ORDER9_4_5_PARTIAL_CENSUS_V1",
            "status": "MODULAR_KERNEL_FOUND" if hit else "EXACT_INTERVAL_CLEAR" if complete_stop == stop else "RESOURCE_LIMIT_PARTIAL_CLEAR",
            "requested_rows": [start, stop], "completed_rows": [start, complete_stop],
            "state_counts": [len(positive), len(negative)],
            "primitive_cosets_checked": primitive, "cancelled_pairs": cancelled,
            "rejection_depth_counts": counters, "kernel": hit,
            "brc_evaluations": TRACE_COUNT, "trace_samples": TRACE_SAMPLES,
            "elapsed_seconds": time.monotonic() - started,
            "scope": "Only the named order-4 row interval against every order-5 state; not full order9 or T6"}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("command", choices=["build", "verify", "run"])
    parser.add_argument("--input", type=Path, default=Path(__file__).with_name("input.json"))
    parser.add_argument("--output", type=Path)
    parser.add_argument("--start", type=int, default=0)
    parser.add_argument("--stop", type=int, default=8124)
    parser.add_argument("--max-seconds", type=int, default=240)
    args = parser.parse_args()
    if args.command == "build":
        data = build_input()
        args.input.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8", newline="\n")
        print(json.dumps({"status": "INPUT_BUILT_AND_VERIFIED", "brc_evaluations": TRACE_COUNT}))
        return
    data = json.loads(args.input.read_text(encoding="utf-8"))
    verify_input(data)
    if args.command == "verify":
        print(json.dumps({"status": "DIRECT_INTEGER_INPUT_CHECK_PASS", "brc_evaluations": TRACE_COUNT}))
        return
    result = census(data, args.start, args.stop, args.max_seconds)
    result["input_sha256"] = hashlib.sha256(args.input.read_bytes()).hexdigest()
    result["source_sha256"] = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    if args.output is None:
        raise ValueError("--output is required for a census")
    args.output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8", newline="\n")
    print(json.dumps(result, ensure_ascii=False), flush=True)


if __name__ == "__main__":
    main()
