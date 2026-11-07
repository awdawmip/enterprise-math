"""Four prescribed small examples: square completion versus original splitting.

No multiplier search, factor search, external input, or arbitrary-modulus CLI.
The queried moduli and multipliers are literals below 2**16. Known prime labels
are used only to audit returned arithmetic, not as witness-function arguments.
"""
import hashlib
import json
import math
import sys
from dataclasses import asdict
from pathlib import Path

HERE = Path(__file__).resolve().parent
CHECKOUT = HERE / "native-root-checkout"
OUT = HERE / "brc_multiplier_trap_certificate_20260915.json"
PARENT = "52b8b2345048f602e4b7f6f75af8867d2c1276f9"
SOURCES = {
    "brc_multiplier_basin.py": "4d03ded19b38f5aa13d3e873e911205d35be5c5f",
    "brc_square_gap_prefilter.py": "42d4e9a397b56d9d371f034780ffc736d43e6d96",
    "core.py": "2b7ab070868ef4a2b6d8b33f5e3bc69dbac62c07",
}
CASES = (
    ("baseline", 43423, 1, (173, 251), False, False),
    ("useful_prescribed_multiplier", 43423, 35, (173, 251), True, True),
    ("same_lengths_same_multiplier_miss", 32881, 35, (131, 251), False, False),
    ("forced_closure_without_original_split", 43423, 43425, (173, 251), True, False),
)


def main():
    if OUT.exists():
        raise RuntimeError("preserve the already recorded certificate")
    for name, expected in SOURCES.items():
        raw = (CHECKOUT / "src/enterprise_math" / name).read_bytes()
        raw = raw.replace(b"\r\n", b"\n").rstrip(b"\n") + b"\n"
        found = hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()
        if found != expected:
            raise ValueError((name, found, expected))
    prime_table = HERE / "brc_equal_bit_product_observers_20260909.json"
    saved = prime_table.read_bytes()
    expected_hash = "121b51c4b82f62d6bdddc9a25412ed45d7c7275f92b0008605beca4445d6857e"
    if hashlib.sha256(saved).hexdigest() != expected_hash:
        raise ValueError("saved exact small-prime table changed")
    known_primes = set(json.loads(saved)["cohorts"][0]["primes"])
    sys.path.insert(0, str(CHECKOUT / "src"))
    from enterprise_math.brc_multiplier_basin import point_cost_state
    from enterprise_math.brc_square_gap_prefilter import ceiling_completion_square_witness
    rows = []
    for label, n, m, pair, expect_closure, expect_split in CASES:
        p, q = pair
        if not (1 < n < 2**16 and 0 < m < 2**16 and n*m < 2**32):
            raise ValueError("outside the fixed small-example domain")
        assert p in known_primes and q in known_primes
        assert p*q == n and p.bit_length() == q.bit_length() == 8
        assert n.bit_length() == 16 and math.gcd(n, m) == 1
        state = point_cost_state(n, m)
        witness = ceiling_completion_square_witness(n, m)
        assert (witness is not None) == expect_closure
        row = dict(id=label, N=n, multiplier=m, known_prime_pair=list(pair),
            factor_bits=[8, 8], N_bits=16, state=asdict(state),
            direction="D" if state.subtraction_cost < state.addition_cost else "U",
            immediate_square_closure=witness is not None,
            witness=list(witness) if witness is not None else None)
        parts, gcds = [], []
        if witness is not None:
            h, b = witness
            parts = [h-b, h+b]
            assert parts[0]*parts[1] == m*n
            gcds = [math.gcd(x, n) for x in parts]
        proper = sorted({g for g in gcds if 1 < g < n})
        assert bool(proper) == expect_split
        if proper:
            assert proper == sorted(pair) and proper[0]*proper[1] == n
        row.update(parts_of_multiplier_product=parts, original_modulus_gcds=gcds,
            original_factor_split=bool(proper))
        rows.append(row)
    assert rows[1]["parts_of_multiplier_product"] == [7*173, 5*251]
    assert rows[3]["multiplier"] == rows[3]["N"]+2
    result = dict(schema="BRC_MULTIPLIER_TRAP_CERTIFICATE_V1",
        canonical_sha="e26a169a2fec4af96be6c7860bab1e47fbb5f082", project_parent=PARENT,
        activity_id="RA-EM-HME-0CE4FD-SEMIPRIME-20260909", source_blobs=SOURCES,
        prime_table_sha256=expected_hash,
        scope=dict(prescribed_examples=4, unique_original_moduli=2,
            multiplier_search=False, external_inputs=0, public_RSA_inputs=0,
            timing_claim=False, population_probability_claim=False,
            multiplier_selection="literal illustrative choices; no guarantee derived from bit lengths"),
        rows=rows, all_assertions_pass=True)
    OUT.write_bytes((json.dumps(result, indent=2, ensure_ascii=True)+"\n").encode())
    print(json.dumps(result, ensure_ascii=True))


if __name__ == "__main__":
    main()
