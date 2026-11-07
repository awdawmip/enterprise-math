"""Two prescribed toy checks of the user's paired hidden-prime construction.

Construction explicitly uses known p,q. Recovery receives only N, KL and c.
This verifies a conditional identity; it is not an N-only RSA construction.
No external modulus or factor-search CLI is supplied.
"""
import hashlib
import importlib.util
import json
import math
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE / "native-root-checkout"
OUT = HERE / "brc_paired_hidden_prime_traps_20260915.json"
CASES = ((149, 251, 5), (139, 241, 7))
PINS = {
    "core.py": "2b7ab070868ef4a2b6d8b33f5e3bc69dbac62c07",
    "brc_multiplier_basin.py": "4d03ded19b38f5aa13d3e873e911205d35be5c5f",
    "brc_square_gap_prefilter.py": "42d4e9a397b56d9d371f034780ffc736d43e6d96",
}


def checked(path, expected):
    b = path.read_bytes().replace(b"\r\n", b"\n").rstrip(b"\n")+b"\n"
    assert hashlib.sha1(b"blob "+str(len(b)).encode()+b"\0"+b).hexdigest() == expected


def main():
    if OUT.exists():
        raise RuntimeError("preserve the existing paired-construction observations")
    for name, blob in PINS.items():
        checked(ROOT / "src/enterprise_math" / name, blob)
    residual_source = HERE / "brc_residual_candidate_families_20260908.py"
    checked(residual_source, "e8ea67310094c517b5a882d5e2e1709be975c675")
    prime_bytes = (HERE / "brc_equal_bit_product_observers_20260909.json").read_bytes()
    assert hashlib.sha256(prime_bytes).hexdigest() == "121b51c4b82f62d6bdddc9a25412ed45d7c7275f92b0008605beca4445d6857e"
    primes = {p for cohort in json.loads(prime_bytes)["cohorts"] for p in cohort["primes"]}
    sys.path.insert(0, str(ROOT / "src"))
    from enterprise_math.core import integer_nth_root
    from enterprise_math.brc_multiplier_basin import point_cost_state
    from enterprise_math.brc_square_gap_prefilter import ceiling_completion_square_witness as witness
    spec = importlib.util.spec_from_file_location("fixed_residual_packet", residual_source)
    packet = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(packet)
    packet.ROOT = integer_nth_root

    def recover(n, paired_product, c):
        # Deliberately no p,q inputs here. Their use in construction is recorded below.
        found = witness(paired_product, 1)
        assert found is not None
        h, z = found
        p1, r1 = divmod(h-z-4*n, c)
        q1, r2 = divmod(h+z-4*n, c)
        assert r1 == r2 == 0 and 1 < p1 < q1 and p1*q1 == n
        return dict(H=h, z=z, recovered=[p1, q1],
                    cross_parts=[h-z, h+z], gcds=[math.gcd(h-z, n), math.gcd(h+z, n)])

    rows = []
    for p, q, c in CASES:
        n, s = p*q, p+q
        a, b = 4*p+c, 4*q+c
        assert p < q < 2*p and n < 2**16
        assert {p, q, a, b} <= primes
        k, ell = a*p, b*q
        assert packet._complete(k)[0] == p and packet._complete(ell)[0] == q
        scalar = a*b
        m = k*ell
        user_product = m*n
        assert m == scalar*n and user_product == scalar*n*n
        assert scalar == 16*n+4*c*s+c*c
        cross = [4*n+c*p, 4*n+c*q]
        assert math.prod(cross) == m
        recovered = recover(n, m, c)
        assert recovered["recovered"] == [p, q] and recovered["cross_parts"] == cross
        quotient, remainder = divmod(user_product, n)
        assert remainder == 0 and quotient == m
        assert recover(n, quotient, c) == recovered
        computed_s, rem = divmod(scalar-16*n-c*c, 4*c)
        assert rem == 0 and computed_s == s

        base = point_cost_state(n, 1)
        h0 = base.target_root+1
        gap0 = base.addition_cost
        scalar0 = 16*n+8*c*h0+c*c
        m0 = n*scalar0
        x0 = 4*n+c*h0
        expected_gap = c*c*gap0
        assert x0*x0-m0 == expected_gap and 0 < expected_gap < 2*x0-1
        raw_base = witness(n, 1)
        raw_surrogate = witness(m0, 1)
        assert (raw_base is None) == (raw_surrogate is None)
        assert raw_base is None and scalar0 != scalar
        assert integer_nth_root(m0, 2)+1 == x0

        rows.append(dict(p=p, q=q, N=n, c=c, a=a, b=b, K=k, L=ell,
            K_factor_bits=[p.bit_length(), a.bit_length()],
            L_factor_bits=[q.bit_length(), b.bit_length()],
            both_K_L_semiprime_labels_exact=True,
            both_original_residual_shortcuts_pass=True,
            construction_inputs_include_hidden_factors=["p", "q"],
            actual_scalar_ab=scalar, user_m_KL=m, user_mN=user_product,
            recovery_from_KL=recovered, recovery_from_user_mN_after_dividing_N=recovered,
            direct_first_completion_on_user_mN=witness(user_product, 1),
            residual_packet_factor_on_user_mN=packet._complete(user_product)[0],
            sum_recovered_from_numeric_ab=computed_s,
            N_only_surrogate=dict(H0=h0, A0=gap0, scalar_ab_surrogate=scalar0,
                product=m0, completion_root=x0, completion_gap=expected_gap,
                original_first_completion=raw_base, transformed_first_completion=raw_surrogate,
                exact_paired_product=False)))
    result = dict(schema="BRC_PAIRED_HIDDEN_PRIME_TRAPS_V1",
        canonical_sha="73282863250128a33c0473202f90b2b801e93fc1",
        project_parent="7ea1f5e5b9d1cecf2eaa3deb861000e5662055c3",
        activity_id="RA-EM-HME-0CE4FD-SEMIPRIME-20260909", source_blobs=PINS,
        residual_source_blob="e8ea67310094c517b5a882d5e2e1709be975c675",
        scope=dict(prescribed_toy_cases=2, public_RSA_queries=0, factor_search=False,
            multiplier_search=False, N_only_exact_constructor_established=False,
            clarification_resolved="K=ap,L=bq,m=KL; output sought is original p,q"),
        rows=rows, all_checks_pass=True)
    OUT.write_bytes((json.dumps(result, indent=2, ensure_ascii=True)+"\n").encode())
    print(json.dumps(result, ensure_ascii=True))


if __name__ == "__main__":
    main()
