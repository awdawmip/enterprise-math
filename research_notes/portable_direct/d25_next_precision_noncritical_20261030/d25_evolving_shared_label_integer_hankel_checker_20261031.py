#!/usr/bin/env python3
"""Exact-integer author checks for finite evolving shared-label BRC observers.

All path counts are nonnegative integers. Rational arithmetic is used solely
for the proof-certificate linear-independence test, never as path weights.
"""
from fractions import Fraction
from itertools import product
import json
from pathlib import Path

P = (4, 4, 4, 4)
Z = (1, -1, -1, 1)
ALPHABET = range(4)


def vec_rank(columns):
    """Rank over Q of columns, with exact Gaussian elimination."""
    if not columns:
        return 0
    n = len(columns[0])
    a = [[Fraction(col[i]) for col in columns] for i in range(n)]
    pivot_row = 0
    for col in range(len(columns)):
        pivot = next((i for i in range(pivot_row, n) if a[i][col]), None)
        if pivot is None:
            continue
        a[pivot_row], a[pivot] = a[pivot], a[pivot_row]
        pivot_val = a[pivot_row][col]
        for j in range(col, len(columns)):
            a[pivot_row][j] /= pivot_val
        for i in range(n):
            if i != pivot_row and a[i][col]:
                factor = a[i][col]
                for j in range(col, len(columns)):
                    a[i][j] -= factor * a[pivot_row][j]
        pivot_row += 1
        if pivot_row == n:
            break
    return pivot_row


def emission(k, y):
    val = P[y] + k * Z[y]
    assert val >= 0
    return val


def word_mass(w, transition, k, word):
    """Independent left-to-right path enumeration by integer DP."""
    n = len(w)
    counts = list(w)
    for y in word:
        after = [0] * n
        for left in range(n):
            for right in range(n):
                after[right] += counts[left] * emission(k[left], y) * transition[left][right]
        counts = after
    return sum(counts)


def linear_basis_certificate(w_a, w_b, transition, k_a, k_b):
    n = len(w_a)
    assert n == len(w_b) == len(transition) == len(k_a) == len(k_b)
    assert all(len(row) == n for row in transition)
    d = 2 * n
    beta = (1,) * d
    alpha = tuple(w_a) + tuple(-x for x in w_b)

    def prepend(y, vec):
        out = [0] * d
        for half, k in ((0, k_a), (1, k_b)):
            for l in range(n):
                out[half * n + l] = emission(k[l], y) * sum(
                    transition[l][r] * vec[half * n + r] for r in range(n)
                )
        return tuple(out)

    queue = [((), beta)]
    vectors = [beta]
    i = 0
    while i < len(queue):
        word, vec = queue[i]
        for y in ALPHABET:
            candidate = prepend(y, vec)
            if vec_rank(vectors + [candidate]) > len(vectors):
                vectors.append(candidate)
                queue.append(((y,) + word, candidate))
        i += 1
    assert len(queue) <= d
    assert max(len(word) for word, _ in queue) <= d - 1
    assert all(vec_rank(vectors + [prepend(y, vec)]) == len(vectors)
               for y in ALPHABET for vec in vectors)
    inner = [sum(a * b for a, b in zip(alpha, vec)) for _, vec in queue]
    assert all(sum(a*b for a,b in zip(alpha, vec)) ==
               word_mass(w_a, transition, k_a, word) -
               word_mass(w_b, transition, k_b, word)
               for word, vec in queue)
    inequivalent = [(word, value) for (word, _), value in zip(queue, inner) if value]
    return {
        'equivalent': not inequivalent,
        'rank': len(queue),
        'basis_words': [''.join(map(str, word)) or 'ε' for word, _ in queue],
        'basis_lengths': [len(word) for word, _ in queue],
        'nonzero_basis_discrepancies': [
            {'word': ''.join(map(str, word)) or 'ε', 'difference': value}
            for word, value in inequivalent
        ],
    }


def brute_equiv_through(w_a, w_b, transition, k_a, k_b, horizon):
    checked = 0
    for t in range(horizon + 1):
        for word in product(ALPHABET, repeat=t):
            checked += 1
            if word_mass(w_a, transition, k_a, word) != word_mass(w_b, transition, k_b, word):
                return False, checked, t, word
    return True, checked, None, None


def distance_at_length(w_a, w_b, transition, k_a, k_b, t):
    l1 = 0
    mass_a = mass_b = 0
    for word in product(ALPHABET, repeat=t):
        va = word_mass(w_a, transition, k_a, word)
        vb = word_mass(w_b, transition, k_b, word)
        l1 += abs(va - vb)
        mass_a += va
        mass_b += vb
    return {'L1':l1, 'mass_a':mass_a, 'mass_b':mass_b}


def run():
    cases = 0
    basis_vs_brute = 0
    max_rank = 0
    for bits in product((0, 1), repeat=4):
        transition = (bits[:2], bits[2:])
        for k_a in product((-1, 0, 1), repeat=2):
            for k_b in product((-1, 0, 1), repeat=2):
                cert = linear_basis_certificate((1,1), (1,1), transition, k_a, k_b)
                equiv, checked, _, _ = brute_equiv_through((1,1), (1,1), transition, k_a, k_b, 3)
                assert equiv == cert['equivalent']
                cases += 1
                basis_vs_brute += checked
                max_rank = max(max_rank, cert['rank'])
    assert cases == 16 * 3**4 == 1296

    reset = ((1,0), (1,0))
    a, b = (1,-1), (-1,1)
    reset0 = distance_at_length((1,1),(1,1),reset,a,b,0)
    reset1 = distance_at_length((1,1),(1,1),reset,a,b,1)
    reset2 = distance_at_length((1,1),(1,1),reset,a,b,2)
    assert reset0['L1'] == reset1['L1'] == 0
    assert reset2 == {'L1':256, 'mass_a':512, 'mass_b':512}
    assert sorted(a) == sorted(b)

    delayed = ((0,1,0),(0,0,1),(0,0,1))
    d_a,d_b = (0,0,1),(0,0,-1)
    delay_stats = [distance_at_length((1,0,0),(1,0,0),delayed,d_a,d_b,t)
                   for t in range(4)]
    assert [x['L1'] for x in delay_stats] == [0,0,0,2048]
    assert delay_stats[3]['mass_a'] == delay_stats[3]['mass_b'] == 4096

    # Full arithmetic witness on three labels and 5-event theorem horizon.
    three_label = linear_basis_certificate((1,0,0),(1,0,0),delayed,d_a,d_b)
    brute, exhaustive, first_len, first_word = brute_equiv_through(
        (1,0,0),(1,0,0),delayed,d_a,d_b,5)
    assert not brute and first_len == 3 and not three_label['equivalent']
    assert all(x['mass_a'] == x['mass_b'] == (16**t) for t,x in enumerate(delay_stats))

    # 48 additional three-label dynamic and reset test comparisons through 5 events.
    probes = 0
    for transpose in ((0,1,0),(1,2,0),(2,0,1)):
        for k_a in ((1,0,-1),(-1,1,0),(0,0,0),(1,1,-1)):
            for k_b in ((0,0,0),(1,0,-1),(-1,-1,1),(0,1,-1)):
                T = tuple(tuple(int(col == transpose[row]) for col in range(3)) for row in range(3))
                cert = linear_basis_certificate((1,1,1),(1,1,1),T,k_a,k_b)
                equiv, _, _, _ = brute_equiv_through((1,1,1),(1,1,1),T,k_a,k_b,5)
                assert equiv == cert['equivalent']
                probes += 1
    assert probes == 48

    return {
        'status':'PASS',
        'classification':'AUTHOR_EXACT_CHECKED_UNREVIEWED_NOT_ADMITTED_NOT_NATIVE',
        'date':'2026-10-31',
        'model':'integer BRC fixed two-source 2x2 emission couplings; evolving finite shared label with full post-emission integer transitions',
        'general_bound':'all words length at most m_A+m_B-1; same m gives 2m-1',
        'exact_span_proof':'Q-linear column closure of block difference representation; never signed BRC path counts',
        'exhaustive_binary_transition_parameter_tests':cases,
        'exact_ground_truth_words_examined_until_first_difference':basis_vs_brute,
        'max_basis_rank_in_exhaustive_cases':max_rank,
        'three_label_full_horizon_5_comparisons':probes,
        'reset_counterexample':{
            'initial_weights':(1,1), 'k_A':a,'k_B':b,'transition':reset,
            'same_initial_histogram':True,'length_0':reset0,'length_1':reset1,'length_2':reset2,
            'basis_certificate':linear_basis_certificate((1,1),(1,1),reset,a,b)
        },
        'delayed_counterexample':{
            'initial_weights':(1,0,0),'k_A':d_a,'k_B':d_b,
            'transition':delayed, 'length_0_3':delay_stats,
            'first_difference_length':3,
            'basis_certificate':three_label,
            'first_distinguishing_word':''.join(map(str,first_word)),
        },
        'scope':['finite label set','integer nonnegative path kernels','fully observed ordered time words','fixed observer and post-emission label transition law','author computation only'],
    }

if __name__ == '__main__':
    result = run()
    output = Path(__file__).with_name('d25_evolving_shared_label_integer_hankel_author_check_20261031.json')
    output.write_text(json.dumps(result,indent=2,ensure_ascii=False,sort_keys=True)+'\n',encoding='utf-8')
    print(json.dumps({k:v for k,v in result.items() if k in (
        'status','exhaustive_binary_transition_parameter_tests',
        'exact_ground_truth_words_examined_until_first_difference',
        'max_basis_rank_in_exhaustive_cases','three_label_full_horizon_5_comparisons')},sort_keys=True))
