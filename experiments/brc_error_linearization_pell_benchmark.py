"""Finite benchmark for derivative-linearized Pell/Padé BRC tail transport.

The benchmark compares the new table-free Pell/Padé predictor with the previous
high-order alternating-Taylor table-free tail at equal formal error order.  It
also records the first multiplier at which each exact <=2-correction certificate
holds on deterministic N=2^bits-159 probes.

Direct isqrt timing is included as an implementation baseline.  No factorization
complexity claim follows from these timings.
"""
from __future__ import annotations

import csv
import statistics
import time
from math import isqrt
from pathlib import Path
from types import SimpleNamespace

from enterprise_math.brc_error_linearization_pell import (
    pell_two_correction_certificate,
    transport_pell_tail,
)
from enterprise_math.brc_table_free_tail import (
    transport_certified_tail,
    two_correction_certificate,
)

CASES = ((512, 32), (1024, 32), (2048, 64), (2048, 128), (4096, 128), (8192, 256))
STEP = 2


def probe_n(bits: int) -> int:
    return (1 << bits) - 159


def source_state(n: int, multiplier: int):
    root = isqrt(multiplier * n)
    return SimpleNamespace(
        n=n,
        multiplier=multiplier,
        root=root,
        remainder=multiplier * n - root * root,
    )


def first_certified(bits: int, order: int, *, pell: bool) -> int:
    n = probe_n(bits)
    degree = 2 * order

    def accepts(m: int) -> bool:
        state = source_state(n, m)
        if pell:
            return pell_two_correction_certificate(state.root, m, STEP, order)
        return two_correction_certificate(state.root, m, STEP, degree)

    lo = STEP
    hi = STEP
    while not accepts(hi):
        hi *= 2
    lo = max(STEP, hi // 2)
    while lo < hi:
        mid = (lo + hi) // 2
        if accepts(mid):
            hi = mid
        else:
            lo = mid + 1
    return lo


def median_seconds(fn, loops: int) -> float:
    fn()
    samples = []
    for _ in range(5):
        start = time.perf_counter()
        for _ in range(loops):
            fn()
        samples.append((time.perf_counter() - start) / loops)
    return statistics.median(samples)


def benchmark_rows() -> list[dict[str, object]]:
    rows = []
    for bits, order in CASES:
        degree = 2 * order
        n = probe_n(bits)
        pell_m = first_certified(bits, order, pell=True)
        taylor_m = first_certified(bits, order, pell=False)

        # Time both certified transports at the later Taylor onset so they are
        # compared on the same source state and both proof certificates hold.
        m = taylor_m
        source = source_state(n, m)
        target = (m + STEP) * n

        def direct():
            root = isqrt(target)
            return root, target - root * root

        def pell_path():
            state = transport_pell_tail(source, m + STEP, order=order)
            return state.root, state.remainder

        def taylor_path():
            state = transport_certified_tail(source, m + STEP, degree=degree)
            return state.root, state.remainder

        expected = direct()
        if pell_path() != expected or taylor_path() != expected:
            raise AssertionError("certified transport paths disagreed")

        loops = 500 if bits <= 1024 else 200 if bits <= 4096 else 80
        direct_s = median_seconds(direct, loops)
        pell_s = median_seconds(pell_path, loops)
        taylor_s = median_seconds(taylor_path, max(10, loops // 10))

        rows.append(
            {
                "n_bits": bits,
                "pade_order": order,
                "taylor_degree": degree,
                "pell_first_certified_m": pell_m,
                "taylor_first_certified_m": taylor_m,
                "taylor_threshold_over_pell": taylor_m / pell_m,
                "benchmark_m": m,
                "direct_isqrt_seconds": direct_s,
                "pell_transport_seconds": pell_s,
                "taylor_transport_seconds": taylor_s,
                "taylor_over_pell_speedup": taylor_s / pell_s,
                "direct_over_pell_speedup": direct_s / pell_s,
            }
        )
    return rows


def write_csv(path: str | Path) -> None:
    rows = benchmark_rows()
    output = Path(path)
    with output.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=rows[0].keys())
        writer.writeheader()
        writer.writerows(rows)


if __name__ == "__main__":
    target = (
        Path(__file__).resolve().parents[1]
        / "research_artifacts"
        / "brc_error_linearization_pell_benchmark_20260907.csv"
    )
    write_csv(target)
    print(target)
