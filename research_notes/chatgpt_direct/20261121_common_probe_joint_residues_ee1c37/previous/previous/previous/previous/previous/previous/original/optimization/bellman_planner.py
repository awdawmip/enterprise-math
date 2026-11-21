"""Exact finite-horizon minimax planning over observed request bits.

The input is a tuple of per-slot observed bit masks/values, not a request table.
Queries cost eight original commands.  Each declared round creates the selected
target, binds slot zero to that key, then releases its source.  Key-independent
business-word lengths are charged separately by the original-core harness.
"""
from __future__ import annotations

from functools import lru_cache


def observe(knowledge, slot, bit, value):
    mask, known = knowledge[slot]
    flag = 1 << bit
    if mask & flag and bool(known & flag) != bool(value):
        raise ValueError('Observation contradicts an already observed bit')
    result = list(knowledge)
    result[slot] = (mask | flag, (known & ~flag) | (int(value) << bit))
    return tuple(result)


def write(knowledge, slot, residue, width):
    result = list(knowledge)
    result[slot] = ((1 << width) - 1, residue % (1 << width))
    return tuple(result)


def compatible(pattern, residue):
    mask, value = pattern
    return residue & mask == value


def key_cost(key, width):
    return 2 * key.bit_count() + 4 * (1 - ((key >> (width - 1)) & 1))


class Planner:
    """Solve the stated finite adversarial decision tree exactly.

    An initial slot may hold any residue consistent with its observed bits.
    A creation is certified only when every slot excludes its residue.
    Future copies/drops and source conflicts are outside this round language.
    """

    def __init__(self, slots, targets):
        if slots < 1 or any(target < 0 for target in targets):
            raise ValueError('Positive slot count and nonnegative targets required')
        self.slots = slots
        self.colors = slots + 1
        self.width = (self.colors - 1).bit_length()
        self.modulus = 1 << self.width
        self.targets = tuple(targets)
        self._decisions = {}
        self.evaluated_queries = 0
        self.evaluated_creations = 0
        self.value = lru_cache(maxsize=None)(self._value)

    def _value(self, knowledge, position):
        if position == len(self.targets):
            return 0
        target = self.targets[position]
        best = None
        best_action = None
        # Creation wins exact ties: it has already obtained sufficient evidence.
        for key in range(1 + target * self.colors, 1 + (target + 1) * self.colors):
            residue = key % self.modulus
            if any(compatible(pattern, residue) for pattern in knowledge):
                continue
            self.evaluated_creations += 1
            tail = write(knowledge, 0, residue, self.width)
            score = key_cost(key, self.width) + self.value(tail, position + 1)
            if best is None or (score, key) < (best, best_action[1]):
                best, best_action = score, ('create', key)
        # Each legal query strictly increases the amount of observed information.
        for bit in reversed(range(self.width)):
            for slot in range(self.slots):
                if knowledge[slot][0] & (1 << bit):
                    continue
                self.evaluated_queries += 1
                score = 8 + max(
                    self.value(observe(knowledge, slot, bit, answer), position)
                    for answer in (0, 1)
                )
                if best is None or score < best:
                    best, best_action = score, ('read', slot, bit)
        if best is None:
            raise AssertionError('M=r+1 must leave a legal unoccupied residue')
        self._decisions[knowledge, position] = best_action
        return best

    def action(self, knowledge, position):
        if len(knowledge) != self.slots or not 0 <= position < len(self.targets):
            raise ValueError('Knowledge length or horizon position mismatch')
        full = self.modulus - 1
        if any(mask < 0 or mask > full or value < 0 or value & ~mask
               for mask, value in knowledge):
            raise ValueError('Knowledge must contain only observed in-domain bits')
        self.value(knowledge, position)
        return self._decisions[knowledge, position]

    def metrics(self):
        info = self.value.cache_info()
        return dict(states=info.currsize, cache_hits=info.hits,
                    query_actions=self.evaluated_queries,
                    creation_actions=self.evaluated_creations)


def control_replay(planner, initial_residues, initial_knowledge=None):
    """Exact control oracle; original-core execution is performed separately."""
    residues = list(initial_residues)
    knowledge = initial_knowledge or ((0, 0),) * planner.slots
    if len(residues) != planner.slots or any(
            not compatible(pattern, residue)
            for pattern, residue in zip(knowledge, residues)):
        raise ValueError('Control input is outside its declared information state')
    position = cost = queries = 0
    events = []
    while position < len(planner.targets):
        action = planner.action(knowledge, position)
        if action[0] == 'read':
            _, slot, bit = action
            answer = (residues[slot] >> bit) & 1
            knowledge = observe(knowledge, slot, bit, answer)
            cost += 8
            queries += 1
            events.append(dict(kind='read', round=position, slot=slot, bit=bit,
                               answer=answer))
        else:
            key = action[1]
            residue = key % planner.modulus
            assert residue not in residues
            cost += key_cost(key, planner.width)
            knowledge = write(knowledge, 0, residue, planner.width)
            residues[0] = residue
            events.append(dict(kind='create', round=position, target=planner.targets[position],
                               key=key, key_weight=key_cost(key, planner.width)))
            position += 1
    return dict(cost=cost, vacancy_bit_reads=queries, events=events,
                final_knowledge=knowledge, final_residues=residues)
