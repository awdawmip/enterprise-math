"""Reproduce covariance checks. Python 3, NumPy and SciPy. Print JSON to stdout."""
import json
import math

import numpy as np
from scipy.special import digamma, polygamma

def squarefree_ramanujan(factors, n):
    return math.prod(p - 1 if n % p == 0 else -1 for p in factors)


def covariance_bounds(factors, p, lags, terms=40):
    """Exact integer outer bounds. Interval endpoints are in 1/1000 units for Cov(E/p)."""
    q = math.prod(factors)
    scale = 1 << 62
    low_w = [0] * q
    high_w = [0] * q
    for k in range(1, q):
        lower = sum(scale // (k + j*q)**2 for j in range(terms))
        end = k + terms*q
        lower += scale // (q * end)
        low_w[k] = lower
        high_w[k] = lower + terms + 1 + (scale + end**2 - 1) // end**2
    values = [squarefree_ramanujan(factors, n) for n in range(q)]
    assert sum(values) == 0
    low, high = [], []
    for b in range(1, q + 1):
        prefix = lo = hi = 0
        for k in range(1, q):
            prefix += values[(k-b) % q]
            lo += prefix**2 * low_w[k]
            hi += prefix**2 * high_w[k]
        low.append(lo)
        high.append(hi)
    den = (q * scale * p)**2
    bounds = []
    for h in lags:
        prod_lo = sum(x * low[(i+h) % q] for i, x in enumerate(low))
        prod_hi = sum(x * high[(i+h) % q] for i, x in enumerate(high))
        lo = q * prod_lo - sum(high)**2
        hi = q * prod_hi - sum(low)**2
        bounds.append([1000 * lo // den, -(-1000 * hi // den)])
    return bounds


def fft_energies(factors, p):
    """Use the periodic primitive and two circular cross-correlations for all phases."""
    q = math.prod(factors)
    k = np.arange(q)
    unit = np.ones(q, dtype=np.int64)
    for ell in factors:
        unit *= np.where(k % ell == 0, ell - 1, -1)
    primitive = np.empty(q, dtype=float)
    primitive[0] = 0
    primitive[1:] = np.cumsum(unit[1:])
    weights = np.zeros(q)
    weights[1:] = polygamma(1, k[1:] / q) / q**2
    transform = np.fft.rfft(weights).conjugate()

    def corr(v):
        return np.fft.irfft(transform * np.fft.rfft(v), n=q)

    energy = corr(primitive**2) - 2 * primitive * corr(primitive) + primitive**2 * sum(weights)
    return energy[(-np.arange(1, q+1)) % q] / p


def covariance(energies, h):
    centered = energies - energies.mean()
    return float(np.mean(centered * np.roll(centered, -h)))


def endpoint_constants(m, factors, r):
    c = [squarefree_ramanujan(factors, j) for j in range(m)]
    a = [v*v for v in c]
    r0, l1 = [], []
    for j in range(m):
        cumulative = np.cumsum([c[(j+k) % m] for k in range(m)])**2

        def weight(u):
            return (digamma((u+1)/m) - digamma(u/m)) / m

        r0.append(-a[j] + sum(cumulative[k % m] * weight(k) for k in range(1, m+1)))
        l1.append(sum(cumulative[k] * weight(k+1) for k in range(m)))
    mr = sum(a[j] * a[(j-r) % m] for j in range(m)) / m
    dr = sum(a[j] * r0[(j-r) % m] + a[(j-r-1) % m] * l1[j] for j in range(m)) / m
    return mr, dr


def fixed_lag_checks():
    n = np.arange(1, 50001, dtype=float)
    s = [float(np.sum(polygamma(1, n) * polygamma(1, n+h))) for h in range(9)]
    # Integral bounds on the omitted product using 1/n <= psi_1(n) <= 1/n + 1/n^2.
    N = len(n)
    z3 = 1.2020569031595942854
    z4 = math.pi**4 / 90
    exact = [3*z3, 3*z3-7*z4/4]
    harmonic = harmonic2 = 0.0
    for h in range(1, 8):
        harmonic += 1/h
        harmonic2 += 1/h**2
        second = 2*harmonic/h**3 - (math.pi**2/6 - harmonic2)/h**2
        exact.append(2*exact[-1] - exact[-2] + second)
    for h, v in enumerate(exact):
        assert 1/(N+h+1)-1e-12 < v-s[h] < (1+1/N)**2/N+1e-12
    return [round(v, 9) for v in exact]


def main():
    finite = []
    for factors, p, lags in [([31], 31, [1, 3, 9]), ([3, 13], 13, [3, 16, 29]),
                             ([3, 101], 101, [14, 115, 216]), ([2, 5, 7], 7, [1, 8, 15])]:
        bounds = covariance_bounds(factors, p, lags)
        values = fft_energies(factors, p)
        for lag, (lo, hi) in zip(lags, bounds):
            assert lo / 1000 <= covariance(values, lag) <= hi / 1000
        finite.append(dict(q=math.prod(factors), p=p, lags=lags, intervals_milli=bounds))
    assert finite[2]["intervals_milli"][0][0] > 0 > finite[2]["intervals_milli"][1][1]
    crt = []
    for m, factors in [(2,[2]),(3,[3]),(5,[5]),(6,[2,3]),(15,[3,5])]:
        for r in range(m):
            mr, dr = endpoint_constants(m, factors, r)
            expected = math.prod((ell-1)*(ell**2-3*ell+3) if r % ell == 0 else 2*ell-3
                                 for ell in factors)
            assert mr == expected
            if m == 3:
                next_mr = 6 if (r+1) % 3 == 0 else 3
                assert abs(dr-(2*next_mr-mr)*math.pi/(3*math.sqrt(3))) < 1e-12
            crt.append([m, r, expected, round(float(dr), 7)])
    measurements = []
    for p in [101, 1009, 10007, 100003]:
        L = math.log(p)
        h = round(p / L)
        prime = fft_energies([p], p)
        centered_prime = prime - prime.mean()
        covariance_curve = np.fft.irfft(abs(np.fft.rfft(centered_prime))**2, n=p) / p
        half_curve = covariance_curve[:p//2+1]
        first_nonpositive = int(np.flatnonzero(half_curve <= 0)[0])
        assert np.all(half_curve[first_nonpositive:] < 0)
        triple = fft_energies([3, p], p)
        v0, v1, v2 = [covariance(triple, h+r*p) for r in range(3)]
        measurements.append(dict(p=p, h=h, prime_cov=round(covariance(prime, h), 6),
                                 first_nonpositive_prime_lag=first_nonpositive,
                                 triple_cov=[round(v, 6) for v in (v0, v1, v2)],
                                 triple_lift_difference_over_log=round((v2-v1)/L, 6)))
    return {"interval_unit":"1/1000 of covariance of E/p", "integer_certificates":finite,
            "fixed_lag_coefficients_h0_to_8":fixed_lag_checks(), "crt_m_r_M_D":crt,
            "floating_fft_at_h_nearest_p_over_log_p":measurements}


if __name__ == "__main__":
    print(json.dumps(main(), ensure_ascii=False, indent=2))
