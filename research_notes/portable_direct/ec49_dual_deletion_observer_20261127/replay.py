"""Replay a mask-free observer for two named deletions against slot matching."""
from collections import Counter
from dataclasses import dataclass
from functools import lru_cache
from itertools import combinations, combinations_with_replacement, product
import json
from random import Random


def classes(keys):
    identifiers = {}
    return tuple(
        0 if key is None else identifiers.setdefault(key, 1 + len(identifiers))
        for key in keys
    )


def small_rank(row, indices, budget):
    if budget == 1:
        return sum(bool(row[i]) for i in indices)
    return len({row[i] for i in indices if row[i]})


@dataclass(frozen=True)
class Observer:
    labels: tuple
    costs: tuple
    profiles: tuple
    budget: int

    def insert(self, label, mask):
        assert label not in self.labels
        costs = []
        profiles = []
        for subset, old_cost in enumerate(self.costs):
            extended = subset | mask
            costs.append(min(old_cost, self.costs[extended] - 1))
            if not self.budget:
                continue
            old = self.profiles[subset]
            if self.costs[extended] > old_cost:
                profiles.append(old + (0,))
                continue
            later = self.profiles[extended]
            if self.budget == 1:
                profiles.append(tuple(bool(x) for x in later) + (1,))
                continue
            keys = [
                (left, right) if left else (0, 0) if right else None
                for left, right in zip(old, later)
            ]
            profiles.append(classes(keys + [(0, 0)]))
        return Observer(self.labels + (label,), tuple(costs), tuple(profiles), self.budget)

    def delete(self, label):
        assert self.budget
        index = self.labels.index(label)
        costs = tuple(cost + bool(row[index]) for cost, row in zip(self.costs, self.profiles))
        profiles = ()
        if self.budget == 2:
            profiles = tuple(
                tuple(bool(group) and (not row[index] or group != row[index])
                      for i, group in enumerate(row) if i != index)
                for row in self.profiles
            )
        labels = self.labels[:index] + self.labels[index+1:]
        return Observer(labels, costs, profiles, self.budget-1)


@lru_cache(maxsize=100_000)
def matching_rank(capacities, masks):
    slots = tuple(port for port, count in enumerate(capacities) for _ in range(count))
    occupants = [-1] * len(slots)

    def augment(target, seen):
        for slot, port in enumerate(slots):
            if slot in seen or not masks[target] & (1 << port):
                continue
            seen.add(slot)
            occupant = occupants[slot]
            if occupant < 0 or augment(occupant, seen):
                occupants[slot] = target
                return True
        return False

    return sum(augment(i, set()) for i in range(len(masks)))


@lru_cache(maxsize=100_000)
def reference_costs(capacities, masks):
    costs = []
    for subset in range(1 << len(capacities)):
        outside = tuple(0 if (subset >> i) & 1 else value
                        for i, value in enumerate(capacities))
        inside = sum(capacities) - sum(outside)
        costs.append(inside + matching_rank(outside, masks) - len(masks))
    return tuple(costs)


def without(masks, removed):
    return tuple(mask for i, mask in enumerate(masks) if i not in removed)


def capacity_assignment(capacities, masks):
    assigned = [[] for _ in capacities]

    def augment(target, seen):
        for port, capacity in enumerate(capacities):
            if not capacity or port in seen or not masks[target] & (1 << port):
                continue
            seen.add(port)
            if len(assigned[port]) < capacity:
                assigned[port].append(target)
                return True
            for index, old_target in enumerate(assigned[port]):
                if augment(old_target, seen):
                    assigned[port][index] = target
                    return True
        return False

    for target in range(len(masks)):
        augment(target, set())
    return tuple(tuple(row) for row in assigned)


def bits(mask):
    while mask:
        first = mask & -mask
        yield first.bit_length() - 1
        mask ^= first


def dual_parallel_classes(capacities, masks, assignment):
    label_count = len(masks)
    port_base = label_count + 1
    graph = [[] for _ in range(port_base + len(capacities))]
    matched = {target for row in assignment for target in row}
    graph[0] = [x+1 for x in range(label_count) if x not in matched]
    for x, mask in enumerate(masks, 1):
        graph[x] = [port_base+i for i in bits(mask) if capacities[i]]
    for i, targets in enumerate(assignment):
        graph[port_base+i] = [x+1 for x in targets]

    reachable, queue = {0}, [0]
    for x in queue:
        for y in graph[x]:
            if y not in reachable:
                reachable.add(y)
                queue.append(y)
    predecessors = [[] for _ in graph]
    for x in queue:
        for y in graph[x]:
            predecessors[y].append(x)

    live = sum(1 << x for x in reachable)
    dom = [live if x in reachable else 0 for x in range(len(graph))]
    dom[0] = 1
    changed = True
    while changed:
        changed = False
        for x in queue[1:]:
            intersection = live
            for previous in predecessors[x]:
                intersection &= dom[previous]
            revised = intersection | (1 << x)
            if revised != dom[x]:
                dom[x] = revised
                changed = True

    label_bits = (1 << port_base) - 2
    return classes(
        min(bits(dom[x] & label_bits), key=lambda y: dom[y].bit_count())
        if x in reachable else None
        for x in range(1, port_base)
    )


def initial_observer(capacities, targets):
    masks = tuple(targets.values())
    costs, rows = [], []
    for subset in range(1 << len(capacities)):
        outside = tuple(0 if (subset >> i) & 1 else value
                        for i, value in enumerate(capacities))
        assignment = capacity_assignment(outside, masks)
        costs.append(sum(capacities)-sum(outside)+sum(map(len, assignment))-len(masks))
        rows.append(dual_parallel_classes(outside, masks, assignment))
    return Observer(tuple(targets), tuple(costs), tuple(rows), 2)

def verify(observer, capacities, targets, counts):
    assert observer.labels == tuple(targets)
    masks = tuple(targets.values())
    base = reference_costs(capacities, masks)
    assert observer.costs == base, (capacities, targets, observer)
    counts['states'] += 1
    counts['port_queries'] += len(base)
    for size in range(1, observer.budget+1):
        for removed in combinations(range(len(masks)), size):
            expected = reference_costs(capacities, without(masks, removed))
            for s, old in enumerate(base):
                assert small_rank(observer.profiles[s], removed, observer.budget) == expected[s]-old, (
                    capacities, targets, observer, removed, s)
            counts['dual_rank_queries'] += len(base)


def insert_and_verify(observer, capacities, targets, label, mask, counts):
    new_targets = dict(targets)
    new_targets[label] = mask
    advanced = observer.insert(label, mask)
    verify(advanced, capacities, new_targets, counts)
    counts['insertions'] += 1
    return advanced, new_targets


def delete_and_verify(observer, capacities, targets, label, counts):
    new_targets = dict(targets)
    del new_targets[label]
    advanced = observer.delete(label)
    verify(advanced, capacities, new_targets, counts)
    counts['deletions'] += 1
    return advanced, new_targets


def exhaustive():
    counts = Counter()
    for capacity in product(range(3), repeat=2):
        for count in range(5):
            for masks in combinations_with_replacement(range(4), count):
                initial = dict(enumerate(masks))
                observer = initial_observer(capacity, initial)
                verify(observer, capacity, initial, counts)
                counts['instances'] += 1
                counts['initial_matching_and_dominator_graphs'] += len(observer.costs)
                for insertion in range(4):
                    added, present = insert_and_verify(observer, capacity, initial, count, insertion, counts)
                    for first in present:
                        once, after = delete_and_verify(added, capacity, present, first, counts)
                        for second in after:
                            twice, rest = delete_and_verify(once, capacity, after, second, counts)
                            insert_and_verify(twice, capacity, rest, count+1, insertion, counts)
    return dict(counts)


def random_cases():
    counts = Counter()
    rng = Random(492611271743)
    for _ in range(320):
        width = rng.randint(1, 6)
        capacity = tuple(rng.randint(0, 3) for _ in range(width))
        present = {i: rng.randrange(1 << width) for i in range(rng.randrange(9))}
        observer = initial_observer(capacity, present)
        verify(observer, capacity, present, counts)
        counts['instances'] += 1
        counts['initial_matching_and_dominator_graphs'] += len(observer.costs)
        for label in range(100, 107):
            if present and observer.budget and rng.randrange(3) == 0:
                removed = rng.choice(tuple(present))
                observer, present = delete_and_verify(observer, capacity, present, removed, counts)
            else:
                mask = rng.randrange(1 << width)
                observer, present = insert_and_verify(observer, capacity, present, label, mask, counts)
    return dict(counts)


def necessary_hierarchy():
    for budget in range(1, 9):
        a = (1,) * (budget + 1) + (2,) * budget
        b = (3,) + a[1:]
        for size in range(budget):
            for labels in combinations(range(len(a)), size):
                assert reference_costs((1, 1), without(a, labels)) == reference_costs((1, 1), without(b, labels))
        witness = set(range(budget+1, len(a)))
        assert matching_rank((1, 1), without(a, witness)) == 1
        assert matching_rank((1, 1), without(b, witness)) == 2
    return 8


if __name__ == '__main__':
    print(json.dumps({
        'exhaustive': exhaustive(),
        'random': random_cases(),
        'hierarchy_budgets': necessary_hierarchy(),
    }, sort_keys=True))
