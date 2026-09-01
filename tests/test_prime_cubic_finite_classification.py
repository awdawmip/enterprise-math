import bisect
import unittest
from math import isqrt

from enterprise_math.legendre import primes_up_to
from enterprise_math.prime_collapse_field import factor_horizon


class PrimeCubicFiniteClassificationTests(unittest.TestCase):
    def test_exact_upper_exception_set_through_1100(self):
        limit = 1100
        max_horizon = factor_horizon(limit, 3)
        primes = primes_up_to(max_horizon + 1000)
        exceptions = {}
        for k in range(2, limit + 1):
            lower = k**3
            upper = (k + 1) ** 3 - 1
            horizon = factor_horizon(k, 3)
            root_lower = isqrt(lower)

            qi = bisect.bisect_right(primes, root_lower) - 1
            ri = bisect.bisect_right(primes, horizon)
            q_max = primes[qi]
            r = primes[ri]
            if not (q_max * horizon > lower and q_max * r > upper):
                continue
            lo = max(lower // horizon, upper // r) + 1
            left = bisect.bisect_left(primes, lo)
            right = bisect.bisect_right(primes, root_lower)
            exceptions[k] = primes[left:right]

        self.assertEqual(
            exceptions,
            {
                23: [109],
                64: [509],
                120: [1303, 1307],
                138: [1621],
                1005: [31859],
            },
        )


if __name__ == "__main__":
    unittest.main()
