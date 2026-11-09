"""Exact finite-horizon language/holonomy quotient of R672's auxiliary scheduler.

Python standard library; exact integer/tuple arithmetic. V17 block-language
model only, not a native V29 network update.
"""
from collections import deque, Counter
from itertools import product
import json

ALPHABET = "ABC"
IDENTITY = (0, 1, 2)
GEN = {"A": (0, 2, 1), "B": (2, 1, 0), "C": (1, 0, 2)}

def compose(p, q):
    return tuple(p[q[i]] for i in range(3))

def next_state(state, letter):
    h, suffix = state
    if letter in suffix:
        return None
    return compose(h, GEN[letter]), (suffix + letter)[-2:]

start = (IDENTITY, "")
seen, queue = {start}, deque([start])
witness = {start: ""}
while queue:
    state = queue.popleft()
    for x in ALPHABET:
        nxt = next_state(state, x)
        if nxt is not None and nxt not in seen:
            seen.add(nxt)
            witness[nxt] = witness[state] + x
            queue.append(nxt)

assert len(seen) == 40
assert len({h for h, _ in seen}) == 6
assert Counter(len(q) for _, q in seen) == {2: 36, 1: 3, 0: 1}

def words_up_to(H):
    return [
        "".join(w)
        for k in range(1, H + 1)
        for w in product(ALPHABET, repeat=k)
    ]

def signature(state, H):
    legal = []
    for word in words_up_to(H):
        candidate = state
        for x in word:
            candidate = next_state(candidate, x)
            if candidate is None:
                break
        if candidate is not None:
            legal.append(word)
    return state[0], tuple(legal)

sizes = {str(H): len({signature(state, H) for state in seen}) for H in range(4)}
assert sizes == {"0": 6, "1": 22, "2": 40, "3": 40}, sizes
assert len({signature(s, 2) for s in seen}) == len(seen)

def follow(word):
    state = start
    for x in word:
        state = next_state(state, x)
        if state is None:
            return None
    return state

s1, s2 = follow("AB"), follow("ACBA")
assert s1[0] == s2[0] == (1, 2, 0)
assert (s1[1], s2[1]) == ("AB", "BA")
assert signature(s1, 1) == signature(s2, 1)
assert signature(s1, 2) != signature(s2, 2)
assert follow("ABCA") is not None and follow("ACBACA") is None

analytic = {"0": 6, "1": 1 + 3 + 3*6, "2": 1 + 3 + 6*6}
assert all(sizes[k] == v for k, v in analytic.items())

summary = {
    "schema": "R673_HORIZON_QUOTIENT_V1",
    "source": "R672 exact V17 three transposition blocks, auxiliary no-last-two-repeat scheduler",
    "group": "S3",
    "alphabet": ALPHABET,
    "right_action_convention": "compose(p,q)[i] = p[q[i]]",
    "generators": {k: list(v) for k, v in GEN.items()},
    "reachable_raw_states": len(seen),
    "counts_by_suffix_length": {"0": 1, "1": 3, "2": 36},
    "quotient_by_prediction_horizon": sizes,
    "stabilizes_at_horizon": 2,
    "example_equal_T1": {
        "history_1": "AB",
        "history_2": "ACBA",
        "shared_group": list(s1[0]),
        "shared_next_letter": "C",
        "distinguishing_future": "CA",
    },
    "independent_combinatorial_counts": analytic,
    "max_shortest_reachable_witness_length": max(map(len, witness.values())),
    "arithmetic": "exact finite tuple permutations and integers; exhaustive BFS of 40 reachable states",
    "pass": True,
}
print(json.dumps(summary, ensure_ascii=False, indent=2, sort_keys=True))
