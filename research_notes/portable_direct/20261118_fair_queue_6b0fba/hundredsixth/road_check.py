"""Anchored energies with integer-labelled shifts. Requires only Python 3.9+."""
from fractions import Fraction as Q
from functools import cache
from math import gcd, lgamma, log, pi, prod
import json


SCALE = 10**18


@cache
def primes(n):
    p, factors = 2, []
    while p*p <= n:
        if n % p == 0:
            factors.append(p)
            while n % p == 0:
                n //= p
        p += 1
    return tuple(factors + ([n] if n>1 else []))


def phi(n):
    for p in primes(n):
        n = n//p*(p-1)
    return n


def mu(n):
    ps = primes(n)
    return (-1)**len(ps) if n == prod(ps) else 0


def raw_block(q):
    divisors = [(d, d*mu(q//d)) for d in range(1, q+1) if q % d == 0]
    row = [sum(a for d, a in divisors if n%d == 0) for n in range(q)]
    assert sum(row) == 0 and sum(v*v for v in row) == q*phi(q)
    return row


def ceil_q(x):
    return -((-x.numerator)//x.denominator)


@cache
def weight(q, a):
    # Bounds, on a fixed integer scale, for the sum of 1/(a+jq)^2.
    J = 10
    z = Q(a, q) + J
    head = sum(Q(1, (a+j*q)**2) for j in range(J))
    tail = 1/z + 1/(2*z**2) + 1/(6*z**3) - 1/(30*z**5)
    lo = SCALE * (head + tail/q**2)
    hi = lo + SCALE/(42*z**7*q**2)
    return lo.numerator//lo.denominator, ceil_q(hi)


def energy_bounds(masses, q):
    return tuple(sum(masses[k-1]*weight(q, k)[j] for k in range(1, q+1)) for j in (0, 1))


@cache
def full(q):
    # Full nonzero frequency grid, including nonprimitive frequencies.
    return energy_bounds([k*(q-k) for k in range(1, q+1)], q)


def enumerate_shifts(q):
    c = raw_block(q)
    totals = [0]*q
    norms = []
    for b in range(1, q+1):
        v = 0
        row = []
        for n in range(1, q+1):
            v += c[(n-b)%q]
            row.append(v*v)
            totals[n-1] += v*v
        norms.append(energy_bounds(row, q))
    return norms, totals


def mobius_average(q):
    lo = hi = 0
    for d in range(1, q+1):
        if q%d == 0:
            sign = mu(d)
            a, b = full(q//d)
            lo += sign*(a if sign>0 else b)
            hi += sign*(b if sign>0 else a)
    return lo, hi


def gamma_approx():
    n = 1000
    return sum(1/k for k in range(1,n+1))-log(n)-1/(2*n)+1/(12*n*n)


def phase_limit(x):
    z = x+16
    psi = log(z)-1/(2*z)-1/(12*z**2)+1/(120*z**4)-1/(252*z**6)
    psi -= sum(1/(x+j) for j in range(16))
    return log(2*pi) - (1-2*x)*psi - 2*lgamma(x)


def median():
    lo, hi = 0.25, 0.4
    for _ in range(40):
        x = (lo+hi)/2
        if phase_limit(x)>phase_limit(x+0.5):
            lo = x
        else:
            hi = x
    return [f"{v:.7f}" for v in (lo, lo+0.5, phase_limit(lo))]


def compound_replay():
    rows = []
    for m, p in ((2, 5), (3, 7), (6, 11), (10, 7)):
        q = m*p
        c, cm = raw_block(q), raw_block(m)
        starts = set()
        checked = 0
        for label in range(1, q+1):
            b = 1 + (label-1) % p
            j = ((b-label)//p) % m
            starts.add((b, j))
            value = background = pulses = 0
            for n in range(1, q+1):
                value += c[(n-label)%q]
                background += cm[(n-label)%m]
                if n >= b and (n-b)%p == 0:
                    pulses += cm[(j+(n-b)//p)%m]
                assert value == p*pulses-background
                checked += 1
        assert len(starts) == q
        avg4 = Q(sum(h**4 for h in cm),m)
        local = prod(Q((l-1)**4+l-1,l) for l in primes(m))
        assert avg4 == local
        rows.append({"m":m, "p":p, "residue_phases":len(starts), "raw_prefixes":checked,
                     "s2_arithmetic_factor":str(avg4)})
    return rows


def main():
    chosen = (2, 3, 5, 11, 31, 60, 72, 101, 180, 210, 257)
    tested = sorted(set(range(2, 50)) | set(chosen))
    records = []
    counts = 0
    gamma = gamma_approx()
    for q in tested:
        norms, totals = enumerate_shifts(q)
        # At each residue k, use the raw integer block and independently recover the
        # averaged prefix energy over all integer shifts by Fourier inclusion-exclusion.
        for k in range(1, q+1):
            val = sum(mu(d)*((k%(q//d))*(q//d-k%(q//d))) for d in range(1,q+1) if q%d == 0)
            assert totals[k-1] == q*val
            counts += 1
        real_lo, real_hi = energy_bounds(totals, q)
        check_lo, check_hi = mobius_average(q)
        assert real_lo <= q*check_hi and q*check_lo <= real_hi
        avg = (real_lo+real_hi)/(2*q*SCALE)
        pred = phi(q)*(log(q)+gamma+1-log(2*pi)+sum(log(p)/(p-1) for p in primes(q)))
        bound = 2*prod(1+p for p in primes(q))/q
        assert max(abs(real_lo/(q*SCALE)-pred), abs(real_hi/(q*SCALE)-pred)) < bound
        if primes(q)==(q,):
            w = [(lo/SCALE, hi/SCALE) for lo,hi in norms]
            for b in range(1, q):
                if q != 2:
                    assert (w[b-1][0] > w[b][1]) if 2*b<q else (w[b-1][1] < w[b][0])
                else:
                    assert norms[0] == norms[1]
            if q>2: assert w[0][0]>w[-1][1]
        if q in chosen:
            info={"q":q, "mean_interval_numerators": [real_lo,real_hi],
                  "mean_interval_denominator": q*SCALE}
            if primes(q)==(q,):
                b=(q+1)//2
                info["minimizing_b"]=[1,2] if q==2 else [b]
                info["first_and_middle_and_last_intervals"]=[norms[0],norms[b-1],norms[-1]]
            records.append(info)
    print(json.dumps({"scaling":SCALE,"q_tested":tested,"number_of_all_shifts":sum(tested),
          "exact_period_prefix_identities":counts,"composite_phase_readouts":compound_replay(),"approximate_limit_median":median(),
          "records":records}, indent=2))


if __name__=="__main__":
    main()
