from __future__ import annotations

import csv
import random
import statistics
import time
from dataclasses import dataclass
from math import isqrt
from pathlib import Path

from enterprise_math.brc_table_free_tail import (
    transport_certified_tail,
    two_correction_certificate,
)

BITS = (512, 1024, 2048, 4096)
DEGREES = (4, 16, 64, 128, 256)
SEED = 20260907


@dataclass(frozen=True)
class Source:
    n: int
    multiplier: int
    root: int
    remainder: int


def source_state(n: int, multiplier: int) -> Source:
    root = isqrt(multiplier * n)
    return Source(n, multiplier, root, multiplier * n - root * root)


def certified_start(n: int, degree: int, step: int = 2) -> int:
    lower = max(step, 2)
    upper = lower
    while True:
        source = source_state(n, upper)
        if two_correction_certificate(source.root, upper, step, degree):
            break
        upper *= 2
    lower = max(step, upper // 2)
    while lower + 1 < upper:
        middle = (lower + upper) // 2
        source = source_state(n, middle)
        if two_correction_certificate(source.root, middle, step, degree):
            upper = middle
        else:
            lower = middle
    return upper


def timing_ratio(
    bits: int,
    degree: int,
    samples: int = 40,
    repeats: int = 3,
) -> tuple[float, float, float, float]:
    rng = random.Random(SEED + bits + degree)
    values = []
    for _ in range(samples):
        n = rng.getrandbits(bits) | (1 << (bits - 1)) | 1
        multiplier = certified_start(n, degree, 2)
        values.append(source_state(n, multiplier))

    sample = values[0]
    transport_certified_tail(sample, sample.multiplier + 2, degree=degree)

    tail_times = []
    direct_times = []
    for _ in range(repeats):
        start = time.perf_counter()
        for source in values:
            transport_certified_tail(
                source, source.multiplier + 2, degree=degree
            )
        tail_times.append(time.perf_counter() - start)

        start = time.perf_counter()
        for source in values:
            isqrt((source.multiplier + 2) * source.n)
        direct_times.append(time.perf_counter() - start)

    tail_seconds = statistics.median(tail_times)
    direct_seconds = statistics.median(direct_times)
    median_multiplier = statistics.median(source.multiplier for source in values)
    return (
        median_multiplier,
        direct_seconds,
        tail_seconds,
        direct_seconds / tail_seconds,
    )


def benchmark_rows() -> list[dict[str, object]]:
    rng = random.Random(SEED)
    values = {
        bits: rng.getrandbits(bits) | (1 << (bits - 1)) | 1 for bits in BITS
    }
    rows: list[dict[str, object]] = []
    for bits in BITS:
        n = values[bits]
        for degree in DEGREES:
            multiplier = certified_start(n, degree, 2)
            rows.append(
                {
                    "row_type": "threshold",
                    "n_bits": bits,
                    "degree": degree,
                    "step": 2,
                    "certified_start_m": multiplier,
                    "certified_start_m_bits": multiplier.bit_length(),
                    "direct_seconds": "",
                    "table_free_seconds": "",
                    "direct_over_table_free": "",
                }
            )

    for bits, degree in (
        (512, 64),
        (1024, 128),
        (2048, 64),
        (2048, 256),
        (4096, 128),
        (4096, 256),
    ):
        multiplier, direct, tail, ratio = timing_ratio(bits, degree)
        rows.append(
            {
                "row_type": "timing",
                "n_bits": bits,
                "degree": degree,
                "step": 2,
                "certified_start_m": multiplier,
                "certified_start_m_bits": int(multiplier).bit_length(),
                "direct_seconds": direct,
                "table_free_seconds": tail,
                "direct_over_table_free": ratio,
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
        / "brc_table_free_tail_benchmark_20260907.csv"
    )
    write_csv(target)
    print(target)
