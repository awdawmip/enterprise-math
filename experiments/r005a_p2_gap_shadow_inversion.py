#!/usr/bin/env python3
"""R005-A p=2 bounded-deficit prime-gap shadow inversion.

This program does not enumerate every k in a q^2 seam.  It consumes a
*complete, attested* catalog of all sufficiently large consecutive-prime gaps
in the required cofactor-floor band, inverts the floor-square map, and checks
only the resulting candidate k values.

The scanner fails closed when catalog coverage or completeness metadata is
insufficient.  Standard library only; exact integer arithmetic throughout.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import sys
from dataclasses import asdict, dataclass
from math import isqrt
from pathlib import Path
from typing import Any, Iterable, Sequence

P85 = 101_412_319_996_363_309_069
DEFAULT_GAP_BOUND = 916
DEFAULT_H = DEFAULT_GAP_BOUND // 2
UINT64_MAX = (1 << 64) - 1
MR_BASES_U64 = (2, 325, 9375, 28178, 450775, 9780504, 1795265022)
SMALL_PRIMES = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37)


class CatalogError(ValueError):
    """Raised when a catalog cannot support a fail-closed certificate."""


def ceil_sqrt(n: int) -> int:
    if n < 0:
        raise ValueError("ceil_sqrt requires n >= 0")
    r = isqrt(n)
    return r if r * r == n else r + 1


def is_prime_u64(n: int) -> bool:
    """Deterministic Miller-Rabin for 0 <= n < 2^64."""
    if n < 2:
        return False
    if n > UINT64_MAX:
        raise ValueError("is_prime_u64 input exceeds 2^64-1")
    for p in SMALL_PRIMES:
        if n % p == 0:
            return n == p
    d = n - 1
    s = 0
    while d % 2 == 0:
        d //= 2
        s += 1
    for a in MR_BASES_U64:
        if a % n == 0:
            continue
        x = pow(a, d, n)
        if x in (1, n - 1):
            continue
        for _ in range(1, s):
            x = (x * x) % n
            if x == n - 1:
                break
        else:
            return False
    return True


def floor_width(k: int, q_square: int) -> int:
    return (k * k + 2 * k) // q_square - (k * k) // q_square


def floor_square_preimage(m: int, q_square: int) -> tuple[int, int]:
    """All k with floor(k^2/Q)=m form this inclusive interval."""
    if m < 0 or q_square <= 0:
        raise ValueError("requires m >= 0 and Q > 0")
    lo = ceil_sqrt(m * q_square)
    hi = ceil_sqrt((m + 1) * q_square) - 1
    return lo, hi


def required_even_gap_min(raw_min: int, floor_start: int) -> int:
    """Normalize a threshold using evenness of prime gaps above 3."""
    if raw_min <= 1 or floor_start <= 2:
        return raw_min
    return raw_min if raw_min % 2 == 0 else raw_min + 1


@dataclass(frozen=True)
class Seam:
    q: int
    q_square: int
    gap_bound: int
    h: int
    k_global_fail: int
    k_q2_width: int
    k_last: int
    s_max: int
    d_max_bound: int
    floor_start: int
    floor_end: int
    required_gap_start_min: int
    required_gap_start_max: int
    required_complete_gap_ge: int
    one_unit_whole_seam: bool


def build_seam(q: int, *, p85: int = P85, gap_bound: int = DEFAULT_GAP_BOUND) -> Seam:
    if q < 2 or not is_prime_u64(q):
        raise ValueError(f"q must be prime, got {q}")
    if gap_bound <= 0 or gap_bound % 2:
        raise ValueError("gap_bound must be a positive even integer")
    Q = q * q
    H = gap_bound // 2
    kg = ceil_sqrt(p85 * q)
    kw = H * Q
    if kg >= kw:
        raise ValueError(f"no q^2 seam for q={q}: k_global_fail >= k_q2_width")
    k_last = kw - 1
    s_max = kw - kg
    # Since 0 <= r < Q in D=G+floor((r-2s)/Q), this is a safe bound.
    d_max = (2 * s_max + Q - 1) // Q
    n0 = (kg * kg) // Q
    n1 = (k_last * k_last) // Q
    raw_gap_min = gap_bound - d_max + 1
    complete_gap_ge = required_even_gap_min(raw_gap_min, n0)
    return Seam(
        q=q,
        q_square=Q,
        gap_bound=gap_bound,
        h=H,
        k_global_fail=kg,
        k_q2_width=kw,
        k_last=k_last,
        s_max=s_max,
        d_max_bound=d_max,
        floor_start=n0,
        floor_end=n1,
        required_gap_start_min=n0 - (d_max - 1),
        required_gap_start_max=n1,
        required_complete_gap_ge=complete_gap_ge,
        one_unit_whole_seam=(2 * s_max <= Q),
    )


@dataclass(frozen=True)
class GapRow:
    start: int
    gap: int

    @property
    def end(self) -> int:
        return self.start + self.gap


def verify_consecutive_gap(row: GapRow) -> None:
    if row.start < 2 or row.gap < 1:
        raise CatalogError(f"invalid gap row {row}")
    if row.end > UINT64_MAX:
        raise CatalogError("gap endpoint exceeds uint64 verifier range")
    if not is_prime_u64(row.start):
        raise CatalogError(f"gap start is not prime: {row.start}")
    if not is_prime_u64(row.end):
        raise CatalogError(f"gap end is not prime: {row.end}")
    first = row.start + 1
    if first % 2 == 0:
        first += 1
    for n in range(first, row.end, 2):
        if is_prime_u64(n):
            raise CatalogError(
                f"row is not consecutive: interior prime {n} in {row.start}+{row.gap}"
            )


def canonical_rows_sha256(rows: Sequence[GapRow]) -> str:
    payload = "".join(f"{r.start},{r.gap}\n" for r in rows).encode("ascii")
    return hashlib.sha256(payload).hexdigest()


def load_catalog(path: Path) -> tuple[dict[str, Any], list[GapRow]]:
    data = json.loads(path.read_text(encoding="utf-8"))
    if data.get("schema") != "R005A_CONSECUTIVE_PRIME_GAP_CATALOG_V1":
        raise CatalogError("unsupported or missing catalog schema")
    rows = [GapRow(int(x["start"]), int(x["gap"])) for x in data.get("rows", [])]
    if rows != sorted(rows, key=lambda r: (r.start, r.gap)):
        raise CatalogError("rows must be sorted by (start,gap)")
    if len(set(rows)) != len(rows):
        raise CatalogError("duplicate gap rows")
    declared_hash = str(data.get("rows_sha256", ""))
    actual_hash = canonical_rows_sha256(rows)
    if declared_hash != actual_hash:
        raise CatalogError(f"rows_sha256 mismatch: declared={declared_hash} actual={actual_hash}")
    return data, rows


def validate_catalog_for_seam(
    metadata: dict[str, Any], rows: Sequence[GapRow], seam: Seam, *, verify_rows: bool
) -> None:
    if metadata.get("completeness_attestation") is not True:
        raise CatalogError("completeness_attestation must be true")
    coverage_start = int(metadata.get("coverage_start", 0))
    coverage_end = int(metadata.get("coverage_end", -1))
    complete_ge = int(metadata.get("complete_for_gap_ge", 10**30))
    max_gap_bound = int(metadata.get("max_gap_bound", 10**30))
    max_bound_start = int(metadata.get("max_gap_bound_start", 0))
    max_bound_end = int(metada.get("max_gap_bound_end", -1))

    if coverage_start > seam.required_gap_start_min or coverage_end < seam.required_gap_start_max:
        raise CatalogError(
            "catalog coverage does not contain required gap-start band "
            f
[{seam.required_gap_start_min},{seam.required_gap_start_max}]"
        )
    if complete_ge > seam.required_complete_gap_ge:
        raise CatalogError(
            f"catalog is complete only for gaps >= {complete_ge}, but >= "
            f"{seam.required_complete_gap_ge} is required"
        )
    if max_gap_bound > seam.gap_bound:
        raise CatalogError(
            f"declared max gap {max_gap_bound} does not prove required bound {seam.gap_bound}"
        )
    if max_bound_start > seam.required_gap_start_min or max_bound_end < seam.required_gap_start_max:
        raise CatalogError("max-gap bound does not cover the required gap-start band")

    relevant = [
        r for r in rows
        if seam.required_gap_start_min <= r.start <= seam.required_gap_start_max
        and r.gap >= seam.required_complete_gap_ge
    ]
    for r in rows:
        if coverage_start <= r.start <= coverage_end and r.gap >= complete_ge:
            if r.gap > seam.gap_bound:
                raise CatalogError(f"catalog row {r} contradicts max gap bound {seam.gap_bound}")
    if verify_rows:
        for row in relevant:
            verify_consecutive_gap(row)


def scan_gap_shadows(seam: Seam, rows: Iterable[GapRow]) -> list[dict[str, int]]:
    """Return all exact prime-free candidates implied by consecutive gaps."""
    hits: dict[int, dict[str, int]] = {}
    G = seam.gap_bound
    Q = seam.q_square
    for row in rows:
        delta = G - row.gap
        if delta < 0:
            raise CatalogError(f"gap {row.gap} exceeds declared bound {G}")
        max_t = seam.d_max_bound - 1 - delta
        if max_t < 0:
            continue
        for t in range(max_t + 1):
            n = row.start + t
            lo, hi = floor_square_preimage(n, Q)
            lo = max(lo, seam.k_global_fail)
            hi = min(hi, seam.k_last)
            if lo > hi:
                continue
            # In this R005 seam 2k+1 > Q, hence this interval is a singleton.
            # Keep the loop exact so the helper remains valid outside that regime.
            for k in range(lo, hi + 1):
                D = floor_width(k, Q)
                d = G - D
                if d < 1:
                    continue
                # Exact gap-shadow equivalence: prime-free iff g > D+t.
                if row.gap > D + t:
                    hits[k] = {
                        "k": k,
                        "floor_start": n,
                        "floor_width": D,
                        "deficit": d,
                        "gap_start": row.start,
                        "gap": row.gap,
                        "shadow_offset": t,
                    }
    return [hits[k] for k in sorted(hits)]


def describe_seam(seam: Seam) -> dict[str, Any]:
    data = asdict(seam)
    data["real_width_at_start_numerator"] = 2 * seam.k_global_fail
    data["real_width_denominator"] = seam.q_square
    if seam.d_max_bound >= 2:
        k_real_915 = (915 * seam.q_square + 1) // 2
        data["first_k_real_width_at_least_915"] = k_real_915
        data["mixed_deficit_prefix_length"] = max(0, k_real_915 - seam.k_global_fail)
        data["one_unit_real_width_tail_length"] = max(0, seam.k_q2_width - k_real_915)
    return data


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--q", type=int, required=True)
    parser.add_argument("--catalog", type=Path)
    parser.add_argument("--output", type=Path)
    parser.add_argument("--describe-only", action="store_true")
    parser.add_argument("--skip-row-primality-check", action="store_true")
    args = parser.parse_args(argv)

    try:
        seam = build_seam(args.q)
        result: dict[str, Any] = {
            "schema": "R005A_P2_GAP_SHADOW_INVERSION_RESULT_V1",
            "seam": describe_seam(seam),
        }
        exit_code = 0
        if args.describe_only:
            result["status"] = "DESCRIPTION_ONLY"
        elif args.catalog is None:
            raise CatalogError("--catalog is required unless --describe-only is used")
        else:
            metadata, rows = load_catalog(args.catalog)
            validate_catalog_for_seam(
                metadata, rows, seam, verify_rows=not args.skip_row_primality_check
            )
            hits = scan_gap_shadows(seam, rows)
            result["catalog"] = {
                "path": str(args.catalog),
                "source_id": metadata.get("source_id"),
                "rows_sha256": metadata.get("rows_sha256"),
                "rows_total": len(rows),
            }
            result["candidate_failures"] = hits
            result["candidate_failure_count"] = len(hits)
            if hits:
                result["status"] = "COUNTEREXAMPLE_FOUND"
                exit_code = 1
            else:
                result["status"] = "CERTIFIED_UNDER_ATTESTED_CATALOG"
        text = json.dumps(result, indent=2, sort_keys=True) + "\n"
    except (CatalogError, ValueError, KeyError, TypeError, json.JSONDecodeError) as exc:
        result = {
            "schema": "R005A_P2_GAP_SHADOW_INVERSION_RESULT_V1",
            "status": "FAIL_CLOSED_INCOMPLETE_OR_INVALID_CATALOG",
            "error": str(exc),
        }
        text = json.dumps(result, indent=2, sort_keys=True) + "\n"
        exit_code = 3

    if args.output:
        args.output.write_text(text, encoding="utf-8")
    sys.stdout.write(text)
    return exit_code


if __name__ == "__main__":
    raise SystemExit(main())
