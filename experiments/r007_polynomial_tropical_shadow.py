"""Polynomial valuation-shadow descent and tropical phase-defect localization.

Executable evidence only; these are theorem targets for the R007 operation-language route.

For f(X)=sum a_k X^k and an input p-adic valuation shell j, set

    lambda_k(j) = v_p(a_k) + k*j,
    m(j)        = min_k lambda_k(j).

After writing n=p^j*u with u a unit and factoring p^m from f(n), the first
residue digit is the initial-form polynomial formed by the terms attaining m.
Phase can affect the output valuation only at a shell where this initial form
has a unit root; in particular, such a shell must be a lower-envelope tie.

If deg(f) < p-1, the initial form cannot vanish on every unit of F_p.  Hence
f descends through the truncated valuation shadow modulo p^beta iff every
visible initial form is root-free on F_p^*.  Since a degree-d lower envelope
has at most d tie depths, all first-order phase defects are localized to at
most d valuation shells, independently of beta.
"""

from __future__ import annotations

from typing import NamedTuple

INF = 10**12


def p_adic_valuation(n: int, p: int) -> int:
    if p < 2:
        raise ValueError("p must be at least 2")
    if n == 0:
        return INF
    n = abs(n)
    value = 0
    while n % p == 0:
        n //= p
        value += 1
    return value


def truncated_valuation(n: int, p: int, beta: int) -> int:
    if beta < 0:
        raise ValueError("beta must be nonnegative")
    if n == 0:
        return beta
    return min(p_adic_valuation(n, p), beta)


def polynomial_degree(coefficients: tuple[int, ...]) -> int:
    degree = len(coefficients) - 1
    while degree >= 0 and coefficients[degree] == 0:
        degree -= 1
    return degree


def polynomial_eval(coefficients: tuple[int, ...], x: int) -> int:
    value = 0
    for coefficient in reversed(coefficients):
        value = value * x + coefficient
    return value


class ShellNewtonData(NamedTuple):
    depth: int
    minimum: int
    minimizers: tuple[int, ...]


def shell_newton_data(
    coefficients: tuple[int, ...], p: int, depth: int
) -> ShellNewtonData:
    degree = polynomial_degree(coefficients)
    if degree < 0:
        return ShellNewtonData(depth, INF, tuple())
    weights = [
        p_adic_valuation(coefficients[k], p) + k * depth
        for k in range(degree + 1)
    ]
    minimum = min(weights)
    minimizers = tuple(k for k, weight in enumerate(weights) if weight == minimum)
    return ShellNewtonData(depth, minimum, minimizers)


def initial_form_value(
    coefficients: tuple[int, ...], p: int, depth: int, unit_residue: int
) -> int:
    if unit_residue % p == 0:
        raise ValueError("unit_residue must be nonzero modulo p")
    data = shell_newton_data(coefficients, p, depth)
    if data.minimum >= INF:
        return 0
    total = 0
    for k in data.minimizers:
        coefficient = coefficients[k]
        valuation = p_adic_valuation(coefficient, p)
        unit_coefficient = (coefficient // (p**valuation)) % p
        total = (total + unit_coefficient * pow(unit_residue, k, p)) % p
    return total


def initial_form_unit_roots(
    coefficients: tuple[int, ...], p: int, depth: int
) -> frozenset[int]:
    return frozenset(
        unit
        for unit in range(1, p)
        if initial_form_value(coefficients, p, depth, unit) == 0
    )


def tropical_tie_shells(
    coefficients: tuple[int, ...], p: int, beta: int
) -> tuple[int, ...]:
    out: list[int] = []
    for depth in range(beta):
        data = shell_newton_data(coefficients, p, depth)
        if data.minimum < beta and len(data.minimizers) >= 2:
            out.append(depth)
    return tuple(out)


def phase_defect_candidate_shells(
    coefficients: tuple[int, ...], p: int, beta: int
) -> tuple[int, ...]:
    out: list[int] = []
    for depth in tropical_tie_shells(coefficients, p, beta):
        if initial_form_unit_roots(coefficients, p, depth):
            out.append(depth)
    return tuple(out)


def polynomial_shadow_descends_bruteforce(
    coefficients: tuple[int, ...], p: int, beta: int
) -> bool:
    modulus = p**beta
    outputs: dict[int, int] = {}
    for residue in range(modulus):
        input_depth = truncated_valuation(residue % modulus, p, beta)
        output_depth = truncated_valuation(
            polynomial_eval(coefficients, residue) % modulus, p, beta
        )
        old = outputs.setdefault(input_depth, output_depth)
        if old != output_depth:
            return False
    return True


def low_degree_shadow_descent_criterion(
    coefficients: tuple[int, ...], p: int, beta: int
) -> bool:
    degree = polynomial_degree(coefficients)
    if degree < 0:
        return True
    if degree >= p - 1:
        raise ValueError("criterion requires deg(f) < p-1")
    for depth in range(beta):
        data = shell_newton_data(coefficients, p, depth)
        if data.minimum >= beta:
            continue
        if initial_form_unit_roots(coefficients, p, depth):
            return False
    return True


def tie_shell_bound_holds(coefficients: tuple[int, ...], p: int, beta: int) -> bool:
    degree = max(polynomial_degree(coefficients), 0)
    return len(tropical_tie_shells(coefficients, p, beta)) <= degree


def quadratic_x2_plus_c_shadow_descends(c: int, p: int, beta: int) -> bool:
    if p <= 3:
        raise ValueError("closed quadratic criterion requires p>3")
    if c == 0:
        return True
    h = p_adic_valuation(c, p)
    if h >= beta or h % 2:
        return True
    depth = h // 2
    if depth >= beta:
        return True
    normalized = (c // (p**h)) % p
    return all((unit * unit + normalized) % p != 0 for unit in range(1, p))
