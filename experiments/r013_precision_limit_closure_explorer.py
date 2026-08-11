#!/usr/bin/env python3
"""Finite falsification/exploration checks for R013 precision-limit closure.

Researcher-ID: EM-R013-0LCGPL

This file is deliberately a finite oracle, not a proof engine.  The report owns
all infinite/general arguments.  In particular the 2-adic section below checks
finite compatibility only; non-realizability in Z is proved symbolically in
`docs/R013_PRECISION_LIMIT_CLOSURE_REPORT.md`.
"""

from __future__ import annotations

from collections import Counter
import json
import math


def cofinal_defect(n: int) -> int:
    """Defect whose even/odd cofinal presentations have different limit behavior."""
    if n % 2 == 0:
        return 0
    return 0 if n % 4 == 1 else 1


def check_cofinal_presentation_instability(limit: int = 40) -> dict[str, object]:
    evens = [cofinal_defect(n) for n in range(2, limit + 1, 2)]
    odds = [cofinal_defect(n) for n in range(1, limit + 1, 2)]
    assert set(evens) == {0}
    assert set(odds) == {0, 1}
    return {
        "even_cofinal_values": sorted(set(evens)),
        "odd_cofinal_prefix": odds[:8],
    }


def two_adic_inverse_family(depth: int = 16) -> list[int]:
    """Return coherent residues 3^{-1} mod 2^n for n=1..depth."""
    residues = [pow(3, -1, 2**n) for n in range(1, depth + 1)]
    for n in range(1, depth):
        # residues[n] is mod 2^(n+1); reduction must equal the prior stage.
        assert residues[n] % (2**n) == residues[n - 1]
        assert (3 * residues[n - 1] - 1) % (2**n) == 0
    return residues


def check_witness_back_failure() -> dict[str, object]:
    """Point existence descends, while exact coarse witness identity has no back lift."""
    X = ("a", "b")
    Y = ("u", "v")
    relation = {("a", "u"), ("b", "v")}
    qx = {"a": "*", "b": "*"}
    qy = {"u": "u", "v": "v"}

    coarse = {(qx[x], qy[y]) for x, y in relation}
    point_exists = {
        x: any(x_fine == x for x_fine, _ in relation)
        for x in X
    }
    assert len(set(point_exists.values())) == 1
    assert all(point_exists.values())

    x = "a"
    y_bar = "v"
    assert (qx[x], y_bar) in coarse
    lifts = [
        y
        for y in Y
        if qy[y] == y_bar and (x, y) in relation
    ]
    assert lifts == []

    return {
        "coarse_relation": sorted(coarse),
        "failed_back_pair": [x, y_bar],
    }


def normalized_shell(n: int) -> list[tuple[int, int]]:
    """S_n={(x,y)>=0: x<=y and x^2+y^2=n}."""
    out: list[tuple[int, int]] = []
    for x in range(math.isqrt(n) + 1):
        y2 = n - x * x
        y = math.isqrt(y2)
        if y * y == y2 and x <= y:
            out.append((x, y))
    return out


def k4_output(c: int, n: int, x: int, y: int, r: int) -> int:
    p = x * x * y * y
    return (c**4 - n * c * c + p) // r


def carry_decomposition(c: int, n: int, p_value: int, r: int) -> tuple[int, tuple[int, int, int]]:
    """Return q_A+q_P+kappa and the remainder interface (a,p,kappa)."""
    a_value = c**4 - n * c * c
    q_a, a = divmod(a_value, r)
    q_p, p = divmod(p_value, r)
    kappa = int(a + p >= r)
    return q_a + q_p + kappa, (a, p, kappa)


def check_carry_identity() -> int:
    checks = 0
    for r in range(2, 11):
        for c in range(0, 21):
            for n in range(0, 21):
                for p_value in range(0, 101, 5):
                    lhs = (c**4 - n * c * c + p_value) // r
                    rhs, _ = carry_decomposition(c, n, p_value, r)
                    assert lhs == rhs
                    checks += 1
    return checks


def check_equal_coarse_carry_collapse() -> int:
    """If r|c then r|(c^4-nc^2), so the cross-term carry is always zero."""
    checks = 0
    for r in range(2, 11):
        for multiple in range(0, 8):
            c = r * multiple
            for n in range(0, 30):
                a_value = c**4 - n * c * c
                assert a_value % r == 0
                for p_value in range(0, 101, 7):
                    lhs = (a_value + p_value) // r
                    rhs = a_value // r + p_value // r
                    assert lhs == rhs
                    _, (a, _, kappa) = carry_decomposition(c, n, p_value, r)
                    assert a == 0
                    assert kappa == 0
                    checks += 1
    return checks


def check_k4_shells(max_n: int = 500, c: int = 1000, r: int = 10) -> dict[str, object]:
    """Check P-injectivity, fibre counts and collision-defect decomposition."""
    shell_state_count = 0
    nontrivial_examples: list[dict[str, object]] = []

    for n in range(max_n + 1):
        shell = normalized_shell(n)
        shell_state_count += len(shell)
        p_values = [x * x * y * y for x, y in shell]

        # High coordinate P must identify the normalized state inside one shell.
        assert len(p_values) == len(set(p_values))

        # Verify the exact monotonicity difference formula used in the report.
        for (x1, y1), (x2, y2) in zip(shell, shell[1:]):
            s1, s2 = x1 * x1, x2 * x2
            p1, p2 = x1 * x1 * y1 * y1, x2 * x2 * y2 * y2
            if s1 < s2:
                assert p2 > p1
                assert p2 - p1 == (s2 - s1) * (n - s1 - s2)

        counts = Counter(k4_output(c, n, x, y, r) for x, y in shell)
        assert sum(counts.values()) == len(shell)

        defect = len(shell) - len(counts)
        assert defect == sum(value - 1 for value in counts.values() if value > 1)

        if len(shell) > 1 and len(nontrivial_examples) < 5:
            nontrivial_examples.append(
                {
                    "n": n,
                    "states": shell,
                    "P": p_values,
                    "output_fibres": sorted(counts.items()),
                }
            )

    return {
        "max_n": max_n,
        "shell_state_count": shell_state_count,
        "first_nontrivial_shells": nontrivial_examples,
    }


def main() -> None:
    summary = {
        "researcher_id": "EM-R013-0LCGPL",
        "cofinal_c4_counterexample": check_cofinal_presentation_instability(),
        "two_adic_inverse_residues": two_adic_inverse_family(),
        "witness_back_counterexample": check_witness_back_failure(),
        "carry_identity_checks": check_carry_identity(),
        "equal_coarse_carry_collapse_checks": check_equal_coarse_carry_collapse(),
        "k4_shell_checks": check_k4_shells(),
    }
    print(json.dumps(summary, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
