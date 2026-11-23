"""R284FG: exact four-cycle finite-state observer test for persistent omissions."""
from collections import deque
from itertools import combinations


def errors(word, length, radius):
    for r in range(radius + 1):
        for positions in combinations(range(length), r):
            v = word
            for k in positions:
                v ^= 1 << k
            yield v


def transition(start, target, order, omissions):
    physical = start
    out = [start]
    for k in order:
        if k not in omissions:
            physical = (physical & ~(1 << k)) | (target & (1 << k))
        out.append(physical)
    return out


def evaluate(words, length, q_by_edge, read_errors, orders=None):
    assert len(words) == 4 and len(set(words)) == 4
    deltas = [words[i] ^ words[(i + 1) % 4] for i in range(4)]
    defaults = [tuple(k for k in range(length) if delta & (1 << k))
                for delta in deltas]
    orders = defaults if orders is None else orders
    assert all(set(a) == set(b) for a, b in zip(orders, defaults))
    stable = [set() for _ in range(4)]
    stable[0].add(words[0])
    queue = deque([(0, words[0])])
    while queue:
        phase, physical = queue.popleft()
        next_phase = (phase + 1) % 4
        order = orders[phase]
        for r in range(min(q_by_edge[phase], len(order)) + 1):
            for omissions in combinations(order, r):
                terminal = transition(physical, words[next_phase], order, omissions)[-1]
                if terminal not in stable[next_phase]:
                    stable[next_phase].add(terminal)
                    queue.append((next_phase, terminal))
    observed = [set(y for physical in stable[phase]
                    for y in errors(physical, length, read_errors))
                for phase in range(4)]
    collisions = [(i, j, len(observed[i] & observed[j]))
                  for i in range(4) for j in range(i + 1, 4)
                  if observed[i] & observed[j]]
    stats = {"stable_sizes": [len(s) for s in stable],
             "observed_sizes": [len(s) for s in observed],
             "collisions": collisions}
    if collisions:
        return False, "stable-observation-collision", stats
    lookup = {y: phase for phase in range(4) for y in observed[phase]}
    prefix_cache = {}
    for phase in range(4):
        next_phase = (phase + 1) % 4
        for physical in stable[phase]:
            order = orders[phase]
            for r in range(min(q_by_edge[phase], len(order)) + 1):
                for omissions in combinations(order, r):
                    trace = transition(physical, words[next_phase], order, omissions)
                    seen_new = False
                    for t, prefix in enumerate(trace):
                        if prefix not in prefix_cache:
                            prefix_cache[prefix] = {
                                lookup[y] for y in errors(prefix, length, read_errors)
                                if y in lookup}
                        labels = prefix_cache[prefix]
                        if labels - {phase, next_phase}:
                            return False, "third-phase-read", dict(
                                stats, witness=(phase, physical, omissions, t,
                                                prefix, sorted(labels)))
                        if seen_new and phase in labels:
                            return False, "new-to-old-rollback", dict(
                                stats, witness=(phase, physical, omissions, t,
                                                prefix, sorted(labels)))
                        if next_phase in labels:
                            seen_new = True
    return True, "valid", dict(stats, physical_prefix_count=len(prefix_cache))


def main():
    ok, reason, cert = evaluate((0, 7, 63, 56), 6, (1, 1, 1, 1), 0)
    assert ok and cert["stable_sizes"] == [16] * 4, (reason, cert)
    print("six-bit Gray q=1,u=0:", reason, cert)

    orders = ((5, 4, 1, 3, 0, 2), (5, 4, 3, 6, 2),
              (5, 4, 1, 3, 0, 2), (5, 4, 3, 6, 2))
    ok, reason, cert = evaluate((0, 63, 67, 124), 7, (0, 0, 0, 0), 1, orders)
    assert ok, (reason, cert)
    print("seven-bit nonseparable q=0,u=1:", reason, cert)

    words = (0, 1751, 5436, 7003)
    ok, reason, cert = evaluate(words, 13, (1, 1, 1, 1), 1)
    assert not ok and reason in {"third-phase-read", "new-to-old-rollback"}, (reason, cert)
    assert cert["collisions"] == []
    assert cert["stable_sizes"] == [80, 90, 80, 90]
    assert cert["observed_sizes"] == [428, 478, 428, 478]
    print("13-bit stable-only false positive:", reason, cert)

    # Explicit admissible carryover history to stable physical 144 in phase 0.
    history = [(0, 1751, (), 1751), (1, 5436, (7,), 5564),
               (2, 7003, (), 7131), (3, 0, (4,), 144)]
    physical = 0
    for phase, target, omissions, expected in history:
        order = tuple(k for k in range(13)
                      if (words[phase] ^ words[(phase + 1) % 4]) & (1 << k))
        physical = transition(physical, target, order, omissions)[-1]
        assert physical == expected
    order = tuple(k for k in range(13) if words[1] & (1 << k))
    prefix = transition(144, words[1], order, ())[4]
    assert prefix == 151
    assert (215 ^ 727).bit_count() <= 1
    assert (135 ^ 133).bit_count() <= 1
    assert (215 ^ prefix).bit_count() <= 1
    assert (135 ^ prefix).bit_count() <= 1
    print("physical 151: observed 215 -> phase1, then 135 -> phase0")


if __name__ == "__main__":
    main()
