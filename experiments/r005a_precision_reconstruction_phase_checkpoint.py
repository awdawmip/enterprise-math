#!/usr/bin/env python3
"""R005-A consolidated precision / reconstruction / desert-phase checkpoint.

This script consolidates three new theorem families:

1. T-A38/T-A39 — lattice-constrained cofactor reconstruction;
2. T-A40 — reconstruction-depth phase boundary;
3. T-A41/T-A42/T-A43 — synchronized prime-desert phase capacity.

It imports the already-published p=2 ambient closure exact verifier for the
finite residual/ambient cross-check.
"""

from __future__ import annotations

import importlib.util
from fractions import Fraction
from pathlib import Path
import json

HERE = Path(__file__).resolve().parent


def load(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


ambient = load("ambient", HERE / "r005a_p2_ambient_shadow_complex.py")
family = ambient.family


def residue_closure(U: int, d: int, m: int, a: int) -> int:
    q = U // d
    a %= m
    return q - ((q - a) % m)


def check_lattice_reconstruction() -> int:
    checks = 0
    for A in range(0, 80):
        for U in range(A + 1, 100):
            W = U - A
            for d in range(1, 50):
                for m in range(1, 8):
                    if d * m < W:
                        continue
                    for a in range(m):
                        vals = [
                            c for c in range(U // d + 1)
                            if c % m == a and A < d * c <= U
                        ]
                        assert len(vals) <= 1
                        C = residue_closure(U, d, m, a)
                        pred = [C] if C >= 0 and A < d * C <= U else []
                        assert vals == pred
                        checks += 1
    return checks


def reconstruction_status(p: int, r: int) -> str:
    lhs = Fraction(r - 2, r)
    rhs = Fraction(p - 1, p)
    if lhs > rhs:
        return "asymptotically_forced_by_scale"
    if lhs < rhs:
        return "not_forced_by_scale"
    if p == 2:
        return "critical_equality_square_exception"
    return "critical_equality_constant_fails"


def check_reconstruction_phase() -> dict:
    for p in range(2, 9):
        for r in range(3, 30):
            status = reconstruction_status(p, r)
            if r > 2 * p:
                assert status == "asymptotically_forced_by_scale"
            elif r < 2 * p:
                assert status == "not_forced_by_scale"
            elif p == 2:
                assert status == "critical_equality_square_exception"
            else:
                assert status == "critical_equality_constant_fails"

    return {
        "generic_boundary": "r>2p",
        "critical_square_exception": "(p,r)=(2,4)",
        "p3_r6": reconstruction_status(3, 6),
        "p3_r7": reconstruction_status(3, 7),
    }


def previous_prime(n: int) -> int:
    x = n - 1
    if x == 2:
        return 2
    if x % 2 == 0:
        x -= 1
    while x >= 2:
        if family.is_prime(x):
            return x
        x -= 2
    raise RuntimeError


def next_prime(n: int) -> int:
    x = n + 1
    if x <= 2:
        return 2
    if x % 2 == 0:
        x += 1
    while not family.is_prime(x):
        x += 2
    return x


def phase_capacity(k: int, support: tuple[int, ...], N: int) -> dict:
    A = k * k
    W = 2 * k
    h = N - A
    left = []
    right = []

    for q in support:
        M = N // q
        left.append((q * (M - previous_prime(M)), q))
        right.append((q * (next_prime(M) - M), q))

    Lstar, qL = min(left)
    Rstar, qR = min(right)
    mu = Lstar + Rstar - W
    ell = h + Rstar - W
    u = Lstar - h

    return {
        "h": h,
        "Lstar": Lstar,
        "Rstar": Rstar,
        "mu": mu,
        "ell": ell,
        "u": u,
        "qL": qL,
        "qR": qR,
        "e1_desert": W - Rstar < h <= Lstar,
    }


def check_desert_phase_capacity() -> dict:
    categories = {
        "cube_spike": 0,
        "no_desert_capacity": 0,
        "positive_capacity_phase_miss": 0,
        "residual": 0,
    }
    positive = 0
    same = 0
    different = 0

    basins = sorted({k for k, _, _ in family.CERTIFICATES})
    for k in basins:
        A = k * k
        U = A + 2 * k
        H = ambient.ambient_blocks(k)
        vertices = set().union(*(set(S) for S in H)) if H else set()
        NF = ambient.nonforced_vertices(k, vertices)

        for support, N in H.items():
            cube_absent = all(not (A < q**3 <= U) for q in support)
            C = phase_capacity(k, support, N)

            if not cube_absent:
                categories["cube_spike"] += 1
            elif C["mu"] <= 0:
                categories["no_desert_capacity"] += 1
            else:
                positive += 1
                if not C["e1_desert"]:
                    categories["positive_capacity_phase_miss"] += 1
                else:
                    assert set(support) <= NF
                    assert C["ell"] >= 1
                    assert C["u"] >= 0
                    assert C["ell"] + C["u"] == C["mu"]
                    categories["residual"] += 1
                    if C["qL"] == C["qR"]:
                        same += 1
                    else:
                        different += 1

    assert categories == {
        "cube_spike": 0,
        "no_desert_capacity": 2440,
        "positive_capacity_phase_miss": 7,
        "residual": 50,
    }
    assert positive == 57
    assert same == 30
    assert different == 20

    return {
        "categories": categories,
        "positive_capacity_blocks": positive,
        "same_bottleneck_residuals": same,
        "split_bottleneck_residuals": different,
    }


def main() -> None:
    result = {
        "status": "R005-A PRECISION / RECONSTRUCTION / DESERT-PHASE CHECKPOINT",
        "lattice_reconstruction_checks": check_lattice_reconstruction(),
        "reconstruction_phase": check_reconstruction_phase(),
        "desert_phase_capacity": check_desert_phase_capacity(),
        "theorems": {
            "T-A38": "fixed residue c mod m is unique in A<d*c<=U when d*m>=U-A",
            "T-A39": "square-basin odd divisor product d>=k is state-complete",
            "T-A40": "under r-root forcing, p-power reconstruction scale is t/r>(p-1)/p; maximal residual last-factor boundary r>2p, with exact (2,4) exception",
            "T-A41": "all e=1 deserts compress to W-R*<h<=L*",
            "T-A42": "mu=L*+R*-W is the exact count of compatible integer phases when positive",
            "T-A43": "residual phase slacks ell+u=mu",
        },
    }
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
