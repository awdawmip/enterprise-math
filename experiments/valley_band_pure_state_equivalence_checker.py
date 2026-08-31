#!/usr/bin/env python3
"""Independent checker for the Valley pure-state equivalence task.

The candidate recurrence and the standard continued-fraction reference are
implemented as separate functions.  This file intentionally contains no
source-prototype code and imports only the Python standard library.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import math
from collections import Counter, defaultdict
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable


RESEARCHER_ID = "EM-VBSEQ-7021BF"
TASK_ID = "RS-VALLEY-BAND-PURE-STATE-EQUIVALENCE-CLASSIFICATION"
SEED = "EM-VBSEQ-7021BF|2026-08-23|balanced-exact-80-bit-semiprime|v1"
CASE_COUNT = 20
STEPS_PER_CASE = 5_000
ROOT = Path(__file__).resolve().parents[1]
CSV_PATH = ROOT / "research_output" / "VALLEY_BAND_STATE_MAP_EXCEPTIONS_20260823.csv"
SUMMARY_PATH = ROOT / "research_output" / "evidence" / "VALLEY_BAND_CHECKER_SUMMARY_20260823.json"
MISMATCH_PATH = ROOT / "research_output" / "evidence" / "VALLEY_BAND_MISMATCH_LOG_20260823.jsonl"


@dataclass(frozen=True)
class CandidateState:
    A: int
    B: int
    C: int


@dataclass(frozen=True)
class ReferenceState:
    m: int
    d: int
    a: int
    d_prev: int | None


def candidate_initial(T: int) -> CandidateState:
    return CandidateState(1, -T, 0)


def candidate_digit(T: int, state: CandidateState) -> int:
    # This is the packet's candidate rule, kept separate from the reference.
    return (math.isqrt(T) + abs(state.C)) // abs(state.A)


def candidate_step(state: CandidateState, a: int) -> CandidateState:
    A, B, C = state.A, state.B, state.C
    return CandidateState(A * a * a + 2 * C * a + B, A, A * a + C)


def reference_initial(T: int) -> ReferenceState:
    s = math.isqrt(T)
    return ReferenceState(0, 1, s, None)


def reference_step(T: int, state: ReferenceState) -> ReferenceState:
    # Standard sqrt(T) complete-quotient recurrence; no candidate helper used.
    s = math.isqrt(T)
    m_next = state.d * state.a - state.m
    numerator = T - m_next * m_next
    if numerator <= 0 or numerator % state.d:
        raise AssertionError("invalid standard complete-quotient transition")
    d_next = numerator // state.d
    a_next = (s + m_next) // d_next
    return ReferenceState(m_next, d_next, a_next, state.d)


def reference_to_candidate(n: int, state: ReferenceState) -> CandidateState:
    if n == 0:
        raise ValueError("n=0 uses the special canonical initializer")
    if state.d_prev is None:
        raise ValueError("missing previous denominator")
    sigma = -1 if n & 1 else 1
    return CandidateState(sigma * state.d, -sigma * state.d_prev, -sigma * state.m)


def candidate_to_reference(n: int, T: int, state: CandidateState) -> ReferenceState:
    if n == 0:
        if state != candidate_initial(T):
            raise ValueError("noncanonical n=0 state")
        return reference_initial(T)
    return ReferenceState(abs(state.C), abs(state.A), candidate_digit(T, state), abs(state.B))


def invariant(state: CandidateState) -> int:
    return state.C * state.C - state.A * state.B


def is_repaired_reduced(T: int, state: CandidateState) -> bool:
    if not (state.A * state.B < 0 and state.A * state.C < 0):
        return False
    s = math.isqrt(T)
    m, d = abs(state.C), abs(state.A)
    # Exact integer equivalents of sqrt(T)-m < d < sqrt(T)+m.
    return m < math.isqrt(T) + 1 and d + m >= s + 1 and d - m <= s


def matmul(P: tuple[int, int, int, int], Q: tuple[int, int, int, int]) -> tuple[int, int, int, int]:
    a, b, c, d = P
    e, f, g, h = Q
    return (a * e + b * g, a * f + b * h, c * e + d * g, c * f + d * h)


def form_coefficients_from_matrix(T: int, P: tuple[int, int, int, int]) -> CandidateState:
    p, q, r, u = P
    return CandidateState(p * p - T * r * r, q * q - T * u * u, p * q - T * r * u)


def deterministic_is_prime(n: int) -> bool:
    if n < 2:
        return False
    small = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37)
    for p in small:
        if n % p == 0:
            return n == p
    d, s = n - 1, 0
    while d % 2 == 0:
        d //= 2
        s += 1
    for a in (2, 325, 9_375, 28_178, 450_775, 9_780_504, 1_795_265_022):
        if a % n == 0:
            continue
        x = pow(a, d, n)
        if x in (1, n - 1):
            continue
        for _ in range(s - 1):
            x = x * x % n
            if x == n - 1:
                break
        else:
            return False
    return True


def derived_40_bit_prime(index: int, side: str, attempt: int) -> int:
    material = f"{SEED}|case={index}|side={side}|attempt={attempt}".encode()
    raw = int.from_bytes(hashlib.sha256(material).digest()[:8], "big")
    candidate = (1 << 39) | (raw & ((1 << 39) - 1)) | 1
    while candidate < (1 << 40):
        if deterministic_is_prime(candidate):
            return candidate
        candidate += 2
    raise RuntimeError("deterministic prime scan crossed 40-bit boundary")


def deterministic_corpus() -> list[dict[str, int]]:
    result: list[dict[str, int]] = []
    for index in range(CASE_COUNT):
        for attempt in range(10_000):
            p = derived_40_bit_prime(index, "p", attempt)
            q = derived_40_bit_prime(index, "q", attempt)
            N = p * q
            if p != q and N.bit_length() == 80:
                result.append({"case": index, "attempt": attempt, "p": p, "q": q, "N": N})
                break
        else:
            raise RuntimeError(f"could not derive exact 80-bit case {index}")
    return result


def primes_through(limit: int) -> list[int]:
    return [n for n in range(2, limit + 1) if deterministic_is_prime(n)]


def legendre(a: int, p: int) -> int:
    a %= p
    if a == 0:
        return 0
    value = pow(a, (p - 1) // 2, p)
    return -1 if value == p - 1 else value


def tonelli_shanks(n: int, p: int) -> int | None:
    n %= p
    if n == 0:
        return 0
    if p == 2:
        return n
    if legendre(n, p) != 1:
        return None
    if p % 4 == 3:
        return pow(n, (p + 1) // 4, p)
    q, s = p - 1, 0
    while q % 2 == 0:
        q //= 2
        s += 1
    z = 2
    while legendre(z, p) != -1:
        z += 1
    c = pow(z, q, p)
    x = pow(n, (q + 1) // 2, p)
    t = pow(n, q, p)
    m = s
    while t != 1:
        i, tt = 1, t * t % p
        while i < m and tt != 1:
            tt = tt * tt % p
            i += 1
        if i == m:
            raise AssertionError("Tonelli-Shanks internal failure")
        b = pow(c, 1 << (m - i - 1), p)
        x = x * b % p
        t = t * b * b % p
        c = b * b % p
        m = i
    return x


def analytic_roots(state: CandidateState, T: int, p: int) -> tuple[list[int], str]:
    A, B, C = state.A % p, state.B % p, state.C % p
    if p == 2:
        if A:
            return [B], "p2_linear_one"
        if B:
            return [], "p2_constant_none"
        return [0, 1], "p2_zero_all"
    if A:
        r = tonelli_shanks(T, p)
        if r is None:
            return [], "quadratic_nonresidue_none"
        inv_A = pow(A, -1, p)
        roots = sorted({((-C + r) * inv_A) % p, ((-C - r) * inv_A) % p})
        return roots, "quadratic_ramified_double" if r == 0 else "quadratic_split_two"
    if C:
        return [(-B * pow(2 * C, -1, p)) % p], "linear_one"
    if B:
        return [], "constant_none"
    return list(range(p)), "zero_polynomial_all"


def brute_roots(state: CandidateState, p: int) -> list[int]:
    return [t for t in range(p) if (state.A * t * t + 2 * state.C * t + state.B) % p == 0]


def factor_signed(value: int) -> dict[int, int]:
    if value == 0:
        raise ValueError("zero has no finite prime-exponent vector")
    factors: Counter[int] = Counter()
    if value < 0:
        factors[-1] = 1
        value = -value
    while value % 2 == 0:
        factors[2] += 1
        value //= 2
    p = 3
    while p * p <= value:
        while value % p == 0:
            factors[p] += 1
            value //= p
        p += 2
    if value > 1:
        factors[value] += 1
    return dict(sorted(factors.items()))


def product_from_factors(factors: dict[int, int]) -> int:
    value = 1
    for p, exponent in factors.items():
        value *= p ** exponent
    return value


def combine_relation_indices(relations: list[dict], indices: Iterable[int], N: int) -> dict:
    exponents: Counter[int] = Counter()
    X = 1
    for index in indices:
        relation = relations[index]
        if relation["witness"] * relation["witness"] % N != relation["value"] % N:
            raise AssertionError("input relation fails its congruence")
        X = X * relation["witness"] % N
        exponents.update(relation["factors"])
    odd = sorted(p for p, exponent in exponents.items() if exponent & 1)
    if odd:
        return {"valid_dependency": False, "odd_factors": odd}
    Y = 1
    for p, exponent in exponents.items():
        if p != -1:
            Y = Y * pow(p, exponent // 2, N) % N
    if X * X % N != Y * Y % N:
        raise AssertionError("even exponent dependency failed square congruence")
    return {
        "valid_dependency": True,
        "X": X,
        "Y": Y,
        "gcd_minus": math.gcd((X - Y) % N, N),
        "gcd_plus": math.gcd((X + Y) % N, N),
    }


def check_orbits(corpus: list[dict], mismatch_rows: list[dict], csv_rows: list[dict]) -> dict:
    digest = hashlib.sha256()
    paired_steps = 0
    map_roundtrips = 0
    reduced_checks = 0
    samples: list[dict] = []
    checkpoints = {0, 1, 2, 3, STEPS_PER_CASE - 1}

    def mismatch(kind: str, case: int, n: int, expected, observed) -> None:
        mismatch_rows.append({"phase": "orbit", "kind": kind, "case": case, "n": n,
                              "expected": expected, "observed": observed})

    for case in corpus:
        T = case["N"]
        candidate = candidate_initial(T)
        reference = reference_initial(T)
        for n in range(STEPS_PER_CASE):
            paired_steps += 1
            q = candidate_digit(T, candidate)
            if invariant(candidate) != T:
                mismatch("invariant", case["case"], n, T, invariant(candidate))
            if q != reference.a:
                mismatch("digit", case["case"], n, reference.a, q)
            if n == 0:
                expected = candidate_initial(T)
            else:
                expected = reference_to_candidate(n, reference)
                reduced_checks += 1
                if not is_repaired_reduced(T, candidate):
                    mismatch("repaired_reduced_domain", case["case"], n, True, False)
                reverse = candidate_to_reference(n, T, candidate)
                if reverse != reference:
                    mismatch("candidate_to_reference", case["case"], n, reference.__dict__, reverse.__dict__)
                if reference_to_candidate(n, reverse) != candidate:
                    mismatch("map_roundtrip", case["case"], n, candidate.__dict__,
                             reference_to_candidate(n, reverse).__dict__)
                map_roundtrips += 1
            if candidate != expected:
                mismatch("reference_to_candidate", case["case"], n, expected.__dict__, candidate.__dict__)

            digest.update((f"{case['case']}|{n}|{T}|{candidate.A}|{candidate.B}|{candidate.C}|{q}|"
                           f"{reference.m}|{reference.d}|{reference.a}|{reference.d_prev}\n").encode())

            if n < 12:
                samples.append({"case": case["case"], "n": n, "T": T, "state": candidate})
            if n in checkpoints:
                csv_rows.append({
                    "record_type": "canonical_map_checkpoint", "case": case["case"], "n": n,
                    "T": T, "A": candidate.A, "B": candidate.B, "C": candidate.C,
                    "candidate_a": q, "m": reference.m, "d": reference.d,
                    "d_prev": "" if reference.d_prev is None else reference.d_prev,
                    "reference_a": reference.a, "condition": "exact indexed map and invariant",
                    "expected": "match", "observed": "match" if candidate == expected and q == reference.a else "mismatch",
                    "status": "PASS" if candidate == expected and q == reference.a else "FAIL",
                })

            candidate = candidate_step(candidate, q)
            reference = reference_step(T, reference)

    return {
        "paired_steps": paired_steps,
        "map_roundtrips": map_roundtrips,
        "reduced_domain_checks": reduced_checks,
        "paired_stream_sha256": digest.hexdigest(),
        "sample_states": samples,
    }


def check_matrix_and_band_relations(mismatch_rows: list[dict]) -> dict:
    checks = 0
    principal_endpoint_checks = 0
    intermediate_parameter_checks = 0
    extrapolated_parameter_checks = 0
    signed_negative_values = 0
    square_values = 0
    multiplier_cases = []

    for N, M in ((77, 1), (77, 3), (77, 5), (77, 9), (77, 25), (91, 1)):
        T = M * N
        if math.isqrt(T) ** 2 == T:
            continue
        state = candidate_initial(T)
        P = (1, 0, 0, 1)
        case_checks = 0
        for n in range(24):
            mapped = form_coefficients_from_matrix(T, P)
            if mapped != state:
                mismatch_rows.append({"phase": "relation", "kind": "matrix_form_coefficients", "N": N,
                                      "M": M, "n": n, "expected": state.__dict__, "observed": mapped.__dict__})
            a = candidate_digit(T, state)
            for t in range(-4, a + 5):
                D = state.A * t * t + 2 * state.C * t + state.B
                x = P[0] * t + P[1]
                y = P[2] * t + P[3]
                w = state.A * t + state.C
                ok_global = D == x * x - T * y * y and (x * x - D) % N == 0
                ok_local = w * w - state.A * D == T and (w * w - state.A * D) % N == 0
                if not (ok_global and ok_local):
                    mismatch_rows.append({"phase": "relation", "kind": "band_identity", "N": N, "M": M,
                                          "n": n, "t": t, "expected": True,
                                          "observed": {"global": ok_global, "local": ok_local}})
                checks += 1
                case_checks += 1
                if 0 <= t <= a:
                    intermediate_parameter_checks += 1
                else:
                    extrapolated_parameter_checks += 1
                if D < 0:
                    signed_negative_values += 1
                if D and math.isqrt(abs(D)) ** 2 == abs(D):
                    square_values += 1
            D_at_a = state.A * a * a + 2 * state.C * a + state.B
            next_state = candidate_step(state, a)
            if D_at_a != next_state.A:
                mismatch_rows.append({"phase": "relation", "kind": "principal_endpoint", "N": N, "M": M,
                                      "n": n, "expected": next_state.A, "observed": D_at_a})
            principal_endpoint_checks += 1
            P = matmul(P, (a, 1, 1, 0))
            state = next_state
        multiplier_cases.append({"N": N, "M": M, "T": T, "checks": case_checks})

    # Multipliers in the same square class have equal characters away from the
    # ramified primes, but their integer form orbits are not identical.
    character_checks = 0
    for p in primes_through(257):
        if p not in (2, 3, 5, 7, 11) and math.gcd(p, 3 * 25 * 77) == 1:
            if legendre(3, p) != legendre(3 * 25, p):
                mismatch_rows.append({"phase": "relation", "kind": "square_multiplier_character", "p": p,
                                      "expected": legendre(3, p), "observed": legendre(75, p)})
            character_checks += 1
    orbit3 = [candidate_initial(3 * 77)]
    orbit75 = [candidate_initial(75 * 77)]
    for states, T in ((orbit3, 3 * 77), (orbit75, 75 * 77)):
        for _ in range(5):
            states.append(candidate_step(states[-1], candidate_digit(T, states[-1])))
    square_class_orbits_distinct = orbit3 != orbit75
    if not square_class_orbits_distinct:
        mismatch_rows.append({"phase": "relation", "kind": "square_class_orbits", "expected": "distinct",
                              "observed": "identical"})

    early_factor = math.gcd(7, 77)
    if early_factor != 7:
        mismatch_rows.append({"phase": "relation", "kind": "multiplier_gcd", "expected": 7,
                              "observed": early_factor})

    return {
        "matrix_and_relation_checks": checks,
        "principal_endpoint_checks": principal_endpoint_checks,
        "intermediate_parameter_checks": intermediate_parameter_checks,
        "extrapolated_parameter_checks": extrapolated_parameter_checks,
        "negative_band_values_seen": signed_negative_values,
        "square_absolute_band_values_seen": square_values,
        "multiplier_cases": multiplier_cases,
        "square_multiplier_character_checks": character_checks,
        "square_class_orbits_distinct": square_class_orbits_distinct,
        "gcd_M_N_early_factor": early_factor,
    }


def check_roots(samples: list[dict], mismatch_rows: list[dict]) -> dict:
    synthetic = [
        {"case": "synthetic_double", "n": 0, "T": 3, "state": CandidateState(1, -3, 0)},
        {"case": "synthetic_linear", "n": 0, "T": 4, "state": CandidateState(3, -1, 1)},
        {"case": "synthetic_constant", "n": 0, "T": 3, "state": CandidateState(3, -1, 0)},
        {"case": "synthetic_zero", "n": 0, "T": 18, "state": CandidateState(3, -3, 3)},
        {"case": "synthetic_p2_none", "n": 0, "T": 3, "state": CandidateState(2, -1, 1)},
        {"case": "synthetic_p2_all", "n": 0, "T": 5, "state": CandidateState(2, -2, 1)},
    ]
    declared = samples + synthetic
    small_primes = primes_through(257)
    large_primes = [1009, 1013, 4099, 65537]
    branch_counts: Counter[str] = Counter()
    exhaustion_cases = 0
    residues_tested = 0
    invalid_root_negative_controls = 0

    def exhaust(sample: dict, p: int) -> None:
        nonlocal exhaustion_cases, residues_tested, invalid_root_negative_controls
        state, T = sample["state"], sample["T"]
        analytic, branch = analytic_roots(state, T, p)
        brute = brute_roots(state, p)
        exhaustion_cases += 1
        residues_tested += p
        branch_counts[branch] += 1
        if analytic != brute:
            mismatch_rows.append({"phase": "roots", "kind": "analytic_vs_brute", "case": sample["case"],
                                  "n": sample["n"], "p": p, "expected": brute, "observed": analytic})
        nonroots = [t for t in range(p) if t not in set(brute)]
        if nonroots:
            t = nonroots[0]
            if (state.A * t * t + 2 * state.C * t + state.B) % p == 0:
                mismatch_rows.append({"phase": "roots", "kind": "invalid_root_control", "p": p,
                                      "expected": "reject", "observed": "accepted"})
            else:
                invalid_root_negative_controls += 1

    for sample in declared:
        for p in small_primes:
            exhaust(sample, p)
    for sample in declared[:12] + synthetic:
        for p in large_primes:
            exhaust(sample, p)

    required = {
        "p2_linear_one", "p2_constant_none", "p2_zero_all", "quadratic_nonresidue_none",
        "quadratic_ramified_double", "quadratic_split_two", "linear_one", "constant_none",
        "zero_polynomial_all",
    }
    missing = sorted(required - set(branch_counts))
    if missing:
        mismatch_rows.append({"phase": "roots", "kind": "root_branch_coverage", "expected": sorted(required),
                              "observed_missing": missing})

    # Exhaust p^2 and verify the exact unique-lift statement only at simple roots.
    hensel_simple_roots = 0
    hensel_unique_lifts = 0
    ramified_lift_profiles: Counter[str] = Counter()
    for sample in declared[:8] + synthetic:
        state = sample["state"]
        for p in (2, 3, 5, 7, 11, 13):
            roots_p = brute_roots(state, p)
            roots_p2 = brute_roots(state, p * p)
            for r in roots_p:
                derivative = (2 * state.A * r + 2 * state.C) % p
                lifts = [x for x in roots_p2 if x % p == r]
                if derivative:
                    hensel_simple_roots += 1
                    if len(lifts) == 1:
                        hensel_unique_lifts += 1
                    else:
                        mismatch_rows.append({"phase": "roots", "kind": "simple_hensel_lift", "p": p,
                                              "r": r, "expected": 1, "observed": len(lifts)})
                else:
                    ramified_lift_profiles[str(len(lifts))] += 1

    return {
        "root_exhaustion_cases": exhaustion_cases,
        "root_residues_tested": residues_tested,
        "root_branch_counts": dict(sorted(branch_counts.items())),
        "invalid_root_negative_controls": invalid_root_negative_controls,
        "hensel_simple_roots": hensel_simple_roots,
        "hensel_unique_lifts": hensel_unique_lifts,
        "ramified_lift_profiles": dict(sorted(ramified_lift_profiles.items())),
    }


def build_band_relation(N: int, T: int, state: CandidateState, t: int) -> dict:
    D = state.A * t * t + 2 * state.C * t + state.B
    value = state.A * D
    witness = state.A * t + state.C
    if witness * witness - value != T:
        raise AssertionError("local band identity failed")
    if value == 0:
        raise ValueError("zero relation excluded")
    return {"N": N, "T": T, "state": state, "t": t, "witness": witness,
            "value": value, "factors": factor_signed(value)}


def gf2_dependencies(relations: list[dict], limit: int = 256) -> list[list[int]]:
    universe = sorted({p for relation in relations for p, e in relation["factors"].items() if e & 1})
    positions = {p: i for i, p in enumerate(universe)}
    basis: dict[int, tuple[int, int]] = {}
    dependencies: list[list[int]] = []
    for index, relation in enumerate(relations):
        vector = 0
        for p, exponent in relation["factors"].items():
            if exponent & 1:
                vector ^= 1 << positions[p]
        combo = 1 << index
        while vector:
            pivot = vector.bit_length() - 1
            if pivot not in basis:
                basis[pivot] = (vector, combo)
                break
            vector ^= basis[pivot][0]
            combo ^= basis[pivot][1]
        if vector == 0:
            dependencies.append([i for i in range(index + 1) if combo >> i & 1])
            if len(dependencies) >= limit:
                break
    return dependencies


def check_relation_assembly(mismatch_rows: list[dict]) -> dict:
    relations: list[dict] = []
    for N in (15, 21, 33, 35, 55, 77, 91, 143):
        T = N
        state = candidate_initial(T)
        for _ in range(18):
            a = candidate_digit(T, state)
            for t in range(-8, 9):
                try:
                    relation = build_band_relation(N, T, state, t)
                except ValueError:
                    continue
                # Keep the arithmetic bounded and the relation set deterministic.
                if abs(relation["value"]) <= 2_000_000:
                    relations.append(relation)
            state = candidate_step(state, a)

    dependencies = gf2_dependencies(relations)
    verified_dependencies = 0
    nontrivial_factor_dependencies = 0
    for indices in dependencies:
        N = relations[indices[0]]["N"]
        if any(relations[i]["N"] != N for i in indices):
            # The global GF(2) finder can algebraically combine different N;
            # those rows are deliberately not meaningful as one congruence.
            continue
        result = combine_relation_indices(relations, indices, N)
        if not result["valid_dependency"]:
            mismatch_rows.append({"phase": "assembly", "kind": "gf2_dependency", "expected": "even",
                                  "observed": result})
            continue
        verified_dependencies += 1
        if any(1 < result[key] < N for key in ("gcd_minus", "gcd_plus")):
            nontrivial_factor_dependencies += 1

    # Explicit signed, square-factor, single-large-prime, and double-large-prime
    # relations, all obtained from the actual initialization band D(t)=t^2-N.
    init5 = candidate_initial(5)
    signed = build_band_relation(5, 5, init5, 2)       # value -1
    square = build_band_relation(5, 5, init5, 3)       # value 4 = 2^2
    single_a = build_band_relation(5, 5, init5, 6)     # value 31
    single_b = build_band_relation(5, 5, init5, -6)    # same large prime
    double_a = build_band_relation(5, 5, init5, 28)    # 779 = 19*41
    double_b = build_band_relation(5, 5, init5, -28)   # parallel-edge 2-cycle

    signed_result = combine_relation_indices([signed], [0], 5)
    if signed_result["valid_dependency"] or signed_result.get("odd_factors") != [-1]:
        mismatch_rows.append({"phase": "assembly", "kind": "signed_factor", "expected": [-1],
                              "observed": signed_result})
    square_result = combine_relation_indices([square], [0], 5)
    single_result = combine_relation_indices([single_a, single_b], [0, 1], 5)
    double_result = combine_relation_indices([double_a, double_b], [0, 1], 5)
    for name, result in (("square_factor", square_result), ("single_large_prime_pair", single_result),
                         ("double_large_prime_cycle", double_result)):
        if not result["valid_dependency"]:
            mismatch_rows.append({"phase": "assembly", "kind": name, "expected": "valid dependency",
                                  "observed": result})

    # Two independent negative controls: mutate the witness and drop A from the
    # state-only congruence.  Each must be rejected for a deterministically found row.
    chosen = next(r for r in relations if (r["witness"] + 1) ** 2 % r["N"] != r["value"] % r["N"])
    mutated_witness_rejected = (chosen["witness"] + 1) ** 2 % chosen["N"] != chosen["value"] % chosen["N"]
    mutated_value_rejected = chosen["witness"] ** 2 % chosen["N"] != (chosen["value"] + 1) % chosen["N"]
    dropped_A = next(r for r in relations if r["witness"] ** 2 % r["N"] !=
                     (r["value"] // r["state"].A) % r["N"])
    dropped_A_rejected = dropped_A["witness"] ** 2 % dropped_A["N"] != (
        dropped_A["value"] // dropped_A["state"].A) % dropped_A["N"]
    if not (mutated_witness_rejected and mutated_value_rejected and dropped_A_rejected):
        mismatch_rows.append({"phase": "assembly", "kind": "relation_negative_control",
                              "expected": True, "observed": False})

    return {
        "band_relations_fully_factored": len(relations),
        "gf2_dependencies_found": len(dependencies),
        "same_modulus_dependencies_verified": verified_dependencies,
        "nontrivial_factor_dependencies": nontrivial_factor_dependencies,
        "signed_minus_one_rejected_if_sign_omitted": not signed_result["valid_dependency"],
        "square_factor_dependency_verified": square_result["valid_dependency"],
        "single_large_prime_pair_verified": single_result["valid_dependency"],
        "double_large_prime_parallel_edge_cycle_verified": double_result["valid_dependency"],
        "mutated_witness_rejected": mutated_witness_rejected,
        "mutated_value_rejected": mutated_value_rejected,
        "dropped_A_relation_rejected": dropped_A_rejected,
    }


SIGN_VARIANTS = {
    "flip_Aa2": (-1, 1, 1, 1, 1, 1),
    "flip_2Ca": (1, -1, 1, 1, 1, 1),
    "flip_B_term": (1, 1, -1, 1, 1, 1),
    "flip_Bprime": (1, 1, 1, -1, 1, 1),
    "flip_Aa_in_Cprime": (1, 1, 1, 1, -1, 1),
    "flip_C_in_Cprime": (1, 1, 1, 1, 1, -1),
}


def perturbed_step(state: CandidateState, a: int, signs: tuple[int, ...]) -> CandidateState:
    s1, s2, s3, s4, s5, s6 = signs
    A, B, C = state.A, state.B, state.C
    return CandidateState(s1 * A * a * a + s2 * 2 * C * a + s3 * B, s4 * A,
                          s5 * A * a + s6 * C)


def check_negative_controls(csv_rows: list[dict], mismatch_rows: list[dict]) -> dict:
    failures: dict[str, dict] = {}
    odd_nonsquares = [T for T in range(3, 500, 2) if math.isqrt(T) ** 2 != T]
    for name, signs in SIGN_VARIANTS.items():
        found = None
        for T in odd_nonsquares:
            state = candidate_initial(T)
            reference = reference_initial(T)
            for n in range(32):
                a = candidate_digit(T, state)
                expected = candidate_step(state, a)
                observed = perturbed_step(state, a, signs)
                if observed != expected or invariant(observed) != T:
                    found = {"T": T, "n": n, "state": state.__dict__, "a": a,
                             "expected": expected.__dict__, "observed": observed.__dict__,
                             "observed_invariant": invariant(observed)}
                    break
                state = expected
                reference = reference_step(T, reference)
            if found:
                break
        if not found:
            mismatch_rows.append({"phase": "negative", "kind": name, "expected": "rejected",
                                  "observed": "not detected"})
            continue
        failures[name] = found
        csv_rows.append({
            "record_type": "sign_negative_control", "case": name, "n": found["n"], "T": found["T"],
            "A": found["state"]["A"], "B": found["state"]["B"], "C": found["state"]["C"],
            "candidate_a": found["a"], "m": "", "d": "", "d_prev": "", "reference_a": found["a"],
            "condition": name, "expected": json.dumps(found["expected"], sort_keys=True),
            "observed": json.dumps(found["observed"], sort_keys=True), "status": "REJECTED_AS_REQUIRED",
        })

    # Wrong quotient direction, and the smallest weak-domain orientation failure.
    T = 3
    state = candidate_step(candidate_initial(T), candidate_digit(T, candidate_initial(T)))
    correct = candidate_digit(T, state)
    wrong = (math.isqrt(T) - abs(state.C)) // abs(state.A)
    wrong_direction_rejected = wrong != correct and candidate_step(state, wrong) != candidate_step(state, correct)
    if not wrong_direction_rejected:
        mismatch_rows.append({"phase": "negative", "kind": "wrong_quotient_direction",
                              "expected": "rejected", "observed": "not detected"})
    csv_rows.append({
        "record_type": "quotient_direction_negative_control", "case": "smallest", "n": 1, "T": 3,
        "A": state.A, "B": state.B, "C": state.C, "candidate_a": correct, "m": abs(state.C),
        "d": abs(state.A), "d_prev": abs(state.B), "reference_a": correct,
        "condition": "replace s+|C| by s-|C|", "expected": correct, "observed": wrong,
        "status": "REJECTED_AS_REQUIRED",
    })

    weak = CandidateState(-2, 1, -1)
    weak_a = candidate_digit(3, weak)
    weak_next = candidate_step(weak, weak_a)
    weak_domain_counterexample = (
        invariant(weak) == 3 and weak.A * weak.B < 0 and abs(weak.C) < math.sqrt(3)
        and weak.A * weak.C > 0 and not is_repaired_reduced(3, weak)
        and not (weak_next.A * weak_next.B < 0 and abs(weak_next.C) < math.sqrt(3))
    )
    if not weak_domain_counterexample:
        mismatch_rows.append({"phase": "negative", "kind": "weak_domain_counterexample",
                              "expected": True, "observed": False})
    csv_rows.append({
        "record_type": "weak_domain_counterexample", "case": "smallest_odd_nonsquare", "n": 0, "T": 3,
        "A": weak.A, "B": weak.B, "C": weak.C, "candidate_a": weak_a, "m": "", "d": "",
        "d_prev": "", "reference_a": "", "condition": "AB<0, |C|<sqrt(T), but AC>0",
        "expected": "packet weak domain should stay in reduced orbit",
        "observed": json.dumps(weak_next.__dict__, sort_keys=True), "status": "COUNTEREXAMPLE_CONFIRMED",
    })

    oriented = CandidateState(-2, 1, 1)
    negated = CandidateState(2, -1, -1)
    orientation_quotient = candidate_digit(3, oriented)
    global_sign_cover_commutes = (
        candidate_digit(3, negated) == orientation_quotient
        and candidate_step(negated, orientation_quotient) == CandidateState(
            -candidate_step(oriented, orientation_quotient).A,
            -candidate_step(oriented, orientation_quotient).B,
            -candidate_step(oriented, orientation_quotient).C,
        )
    )
    if not global_sign_cover_commutes:
        mismatch_rows.append({"phase": "negative", "kind": "global_sign_cover", "expected": True,
                              "observed": False})
    csv_rows.append({
        "record_type": "global_sign_double_cover", "case": "T=3_oriented_pair", "n": 1, "T": 3,
        "A": oriented.A, "B": oriented.B, "C": oriented.C, "candidate_a": orientation_quotient,
        "m": 1, "d": 2, "d_prev": 1, "reference_a": 1,
        "condition": "V and -V have the same digit; transition commutes with negation",
        "expected": "same quotient orbit", "observed": "commutes",
        "status": "PASS" if global_sign_cover_commutes else "FAIL",
    })

    # T=5 has the symmetric reduced state V=(1,-1,-2), a=4.  One step gives
    # -V, so it is fixed only after quotienting by global sign; it is not a
    # zero or terminal state.
    symmetric = CandidateState(1, -1, -2)
    symmetric_a = candidate_digit(5, symmetric)
    symmetric_next = candidate_step(symmetric, symmetric_a)
    ambiguous_sign_fixed_nonterminal = (
        invariant(symmetric) == 5 and is_repaired_reduced(5, symmetric)
        and symmetric_a == 4 and symmetric_next == CandidateState(-1, 1, 2)
        and invariant(symmetric_next) == 5
    )
    if not ambiguous_sign_fixed_nonterminal:
        mismatch_rows.append({"phase": "negative", "kind": "ambiguous_sign_fixed_state",
                              "expected": True, "observed": False})
    csv_rows.append({
        "record_type": "ambiguous_sign_fixed_nonterminal", "case": "T=5_period_one_mod_sign", "n": 1,
        "T": 5, "A": symmetric.A, "B": symmetric.B, "C": symmetric.C,
        "candidate_a": symmetric_a, "m": 2, "d": 1, "d_prev": 1, "reference_a": 4,
        "condition": "V'=-V; fixed only modulo global sign",
        "expected": "nonterminal reduced cycle", "observed": json.dumps(symmetric_next.__dict__, sort_keys=True),
        "status": "PASS",
    })

    square_terminal_detected = False
    try:
        reference_step(9, reference_initial(9))
    except (AssertionError, ZeroDivisionError):
        square_terminal_detected = True
    if not square_terminal_detected:
        mismatch_rows.append({"phase": "negative", "kind": "square_T_terminal", "expected": True,
                              "observed": False})
    csv_rows.append({
        "record_type": "square_input_exception", "case": "T=9", "n": 0, "T": 9,
        "A": 1, "B": -9, "C": 0, "candidate_a": 3, "m": 0, "d": 1, "d_prev": "",
        "reference_a": 3, "condition": "d1=T-floor(sqrt(T))^2=0",
        "expected": "excluded square input", "observed": "zero denominator detected",
        "status": "PASS" if square_terminal_detected else "FAIL",
    })

    return {
        "recurrence_sign_variants_rejected": len(failures),
        "recurrence_sign_failures": failures,
        "wrong_quotient_direction_rejected": wrong_direction_rejected,
        "weak_domain_smallest_counterexample_confirmed": weak_domain_counterexample,
        "global_sign_double_cover_commutes": global_sign_cover_commutes,
        "ambiguous_sign_fixed_state_nonterminal": ambiguous_sign_fixed_nonterminal,
        "square_T_terminal_detected": square_terminal_detected,
    }


def write_csv(rows: list[dict]) -> None:
    fields = ["record_type", "case", "n", "T", "A", "B", "C", "candidate_a", "m", "d", "d_prev",
              "reference_a", "condition", "expected", "observed", "status"]
    CSV_PATH.parent.mkdir(parents=True, exist_ok=True)
    with CSV_PATH.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, extrasaction="ignore", lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def write_json(path: Path, value: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def write_mismatches(rows: list[dict]) -> None:
    MISMATCH_PATH.parent.mkdir(parents=True, exist_ok=True)
    with MISMATCH_PATH.open("w", encoding="utf-8", newline="\n") as handle:
        handle.write(json.dumps({"record_type": "mismatch_summary", "count": len(rows)}, sort_keys=True) + "\n")
        for row in rows:
            handle.write(json.dumps(row, sort_keys=True, default=str) + "\n")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--quick", action="store_true", help="use 2 cases x 100 steps for local debugging")
    args = parser.parse_args()
    global CASE_COUNT, STEPS_PER_CASE
    if args.quick:
        CASE_COUNT, STEPS_PER_CASE = 2, 100

    mismatches: list[dict] = []
    csv_rows: list[dict] = []
    corpus = deterministic_corpus()
    orbit = check_orbits(corpus, mismatches, csv_rows)
    roots = check_roots(orbit.pop("sample_states"), mismatches)
    band = check_matrix_and_band_relations(mismatches)
    assembly = check_relation_assembly(mismatches)
    negative = check_negative_controls(csv_rows, mismatches)

    summary = {
        "schema": "enterprise_math.valley_band_checker_summary.v1",
        "researcher_id": RESEARCHER_ID,
        "task_id": TASK_ID,
        "validation_status": "PASS" if not mismatches else "FAIL",
        "corpus_rule": {
            "seed": SEED,
            "construction": "SHA-256-derived 40-bit odd start; upward deterministic prime scan; retry until p!=q and bit_length(p*q)=80",
            "case_count": len(corpus),
            "steps_per_case": STEPS_PER_CASE,
            "cases": corpus,
        },
        "orbit": orbit,
        "roots": roots,
        "band_and_multiplier_relations": band,
        "relation_assembly": assembly,
        "negative_controls": negative,
        "mismatch_count": len(mismatches),
        "mismatch_log": str(MISMATCH_PATH),
    }
    write_csv(csv_rows)
    write_mismatches(mismatches)
    write_json(SUMMARY_PATH, summary)
    print(json.dumps(summary, indent=2, sort_keys=True))
    return 0 if not mismatches else 1


if __name__ == "__main__":
    raise SystemExit(main())
