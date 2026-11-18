"""Exact finite witnesses for anchored road kernels. Python standard library."""
from argparse import ArgumentParser
from fractions import Fraction as F
from itertools import product
from math import gcd, isqrt
from pathlib import Path
import json


# Real and imaginary coordinates in the basis 1, z with z^2=z-1.
ONE = (F(1), F(0))
ZERO = (F(0), F(0))
ROOT = (F(0), F(1))


def add(x, y):
    return x[0]+y[0], x[1]+y[1]


def scale(q, x):
    return q*x[0], q*x[1]


def times(x, y):
    a, b = x
    c, d = y
    return a*c-b*d, a*d+b*c+b*d


def conj(x):
    return x[0]+x[1], -x[1]


def norm(x):
    return times(x, conj(x))[0]


def summation(items):
    total = ZERO
    for item in items:
        total = add(total, item)
    return total


def rational(x):
    assert x[1] == 0
    return x[0]


def finite_kernel():
    roots = [ONE]
    for _ in range(6):
        roots.append(times(roots[-1], ROOT))
    assert roots[-1] == ONE
    c = F(2, 3)  # Finite Euler road for the primes 2,3 at a=1.
    gamma = 1+c/2
    amplitudes = {1: F(1,36), 2: -F(1,12), 3: -F(2,9), 4: -F(1,12), 5: F(1,36)}
    modes = range(6)
    coefficients = [-gamma]+[amplitudes[j] for j in range(1,6)]
    gram = [[ZERO for _ in modes] for _ in modes]
    cumulative = F(0)
    energy = F(0)
    samples = []
    horizon = 19
    for n in range(1, horizon+1):
        mass = (F(1,2) if n % 2 == 0 else 1)*(F(2,3) if n % 3 == 0 else 1)
        cumulative += mass-c
        anchored = cumulative-gamma
        h = [ONE]+[summation(roots[j*k % 6] for k in range(1,n+1)) for j in range(1,6)]
        assert anchored == rational(summation(scale(t,v) for t,v in zip(coefficients,h)))
        samples.append(anchored)
        energy += anchored**2/n**2
        for j,k in product(modes,repeat=2):
            gram[j][k] = add(gram[j][k], scale(F(1,n*n),times(h[j],conj(h[k]))))
    reconstructed = rational(summation(scale(coefficients[j]*coefficients[k],gram[j][k])
                                         for j,k in product(modes,repeat=2)))
    diagonal = sum(coefficients[j]**2*rational(gram[j][j]) for j in modes)
    centered_out = sum((v+gamma)**2/F(n*n) for n,v in enumerate(samples,1))
    assert energy == reconstructed and energy != diagonal and energy != centered_out

    # Parseval at infinite horizon for this finite model; compare the exact period.
    degeneracy = {2: 1, 3: 2, 6: 2}
    jordan = {2: 3, 3: 8, 6: 24}
    by_q = {2: amplitudes[3], 3: amplitudes[2], 6: amplitudes[1]}
    zero_channel = -gamma-sum(by_q[q]*degeneracy[q] for q in by_q)/2
    expected_mean = zero_channel**2+sum(by_q[q]**2*jordan[q]/12 for q in by_q)
    assert sum(v*v for v in samples[:6])/6 == expected_mean
    assert all(samples[k] == samples[k%6] for k in range(len(samples)))
    # Compare dyadic-tail truncation through two complete subperiods.
    comparisons = []
    for x in (6, 12, 24):
        truncation = sum(samples[(n-1)%6]**2/F(n*n) for n in range(x+1,2*x+1))
        comparisons.append([x,str(truncation)])
    return dict(horizon=horizon,energy=str(energy),full_gram=str(reconstructed),
                diagonal_only=str(diagonal),centering_omitted=str(centered_out),
                rank_one_constant=str(zero_channel),period_mean_square=str(expected_mean),
                dyadic_examples=comparisons)


def coefficient_checks():
    ratios = []
    for s in range(2,7):
        ratio = F(3**s-1,2**s-1)**2
        if ratios:
            assert F(3,2) < ratio/ratios[-1] < F(9,4)
        ratios.append(ratio)
    # At the arithmetic point a=1/2, get c>=1/3 from zeta(3/2)<=3.
    x = 2**80
    qmax = 4096
    k = 40
    assert (2*k*3)**2*qmax**5 <= x  # 2 K Q^(2+a) <= c X^a
    assert qmax**4 <= x
    squarefree = bytearray([1])*(qmax+1)
    for n in range(2, isqrt(qmax)+1):
        for m in range(n*n, qmax+1, n*n):
            squarefree[m] = 0
    harmonic = sum(F(1,q) for q in range(2,qmax+1) if squarefree[q])
    # c^2/(96*zeta(2)) >= 1/1728. Round the certified bound down.
    bound = harmonic/1728
    rounded = F(int(bound*10**8),10**8)
    assert rounded > 0 and rounded <= bound
    # log(2X)<81 since X=2^80. Test the stronger denominator cutoff
    # using squares of integers and round every harmonic summand down.
    improved_q = 2**17
    assert (2*k*3*83)**2*improved_q**3 <= x
    assert improved_q**2*35 <= x  # 1+2 log(2^17)<35
    sf = bytearray([1])*(improved_q+1)
    for n in range(2,isqrt(improved_q)+1):
        for m in range(n*n,improved_q+1,n*n):
            sf[m] = 0
    scale = 10**12
    lower = F(sum(scale//q for q in range(2,improved_q+1) if sf[q]),scale*1728)
    improved_rounded = F(int(lower*10**8),10**8)
    assert improved_rounded > rounded
    return dict(primes=[2,3],powers_ratio_squared=[str(x) for x in ratios],
                inverse_log_lipschitz="1/log(3/2)",arithmetic_half=dict(
                    X=str(x),Q_used=qmax,K=40,squarefree_q_count=sum(squarefree[2:]),
                    mean_square_lower_rounded_down=str(rounded),
                    stronger_Q_used=improved_q,
                    stronger_squarefree_count=sum(sf[2:]),
                    stronger_mean_square_lower_rounded_down=str(improved_rounded)))


def prefix_checks():
    # A separate divisor-based identity for the signed sums of primitive modes.
    def mu(n):
        primes = 0
        for p in range(2, isqrt(n)+1):
            if n % p == 0:
                n //= p
                if n % p == 0:
                    return 0
                primes += 1
        return (-1)**(primes+(n>1))

    checks = 0
    for q in range(2,50):
        divs = [d for d in range(1,q+1) if q % d == 0]
        prefix = 0
        for n in range(1,91):
            prefix += sum(d*mu(q//d) for d in divs if gcd(q,n)%d == 0)
            floor_sum = sum(d*mu(q//d)*(n//d) for d in divs)
            remainder_sum = -sum(mu(q//d)*(n%d) for d in divs)
            assert prefix == floor_sum == remainder_sum
            checks += 1
    return checks


def main():
    parser = ArgumentParser(description=__doc__)
    parser.add_argument('--json', type=Path)
    path = parser.parse_args().json
    out = dict(finite_kernel=finite_kernel(),coefficient_witnesses=coefficient_checks(),
               exact_divisor_prefix_checks=prefix_checks())
    data = json.dumps(out,sort_keys=True,indent=2)+'\n'
    if path:
        path.write_text(data)
    else:
        print(data,end='')


if __name__ == '__main__':
    main()
