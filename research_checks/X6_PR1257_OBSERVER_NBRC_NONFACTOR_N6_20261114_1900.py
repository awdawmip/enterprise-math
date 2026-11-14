"""Exact independent integer certificate for the historical PR #1257 observer's
positive native six-axis N-BRC information loss (not the old PR regression)."""
from collections import Counter, defaultdict
from itertools import combinations_with_replacement
from math import factorial, prod

# Pinned historical PR #1257 @ 472ebb9fd09b83035ecd66ebcb3ee491ff89fcfc
# experiments/x6_native_universal_completion_v2_20260905/x6_cell.py
G = ((1, 0, 0), (0, 1, 0), (-1, -1, 0),
     (-1, -1, 1), (0, 1, 1), (1, 0, 1))


def observer(z):
    return (sum(z[i] * G[i][0] for i in range(6)),
            sum(z[i] * G[i][1] for i in range(6)),
            sum(z[i] * G[i][2] for i in range(6)) % 2)


def mass(z):
    return factorial(sum(z)) // prod(factorial(k) for k in z)


def enumerate_shell(n):
    by_q, by_q_quad = defaultdict(list), defaultdict(list)
    for axes in combinations_with_replacement(range(6), n):
        c = Counter(axes)
        z = tuple(c.get(i, 0) for i in range(6))
        key = observer(z)
        by_q[key].append(mass(z))
        by_q_quad[(key, sum(k*k for k in z))].append(mass(z))
    return by_q, by_q_quad


shells = {}
for n in range(7):
    a, b = enumerate_shell(n)
    shells[n] = (a, b)
    assert sum(sum(v) for v in a.values()) == 6**n
    assert sum(len(v) for v in a.values()) == factorial(n+5)//(factorial(n)*factorial(5))

assert [len(shells[n][0]) for n in range(7)] == [1,6,12,20,30,42,56]
assert [sum(len(set(m)) > 1 for m in shells[n][0].values()) for n in range(4)] == [0,0,0,18]
assert [sum(len(set(m)) > 1 for m in shells[n][1].values()) for n in range(7)] == [0,0,0,0,0,0,6]

for t in range(12):
    A = (3, 1, t, 0, 1, 1)
    B = (2, 2, t, 0, 0, 2)
    assert observer(A) == observer(B) == (4-t, 2-t, 0)
    assert sum(A) == sum(B) == 6+t
    assert sum(j*j for j in A) == sum(j*j for j in B) == 12+t*t
    assert 3*mass(A) == 4*mass(B)

print('PASS_X6_PR1257_OBSERVER_NBRC_NONFACTOR')
print('positive_endpoint_counts_n0_6=',[factorial(n+5)//(factorial(n)*factorial(5)) for n in range(7)])
print('quotient_endpoint_counts_n0_6=',[len(shells[n][0]) for n in range(7)])
print('first_mixed_fibre_q_plus_L1=n3; mixed_fibres=18/20')
print('first_mixed_fibre_q_plus_L1_plus_Q=n6; mixed_fibres=6/166')
print('same_observer_length_quad_witness_n6:',(3,1,0,0,1,1),(2,2,0,0,0,2),'B=120 vs 90')
