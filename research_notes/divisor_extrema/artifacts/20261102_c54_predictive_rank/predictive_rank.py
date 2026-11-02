"""C54: exact score-matched continuation tables and predictive-rank tests.

Population is a finite multiset of prime labels, not a physical time process.
Positive probabilities retain signed score labels; terminal selection is
allowed to depend on the score, and is removed only by proved invariants.
"""
from __future__ import annotations
from collections import defaultdict
from fractions import Fraction as F
from functools import lru_cache
from itertools import permutations
from math import factorial
from pathlib import Path
from typing import Callable, Mapping, Sequence
import sys

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT / 'inherited' / 'c53'))
import history_memory as inherited

PRIMES = (2, 3, 5, 7)
COUNTS = (4, 2, 2, 1)
HISTORIES = tuple(inherited.word(s) for s in ('223322', '232232', '322223'))
TAILS = tuple(inherited.word(s) for s in ('557', '575', '755'))
SCORES = inherited.scores_for_counts
DELTA = {(0, 1): 1, (0, 2): -1, (0, 3): 1,
         (1, 2): 1, (1, 3): -1}


def state_after(word: Sequence[int]) -> int:
    """Number of trailing visible 2s, capped at two; 3 resets, 5/7 preserve."""
    state = 0
    for symbol in word:
        if symbol == 0:
            state = min(2, state + 1)
        elif symbol == 1:
            state = 0
    return state


def state_rates(state: int, x: F, y: F, z: Sequence[F]) -> tuple[F, ...]:
    return x, y, z[state], F(1)


def reference_word(word: Sequence[int], x: F = F(1), y: F = F(1),
                   z: Sequence[F] = (F(1, 4), F(1), F(4))) -> F:
    """Reference word probability for the explicit three-state preparation."""
    if x <= 0 or y <= 0 or len(z) != 3 or any(a <= 0 for a in z):
        raise ValueError('All preparation rates must be positive')
    remaining = [word.count(i) for i in range(4)]
    state, result = 0, F(1)
    for symbol in word:
        rates = state_rates(state, x, y, z)
        total = sum(rates[i] * remaining[i] for i in range(4))
        result *= rates[symbol] * remaining[symbol] / total
        remaining[symbol] -= 1
        if symbol == 0:
            state = min(2, state + 1)
        elif symbol == 1:
            state = 0
    return result


def reference_histogram(counts: tuple[int, ...], x: F, y: F,
                        z: Sequence[F]) -> dict[tuple[int, int], F]:
    """DP quotient proved sufficient for this transition and final score law."""
    states = {((0, 0, 0, 0), 0, 0, 0): F(1)}
    for _ in range(sum(counts)):
        out = defaultdict(F)
        for (used, ar, br, state), mass in states.items():
            remaining = [counts[i] - used[i] for i in range(4)]
            rates = state_rates(state, x, y, z)
            total = sum(rates[i] * remaining[i] for i in range(4))
            for symbol, amount in enumerate(remaining):
                if not amount:
                    continue
                nxt = list(used)
                nxt[symbol] += 1
                da = 2 * sum(used[i] * DELTA.get((i, symbol), 0)
                             for i in range(symbol))
                db = 2 * used[2] if symbol == 3 else 0
                ns = min(2, state + 1) if symbol == 0 else 0 if symbol == 1 else state
                out[(tuple(nxt), ar + da, br + db, ns)] += (
                    mass * rates[symbol] * amount / total)
        states = dict(out)
    offset_a = sum(counts[i] * counts[j] * v for (i, j), v in DELTA.items())
    offset_b = counts[2] * counts[3]
    result = defaultdict(F)
    for (used, ar, br, state), mass in states.items():
        result[ar - offset_a, br - offset_b] += mass
    return dict(result)


def selected_law(base: Mapping[tuple[int, ...], F],
                 weight: Callable[[int, int], F], use_brc: bool = False):
    masses = {}
    total = inherited.native.weight_histogram([]) if use_brc else F(0)
    operations = 0
    for word, probability in base.items():
        terminal = weight(*SCORES(word))
        if terminal <= 0:
            raise ValueError('Strictly positive terminal weights required')
        if use_brc:
            weighted = inherited.native.histogram_serial(
                inherited.native.weight_histogram([probability]),
                inherited.native.weight_histogram([terminal]))
            total = inherited.native.histogram_recoalesce(total, weighted)
            masses[word] = weighted.total_mass
            operations += 2
        else:
            masses[word] = probability * terminal
            total += masses[word]
    normalizer = total.total_mass if use_brc else total
    return {word: mass / normalizer for word, mass in masses.items()}, operations


def table(law: Mapping[tuple[int, ...], F], histories=HISTORIES, tails=TAILS):
    return [[law[h + c] for c in tails] for h in histories]


def determinant(matrix: Sequence[Sequence[F]]) -> F:
    """Exact Gaussian elimination; ordinary matrix rank is used, not NMF."""
    a = [list(map(F, row)) for row in matrix]
    n = len(a)
    if any(len(row) != n for row in a):
        raise ValueError('Square matrix required')
    result = F(1)
    for col in range(n):
        pivot = next((i for i in range(col, n) if a[i][col]), None)
        if pivot is None:
            return F(0)
        if pivot != col:
            a[col], a[pivot] = a[pivot], a[col]
            result = -result
        pv = a[col][col]
        result *= pv
        for row in range(col + 1, n):
            factor = a[row][col] / pv
            for j in range(col + 1, n):
                a[row][j] -= factor * a[col][j]
    return result


def canonical_table(matrix: Sequence[Sequence[F]]):
    """Remove positive row and column scalings using the first row/column."""
    return [[x * matrix[0][0] / (matrix[i][0] * matrix[0][j])
             for j, x in enumerate(row)] for i, row in enumerate(matrix)]


def signed_sums3(a: Sequence[Sequence[F]]) -> tuple[F, F]:
    pos = a[0][0]*a[1][1]*a[2][2] + a[0][1]*a[1][2]*a[2][0] + a[0][2]*a[1][0]*a[2][1]
    neg = a[0][2]*a[1][1]*a[2][0] + a[0][1]*a[1][0]*a[2][2] + a[0][0]*a[1][2]*a[2][1]
    return pos, neg


def invariant_ratio(matrix):
    positive, negative = signed_sums3(matrix)
    return positive / negative


def error_box(ratio: F, relative_error: F) -> tuple[F, F]:
    """Nine entrywise relative budgets, stated relative to displayed centers."""
    if not 0 <= relative_error < 1:
        raise ValueError('Require 0 <= relative error < 1')
    factor = ((1 + relative_error)/(1 - relative_error))**3
    return ratio / factor, ratio * factor


def suffix_probability(repetitions: int, before_singleton: int, rate: F) -> F:
    """PL probability of 5^j 7 5^(r-j), ratio lambda5/lambda7=rate."""
    if not 0 <= before_singleton <= repetitions or rate <= 0:
        raise ValueError('Invalid tail or rate')
    probability = F(1)
    for remaining in range(repetitions, repetitions-before_singleton, -1):
        probability *= remaining * rate / (1 + remaining * rate)
    return probability / (1 + (repetitions-before_singleton) * rate)


def suffix_determinant_formula(rates: Sequence[F]) -> F:
    """Columns j=0,...,r, with r+1 distinct positive rate ratios."""
    r = len(rates) - 1
    factor = F(1)
    for j in range(r + 1):
        factor *= F(factorial(r), factorial(r-j))
    for j in range(r + 1):
        for i in range(j):
            factor *= rates[j] - rates[i]
    for rate in rates:
        for k in range(1, r + 1):
            factor /= 1 + k*rate
    return factor


@lru_cache(None)
def inversion_counts(a: int, b: int) -> tuple[int, ...]:
    """Coefficient counts for binary words with a first-type, b second-type."""
    if a == 0 or b == 0:
        return (1,)
    result = [0] * (a*b + 1)
    for i, amount in enumerate(inversion_counts(a-1, b)):
        result[i] += amount
    for i, amount in enumerate(inversion_counts(a, b-1)):
        result[i+a] += amount
    return tuple(result)


def minimum_carrier(k: int, upper_bound: int):
    """Minimum matching-table capacity in the declared two+two-prime design.

    Hidden tail multiplicities k-1,1 suffice and are minimal.  The product
    lower bound 2^(a+b+k) limits all candidate visible counts under the
    supplied feasible upper bound; larger candidates cannot improve it.
    This is capacity of a score-matched k by k table, not an unconditional
    rank guarantee for every probability model on that table.
    """
    r = k - 1
    max_sum = upper_bound.bit_length() - 1 - r - 1
    best = None
    examined = 0
    for a in range(1, max_sum):
        for b in range(1, min(a, max_sum-a) + 1):
            examined += 1
            mult = max(inversion_counts(a, b))
            if mult < k:
                continue
            exponents = sorted((a, b, r, 1), reverse=True)
            n = 1
            for prime, exponent in zip(PRIMES, exponents):
                n *= prime**exponent
            if n <= upper_bound and (best is None or n < best['integer']):
                best = {'integer': n, 'visible_counts': (a, b),
                        'hidden_counts': (r, 1), 'ordered_exponents': exponents,
                        'collision_size': mult}
    if best is None:
        raise ValueError('No feasible carrier inside bound')
    best['candidates_examined'] = examined
    return best


def serialize(obj):
    if isinstance(obj, F):
        return {'n': obj.numerator, 'd': obj.denominator, 'approx': float(obj)}
    if isinstance(obj, dict):
        return {str(k): serialize(v) for k, v in obj.items()}
    if isinstance(obj, (tuple, list)):
        return [serialize(v) for v in obj]
    return obj
