#!/usr/bin/env python3
"""New finite checks for the parameter-uniform moving-thickness return theorem.

Reads immutable predecessor constants and its integer-interval helper.  It does
not invoke any predecessor main program or rerun a predecessor certificate.
All pass/fail decisions use exact fractions or outward integer intervals.
"""

from fractions import Fraction as F
from pathlib import Path
from math import isqrt
import argparse
import hashlib
import importlib.util
import json
import sys

sys.dont_write_bytecode = True


EXPECTED = {
    "certify_fast_harmonic_energy.py":
        "d1c3201cfe08d770d3b7de48548b7ab575860c984fa823ce9e9ba42765be1377",
    "three_thickness_certificate.json":
        "eb8b302704d4de371dcccd1632332fec9cf6851a6c1c3ab94a2f780c92256d78",
    "log_energy_constants_certificate.json":
        "6346dc7b31527954311caf5d4e6a1c7ca48866c0b2bfa075e5f8ba21780f7733",
    "FIXED_SHIFTED_ROADS_AND_RETURN_COST.md":
        "8e646543ee2519eaaf059085af87441074567c4f4a986d9c63481d2b8b5e60ab",
    "LOGARITHMIC_RETURN_ENERGY.md":
        "c5db488bea5dee89d6f861e8db0f92d237e3e7c57749609e832d360b56454633",
}


def find_pinned(previous, basename):
    matches = list(previous.rglob(basename))
    assert len(matches) == 1, (basename, len(matches))
    path = matches[0]
    digest = hashlib.sha256(path.read_bytes()).hexdigest()
    assert digest == EXPECTED[basename], (basename, digest)
    return path


def mobius_and_factors(limit):
    factors = [[] for _ in range(limit + 1)]
    mu = [1] * (limit + 1)
    mu[0] = 0
    for p in range(2, limit + 1):
        if factors[p]:
            continue
        for n in range(p, limit + 1, p):
            factors[n].append(p)
            mu[n] *= -1
        for n in range(p * p, limit + 1, p * p):
            mu[n] = 0
    return mu, factors


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--previous", required=True, type=Path)
    parser.add_argument("--output", type=Path,
                        default=Path(__file__).with_name(
                            "uniform_moving_return_certificate.json"))
    args = parser.parse_args()
    previous = args.previous.resolve()
    paths = {name: find_pinned(previous, name) for name in EXPECTED}

    spec = importlib.util.spec_from_file_location(
        "moving_return_interval_helper", paths["certify_fast_harmonic_energy.py"])
    iv = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(iv)
    scale = iv.S

    def inv(x):
        assert x[0] > 0
        return scale * scale // x[1], iv.ceildiv(scale * scale, x[0])

    def sqrt_iv(x):
        assert x[0] >= 0
        lo = isqrt(x[0] * scale)
        hi = isqrt(x[1] * scale)
        hi += hi * hi < x[1] * scale
        return lo, hi

    def div(x, y):
        return iv.mul(x, inv(y))

    regular = json.loads(paths["three_thickness_certificate.json"].read_text())
    old = json.loads(paths["log_energy_constants_certificate.json"].read_text())
    assert regular["status"] == old["status"] == "PASS"
    gamma = iv.decode(regular["regular_constants"]["gamma"])
    log_two = iv.decode(old["constants"]["log_2"])
    variance = iv.decode(old["constants"]["V_simple_zero_baseline"])
    one_sided = iv.decode(old["constants"]["one_sided_logarithmic_floor"])
    assert gamma[0] > scale // 2 and gamma[1] < scale
    assert log_two[1] * 4 < 3 * scale
    assert variance[0] > 0 and one_sided[0] > 0

    # Exact Mobius convolution and the bounded 1/d partial sums.
    limit = 512
    mu, factors = mobius_and_factors(limit)
    s_one = [F(0)]
    convolution_checks = 0
    for n in range(1, limit + 1):
        assert sum(mu[d] * (n // d) for d in range(1, n + 1)) == 1
        convolution_checks += 1
        s_one.append(s_one[-1] + F(mu[n], n))
        assert abs(s_one[-1]) <= 1

    # Exact finite Abel identities for a = 1, 2, 3, 4.
    abel_checks = 0
    for a in (1, 2, 3, 4):
        direct = F(0)
        variation = F(0)
        for n in range(1, limit + 1):
            direct += F(mu[n], n ** a)
            multiplier = F(1, n ** (a - 1))
            if n > 1:
                old_multiplier = F(1, (n - 1) ** (a - 1))
                variation += s_one[n - 1] * (old_multiplier - multiplier)
            assert direct == s_one[n] * multiplier + variation
            assert abs(direct) <= 1
            abel_checks += 1

    # Fractional a = 1/2, 3/4, 3/2: interval bounds, including increasing
    # and decreasing Abel multipliers.  No floating exponent evaluations.
    fractional_sums = {"1/2": iv.ZERO, "3/4": iv.ZERO, "3/2": iv.ZERO}
    fractional_checks = 0
    for n in range(1, limit + 1):
        sqn = sqrt_iv(iv.rat(n))
        qrn = sqrt_iv(sqn)
        powers = {
            "1/2": inv(sqn),
            "3/4": inv(sqrt_iv(sqrt_iv(iv.rat(n ** 3)))),
            "3/2": inv(iv.qmul(sqn, n)),
        }
        bounds = {
            "1/2": iv.sub(iv.qmul(sqn, 2), iv.ONE),
            "3/4": iv.sub(iv.qmul(qrn, 2), iv.ONE),
            "3/2": iv.ONE,
        }
        for name in fractional_sums:
            fractional_sums[name] = iv.add(
                fractional_sums[name], iv.qmul(powers[name], mu[n]))
            value = fractional_sums[name]
            # Using the lower endpoint of a positive bound certifies the
            # stronger inclusion for the whole computed source interval.
            assert max(abs(value[0]), abs(value[1])) <= bounds[name][0]
            fractional_checks += 1

    # Noninteger floor phases in the complete harmonic kernel.
    harmonics = [F(0)]
    for n in range(1, 129):
        harmonics.append(harmonics[-1] + F(1, n))
    offsets = tuple(map(F, ["0", "1/16", "1/8", "1/4", "1/2",
                           "3/4", "7/8", "15/16"]))
    kernel_checks = 0
    max_scaled_error_upper = F(0)
    for n in range(1, 129):
        for offset in offsets:
            z = F(n) + offset
            kernel = z * harmonics[n] - n
            log_z = iv.sub(iv.log_int(z.numerator), iv.log_int(z.denominator))
            leading = iv.qmul(iv.sub(iv.add(log_z, gamma), iv.ONE), z)
            error = iv.sub(iv.sub(iv.rat(kernel), leading), iv.rat(F(1, 2)))
            absolute_upper = F(max(abs(error[0]), abs(error[1])), scale)
            assert absolute_upper <= 1 / z
            max_scaled_error_upper = max(max_scaled_error_upper, z * absolute_upper)
            kernel_checks += 1

    # Actual complete D_a, including all composite source values and the
    # exact unit correction.  These finite identities are entirely rational.
    product_checks = 0
    road_checks = 0
    for a in (1, 2, 3, 4):
        source = [F(0)] * 33
        for n in range(2, 33):
            product = F(1, a)
            for p in factors[n]:
                product *= 1 - F(1, p ** a)
            divisor_sum = sum((F(mu[d], a * d ** a)
                               for d in range(1, n + 1) if n % d == 0), F(0))
            assert product == divisor_sum
            source[n] = product
            product_checks += 1
        for n in range(1, 33):
            for offset in (F(0), F(1, 4), F(1, 2), F(3, 4)):
                y = F(n) + offset
                direct = sum(((y / k - 1) * source[k]
                              for k in range(2, n + 1)), F(0))
                transformed = -(y - 1) / a
                for d in range(1, n + 1):
                    z = y / d
                    floor_z = z.numerator // z.denominator
                    kernel = z * harmonics[floor_z] - floor_z
                    transformed += F(mu[d], a * d ** a) * kernel
                assert direct == transformed
                road_checks += 1

    # Explicit uniform constants and lambda=2 coefficient floors.
    h_one = iv.sub(iv.add(iv.rat(F(13, 2)), iv.qmul(log_two, 2)),
                   iv.qmul(gamma, 2))
    common = iv.sub(iv.add(iv.ONE, log_two), gamma)
    two_three_quarters = sqrt_iv(sqrt_iv(iv.rat(8)))
    h_three_quarters = iv.add(
        iv.rat(F(5, 2)),
        iv.mul(two_three_quarters,
               iv.add(iv.qmul(common, F(4, 3)), iv.rat(F(16, 9)))))
    assert h_one[1] < 7 * scale
    assert F(h_three_quarters[1], scale) < F(169, 18)
    constants = {
        "H_1": iv.record(h_one),
        "H_3_over_4": iv.record(h_three_quarters),
        "H_1_rational_upper": "7",
        "H_3_over_4_rational_upper": "169/18",
    }
    floors = {}
    for alpha, h_alpha in ((F(1), h_one), (F(3, 4), h_three_quarters)):
        label = str(alpha)
        floors[label] = {}
        for direction, spectral in (("absolute", variance), ("one_fixed_sign", one_sided)):
            m_floor = div(sqrt_iv(iv.qmul(spectral, 2 * alpha - 1)), h_alpha)
            w_floor = iv.qmul(m_floor, alpha)
            floors[label][direction] = {
                "M_normalization": "A^(alpha-1/2)*sqrt(log(A))",
                "M_required_limsup_floor": iv.record(m_floor),
                "W_required_limsup_floor": iv.record(w_floor),
            }

    # Exact sparse witness: n_k = 2^(4^k), b_(n_k) = 4^(2k).
    # At A_k = 2*n_k and lambda=2, the entire window is between supports.
    sparse_witness = []
    cumulative_mass = 0
    last_ratio = F(0)
    for k in range(1, 6):
        exponent = 4 ** k
        cumulative_mass += 4 ** (2 * k)
        prefix_ratio_over_log_two = F(cumulative_mass, exponent)
        assert prefix_ratio_over_log_two > last_ratio
        last_ratio = prefix_ratio_over_log_two
        start_exponent = exponent + 1
        end_exponent = 2 * start_exponent
        next_support_exponent = 4 ** (k + 1)
        assert exponent < start_exponent <= end_exponent < next_support_exponent
        sparse_witness.append({
            "k": k,
            "support_binary_exponent": exponent,
            "closed_window_binary_exponents": [start_exponent, end_exponent],
            "next_support_binary_exponent": next_support_exponent,
            "window_mass": "0",
            "prefix_energy_div_log_N_times_log_2": str(prefix_ratio_over_log_two),
        })

    result = {
        "status": "PASS",
        "researcher_id": "EM-DIRECT-E7559A / TASK_RESEARCH",
        "activity": "RA-D2F111EA1C0D4B1DBEFBC1B4",
        "review_status": "author finite verification; not independent Review or formal Result",
        "arithmetic": "exact fractions and outward integer intervals; no floating-point pass/fail",
        "checks": {
            "mobius_floor_convolutions": convolution_checks,
            "mobius_reciprocal_partial_sums": limit,
            "integer_thickness_Abel_identities_and_bounds": abel_checks,
            "fractional_thickness_partial_sum_bounds": fractional_checks,
            "harmonic_floor_phase_points": kernel_checks,
            "complete_source_product_divisor_identities": product_checks,
            "complete_Mobius_harmonic_road_identities": road_checks,
            "empty_power_window_sparse_witnesses": len(sparse_witness),
        },
        "harmonic_kernel_scaled_absolute_error_upper":
            iv.record(iv.rat(max_scaled_error_upper)),
        "uniform_constants": constants,
        "lambda_2_necessary_coefficient_floors": floors,
        "sparse_sequence_quantifier_witness": sparse_witness,
        "dependencies": [
            {"path": str(paths[name].relative_to(previous)), "sha256": EXPECTED[name]}
            for name in EXPECTED
        ],
        "scope": {
            "new_zeta_or_zero_evaluations": 0,
            "new_reference_road_values": 0,
            "new_prime_or_mobius_sieve_limit": limit,
            "integer_thickness_source_geometry":
                "a in {1,2,3,4}; y=N+r/4 with 1<=N<=32 and 0<=r<=3",
            "fractional_thicknesses": ["1/2", "3/4", "3/2"],
            "harmonic_floor_phase_geometry":
                "z=N+r; 1<=N<=128; r in {0,1/16,1/8,1/4,1/2,3/4,7/8,15/16}",
            "unbounded_claims": "analytic proofs in the accompanying note, not finite extrapolation",
            "necessary_cost": "not an approximation construction at or above the threshold",
            "limsup_quantifier": "all integer starts or any bounded-ratio integer grid; not arbitrary sparse starts",
            "predecessor_main_programs_executed": False,
        },
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2, ensure_ascii=False) + "\n")
    print(json.dumps({"status": "PASS", "checks": result["checks"],
                      "output": str(args.output)}, ensure_ascii=False))


if __name__ == "__main__":
    main()
