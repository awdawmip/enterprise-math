#!/usr/bin/env python3
"""Independent verifier for RS-FACTOR-BLIND-SQUARE-MULTIPLICATIVE-SHELL-BRIDGE.

This checker does not replay the private authoring corpus. It verifies the exact
factor-blind feature identities, the BCT finite-partition bound, the published
adversarial collision, hidden-label separation inside the verifier compartment,
and that the public artifacts contain no serialized p/q rows.
"""
from __future__ import annotations
import hashlib
import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ART = ROOT / "research_artifacts" / "FACTOR_BLIND_SQUARE_MULTIPLICATIVE_SHELL_BRIDGE"
MANIFEST = ART / "public_manifest.json"
SUMMARY = ART / "result_summary.json"

K_CARRY = list(range(2, 65))
K_PRIME = [1, 2, 3, 5, 7, 11, 13, 17, 19, 23]
ADV = [(9_990_157, 3_119, 3_203), (9_990_159, 3, 3_330_053)]


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    small = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37)
    for p in small:
        if n == p:
            return True
        if n % p == 0:
            return False
    d = 41
    step = 2
    limit = math.isqrt(n)
    while d <= limit:
        if n % d == 0:
            return False
        d += step
        step = 6 - step
    return True


def prev_prime(x: int) -> int:
    y = x if is_prime(x) else x - 1
    while y >= 2 and not is_prime(y):
        y -= 1
    return y


def next_prime(x: int) -> int:
    y = x if is_prime(x) else x + 1
    while not is_prime(y):
        y += 1
    return y


def carry_word(n: int):
    s = math.isqrt(n)
    return tuple(math.isqrt(k * n) - math.isqrt(k * s * s) for k in K_CARRY)


def transported_prime_gap_signature(n: int):
    out = []
    for k in K_PRIME:
        x = math.isqrt(k * n)
        p0 = prev_prime(x)
        p1 = next_prime(x)
        out.append((x, x - p0, p1 - x, p1 - p0))
    return tuple(out)


def sieve(limit: int):
    a = bytearray(b"\x01") * (limit + 1)
    a[:2] = b"\x00\x00"
    for p in range(2, math.isqrt(limit) + 1):
        if a[p]:
            start = p * p
            a[start : limit + 1 : p] = b"\x00" * (((limit - start) // p) + 1)
    primes = [i for i in range(2, limit + 1) if a[i]]
    return a, primes


def hidden_labels_for_adversary():
    _, primes = sieve(5_000_000)
    idx = {p: i + 1 for i, p in enumerate(primes)}
    R = len(primes)
    max_gr = R * (R + 1) // 2 - 1
    labels = []
    for n, p, q in ADV:
        s = math.isqrt(n)
        pi_s = 0
        # bisect without importing another module
        lo, hi = 0, len(primes)
        while lo < hi:
            mid = (lo + hi) // 2
            if primes[mid] <= s:
                lo = mid + 1
            else:
                hi = mid
        pi_s = lo
        i, j = idx[p], idx[q]
        pclass = min(31, int(32 * (i - 1) / max(1, pi_s)))
        qclass = min(31, int(32 * math.log(j) / math.log(R)))
        if i == j:
            gr = j * (j + 1) // 2 - 1
        elif i == j - 1:
            gr = j * (j - 1) // 2
        else:
            gr = j * (j - 1) // 2 + i
        gclass = min(31, int(32 * math.log1p(gr) / math.log1p(max_gr)))
        T = (p + q) // 2 - (s + 1)
        tclass = 0 if T == 0 else 1 + min(31, int(32 * math.log2(T + 1) / math.log2(n)))
        labels.append((pclass, qclass, gclass, tclass, T))
    return labels


def main():
    manifest = json.loads(MANIFEST.read_text())
    summary = json.loads(SUMMARY.read_text())

    assert manifest["worker_request_schema"]["allowed"] == [
        "N", "public_seed", "candidate_id", "precommitted_parameters"
    ]
    assert manifest["corpus"]["private_factors_serialized_to_worker"] is False
    assert summary["private_factors_in_summary"] is False

    # Information-preserving square-shell identity on public audit probes.
    for vals in manifest["corpus"]["audit_probe_N"].values():
        for n in vals:
            s = math.isqrt(n)
            assert s * s < n < (s + 1) * (s + 1)
            a = n - s * s
            b = (s + 1) * (s + 1) - n
            L = 2 * s + 1
            D = b - a
            assert 4 * n - 1 == L * L - 2 * D
            assert n == (L * L + 1 - 2 * D) // 4

    # Exact BCT theorem: each coordinate is a monotone step function of shell r.
    # For k=2..64 the total possible jumps are <= sum ceil(sqrt(k)) = 371.
    assert sum(math.ceil(math.sqrt(k)) for k in K_CARRY) == 371
    s = 3160
    previous = None
    words = []
    for r in range(1, 2 * s + 1):
        n = s * s + r
        w = carry_word(n)
        if previous is not None:
            assert all(x >= y for x, y in zip(w, previous))
        if not words or w != words[-1]:
            words.append(w)
        previous = w
    assert len(words) <= 372

    # Strong exact collision: the new BCT+TPGR signature cannot point-identify
    # the hidden multiplicative layout.
    n0, p0, q0 = ADV[0]
    n1, p1, q1 = ADV[1]
    assert p0 * q0 == n0 and p1 * q1 == n1
    assert all(is_prime(x) for x in (p0, q0, p1, q1))
    assert math.isqrt(n0) == math.isqrt(n1) == 3160
    assert carry_word(n0) == carry_word(n1)
    assert transported_prime_gap_signature(n0) == transported_prime_gap_signature(n1)

    labels = hidden_labels_for_adversary()
    expected_digest = summary["adversarial_collision"]["hidden_label_bucket_vectors_private_verifier_sha256"]
    got = "sha256:" + hashlib.sha256(
        json.dumps(labels, separators=(",", ":")).encode()
    ).hexdigest()
    assert got == expected_digest
    assert labels[0][0] - labels[1][0] >= 30
    assert labels[1][2] - labels[0][2] >= 15
    assert labels[0][4] == 0 and labels[1][4] > 1_000_000

    # Published terminal boundary must not overclaim factorization gain.
    assert summary["terminal_verdict"] == "NEGATIVE_BOUNDARY"
    assert summary["success_levels"] == {"S1": False, "S2": False, "S3": False}
    assert summary["deployment_metrics"]["BCT_TPGR"]["p_rank_bucket"]["0.99"]["support_compression"] == 1.0
    assert (
        summary["deployment_metrics"]["BCT_TPGR"]["m2_q_block"]["0.99"]["support_compression"]
        < summary["deployment_metrics"]["SIZE"]["m2_q_block"]["0.99"]["support_compression"]
    )
    assert (
        summary["deployment_metrics"]["BCT_TPGR"]["gray_rank_bucket"]["0.99"]["support_compression"]
        < summary["deployment_metrics"]["SIZE"]["gray_rank_bucket"]["0.99"]["support_compression"]
    )

    print(json.dumps({
        "status": "PASS",
        "carry_partition_cells_at_s3160": len(words),
        "adversarial_N": [n0, n1],
        "same_BCT": True,
        "same_TPGR": True,
        "hidden_label_digest": got,
    }, sort_keys=True))


if __name__ == "__main__":
    main()
