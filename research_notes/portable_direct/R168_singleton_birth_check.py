#!/usr/bin/env python3
"""Exact, dependency-free verification of R168 singleton collision birth.
Computations use only integers and fractions; finite checks supplement the symbolic theorem.
"""
from fractions import Fraction as Q
import json


def signature_reference(word):
    p = [0]
    for bit in word:
        p.append(p[-1] + int(bit))
    m = len(word)
    alpha, beta = Q(0), Q(1)
    for i in range(m + 1):
        for k in range(i + 1, m + 1):
            alpha = max(alpha, Q(p[k] - p[i] - 1, k - i))
            beta = min(beta, Q(p[k] - p[i] + 1, k - i))
    if alpha >= beta:
        return None
    A = min(Q(p[i] + 1) - i * alpha for i in range(m + 1))
    B = max(Q(p[i]) - i * beta for i in range(m + 1))
    return alpha, beta, A, B


def signature_singleton(n, k):
    """Signature of 0**(k-1) + 1 + 0**(n-k), with 1<=k<=n."""
    assert 1 <= k <= n and n >= 2
    terms = [Q(1), Q(2, n)]
    if k >= 2:
        terms.append(Q(1, k - 1))
    if k < n:
        terms.append(Q(1, n - k))
    beta = min(terms)
    return Q(0), beta, Q(1), max(Q(0), Q(1) - k * beta)


def singleton(n, k):
    return '0' * (k - 1) + '1' + '0' * (n - k)


def main():
    # Independent O(n^2) strip oracle against closed singleton formula.
    reference_count = 0
    for n in range(2, 22):
        for k in range(1, n + 1):
            assert signature_reference(singleton(n, k)) == signature_singleton(n, k), (n, k)
            reference_count += 1
    # For each adjacent position j / j+1, characterize every tested final length.
    exact_collision_tests = 0
    for j in range(1, 16):
        for n in range(j + 1, 3*j + 8):
            a = singleton(n, j + 1)
            b = singleton(n, j)
            ar, br = signature_reference(a), signature_reference(b)
            assert ar == signature_singleton(n, j + 1)
            assert br == signature_singleton(n, j)
            assert (ar == br) == (n == 2*j), (j, n, ar, br)
            exact_collision_tests += 1
    # Large j checks test the closed formula, including all transition cases.
    symbolic_transition_checks = 0
    for j in range(1, 10001):
        ns = sorted(set([j+1, max(j+1,2*j-1), 2*j, 2*j+1, 3*j+1]))
        for n in ns:
            a = signature_singleton(n, j+1)
            b = signature_singleton(n, j)
            assert (a == b) == (n == 2*j), (j,n,a,b)
            symbolic_transition_checks += 1
    output = {
        'record':'R168_SINGLETON_EXACT_COLLISION_BIRTH',
        'status':'AUTHOR_CHECKED_NOT_REVIEWED',
        'arithmetic':'exact fractions',
        'reference_formula_crosschecks':reference_count,
        'exact_full_length_collision_tests':exact_collision_tests,
        'large_j_transition_cases':symbolic_transition_checks,
        'max_j_checked':10000,
        'example_j_4':{
           'at_n_7':[str(x) for x in signature_singleton(7,5)],
           'at_n_8':[str(x) for x in signature_singleton(8,5)],
           'at_n_9':[str(x) for x in signature_singleton(9,5)],
           'at_n_8_other':[str(x) for x in signature_singleton(8,4)]
        },
        'conclusion':'Family has a collision iff n=2j; proof not inferred from finite checks.'
    }
    print('R168_SINGLETON_BIRTH_EXACT_PASS')
    print(json.dumps(output,indent=2,ensure_ascii=False))
    with open('R168_verification.json','w') as f:
        json.dump(output,f,ensure_ascii=False,indent=2)

if __name__ == '__main__':
    main()
