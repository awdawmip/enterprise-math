"""Exact Fraction certificate: identical source-outcome marginals, different
structural deletion under state-local enabled-transition renormalization.
This is an external Petri model, not the native Enterprise BRC runtime.
"""
from fractions import Fraction as Q
from collections import defaultdict

A = {"p0": [("done", Q(1), "a", "y"), ("done", Q(1), "b", "y")]}
B = {"p0": [("left", Q(1), None, ""), ("right", Q(1), None, "")],
     "left": [("done", Q(1), "a", "y")],
     "right": [("done", Q(1), "b", "y")]}

def run(net, delete=frozenset()):
    output = defaultdict(lambda: Q(0))
    def step(state, mass, used, word):
        if state == "done":
            output[(used, word)] += mass
            return
        edges = [e for e in net.get(state, []) if e[2] not in delete]
        if not edges:
            output[(used, "ABORT")] += mass
            return
        denominator = sum((edge[1] for edge in edges), Q(0))
        for dst, weight, source, obs in edges:
            new_used = used | (frozenset((source,)) if source is not None else frozenset())
            step(dst, mass * weight / denominator, new_used, word + obs)
    step("p0", Q(1), frozenset(), "")
    return dict(output)

p_a, p_b = run(A), run(B)
assert p_a == p_b == {
    (frozenset(("a",)), "y"): Q(1, 2),
    (frozenset(("b",)), "y"): Q(1, 2),
}
q_a = run(A, frozenset(("a",)))
q_b = run(B, frozenset(("a",)))
assert q_a == {(frozenset(("b",)), "y"): Q(1)}
assert q_b == {
    (frozenset(), "ABORT"): Q(1, 2),
    (frozenset(("b",)), "y"): Q(1, 2),
}
assert sum(q_a.values()) == sum(q_b.values()) == Q(1)
print("PASS identical full source-outcome baseline, divergent structural knockout")
