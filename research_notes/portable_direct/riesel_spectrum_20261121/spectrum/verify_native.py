"""Native BRC execution of the already certified exact-cost-eight root.

This integration checks the actual pinned native update and readout paths.
It reuses the companion arithmetic certificate's prime/period/gcd results.
"""
from __future__ import annotations

import argparse
from fractions import Fraction
from hashlib import sha1, sha256
import json
from pathlib import Path
import sys

HERE = Path(__file__).resolve().parent
BASE_REL = Path("research_notes/portable_direct/riesel_mixed_20261119/certificate.json")
BASE_BLOB = "c1909a5e2e209b0f6bd5f613d0f758dde45caee9"
NATIVE_COMMIT = "b1efc6c805661ed7b476e6e730107da6043176ee"


def git_blob(data):
    return sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()


def positive_integer_digest(value):
    assert value > 0
    data = value.to_bytes((value.bit_length()+7)//8, "big", signed=False)
    return {"bit_length": value.bit_length(), "unsigned_big_endian_sha256": sha256(data).hexdigest()}


def main():
    root = next(p for p in HERE.parents if (p/BASE_REL).is_file())
    source_default = next(p for p in (root/"src", root/"vendor_src")
                          if (p/"enterprise_math/brc_transport.py").is_file())
    parser = argparse.ArgumentParser()
    parser.add_argument("--source-dir", type=Path, default=source_default)
    parser.add_argument("--arithmetic-certificate", type=Path,
                        default=HERE/"small_spectrum_certificate.json")
    parser.add_argument("--output", type=Path, default=HERE/"native_certificate.json")
    args = parser.parse_args()
    sys.set_int_max_str_digits(0)

    base_bytes = (root/BASE_REL).read_bytes()
    assert git_blob(base_bytes) == BASE_BLOB
    base = json.loads(base_bytes)
    assert base["project_source_commit"] == NATIVE_COMMIT
    source_checks = []
    for filename, expected in base["project_source_blobs"].items():
        actual = git_blob((args.source_dir/"enterprise_math"/filename).read_bytes())
        assert actual == expected
        source_checks.append({"module": filename, "expected_blob": expected, "actual_blob": actual})
    assert len(source_checks) == 4

    certificate_bytes = args.arithmetic_certificate.read_bytes()
    certificate = json.loads(certificate_bytes)
    numeric = certificate["numeric_cost_8"]
    rows = certificate["seeds"][3]["rows"]
    assert len(rows) == numeric["additional_cost"] == 8
    old = certificate["old_rows"]
    a = int(numeric["root_hex"], 16)
    astar = int(certificate["a_star"])
    assert astar == int(base["optimized"]["a"])
    assert sha256(str(a).encode()).hexdigest() == numeric["root_decimal_sha256"]
    assert (a-astar) % (2*int(certificate["M"])) == 0
    indices = numeric["private_indices"]
    channels = [r[0] for r in old]+[r["p"] for r in rows]
    assert len(indices) == len(set(indices)) == len(channels) == 28
    assert max(indices) == 1040

    sys.path.insert(0, str(args.source_dir))
    from enterprise_math.brc_transport import Affine, EffectHistogram, euclidean_digits

    step = EffectHistogram.from_terms(1, [(1, Affine(((2,),), (1,)), 1)])
    assert step.entries == ((Fraction(1), Affine(((2,),), (1,)), 1),)
    twice = step.then(step)
    assert twice.entries == ((Fraction(1), Affine(((4,),), (3,)), 1),)

    def advance(packet, value):
        (point, weight), = packet.evaluate((value,)).items()
        assert weight.entries == ((Fraction(1), 1),)
        assert point[0].denominator == 1
        return int(point[0])

    assert advance(step, -1) == advance(twice, -1) == -1
    x = a*a-1
    selected = {}
    nset = set(indices)
    for n in range(1, max(indices)+1):
        x = advance(step, x)
        assert x == (a*a << n)-1
        if n in nset:
            selected[n] = x

    witnesses = []
    old_projection_count = 0
    all_projection_count = 0
    for assigned, n in zip(channels, indices):
        value = selected[n]
        hits = []
        old_readouts = []
        for q in channels:
            quotient, digits = euclidean_digits(value, (q,))
            residual, = digits
            assert quotient*q+residual == value and 0 <= residual < q
            all_projection_count += 1
            if residual == 0:
                hits.append(q)
            if q in channels[:20]:
                expected = (astar*astar*pow(2, n, q)-1) % q
                assert residual == expected
                old_projection_count += 1
                old_readouts.append([q, residual])
        assert hits == [assigned] and 1 < assigned < value
        witnesses.append({"n": n, "assigned_prime": assigned, "cover_hits": hits,
                          "old_readouts": old_readouts, **positive_integer_digest(value)})
    assert old_projection_count == 560 and all_projection_count == 784
    assert all(all(residual for _, residual in w["old_readouts"]) for w in witnesses[20:])

    result = {
        "schema": "riesel-small-spectrum-native-integration-v1",
        "status": "AUTHOR_NATIVE_EXECUTION_CHECK; NOT_INDEPENDENT_REVIEW",
        "native_source_commit": NATIVE_COMMIT,
        "native_source_blobs": source_checks,
        "base_certificate_git_blob": BASE_BLOB,
        "arithmetic_certificate_sha256": sha256(certificate_bytes).hexdigest(),
        "root_decimal_sha256": numeric["root_decimal_sha256"],
        "root_decimal_digits": numeric["root_decimal_digits"],
        "native_update": "EffectHistogram.from_terms(1, [(1, Affine(((2,),), (1,)), 1)])",
        "update_count": max(indices),
        "every_update_equals_closed_form": True,
        "weight": "1", "multiplicity": 1,
        "selected_terms": len(witnesses),
        "euclidean_digit_projections": all_projection_count,
        "old_projection_equalities": old_projection_count,
        "selected_private_terms": witnesses,
        "term_digest_encoding": "Minimal-length unsigned big-endian bytes for each positive integer.",
        "arithmetic_reuse": "The 378 pairwise-gcd identities, trial-division primality and complete-period coverage remain in the unchanged arithmetic certificate; exact equality of each native term to its arithmetic value is checked here.",
        "native_scope": "Fixed X6 anchor; scalar typed integer register; prime channels are readouts, not spatial axes; index n labels updates, not physical time."
    }
    args.output.write_text(json.dumps(result, ensure_ascii=False, indent=2)+"\n")
    print(json.dumps({"output": str(args.output), "native_updates": max(indices),
                      "selected_terms": len(witnesses), "old_readouts": old_projection_count,
                      "all_readouts": all_projection_count, "source_blob_checks": len(source_checks)}))


if __name__ == "__main__":
    main()
