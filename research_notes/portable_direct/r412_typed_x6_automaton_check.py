#!/usr/bin/env python3
"""Finite exact checks of r412; candidate algebra only, not native P000-event admission."""
from collections import deque
from itertools import permutations, product


def even(p):
    return sum(p[i] > p[j] for i in range(6) for j in range(i + 1, 6)) % 2 == 0


def transform(g, triple):
    perm, signs = g
    return tuple((1 if x > 0 else -1) * signs[abs(x) - 1]
                 * perm[abs(x) - 1] for x in triple)


def stabilizer(suffix):
    """H=(C2)^6 semidirect A6, acting on the signed-axis record code."""
    return [(p, eps)
            for p in permutations(range(1, 7)) if even(p)
            for eps in product((-1, 1), repeat=6)
            if all(transform((p, eps), word) == word for word in suffix)]


def find_collision(events, transition, start, accept, suffix):
    """BFS over pair-DFA states; returns concrete counterexample or None.

    transition[(state, event)] = next_state; missing transitions reject.
    Event codes are distinct tuples of exactly three signed axes.
    """
    events = tuple(events)
    assert len(set(events)) == len(events)
    assert all(len(a) == 3 for a in events)
    assert all(a in events for a in suffix)

    def after_suffix(state):
        for a in suffix:
            state = transition.get((state, a))
            if state is None:
                return None
        return state

    for group_element in stabilizer(suffix):
        legal_pairs = [(a, transform(group_element, a)) for a in events
                       if transform(group_element, a) in events]
        initial = (start, start, False)
        queue = deque([(initial, (), ())])
        visited = {initial}

        while queue:
            (q, r, distinct), u, v = queue.popleft()
            if distinct and after_suffix(q) in accept and after_suffix(r) in accept:
                assert u != v
                assert all(transform(group_element, a) == b for a, b in zip(u, v))
                return group_element, u, v

            for a, b in legal_pairs:
                q2 = transition.get((q, a))
                r2 = transition.get((r, b))
                if q2 is None or r2 is None:
                    continue
                key = (q2, r2, distinct or a != b)
                if key in visited:
                    continue
                visited.add(key)
                queue.append((key, u + (a,), v + (b,)))
    return None


def main():
    a, b, d = (1, 2, 3), (4, 2, 3), (-4, 2, 3)
    E = (a, b, d)
    suffix = (a,)
    assert len(stabilizer(suffix)) == 24

    tests = {
        "singleton": ((a,), {(0, a): 0}, {0}, False),
        "free-three-events": (E, {(0, x): 0 for x in E}, {0}, True),
        "a-star-legality": (E, {(0, a): 0}, {0}, False),
        "ba-or-da-legality": (E, {(0, b): 1, (0, d): 1, (1, a): 2}, {2}, True),
    }
    for title, (events, transitions, accepting, expected_collision) in tests.items():
        collision = find_collision(events, transitions, 0, accepting, suffix)
        assert (collision is not None) == expected_collision, title
        if collision:
            g, u, v = collision
            assert u == (b,) and v == (d,) or u == (d,) and v == (b,)
        print(f"{title}: {'COLLISION' if collision else 'INJECTIVE'}")

    print("r412 finite checks PASS: |H|=23040; |Stab_H(a)|=24")


if __name__ == "__main__":
    main()
