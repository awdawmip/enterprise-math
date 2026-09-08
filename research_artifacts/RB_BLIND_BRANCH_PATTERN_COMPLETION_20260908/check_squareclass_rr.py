"""Task-local integer identities for the blind square-class and RR reduction.

This does not evaluate roots, rational functions, RR bases or elliptic maps.
All ring operations below are integer polynomial additions, multiplications
and formal relation rewrites. The named generators are not evaluated numbers.
"""
from __future__ import annotations

import argparse
import hashlib
import itertools
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
REL = "research_artifacts/RB_BLIND_BRANCH_PATTERN_COMPLETION_20260908"
ASSIGNMENT_SHA = "a83524c6b9b8cb6e00561c014e7129c614e9b1c46eedcbd9c9e79f2ff5ee89a0"
SOURCE_SHA = "516400d46ae5dd5a8aa2d25520021ee3a57dc839538746a550ad2a7bfae2a473"
NAMES = ("a", "b", "c", "d", "e", "f", "R", "t", "k", "s")
ZERO_MONOMIAL = (0,) * len(NAMES)
V4 = ((0, 1, 2, 3), (1, 0, 3, 2), (2, 3, 0, 1), (3, 2, 1, 0))


def encoded(value):
    return (json.dumps(value, ensure_ascii=False, sort_keys=True, indent=2) + "\n").encode("utf-8")


def add(*polynomials):
    result = {}
    for polynomial in polynomials:
        for monomial, coefficient in polynomial.items():
            result[monomial] = result.get(monomial, 0) + coefficient
    return {monomial: coefficient for monomial, coefficient in result.items() if coefficient}


def scale(polynomial, integer):
    return {monomial: coefficient * integer for monomial, coefficient in polynomial.items()
            if coefficient * integer}


def constant(integer):
    return {ZERO_MONOMIAL: integer} if integer else {}


def rr_fiber_difference(x_section, shifted_fiber_section):
    """X minus (X-a), or their common-denominator numerator sections."""
    return add(x_section, scale(shifted_fiber_section, -1))


def variable(index):
    powers = list(ZERO_MONOMIAL)
    powers[index] = 1
    return {tuple(powers): 1}


def reduce_curve(polynomial):
    """Formal rules s^2=3 and t^2=R^3-3R; no value of s or t is computed."""
    work = list(polynomial.items())
    result = {}
    while work:
        monomial, coefficient = work.pop()
        powers = list(monomial)
        if powers[9] >= 2:
            powers[9] -= 2
            work.append((tuple(powers), 3 * coefficient))
        elif powers[7] >= 2:
            powers[7] -= 2
            cubic = list(powers)
            cubic[6] += 3
            linear = list(powers)
            linear[6] += 1
            work.append((tuple(cubic), coefficient))
            work.append((tuple(linear), -3 * coefficient))
        else:
            result[monomial] = result.get(monomial, 0) + coefficient
    return add(result)


def multiply(*polynomials):
    result = constant(1)
    for polynomial in polynomials:
        product = {}
        for left, left_coefficient in result.items():
            for right, right_coefficient in polynomial.items():
                powers = tuple(x + y for x, y in zip(left, right))
                product[powers] = product.get(powers, 0) + left_coefficient * right_coefficient
        result = reduce_curve(product)
    return result


def twice_delta(polynomial):
    """The derivation 2*delta has D(R)=2t, D(t)=3R^2-3."""
    result = {}
    for monomial, coefficient in polynomial.items():
        if monomial[6]:
            powers = list(monomial)
            exponent = powers[6]
            powers[6] -= 1
            powers[7] += 1
            result = add(result, {tuple(powers): 2 * exponent * coefficient})
        if monomial[7]:
            powers = list(monomial)
            exponent = powers[7]
            powers[7] -= 1
            square = list(powers)
            square[6] += 2
            result = add(result, {tuple(square): 3 * exponent * coefficient},
                         {tuple(powers): -3 * exponent * coefficient})
    return reduce_curve(result)


def restrict_to_critical_divisor(polynomial):
    """Formal substitutions t=-k and R^3=3R+k^2, with integer coefficients."""
    work = []
    for monomial, coefficient in polynomial.items():
        powers = list(monomial)
        while powers[7]:
            powers[7] -= 1
            powers[8] += 1
            coefficient = -coefficient
        work.append((tuple(powers), coefficient))
    result = {}
    while work:
        monomial, coefficient = work.pop()
        if monomial[6] >= 3:
            linear = list(monomial)
            linear[6] -= 2
            constant_term = list(monomial)
            constant_term[6] -= 3
            constant_term[8] += 2
            work.append((tuple(linear), 3 * coefficient))
            work.append((tuple(constant_term), coefficient))
        else:
            result[monomial] = result.get(monomial, 0) + coefficient
    return add(result)


def polynomial_rows(polynomial):
    return [{"coefficient": coefficient, "powers": dict(zip(NAMES, monomial))}
            for monomial, coefficient in sorted(polynomial.items())]


def check_integer_identities():
    a, b, c, d, e, f, R, t, k, s = (variable(i) for i in range(len(NAMES)))
    gamma = (constant(1), R, add(R, scale(s, -1)), add(R, s))
    allowed = []
    rejected = 0
    for twists in itertools.product(range(4), repeat=3):
        first, second, third = twists
        if first ^ second ^ third:
            rejected += 1
            continue
        nonzero = tuple(x for x in twists if x)
        if not nonzero:
            factor, factor_name = constant(1), "1"
        elif len(nonzero) == 2:
            if nonzero[0] != nonzero[1]:
                raise AssertionError("zero torsion class did not pair")
            factor, factor_name = gamma[nonzero[0]], ("1", "R", "R-s", "R+s")[nonzero[0]]
        else:
            if set(nonzero) != {1, 2, 3}:
                raise AssertionError("invalid three-torsion product")
            factor, factor_name = t, "t"
        if multiply(*(gamma[x] for x in twists)) != multiply(factor, factor):
            raise AssertionError("geometric square-class product identity failed")
        allowed.append({"twists_0_1_lambda": twists, "product_square_factor": factor_name})
    if len(allowed) != 16 or rejected != 48:
        raise AssertionError("incomplete torsion compatibility table")

    numerator = add(multiply(a, t), multiply(b, R), c)
    denominator = add(multiply(d, t), multiply(e, R), f)
    A = add(multiply(a, e), scale(multiply(b, d), -1))
    B = add(multiply(a, f), scale(multiply(c, d), -1))
    C = add(multiply(b, f), scale(multiply(c, e), -1))
    actual = add(multiply(twice_delta(numerator), denominator),
                 scale(multiply(numerator, twice_delta(denominator)), -1))
    expected = add(multiply(A, add(multiply(R, R, R), scale(R, 3))),
                   scale(multiply(B, add(multiply(R, R), constant(-1))), 3),
                   scale(multiply(C, t), 2))
    if actual != expected:
        raise AssertionError("cleared derivative numerator identity failed")
    restricted = restrict_to_critical_divisor(actual)
    expected_restricted = add(multiply(A, add(multiply(k, k), scale(R, 6))),
                              scale(multiply(B, add(multiply(R, R), constant(-1))), 3),
                              scale(multiply(C, k), -2))
    if restricted != expected_restricted:
        raise AssertionError("critical-divisor restriction identity failed")
    # This checks polynomial values, not the spelling of the displayed equations.
    # Here the free coefficient a is only a generic nonzero target-value symbol.
    x_section = add(multiply(R, R), t, b)
    denominator_square = multiply(d, d)
    for shift in (constant(1), a):
        shifted = add(x_section, scale(shift, -1))
        if rr_fiber_difference(x_section, shifted) != shift:
            raise AssertionError("RR fiber-difference sign failed")
        if rr_fiber_difference(multiply(x_section, denominator_square),
                               multiply(shifted, denominator_square)) != multiply(shift, denominator_square):
            raise AssertionError("denominator-cleared RR sign failed")
        if rr_fiber_difference(shifted, x_section) == shift:
            raise AssertionError("the old reversed RR sign was silently accepted")
    # Keep every coefficient; no numerical specialization of k is performed.
    return {"compatible_geometric_twists": allowed, "incompatible_torsion_triples": rejected,
            "cleared_derivative_numerator": polynomial_rows(actual),
            "critical_divisor_restriction": polynomial_rows(restricted),
            "vanishing_coefficients": ["3B", "6A", "A*k^2-3B-2C*k"],
            "rr_sign_identities": ["X-(X-1)=1", "X-(X-a)=a", "D^2*X-D^2*(X-1)=D^2", "D^2*X-D^2*(X-a)=a*D^2"],
            "paper_inference": "The three frozen Q roots are distinct and k is nonzero; hence A=B=C=0, contradicting a degree-three quotient of independent linear forms."}


def build_certificate(root):
    source = root.joinpath(REL, "source_binding.json").read_bytes()
    assignment = root.joinpath(REL, "branch_assignment_classification.json").read_bytes()
    if hashlib.sha256(source).hexdigest() != SOURCE_SHA:
        raise ValueError("source binding changed")
    if hashlib.sha256(assignment).hexdigest() != ASSIGNMENT_SHA:
        raise ValueError("frozen assignment certificate changed")
    inputs = json.loads(assignment)
    patterns = {}
    dimensions = {0: 3, 2: 2, 4: 1}
    for pattern, data in inputs["patterns"].items():
        rows = []
        for orbit in data["partitions"]["fixed_lambda_fixed_k_V4"]:
            original = orbit["representative"]
            candidates = [(tuple(permutation[x] for x in original), permutation)
                          for permutation in V4 if 3 not in tuple(permutation[x] for x in original)]
            if not candidates:
                raise AssertionError("no empty infinity normalization")
            normalized, transport = min(candidates)
            blocks = [tuple(i for i, value in enumerate(normalized) if value == label)
                      for label in range(3)]
            dims = tuple(dimensions[len(block)] for block in blocks)
            if sum(dims) != 6:
                raise AssertionError("incorrect elliptic RR dimensions")
            rows.append({"fixed_parameter_representative": original,
                         "target_V4_transport": transport,
                         "infinity_empty_representative": normalized,
                         "finite_branch_blocks_0_1_lambda": blocks,
                         "RR_section_dimensions_0_1_lambda": dims,
                         "compatible_geometric_twist_table_size": 16})
        if len({tuple(row["infinity_empty_representative"]) for row in rows}) != len(rows):
            raise AssertionError("normalization merged different fixed-parameter orbits")
        patterns[pattern] = {"assignment_components": len(rows),
                             "geometric_squareclass_components": len(rows) * 16,
                             "rows": rows}
    identities = check_integer_identities()
    return {"schema": "RB_BLIND_SQUARECLASS_RR_CERTIFICATE_V1",
            "phase": "BLIND_FORWARD_PROGRESS_NOT_FINAL_RAW_FREEZE",
            "source_binding_sha256": SOURCE_SHA, "assignment_sha256": ASSIGNMENT_SHA,
            "scope": "Exact geometric square-class and RR normal forms; not a solved RR/ODE system or an arithmetic descent certificate.",
            "geometric_field_boundary": "Over an algebraic closure, modulo constant square classes. Base half-points are formal choices; field of definition and nonzero constant factors remain explicit unknowns.",
            "patterns": patterns, "integer_identities": identities,
            "rr_equations": ["alpha0*G0*gamma0*u0^2-alpha1*G1*gamma1*u1^2=1", "alpha0*G0*gamma0*u0^2-alphaLambda*GLambda*gammaLambda*uLambda^2=lambda", "alpha0*G0*gamma0*v0^2-alpha1*G1*gamma1*v1^2=d^2", "alpha0*G0*gamma0*v0^2-alphaLambda*GLambda*gammaLambda*vLambda^2=lambda*d^2"],
            "exclusions": [
                {"subfamily": "X in K(R)", "status": "EXCLUDED_PAPER", "reason": "Even part of fixed-k ODE cannot vanish for nonconstant X and nonzero K."},
                {"subfamily": "4+2 with a finite empty special fiber geometrically square and degree-three square-root pole divisor linearly equivalent to 3O", "status": "EXCLUDED_PAPER_AND_CLEARED_INTEGER_IDENTITY", "reason": "All three Q would be critical for a quotient of independent sections of L(3O); the exact coefficient equations force rank at most one."}],
            "not_excluded": "All 135 branch-assignment components remain represented. General degree-three pole line-bundle class and nontrivial unramified square classes are not removed.",
            "arithmetic": {"evaluated_divisions": 0, "evaluated_roots": 0, "brc_calls": 0,
                           "formal_integer_polynomial_relations": ["s^2=3", "t^2=R^3-3R", "t=-k and R^3=3R+k^2 at the permitted critical divisor"]}}


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT)
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args(argv)
    certificate = build_certificate(args.root)
    data = encoded(certificate)
    path = args.root.joinpath(REL, "squareclass_rr_certificate.json")
    if args.write:
        path.write_bytes(data)
    elif path.read_bytes() != data:
        raise SystemExit("SQUARECLASS_RR: FAIL (certificate bytes differ)")
    print(json.dumps({"status": "PASS", "sha256": hashlib.sha256(data).hexdigest(),
                      "components": {name: row["geometric_squareclass_components"]
                                     for name, row in certificate["patterns"].items()},
                      "compatible_twists": 16, "incompatible_torsion_triples": 48,
                      "cleared_integer_identities": 2,
                      "RR_or_ODE_solution_claimed": False}, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
