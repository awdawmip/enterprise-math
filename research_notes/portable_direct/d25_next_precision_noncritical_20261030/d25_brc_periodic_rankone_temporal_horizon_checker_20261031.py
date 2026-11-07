#!/usr/bin/env python3
"""Exact integer author-side checks for periodic BRC rank-one observation horizons.

Only auxiliary positive-integer hidden-label systems are checked; no native X6 run.
"""
from __future__ import annotations

from fractions import Fraction
from itertools import product
import json
import random
from pathlib import Path

PORTS = (0, 1)


def dot(a, b):
    return sum(x * y for x, y in zip(a, b))


def mat_vec(row, matrix):
    return [sum(row[i] * matrix[i][j] for i in range(len(row))) for j in range(len(row))]


def raw_history(a, transitions, emissions, word):
    row = list(a)
    p = len(transitions)
    for index, letter in enumerate(word):
        phase = index % p
        weighted = [row[i] * emissions[phase][letter][i] for i in range(len(row))]
        row = mat_vec(weighted, transitions[phase])
    return sum(row)


def scalar_rank_one_formula(a, u, v, emissions, word):
    if not word:
        return sum(a)
    p = len(u)
    K = [sum(x) for x in v]
    first = dot(a, [emissions[0][word[0]][j] * u[0][j]
                    for j in range(len(a))]) * K[0]
    answer = Fraction(first)
    for i in range(1, len(word)):
        s = i % p
        prev = (s - 1) % p
        interaction = sum(v[prev][j] * emissions[s][word[i]][j] * u[s][j]
                          for j in range(len(a)))
        answer *= Fraction(interaction * K[s], K[prev])
    if answer.denominator != 1:
        raise AssertionError('a formally integral history became fractional')
    return answer.numerator


def rank_one_experiment(p):
    a = [1, 2]
    T = [[[1, 1], [1, 1]] for _ in range(p)]
    A = [{0: [1, 1], 1: [1, 1]} for _ in range(p)]
    B = [{0: [1, 1], 1: [1, 1]} for _ in range(p)]
    A[0] = {0: [2, 2], 1: [4, 1]}
    B[0] = {0: [4, 1], 1: [2, 2]}
    checked = 0
    early = 0
    for t in range(p + 2):
        sum_a = sum_b = 0
        for word in product(PORTS, repeat=t):
            va = raw_history(a, T, A, word)
            vb = raw_history(a, T, B, word)
            checked += 1
            sum_a += va
            sum_b += vb
            if t <= p:
                assert va == vb, (p, t, word, va, vb)
                early += 1
            else:
                if word == (0,) * (p + 1):
                    assert va == 6 * (2 ** p) * 4, (p, va)
                    assert vb == 6 * (2 ** p) * 5, (p, vb)
        assert sum_a == sum_b, (p, t, sum_a, sum_b)
    word = (0,) * (p + 1)
    return {
        'period': p,
        'rank_each_phase': 1,
        'first_split_length': p + 1,
        'witness_word': list(word),
        'a_witness_mass': raw_history(a, T, A, word),
        'b_witness_mass': raw_history(a, T, B, word),
        'word_checks': checked,
        'equal_pre_split_checks': early,
    }


def arbitrary_time_experiment(N):
    # One state, T_t = [1] always, with a single temporal observer change.
    # A and B have equal sum_y J_t(y) = 5 for every t.
    emissions_A = [[2, 1, 1, 1] for _ in range(N + 2)]
    emissions_B = [list(v) for v in emissions_A]
    emissions_B[N - 1] = [1, 2, 1, 1]
    a0 = 1
    for t in range(N + 1):
        all_A, all_B = 0, 0
        for word in product(range(4), repeat=t):
            a = a0
            b = a0
            for i, y in enumerate(word):
                a *= emissions_A[i][y]
                b *= emissions_B[i][y]
            all_A += a
            all_B += b
            if t < N:
                assert a == b, (N, t, word)
        assert all_A == all_B == 5 ** t
    w = (0,) * N
    va = 2 ** N
    vb = 2 ** (N - 1)
    return {'first_split': N, 'a_witness_mass': va, 'b_witness_mass': vb,
            'total_mass_each': 5 ** N}


def randomized_rankone_factorization():
    rng = random.Random(20261031)
    cases = 0
    word_checks = 0
    for p in (1, 2, 3, 4):
        for m in (2, 3):
            for _ in range(3):
                a = [rng.randint(1, 5) for _ in range(m)]
                u = [[rng.randint(1, 4) for _ in range(m)] for _ in range(p)]
                v = [[rng.randint(1, 4) for _ in range(m)] for _ in range(p)]
                T = [[[u[s][i] * v[s][j] for j in range(m)]
                      for i in range(m)] for s in range(p)]
                E = [{letter: [rng.randint(1, 5) for _ in range(m)]
                      for letter in PORTS} for _ in range(p)]
                for t in range(p + 4):
                    for word in product(PORTS, repeat=t):
                        assert raw_history(a, T, E, word) == scalar_rank_one_formula(a, u, v, E, word)
                        word_checks += 1
                cases += 1
    return {'parameter_cases': cases, 'history_word_checks': word_checks}



def exact_rank(matrix):
    A = [[Fraction(x) for x in row] for row in matrix]
    if not A:
        return 0
    rank = 0
    for col in range(len(A[0])):
        pivot = next((i for i in range(rank, len(A)) if A[i][col]), None)
        if pivot is None:
            continue
        A[rank], A[pivot] = A[pivot], A[rank]
        scale = A[rank][col]
        A[rank] = [v / scale for v in A[rank]]
        for i in range(len(A)):
            if i != rank and A[i][col]:
                factor = A[i][col]
                A[i] = [x - factor * y for x, y in zip(A[i], A[rank])]
        rank += 1
    return rank


def periodic_phase_lift_check():
    rng = random.Random(2061031)
    total = 0
    word_checks = 0
    for p in (2, 3):
        for m in (2, 3):
            for _ in range(3):
                a = [rng.randint(1, 4) for _ in range(m)]
                T = [[[rng.randint(1, 4) for _ in range(m)]
                      for _ in range(m)] for _ in range(p)]
                E = [{letter: [rng.randint(1, 4) for _ in range(m)]
                      for letter in PORTS} for _ in range(p)]
                lifted = {}
                for letter in PORTS:
                    matrix = [[0] * (p * m) for _ in range(p * m)]
                    for phase in range(p):
                        nxt = (phase + 1) % p
                        for i in range(m):
                            for j in range(m):
                                matrix[phase * m + i][nxt * m + j] = E[phase][letter][i] * T[phase][i][j]
                    lifted[letter] = matrix
                phase_T = [[0] * (p * m) for _ in range(p * m)]
                for phase in range(p):
                    nxt = (phase + 1) % p
                    for i in range(m):
                        for j in range(m):
                            phase_T[phase * m + i][nxt * m + j] = T[phase][i][j]
                assert exact_rank(phase_T) == sum(exact_rank(x) for x in T)
                for t in range(p + 4):
                    for word in product(PORTS, repeat=t):
                        row = list(a) + [0] * ((p - 1) * m)
                        for letter in word:
                            row = mat_vec(row, lifted[letter])
                        assert sum(row) == raw_history(a, T, E, word)
                        word_checks += 1
                total += 1
    return {'cases': total, 'lifted_word_checks': word_checks, 'exact_rank_checks': total}


def main():
    sharp = [rank_one_experiment(p) for p in range(1, 8)]
    delay = [arbitrary_time_experiment(N) for N in range(1, 7)]
    fact = randomized_rankone_factorization()
    lifted = periodic_phase_lift_check()
    result = {
        'schema': 'D25_BRC_PERIODIC_TEMPORAL_RANKONE_AUTHOR_CHECK_V1',
        'date': '2026-10-31',
        'status': 'AUTHOR_EXACT_CHECKED_NOT_NATIVE_UNREVIEWED',
        'checks': {
            'sharp_periodic': sharp,
            'nonperiodic_delay': delay,
            'rankone_factorization': fact,
            'periodic_phase_lift': lifted,
            'total_periodic_word_checks': sum(x['word_checks'] for x in sharp),
            'total_pre_split_equalities': sum(x['equal_pre_split_checks'] for x in sharp),
        },
        'verdict': 'PASS',
    }
    dest = Path(__file__).with_name('d25_brc_periodic_rankone_temporal_horizon_author_check_20261031.json')
    dest.write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print(json.dumps({'verdict': result['verdict'], 'periods': [x['period'] for x in sharp],
                      'periodic_word_checks': result['checks']['total_periodic_word_checks'],
                      'pre_split_equalities': result['checks']['total_pre_split_equalities'],
                      **fact, **lifted, 'output': str(dest)}, ensure_ascii=False))


if __name__ == '__main__':
    main()
