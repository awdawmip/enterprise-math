#!/usr/bin/env python3
"""R005-A exact p=2 three-factor shell verifier.

Consumes the independent 49-basin / 50-residual certificate family and checks the exact shell normal form implied by T-A21 when the fourth-root core is forced.
"""

from __future__ import annotations
import importlib.util
from pathlib import Path
import json

HERE = Path(__file__).resolve().parent
SRC = HERE / "r005a_p2_exact_residual_family.py"
spec = importlib.util.spec_from_file_location("p2family", SRC)
if spec is None or spec.loader is None:
    raise RuntimeError(f"cannot load {SRC}")
family = importlib.util.module_from_spec(spec)
spec.loader.exec_module(family)


def main() -> None:
    repeated = 0
    squarefree = 0
    rows = []

    for k, n, factors in family.CERTIFICATES:
        U = k * k + 2 * k
        c4 = family.integer_root(U, 4)
        c3 = family.integer_root(U, 3)

        prime_multiset = []
        for p, e in factors:
            prime_multiset.extend([p] * e)
        prime_multiset.sort()
        assert len(prime_multiset) == 3
        a, b, c = prime_multiset

        assert c4 < a <= c3
        assert a <= k
        assert b <= k

        support = tuple(sorted(p for p, _ in factors if p <= k))
        assert len(set(support)) >= 2
        assert all(not family.witness_forced(k, q) for q in support)

        if len(set(prime_multiset)) == 2:
            repeated += 1
            pattern = "repeated-prime q^2*r / q*r^2"
        elif len(set(prime_multiset)) == 3:
            squarefree += 1
            pattern = "squarefree q*r*s"
        else:
            raise AssertionError(("prime cube cannot be residual", k, n, factors))

        rows.append({
            "k": k,
            "n": n,
            "prime_multiset": prime_multiset,
            "fourth_root_core": c4,
            "cube_root_core": c3,
            "candidate_support": support,
            "pattern": pattern,
        })

    assert repeated + squarefree == 50
    assert squarefree > 0
    assert repeated > 0

    result = {
        "status": "R005-A EXACT P2 THREE-FACTOR SHELL CHECK",
        "certificate_count": len(rows),
        "repeated_prime_count": repeated,
        "squarefree_count": squarefree,
        "shell": "U^(1/4) < a <= U^(1/3), a<=b<=c, a and b candidate non-forced",
        "rows": rows,
    }
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
