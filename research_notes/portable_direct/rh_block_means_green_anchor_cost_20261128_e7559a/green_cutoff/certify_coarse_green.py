#!/usr/bin/env python3
"""Exact finite verification of the round-9 original Green cutoff theorem.

No numerical quadrature, floating-point comparison, random input, or third-party
dependency is used.  The analytic proof handles arbitrary intervals and sources;
these checks verify its discrete implementation and finite boundary examples.
"""

from __future__ import annotations

import argparse
from collections import Counter
from fractions import Fraction as Q
import hashlib
import json
from pathlib import Path


BASE = Path(__file__).resolve().parent
INPUT = BASE / "coarse_green_inputs.json"
PROOF = BASE / "COARSE_BLOCK_MEANS_TO_ORIGINAL_GREEN.md"
CERT = BASE / "coarse_green_certificate.json"


def require(condition, message):
    if not condition:
        raise AssertionError(message)


def sha256(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def pos(value):
    return max(Q(0), value)


def dyadics_below(value):
    d = 1
    while d < value:
        yield d
        d *= 2


def green(L, R, n, m):
    return Q((min(n, m) - L) * (R - max(n, m)), R - L)


def kernel(L, R, n, m):
    return green(L, R, n, m) / m


def interpolate(xs, values, t):
    if t == xs[-1]:
        return values[-1]
    for a, b, va, vb in zip(xs[:-1], xs[1:], values[:-1], values[1:]):
        if a <= t <= b:
            return (va * (b - t) + vb * (t - a)) / (b - a)
    raise AssertionError("point outside interpolation interval")


def antitone_fit(values):
    # A pool stores its exact sum, its cardinality, and its first index.
    pools = []
    for i, value in enumerate(values):
        pools.append([value, 1, i])
        while len(pools) >= 2:
            left, right = pools[-2:]
            if left[0] / left[1] >= right[0] / right[1]:
                break
            pools[-2:] = [[left[0] + right[0], left[1] + right[1], left[2]]]
    fitted = [Q(0)] * len(values)
    for total, size, start in pools:
        fitted[start:start + size] = [total / size] * size
    residual = [a - b for a, b in zip(values, fitted)]
    require(all(a >= b for a, b in zip(fitted[:-1], fitted[1:])), "PAV direction")
    require(sum(residual, Q(0)) == 0, "PAV total residual")
    prefix = Q(0)
    for value in residual:
        prefix += value
        require(prefix <= 0, "PAV polar cone prefix")
    require(sum((a * b for a, b in zip(residual, fitted)), Q(0)) == 0,
            "PAV complementarity")
    return fitted, sum((v * v for v in residual), Q(0))


def two_root_bound(square_energy, A, B):
    # Equivalent to sqrt(square_energy) <= sqrt(A) + sqrt(B), with no roots.
    require(A >= 0 and B >= 0 and square_energy >= 0, "nonnegative energy inputs")
    if square_energy <= A + B:
        return True
    return (square_energy - A - B) ** 2 <= 4 * A * B


def source_values(family, L, R, r, config):
    h = R - L
    values = {}
    for m in range(L + 1, R):
        if family == "all_one":
            b = Q(1)
        elif family == "all_minus_one":
            b = Q(-1)
        elif family == "rational_wave":
            b = 1 - Q((17 * m + 3 * L + 5 * h + r) % 13, 4)
        elif family == "deep_negative":
            b = (Q(-(config["deep_negative_magnitude"] + L * h + r), 7)
                 if m == L + max(1, h // 2) else Q(1))
        elif family == "hidden_grid":
            b = Q(1 - r if (m - L) % r == 0 else 1)
        elif family == "localized_positive":
            b = Q(1 if (m - L) * 3 <= h else -2)
        else:
            raise AssertionError("unknown fixed source family")
        require(b <= 1, "one-sided source bound")
        values[m] = b
    return values


def meshes(L, R, families):
    result = []
    seen = set()
    for name in families:
        if name == "full_integer":
            nodes = list(range(L, R + 1))
        elif name == "endpoints_only":
            nodes = [L, R]
        elif name == "residue_one_mod_three":
            nodes = sorted({L, R} | {n for n in range(L + 1, R) if (n - L) % 3 == 1})
        elif name == "one_offcenter_node":
            nodes = sorted({L, R, L + (R - L + 2) // 3})
        else:
            raise AssertionError("unknown fixed mesh family")
        key = tuple(nodes)
        if key not in seen:
            result.append((name, nodes))
            seen.add(key)
    return result


def build_certificate():
    config = json.loads(INPUT.read_text())
    counts = Counter()
    max_rho_ratio = Q(0)
    max_rho_witness = None
    sharpness_examples = []
    min_source = Q(1)
    all_case_digest = hashlib.sha256()

    for L in config["L_values"]:
        h_values = {h for h in config["h_candidates"] if h <= L}
        if config["include_h_equals_L"]:
            h_values.add(L)
        for h in sorted(h_values):
            R = L + h
            for r in [r for r in range(1, h + 1) if h % r == 0]:
                M = h // r
                xs = list(range(L, R + 1, r))
                counts["geometries"] += 1
                rows = {}
                for n in range(L + 1, R):
                    E = Q(R * (n - L) * r * r, h * n ** 3)
                    K = {m: kernel(L, R, n, m) for m in range(L, R + 1)}
                    original_nodes = [K[x] for x in xs]
                    sigma = [pos(K[x] - E) for x in xs]
                    require(sigma[0] == sigma[-1] == 0, "zero coarse endpoints")
                    rho = Q(0)
                    signed_interpolation_loss = Q(0)
                    clip_loss = Q(0)
                    Khat = {}
                    for m in range(L + 1, R):
                        khat = interpolate(xs, sigma, Q(m))
                        original_linear = interpolate(xs, original_nodes, Q(m))
                        require(0 <= khat <= K[m], "integer kernel minorant")
                        Khat[m] = khat
                        rho += K[m] - khat
                        signed_interpolation_loss += K[m] - original_linear
                        clip_loss += original_linear - khat
                        counts["integer_kernel_checks"] += 1

                    subdivisions = config["probe_subdivision"]
                    for p in range(h * subdivisions + 1):
                        t = Q(L) + Q(p, subdivisions)
                        kt = kernel(L, R, n, t)
                        khat = interpolate(xs, sigma, t)
                        require(0 <= khat <= kt, "rational-point kernel minorant")
                        counts["rational_kernel_probes"] += 1

                    require(rho == signed_interpolation_loss + clip_loss, "loss decomposition")
                    require(signed_interpolation_loss <= Q(5 * r * r, 32 * L),
                            "negative variation interpolation payment")
                    require(0 <= clip_loss <= (h - 1) * E, "clipping payment")
                    require((h - 1) * E <= Q(8 * r * r, 27 * L), "clipping uniform bound")
                    require(0 <= rho <= Q(391 * r * r, 864 * L), "rho strong constant")
                    require(rho <= Q(r * r, 2 * L), "rho clean constant")
                    ratio = rho / Q(r * r, L)
                    if ratio > max_rho_ratio:
                        max_rho_ratio, max_rho_witness = ratio, [L, R, r, n]

                    left_derivative_constant = Q((R - n) * L, h)
                    right_derivative_constant = Q((n - L) * R, h)
                    derivative_energy = (
                        left_derivative_constant ** 2 * Q(1, 3)
                        * (Q(1, L ** 3) - Q(1, n ** 3))
                        + right_derivative_constant ** 2 * Q(1, 3)
                        * (Q(1, n ** 3) - Q(1, R ** 3))
                    )
                    gradient = sum(((b - a) ** 2 for a, b in zip(sigma[:-1], sigma[1:])), Q(0))
                    Gdiag = green(L, R, n, n)
                    require(gradient <= r * derivative_energy, "coarse gradient Cauchy bound")
                    require(derivative_energy <= Gdiag / L ** 2, "weighted Green derivative bound")
                    rows[n] = (K, Khat, sigma, rho, gradient, Gdiag)
                    counts["output_kernel_rows"] += 1

                for family in config["source_families"]:
                    source = source_values(family, L, R, r, config)
                    if source:
                        min_source = min(min_source, min(source.values()))
                    A = [Q(0)]
                    for m in range(L + 1, R):
                        A.append(A[-1] + source[m])
                    require(len(A) == h, "edge cumulative length")
                    w = [sum(A[j * r:(j + 1) * r], Q(0)) / r for j in range(M)]
                    for j in range(1, M):
                        hat_sum = Q(0)
                        for m in range(xs[j - 1] + 1, xs[j + 1]):
                            phi = Q(min(m - xs[j - 1], xs[j + 1] - m), r)
                            hat_sum += phi * source[m]
                        require(hat_sum == w[j] - w[j - 1], "exact block-mean hat identity")
                        counts["block_mean_hat_identities"] += 1

                    fitted, D = antitone_fit(w)
                    Jw = {}
                    for d in dyadics_below(M):
                        Jw[d] = sum((pos(w[i + d] - w[i]) ** 2 for i in range(M - d)), Q(0))
                        Jb = sum((pos(A[u + r * d] - A[u]) ** 2 for u in range(h - r * d)), Q(0))
                        require(Jw[d] <= Jb / r, "Jensen C-to-K direction")
                        counts["jensen_length_checks"] += 1
                    require(2 * D <= sum(Jw.values(), Q(0)), "round8 directed dyadic cone bound")
                    counts["cone_distance_checks"] += 1

                    U = {L: Q(0), R: Q(0)}
                    for n in range(L + 1, R):
                        K, Khat, sigma, rho, gradient, Gdiag = rows[n]
                        U[n] = sum((K[m] * source[m] for m in source), Q(0))
                        coarse = sum((sigma[j] * (w[j] - w[j - 1]) for j in range(1, M)), Q(0))
                        residual = sum(((K[m] - Khat[m]) * source[m] for m in source), Q(0))
                        require(U[n] == coarse + residual, "signed source equality")
                        require(U[n] <= coarse + rho, "one-sided source transfer")
                        require(pos(coarse) ** 2 <= D * gradient, "cone pairing bound")
                        require(pos(U[n] - rho) ** 2 <= D * gradient, "actual point local payment")
                        require(pos(U[n] - Q(r * r, 2 * L)) ** 2 <= D * r * Gdiag / L ** 2,
                                "actual point uniform payment")
                        counts["source_point_checks"] += 1

                    coefficient_D = Q(r * (h * h - 1), 6 * L ** 4)
                    fine_square = Q(r ** 4 * (h - 1), 4 * L ** 4)
                    C = None
                    if L == h and M & (M - 1) == 0:
                        C = max((value / (L * d) for d, value in Jw.items()), default=Q(0))
                        coefficient_C = Q(1, 12) * (1 - Q(r, L)) * (1 - Q(1, L * L))

                    source_energies = {}
                    for mesh_name, nodes in meshes(L, R, config["mesh_families"]):
                        V = {n: interpolate(nodes, [U[x] for x in nodes], Q(n))
                             for n in range(L, R + 1)}
                        require(V[L] == V[R] == 0, "real interpolation endpoints")
                        for n in range(L + 1, R):
                            require(pos(V[n] - Q(r * r, 2 * L)) ** 2
                                    <= D * r * green(L, R, n, n) / L ** 2,
                                    "arbitrary-mesh point bound")
                            counts["interpolated_point_checks"] += 1
                        energy = sum((pos(V[n]) ** 2 / n ** 2 for n in range(L, R + 1)), Q(0))
                        require(two_root_bound(energy, coefficient_D * D, fine_square),
                                "original weighted energy theorem")
                        require(two_root_bound(energy, coefficient_D * sum(Jw.values(), Q(0)) / 2,
                                               fine_square), "dyadic form of energy theorem")
                        if C is not None:
                            require(two_root_bound(energy, coefficient_C * C, fine_square),
                                    "normalized C statistic transfer")
                            counts["normalized_C_energy_checks"] += 1
                        source_energies[mesh_name] = energy
                        counts["mesh_energy_checks"] += 1

                    if family == "hidden_grid":
                        require(all(value == Q(r - 1, 2) for value in w), "constant hidden block means")
                        require(D == 0 and all(value == 0 for value in Jw.values()), "zero hidden statistic")
                        require(all(U[x] >= 0 for x in xs), "nonnegative hidden coarse nodes")
                        for a in xs[:-1]:
                            for t in range(1, r):
                                require(U[a + t] >= Q(t * (r - t), 2 * R), "hidden local bubble lower bound")
                                counts["sharpness_bubble_checks"] += 1
                        lower = Q(h * (r ** 4 - 1), 120 * R ** 4)
                        actual = source_energies["full_integer"]
                        require(actual >= lower, "same-class sharpness energy lower bound")
                        counts["sharpness_examples"] += 1
                        if L == h and L in [8, 16, 32] and r in [2, 4, 8]:
                            sharpness_examples.append({"L": L, "R": R, "r": r,
                                                       "block_mean": str(w[0]),
                                                       "C": "0", "energy_exact": str(actual),
                                                       "energy_lower_bound": str(lower)})

                    counts["source_cases"] += 1
                    all_case_digest.update(
                        json.dumps([L, R, r, family, [str(t) for t in w], str(D),
                                    {k: str(v) for k, v in source_energies.items()}],
                                   sort_keys=True, separators=(",", ":")).encode()
                    )

    return {
        "schema": "coarse_block_means_original_green_certificate_v1",
        "status": "PASS",
        "arithmetic": "exact fractions.Fraction; no floating point or square roots",
        "claim_scope": "finite author checks; analytic proof establishes unbounded theorem",
        "not_independent_review": True,
        "files": {"input_sha256": sha256(INPUT), "script_sha256": sha256(Path(__file__)),
                  "proof_sha256": sha256(PROOF)},
        "counts": dict(sorted(counts.items())),
        "case_output_sha256": all_case_digest.hexdigest(),
        "smallest_tested_source": str(min_source),
        "largest_exact_rho_ratio_to_r_squared_over_L": str(max_rho_ratio),
        "largest_rho_ratio_witness_L_R_r_n": max_rho_witness,
        "proved_uniform_rho_ratio": "391/864 < 1/2",
        "selected_exact_zero_statistic_examples": sharpness_examples,
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="recompute and compare saved certificate")
    args = parser.parse_args()
    certificate = build_certificate()
    if args.check:
        require(CERT.exists(), "saved certificate missing")
        require(json.loads(CERT.read_text()) == certificate, "certificate replay mismatch")
    else:
        CERT.write_text(json.dumps(certificate, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps({"status": "PASS", "mode": "check" if args.check else "write",
                      "counts": certificate["counts"],
                      "case_output_sha256": certificate["case_output_sha256"]},
                     ensure_ascii=False, sort_keys=True))


if __name__ == "__main__":
    main()
