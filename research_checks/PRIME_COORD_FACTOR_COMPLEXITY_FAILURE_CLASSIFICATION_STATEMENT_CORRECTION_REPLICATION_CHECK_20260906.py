#!/usr/bin/env python3
"""Independent exact audit of the PCF7 fixed-probe zero-value correction.

The load-bearing point is intentionally tiny: support compression is valid only
for nonzero fixed integers.  A zero probe has no prime-support payload but gives
`gcd(N, 0) = N`, so a zero/nonzero branch flag must survive that compression.
"""
from __future__ import annotations

import hashlib
import math
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE_CHECKER = ROOT / "research_checks/PRIME_COORD_FACTOR_COMPLEXITY_FAILURE_CLASSIFICATION_CHECK_20260831.py"
EXPECTED_SOURCE_BLOB = "b2a53c365f442fb2915cd869b77b62d9ce8a9ec8"


def git_blob_sha1(path: Path) -> str:
    data = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    d = 3
    while d * d <= n:
        if n % d == 0:
            return False
        d += 2
    return True


def probes(s: int):
    return (
        ("quadratic_plus_one", s * s + 1),
        ("quadratic_cyclotomic", s * s + s + 1),
        ("sixth_minus_one_abs", abs(s**6 - 1)),
        ("sixth_plus_one", s**6 + 1),
    )


def main() -> None:
    # Exact branch census on the frozen seed range.
    zeros = []
    nonzeros = []
    for s in range(64):
        for family, value in probes(s):
            if value == 0:
                zeros.append((family, s, value))
            else:
                nonzeros.append((family, s, value))
    assert zeros == [("sixth_minus_one_abs", 1, 0)]
    assert len(nonzeros) == 255

    # Direct algebraic reason for uniqueness of the zero branch on s>=0:
    # s^2+1>0; s^2+s+1>0; s^6+1>0; |s^6-1|=0 iff s=1.
    assert all(s * s + 1 > 0 for s in range(64))
    assert all(s * s + s + 1 > 0 for s in range(64))
    assert all(s**6 + 1 > 0 for s in range(64))
    assert [s for s in range(64) if s**6 == 1] == [1]

    # Independent balanced-semiprime witness from the frozen domain.
    p, q = 10007, 10009
    assert is_prime(p) and is_prime(q) and q < 2 * p
    N = p * q
    assert N == 100160063
    for _, _, value in nonzeros:
        assert value % p != 0 and value % q != 0
        assert math.gcd(N, value) == 1
    assert math.gcd(N, 0) == N

    # General two-branch theorem: if each hidden prime avoids a nonzero a,
    # gcd(pq,a)=1; the zero branch is exactly the trivial gcd N.
    sample_nonzero = (2, 5, 17, 65, 1001)
    for a in sample_nonzero:
        if a % p and a % q:
            assert math.gcd(N, a) == 1
    assert not (1 < math.gcd(N, 0) < N)

    # Bind and replay the original checker without changing its bytes.
    assert git_blob_sha1(SOURCE_CHECKER) == EXPECTED_SOURCE_BLOB
    text = SOURCE_CHECKER.read_text(encoding="utf-8")
    assert "return [v for v in vals if v != 0]" in text
    assert "if v:" in text
    assert "assert gcd(N2, v) == 1" in text
    proc = subprocess.run(
        [sys.executable, str(SOURCE_CHECKER)],
        cwd=ROOT,
        check=True,
        capture_output=True,
        text=True,
    )
    stdout = proc.stdout.strip()
    assert stdout.startswith("PCF7_CHECK_PASS ")

    print(
        "PASS: PCF7 fixed-probe correction; zero_count=1, zero_seed=1, "
        "gcd(N,0)=N, all 255 nonzero witness probes give gcd=1; source checker replay PASS."
    )


if __name__ == "__main__":
    main()
