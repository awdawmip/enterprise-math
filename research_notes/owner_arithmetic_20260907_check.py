"""Independent factorial/full-signed-endpoint census; no carry formula oracle."""

from collections import Counter
from itertools import product
from math import comb, factorial, prod
from pathlib import Path
import json

from owner_arithmetic_20260907 import (
    ComputationBudgetExceeded,
    signed_valuation_spectrum,
)


def compositions(total, width):
    if width == 0:
        if total == 0:
            yield ()
    elif width == 1:
        yield (total,)
    else:
        for first in range(total + 1):
            for rest in compositions(total - first, width - 1):
                yield (first,) + rest


def valuation(value, prime):
    exponent = 0
    while value % prime == 0:
        value //= prime
        exponent += 1
    return exponent


def shell_size(radius):
    if radius == 0:
        return 1
    return sum(2**r * comb(6, r) * comb(radius - 1, r - 1)
               for r in range(1, min(6, radius) + 1))


def direct_signed(radius, primes):
    factorials = [factorial(i) for i in range(radius + 1)]
    counts = {prime: Counter() for prime in primes}
    joint = {prime: Counter() for prime in primes}
    endpoints = 0
    for magnitudes in compositions(radius, 6):
        for endpoint in product(*[(-a, a) if a else (0,) for a in magnitudes]):
            assert sum(map(abs, endpoint)) == radius
            multiplicity = factorials[radius] // prod(factorials[abs(z)] for z in endpoint)
            active = sum(z != 0 for z in endpoint)
            endpoints += 1
            for prime in primes:
                exponent = valuation(multiplicity, prime)
                counts[prime][exponent] += 1
                joint[prime][(active, exponent)] += 1
    return endpoints, counts, joint


def direct_positive(radius, prime, width):
    counts = Counter()
    for magnitudes in compositions(radius, width):
        multiplicity = factorial(radius) // prod(factorial(a) for a in magnitudes)
        counts[valuation(multiplicity, prime)] += 1
    return counts


def labels(radius):
    trial_prime = radius >= 2 and all(radius % d for d in range(2, radius))
    return {
        "zero": radius == 0,
        "unit": radius == 1,
        "even": radius % 2 == 0,
        "prime": trial_prime,
        "composite": radius >= 2 and not trial_prime,
    }


def main():
    primes = (2, 3, 5, 7)
    rows = []
    total_endpoints = 0
    for radius in range(11):
        endpoint_count, direct, direct_joint = direct_signed(radius, primes)
        assert endpoint_count == shell_size(radius)
        total_endpoints += endpoint_count
        for prime in primes:
            computed = signed_valuation_spectrum(radius, prime)
            assert computed.valuation_counts() == dict(direct[prime])
            actual_joint = {}
            for active, histogram in computed.signed_by_active:
                for weight, count in histogram.entries:
                    actual_joint[(active, valuation(weight.numerator, prime))] = count
            assert actual_joint == dict(direct_joint[prime])
            assert computed.signed_histogram.count == endpoint_count
            positive = direct_positive(radius, prime, 6)
            lucas = prod(comb(digit + 5, 5) for digit in computed.digits)
            assert positive[0] == lucas
            lifted = Counter()
            for width in range(7):
                coefficient = comb(6, width) * (-1)**(6 - width) * 2**width
                for exponent, count in direct_positive(radius, prime, width).items():
                    lifted[exponent] += coefficient * count
            assert {e: c for e, c in lifted.items() if c} == dict(direct[prime])
            rows.append({"N": radius, "p": prime, "labels": labels(radius),
                         "endpoints": endpoint_count,
                         "H": dict(sorted(direct[prime].items())),
                         "positive_Lucas_nonzero": lucas})

    assert signed_valuation_spectrum(0, 2).valuation_counts() == {0: 1}
    assert signed_valuation_spectrum(1, 2).valuation_counts() == {0: 12}
    assert signed_valuation_spectrum(2, 2).valuation_counts() == {0: 12, 1: 60}
    assert signed_valuation_spectrum(4, 2).valuation_counts() == {0: 12, 1: 60, 2: 600, 3: 240}
    # Independent explicit witness: carries (3,1,0) versus factorial quotient 720.
    assert 6 + 0 == 0 + 2 * 3
    assert 0 + 3 == 1 + 2 * 1
    assert 0 + 1 == 1 + 2 * 0
    assert valuation(factorial(6), 2) == 3 + 1 + 0 == 4
    assert valuation(factorial(6), 2) != 2  # nonzero carry-position count
    assert valuation(4, 2) == 2 and valuation(6, 2) == 1

    failures = []
    for radius, prime, options, error in [
        (-1, 2, {}, ValueError), (True, 2, {}, TypeError),
        (2, 4, {}, ValueError), (2, True, {}, TypeError),
        (2, 37, {}, ComputationBudgetExceeded),
        (4, 2, {"max_digits": 2}, ComputationBudgetExceeded),
    ]:
        try:
            signed_valuation_spectrum(radius, prime, **options)
        except error:
            failures.append(error.__name__)
        else:
            raise AssertionError("expected exact input/resource exception")

    large = []
    for radius in (10**6 + 1, 10**12 + 39):
        for prime in (2, 3, 5):
            computed = signed_valuation_spectrum(radius, prime)
            assert computed.signed_histogram.count == shell_size(radius)
            large.append({"N": radius, "p": prime,
                          "digits": len(computed.digits),
                          "endpoint_count": computed.signed_histogram.count,
                          "valuation_bins": len(computed.valuation_counts()),
                          "endpoint_oracle": "closed shell count only; no large-domain factorial census"})

    output = {
        "status": "PASS",
        "scope": "complete signed endpoints N=0..10; primes 2,3,5,7",
        "small_signed_endpoints_enumerated_once": total_endpoints,
        "small_endpoint_prime_checks": total_endpoints * len(primes),
        "small_cases": len(rows),
        "joint_active_valuation_checked": True,
        "lifting_and_positive_Lucas_checked": True,
        "carry_gt_one_witness": {"N": 6, "p": 2, "abs_endpoint": [1]*6,
                                  "carries": [3, 1, 0], "multiplicity": 720, "valuation": 4},
        "exception_checks": failures,
        "rows": rows,
        "large_count_only_checks": large,
    }
    destination = Path(__file__).with_name("owner_arithmetic_20260907_results.json")
    destination.write_text(json.dumps(output, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({k: v for k, v in output.items() if k not in ("rows", "large_count_only_checks")}, ensure_ascii=False))


if __name__ == "__main__":
    main()
