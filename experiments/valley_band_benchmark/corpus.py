#!/usr/bin/env python3
"""Deterministic frozen balanced-semiprime corpus generator."""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
CONFIG_PATH = Path(__file__).with_name("frozen_config.json")
DEFAULT_OUTPUT = ROOT / "research_output" / "VALLEY_BAND_BENCHMARK_CORPUS_20260823.csv"

FIXED = (
    ("F104", "fixed_checkpoint", 104, 11681976071094177586960974447503, 2863308968584027, 4079886662343389),
    ("F112", "fixed_checkpoint", 112, 3023488086125431650366346299720263, 53570471665823809, 56439452409270407),
    ("F128", "fixed_checkpoint", 128, 236865402759503171708411529790601388017, 14465361523279898393, 16374661800073417369),
)


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    for p in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37):
        if n % p == 0:
            return n == p
    d, s = n - 1, 0
    while d % 2 == 0:
        d //= 2
        s += 1
    for a in (2, 325, 9375, 28178, 450775, 9780504, 1795265022):
        if a % n == 0:
            continue
        x = pow(a, d, n)
        if x in (1, n - 1):
            continue
        for _ in range(s - 1):
            x = x * x % n
            if x == n - 1:
                break
        else:
            return False
    return True


def candidate(seed: str, bits: int, row: int, side: str, attempt: int) -> int:
    payload = f"{seed}|{bits}|{row}|{side}|{attempt}".encode("utf-8")
    raw = int.from_bytes(hashlib.sha256(payload).digest(), "big")
    mask = (1 << bits) - 1
    value = raw & mask
    value |= 3 << (bits - 2)
    value |= 1
    return value


def deterministic_prime(seed: str, bits: int, row: int, side: str) -> tuple[int, int]:
    for attempt in range(1_000_000):
        value = candidate(seed, bits, row, side, attempt)
        if is_prime(value):
            return value, attempt
    raise RuntimeError("deterministic prime search exhausted")


def generate_rows() -> list[dict[str, object]]:
    config = json.loads(CONFIG_PATH.read_text(encoding="utf-8"))
    seed = config["corpus"]["seed"]
    train = set(config["splits"]["training_ids"])
    holdout = set(config["splits"]["holdout_ids"])
    rows: list[dict[str, object]] = []
    for group in config["corpus"]["groups"]:
        bits = int(group["bits"])
        half = bits // 2
        prefix = "E" if group["purpose"] == "state_equivalence" else "R"
        for index in range(int(group["count"])):
            corpus_id = f"{prefix}{bits}-{index:02d}"
            p, p_attempt = deterministic_prime(seed, half, index, f"{corpus_id}:p")
            q, q_attempt = deterministic_prime(seed, half, index, f"{corpus_id}:q")
            if p == q:
                q, q_attempt = deterministic_prime(seed, half, index + 10_000, f"{corpus_id}:q2")
            n = p * q
            if n.bit_length() != bits:
                raise AssertionError((corpus_id, n.bit_length(), bits))
            rows.append(
                {
                    "corpus_id": corpus_id,
                    "purpose": group["purpose"],
                    "split": "training" if corpus_id in train else "holdout" if corpus_id in holdout else "equivalence",
                    "bits": bits,
                    "N": n,
                    "factor_p_validation_only": min(p, q),
                    "factor_q_validation_only": max(p, q),
                    "p_attempt": p_attempt,
                    "q_attempt": q_attempt,
                    "generator_seed": seed,
                    "generator_rule": config["corpus"]["prime_rule"],
                }
            )
    for corpus_id, purpose, bits, n, p, q in FIXED:
        rows.append(
            {
                "corpus_id": corpus_id,
                "purpose": purpose,
                "split": "holdout",
                "bits": bits,
                "N": n,
                "factor_p_validation_only": p,
                "factor_q_validation_only": q,
                "p_attempt": "",
                "q_attempt": "",
                "generator_seed": "locked_packet",
                "generator_rule": "verbatim fixed checkpoint; factors validation-only",
            }
        )
    return rows


def canonical_digest(rows: list[dict[str, object]]) -> str:
    raw = json.dumps(rows, sort_keys=True, separators=(",", ":")).encode("utf-8")
    return hashlib.sha256(raw).hexdigest()


def write_csv(path: Path, rows: list[dict[str, object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    rows = generate_rows()
    if args.check:
        with args.output.open(encoding="utf-8", newline="") as handle:
            existing = list(csv.DictReader(handle))
        normalized = [{k: str(v) for k, v in row.items()} for row in rows]
        if existing != normalized:
            raise SystemExit("frozen corpus mismatch")
    else:
        write_csv(args.output, rows)
    print(json.dumps({"rows": len(rows), "digest": canonical_digest(rows), "output": str(args.output)}))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
