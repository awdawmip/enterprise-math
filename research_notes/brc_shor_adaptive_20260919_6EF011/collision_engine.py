#!/usr/bin/env python3
"""Exact BRC collision coefficient by residue-keyed affine moments.

Only N, a, and the window Q are inputs. No order oracle, factors, CRT data,
or floating-point probability is supplied. The adaptive algorithm needs only
a square-root-size baby table, not a full-orbit traversal. Oversized fixed
windows can nevertheless cover every residue of a short orbit.
This is a weighted baby-step/giant-step specialization, NOT a new asymptotic
order-finding algorithm and NOT a full quantum-circuit simulator.
"""
from __future__ import annotations

import argparse
from dataclasses import asdict, dataclass
from math import gcd, isqrt
import json


@dataclass(frozen=True)
class CollisionResult:
    N: int
    a: int
    Q: int
    K: int
    block_size: int
    blocks: int
    baby_multiplications: int
    giant_multiplications: int
    modular_inversions: int
    residue_buckets: int
    tail_buckets: int
    stored_moment_integers: int
    matching_blocks: int


def _integer(value: int, name: str, lower: int) -> None:
    if isinstance(value, bool) or not isinstance(value, int) or value < lower:
        raise ValueError(f"{name} must be an integer >= {lower}")


def _unit(N: int, a: int) -> None:
    _integer(N, "N", 2)
    _integer(a, "a", 1)
    if a >= N or gcd(a, N) != 1:
        raise ValueError("require 1 <= a < N and gcd(a, N) = 1")


def collision_mass(N: int, a: int, Q: int, *, block_size: int | None = None,
                   max_baby_steps: int = 2_000_000) -> CollisionResult:
    """Compute #{(x,y) in [0,Q)^2: a^x = a^y mod N}, exactly.

    For d=i*B+j, each complete block contributes
      (Q-i*B)*count(a^j=a^(-iB)) - sum(j for these matches).
    Zero difference is removed before doubling, then restored once.
    The final, possibly ragged, block uses its OWN prefix moments.

    Group multiplications: B + ceil(Q/B)-1; one modular inverse.
    Table storage: O(B) residues and O(B log Q) moment bits, plus residue keys.
    Hash lookup costs are expected/amortized, not worst-case constant bit cost.
    """
    _unit(N, a)
    _integer(Q, "Q", 1)
    _integer(max_baby_steps, "max_baby_steps", 1)
    B = isqrt(Q - 1) + 1 if block_size is None else block_size
    _integer(B, "block_size", 1)
    if B > Q:
        raise ValueError("block_size must be <= Q")
    if B > max_baby_steps:
        raise MemoryError("requested baby table exceeds max_baby_steps")
    blocks = (Q + B - 1) // B
    last_size = Q - (blocks - 1) * B
    table: dict[int, tuple[int, int]] = {}
    tail: dict[int, tuple[int, int]] | None = {} if last_size != B else None
    value = 1
    for j in range(B):
        count, first = table.get(value, (0, 0))
        table[value] = (count + 1, first + j)
        if tail is not None and j < last_size:
            count, first = tail.get(value, (0, 0))
            tail[value] = (count + 1, first + j)
        value = (value * a) % N
    inverse_block = pow(value, -1, N)  # value = a^B; no factorization.
    target = 1
    weighted_positive_returns = 0
    matching_blocks = 0
    for i in range(blocks):
        current = tail if i == blocks - 1 and tail is not None else table
        count, first = current.get(target, (0, 0))
        weighted = (Q - i * B) * count - first
        if i == 0:
            weighted -= Q  # remove d=0, which is ALWAYS one of these matches.
        if weighted < 0:
            raise ArithmeticError("invalid positive-return aggregate")
        weighted_positive_returns += weighted
        matching_blocks += int(count > 0)
        if i + 1 < blocks:
            target = (target * inverse_block) % N
    K = Q + 2 * weighted_positive_returns
    if K < Q or K > Q * Q or (K - Q) % 2:
        raise ArithmeticError("collision invariants failed")
    tail_buckets = 0 if tail is None else len(tail)
    return CollisionResult(N, a, Q, K, B, blocks, B, blocks - 1, 1,
                           len(table), tail_buckets,
                           2 * (len(table) + tail_buckets), matching_blocks)


def model_collision(Q: int, candidate: int) -> int:
    """Integer decoder model only. Not used to obtain a collision coefficient."""
    _integer(Q, "Q", 1)
    _integer(candidate, "candidate", 1)
    q, s = divmod(Q, candidate)
    return (candidate - s) * q * q + s * (q + 1) * (q + 1)


def decode_fixed_window(Q: int, K: int, upper: int) -> int:
    """Invert strictly decreasing model K_Q(r) for 1 <= r <= upper <= Q."""
    _integer(Q, "Q", 1)
    _integer(K, "K", 1)
    _integer(upper, "upper", 1)
    if upper > Q or not model_collision(Q, upper) <= K <= Q * Q:
        raise ValueError("K is outside the declared order interval")
    lo, hi = 1, upper
    while lo < hi:
        mid = (lo + hi) // 2
        if model_collision(Q, mid) > K:
            lo = mid + 1
        else:
            hi = mid
    if model_collision(Q, lo) != K:
        raise ValueError("K is not realizable by a period in the declared range")
    return lo


def adaptive_order(N: int, a: int, *, max_baby_steps: int = 2_000_000) -> dict:
    """Double Q until K_Q > Q, then return (3Q-K_Q)//2.

    No order input is passed to the coefficient engine. Previous zero-collision
    windows certify minimality; final modular powering is a consistency check,
    not the sole proof of minimality. Total group work and storage are O(sqrt(r)).
    """
    _unit(N, a)
    _integer(max_baby_steps, "max_baby_steps", 1)
    Q = 1
    limit = 1 << (N - 1).bit_length()
    stages: list[dict] = []
    total_multiplications = 0
    peak_buckets = 0
    while Q <= limit:
        # Dyadic B divides Q, so adaptive windows need no ragged-tail table.
        B = 1 << ((Q.bit_length() - 1) // 2)
        result = collision_mass(N, a, Q, block_size=B,
                                max_baby_steps=max_baby_steps)
        row = asdict(result)
        stages.append(row)
        total_multiplications += result.baby_multiplications + result.giant_multiplications
        peak_buckets = max(peak_buckets, result.residue_buckets + result.tail_buckets)
        if result.K > Q:
            numerator = 3 * Q - result.K
            if numerator % 2:
                raise ArithmeticError("nonintegral first-collision decoder")
            recovered = numerator // 2
            if not Q // 2 <= recovered < Q or pow(a, recovered, N) != 1:
                raise ArithmeticError("invalid first-collision order certificate")
            return {
                "N": N, "a": a, "order": recovered, "first_window": Q,
                "K": result.K, "peak_residue_buckets": peak_buckets,
                "group_multiplications": total_multiplications,
                "modular_inversions": len(stages),
                "final_consistency_powers": 1,
                "stages": stages,
                "status": "EXACT_WEIGHTED_BSGS_BASELINE_NOT_QUANTUM_SPEEDUP",
            }
        Q *= 2
    raise ArithmeticError("finite-unit order bound violated")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("N", type=int)
    parser.add_argument("a", type=int)
    parser.add_argument("--window", type=int)
    parser.add_argument("--block-size", type=int)
    parser.add_argument("--max-baby-steps", type=int, default=2_000_000)
    args = parser.parse_args()
    try:
        if args.window is None:
            if args.block_size is not None:
                parser.error("--block-size requires --window")
            output = adaptive_order(args.N, args.a, max_baby_steps=args.max_baby_steps)
        else:
            output = asdict(collision_mass(args.N, args.a, args.window,
                           block_size=args.block_size,
                           max_baby_steps=args.max_baby_steps))
    except (ValueError, MemoryError, ArithmeticError) as exc:
        parser.exit(2, f"error: {exc}\n")
    print(json.dumps(output, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
