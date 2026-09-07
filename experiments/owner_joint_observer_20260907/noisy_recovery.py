"""Finite-carrier, budgeted raw X6 fitting by existing exact Phase-I feasibility.

This composes the current BRC observer and rational solver; it does not add a
solver, a BRC family, an optimizer, or a Foundation theorem. For every labeled
address in candidate projections UNION explicitly supplied noise, compile

    A nu + r_plus - r_minus = y,
    sum(r_plus + r_minus) + slack = residual_budget,

with all variables nonnegative. These equations are feasible exactly when a
nonnegative measure on the declared finite carrier has stacked l1 residual at
most the budget. Missing addresses are zero, including candidate projections
absent from the data. Noise may be negative or have inconsistent table totals.

A successful fit is checked against the original compiled equations and its
ACTUAL residual is separately rebuilt through the existing BRC observer. It
need not minimize residual or be unique. A Farkas failure concerns only this
carrier and budget. Resource limits and solver failures yield no such claim.
"""
from __future__ import annotations

from collections.abc import Iterable, Mapping
from fractions import Fraction
from itertools import combinations

from exact_feasibility import solve_nonnegative, verify_certificate
from observer_certificate import Branch, all_three_axis_tables

AXES = tuple(combinations(range(6), 3))
STABILITY_CONSTANT = Fraction(111, 20)


class NoiseFitResourceLimitError(RuntimeError):
    """A declared size limit was reached; no mathematical conclusion."""


class InfeasibleNoiseBudgetError(ValueError):
    """Verified Farkas obstruction for the given carrier AND residual budget."""

    def __init__(self, rows, rhs, candidates, residual_budget, observation_rows, certificate):
        super().__init__("verified Farkas certificate: no fit on the declared carrier within the declared residual budget")
        self.rows = rows
        self.rhs = rhs
        self.candidates = candidates
        self.residual_budget = residual_budget
        self.observation_rows = observation_rows
        self.certificate = certificate
        self.scope = "DECLARED_FINITE_CARRIER_AND_RESIDUAL_BUDGET_ONLY"


def _exact(value, name):
    if isinstance(value, bool) or not isinstance(value, (int, Fraction)):
        raise TypeError(f"{name} must be exact int or Fraction, never float or bool")
    return Fraction(value)


def _nonnegative(value, name):
    value = _exact(value, name)
    if value < 0:
        raise ValueError(f"{name} must be nonnegative")
    return value


def _limit(value, name):
    if type(value) is not int or value < 0:
        raise ValueError(f"{name} must be a nonnegative integer")
    return value


def fit_budgeted_noise(
    noisy_tables: Mapping,
    candidate_cells: Iterable,
    *,
    residual_budget: int | Fraction,
    truth_noise_budget: int | Fraction | None = None,
    max_candidates: int = 64,
    max_observations: int = 512,
    max_tableau_entries: int = 500_000,
) -> dict:
    """Return a certified feasible fit, or a carrier/budget-scoped obstruction.

    All 20 sorted zero-based axis triples must be present. Their finite tables
    map raw signed integer triples to exact rational (possibly negative) data.
    Candidate Cells are distinct tuple/list six-integer addresses in one common
    X6 anchor chart; their coordinates are copied before use.

    If truth_noise_budget=epsilon is supplied, the returned conditional bound
    is (111/20)*(epsilon + actual_stacked_l1_residual). This assumes an unknown
    finite nonnegative truth mu with <=7 distinct spatial support points, the
    SAME anchor/axis/raw observer, and ||M mu-y||_stack,1 <= epsilon. These truth
    premises are NOT verified by this function. Truth support need not lie in
    candidate_cells for this conditional bound to hold after a successful fit;
    without that membership, existence of a fit is not guaranteed.

    Size caps are checked before dense compilation/solver invocation. The
    tableau cap counts (constraint rows)*(variables + artificial columns + rhs).
    It is not a wall-time, pivot, Fraction-bit-length, or total-memory guarantee.
    Runtime/interrupt/resource exceptions propagate without becoming infeasible.
    """
    budget = _nonnegative(residual_budget, "residual_budget")
    epsilon = None if truth_noise_budget is None else _nonnegative(truth_noise_budget, "truth_noise_budget")
    max_candidates = _limit(max_candidates, "max_candidates")
    max_observations = _limit(max_observations, "max_observations")
    max_tableau_entries = _limit(max_tableau_entries, "max_tableau_entries")

    if not isinstance(noisy_tables, Mapping):
        raise TypeError("noisy_tables must be a mapping")
    if any(not isinstance(axes, tuple) or len(axes) != 3
           or any(type(axis) is not int for axis in axes) or axes not in AXES
           for axes in noisy_tables):
        raise ValueError("axis labels must be sorted triples of distinct integer axes")
    if set(noisy_tables) != set(AXES):
        raise ValueError("exactly 20 labeled raw three-axis tables are required")

    # Retain explicit zeros as well: the compiled address population is declared
    # independently of whether an observed value happens to be zero.
    tables = {}
    observations = set()
    for axes in AXES:
        if not isinstance(noisy_tables[axes], Mapping):
            raise TypeError("each noisy table must be a mapping")
        table = {}
        for address, value in noisy_tables[axes].items():
            if not isinstance(address, tuple) or len(address) != 3 or any(type(v) is not int for v in address):
                raise ValueError("raw addresses must be three signed integers")
            observations.add((axes, address))
            if len(observations) > max_observations:
                raise NoiseFitResourceLimitError("observation budget exceeded; no mathematical conclusion")
            table[address] = _exact(value, "noise table entry")
        tables[axes] = table

    candidates = []
    seen = set()
    for coordinate in candidate_cells:
        if len(candidates) >= max_candidates:
            raise NoiseFitResourceLimitError("candidate budget exceeded; no mathematical conclusion")
        if not isinstance(coordinate, (tuple, list)) or len(coordinate) != 6 or any(type(v) is not int for v in coordinate):
            raise ValueError("candidate Cells must have six signed integer coordinates")
        coordinate = tuple(coordinate)
        if coordinate in seen:
            raise ValueError("candidate Cells must be distinct")
        seen.add(coordinate)
        candidates.append(coordinate)
        for axes in AXES:
            observations.add((axes, tuple(coordinate[i] for i in axes)))
            if len(observations) > max_observations:
                raise NoiseFitResourceLimitError("observation budget exceeded; no mathematical conclusion")
    candidates = tuple(candidates)
    observation_rows = tuple(sorted(observations))
    count, observed = len(candidates), len(observation_rows)
    width = count + 2 * observed + 1
    height = observed + 1
    tableau_entries = height * (width + height + 1)
    if tableau_entries > max_tableau_entries:
        raise NoiseFitResourceLimitError("dense Phase-I tableau budget exceeded; no mathematical conclusion")

    rows, rhs = [], []
    for i, (axes, address) in enumerate(observation_rows):
        row = [int(tuple(coordinate[j] for j in axes) == address) for coordinate in candidates]
        row += [int(j == i) for j in range(observed)]
        row += [-int(j == i) for j in range(observed)]
        row.append(0)
        rows.append(tuple(row))
        rhs.append(tables[axes].get(address, Fraction(0)))
    rows.append((0,) * count + (1,) * (2 * observed) + (1,))
    rhs.append(budget)
    rows, rhs = tuple(rows), tuple(rhs)

    certificate = solve_nonnegative(rows, rhs)
    if not verify_certificate(rows, rhs, certificate):
        raise ArithmeticError("noise solver output failed independent compiled-equation certificate verification")
    if certificate.status == "INFEASIBLE":
        raise InfeasibleNoiseBudgetError(rows, rhs, candidates, budget, observation_rows, certificate)

    distribution = tuple((coordinate, Fraction(value)) for coordinate, value
                         in zip(candidates, certificate.primal[:count]) if value)
    recovered = tuple(Branch(f"noise-fit:{i}", coordinate, value)
                      for i, (coordinate, value) in enumerate(distribution))
    fitted_tables = all_three_axis_tables(recovered)
    # This union is independently rebuilt from the actual BRC output and noise,
    # not from the compiler's row list or auxiliary residual-variable objective.
    actual_residual = sum(
        (abs(fitted_tables[axes].get(address, Fraction(0)) - tables[axes].get(address, Fraction(0)))
         for axes in AXES for address in fitted_tables[axes].keys() | tables[axes].keys()),
        Fraction(0),
    )
    if actual_residual > budget:
        raise ArithmeticError("fit failed independent full BRC stacked-l1 residual verification")

    premises = None if epsilon is None else (
        "TRUTH_IS_A_FINITE_NONNEGATIVE_SPATIAL_MASS_DISTRIBUTION",
        "TRUTH_HAS_AT_MOST_SEVEN_DISTINCT_SPATIAL_SUPPORT_POINTS",
        "TRUTH_AND_FIT_USE_THE_SAME_ANCHOR_AND_LABELED_RAW_SIX_AXIS_OBSERVER",
        "TRUTH_STACKED_L1_RESIDUAL_TO_SUPPLIED_NOISY_TABLES_IS_AT_MOST_TRUTH_NOISE_BUDGET",
    )
    return {
        "status": "FEASIBLE_WITHIN_DECLARED_CARRIER_AND_RESIDUAL_BUDGET",
        "distribution": distribution,
        "candidate_cells": candidates,
        "support_count": len(distribution),
        "residual_budget": budget,
        "actual_stacked_l1_residual": actual_residual,
        "certificate": certificate,
        "compiled_matrix": rows,
        "compiled_rhs": rhs,
        "observation_rows": observation_rows,
        "variable_layout": {
            "mass_columns_half_open": (0, count),
            "residual_plus_columns_half_open": (count, count + observed),
            "residual_minus_columns_half_open": (count + observed, count + 2 * observed),
            "slack_column": width - 1,
        },
        "tableau_entries": tableau_entries,
        "certificate_verified_on_compiled_system": True,
        "actual_residual_verified_by_brc": True,
        "optimality_claimed": False,
        "uniqueness_claimed": False,
        "truth_noise_budget": epsilon,
        "truth_premises_verified": False,
        "truth_membership_in_carrier_required_for_bound": False,
        "conditional_l1_bound": None if epsilon is None else STABILITY_CONSTANT * (epsilon + actual_residual),
        "conditional_l1_bound_assumptions": premises,
    }
