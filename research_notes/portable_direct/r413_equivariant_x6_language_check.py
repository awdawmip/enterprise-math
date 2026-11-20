"""Exact finite checks for X6 r413 static candidate models (NOT P000 event legality)."""
from itertools import permutations, product

AXES = range(1, 7)
a = (1, 2, 3)
b = (4, 2, 3)
d = (-4, 2, 3)

def is_even(p):
    return sum(p[i] > p[j] for i in range(6) for j in range(i + 1, 6)) % 2 == 0

def act(g, letter):
    p, signs = g
    i = abs(letter) - 1
    return (1 if letter > 0 else -1) * signs[i] * p[i]

def event_action(g, event):
    return tuple(act(g, x) for x in event)

def group_elements():
    for p in permutations(AXES):
        if is_even(p):
            for signs in product((-1, 1), repeat=6):
                yield p, signs

def check():
    group = list(group_elements())
    assert len(group) == 23040
    E = {event_action(g, a) for g in group}
    assert len(E) == 960
    K = [g for g in group if event_action(g, a) == a]
    assert len(K) == 24
    fixed = {e for e in E if all(event_action(g, e) == e for g in K)}
    assert len(fixed) == 48
    assert all({abs(x) for x in e} == {1, 2, 3} for e in fixed)
    flip_four = ((1, 2, 3, 4, 5, 6), (1, 1, 1, -1, 1, 1))
    assert flip_four in K
    assert b in E and d in E and b not in fixed
    assert event_action(flip_four, b) == d
    assert event_action(flip_four, a) == a
    assert tuple(event_action(flip_four, x) for x in (b, a)) == (d, a)
    assert a in fixed
    print(f"|H|={len(group)} |E|={len(E)} |K_a|={len(K)} |E^K_a|={len(fixed)}")
    print("L_repeat/a=a*: injective for arbitrary prefix lengths by Theorem A")
    print("L_free/a=E*: collision (b,a) and (d,a) under sign flip of axis 4")

if __name__ == "__main__":
    check()
