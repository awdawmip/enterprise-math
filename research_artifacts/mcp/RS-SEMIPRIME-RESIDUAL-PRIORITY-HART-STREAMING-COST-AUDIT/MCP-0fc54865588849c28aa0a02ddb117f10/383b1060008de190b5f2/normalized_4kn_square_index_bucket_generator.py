"""Post-open exact normalized 4kN bucket generator; no factoring labels as inputs.

Owner EM-SEMIPRIME-1F8B9B / RUN-02bc03dfff15c15ce7daf2f3.
Logical event ledger is distinct from wall time and bit cost.
Original primitive candidate: x=ceil_sqrt(4*k*N), e=x*x-4*k*N.
"""
from __future__ import annotations

from dataclasses import dataclass, field
from math import isqrt, gcd
from typing import Iterator


@dataclass
class PaidLedger:
    counts: dict[str, int] = field(default_factory=dict)

    def charge(self, event: str, amount: int = 1) -> None:
        if amount < 0:
            raise ValueError("negative charge")
        self.counts[event] = self.counts.get(event, 0) + amount


@dataclass(frozen=True)
class Candidate:
    k: int
    x: int
    residual: int
    bucket: int


def ceil_sqrt(n: int, meter: PaidLedger) -> int:
    if n < 0:
        raise ValueError("negative radicand")
    meter.charge("integer_sqrt")
    z = isqrt(n)
    meter.charge("root_rounding_square")
    meter.charge("root_rounding_compare")
    if z * z != n:
        meter.charge("root_rounding_increment")
        z += 1
    return z


def ceil_cuberoot(n: int, meter: PaidLedger) -> int:
    """Public integer budget. Preparation charged equally to both schedules."""
    if n < 1:
        raise ValueError("positive N required")
    lo, hi = 0, 1 << ((n.bit_length() + 2) // 3)
    meter.charge("budget_bound_init")
    while lo < hi:
        meter.charge("budget_binary_step")
        mid = (lo + hi) // 2
        meter.charge("budget_cube_products", 2)
        if mid * mid * mid >= n:
            hi = mid
        else:
            lo = mid + 1
    return lo


def bucket_stream(N: int, K: int, B: int, meter: PaidLedger) -> Iterator[Candidate]:
    """Exact priority (bucket,k), coarse normalized scores, no cached full lists.

    All a rows, including rows with an empty admissible interval, are charged.
    Works beyond K<=N by intersecting full per-a multi-k intervals.
    Consumers may stop at a true nontrivial factor; inspected prefixes remain paid.
    """
    if min(N, K, B) < 1:
        raise ValueError("positive N,K,B required")
    meter.charge("generator_setup_products", 2)
    D = 4 * N
    BD = B * D
    a0 = ceil_sqrt(D, meter)
    amax = ceil_sqrt(D * K, meter)
    meter.charge("generator_setup_products")
    meter.charge("initial_square_products")
    first_s = a0 * a0
    meter.charge("initial_denominator_arithmetic", 2)
    first_q = 2 * a0 - 1
    meter.charge("initial_previous_square_subtraction")
    first_previous = first_s - first_q

    for b in range(B):
        meter.charge("bucket_pass")
        meter.charge("bucket_state_initialization", 4)
        meter.charge("bucket_index_increment")
        next_bucket = b + 1
        s, previous_s, q = first_s, first_previous, first_q
        for a in range(a0, amax + 1):
            meter.charge("square_index_row")
            meter.charge("row_floor_divisions", 4)
            meter.charge("row_products", 3)
            meter.charge("row_interval_arithmetic", 4)
            lower_candidate = max(1, previous_s // D + 1)
            upper_candidate = min(K, s // D)
            scaled_s = B * s
            lower_bucket = (scaled_s - next_bucket * q) // BD + 1
            upper_bucket = (scaled_s - b * q) // BD
            meter.charge("row_interval_bound_comparisons", 4)
            lower = max(lower_candidate, lower_bucket)
            upper = min(upper_candidate, upper_bucket)
            meter.charge("row_empty_interval_check")
            if lower <= upper:
                for k in range(lower, upper + 1):
                    meter.charge("candidate_emission")
                    meter.charge("emission_product")
                    meter.charge("emission_subtraction")
                    meter.charge("emitted_integer_fields", 4)
                    yield Candidate(k, a, s - D * k, b)
            if a < amax:
                meter.charge("square_index_transport")
                meter.charge("transport_additions", 3)
                meter.charge("transport_state_copy")
                previous_s = s
                s += q + 2
                q += 2


def ascending_hart_stream(N: int, K: int, B: int,
                          meter: PaidLedger) -> Iterator[Candidate]:
    """Same original 4kN upper points in k order (not a new Hart claim).

    Bucket annotations are evaluator metadata: this baseline does not compute
    rational priorities in its deployment schedule.
    """
    if min(N, K, B) < 1:
        raise ValueError("positive N,K,B required")
    D = 4 * N
    meter.charge("baseline_setup_product")
    for k in range(1, K + 1):
        meter.charge("multiplier_point")
        meter.charge("point_products", 2)
        radicand = D * k
        x = ceil_sqrt(radicand, meter)
        e = x * x - radicand
        meter.charge("point_subtraction")
        yield Candidate(k, x, e, -1)


def build_qr_tables(moduli: tuple[int, ...], meter: PaidLedger) -> tuple[tuple[bool, ...], ...]:
    tables = []
    for m in moduli:
        if m < 1:
            raise ValueError("positive sieve moduli")
        meter.charge("table_cell_initialization", m)
        table = [False] * m
        for j in range(m):
            meter.charge("table_square_product")
            meter.charge("table_mod_reduction")
            meter.charge("table_cell_write")
            table[j * j % m] = True
        tables.append(tuple(table))
        meter.charge("table_frozen_cells", m)
    return tuple(tables)


def consume_for_factor(N: int, stream: Iterator[Candidate],
                       moduli: tuple[int, ...], tables: tuple[tuple[bool, ...], ...],
                       meter: PaidLedger) -> tuple[int | None, Candidate | None]:
    """Pure factor-blind evaluator: no p,q or productive labels supplied.

    gcd=1 and gcd=N are failures and must not terminate successfully.
    QR table creation is separate common charged preparation.
    """
    for candidate in stream:
        meter.charge("consumer_candidate")
        rejected = False
        for m, table in zip(moduli, tables):
            meter.charge("modular_check")
            meter.charge("modular_reduction")
            meter.charge("table_lookup")
            if not table[candidate.residual % m]:
                meter.charge("sieve_rejection")
                rejected = True
                break
        if rejected:
            continue
        meter.charge("residual_square_test")
        meter.charge("residual_integer_sqrt")
        y = isqrt(candidate.residual)
        meter.charge("residual_square_product")
        if y * y != candidate.residual:
            meter.charge("nonsquare_failure")
            continue
        for sign in (-1, 1):
            meter.charge("gcd_input_arithmetic")
            meter.charge("gcd")
            d = gcd(candidate.x + sign * y, N)
            meter.charge("gcd_nontriviality_comparisons", 2)
            if 1 < d < N:
                meter.charge("productive_hit")
                return d, candidate
            meter.charge("trivial_gcd_failure")
    meter.charge("range_exhaustion")
    return None, None

