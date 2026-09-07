"""Original-word checks and the concrete m3 obstruction to power moments."""

from __future__ import annotations

from copy import deepcopy
from fractions import Fraction as F
import hashlib
import importlib.util
from itertools import combinations, product
import json
from math import comb
from pathlib import Path
import random

import finite_hcm_brc as consumer
from enterprise_math.brc_histogram import WeightHistogram

ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
PP_SOURCE = ROOT / "research_checks/PERFECT_PRIME_AP_RESIDUAL_MOBIUS_BERNSTEIN_COEFFICIENT_POSITIVITY_CHECK_20260903.py"


def text(q):
    q = F(q)
    return f"{q.numerator}/{q.denominator}"


def main():
    rng = random.Random(202609071)
    random_instances = prefix_checks = coefficient_checks = 0
    for d in range(7):
        for trial in range(9):
            original_beta = [F(rng.randrange(0, 8), rng.randrange(1, 9)) for _ in range(d+1)]
            words = [(word, original_beta[sum(word)]) for word in product((0, 1), repeat=d)]
            h = [sum((mass for word, mass in words if all(word[:a])), F(0)) for a in range(d+1)]
            certificate = consumer.build_certificate(h)
            assert certificate["status"] == "REALIZED"
            assert consumer.verify_certificate(h, certificate)["valid"]
            assert tuple(F(v) for v in certificate["beta"]) == tuple(original_beta)
            for r in range(d+1):
                for k in range(d-r+1):
                    kept = [mass for word, mass in words
                            if mass and all(word[:r]) and not any(word[r:r+k])]
                    observed = consumer.prefix_observation_histogram(h, r, k)
                    assert observed == WeightHistogram.from_weights(kept)
                    assert observed.total_mass == sum(((-1)**a*comb(k, a)*h[r+a] for a in range(k+1)), F(0))
                    prefix_checks += 1
            for k in range(d+1):
                marked_weights = [mass for word, mass in words if mass
                                  for _ in combinations([i for i, bit in enumerate(word) if bit == 0], k)]
                observed = consumer.coefficient_histogram(h, k)
                assert observed == WeightHistogram.from_weights(marked_weights)
                coefficient_checks += 1
            random_instances += 1

    toy = (F(1), F(1, 2), F(1, 5))
    toy_brc = consumer.build_certificate(toy)
    toy_obstruction = consumer.verify_square_obstruction(toy, (F(-1, 2), F(1)))
    assert toy_obstruction["square_readout"] == "-1/20"
    assert consumer.build_certificate((1, 1, 0))["status"] == "OBSTRUCTED"
    assert consumer.verify_square_obstruction((1, 0, 0), (0, 1))["status"] == "UNDETERMINED"
    mutation_checks = 0
    for key, replacement in (("beta", ["0/1"]*3), ("scope", "POWER_MOMENTS"),
                             ("power_moment_measure", "EXISTS"), ("status", "OBSTRUCTED")):
        damaged = deepcopy(toy_brc)
        damaged[key] = replacement
        assert not consumer.verify_certificate(toy, damaged)["valid"]
        mutation_checks += 1
    for mutate in (
        lambda c: c["layers"][0].__setitem__("j", False),
        lambda c: c["layers"][0].__setitem__("word_count", 1.0),
        lambda c: c["histogram"].__setitem__("branch_count", 4.0),
        lambda c: c["beta"].__setitem__(0, "1/0"),
        lambda c: c.__setitem__("beta", iter(c["beta"])),
        lambda c: c.__setitem__("beta", c["beta"]+["0/1"]),
    ):
        damaged = deepcopy(toy_brc)
        mutate(damaged)
        assert consumer.verify_certificate(toy, damaged)["status"] == "INVALID_CERTIFICATE"
        mutation_checks += 1
    damaged = consumer.build_certificate((1, 1, 0))
    damaged["power_moment_measure"] = "EXISTS"
    assert consumer.verify_certificate((1, 1, 0), damaged)["status"] == "INVALID_CERTIFICATE"
    mutation_checks += 1
    for bad in ((1, 0.5, 0.2), (1, True, 0)):
        try:
            consumer.build_certificate(bad)
        except TypeError:
            pass
        else:
            raise AssertionError("inexact or boolean input accepted")
    assert consumer.verify_certificate(toy, toy_brc, max_degree=1)["status"] == "UNVERIFIED"
    huge = 10**4500
    try:
        consumer.build_certificate((huge,))
    except consumer.ResourceLimit:
        pass
    else:
        raise AssertionError("oversized exact input did not report representation budget")
    assert consumer.verify_certificate((huge,), {})["status"] == "UNVERIFIED"
    damaged = deepcopy(toy_brc)
    damaged["beta"][0] = "1" + "0"*4500 + "/1"
    assert consumer.verify_certificate(toy, damaged)["status"] == "UNVERIFIED"

    spec = importlib.util.spec_from_file_location("owner_pp_original_m3", PP_SOURCE)
    pp = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(pp)
    # Only m3 is needed for the new obstruction. Do not run the old m2..10 suite.
    q = pp.q_coefficients(3)
    d = len(q)-1
    raw_h = [(-1)**a * value / comb(d, a) for a, value in enumerate(q)]
    h = [value/raw_h[0] for value in raw_h]
    certificate = consumer.build_certificate(h)
    square = consumer.verify_square_obstruction(h, (F(-3, 10), F(8, 7), F(1)))
    assert square["square_readout"] == "-7205915063/2893645755000"
    assert square["status"] == "NO_POSITIVE_POWER_MOMENT_MEASURE"
    finite_differences = [sum(((-1)**a * comb(k, a)*h[r+a] for a in range(k+1)), F(0))
                          for r in range(d+1) for k in range(d-r+1)]
    assert len(finite_differences) == 28 and min(finite_differences) > 0
    coefficients = []
    for k in range(d+1):
        actual = sum((q[a]/raw_h[0]*comb(d-a, k-a) for a in range(k+1)), F(0))
        observed = consumer.coefficient_histogram(h, k)
        assert actual == observed.total_mass > 0
        coefficients.append(dict(k=k, coefficient=text(actual),
                                 brc_histogram=consumer.histogram_record(observed)))
    payload = dict(status="PASS", random_word_ensembles=random_instances,
                   direct_word_prefix_checks=prefix_checks,
                   direct_marked_word_coefficient_checks=coefficient_checks,
                   certificate_mutations_rejected=mutation_checks,
                   source_sha256={str(PP_SOURCE.relative_to(ROOT)).replace("\\", "/"):hashlib.sha256(PP_SOURCE.read_bytes()).hexdigest(),
                       "finite_hcm_brc.py":hashlib.sha256(Path(consumer.__file__).read_bytes()).hexdigest(),
                       "run_finite_brc_checks.py":hashlib.sha256(Path(__file__).read_bytes()).hexdigest()},
                   toy=dict(h=[text(v) for v in toy], brc=toy_brc, square_obstruction=toy_obstruction),
                   actual_m3=dict(degree=d, q=[text(v) for v in q], normalization_h0=text(raw_h[0]),
                       normalized_h=[text(v) for v in h], finite_difference_cells=28,
                       all_signed_finite_differences_strict=True,
                       brc_certificate=certificate, square_obstruction=square,
                       coefficients=coefficients),
                   scope="finite BRC and one exact counterexample; all-m HCM0 remains open")
    output = HERE / "finite_brc_certificate_20260907.json"
    output.write_bytes((json.dumps(payload, ensure_ascii=False, sort_keys=True, indent=2)+"\n").encode("utf-8"))
    print(json.dumps({key:payload[key] for key in ("status", "random_word_ensembles",
        "direct_word_prefix_checks", "direct_marked_word_coefficient_checks",
        "certificate_mutations_rejected")}, sort_keys=True))
    print("m3 square obstruction:", square["square_readout"], "all 28 finite differences positive")


if __name__ == "__main__":
    main()
