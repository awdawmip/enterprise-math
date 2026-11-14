#!/usr/bin/env python3
"""R762AK: integer exhaustive classification of paired C3/S3 and S3/S3 actions.

No network access, dependencies or randomized sampling. Uses permutation tuples.
"""
import itertools
import json
from collections import Counter, deque
from pathlib import Path

E = (0, 1, 2)
S3 = tuple(itertools.permutations(E))

def parity(p):
    return sum(p[i] > p[j] for i in range(3) for j in range(i + 1, 3)) % 2

C3 = tuple(p for p in S3 if parity(p) == 0)

def multiply(p, q):
    return tuple(p[q[i]] for i in range(3))

def inverse(p):
    return tuple(p.index(i) for i in range(3))

def pair_multiply(x, y):
    return multiply(x[0], y[0]), multiply(x[1], y[1])

def closure(generators):
    identity = (E, E)
    found = {identity}
    queue = deque([identity])
    while queue:
        x = queue.popleft()
        for g in generators:
            y = pair_multiply(g, x)
            if y not in found:
                found.add(y)
                queue.append(y)
    return frozenset(found)

def all_subgroups(left, right):
    domain = tuple(itertools.product(left, right))
    identity_group = frozenset([(E, E)])
    seen = {identity_group}
    queue = deque([identity_group])
    while queue:
        group = queue.popleft()
        for element in domain:
            if element not in group:
                nxt = closure(tuple(group) + (element,))
                if nxt not in seen:
                    seen.add(nxt)
                    queue.append(nxt)
    return seen

def subdirects(left, right):
    all_groups = all_subgroups(left, right)
    subs = [g for g in all_groups
            if {x[0] for x in g} == set(left)
            and {x[1] for x in g} == set(right)]
    return all_groups, subs

def ctype(x):
    return "E" if x == E else ("C" if x in C3 else "T")

def verify_distinguishing(group):
    for x, y in itertools.combinations(group, 2):
        witness = inverse(x[0]), inverse(x[1])
        assert witness in group
        first = pair_multiply(witness, x)
        second = pair_multiply(witness, y)
        assert (ctype(first[0]), ctype(first[1])) == ("E", "E")
        assert (ctype(second[0]), ctype(second[1])) != ("E", "E")
    return len(group) * (len(group) - 1) // 2

def short_generators(group):
    nonidentity = sorted(x for x in group if x != (E, E))
    for count in range(1, 4):
        for gens in itertools.combinations(nonidentity, count):
            if closure(gens) == group:
                return gens
    raise AssertionError("No <=3-generator example")

all18, sub18 = subdirects(C3, S3)
all36, sub36 = subdirects(S3, S3)
assert len(all18) == 14 and len(sub18) == 1
assert sub18[0] == frozenset(itertools.product(C3, S3))
assert len(all36) == 60
assert Counter(map(len, sub36)) == Counter({6: 6, 18: 1, 36: 1})
assert all(verify_distinguishing(g) == len(g) * (len(g) - 1) // 2
           for g in sub18 + sub36)

parity_locked = frozenset((a,b) for a in S3 for b in S3
                          if parity(a) == parity(b))
assert parity_locked in sub36
for subgroup in sub36:
    if len(subgroup) == 18:
        assert subgroup == parity_locked
    if len(subgroup) == 6:
        assert all((a == E) == (b == E) for a,b in subgroup)

gens = short_generators(parity_locked)
assert len(gens) == 3
weights = (2, 3, 5)
W = {(E, E): 1}
mass_checks = []
for k in range(8):
    # independent ordered-word enumeration
    direct = {}
    for word in itertools.product(range(3), repeat=k):
        state, mass = (E, E), 1
        for index in word:
            state = pair_multiply(gens[index], state)
            mass *= weights[index]
        direct[state] = direct.get(state, 0) + mass
    assert W == direct
    assert sum(W.values()) == sum(weights) ** k
    mass_checks.append({"k": k, "support": len(W),
                        "total_mass": str(sum(W.values()))})
    nxt = {}
    for state, mass in W.items():
        for move, weight in zip(gens, weights):
            dest = pair_multiply(move, state)
            nxt[dest] = nxt.get(dest, 0) + mass * weight
    W = nxt

cycle = next(p for p in C3 if p != E)
left = {(E,E): 1, (cycle,cycle): 1}
right = {(E,cycle): 1, (cycle,E): 1}
def marginal(distribution, index):
    result = Counter()
    for state, mass in distribution.items():
        result[state[index]] += mass
    return result

assert left != right and all(marginal(left, k) == marginal(right, k)
                             for k in (0,1))


# AK4: exact finite partial-action witness, with full marginals but 8 states.
t = next(p for p in S3 if parity(p) == 1)
def partial_step(state, label):
    if state is None:
        return None
    s, h = state
    if label == "S" and h == E:
        return multiply(cycle, s), h
    if label == "C" and s == E:
        return s, multiply(cycle, h)
    if label == "T" and s == E:
        return s, multiply(t, h)
    return None

reachable = {(E, E)}
frontier = deque([(E, E)])
while frontier:
    state = frontier.popleft()
    for label in "SCT":
        nxt = partial_step(state, label)
        if nxt is not None and nxt not in reachable:
            reachable.add(nxt)
            frontier.append(nxt)
expected_reachable = {(E, h) for h in S3} | {(s, E) for s in C3}
assert reachable == expected_reachable and len(reachable) == 8
assert {s for s,h in reachable} == set(C3)
assert {h for s,h in reachable} == set(S3)

states = list(sorted(reachable)) + [None]  # None = absorbing undefined.
classes = {state: ("UNDEFINED",) if state is None
           else (ctype(state[0]), ctype(state[1])) for state in states}
refinements = 0
while True:
    signature = {state: (classes[state],) + tuple(
        classes[partial_step(state, label)] for label in "SCT")
        for state in states}
    names = {sg:i for i,sg in enumerate(sorted(set(signature.values()), key=repr))}
    updated = {state: names[signature[state]] for state in states}
    unchanged_equivalence = all(
        (classes[x] == classes[y]) == (updated[x] == updated[y])
        for x in states for y in states)
    if unchanged_equivalence:
        break
    classes = updated
    refinements += 1
assert refinements == 2 and len(set(classes.values())) == 9
partial_action_result = {
    "reachable_states": len(reachable),
    "source_marginal_order": len({s for s,h in reachable}),
    "frame_marginal_order": len({h for s,h in reachable}),
    "joint_observer_classes_including_undefined": len(set(classes.values())),
    "strict_refinement_rounds": refinements,
    "fixed_binary_bits_on_nonfailure_states": 3
}

result = {
  "schema": "R762AK_EXACT_EVIDENCE_V1",
  "domain": "finite total reversible paired left group actions; joint cycle-type observer",
  "method": "complete subgroup enumeration via adjoining generators and closure",
  "C3xS3": {"all_subgroups": len(all18), "subdirect_count": len(sub18),
            "subdirect_orders": {"18": 1}, "distinguished_pairs": 153},
  "S3xS3": {"all_subgroups": len(all36), "subdirect_count": len(sub36),
            "subdirect_orders": {"6": 6, "18": 1, "36": 1},
            "distinguished_pairs": 873},
  "weighted_integer_group_ring": {"generators": len(gens),
       "weights": list(weights), "checks": mass_checks},
  "equal_marginals_distinct_joint_counterexample": True,
  "checks_passed": True,
  "partial_action_witness": partial_action_result,
  "scientific_scope": "conditional subgroup model; native TRIADIC_CLOSURE_E unresolved"
}
Path(__file__).with_name("R762AK_COUPLED_SOURCE_FRAME_EVIDENCE.json").write_text(
    json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True)+"\n",
    encoding="utf-8"
)
print(json.dumps(result, indent=2, sort_keys=True))
