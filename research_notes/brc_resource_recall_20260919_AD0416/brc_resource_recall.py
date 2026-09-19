"""BRC research adapter for resource-guarded, step-rounded max-score recall.

Not production Nollm code. No beam approximation or positive-mass interpretation.
The callback supplies the actual, resource-sensitive transitions. All quotients
are within one (cell, depth). Scores mode preserves reachable maximum scores;
paths mode additionally preserves the lexicographically selected kernel word.
"""
from __future__ import annotations
from dataclasses import dataclass
from typing import Callable, Hashable, Iterable, Literal

Q16 = 1 << 16
Mode = Literal['scores', 'paths']


def _nat(value: int, name: str) -> int:
    if type(value) is not int or value < 0:
        raise ValueError(f'{name} must be a nonnegative integer')
    return value


@dataclass(frozen=True)
class RoundedWord:
    """A composable exact score action, not a flattened Q16 scalar product."""
    weights: tuple[int, ...] = ()
    quantum: int = Q16

    def __post_init__(self) -> None:
        if type(self.quantum) is not int or self.quantum < 1:
            raise ValueError('positive integer quantum required')
        if type(self.weights) is not tuple or any(type(w) is not int or not 0 < w <= self.quantum for w in self.weights):
            raise ValueError('weights must be a tuple of bounded positive integers')

    def apply(self, score: int | None) -> int | None:
        # None is unreachable; integer zero is a reached, rounded-to-zero score.
        if score is None:
            return None
        _nat(score, 'score')
        if score > self.quantum:
            raise ValueError('score exceeds quantum')
        for weight in self.weights:
            score = score * weight // self.quantum
        return score

    def then(self, later: 'RoundedWord') -> 'RoundedWord':
        if self.quantum != later.quantum:
            raise ValueError('quantum mismatch')
        return RoundedWord(self.weights + later.weights, self.quantum)

    def table(self) -> tuple[int, ...]:
        """Exact finite semantic signature; O(quantum * word length), not free."""
        return tuple(self.apply(s) for s in range(self.quantum + 1))


@dataclass(frozen=True)
class Label:
    cell: Hashable
    score: int
    bridges: int
    depth: int
    path: tuple[str, ...]

    def __post_init__(self) -> None:
        hash(self.cell)
        for name in ('score', 'bridges', 'depth'):
            _nat(getattr(self, name), name)
        if self.score > Q16 or self.bridges > self.depth:
            raise ValueError('score or bridge consumption outside this recall model')
        if type(self.path) is not tuple or len(self.path) != self.depth or any(type(k) is not str or not k for k in self.path):
            raise ValueError('one nonempty kernel label per step is required')
        if self.bridges != self.path.count('bridge'):
            raise ValueError('Bridge consumption must match the kernel word')


def dominates(left: Label, right: Label, *, mode: Mode) -> bool:
    if mode not in ('scores', 'paths'):
        raise ValueError('unknown observer mode')
    if (left.cell, left.depth) != (right.cell, right.depth):
        return False
    return (left.bridges <= right.bridges and left.score >= right.score
            and (mode == 'scores' or left.path <= right.path))


def coalesce(labels: Iterable[Label], *, mode: Mode = 'paths') -> tuple[Label, ...]:
    """Resource-conditioned maximal antichain; never coalesce by Cell alone.

    Lexicographic comparison is suffix-safe here because depths are equal.
    This intentionally forgets multiplicity under the max-score observer.
    """
    if mode not in ('scores', 'paths'):
        raise ValueError('unknown observer mode')
    groups: dict[tuple[Hashable, int], list[Label]] = {}
    for candidate in labels:
        if type(candidate) is not Label:
            raise TypeError('Label values required')
        group = groups.setdefault((candidate.cell, candidate.depth), [])
        if any(dominates(old, candidate, mode=mode) for old in group):
            continue
        group[:] = [old for old in group if not dominates(candidate, old, mode=mode)]
        group.append(candidate)
    return tuple(label for group in groups.values() for label in group)


Transition = tuple[Hashable, int, int, str]  # target, Q16 weight, total bridge use, kernel
Targets = Callable[[Hashable, int], Iterable[Transition]]


@dataclass(frozen=True)
class SearchResult:
    best: dict[Hashable, tuple[int, tuple[str, ...]]]
    frontier_widths: tuple[int, ...]
    generated_labels: int


def bounded_recall(entry: Hashable, targets: Targets, *, max_steps: int,
                   max_bridges: int, mode: Mode = 'paths',
                   frontier_cap: int = 100000) -> SearchResult:
    """Exact bounded reference search, conditional on a monotone resource guard.

    Caller contract: edges/weights depend on Cell and allowed resource usage,
    not score or hidden history. Lower bridge use permits every edge allowed
    from higher bridge use; next use adds the same edge cost (0 or 1).
    frontier_cap raises rather than silently becoming an approximate beam.
    Returns all reached Cells and best score/path; production item/trace/budget
    formatting is separate. Scores mode does NOT promise the same tie path.
    """
    _nat(max_steps, 'max_steps'); _nat(max_bridges, 'max_bridges')
    if type(frontier_cap) is not int or frontier_cap < 1:
        raise ValueError('positive frontier cap required')
    if mode not in ('scores', 'paths'):
        raise ValueError('unknown observer mode')
    frontier = (Label(entry, Q16, 0, 0, ()),)
    best: dict[Hashable, tuple[int, tuple[str, ...]]] = {}
    widths = []; generated = 0
    for depth in range(max_steps + 1):
        widths.append(len(frontier))
        for label in frontier:
            prior = best.get(label.cell)
            if prior is None or label.score > prior[0] or (label.score == prior[0] and label.path < prior[1]):
                best[label.cell] = label.score, label.path
        if depth == max_steps or not frontier:
            break
        following = []
        for label in frontier:
            for target, weight, used, kernel in targets(label.cell, label.bridges):
                if type(used) is not int or used not in (label.bridges, label.bridges + 1):
                    raise ValueError('edge must consume zero or one Bridge')
                if used > max_bridges:
                    continue
                score = RoundedWord((weight,)).apply(label.score)
                following.append(Label(target, score, used, depth+1, label.path+(kernel,)))
        generated += len(following)
        frontier = coalesce(following, mode=mode)
        if len(frontier) > frontier_cap:
            raise RuntimeError('exact frontier cap exceeded; no silent beam truncation')
    return SearchResult(best, tuple(widths), generated)
