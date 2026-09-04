"""Task-local graded finite-state S4-equivariant first-return RG checker.

For remaining future horizon h, the exact unlabeled predictive quotient of the
branch-imbalance counter is

    Q_h = {0,1,...,h,FAR_h}.

One branch step lowers the remaining horizon, so the correct finite dynamics is
graded: T_h : Q_h -> weighted subsets of Q_{h-1}.  This makes the far class
operation-safe and yields exact projection/dynamics commutation across horizons.

Tensoring with the 12 K4/FCC unordered diamond positions gives an S4-equivariant
finite state tower X_h = D_12 x Q_h.  The weighted graded kernel reproduces the
Catalan first-return masses, hence every finite F_N used by the post-#1161 AGM
chord/mean RG.
"""

from __future__ import annotations

from fractions import Fraction
from itertools import combinations, permutations
from math import comb


FAR = "FAR"
VERTICES = tuple("ABCD")
GROUP = tuple(permutations(VERTICES))


def add_mass(target: dict[object, Fraction], state: object, mass: Fraction) -> None:
    target[state] = target.get(state, Fraction(0)) + mass


def q(horizon: int, distance: int) -> int | str:
    if horizon < 0 or distance < 0:
        raise ValueError("nonnegative horizon/distance required")
    return distance if distance <= horizon else FAR


def q_states(horizon: int) -> tuple[int | str, ...]:
    return tuple(range(horizon + 1)) + (FAR,)


def project_label(high: int, low: int, state: int | str) -> int | str:
    if not 0 <= low <= high:
        raise ValueError("require 0 <= low <= high")
    if state == FAR:
        return FAR
    if not isinstance(state, int) or not 0 <= state <= high:
        raise ValueError("state not in Q_high")
    return state if state <= low else FAR


def graded_kernel(horizon: int, state: int | str) -> dict[int | str, Fraction]:
    """Weighted one-step map Q_h -> Q_{h-1}, h>=1.

    State zero is absorbing for the verification representation of a first-hit
    observer.  FAR aggregates both branch choices to FAR with total mass one.
    """
    if horizon < 1:
        raise ValueError("graded kernel requires horizon >= 1")
    out: dict[int | str, Fraction] = {}
    if state == 0:
        add_mass(out, 0, Fraction(1))
        return out
    if state == FAR:
        add_mass(out, FAR, Fraction(1))
        return out
    if not isinstance(state, int) or not 1 <= state <= horizon:
        raise ValueError("state not in Q_h")
    add_mass(out, q(horizon - 1, state - 1), Fraction(1, 2))
    add_mass(out, q(horizon - 1, state + 1), Fraction(1, 2))
    return out


def pushforward(
    distribution: dict[object, Fraction],
    mapping,
) -> dict[object, Fraction]:
    out: dict[object, Fraction] = {}
    for state, mass in distribution.items():
        add_mass(out, mapping(state), mass)
    return out


def full_counter_kernel(distance: int) -> dict[int, Fraction]:
    if distance < 0:
        raise ValueError("distance must be nonnegative")
    if distance == 0:
        return {0: Fraction(1)}
    return {
        distance - 1: Fraction(1, 2),
        distance + 1: Fraction(1, 2),
    }


def pmap(p: tuple[str, ...], x: str) -> str:
    return p[VERTICES.index(x)]


def canonical_pair(a: str, b: str) -> tuple[str, str]:
    return tuple(sorted((a, b)))


def diamonds() -> tuple[tuple[str, tuple[str, str]], ...]:
    out = []
    for center in VERTICES:
        leaves = [v for v in VERTICES if v != center]
        for u, v in combinations(leaves, 2):
            out.append((center, canonical_pair(u, v)))
    return tuple(out)


DIAMONDS = diamonds()


def act_diamond(p: tuple[str, ...], d: tuple[str, tuple[str, str]]):
    center, (u, v) = d
    return (pmap(p, center), canonical_pair(pmap(p, u), pmap(p, v)))


def skew_kernel(
    horizon: int,
    state: tuple[tuple[str, tuple[str, str]], int | str],
) -> dict[tuple[tuple[str, tuple[str, str]], int | str], Fraction]:
    d, counter = state
    return {(d, target): mass for target, mass in graded_kernel(horizon, counter).items()}


def catalan(n: int) -> int:
    return comb(2 * n, n) // (n + 1)


def finite_first_return_masses(depth: int) -> list[Fraction]:
    """Return hit masses after the first aggregated step, through total depth N.

    Starting at counter 1 after the first two concrete first-step witnesses have
    recoalesced with total scalar mass one, a first hit after 2n-1 further steps
    has mass f_n=Catalan(n-1)/2^(2n-1).
    """
    if depth < 1:
        raise ValueError("depth must be positive")
    horizon = 2 * depth - 1
    distribution: dict[int | str, Fraction] = {1: Fraction(1)}
    hits: list[Fraction] = []
    for h in range(horizon, 0, -1):
        next_distribution: dict[int | str, Fraction] = {}
        hit = Fraction(0)
        for state, outer_mass in distribution.items():
            for target, transition_mass in graded_kernel(h, state).items():
                mass = outer_mass * transition_mass
                if target == 0:
                    hit += mass
                else:
                    add_mass(next_distribution, target, mass)
        hits.append(hit)
        distribution = next_distribution
    return hits


def run() -> dict[str, object]:
    if len(DIAMONDS) != 12:
        raise AssertionError("expected 12 S4 diamond positions")

    factorization_cases = 0
    naturality_cases = 0
    s4_cases = 0

    # Exact factorization of the infinite counter step through each finite
    # predictive quotient Q_h, and exact inter-horizon transition naturality.
    for h in range(1, 33):
        for distance in range(0, 3 * h + 9):
            lhs = pushforward(full_counter_kernel(distance), lambda d: q(h - 1, d))
            rhs = graded_kernel(h, q(h, distance))
            if lhs != rhs:
                raise AssertionError(f"counter factorization failed at h={h}, d={distance}")
            factorization_cases += 1

        for low in range(1, h + 1):
            for state in q_states(h):
                lhs = pushforward(
                    graded_kernel(h, state),
                    lambda t: project_label(h - 1, low - 1, t),
                )
                rhs = graded_kernel(low, project_label(h, low, state))
                if lhs != rhs:
                    raise AssertionError(
                        f"graded naturality failed at high={h}, low={low}, state={state}"
                    )
                naturality_cases += 1

    # Projection-chain composition.
    projection_cases = 0
    for high in range(0, 33):
        for middle in range(0, high + 1):
            for low in range(0, middle + 1):
                for state in q_states(high):
                    direct = project_label(high, low, state)
                    staged = project_label(middle, low, project_label(high, middle, state))
                    if direct != staged:
                        raise AssertionError("predictive precision projection failed to compose")
                    projection_cases += 1

    # S4 commutes with every graded transition on X_h=D_12 x Q_h.
    for h in range(1, 9):
        for p in GROUP:
            for d in DIAMONDS:
                for counter in q_states(h):
                    state = (d, counter)
                    moved_then_step = skew_kernel(h, (act_diamond(p, d), counter))
                    step_then_moved = {
                        (act_diamond(p, td), tc): mass
                        for (td, tc), mass in skew_kernel(h, state).items()
                    }
                    if moved_then_step != step_then_moved:
                        raise AssertionError("S4/skew transition equivariance failed")
                    s4_cases += 1

    # The finite graded kernel reconstructs every Catalan first-return mass
    # through depth 32 without using a square-root selector.
    hits = finite_first_return_masses(32)
    recovered: list[str] = []
    for n in range(1, 33):
        expected = Fraction(catalan(n - 1), 2 ** (2 * n - 1))
        if hits[2 * n - 2] != expected:
            raise AssertionError(f"first-return mass mismatch at n={n}")
        if 2 * n - 1 < len(hits) and hits[2 * n - 1] != 0:
            raise AssertionError("even-offset first-return mass should vanish")
        if n <= 8:
            recovered.append(str(expected))

    state_counts = [len(DIAMONDS) * len(q_states(h)) for h in range(0, 9)]
    expected_counts = [12 * (h + 2) for h in range(0, 9)]
    if state_counts != expected_counts:
        raise AssertionError("graded S4 state count mismatch")

    return {
        "counter_factorization_cases": factorization_cases,
        "inter_horizon_naturality_cases": naturality_cases,
        "projection_composition_cases": projection_cases,
        "s4_equivariance_cases": s4_cases,
        "first_return_depths_recovered": 32,
        "first_eight_return_masses": recovered,
        "x_h_state_counts_h0_to_h8": state_counts,
    }


if __name__ == "__main__":
    result = run()
    expected = {
        "counter_factorization_cases": 1872,
        "inter_horizon_naturality_cases": 12496,
        "projection_composition_cases": 170170,
        "s4_equivariance_cases": 14976,
        "first_return_depths_recovered": 32,
        "first_eight_return_masses": ["1/2", "1/8", "1/16", "5/128", "7/256", "21/1024", "33/2048", "429/32768"],
        "x_h_state_counts_h0_to_h8": [24, 36, 48, 60, 72, 84, 96, 108, 120],
    }
    if result != expected:
        raise SystemExit(f"unexpected graded S4 return-RG output: {result!r}")
    for key, value in result.items():
        print(f"{key}={value}")
