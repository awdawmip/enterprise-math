"""Exact Boolean sumset tools reconstructed from the PREFIX180 producer method.

Author research companion, not an admitted replacement of canonical BRC.
Coverage concerns endpoints only, not weights, multiplicity or path provenance.
"""
from dataclasses import dataclass
from itertools import combinations_with_replacement


def simplex(total, dimension=4):
    """All nonnegative integer tuples of the given sum, lexicographic order."""
    if total < 0 or dimension < 1:
        raise ValueError("need nonnegative total and positive dimension")
    if dimension == 1:
        return [(total,)]
    return [(a,) + tail for a in range(total + 1)
            for tail in simplex(total - a, dimension - 1)]


def support(point):
    return sum(x != 0 for x in point)


def add(left, right):
    if len(left) != len(right):
        raise ValueError("sum dimensions differ")
    return tuple(x + y for x, y in zip(left, right))


def sumset(points):
    return {add(x, y) for x, y in combinations_with_replacement(points, 2)}


def layers(n, removed=(4, 4, 0, 0)):
    """The four-label restricted family; removed must be two-supported."""
    population = simplex(n)
    if removed not in population or support(removed) != 2:
        raise ValueError("removed must be a degree-n point of support exactly two")
    return (tuple(p for p in population if support(p) <= 2 and p != removed),
            tuple(p for p in population if support(p) == 3),
            tuple(p for p in population if support(p) == 4))


def hard_targets(n, removed):
    """Uncovered non-full-support targets. Full sufficiency needs n >= 7."""
    base, _, _ = layers(n, removed)
    covered = sumset(base)
    return tuple(p for p in simplex(2 * n) if support(p) <= 3 and p not in covered)


def hard_targets_closed_form(n, removed):
    """Exactly 2(n-2)+[a=1]+[b=1] hard targets for a removed (a,b) pair.

    Valid for n>=2. The separate any-completion theorem still requires n>=7.
    Construction uses O(n) targets without enumerating the degree-2n simplex.
    """
    if n < 2 or len(removed) != 4 or any(x < 0 for x in removed) or sum(removed) != n or support(removed) != 2:
        raise ValueError("need a four-coordinate degree-n support-two deletion")
    i, j = [k for k, x in enumerate(removed) if x]
    a, b = removed[i], removed[j]
    targets = set()
    for k in set(range(4)) - {i, j}:
        for t in range(1, b):
            y = [0]*4
            y[i], y[j], y[k] = a, n+b-t, t
            targets.add(tuple(y))
        for t in range(1, a):
            y = [0]*4
            y[i], y[j], y[k] = n+a-t, b, t
            targets.add(tuple(y))
    if a == 1:
        y = [0]*4
        y[i], y[j] = 1, 2*n-1
        targets.add(tuple(y))
    if b == 1:
        y = [0]*4
        y[i], y[j] = 2*n-1, 1
        targets.add(tuple(y))
    return tuple(sorted(targets))


def support_obstructions(n, removed, q):
    """For n>=7, empty output is equivalent to some full-support completion."""
    if n < 7:
        raise ValueError("the general single-deletion theorem requires n >= 7")
    base, x3, _ = layers(n, removed)
    if not set(q).issubset(x3):
        raise ValueError("q must use degree-n support-three points")
    covered = sumset(base + tuple(q))
    return tuple(p for p in hard_targets_closed_form(n, removed) if p not in covered)


def producer_clauses(targets, base, candidates):
    """One OR-of-ANDs clause per target outside base+base; bits select points.

    An empty clause proves impossibility. Inclusion-dominated producers are
    removed: if A is contained in B, selecting B already selects A.
    """
    if len(set(candidates)) != len(candidates):
        raise ValueError("candidate points must be distinct")
    residual = sorted(set(targets) - sumset(base))
    by_target = {p: set() for p in residual}
    for i, x in enumerate(candidates):
        for y in base:
            value = add(x, y)
            if value in by_target:
                by_target[value].add(1 << i)
        for j in range(i, len(candidates)):
            value = add(x, candidates[j])
            if value in by_target:
                by_target[value].add((1 << i) | (1 << j))
    clauses = []
    for target in residual:
        minimal = []
        for mask in sorted(by_target[target], key=lambda m: (m.bit_count(), m)):
            if not any(old & mask == old for old in minimal):
                minimal.append(mask)
        clauses.append(tuple(minimal))
    return tuple(residual), tuple(clauses)


@dataclass(frozen=True)
class SearchResult:
    status: str
    selected: tuple[int, ...]
    nodes: int


def solve_budget(clauses, budget, node_limit=None):
    """Complete producer branching with a sound disjoint-union lower bound.

    The cache contains only exhaustively refuted masks. Exceeding an explicit
    node limit yields UNKNOWN, never NO. The empty conjunction is true.
    """
    if budget < 0:
        return SearchResult("NO", (), 0)
    if node_limit is not None and node_limit < 0:
        raise ValueError("node_limit must be nonnegative")
    if any(mask <= 0 for clause in clauses for mask in clause):
        raise ValueError("producer masks must be positive")
    nodes, refuted = 0, set()

    class LimitReached(Exception):
        pass

    def visit(chosen):
        nonlocal nodes
        nodes += 1
        if node_limit is not None and nodes > node_limit:
            raise LimitReached
        left = budget - chosen.bit_count()
        if left < 0 or chosen in refuted:
            return None
        pending, unions = [], []
        for clause in clauses:
            if any(mask & chosen == mask for mask in clause):
                continue
            choices = {mask & ~chosen for mask in clause
                       if (mask & ~chosen).bit_count() <= left}
            if not choices:
                refuted.add(chosen)
                return None
            pending.append(choices)
            union = 0
            for mask in choices:
                union |= mask
            unions.append(union)
        if not pending:
            return chosen
        used, lower = 0, 0
        for union in sorted(unions, key=lambda m: (m.bit_count(), m)):
            if not union & used:
                lower += 1
                used |= union
        if lower > left:
            refuted.add(chosen)
            return None
        choices = min(pending, key=lambda values: (len(values), sorted(values)))
        for mask in sorted(choices, key=lambda m: (m.bit_count(), m)):
            answer = visit(chosen | mask)
            if answer is not None:
                return answer
        refuted.add(chosen)
        return None

    try:
        answer = visit(0)
    except LimitReached:
        return SearchResult("UNKNOWN", (), nodes)
    if answer is None:
        return SearchResult("NO", (), nodes)
    return SearchResult("YES", tuple(i for i in range(answer.bit_length())
                                     if answer & (1 << i)), nodes)
