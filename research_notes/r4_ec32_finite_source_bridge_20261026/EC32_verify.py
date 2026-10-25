#!/usr/bin/env python3
"""EC32: exact positive-branch BRC word observers and finite-state certificates.

No numerical approximation, external packages, native heartbeat invocation, or phase dynamics.
"""
from __future__ import annotations
import itertools
import json
from fractions import Fraction
from pathlib import Path

ALPHABET = ('A', 'B', 'C')


def words_upto(h: int):
    for k in range(h + 1):
        yield from map(''.join, itertools.product(ALPHABET, repeat=k))


def mat(n: int):
    return [[0] * n for _ in range(n)]


def ec29_model():
    n = 2
    A, B, C = mat(n), mat(n), mat(n)
    for q in range(n):
        A[q][1] = 1       # after A, last-A bit = 1
        B[q][0] = 1       # after B, last-A bit = 0
    C[0][0] = 1
    C[1][0] = 2           # C has two independent positive sources after A
    return {'A': A, 'B': B, 'C': C}, [1, 0], [1, 1]


def permute_two_state(model):
    mats, alpha, beta = model
    pi = (1, 0)
    return ({a: [[M[pi[i]][pi[j]] for j in range(2)] for i in range(2)]
             for a, M in mats.items()},
            [alpha[i] for i in pi], [beta[i] for i in pi])


def base_model():
    return ({a: [[1]] for a in ALPHABET}, [1], [1])


def delayed_source_model(H: int):
    assert H >= 1
    n = H + 1
    A, B, C = mat(n), mat(n), mat(n)
    for r in range(n):
        A[r][min(H, r + 1)] = 1
        B[r][0] = 1
        C[r][0] = 2 if r == H else 1
    return {'A': A, 'B': B, 'C': C}, [1] + [0] * H, [1] * n


def row_step(row, M):
    n = len(row)
    return [sum(row[i] * M[i][j] for i in range(n)) for j in range(n)]


def count_word(model, word):
    matrices, alpha, beta = model
    row = alpha[:]
    for a in word:
        row = row_step(row, matrices[a])
    return sum(x * y for x, y in zip(row, beta))


def ec29_combinatorial(word, q):
    mult = 1
    for a in word:
        if a == 'C' and q == 1:
            mult *= 2
        q = int(a == 'A')
    return mult


def delayed_combinatorial(word, H):
    run = 0
    mult = 1
    for a in word:
        if a == 'A':
            run = min(H, run + 1)
        else:
            if a == 'C' and run == H:
                mult *= 2
            run = 0
    return mult


def block_difference(M1, M2):
    m, n = len(M1), len(M2)
    out = mat(m + n)
    for i in range(m):
        for j in range(m):
            out[i][j] = M1[i][j]
    for i in range(n):
        for j in range(n):
            out[m + i][m + j] = M2[i][j]
    return out


def rational_basis_certificate(model1, model2):
    mats1, alpha1, beta1 = model1
    mats2, alpha2, beta2 = model2
    mats = {a: block_difference(mats1[a], mats2[a]) for a in ALPHABET}
    alpha = tuple(Fraction(x) for x in (alpha1 + [-x for x in alpha2]))
    beta = tuple(beta1 + beta2)
    basis = []
    pivots = []
    pending = []
    observed = 0

    def add(v, w):
        z = [Fraction(x) for x in v]
        for pivot, row in sorted(zip(pivots, basis), key=lambda p: p[0]):
            if z[pivot]:
                k = z[pivot]
                z = [a - k * b for a, b in zip(z, row)]
        nonzero = next((i for i, z_i in enumerate(z) if z_i), None)
        if nonzero is None:
            return False
        k = z[nonzero]
        pivots.append(nonzero)
        basis.append(tuple(a / k for a in z))
        pending.append((tuple(v), w))
        return True

    add(alpha, '')
    witness = None
    max_basis_word_length = 0
    while pending:
        v, w = pending.pop(0)
        observed += 1
        max_basis_word_length = max(max_basis_word_length, len(w))
        value = sum(x * y for x, y in zip(v, beta))
        if value and witness is None:
            witness = {'word': w, 'difference_first_minus_second': int(value), 'length': len(w)}
        for a in ALPHABET:
            add(tuple(row_step(v, mats[a])), w + a)
    dim_bound = len(alpha)
    assert len(basis) <= dim_bound
    assert max_basis_word_length <= dim_bound - 1
    return {'dimension_bound': dim_bound, 'reachable_rank': len(basis),
            'basis_vectors_checked': observed, 'maximum_basis_word_length': max_basis_word_length,
            'equivalent_all_words': witness is None, 'first_basis_nonzero': witness}


def verify():
    ec29 = ec29_model()
    ec29_swapped = permute_two_state(ec29)
    count_checks = 0
    for w in words_upto(7):
        x = count_word(ec29, w)
        assert x == ec29_combinatorial(w, 0)
        assert x == count_word(ec29_swapped, w)
        count_checks += 1
    ec29_q1_checks = 0
    m, _, b = ec29
    q1 = (m, [0, 1], b)
    for w in words_upto(7):
        assert count_word(q1, w) == ec29_combinatorial(w, 1)
        ec29_q1_checks += 1
    permuted_cert = rational_basis_certificate(ec29, ec29_swapped)
    assert permuted_cert['equivalent_all_words']

    cases = []
    aggregate_word_checks = 0
    for H in range(1, 9):
        baseline, late = base_model(), delayed_source_model(H)
        checks = 0
        for w in words_upto(H):
            assert count_word(baseline, w) == 1
            assert count_word(late, w) == delayed_combinatorial(w, H) == 1
            checks += 1
        witness = 'A' * H + 'C'
        assert count_word(late, witness) == delayed_combinatorial(witness, H) == 2
        assert count_word(baseline, witness) == 1
        cert = rational_basis_certificate(late, baseline)
        assert cert['dimension_bound'] == H + 2
        assert cert['reachable_rank'] <= H + 2
        assert cert['first_basis_nonzero'] is not None
        assert cert['first_basis_nonzero']['length'] == H + 1
        assert not cert['equivalent_all_words']
        aggregate_word_checks += checks + 1
        cases.append({'H': H, 'models_dimensions': [H + 1, 1],
                      'finite_certificate_cutoff': H + 1,
                      'matching_short_words': checks, 'first_counterexample': witness,
                      'baseline_weight': 1, 'delayed_weight': 2, 'span_certificate': cert})

    return {'schema': 'EM_R4_EC32_EXACT_VERIFY_V1', 'status': 'PASS',
            'runtime': 'CPython, standard library Fraction, exact integers',
            'scope': 'finite positive-source word-weighted automata over {A,B,C}; no native P000 heartbeat evaluation',
            'ec29_direct_word_checks_q0': count_checks,
            'ec29_direct_word_checks_q1': ec29_q1_checks,
            'equivalent_two_state_span_certificate': permuted_cert,
            'delayed_source_cases': cases,
            'aggregate_delayed_counterexample_checks': aggregate_word_checks,
            'all_depth_theorems_from_proof_not_enumeration': True,
            'next_question': 'Obtain actual native X6 source-labelled heartbeat transition, grade, observer and finite-state dimension or a proved bisimulation; then apply a scoped finite cutoff.'}


if __name__ == '__main__':
    report = verify()
    out = Path(__file__).resolve().parent / 'EC32_REPORT.json'
    out.write_text(json.dumps(report, ensure_ascii=False, indent=2, sort_keys=True) + '\n', encoding='utf-8')
    print(json.dumps({'status': report['status'], 'ec29_checks_each_state': report['ec29_direct_word_checks_q0'],
                      'total_delayed_checks': report['aggregate_delayed_counterexample_checks'],
                      'last_case': report['delayed_source_cases'][-1]}, ensure_ascii=False))
