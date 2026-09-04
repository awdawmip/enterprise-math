#!/usr/bin/env python3
"""Exact finite checks for the prime-winding Möbius/Selberg RG frontier.

The checker uses only integers, Fraction, and formal prime-labelled tensors.
There is no floating evaluation of pi/tau, no numerical PNT assumption, and no
zeta-zero input.
"""

from __future__ import annotations

from collections import defaultdict
from fractions import Fraction
from itertools import permutations
from math import comb, factorial, gcd

Tensor = dict[tuple[int, ...], int]


def factorint(n: int) -> dict[int, int]:
    assert n >= 1
    out: dict[int, int] = {}
    d = 2
    while d * d <= n:
        while n % d == 0:
            out[d] = out.get(d, 0) + 1
            n //= d
        d += 1
    if n > 1:
        out[n] = out.get(n, 0) + 1
    return out


def is_prime(n: int) -> bool:
    return n >= 2 and factorint(n) == {n: 1}


def primes_upto(limit: int) -> list[int]:
    return [n for n in range(2, limit + 1) if is_prime(n)]


def divisors(n: int) -> list[int]:
    assert n >= 1
    ds = [1]
    for p, e in factorint(n).items():
        old = list(ds)
        power = 1
        for _ in range(e):
            power *= p
            ds.extend(d * power for d in old)
    return sorted(ds)


def mobius(n: int) -> int:
    fac = factorint(n)
    if any(e > 1 for e in fac.values()):
        return 0
    return -1 if len(fac) % 2 else 1


def prime_power_base(n: int) -> int | None:
    """Return p when n=p^a with p prime and a>=1; otherwise None."""
    if n < 2:
        return None
    fac = factorint(n)
    if len(fac) != 1:
        return None
    return next(iter(fac))


def lcm(a: int, b: int) -> int:
    return a // gcd(a, b) * b


def lcm_upto(limit: int) -> int:
    value = 1
    for n in range(1, limit + 1):
        value = lcm(value, n)
    return value


def winding_height(p: int, limit: int) -> int:
    assert is_prime(p) and limit >= 1
    height = 0
    power = p
    while power <= limit:
        height += 1
        power *= p
    return height


def saturated_winding_det(limit: int) -> int:
    value = 1
    for p in primes_upto(limit):
        value *= p ** winding_height(p, limit)
    return value


def tensor_clean(tensor: dict[tuple[int, ...], int]) -> Tensor:
    return {word: coefficient for word, coefficient in tensor.items() if coefficient}


def tensor_add(*tensors: Tensor) -> Tensor:
    out: defaultdict[tuple[int, ...], int] = defaultdict(int)
    for tensor in tensors:
        for word, coefficient in tensor.items():
            out[word] += coefficient
    return tensor_clean(dict(out))


def tensor_scale(coefficient: int, tensor: Tensor) -> Tensor:
    return tensor_clean({word: coefficient * value for word, value in tensor.items()})


def tensor_product(left: Tensor, right: Tensor) -> Tensor:
    out: defaultdict[tuple[int, ...], int] = defaultdict(int)
    for word_left, coefficient_left in left.items():
        for word_right, coefficient_right in right.items():
            out[word_left + word_right] += coefficient_left * coefficient_right
    return tensor_clean(dict(out))


def log_tensor(n: int) -> Tensor:
    """Formal prime-exponent vector ell(n)=sum_p v_p(n)e_p."""
    assert n >= 1
    return {(p,): e for p, e in factorint(n).items()}


def tensor_power_of_log(n: int, degree: int) -> Tensor:
    assert degree >= 0
    result: Tensor = {(): 1}
    base = log_tensor(n)
    for _ in range(degree):
        result = tensor_product(result, base)
    return result


def primitive_tensor(n: int, degree: int) -> Tensor:
    """Lambda_degree(n)=sum_{d|n} mu(d) ell(n/d)^(tensor degree)."""
    terms: list[Tensor] = []
    for d in divisors(n):
        mu = mobius(d)
        if mu:
            terms.append(tensor_scale(mu, tensor_power_of_log(n // d, degree)))
    return tensor_add(*terms)


def lambda_one_tensor(n: int) -> Tensor:
    p = prime_power_base(n)
    return {} if p is None else {(p,): 1}


def formal_trace_energy(cutoff: int, degree: int) -> Tensor:
    """sum_{m<=cutoff} ell(m)^(tensor degree)."""
    result: Tensor = {}
    for m in range(1, cutoff + 1):
        result = tensor_add(result, tensor_power_of_log(m, degree))
    return result


def primitive_quotient_trace(cutoff: int, degree: int) -> Tensor:
    """sum_{d<=M} mu(d) Tr(log K^+_{floor(M/d)})^degree."""
    result: Tensor = {}
    for d in range(1, cutoff + 1):
        mu = mobius(d)
        if mu:
            result = tensor_add(
                result,
                tensor_scale(mu, formal_trace_energy(cutoff // d, degree)),
            )
    return result


def cumulative_primitive_current(cutoff: int, degree: int) -> Tensor:
    result: Tensor = {}
    for n in range(1, cutoff + 1):
        result = tensor_add(result, primitive_tensor(n, degree))
    return result


def carry_count_double(n: int, p: int) -> int:
    assert n >= 0 and is_prime(p)
    count = 0
    carry = 0
    while n > 0 or carry:
        digit = n % p
        n //= p
        carry = 1 if 2 * digit + carry >= p else 0
        count += carry
    return count


def vp_int(n: int, p: int) -> int:
    assert n >= 1 and is_prime(p)
    exponent = 0
    while n % p == 0:
        n //= p
        exponent += 1
    return exponent


def check_saturated_winding_determinant(limit: int = 250) -> None:
    previous = 1
    for M in range(1, limit + 1):
        L = lcm_upto(M)
        assert saturated_winding_det(M) == L, M

        ratio = L // previous
        p = prime_power_base(M)
        expected = p if p is not None else 1
        assert ratio == expected, (M, ratio, expected)
        previous = L


def check_quotient_determinant_rg(limit: int = 140) -> None:
    for M in range(1, limit + 1):
        quotient_product = 1
        for k in range(1, M + 1):
            quotient_product *= lcm_upto(M // k)
        assert quotient_product == factorial(M), M

        recursive = factorial(M)
        for k in range(2, M + 1):
            recursive //= lcm_upto(M // k)
        assert recursive == lcm_upto(M), M

        inverse = Fraction(1, 1)
        for k in range(1, M + 1):
            mu = mobius(k)
            block_det = factorial(M // k)
            if mu == 1:
                inverse *= block_det
            elif mu == -1:
                inverse /= block_det
        assert inverse.denominator == 1, (M, inverse)
        assert inverse.numerator == lcm_upto(M), (M, inverse)


def check_primitive_tensor_hierarchy(limit: int = 220, max_degree: int = 4) -> None:
    for n in range(1, limit + 1):
        support = sorted(factorint(n))
        omega = len(support)

        assert primitive_tensor(n, 1) == lambda_one_tensor(n), n

        for degree in range(1, max_degree + 1):
            tensor = primitive_tensor(n, degree)
            if omega > degree:
                assert tensor == {}, (n, degree, tensor)
            elif omega == degree:
                expected: Tensor = {
                    tuple(ordering): 1 for ordering in permutations(support)
                }
                assert tensor == expected, (n, degree, tensor, expected)


def check_quadratic_selberg_tensor_identity(limit: int = 300) -> None:
    for n in range(1, limit + 1):
        diagonal = tensor_product(lambda_one_tensor(n), log_tensor(n))

        convolution: Tensor = {}
        for a in divisors(n):
            b = n // a
            convolution = tensor_add(
                convolution,
                tensor_product(lambda_one_tensor(a), lambda_one_tensor(b)),
            )

        expected = tensor_add(diagonal, convolution)
        actual = primitive_tensor(n, 2)
        assert actual == expected, (n, actual, expected)

    for M in range(1, 90):
        left = primitive_quotient_trace(M, 2)
        middle = cumulative_primitive_current(M, 2)
        assert left == middle, M

        diagonal_sum: Tensor = {}
        for n in range(1, M + 1):
            diagonal_sum = tensor_add(
                diagonal_sum,
                tensor_product(lambda_one_tensor(n), log_tensor(n)),
            )

        pair_sum: Tensor = {}
        for a in range(1, M + 1):
            for b in range(1, M // a + 1):
                pair_sum = tensor_add(
                    pair_sum,
                    tensor_product(lambda_one_tensor(a), lambda_one_tensor(b)),
                )

        assert middle == tensor_add(diagonal_sum, pair_sum), M


def check_first_primitive_trace(limit: int = 120) -> None:
    for M in range(1, limit + 1):
        quotient_trace = primitive_quotient_trace(M, 1)
        current = cumulative_primitive_current(M, 1)
        expected: Tensor = {}
        for p in primes_upto(M):
            expected[(p,)] = winding_height(p, M)
        assert quotient_trace == current == expected, M


def check_dyadic_carry_projector(limit: int = 180) -> None:
    for N in range(1, limit + 1):
        reconstructed = 1
        for p in primes_upto(2 * N):
            power = p
            projected_layers = 0
            while power <= 2 * N:
                epsilon = (2 * N) // power - 2 * (N // power)
                assert epsilon in (0, 1), (N, power, epsilon)
                projected_layers += epsilon
                reconstructed *= p**epsilon
                power *= p

            central = comb(2 * N, N)
            assert projected_layers == vp_int(central, p), (N, p)
            assert projected_layers == carry_count_double(N, p), (N, p)

        assert reconstructed == comb(2 * N, N), N


def main() -> None:
    check_saturated_winding_determinant()
    check_quotient_determinant_rg()
    check_primitive_tensor_hierarchy()
    check_first_primitive_trace()
    check_quadratic_selberg_tensor_identity()
    check_dyadic_carry_projector()
    print("prime-winding Mobius/Selberg RG exact checks: PASS")


if __name__ == "__main__":
    main()
