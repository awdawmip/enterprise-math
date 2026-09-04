#!/usr/bin/env python3
"""Exact formal-tensor checks for the prime-winding Selberg return operator.

This imports the formal prime-labelled tensor algebra from the parent exact RG
checker.  No floating logarithm is used in the theorem checks: `log n` is the
prime-exponent vector ell(n).
"""

from __future__ import annotations

from check_free_research_prime_winding_selberg_rg import (
    Tensor,
    cumulative_primitive_current,
    lambda_one_tensor,
    log_tensor,
    tensor_add,
    tensor_product,
    tensor_scale,
)


def psi_tensors(limit: int) -> list[Tensor]:
    prefix: list[Tensor] = [{}]
    current: Tensor = {}
    for n in range(1, limit + 1):
        current = tensor_add(current, lambda_one_tensor(n))
        prefix.append(current)
    return prefix


def full_log_spectrum_tensors(limit: int) -> list[Tensor]:
    prefix: list[Tensor] = [{}]
    current: Tensor = {}
    for n in range(1, limit + 1):
        current = tensor_add(current, log_tensor(n))
        prefix.append(current)
    return prefix


def check_abel_and_return_balance(limit: int = 140) -> None:
    psi = psi_tensors(limit)

    self_energy_prefix: list[Tensor] = [{}]
    self_energy: Tensor = {}
    for n in range(1, limit + 1):
        self_energy = tensor_add(
            self_energy,
            tensor_product(lambda_one_tensor(n), log_tensor(n)),
        )
        self_energy_prefix.append(self_energy)

    primitive_two_prefix: list[Tensor] = [{}]
    primitive_two: Tensor = {}
    for n in range(1, limit + 1):
        primitive_two = tensor_add(
            primitive_two,
            cumulative_primitive_current(n, 2),
            tensor_scale(-1, cumulative_primitive_current(n - 1, 2))
            if n > 1
            else {},
        )
        # The line above deliberately reconstructs the nth increment from
        # cumulative surfaces, independently of self-energy/convolution.
        primitive_two_prefix.append(primitive_two)

    for M in range(1, limit + 1):
        boundary: Tensor = {}
        for m in range(1, M):
            delta_log = tensor_add(log_tensor(m + 1), tensor_scale(-1, log_tensor(m)))
            boundary = tensor_add(
                boundary,
                tensor_product(psi[m], delta_log),
            )

        present = tensor_product(psi[M], log_tensor(M))
        abel_reconstruction = tensor_add(present, tensor_scale(-1, boundary))
        assert self_energy_prefix[M] == abel_reconstruction, (
            "Abel",
            M,
            self_energy_prefix[M],
            abel_reconstruction,
        )

        quotient_return: Tensor = {}
        for a in range(1, M + 1):
            quotient_return = tensor_add(
                quotient_return,
                tensor_product(lambda_one_tensor(a), psi[M // a]),
            )

        direct_pair_energy: Tensor = {}
        for a in range(1, M + 1):
            for b in range(1, M // a + 1):
                direct_pair_energy = tensor_add(
                    direct_pair_energy,
                    tensor_product(lambda_one_tensor(a), lambda_one_tensor(b)),
                )
        assert quotient_return == direct_pair_energy, ("return", M)

        primitive_balance = tensor_add(self_energy_prefix[M], quotient_return)
        assert primitive_balance == cumulative_primitive_current(M, 2), (
            "primitive",
            M,
        )

        return_balance_left = tensor_add(present, quotient_return)
        return_balance_right = tensor_add(
            cumulative_primitive_current(M, 2),
            boundary,
        )
        assert return_balance_left == return_balance_right, ("balance", M)


def check_factorial_return_mass(limit: int = 300) -> None:
    psi = psi_tensors(limit)
    full_log = full_log_spectrum_tensors(limit)

    for M in range(1, limit + 1):
        weighted_current: Tensor = {}
        for a in range(1, M + 1):
            weighted_current = tensor_add(
                weighted_current,
                tensor_scale(M // a, lambda_one_tensor(a)),
            )

        # Formal version of sum Lambda(a) floor(M/a) = log(M!).
        assert weighted_current == full_log[M], (M, weighted_current, full_log[M])

        # Independent divisor-expansion check of the same mass identity.
        divisor_expansion: Tensor = {}
        for n in range(1, M + 1):
            divisor_sum: Tensor = {}
            for a in range(1, n + 1):
                if n % a == 0:
                    divisor_sum = tensor_add(divisor_sum, lambda_one_tensor(a))
            assert divisor_sum == log_tensor(n), (n, divisor_sum, log_tensor(n))
            divisor_expansion = tensor_add(divisor_expansion, divisor_sum)
        assert divisor_expansion == full_log[M]

        # The quotient-return current really lands only on strictly smaller
        # states whenever a contributes nonzero mass and a>1.
        for a in range(2, M + 1):
            if lambda_one_tensor(a):
                assert 1 <= M // a < M

        # Prefix current is consistent with the winding-height interpretation.
        assert psi[M] == tensor_add(psi[M - 1], lambda_one_tensor(M))


def main() -> None:
    check_abel_and_return_balance()
    check_factorial_return_mass()
    print("prime-winding Selberg return formal checks: PASS")


if __name__ == "__main__":
    main()
