"""Exact finite-spectrum and local-trace certificates. Python 3.9+; standard library."""
import hashlib
import json
from fractions import Fraction
from functools import lru_cache
from math import lcm, prod


def add(a, b, factor=1):
    out = a[:] + [0] * max(0, len(b) - len(a))
    for i, value in enumerate(b):
        out[i] += factor * value
    return out


def multiply(a, b):
    out = [0] * (len(a) + len(b) - 1)
    for i, value in enumerate(a):
        for j, other in enumerate(b):
            out[i+j] += value * other
    return out


def exact_monic_quotient(a, b):
    assert b[-1] == 1
    work = a[:]
    result = [0] * (len(a) - len(b) + 1)
    for i in reversed(range(len(result))):
        result[i] = work[i+len(b)-1]
        for j, value in enumerate(b):
            work[i+j] -= result[i] * value
    assert not any(work)
    return result


def proper_divisors(n):
    return (k for k in range(1, n) if n % k == 0)


@lru_cache(None)
def cyclotomic(n):
    coeff = [-1] + [0]*(n-1) + [1]
    for k in proper_divisors(n):
        coeff = exact_monic_quotient(coeff, cyclotomic(k))
    return coeff


def real_factor(n):
    phi = cyclotomic(n)
    e = (len(phi)-1)//2
    assert n >= 3 and len(phi) == 2*e+1 and phi == phi[::-1]
    older, current = [2], [2, -1]
    value = [phi[e]]
    for j in range(1, e+1):
        value = add(value, current, phi[e+j])
        older, current = current, add(multiply(current, [2, -1]), older, -1)
    return [(-1)**e * c for c in value]


@lru_cache(None)
def full_dirichlet(d):
    if d == 1:
        return [1]
    if d == 2:
        return [-2, 1]
    return add(multiply(full_dirichlet(d-1), [-2, 1]), full_dirichlet(d-2), -1)


@lru_cache(None)
def primitive_dirichlet(d):
    value = full_dirichlet(d)
    for k in proper_divisors(d):
        value = exact_monic_quotient(value, primitive_dirichlet(k))
    return value


def inverse_moments(f, maximum):
    """Integer Newton sums for |f(0)|/root, then remove that scale."""
    c = abs(f[0])
    e = len(f)-1
    a = [1] + [f[j]*c**j//f[0] for j in range(1, e+1)]
    sums = [e]
    for n in range(1, maximum+1):
        total = n*a[n] if n <= e else 0
        total += sum(a[j]*sums[n-j] for j in range(1, min(e, n-1)+1))
        sums.append(-total)
    return [Fraction(value, c**n) for n, value in enumerate(sums)]


def prime_power(n):
    divisor = next((k for k in range(2, n+1) if n % k == 0), None)
    if divisor is None:
        return None
    a, rest = 0, n
    while rest % divisor == 0:
        a += 1
        rest //= divisor
    return (divisor, a) if rest == 1 else None


def parameters(p, a):
    if p == 2:
        e = 2**(a-1)
        return e, a*e-1
    return p**(a-1)*(p-1)//2, (p**(a-1)*(a*p-a-1)-1)//2


def divide_by_uniformizer(coeff, f, count):
    """Exact in Z[u]: divide by u, eliminating the constant with f(u)=0."""
    for _ in range(count):
        v, rem = divmod(coeff[0], f[0])
        assert rem == 0
        coeff = [a-v*b for a,b in zip(coeff[1:]+[0], f[1:])]
    return coeff


def step(a, b, p):
    return [x % p for x in multiply(a, b)[:len(a)]]


def p_residue(x, p):
    assert x.denominator % p != 0
    return x.numerator * pow(x.denominator, -1, p) % p


def valuation(x, p):
    assert x
    n, d, v = x.numerator, x.denominator, 0
    while n % p == 0:
        n //= p
        v += 1
    while d % p == 0:
        d //= p
        v -= 1
    return v


def digest(rows):
    data = json.dumps(rows, separators=(',', ':')).encode('ascii')
    return hashlib.sha256(data).hexdigest()


def verify():
    cap = 128
    heights = range(1, 21)
    collective = [1] * (max(heights)+1)
    local = []
    count = 0
    digit_count = 0
    moments_hash = hashlib.sha256()
    examples = {}
    for d in range(2, cap+1):
        f = real_factor(2*d) if d % 2 == 0 else real_factor(d)
        split = f if d % 2 == 0 else multiply(f, real_factor(2*d))
        source = primitive_dirichlet(d)
        assert source == split
        pa = prime_power(d)
        max_n = max(heights)
        if pa:
            p, a = pa
            e, delta = parameters(p, a)
            rounds = p if a == 1 and 5 <= p <= 31 else 4
            max_n = max(max_n, delta + rounds*e)
        moments = inverse_moments(source, max_n)
        moments_hash.update(f'{d}:'.encode())
        for n, value in enumerate(moments[1:], 1):
            count += 1
            moments_hash.update(f'{value};'.encode())
            if n <= max(heights):
                collective[n] = lcm(collective[n], value.denominator)
            if not pa:
                assert value.denominator == 1
            else:
                assert value.denominator == p**max(0, -valuation(value,p))
                assert valuation(value,p) >= (delta-n)//e
        if not pa:
            continue
        assert len(f) == e+1
        W = divide_by_uniformizer([p]+[0]*(e-1), f, e)
        V = divide_by_uniformizer([i*f[i] for i in range(1,e+1)], f, delta)
        sign_u = (-1)**(e+1) % p
        sign_v = 1 if p == 2 else pow(-1, e+a+1-delta, p)*pow(2,-1,p) % p
        assert W[0] % p == sign_u and V[0] % p == sign_v
        assert next(n for n in range(1,max_n+1) if moments[n].denominator != 1) == delta+1
        prefix_digits = []
        table = []
        row = [x % p for x in V]
        for t in range(rounds):
            row = step(row, W, p)
            actual = [p_residue(p**(t+1)*moments[delta+1+t*e+s], p) for s in range(e)]
            assert row == actual
            digit_count += e
            assert actual[0] == pow(sign_u,t+1,p)*sign_v % p
            prefix_digits.append(actual[0])
            table.append([y*pow(sign_u, -t-1, p)%p for y in actual])
        complete_period = None
        if rounds == p and p >= 5 and a == 1:
            assert W[1]*pow(sign_u,-1,p)%p == -pow(24,-1,p)%p
            zero_counts = []
            for s in range(e):
                values = [row[s] for row in table]
                zero_counts.append(values.count(0))
                for _ in range(s):
                    values = [(v-u)%p for u,v in zip(values,values[1:])]
                assert len(set(values)) == 1 and values[0] != 0
                assert zero_counts[-1] <= s
            assert zero_counts[1] == 1
            for t, residues in enumerate(table):
                T = t+1
                assert residues[1] == -(e*T+1)*pow(24,-1,p) % p
                if e > 2:
                    assert residues[2] == (e*T+2)*(5*T-22)*pow(5760,-1,p) % p
                for s in range(1, e):
                    if (e*T+s) % p == 0:
                        assert residues[s] == 0
            complete_period = zero_counts
        local.append({'d':d, 'p':p, 'a':a, 'e':e, 'delta':delta,
                      'first_nonintegral': delta+1, 'boundary_digits_first_four':prefix_digits[:4],
                      'all_offsets_grid_sha256':digest(table),
                      **({'zero_counts_by_offset_one_primitive_period':complete_period} if complete_period else {})})
        if d in (2, 3, 4, 5, 7, 9, 25):
            examples[str(d)] = {'first_fraction':str(moments[delta+1]),
                                'preceding_fraction':str(moments[delta]) if delta else None}
    primes = [p for p in range(3,2*max(heights)+2,2) if prime_power(p)==(p,1)]
    for h in heights:
        collective[h] = lcm(collective[h-1], collective[h])
        assert collective[h] == 2**h * prod(p**(2*h//(p-1)) for p in primes)
    return {'schema':1, 'arithmetic':'exact integer polynomials and rational Newton sums',
            'd_range':[2,cap], 'tested_primitive_moments':count, 'primitive_moment_stream_sha256':moments_hash.hexdigest(),
            'local_digits_compared_to_full_source':digit_count, 'prime_power_rows':local,
            'sample_full_spectrum_values':examples, 'joint_denominators_H_1_to_20':collective[1:]}


if __name__ == '__main__':
    print(json.dumps(verify(), ensure_ascii=False, sort_keys=True, indent=2))
