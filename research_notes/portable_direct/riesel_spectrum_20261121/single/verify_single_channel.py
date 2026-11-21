"""Exact one-channel classification and an exact (delta,tau)=(1,21) root.

The universal classification is proved in proof.md.  This file checks the
finite old observer, constructs the complete CRT progression, and evaluates
its private witnesses through the pinned native positive BRC packet.
"""
from __future__ import annotations

import argparse
from fractions import Fraction
from hashlib import sha1, sha256
from itertools import combinations
import json
from math import gcd, lcm, prod
from pathlib import Path
import sys

HERE = Path(__file__).resolve().parent
BASE = Path("research_notes/portable_direct/riesel_mixed_20261119/certificate.json")
ROOT = next(p for p in HERE.parents if (p / BASE).is_file())
PIN = "b1efc6c805661ed7b476e6e730107da6043176ee"


def blob(data: bytes) -> str:
    return sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()


def strip(value: int, primes: list[int]) -> tuple[int, dict[str, int]]:
    removed = {}
    for p in primes:
        exponent = 0
        while value % p == 0:
            value //= p
            exponent += 1
        if exponent:
            removed[str(p)] = exponent
    return value, removed


def integer_summary(value: int) -> dict:
    raw = value.to_bytes((value.bit_length() + 7) // 8, "big")
    return {"bit_length": value.bit_length(),
            "decimal_digits": len(str(value)),
            "unsigned_big_endian_sha256": sha256(raw).hexdigest()}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source-dir", type=Path)
    parser.add_argument("--output", type=Path, default=HERE / "single_channel_certificate.json")
    args = parser.parse_args()
    sys.set_int_max_str_digits(0)
    source = args.source_dir or next(p for p in (ROOT / "src", ROOT / "vendor_src")
                                    if (p / "enterprise_math/brc_transport.py").is_file())
    old_data = (ROOT / BASE).read_bytes()
    old = json.loads(old_data)
    assert old["project_source_commit"] == PIN
    source_checks = {}
    for filename, expected in old["project_source_blobs"].items():
        observed = blob((source / "enterprise_math" / filename).read_bytes())
        assert observed == expected
        source_checks[filename] = observed
    rows = old["optimized"]["rows"]
    a_star = int(old["optimized"]["a"])
    P = [r["p"] for r in rows]
    M = prod(P)
    period = lcm(*(r["order"] for r in rows))
    assert period == 6720 and len(P) == 20 and 3 not in P
    assert a_star % 3 == 0 and gcd(2 * M, 3) == 1

    def old_hits(n: int) -> list[int]:
        return [r["p"] for r in rows if n % r["order"] == r["exponent_phase"]]

    # Full-period verification distinguishes the periodic old-hole set from a prefix.
    holes = {u for u in range(105) if not old_hits(2 * u)}
    assert len(holes) == 36 and {0, 1}.issubset(holes)
    assert all(old_hits(n) for n in range(1, period, 2))
    assert all((not old_hits(2 * u)) == (u % 105 in holes) for u in range(period // 2))
    assert not old_hits(210) and not old_hits(212)
    assert (1 << (212 - 210)) - 1 == 3

    witnesses = [{"prime": p, "n": next(n for n in range(1, period, 2)
                                         if old_hits(n) == [p])} for p in P]
    witnesses.append({"prime": 3, "n": 2})
    primes = P + [3]
    indices = [w["n"] for w in witnesses]
    assert len(set(indices)) == 21
    D = lcm(*((1 << abs(n - m)) - 1 for n, m in combinations(indices, 2)))
    E, removed = strip(D, primes)
    modulus = 2 * M
    # First impose the old root class and a=1 mod3, then force E|a.
    b = a_star + modulus * (((1 - a_star) * pow(modulus, -1, 3)) % 3)
    K = 3 * modulus
    assert gcd(E, K) == 1
    a = E * ((b * pow(E, -1, K)) % K)
    progression_modulus = E * K
    assert 0 < a < progression_modulus and a % modulus == a_star
    assert a % 3 == 1 and a % E == 0 and 2 * a * a - 1 > max(primes)

    sys.path.insert(0, str(source))
    from enterprise_math.brc_transport import Affine, EffectHistogram
    packet = EffectHistogram.from_terms(1, [(1, Affine(((2,),), (1,)), 1)])
    assert packet.then(packet).entries == ((Fraction(1), Affine(((4,),), (3,)), 1),)
    value = a * a - 1
    terms = {}
    for n in range(1, max(indices) + 1):
        ((point, weights),) = packet.evaluate((value,)).items()
        assert weights.entries == ((Fraction(1), 1),) and point[0].denominator == 1
        value = int(point[0])
        if n in indices:
            assert value == (a * a << n) - 1
            terms[n] = value
    for w in witnesses:
        n, p = w["n"], w["prime"]
        assert [q for q in primes if terms[n] % q == 0] == [p]
        assert 1 < p < terms[n]
        w.update(integer_summary(terms[n]))
    gcds = []
    for n, m in combinations(indices, 2):
        g = gcd(terms[n], terms[m])
        assert g == 1
        gcds.append({"n1": n, "n2": m, "gcd": g})
    for n in range(period):
        assert old_hits(n) or n % 2 == 0
    assert all((a * a * pow(2, r["exponent_phase"], r["p"]) - 1) % r["p"] == 0
               for r in rows)

    # Parameter t in a=a_star+2Mt is periodic mod3.  Exactly two classes need one channel.
    t_classes = [{"t_mod3": t, "a_mod3": (a_star + modulus * t) % 3,
                  "delta_is_one": (a_star + modulus * t) % 3 != 0} for t in range(3)]
    assert sum(c["delta_is_one"] for c in t_classes) == 2
    result = {
        "schema": "enterprise-math.riesel-single-extra-channel.v1",
        "researcher_id": "EM-DIRECT-970E1C",
        "research_activity_id": "RA-D2EC212845B63844081F9A14",
        "status": "Author proof and exact arithmetic verification; not independent project Review",
        "native_source_commit": PIN, "native_source_blobs": source_checks,
        "base_certificate_sha256": sha256(old_data).hexdigest(),
        "a_star": str(a_star), "M": str(M), "P": P,
        "old_holes_u_mod105": sorted(holes), "old_full_period_n": period,
        "one_channel_necessity_witness_indices": [210, 212],
        "one_channel_necessary_prime": 3,
        "classification": "For every positive odd a=a_star mod2M, delta_P(a)=1 iff 3 does not divide a; delta_P(a)=0 never occurs.",
        "relative_density": {"numerator": 2, "denominator": 3, "parameter_classes": t_classes},
        "numeric": {"root_a_hex": hex(a), "root_progression_modulus_hex": hex(progression_modulus),
                    "root_summary": integer_summary(a), "crt_b": str(b), "crt_K": str(K),
                    "D_summary": integer_summary(D), "E_summary": integer_summary(E),
                    "D_removed_prime_valuations": removed, "witnesses": witnesses,
                    "all_pairwise_gcds": gcds, "exact_delta_P": 1, "exact_total_tau": 21,
                    "full_cover_period_n": period, "native_steps": max(indices)},
        "integer_hash_encoding": "Minimal unsigned big-endian bytes; no length prefix or sign byte",
        "native_semantics": "Fixed X6 anchor; positive singleton BRC x->2x+1 with weight=multiplicity=1; integer index is not physical time; prime channels are not spatial axes"
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps({"verified": True, "root_decimal_digits": result["numeric"]["root_summary"]["decimal_digits"],
                      "delta_P": 1, "tau": 21, "pairwise_gcd_checks": len(gcds),
                      "full_period": period, "native_steps": max(indices), "output": str(args.output)}, indent=2))


if __name__ == "__main__":
    main()
